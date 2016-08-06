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
Purpose: Create price lists for uniques and divination cards from exiletools api data
         This file creates updated priority lists for uniques and divination cards
Note: Requires Python 3.4.x
"""

import requests
from io import open
from api_key import user, password
from datetime import datetime

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


def gen_lists():
	league1 = "Prophecy"
	league2 = "Hardcore Prophecy"
	league3 = "Standard"
	league4 = "Hardcore"

	league1queryunique = '''{{"query":{{"bool":{{"must":[{{"term":{{"attributes.league":{{"value":"{0}"}}}}}},{{"term":{{"attributes.rarity":{{"value":"Unique"}}}}}},{{"term":{{"shop.hasPrice":{{"value":"true"}}}}}}]}}}},"aggs":{{"{0} Uniques":{{"terms":{{"field":"info.typeLine","size":1000,"order":{{"avgPrice[50.0]":"desc"}}}},"aggs":{{"avgPrice":{{"percentiles":{{"field":"shop.chaosEquiv","percents":[50]}}}}}}}}}},size:0}}'''.format(league1)
	league1querycard = '''{{"query": {{"bool": {{"must": [{{"term": {{"attributes.league": {{"value": "{0}"}}}}}},{{"term": {{"attributes.baseItemType": {{"value": "Card"}}}}}},{{"term": {{"shop.hasPrice": {{"value": "true"}}}}}}]}}}},"aggs": {{"{0} Cards": {{"terms": {{"field": "info.typeLine","size": 1000,"order" : {{"avgPrice[50.0]" : "desc"}}}},"aggs": {{"avgPrice": {{"percentiles": {{"field": "shop.chaosEquiv","percents": [50]}}}}}}}}}},size:0}}'''.format(league1)

	league2queryunique = '''{{"query":{{"bool":{{"must":[{{"term":{{"attributes.league":{{"value":"{0}"}}}}}},{{"term":{{"attributes.rarity":{{"value":"Unique"}}}}}},{{"term":{{"shop.hasPrice":{{"value":"true"}}}}}}]}}}},"aggs":{{"{0} Uniques":{{"terms":{{"field":"info.typeLine","size":1000,"order":{{"avgPrice[50.0]":"desc"}}}},"aggs":{{"avgPrice":{{"percentiles":{{"field":"shop.chaosEquiv","percents":[50]}}}}}}}}}},size:0}}'''.format(league2)
	league2querycard = '''{{"query": {{"bool": {{"must": [{{"term": {{"attributes.league": {{"value": "{0}"}}}}}},{{"term": {{"attributes.baseItemType": {{"value": "Card"}}}}}},{{"term": {{"shop.hasPrice": {{"value": "true"}}}}}}]}}}},"aggs": {{"{0} Cards": {{"terms": {{"field": "info.typeLine","size": 1000,"order" : {{"avgPrice[50.0]" : "desc"}}}},"aggs": {{"avgPrice": {{"percentiles": {{"field": "shop.chaosEquiv","percents": [50]}}}}}}}}}},size:0}}'''.format(league2)

	league3queryunique = '''{{"query":{{"bool":{{"must":[{{"term":{{"attributes.league":{{"value":"{0}"}}}}}},{{"term":{{"attributes.rarity":{{"value":"Unique"}}}}}},{{"term":{{"shop.hasPrice":{{"value":"true"}}}}}}]}}}},"aggs":{{"{0} Uniques":{{"terms":{{"field":"info.typeLine","size":1000,"order":{{"avgPrice[50.0]":"desc"}}}},"aggs":{{"avgPrice":{{"percentiles":{{"field":"shop.chaosEquiv","percents":[50]}}}}}}}}}},size:0}}'''.format(league3)
	league3querycard = '''{{"query": {{"bool": {{"must": [{{"term": {{"attributes.league": {{"value": "{0}"}}}}}},{{"term": {{"attributes.baseItemType": {{"value": "Card"}}}}}},{{"term": {{"shop.hasPrice": {{"value": "true"}}}}}}]}}}},"aggs": {{"{0} Cards": {{"terms": {{"field": "info.typeLine","size": 1000,"order" : {{"avgPrice[50.0]" : "desc"}}}},"aggs": {{"avgPrice": {{"percentiles": {{"field": "shop.chaosEquiv","percents": [50]}}}}}}}}}},size:0}}'''.format(league3)

	league4queryunique = '''{{"query":{{"bool":{{"must":[{{"term":{{"attributes.league":{{"value":"{0}"}}}}}},{{"term":{{"attributes.rarity":{{"value":"Unique"}}}}}},{{"term":{{"shop.hasPrice":{{"value":"true"}}}}}}]}}}},"aggs":{{"{0} Uniques":{{"terms":{{"field":"info.typeLine","size":1000,"order":{{"avgPrice[50.0]":"desc"}}}},"aggs":{{"avgPrice":{{"percentiles":{{"field":"shop.chaosEquiv","percents":[50]}}}}}}}}}},size:0}}'''.format(league4)
	league4querycard = '''{{"query": {{"bool": {{"must": [{{"term": {{"attributes.league": {{"value": "{0}"}}}}}},{{"term": {{"attributes.baseItemType": {{"value": "Card"}}}}}},{{"term": {{"shop.hasPrice": {{"value": "true"}}}}}}]}}}},"aggs": {{"{0} Cards": {{"terms": {{"field": "info.typeLine","size": 1000,"order" : {{"avgPrice[50.0]" : "desc"}}}},"aggs": {{"avgPrice": {{"percentiles": {{"field": "shop.chaosEquiv","percents": [50]}}}}}}}}}},size:0}}'''.format(league4)

	url = 'http://api.exiletools.com/index/_msearch?pretty'

	req = requests.get(url, data="{{}}\n{}\n{{}}\n{}\n{{}}\n{}\n{{}}\n{}\n{{}}\n{}\n{{}}\n{}\n{{}}\n{}\n{{}}\n{}\n".format(league1queryunique, league1querycard, league2queryunique, league2querycard, league3queryunique, league3querycard, league4queryunique, league4querycard), auth=(user, password))

	data = req.json(encoding='utf-8')

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

	gen_lists()
