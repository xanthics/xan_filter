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

import math
import requests
from io import open
from datetime import datetime, time
import re
from pymongo import MongoClient
from bson import Code

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
	standard = {"exa": 80, "chaos": 1, "fuse": .333, "regal": 1, "alt": 0.1875, "alch": .333, "jew": 0.1, "gcp": 1,
				"divine": 35, "scour": 0.5, "blessed": 0.5, "vaal": 0.666, "chance": 0.10, "regret": 0.75, "chrom": 0.1875,
				"mirror": 20000, "chisel": 0.25, "silver": 0.333}
	hardcore = {"exa": 40, "chaos": 1, "fuse": .333, "regal": 1, "alt": 0.1875, "alch": .333, "jew": 0.1, "gcp": 1,
				"divine": 10, "scour": 0.5, "blessed": 0.5, "vaal": 0.666, "chance": 0.10, "regret": 0.75, "chrom": 0.1875,
				"mirror": 10000, "chisel": 0.25, "silver": 0.333}
	challenge = {"exa": 60, "chaos": 1, "fuse": .333, "regal": 1, "alt": 0.1875, "alch": .333, "jew": 0.1, "gcp": 1,
				"divine": 7, "scour": 0.5, "blessed": 0.5, "vaal": 0.666, "chance": 0.10, "regret": 0.75, "chrom": 0.1875,
				"mirror": 15000, "chisel": 0.25, "silver": 0.333}
	challengehc = {"exa": 30, "chaos": 1, "fuse": .333, "regal": 1, "alt": 0.1875, "alch": .333, "jew": 0.1, "gcp": 1,
				"divine": 6, "scour": 0.5, "blessed": 0.5, "vaal": 0.666, "chance": 0.10, "regret": 0.75, "chrom": 0.1875,
				"mirror": 8100, "chisel": 0.25, "silver": 0.333}
	if league == 'Standard':
		return cost * standard[unit]
	elif league == 'Hardcore':
		return cost * hardcore[unit]
	elif 'Hardcore' in league:
		return cost * challenge[unit]
	else:
		return cost * challengehc[unit]


#  Update chaos equiv on items based on league
def updatechaosequiv(ldb):
	for i in ldb.items.find():
		ldb.items.update({'_id': i['_id']}, {'$set': {'chaosequiv': chaosequiv(i['cost'], i['unit'], i['league'])}})


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
							elif 'stash' in ii and ('~b/o' in ii['stash'] or '~price' in ii['stash']):
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

	verygoodcard = ["Abandoned Wealth",  # 3x Exalted Orbs
					"Bowyer's Dream",  # 6l ilvl 91 Harbinger
					"Chaotic Disposition",  # 5x Chaos
					"Emperor of Purity",  # 6l ilvl 60 Holy Chainmail
					"Heterochromia",  # Two-Stone Ring
					"House of Mirrors",  # Mirror of Kalandra
					"Hunter's Reward",  # The Taming
					"Last Hope",  # Mortal Hope
					"Pride Before the Fall",  # Kaom's Heart (corrupted)
					"The Artist",  # Enhance level 4
					"The Brittle Emperor",  # Voll's Devotion (corrupted)
					"The Celestial Justicar",  # 6l Astral
					"The Cursed King",  # Rigwald's Curse
					"The Dark Mage",  # 6l ilvl 55 staff
					"The Doctor",  # Headhunter
					"The Dragon's Heart",  # Empower level 4
					"The Enlightened",  # Enlighten level 3
					"The Harvester",  # The Harvest
					"The Hunger",  # Taste of Hate
					"The Immortal",  # House of Mirrors
					"The King's Heart",  # Kaom's Heart
					"The Last One Standing",  # Atziri's Disfavour
					"The Offering",  # Shavronne's Wrapping
					"The Queen",  # Atziri's Acuity
					"The Thaumaturgist",  # Shavronne's Revelation (corrupted)
					"The Warlord",  # 6l ilvl 83 Coronal Maul
					"Time-Lost Relic",  # League Specific item
					"Wealth and Power"]  # Enlighten level 4

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

	predefinedcards = badcards + lowcards + verygoodcard

	for l in data.keys():
		if l == 'Standard':
			name = ""
		elif l == 'Hardcore':
			name = "hc"
		elif 'Hardcore' in l:
			name = "phc"
		else:
			name = "p"
		items = {'very high': [], 'high': []}

		for u in data[l][3].keys():

			if data[l][3][u] >= 50:
				items['very high'].append(u)
			elif data[l][3][u] >= 10:
				items['high'].append(u)

		with open('auto_gen\\{}uniques.py'.format(name), 'w', encoding='utf-8') as f:
			f.write(u'''{}\ndesc = "Unique"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), l)))
			for ii in sorted(items['very high']):
				f.write(u'\t"0 {0}": {{"base": "{0}", "type": "unique very high"}},\n'.format(ii))
			for ii in sorted(items['high']):
				f.write(u'\t"1 {0}": {{"base": "{0}", "type": "unique high"}},\n'.format(ii))
			f.write(u'\t"9 Other uniques": {"type": "unique normal"}\n}\n')

		items = {'high': verygoodcard[:], 'normal': [], 'low': lowcards[:]}
		for c in data[l][6]:
			if c in predefinedcards:
				pass
			elif data[l][6][c] > 10:
				items['high'].append(c)
			elif data[l][6][c] > 1.5:
				items['normal'].append(c)
			elif data[l][6][c] < 0.5:
				items['low'].append(c)
		with open('auto_gen\\{}divination.py'.format(name), 'w', encoding='utf-8') as f:
			f.write(u'''{}\ndesc = "Divination Card"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), l)))
			for ii in sorted(items['high']):
				f.write(u'\t"0 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination very high"}},\n'.format(ii))
			for ii in sorted(items['normal']):
				f.write(u'\t"1 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination high"}},\n'.format(ii))
			for ii in sorted(items['low']):
				f.write(u'\t"2 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination low"}},\n'.format(ii))
			for ii in sorted(badcards):
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

if __name__ == '__main__':
	divuniqueupdate()
