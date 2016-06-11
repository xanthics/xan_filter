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
from codecs import open
from api_key import user, password
from datetime import datetime

header = '''#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: {} PST from "{}" data
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

def gen_uniques(league):
	query = '''
	{{
	  "query": {{"bool": {{"must": [{{"term": {{"attributes.league": {{"value": "{}"}}}}}},
								  {{"term": {{"attributes.rarity": {{"value": "Unique"}}}}}},
								  {{"term": {{"shop.hasPrice": {{"value": "true"}}}}}}
								 ]}}}},
	  "aggs": {{"uniqueNames": {{"terms": {{"field": "info.typeLine","size": 1000,"order" : {{"avgPrice[50.0]" : "desc"}}}},
										 "aggs": {{"avgPrice": {{"percentiles": {{"field": "shop.chaosEquiv","percents": [50]}}}}}}}}
			  }},
	  size:0
	}}
	'''.format(league)

	url = 'http://api.exiletools.com/index/_search?pretty'

	req = requests.get(url, headers={'Connection': 'close'}, data=query, auth=(user, password))

	data = req.json(encoding='utf-8')

	if 'aggregations' in data and 'uniqueNames' in data['aggregations'] and 'buckets' in data['aggregations']['uniqueNames'] and data['aggregations']['uniqueNames']['buckets']:
		items = {'very high': [], 'high': []}

		for i in data['aggregations']['uniqueNames']['buckets']:
			if i['avgPrice']['values']['50.0'] >= 50:
				items['very high'].append(i[u'key'])
			elif i['avgPrice']['values']['50.0'] >= 10:
				items['high'].append(i[u'key'])

		with open('autogen\\uniques.py', 'w', 'utf-8') as f:
			f.write(u'''{}\ndesc = "Unique"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),league)))
			for ii in items['very high']:
				f.write(u'\t"0 {0}": {{"base": "{0}", "type": "unique very high"}},\n'.format(ii))
			for ii in items['high']:
				f.write(u'\t"1 {0}": {{"base": "{0}", "type": "unique high"}},\n'.format(ii))
			f.write(u'\t"9 Other uniques": {"type": "unique normal"}\n}\n')
	else:
		print(req.text)


def gen_divination(league):
	query = '''
	{{
	  "query": {{"bool": {{"must": [{{"term": {{"attributes.league": {{"value": "{}"}}}}}},
								  {{"term": {{"attributes.baseItemType": {{"value": "Card"}}}}}},
								  {{"term": {{"shop.hasPrice": {{"value": "true"}}}}}}
								 ]}}}},
	  "aggs": {{"CardNames": {{"terms": {{"field": "info.typeLine","size": 1000,"order" : {{"avgPrice[50.0]" : "desc"}}}},
					  			       "aggs": {{"avgPrice": {{"percentiles": {{"field": "shop.chaosEquiv","percents": [50]}}}}}}}}
			  }},
	  size:0
	}}
	'''.format(league)

	url = 'http://api.exiletools.com/index/_search?pretty'

	req = requests.get(url, headers={'Connection': 'close'}, data=query, auth=(user, password))

	data = req.json(encoding='utf-8')

	badcards = ["A Mother's Parting Gift",
				"The Carrion Crow",
				"The Rabid Rhoa",
				"The King's Blade",
				"The Inoculated",
				"Turn the Other Cheek"]

	lowcards = ["Thunderous Skies",
				"The Scholar"]

	if 'aggregations' in data and 'CardNames' in data['aggregations'] and 'buckets' in data['aggregations']['CardNames'] and data['aggregations']['CardNames']['buckets']:
		items = {'high': [], 'normal': [], 'low': []}

		for i in data['aggregations']['CardNames']['buckets']:
			if i['key'] in badcards or i['key'] in lowcards:
				pass
			elif i['avgPrice']['values']['50.0'] >= 6:
				items['high'].append(i[u'key'])
			elif i['avgPrice']['values']['50.0'] >= 1:
				items['normal'].append(i[u'key'])

		with open('autogen\\divination.py', 'w', 'utf-8') as f:
			f.write(u'''{}\ndesc = "Divination Card"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),league)))
			for ii in items['high']:
				f.write(u'\t"0 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination very high"}},\n'.format(ii))
			for ii in items['normal']:
				f.write(u'\t"1 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination high"}},\n'.format(ii))
			for ii in lowcards:
				f.write(u'\t"2 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination low"}},\n'.format(ii))
			for ii in badcards:
				f.write(u'\t"7 {0}": {{"base": "{0}", "class": "Divination Card", "type": "hide"}},\n'.format(ii))
			f.write(u'\t"9 Other uniques": {"class": "Divination Card", "type": "divination normal"}\n}\n')
	else:
		print(req.text)


if __name__ == '__main__':
	league = "Prophecy"
	#league = "Hardcore Prophecy"

	#league = "Standard"
	#league = "Hardcore"

	# Change which gen is commented out to generate that list.  Due to session caching, they can't be ran back to back
	gen_uniques(league)
	#gen_divination(league)