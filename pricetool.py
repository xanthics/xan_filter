#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
* Copyright (c) 2016 Jeremy Parks. All rights reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a
* copy of this software and associated documentation files (the "Software"),
* to deal in the Software without restriction, including without limitation
* the rights to use, copy, modify, merge, publish, distribute, sublicense,
* and/or sell copies of the Software, and to permit persons to whom the
* Software is furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
* DEALINGS IN THE SOFTWARE.

Author: Jeremy Parks
Purpose: Create price lists for uniques and divination cards from ggg api data
         This file creates updated priority lists for uniques and divination cards
Note: Requires Python 3.4.x
      Requires a local MongoDB 3.2.x instance
"""

from collections import defaultdict

import requests
from io import open
from datetime import datetime
import time
import re
from pymongo import MongoClient

from auto_gen import currencyrates
from auto_gen import hccurrencyrates
from auto_gen import pcurrencyrates
from auto_gen import phccurrencyrates

header = '''#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: {} UTC from "{}" data
"""
* Copyright (c) 2016 Jeremy Parks. All rights reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a
* copy of this software and associated documentation files (the "Software"),
* to deal in the Software without restriction, including without limitation
* the rights to use, copy, modify, merge, publish, distribute, sublicense,
* and/or sell copies of the Software, and to permit persons to whom the
* Software is furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
* DEALINGS IN THE SOFTWARE.

Author: Jeremy Parks
Purpose: Create an item filter based on config files
Note: Requires Python 3.4.x
"""
'''


#  Calculate chaos equiv based on league
def chaosequiv(cost, unit, league):
	if league == 'Standard':
		return cost * currencyrates.items[unit]
	elif league == 'Hardcore':
		return cost * hccurrencyrates.items[unit]
	elif 'Hardcore' in league:
		return cost * pcurrencyrates.items[unit]
	else:
		return cost * phccurrencyrates.items[unit]


# Update chaos equiv on items based on league
def updatechaosequiv(ldb):
	print('Starting update of existing data')
	count = ldb.items.count()
	steps = 100
	thresholds = [i*count//steps for i in range(steps)]
	for c, i in enumerate(ldb.items.find()):
		if c in thresholds:
			print('{:.2f}% done'.format(c/count*100))
		ldb.items.update({'_id': i['_id']}, {'$set': {'chaosequiv': chaosequiv(i['cost'], i['unit'], i['league'])}})
	print('Finished updating existing data')


# Add current data to the ldb
def adddata(nextchange, remove, add, ldb):
	print("Adding {} items.  Updating {} tabs.".format(len(add), len(remove)))

	# Remove items that have a stash tab that matches this update
	if remove:
		ldb.items.delete_many({'tabid': {'$in': remove}})

	# Insert our new data
	if add:
		ldb.items.insert_many(add)

	# Update Next ID now that we are done with this one
	ldb.key.update_one({}, {'$set': {'next': nextchange}}, True)


#  Retrieve Stash Tab API data from GGG
def get_stashes(ldb, start=None):
	if not start:
		if 'key' in ldb.collection_names():
			start = ldb.key.find_one()['next']

	if start:
		url = 'https://www.pathofexile.com/api/public-stash-tabs?id={}'.format(start)
	else:
		url = 'https://www.pathofexile.com/api/public-stash-tabs'

	print("Starting {}".format(url))
	req = requests.get(url)

	data = req.json(encoding='utf-8')

	nextchange = ""
	remove = []
	add = []
	keys = {}
	for i in data:
		if 'stashes' == i:
			for ii in data[i]:
				remove.append(ii['id'])
				if 'items' in ii and ii['items']:
					for iii in ii['items']:
						if iii['frameType'] in [3, 6]:
							note = ""
							if 'note' in iii and ('~b/o' in iii['note'] or '~price' in iii['note']):
								note = iii['note']
							elif 'stash' in ii and ii['stash'] and ('~b/o' in ii['stash'] or '~price' in ii['stash']):
								note = ii['stash']
								keys[ii['stash']] = True
							if note:
								price = re.search(r'(~b/o|~price) (-?\d*(\.\d+)?) (silver|vaal|jew|chrom|alt|jewel|chance|chisel|cartographer|fuse|fusing|alch|scour|blessed|chaos|regret|regal|gcp|gemcutter|divine|exalted|exa|ex|mirror)', note.lower())
								if price and price.group(2):
									if float(price.group(2)) >= 0:
										unit = price.group(4)
										if unit in ['exalted', 'ex']:
											unit = 'exa'
										elif unit in ['fusing']:
											unit = 'fuse'
										add.append({'type': iii['frameType'], 'league': iii['league'], 'base': iii['typeLine'].replace("Superior ", ""), 'cost': float(price.group(2)), 'unit': unit, 'tabid': ii['id'], 'ids': iii['id'], 'chaosequiv': chaosequiv(float(price.group(2)), unit, iii['league'])})

								else:
									with open('erroritems.txt', 'a', encoding='utf-8') as f:
										f.write(u"{} *** {}\n".format(note, {'type': iii['frameType'], 'league': iii['league'], 'base': iii['typeLine'], 'tabid': ii['id'], 'ids': iii['id']}))
		elif 'next_change_id' == i:
			nextchange = data[i]
		else:
			raise ValueError("Invalid JSON data returned: {}".format(i))

	adddata(nextchange, remove, add, ldb)

	# Stop updating if we get less than 50 new tabs as we don't need the absolute most current data
	if len(remove) > 50:
		return nextchange
	else:
		return start


def gen_lists(ldb):
	league = ldb.items.distinct('league')

	res = ldb.items.aggregate([
		{'$group': {
			'_id': {
				'league': '$league',
				'base': '$base',
				'type': '$type'
			},
			'value': {'$push': '$chaosequiv'}
		}},
		{'$unwind': '$value'},
		{'$sort': {'value': 1}},
		{'$group': {'_id': '$_id', 'value': {'$push': '$value'}}},
		{'$project': {
			'_id': 1,
			'value': {'$arrayElemAt': ['$value', {'$floor': {'$multiply': [0.25, {'$size': '$value'}]}}]}
		}}
	], allowDiskUse=True)

	data = {league[0]: defaultdict(dict), league[1]: defaultdict(dict), league[2]: defaultdict(dict), league[3]: defaultdict(dict)}

	for i in res:
		data[i['_id']['league']][i['_id']['type']][i['_id']['base']] = i['value']

	# If Div card doesn't exist in league market copy from Standard league
	# This is mostly for fresh leagues
	other = league[:]
	other.remove('Standard')
	for ind in other:
		for card in data['Standard'][6]:
			if card not in data[ind][6]:
				print("{}: {}".format(ind, card))
				data[ind][6][card] = data['Standard'][6][card]
	# Same thing as cards but for uniques
	for unique in data['Standard'][3]:
		for ind in other:
			if unique not in data[ind][3]:
				data[ind][3][unique] = data['Standard'][3][unique]

	substringcards = find_substrings(ldb)

	# Cards that are so rare they may not even be on Standard
	verygoodcards = ['House of Mirrors']

	# Cards that will never be displayed
	badcards = ["The Carrion Crow",
				"The King's Blade",
				"The Inoculated",
				"Turn the Other Cheek"]

	# Cards that won't make a drop noise
	lowcards = ["Thunderous Skies",
				"The Rabid Rhoa",
				"The Surgeon",
				"The Twins",
				"The Scholar",
				"Destined to Crumble"]

	predefinedcards = badcards + lowcards + substringcards + verygoodcards

	for l in data.keys():
		bcards = badcards[:]
		if l == 'Standard':
			name = ""
		elif l == 'Hardcore':
			name = "hc"
		elif 'Hardcore' in l:
			name = "phc"
		else:
			name = "p"
		items = {'very high': [], 'high': [], 'low': []}

		for u in data[l][3].keys():

			if data[l][3][u] >= chaosequiv(1, 'exa', l):
				items['very high'].append(u)
			elif data[l][3][u] >= chaosequiv(.2, 'exa', l):
				items['high'].append(u)
			elif data[l][3][u] < 0.5:
				items['low'].append(u)

		with open('auto_gen\\{}uniques.py'.format(name), 'w', encoding='utf-8') as f:
			f.write(u'''{}\ndesc = "Unique"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), l)))
			for ii in sorted(items['very high']):
				f.write(u'\t"0 {0}": {{"base": "{0}", "type": "unique very high"}},\n'.format(ii))
			for ii in sorted(items['high']):
				f.write(u'\t"1 {0}": {{"base": "{0}", "type": "unique high"}},\n'.format(ii))
			for ii in sorted(items['low']):
				f.write(u'\t"7 {0}": {{"base": "{0}", "type": "unique low"}},\n'.format(ii))
			f.write(u'\t"9 Other uniques": {"type": "unique normal"}\n}\n')

		items = {'high': verygoodcards[:], 'normal': [], 'low': lowcards[:]}
		for card in substringcards:
			if card in items['low']:
				items['low'].remove(card)
		for c in data[l][6]:
			if c in predefinedcards:
				pass
			elif data[l][6][c] > chaosequiv(.2, 'exa', l):
				items['high'].append(c)
			elif data[l][6][c] > chaosequiv(.035, 'exa', l):
				items['normal'].append(c)
			elif data[l][6][c] < 0.5:
				items['low'].append(c)
		with open('auto_gen\\{}divination.py'.format(name), 'w', encoding='utf-8') as f:
			f.write(u'''{}\ndesc = "Divination Card"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), l)))
			for c, ii in enumerate(substringcards):
				if ii in bcards:
					lvl = 'hide'
					bcards.remove(ii)
				elif data[l][6][ii] > chaosequiv(.2, 'exa', l):
					lvl = 'divination very high'
				elif data[l][6][ii] > chaosequiv(.035, 'exa', l):
					lvl = 'divination high'
				elif data[l][6][ii] < 0.5:
					lvl = 'divination low'
				else:
					lvl = 'divination normal'
				f.write(u'\t"{0:03d} {1}": {{"base": "{1}", "class": "Divination Card", "type": "{2}"}},\n'.format(c, ii, lvl))
			for ii in sorted(items['high']):
				f.write(u'\t"1 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination very high"}},\n'.format(ii))
			for ii in sorted(items['normal']):
				f.write(u'\t"2 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination high"}},\n'.format(ii))
			for ii in sorted(items['low']):
				f.write(u'\t"3 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination low"}},\n'.format(ii))
			for ii in sorted(bcards):
				f.write(u'\t"7 {0}": {{"base": "{0}", "class": "Divination Card", "type": "hide"}},\n'.format(ii))
			f.write(u'\t"9 Other uniques": {"class": "Divination Card", "type": "divination normal"}\n}\n')


def divuniqueupdate():
	# Make sure error file exists for invalid tab data
	from os.path import exists
	if not exists('erroritems.txt'):
		open('erroritems.txt', 'w')

	with MongoClient() as client:
		ldb = client.stashdata

		nc = None
		oldnc = nc

		while True:
			try:
				nc = get_stashes(ldb, nc)
				if oldnc == nc:
					break
				oldnc = nc
			except ValueError as ve:
				print("ValueError: {}".format(ve))
				break
			except TypeError as te:
				print("TypeError: {}".format(te))
				time.sleep(120)

		gen_lists(ldb)


# Find all divination cards that have cards which are substrings
def find_substrings(ldb):
	cardnames = ldb.items.distinct('base', {'type': 6})

	substringmatches = {}
	for index in range(len(cardnames) - 1):
		for card in cardnames[index + 1:]:
			if cardnames[index] in card or card in cardnames[index]:
				if card in cardnames[index]:
					sub, full = card, cardnames[index]
				else:
					sub, full = cardnames[index], card
				if sub not in substringmatches:
					substringmatches[sub] = [full]
				else:
					substringmatches[sub].append(full)

	badcards = [badcards for substring in substringmatches for badcards in substringmatches[substring]]
	# distinct values by converting to a set
	# reverse sort in case any names such as "a", "ab", "abc" exist due to how Python sorts
	return sorted(set(badcards), reverse=True)


# scrape poe.trade for currency exchange rates
def poetrade_getcurrencyrates():
	currencies = {"exa": 6, "fuse": 2, "regal": 14, "alt": 1, "alch": 3, "jew": 8, "gcp": 5,
				  "divine": 15, "scour": 11, "blessed": 12, "vaal": 16, "chance": 9, "regret": 13, "chrom": 7,
				  "chisel": 10, "silver": 35}

	chaos = 4

	defaults = {"exa": 60.0, "chaos": 1.0, "fuse": 0.5, "regal": 1, "alt": 1/16, "alch": 1/3, "jew": 1/8, "gcp": 1,
				"divine": 15.0, "scour": 0.5, "blessed": 0.5, "vaal": 1, "chance": 1/14, "regret": 1.0, "chrom": 1/15,
				"mirror": 20000.0, "chisel": 0.25, "silver": 0.333}

	with MongoClient() as client:
		ldb = client.stashdata
		league = ldb.items.distinct('league')

		for l in league:
			if l == 'Standard':
				name = ""
			elif l == 'Hardcore':
				name = "hc"
			elif 'Hardcore' in l:
				name = "phc"
			else:
				name = "p"

			# Populate ratios with amount currency is being bought for chaos
			ratios = [[] for i in range(max(currencies.values()) + 1)]
			url = "http://currency.poe.trade/search?league={}&online=x&want={}&have={}".format(l, chaos, '-'.join([str(currencies[d]) for d in currencies]))
			req = requests.get(url).text
			for i in (req.split('\n')):
				if 'data-sellcurrency="4"' in i:
					crate = float(re.search(r'data-sellvalue="(-?\d*(\.\d+)?)"', i.lower()).group(1))
					rtype = int(re.search(r'data-buycurrency="(-?\d*(\.\d+)?)"', i.lower()).group(1))
					rrate = float(re.search(r'data-buyvalue="(-?\d*(\.\d+)?)"', i.lower()).group(1))
					ratios[rtype].append(crate / rrate)

			# Populate ratios with amount of currency you can buy for a chaos
			url = "http://currency.poe.trade/search?league={}&online=x&want={}&have={}".format(l, '-'.join([str(currencies[d]) for d in currencies]), chaos)
			req = requests.get(url).text
			for i in (req.split('\n')):
				if 'data-buycurrency="4"' in i:
					crate = float(re.search(r'data-buyvalue="(-?\d*(\.\d+)?)"', i.lower()).group(1))
					rtype = int(re.search(r'data-sellcurrency="(-?\d*(\.\d+)?)"', i.lower()).group(1))
					rrate = float(re.search(r'data-sellvalue="(-?\d*(\.\d+)?)"', i.lower()).group(1))
					ratios[rtype].append(crate / rrate)

			with open('auto_gen\\{}currencyrates.py'.format(name), 'w', encoding='utf-8') as f:
				f.write(u'''{}\ndesc = "Currency Rates"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), l)))
				for cur in sorted(defaults.keys()):
					if cur in currencies and ratios[currencies[cur]] and len(ratios[currencies[cur]]) > 5:
						ratios[currencies[cur]].sort()
						f.write(u'\t"{}": {},\n'.format(cur, ratios[currencies[cur]][(len(ratios[currencies[cur]]) * 3) // 4]))
					else:
						if cur in currencies:
							# print the currencies that didn't have enough data
							print(cur, l, ratios[currencies[cur]], len(ratios[currencies[cur]]))
						f.write(u'\t"{}": {},\n'.format(cur, defaults[cur]))
				f.write(u'}\n')

		updatechaosequiv(ldb)
		gen_lists(ldb)

if __name__ == '__main__':
	# poetrade_getcurrencyrates()
	# divuniqueupdate()

	if True:
		with MongoClient() as client:
			ldb = client.stashdata
			gen_lists(ldb)

