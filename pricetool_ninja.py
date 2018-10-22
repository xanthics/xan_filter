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


# Helper function to tier items based on value of ex
def gentierval(exa):
	ret = {'extremely': exa if exa > 50 else 50,
		   'very': exa // 10 if exa > 50 else 5,
		   'high': 1,
		   'normal': 1/4,
		   'low': 1/15,
		   'min': 1/30}
	return ret


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
def currencyclassify(cur, val, curvals, stacks=1):
	# list of currency to always give a border to
	ah = ["Splinter of Chayula", "Splinter of Xoph", "Splinter of Uul-Netol", "Splinter of Tul", "Splinter of Esh",
		  "Chromatic Orb", "Perandus Coin", "Orb of Chance", "Cartographer's Chisel"]  # , "Jeweller's Orb", "Orb of Alteration", "Silver Coin"
	if ((cur in ah) or 'Fossil' in cur) and val < curvals['normal']:
		tier = 'currency show'
	elif 'Alchemical Resonator' in cur and 'Prime' not in cur:
		tier= 'currency very low'
	elif val >= curvals['extremely']:
		tier = 'currency extremely high'
	elif val >= curvals['very']:
		tier = 'currency very high'
	elif val >= curvals['high']:
		tier = 'currency high'
	elif val >= curvals['normal']:
		tier = 'currency normal'
	elif val >= curvals['low']:
		tier = 'currency low'
	elif val >= curvals['min']:
		tier = 'currency very low'
	else:
		#tier = 'currency very low'
		tier = 'hide'
	if stacks > 1:
		return "$ {0}\": {{\"base\": \"{0}\", 'other': ['StackSize >= {2}'], \"class\": \"Currency\", \"type\": \"{1}\"}}".format(cur, tier, stacks)
	return "1 {0}\": {{\"base\": \"{0}\", \"class\": \"Currency\", \"type\": \"{1}\"}}".format(cur, tier)


# given a league grouped list of currency determine all unique entries and then output for each league
def gen_currency(currency_list, league):
	stackable = ['Orb', 'Splinter', 'Chisel', 'Coin', 'Bauble', 'Sextant', 'Shard', 'Whetstone', 'Scroll', 'Scrap']

	defaults = {"Exalted Orb": 80.0, "Chaos Orb": 1.0, "Orb of Fusing": 0.5, "Regal Orb": 1, "Orb of Alteration": 1 / 16, "Orb of Alchemy": 1 / 3, "Jeweller's Orb": 1 / 8, "Gemcutter's Prism": 1,
	            "Divine Orb": 15.0, "Orb of Scouring": 0.5, "Blessed Orb": 0.5, "Vaal Orb": 1, "Orb of Chance": 1 / 8, "Orb of Regret": 1.0, "Chromatic Orb": 1 / 15, "Cartographer's Chisel": 0.25,
	            "Silver Coin": 1 / 3, "Glassblower's Bauble": 1 / 8, "Orb of Augmentation": 1 / 32, "Orb of Transmutation": 1 / 64, "Perandus Coin": 1 / 45, "Apprentice Cartographer's Sextant": .5,
	            "Journeyman Cartographer's Sextant": 2, "Master Cartographer's Sextant": 5, 'Eternal Orb': 300, "Blessing of Chayula": 300, "Blessing of Esh": 30, "Blessing of Uul-Netol": 10,
	            "Blessing of Tul": 2, "Blessing of Xoph": 3, "Splinter of Chayula": 3, "Splinter of Xoph": 0.333, "Splinter of Uul-Netol": 0.5, "Splinter of Tul": 1 / 5, "Splinter of Esh": 0.333,
	            "Blacksmith's Whetstone": 1 / 30, "Portal Scroll": 1 / 100, "Armourer's Scrap": 1 / 50, "Mirror Shard": 52, "Ancient Orb": 7, "Harbinger's Orb": 4, "Orb of Annulment": 3, "Exalted Shard": 7 / 3,
	            "Orb of Horizons": 2 / 3, "Engineer's Orb": 0.5, "Annulment Shard": 0.5, "Orb of Binding": 1 / 4, "Scroll of Wisdom": 1 / 100, 'Chaos Shard': 1 / 20, 'Mirror of Kalandra': 30000,

				"Prime Chaotic Resonator": 14.58, "Prime Alchemical Resonator": 13.86, "Powerful Chaotic Resonator": 1.0, "Powerful Alchemical Resonator": 1.0,
				"Primitive Alchemical Resonator": 0.43, "Primitive Chaotic Resonator": 0.43, "Potent Alchemical Resonator": 0.43, "Potent Chaotic Resonator": 0.43,
				"Fractured Fossil ": 139.02, "Faceted Fossil": 73.47, "Glyphic Fossil": 60.41, "Hollow Fossil": 37.09, "Tangled Fossil": 35.0, "Shuddering Fossil": 34.5,
				"Bloodstained Fossil": 27.5, "Gilded Fossil": 15.0, "Sanctified Fossil": 15.0, "Lucent Fossil": 5.0, "Encrusted Fossil": 4.0, "Bound Fossil": 3.0,
				"Prismatic Fossil": 3.0, "Enchanted Fossil": 3.0, "Perfect Fossil": 2.0, "Serrated Fossil": 1.93, "Aetheric Fossil": 1.14, "Jagged Fossil": 1.0,
				"Scorched Fossil": 1.0, "Pristine Fossil": 1.0, "Corroded Fossil": 1.0, "Metallic Fossil": 0.88, "Dense Fossil": 0.86, "Aberrant Fossil": 0.43, "Frigid Fossil": 0.43,

				}

	shards = {'Binding Shard': 'Orb of Binding', 'Horizon Shard': 'Orb of Horizons', 'Harbinger\'s Shard': 'Harbinger\'s Orb', 'Engineer\'s Shard': 'Engineer\'s Orb', 'Ancient Shard': 'Ancient Orb',
	          'Regal Shard': 'Regal Orb', 'Alchemy Shard': 'Orb of Alchemy', 'Alteration Shard': 'Orb of Alteration', 'Transmutation Shard': 'Orb of Transmutation', 'Scroll Fragment': 'Scroll of Wisdom'}

	c_list = list(defaults.keys()) + list(shards.keys())
	unknown = defaultdict(list)
	curval = '''{}\ndesc = "Currency Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

	if 'Exalted Orb' not in currency_list:
		currency_list['Exalted Orb'] = defaults['Exalted Orb']

	curvals = gentierval(currency_list['Exalted Orb'])

	for cur in sorted(c_list):
		if any(stack in cur for stack in stackable):
			if cur in currency_list:
				val = currency_list[cur]
				retstr = currencyclassify(cur, currency_list[cur], curvals)
			elif cur in shards:
				val = (currency_list[shards[cur]] if shards[cur] in currency_list else defaults[shards[cur]]) / 20
				retstr = currencyclassify(cur, (currency_list[shards[cur]] if shards[cur] in currency_list else defaults[shards[cur]]) / 20, curvals)
			else:
				val = defaults[cur]
				retstr = currencyclassify(cur, defaults[cur], curvals)
			curval += '\t"{},\n'.format(retstr)

			prevval = retstr[-20:]
			count = 9
			for i in range(2, 21):
				if cur in currency_list:
					retstr = currencyclassify(cur, currency_list[cur] * i, curvals, i)
				else:
					if cur in shards:
						retstr = currencyclassify(cur, (currency_list[shards[cur]] if shards[cur] in currency_list else defaults[shards[cur]]) / 20 * i, curvals, i)
					else:
						retstr = currencyclassify(cur, defaults[cur] * i, curvals, i)
				if prevval != retstr[-20:]:
					curval += '\t"{},\n'.format(retstr.replace('$', '{:02}'.format(count)))
					count -= 1
					prevval = retstr[-20:]

		else:
			if cur in currency_list:
				retstr = currencyclassify(cur, currency_list[cur], curvals)
			else:
				if cur in shards:
					retstr = currencyclassify(cur, (currency_list[shards[cur]] if shards[cur] in currency_list else defaults[shards[cur]]) / 20, curvals)
				else:
					retstr = currencyclassify(cur, defaults[cur], curvals)
				print('No data for {} in {}.  Using default,'.format(cur, league))
			curval += '\t"{},\n'.format(retstr)

	curval += u'}\n'

	name = convertname(league)

	with open('auto_gen\\{}currency.py'.format(name), 'w', encoding='utf-8') as f:
		f.write(curval)

	for v in currency_list.keys():
		if v not in defaults:
			unknown[v].append(currency_list[v])

	for u in unknown:
		#print("Unknown currency: {}".format(u))
		print('"{}": {},'.format(u, currency_list[u]), end=' ')
	print()
	return curvals


# Convert a essence value to string.  returns a string
def essenceclassify(cur, val, curvals):
	if val >= curvals['extremely']:
		tier = 'currency extremely high'
	elif val > curvals['very']:
		tier = 'currency very high'
	elif val > curvals['high']:
		tier = 'currency high'
	elif val > curvals['high'] / 2:
		tier = 'currency normal'
	else:
		tier = 'currency low'

	return "0 {0}\": {{\"base\": \"{0}\", \"class\": \"Currency\", \"type\": \"{1}\"}}".format(cur, tier)


# given a league grouped list of essences determine all unique entries and then output for each league
def gen_essence(essence_list, league, curvals):
	curval = '''{}\ndesc = "Essence Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

	for cur in sorted(essence_list.keys()):
		retstr = essenceclassify(cur, essence_list[cur], curvals)
		if retstr:
			curval += '\t"{},\n'.format(retstr)

	curval += '\t"7 Essence default": {"base": "Essence", "class": "Currency", "type": "currency low"}'
	curval += u'}\n'

	name = convertname(league)

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


def gen_div(div_list, league, curvals):
	substringcards = find_substrings(div_list)

	# Cards that are so rare they may not even be on Standard
	verygoodcards = ['House of Mirrors']

	# Cards that will never be displayed
	badcards = ["The Twins",
				"Destined to Crumble",
				"The Rabid Rhoa",
				"Thunderous Skies",
				"The Carrion Crow",
				"The King's Blade",
				"The Inoculated",
				"Struck by Lightning",
	            'The Web',
	            'The Sigil',
	            'The Surgeon',
	            'Prosperity',
				'The Metalsmith\'s Gift',
				'Dying Anguish',
				'The Road to Power',
				'The Lord in Black',
				'The Tyrant',
				'Merciless Armament',
				'The Jester',
				'The Spoiled Prince',
				'The Undisputed',
				'Blessing of God',
				'The Scarred Meadow',
				'Rain Tempter']

	# Cards that will never make a drop noise
	lowcards = ["The Scholar",
				'The Incantation',
	            'Shard of Fate',
	            'The Endurance',
				'The Lover',
				'Anarchy\'s Price',
				'Lantador\'s Lost Love',
				'The Opulent']

	predefinedcards = badcards + lowcards + substringcards + verygoodcards

	bcards = badcards[:]

	name = convertname(league)

	items = {'ehigh': verygoodcards[:], 'vhigh': [], 'high': [], 'low': lowcards[:]}

	for card in substringcards:
		if card in items['low']:
			items['low'].remove(card)
	for c in div_list:
		if c in predefinedcards:
			pass
		elif div_list[c] >= curvals['extremely']:
			items['ehigh'].append(c)
		elif div_list[c] > curvals['very']:
			items['vhigh'].append(c)
		elif div_list[c] > curvals['high']:
			items['high'].append(c)
		elif div_list[c] < curvals['high'] / 2:
			items['low'].append(c)
	with open('auto_gen\\{}divination.py'.format(name), 'w', encoding='utf-8') as f:
		f.write(u'''{}\ndesc = "Divination Card"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league)))
		for c, ii in enumerate(substringcards):
			if ii in bcards:
				lvl = 'hide'
				bcards.remove(ii)
			elif div_list[ii] >= curvals['extremely']:
				lvl = 'divination extremely high'
			elif div_list[ii] > curvals['very']:
				lvl = 'divination very high'
			elif div_list[ii] > curvals['high']:
				lvl = 'divination high'
			elif div_list[ii] < curvals['high'] / 2:
				lvl = 'divination low'
			else:
				lvl = 'divination normal'
			f.write(u'\t"{0:03d} {1}": {{"base": "{1}", "class": "Divination Card", "type": "{2}"}},\n'.format(c, ii, lvl))
		for ii in sorted(items['ehigh']):
			f.write(u'\t"1 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination extremely high"}},\n'.format(ii))
		for ii in sorted(items['vhigh']):
			f.write(u'\t"2 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination very high"}},\n'.format(ii))
		for ii in sorted(items['high']):
			f.write(u'\t"3 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination high"}},\n'.format(ii))
		for ii in sorted(items['low']):
			f.write(u'\t"4 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination low"}},\n'.format(ii))
		for ii in sorted(bcards):
			f.write(u'\t"7 {0}": {{"base": "{0}", "class": "Divination Card", "type": "hide"}},\n'.format(ii))
		f.write(u'\t"9 Other Divination Cards": {"class": "Divination Card", "type": "divination normal"}\n}\n')


def gen_unique(unique_list, league, curvals):
	name = convertname(league)
	if 'Catacombs Map' in unique_list:
		del unique_list['Catacombs Map']

	items = {'ehigh': [], 'vhigh': [], 'high': [], 'special': [], 'low': []}

	for u in unique_list.keys():
		# If a unique shares a base and has at least 1 value that is over 2c while average is low, give it a special border
		if len(unique_list[u]) > 1:
			if max(unique_list[u]) > curvals['very'] > min(unique_list[u]):
				items['special'].append(u)
				continue
			unique_list[u] = min(unique_list[u])
		else:
			unique_list[u] = unique_list[u][0]

		if unique_list[u] >= curvals['extremely']:
			items['ehigh'].append(u)
		elif unique_list[u] > curvals['very']:
			items['vhigh'].append(u)
#		elif unique_list[u] > curvals['high']:
			items['high'].append(u)
		elif unique_list[u] < curvals['high'] / 2:
			items['low'].append(u)

	with open('auto_gen\\{}uniques.py'.format(name), 'w', encoding='utf-8') as f:
		f.write(u'''{}\ndesc = "Unique"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league)))
		for ii in sorted(items['ehigh']):
			f.write(u'\t"0 {0}": {{"base": "{0}", "type": "unique extremely high"}},\n'.format(ii))
		for ii in sorted(items['vhigh']):
			f.write(u'\t"1 {0}": {{"base": "{0}", "type": "unique very high"}},\n'.format(ii))
		for ii in sorted(items['high']):
			f.write(u'\t"2 {0}": {{"base": "{0}", "type": "unique high"}},\n'.format(ii))
		for ii in sorted(items['special']):
			f.write(u'\t"6 {0}": {{"base": "{0}", "type": "unique special"}},\n'.format(ii))
		for ii in sorted(items['low']):
			f.write(u'\t"7 {0}": {{"base": "{0}", "type": "unique low"}},\n'.format(ii))
		f.write(u'\t"9 Other uniques": {"type": "unique normal"}\n}\n')


# Convert a essence value to string.  returns a string
def baseclassify(val, curvals):
	if val >= curvals['extremely']:
		tier = 'base extremely high'
	elif val >= curvals['very']:
		tier = 'base very high'
#	elif val >= curvals['high']*2:
#		tier = 'rare high'
	else:
		tier = None

	return tier


def gen_bases(bases_list, league, curvals):
	name = convertname(league)

	items = {'ehigh': {}, 'vhigh': {}}
	# bases[ii['levelRequired']][ii['variant']][ii['baseType']] = ii['chaosValue']
	with open('auto_gen\\{}bases.py'.format(name), 'w', encoding='utf-8') as f:
		f.write(u'''{}\ndesc = "Bases"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league)))
		count = 0
		for level in sorted(bases_list, reverse=True):
			for variant in ['Shaper', 'Elder', None]:
				if variant in bases_list[level]:
					for baseType in sorted(bases_list[level][variant]):
						value = baseclassify(bases_list[level][variant][baseType], curvals)
						if value:
							f.write(u'\t"{4} {2}{0}": {{"base": "{0}", "other": [{1}"ItemLevel >= {3}"], "type": "{5}"}},\n'.format(baseType, '"{}Item True", '.format(variant) if variant else '', variant + ' ' if variant else '', level, count, value))
			count += 1
		f.write(u'\n}\n')


# Entry point for getting price data from poe.ninja
def scrape_ninja(leagues=('Standard', 'Hardcore', 'tmpstandard', 'tmphardcore')):
	# list of all fated uniques to remove them from unique price consideration
	fated = ['Kaltensoul', 'Thirst for Horrors', 'Atziri\'s Reflection', 'The Oak', 'Ezomyte Hold', 'Frostferno', 'Martyr\'s Crown', 'Asenath\'s Chant', 'Deidbellow',
			 'Malachai\'s Awakening', 'Wall of Brambles', 'Wildwrap', 'Fox\'s Fortune', 'Crystal Vault', 'Windshriek', 'Greedtrap', 'Shavronne\'s Gambit', 'Duskblight',
			 'Sunspite', 'Hrimburn', 'Doedre\'s Malevolence', 'Amplification Rod', 'Corona Solaris', 'Sanguine Gambol', 'The Gryphon', 'Dreadsurge', 'Dreadbeak', 'Cameria\'s Avarice',
			 'Silverbough', 'The Tempest', 'Doomfletch\'s Prism', 'Death\'s Opus', 'Mirebough', 'Realm Ender', 'The Stormwall', 'The Cauteriser', 'Queen\'s Escape', 'The Dancing Duo',
			 'Hrimnor\'s Dirge', 'Panquetzaliztli', 'Geofri\'s Devotion', 'Voidheart', 'Kaom\'s Way', 'Winterweave', 'Timetwist', 'Ngamahu Tiki', 'Karui Charge', 'The Effigon',
			 'The Tactician', 'The Nomad', 'The Signal Fire', 'Cragfall', 'Hyrri\'s Demise', 'Chaber Cairn', 'Geofri\'s Legacy', 'The Iron Fortress']

	paths = {
		'currency': 'http://poe.ninja/api/Data/GetCurrencyOverview?league={}',
		'bases': 'http://poe.ninja/api/Data/GetBaseTypeOverview?league={}',
		'div': 'http://poe.ninja/api/Data/GetDivinationCardsOverview?league={}',
		'essence': 'http://poe.ninja/api/Data/GetEssenceOverview?league={}',
		'unique jewel': 'http://poe.ninja/api/Data/GetUniqueJewelOverview?league={}',
		'unique map': 'http://poe.ninja/api/Data/GetUniqueMapOverview?league={}',
		'unique flask': 'http://poe.ninja/api/Data/GetUniqueFlaskOverview?league={}',
		'unique weapon': 'http://poe.ninja/api/Data/GetUniqueWeaponOverview?league={}',
		'unique armor': 'http://poe.ninja/api/Data/GetUniqueArmourOverview?league={}',
		'unique accessory': 'http://poe.ninja/api/Data/GetUniqueAccessoryOverview?league={}',
		'resonator': 'https://poe.ninja/api/data/itemoverview?league={}&type=Resonator',
		'fossil': 'https://poe.ninja/api/data/itemoverview?league={}&type=Fossil'
	}

	os.environ['NO_PROXY'] = 'poe.ninja'
	requester = requests.session()

	for league in leagues:
		currency = {}
		divs = {}
		essences = {}
		bases = {}
		uniques = defaultdict(list)

		for key in paths:
			req = requester.get(paths[key].format(league))
			data = req.json(encoding='utf-8')
			if key == 'currency':
				for i in data:
					for ii in data[i]:
						if 'chaosEquivalent' in ii:
							currency[ii['currencyTypeName']] = ii['chaosEquivalent']

			elif key == 'bases':
				for i in data:
					for ii in data[i]:
						if ii['baseType'].startswith('Superior ') or ii['count'] < 14:
							continue
						if ii['levelRequired'] not in bases:
							bases[ii['levelRequired']] = {}
						if ii['variant'] not in bases[ii['levelRequired']]:
							bases[ii['levelRequired']][ii['variant']] = {}
						bases[ii['levelRequired']][ii['variant']][ii['baseType']] = ii['chaosValue']

			elif key in ['resonator', 'fossil']:
				for i in data:
					for ii in data[i]:
						currency[ii['name']] = ii['chaosValue']

			elif key == 'div':
				for i in data:
					for ii in data[i]:
						divs[ii['name']] = ii['chaosValue']
			elif key == 'essence':
				for i in data:
					for ii in data[i]:
						essences[ii['name']] = ii['chaosValue']

			else:
				for i in data:
					for ii in data[i]:
						if 'links' in ii and ii['links'] or ii['name'] in fated or 'relic' in ii['icon']:
							continue
						uniques[ii['baseType']].append(ii['chaosValue'])

		curvals = gen_currency(currency, league)
		gen_div(divs, league, curvals)
		gen_bases(bases, league, curvals)
		gen_essence(essences, league, curvals)
		gen_unique(uniques, league, curvals)


if __name__ == '__main__':
	scrape_ninja()