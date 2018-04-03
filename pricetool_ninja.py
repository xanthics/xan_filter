#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher

import os
import requests
from collections import defaultdict
from datetime import datetime

header = '''#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: {} UTC from "{}" data
'''


# Helper function to convert a league name to a file prefix
def convertname(l):
	if l == 'Standard':
		return ""
	elif l == 'Hardcore':
		return "hc"
	elif 'tmphardcore' in l:
		return "thc"
	else:
		return "t"


# Convert a currency shorthand to full name.  returns a string
def currencyclassify(cur, val, exa):

	# list of currency to always give a border to
	ah = ["Splinter of Chayula", "Splinter of Xoph", "Splinter of Uul-Netol", "Splinter of Tul", "Splinter of Esh"
	      "Chromatic Orb", "Perandus Coin"]

	if cur in ah and val <= 1 / 8:
		tier = 'show normal'
	elif val >= exa * .5:
		tier = 'currency extremely high'
	elif val >= 3:
		tier = 'currency very high'
	elif val >= 0.95:
		tier = 'currency high'
	elif val >= 1 / 8:
		tier = 'currency normal'
	elif val >= 1 / 20:
		tier = 'currency low'
	else:
	#elif val >= 1 / 200:
		tier = 'currency very low'
	#else:
	#	tier = 'hide'
	return "0 {0}\": {{\"base\": \"{0}\", \"class\": \"Currency\", \"type\": \"{1}\"}}".format(cur, tier)


# given a league grouped list of currency determine all unique entries and then output for each league
def gen_currency(currency_list):
	defaults = {"Exalted Orb": 45.0, "Chaos Orb": 1.0, "Orb of Fusing": 0.5, "Regal Orb": 1, "Orb of Alteration": 1 / 16, "Orb of Alchemy": 1 / 3, "Jeweller's Orb": 1 / 8, "Gemcutter's Prism": 1,
	            "Divine Orb": 15.0, "Orb of Scouring": 0.5, "Blessed Orb": 0.5, "Vaal Orb": 1, "Orb of Chance": 1 / 8, "Orb of Regret": 1.0, "Chromatic Orb": 1 / 15, "Cartographer's Chisel": 0.25,
	            "Silver Coin": 1 / 3, "Glassblower's Bauble": 1 / 8, "Orb of Augmentation": 1 / 32, "Orb of Transmutation": 1 / 64, "Perandus Coin": 1 / 45, "Apprentice Cartographer's Sextant": .5,
	            "Journeyman Cartographer's Sextant": 2, "Master Cartographer's Sextant": 5, 'Eternal Orb': 300, "Blessing of Chayula": 300, "Blessing of Esh": 30, "Blessing of Uul-Netol": 10,
	            "Blessing of Tul": 2, "Blessing of Xoph": 3, "Splinter of Chayula": 3, "Splinter of Xoph": 0.333, "Splinter of Uul-Netol": 0.5, "Splinter of Tul": 1 / 5, "Splinter of Esh": 0.333,
	            "Blacksmith's Whetstone": 1 / 30, "Portal Scroll": 1 / 100, "Armourer's Scrap": 1 / 50, "Mirror Shard": 52, "Ancient Orb": 7, "Harbinger's Orb": 4, "Orb of Annulment": 3, "Exalted Shard": 7 / 3,
	            "Orb of Horizons": 2 / 3, "Engineer's Orb": 0.5, "Annulment Shard": 0.5, "Orb of Binding": 1 / 4, "Scroll of Wisdom": 1 / 100, 'Chaos Shard': 1 / 20}

	shards = {'Binding Shard': 'Orb of Binding', 'Horizon Shard': 'Orb of Horizons', 'Harbinger\'s Shard': 'Harbinger\'s Orb', 'Engineer\'s Shard': 'Engineer\'s Orb', 'Ancient Shard': 'Ancient Orb',
	          'Regal Shard': 'Regal Orb', 'Alchemy Shard': 'Orb of Alchemy', 'Alteration Shard': 'Orb of Alteration', 'Transmutation Shard': 'Orb of Transmutation', 'Scroll Fragment': 'Scroll of Wisdom'}

	c_list = list(defaults.keys()) + list(shards.keys())
	unknown = defaultdict(list)
	for l in currency_list:
		curval = '''{}\ndesc = "Currency Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), l))

		if 'Exalted Orb' not in currency_list[l]:
			currency_list[l]['Exalted Orb'] = defaults['Exalted Orb']
		for cur in sorted(c_list):
			if cur in currency_list[l]:
				# print(cur, currency_list[l][cur], l)
				retstr = currencyclassify(cur, currency_list[l][cur], currency_list[l]['Exalted Orb'])
				curval += '\t"{},\n'.format(retstr)
			else:
				if cur in shards and shards[cur] not in currency_list[l]:
					retstr = currencyclassify(cur, defaults[shards[cur]] / 10, currency_list[l]['Exalted Orb'])
				elif cur in shards and shards[cur] in currency_list[l]:
					retstr = currencyclassify(cur, currency_list[l][shards[cur]] / 10, currency_list[l]['Exalted Orb'])
				else:
					retstr = currencyclassify(cur, defaults[cur], currency_list[l]['Exalted Orb'])
				curval += '\t"{},\n'.format(retstr)
				print('No data for {} in {}.  Using default,'.format(cur, l))
		curval += u'}\n'

		name = convertname(l)

		with open('auto_gen\\{}currency.py'.format(name), 'w', encoding='utf-8') as f:
			f.write(curval)

		for v in currency_list[l].keys():
			if v not in defaults:
				unknown[v].append(currency_list[l][v])

	for u in unknown:
		#print("Unknown currency: {}".format(u))
		print('"{}": 0,'.format(u), end=' ')


# Convert a essence value to string.  returns a string
def essenceclassify(cur, val):
	if val >= 15:
		tier = 'currency very high'
	elif val >= 9:
		tier = 'currency high'
	elif val >= 1.5:
		tier = 'currency normal'
	else:
		return ''
		# tier = 'currency low'

	return "0 {0}\": {{\"base\": \"{0}\", \"class\": \"Currency\", \"type\": \"{1}\"}}".format(cur, tier)


# given a league grouped list of essences determine all unique entries and then output for each league
def gen_essence(essence_list):
	for l in essence_list:
		curval = '''{}\ndesc = "Essence Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), l))

		for cur in sorted(essence_list[l].keys()):
			retstr = essenceclassify(cur, essence_list[l][cur])
			if retstr:
				curval += '\t"{},\n'.format(retstr)

		curval += '\t"7 Essence default": {"base": "Essence", "class": "Currency", "type": "currency low"}'
		curval += u'}\n'

		name = convertname(l)

		with open('auto_gen\\{}essence.py'.format(name), 'w', encoding='utf-8') as f:
			f.write(curval)




# Find all divination cards that have cards which are substrings
def find_substrings(div_defaults):
	cardnames = list(div_defaults.keys())

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


# Generate a list of all known cards with their values for setting default values
# Primarily used for new leagues
def gen_div_default(div_list):
	cards = defaultdict(list)
	for l in div_list:
		for c in div_list[l]:
			cards[c].append(div_list[l][c])

	for c in cards:
		cards[c] = sum(cards[c])/len(cards[c])

	return cards


def gen_div(div_list):
	div_defaults = gen_div_default(div_list)
	substringcards = find_substrings(div_defaults)

	# Cards that are so rare they may not even be on Standard
	verygoodcards = ['House of Mirrors']

	# Cards that will never be displayed
	badcards = ["The Carrion Crow",
				"The King's Blade",
				"The Inoculated",
				"Struck by Lightning",
	            'The Web',
	            'The Sigil',
	            'The Surgeon',
	            'Prosperity']

	# Cards that will never make a drop noise
	lowcards = ["Thunderous Skies",
				"The Rabid Rhoa",
				"The Surgeon",
				"The Twins",
				"The Scholar",
				"Destined to Crumble",
	            'The Incantation',
	            'Shard of Fate',
	            'The Endurance']

	predefinedcards = badcards + lowcards + substringcards + verygoodcards

	for l in div_list:

		tmp = "Adding the following cards to {}:".format(l)
		for c in sorted(div_defaults):
			if c not in div_list[l]:
				tmp += ", {}".format(c)
				div_list[l][c] = div_defaults[c]
		print(tmp)

		bcards = badcards[:]

		name = convertname(l)

		items = {'high': verygoodcards[:], 'normal': [], 'low': lowcards[:]}

		for card in substringcards:
			if card in items['low']:
				items['low'].remove(card)
		for c in div_list[l]:
			if c in predefinedcards:
				pass
			elif div_list[l][c] > 20:
				items['high'].append(c)
			elif div_list[l][c] > 2:
				items['normal'].append(c)
			elif div_list[l][c] < 0.5:
				items['low'].append(c)
		with open('auto_gen\\{}divination.py'.format(name), 'w', encoding='utf-8') as f:
			f.write(u'''{}\ndesc = "Divination Card"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), l)))
			for c, ii in enumerate(substringcards):
				if ii in bcards:
					lvl = 'hide'
					bcards.remove(ii)
				elif div_list[l][ii] > 15:
					lvl = 'divination very high'
				elif div_list[l][ii] > 2:
					lvl = 'divination high'
				elif div_list[l][ii] <= 1:
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


def gen_unique(unique_list):
	
	for l in unique_list:
		name = convertname(l)
		if 'Catacombs Map' in unique_list[l]:
			del unique_list[l]['Catacombs Map']

		items = {'very high': [], 'high': [], 'special': [], 'low': []}

		for u in unique_list[l].keys():
			# If a unique shares a base and has at least 1 value that is over 2c while average is low, give it a special border
			if len(unique_list[l][u]) > 1:
				if max(unique_list[l][u]) > 3 > min(unique_list[l][u]):
					items['special'].append(u)
					continue
				unique_list[l][u] = min(unique_list[l][u])
			else:
				unique_list[l][u] = unique_list[l][u][0]

			if unique_list[l][u] >= 30:
				items['very high'].append(u)
			elif unique_list[l][u] >= 3.5:
				items['high'].append(u)
			elif unique_list[l][u] < 0.75:
				items['low'].append(u)

		with open('auto_gen\\{}uniques.py'.format(name), 'w', encoding='utf-8') as f:
			f.write(u'''{}\ndesc = "Unique"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), l)))
			for ii in sorted(items['very high']):
				f.write(u'\t"0 {0}": {{"base": "{0}", "type": "unique very high"}},\n'.format(ii))
			for ii in sorted(items['high']):
				f.write(u'\t"1 {0}": {{"base": "{0}", "type": "unique high"}},\n'.format(ii))
			for ii in sorted(items['special']):
				f.write(u'\t"6 {0}": {{"base": "{0}", "type": "unique special"}},\n'.format(ii))
			for ii in sorted(items['low']):
				f.write(u'\t"7 {0}": {{"base": "{0}", "type": "unique low"}},\n'.format(ii))
			f.write(u'\t"9 Other uniques": {"type": "unique normal"}\n}\n')


# Entry point for getting price data from poe.ninja
def scrape_ninja():
	leagues = ['Standard', 'Hardcore', 'tmpstandard', 'tmphardcore']

	paths = {
		'currency': 'http://cdn.poe.ninja/api/Data/GetCurrencyOverview?league={}',
		'div': 'http://cdn.poe.ninja/api/Data/GetDivinationCardsOverview?league={}',
		'essence': 'http://cdn.poe.ninja/api/Data/GetEssenceOverview?league={}',
		'unique jewel': 'http://cdn.poe.ninja/api/Data/GetUniqueJewelOverview?league={}',
		'unique map': 'http://cdn.poe.ninja/api/Data/GetUniqueMapOverview?league={}',
		'unique flask': 'http://cdn.poe.ninja/api/Data/GetUniqueFlaskOverview?league={}',
		'unique weapon': 'http://cdn.poe.ninja/api/Data/GetUniqueWeaponOverview?league={}',
		'unique armor': 'http://cdn.poe.ninja/api/Data/GetUniqueArmourOverview?league={}',
		'unique accessory': 'http://cdn.poe.ninja/api/Data/GetUniqueAccessoryOverview?league={}'
	}

	os.environ['NO_PROXY'] = 'cdn.poe.ninja'
	requester = requests.session()

	currency = {}
	divs = {}
	essences = {}
	uniques = defaultdict(list)

	for league in leagues:
		currency[league] = {}
		divs[league] = {}
		essences[league] = {}
		uniques[league] = defaultdict(list)

		for key in paths:
			req = requester.get(paths[key].format(league))
			data = req.json(encoding='utf-8')
			if key == 'currency':
				for i in data:
					for ii in data[i]:
						if 'chaosEquivalent' in ii:
							currency[league][ii['currencyTypeName']] = ii['chaosEquivalent']

			elif key == 'div':
				for i in data:
					for ii in data[i]:
						divs[league][ii['name']] = ii['chaosValue']
			elif key == 'essence':
				for i in data:
					for ii in data[i]:
						essences[league][ii['name']] = ii['chaosValue']

			else:
				for i in data:
					for ii in data[i]:
						if 'links' in ii and ii['links']:
							continue
						uniques[league][ii['baseType']].append(ii['chaosValue'])

	gen_currency(currency)
	gen_div(divs)
	gen_essence(essences)
	gen_unique(uniques)


if __name__ == '__main__':
	scrape_ninja()