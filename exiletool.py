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
      Database opens a new connection and writes after each page is retrieved as
      TinyDB documentation doesn't indicated when the data is written to disk
"""

import requests
from io import open
from datetime import datetime
import re
from pymongo import MongoClient

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


#  Print all leagues in database
def leagues(ldb):
	#  Print Leagues
	league = ldb.items.distinct('league')
	print(league)


# Add current data to the ldb
def adddata(nextchange, remove, add, ldb):
	print("Adding {} items.  Updating {} tabs.".format(len(add), len(remove)))
	# Update Next ID
	ldb.key.update_one({}, {'$set': {'next': nextchange}}, True)

	# Remove items that have a stash tab that matches this update
	for i in remove:
		ldb.items.delete_many({'tabid': i})

	# Insert our new data
	ldb.items.insert_many(add)


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
								if ii['id'] not in remove:
									remove.append(ii['id'])
								price = re.match(r'(~b/o|~price) (-?\d*(\.\d+)?) (vaal|jew|chrom|alt|jewel|chance|chisel|cartographer|fuse|fusing|alch|scour|blessed|chaos|regret|regal|gcp|gemcutter|divine|exalted|exa|ex|mirror)', note.lower())
								if price:
									if float(price.group(2)) > 0:
										unit = price.group(4)
										if unit in ['exalted', 'exa', 'ex']:
											unit = 'exa'
										elif unit in ['fuse', 'fusing']:
											unit = 'fuse'
										add.append({'type': iii['frameType'], 'league': iii['league'], 'base': iii['typeLine'], 'cost': price.group(2), 'unit': unit, 'tabid': ii['id'], 'ids': iii['id']})
								else:
									with open('database/erroritems.txt', 'a') as f:
										f.write("{} *** {}\n".format(note, {'type': iii['frameType'], 'league': iii['league'], 'base': iii['typeLine'], 'tabid': ii['id'], 'ids': iii['id']}))
		else:
			nextchange = data[i]

	adddata(nextchange, remove, add, ldb)
	return nextchange


def gen_lists():
	league1 = "Essence"
	league2 = "Hardcore Essence"
	league3 = "Standard"
	league4 = "Hardcore"

	#  TODO: extract price data from database
	data = []
	#  TODO: end

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

#	cardtracker = {}

	if 'responses' in data:
		for l in data['responses']:
			curkey = list(l['aggregations'].keys())[0]
			if "Uniques" in curkey:
				name = ""
				if curkey == "{} Uniques".format(league1):
					name = "p"
				elif curkey == "{} Uniques".format(league2):
					name = "phc"
				elif curkey == "{} Uniques".format(league3):
					name = ""
				elif curkey == "{} Uniques".format(league4):
					name = "hc"
				items = {'very high': [], 'high': []}

				for i in l['aggregations'][curkey]['buckets']:
					if i['avgPrice']['values']['50.0'] >= 50:
						items['very high'].append(i[u'key'])
					elif i['avgPrice']['values']['50.0'] >= 10:
						items['high'].append(i[u'key'])

				with open('auto_gen\\{}uniques.py'.format(name), 'w', encoding='utf-8') as f:
					f.write(u'''{}\ndesc = "Unique"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), curkey)))
					for ii in sorted(items['very high']):
						f.write(u'\t"0 {0}": {{"base": "{0}", "type": "unique very high"}},\n'.format(ii))
					for ii in sorted(items['high']):
						f.write(u'\t"1 {0}": {{"base": "{0}", "type": "unique high"}},\n'.format(ii))
					f.write(u'\t"9 Other uniques": {"type": "unique normal"}\n}\n')

			elif "Cards" in curkey:
				name = ""
				if curkey == "{} Cards".format(league1):
					name = "p"
				elif curkey == "{} Cards".format(league2):
					name = "phc"
				elif curkey == "{} Cards".format(league3):
					name = ""
				elif curkey == "{} Cards".format(league4):
					name = "hc"
				items = {'high': verygoodcard[:], 'normal': [], 'low': lowcards[:]}
				for i in l['aggregations'][curkey]['buckets']:
					if i['key'] in predefinedcards:
						pass
					elif i['avgPrice']['values']['50.0'] > 6:
#						if i[u'key'] in cardtracker:
#							cardtracker[i[u'key']].append("vh {}".format(name))
#						else:
#							cardtracker[i[u'key']] = ["vh {}".format(name)]
						items['high'].append(i[u'key'])
					elif i['avgPrice']['values']['50.0'] > 1:
#						if i[u'key'] in cardtracker:
#							cardtracker[i[u'key']].append("h {}".format(name))
#						else:
#							cardtracker[i[u'key']] = ["h {}".format(name)]
						items['normal'].append(i[u'key'])
				with open('auto_gen\\{}divination.py'.format(name), 'w', encoding='utf-8') as f:
					f.write(u'''{}\ndesc = "Divination Card"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'),curkey)))
					for ii in sorted(items['high']):
						f.write(u'\t"0 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination very high"}},\n'.format(ii))
					for ii in sorted(items['normal']):
						f.write(u'\t"1 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination high"}},\n'.format(ii))
					for ii in sorted(items['low']):
						f.write(u'\t"2 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination low"}},\n'.format(ii))
					for ii in sorted(badcards):
						f.write(u'\t"7 {0}": {{"base": "{0}", "class": "Divination Card", "type": "hide"}},\n'.format(ii))
					f.write(u'\t"9 Other uniques": {"class": "Divination Card", "type": "divination normal"}\n}\n')

#	for card in sorted(cardtracker.keys()):
#		print("{}: {}, {}".format(card, len(cardtracker[card]), cardtracker[card]))


if __name__ == '__main__':
	with MongoClient() as client:
		#client.drop_database('stashdata')
		ldb = client.stashdata
		nc = get_stashes(ldb)

		oldnc = nc
		while True:
			nc = get_stashes(ldb, nc)
			if oldnc == nc:
				break
			oldnc = nc

		leagues(ldb)

		gen_lists()
