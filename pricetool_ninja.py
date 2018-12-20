#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher

import os
import requests
from collections import defaultdict
from datetime import datetime
from ninja_defaults import currencydefaults, essencedefaults, prophecydefaults, divdefaults, uniquedefaults, scarabdefaults

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


# Helper function to find missing items and print a list of them
def fixmissing(ninja_list, defaults, league, name):
	# Print all items that were returned by poe.ninja that don't have a default set
	if set(ninja_list.keys()) - set(defaults.keys()):
		print("{} Missing defaults for {}: \n{}".format(league, name, ', '.join(['"{}": {}'.format(x, ninja_list[x]) for x in set(ninja_list.keys()) - set(defaults.keys())])))
	# add missing items to ninja_list
	for v in set(defaults.keys()) - set(ninja_list.keys()):
		ninja_list[v] = defaults[v]


# Convert a currency shorthand to full name.  returns a string
def currencyclassify(cur, val, curvals, stacks=1):
	# list of currency to always give a border to if their price is low
	ah = [
		"Splinter of Chayula", "Splinter of Xoph", "Splinter of Uul-Netol", "Splinter of Tul", "Splinter of Esh",
		"Chromatic Orb", "Perandus Coin", "Cartographer's Chisel", "Orb of Fusing", "Silver Coin",
		#"Orb of Alteration",
		#"Orb of Augmentation",
		#"Jeweller's Orb",
		#"Orb of Transmutation",
		"Orb of Chance",
	]
	if ((cur in ah) or 'Fossil' in cur) and val < curvals['normal']:
		tier = 'currency show'
	elif 'Alchemical Resonator' in cur and 'Prime' not in cur:
		tier = 'currency very low'
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
		tier = 'currency very low'
		#tier = 'hide'

	if stacks > 1:
		return "$ {0}\": {{\"base\": \"{0}\", 'other': ['StackSize >= {2}'], \"class\": \"Currency\", \"type\": \"{1}\"}}".format(cur, tier, stacks)
	return "1 {0}\": {{\"base\": \"{0}\", \"class\": \"Currency\", \"type\": \"{1}\"}}".format(cur, tier)


# given a league grouped list of currency determine all unique entries and then output for each league
def gen_currency(currency_list, league):
	# Add chaos and Scroll of Wisdom to the default list as poe.ninja does not include them
	currencydefaults["Chaos Orb"] = 1
	currencydefaults["Scroll of Wisdom"] = 1 / 100

	stackable = ['Orb', 'Splinter', 'Chisel', 'Coin', 'Bauble', 'Sextant', 'Shard', 'Whetstone', 'Scroll', 'Scrap']

	shards = {'Binding Shard': 'Orb of Binding', 'Horizon Shard': 'Orb of Horizons', 'Harbinger\'s Shard': 'Harbinger\'s Orb', 'Engineer\'s Shard': 'Engineer\'s Orb', 'Ancient Shard': 'Ancient Orb',
	          'Regal Shard': 'Regal Orb', 'Alchemy Shard': 'Orb of Alchemy', 'Alteration Shard': 'Orb of Alteration', 'Transmutation Shard': 'Orb of Transmutation', 'Scroll Fragment': 'Scroll of Wisdom',
			  'Exalted Shard': 'Exalted Orb', 'Annulment Shard': 'Orb of Annulment', 'Mirror Shard': 'Mirror of Kalandra'}

	fixmissing(currency_list, currencydefaults, league, "currency")

	for s in shards:
		if s not in currency_list:
			currency_list[s] = currency_list[shards[s]] / 20
	#	substringunique = find_substrings(currency_list)

	curval = '''{}\ndesc = "Currency Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

	curvals = gentierval(currency_list['Exalted Orb'])

	for cur in sorted(currency_list):
		if any(stack in cur for stack in stackable):
			val = currency_list[cur]
			retstr = currencyclassify(cur, val, curvals)
			curval += '\t"{},\n'.format(retstr)

			prevval = retstr[-20:]
			count = 9
			for i in range(2, 21):
				retstr = currencyclassify(cur, currency_list[cur] * i, curvals, i)
				if prevval != retstr[-20:]:
					curval += '\t"{},\n'.format(retstr.replace('$', '{:02}'.format(count)))
					count -= 1
					prevval = retstr[-20:]

		else:
			retstr = currencyclassify(cur, currency_list[cur], curvals)
			curval += '\t"{},\n'.format(retstr)

	curval += u'}\n'

	name = convertname(league)

	with open('auto_gen\\{}currency.py'.format(name), 'w', encoding='utf-8') as f:
		f.write(curval)

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

	fixmissing(essence_list, essencedefaults, league, 'essences')

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


# Convert a prophecy value to string.  returns a string
def prophecyclassify(cur, val, curvals):
	if val >= curvals['extremely']:
		tier = 'currency extremely high'
	elif val > curvals['very']:
		tier = 'currency very high'
	elif val > curvals['high']:
		tier = 'currency high'
	elif val < curvals['normal']:
		tier = 'currency very low'
	else:
		return

	return "{0}\": {{\"prophecy\": \"{0}\", \"class\": \"Currency\", \"type\": \"{1}\"}}".format(cur, tier)


# given a league grouped list of prophecies determine all unique entries and then output for each league
def gen_prophecy(prophecy_list, league, curvals):
	fixmissing(prophecy_list, prophecydefaults, league, 'prophecy')

	for invalid in ['A Gracious Master', "Echoes of Lost Love", "Echoes of Mutation", "The Emperor's Trove", "The Blacksmith", "The Forgotten Soldiers", "The Mentor", "The Aesthete's Spirit"]:
		if invalid in prophecy_list:
			del prophecy_list[invalid]

	substringprophecy = find_substrings(prophecy_list)

	curval = '''{}\ndesc = "Prophecy Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

	for c, cur in enumerate(substringprophecy):
		retstr = prophecyclassify(cur, prophecy_list[cur], curvals)
		if not retstr:
			retstr = '{0}": {{"prophecy": "{0}", "class": "Currency", "type": "currency low"}}'.format(cur)
		curval += '\t"{:03d} {},\n'.format(c, retstr)
		del prophecy_list[cur]
	for cur in sorted(prophecy_list.keys()):
		retstr = prophecyclassify(cur, prophecy_list[cur], curvals)
		if retstr:
			curval += '\t"1 {},\n'.format(retstr)

	curval += '\t"7 Prophecy default": {"Prophecy": "", "class": "Currency", "type": "currency low"}\n}\n'

	name = convertname(league)

	with open('auto_gen\\{}prophecy.py'.format(name), 'w', encoding='utf-8') as f:
		f.write(curval)


# Find all keys that have other keys which are substrings
# Convert a scarab value to string.  returns a string
def scarabclassify(cur, val, curvals):
	if val >= curvals['extremely']:
		tier = 'map very good'
	elif val >= curvals['very']:
		tier = 'map red good'
	elif val >= curvals['high']:
		tier = 'map yellow good'
	elif val <= curvals['normal']:
		tier = 'map white'
	else:
		return

	return "{0}\": {{\"base\": \"{0}\", \"class\": \"Map Fragments\", \"type\": \"{1}\"}}".format(cur, tier)


# given a league grouped list of prophecies determine all unique entries and then output for each league
def gen_scarab(scarab_list, league, curvals):
	fixmissing(scarab_list, scarabdefaults, league, 'scarab')

	substringscarab = find_substrings(scarab_list)

	curval = '''{}\ndesc = "scarab Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

	for c, cur in enumerate(substringscarab):
		retstr = scarabclassify(cur, scarab_list[cur], curvals)
		if not retstr:
			retstr = '{0}": {{"base": "{0}", "class": "Map Fragments", "type": "map yellow"}}'.format(cur)
		curval += '\t"{:03d} {},\n'.format(c, retstr)
		del scarab_list[cur]
	for cur in sorted(scarab_list.keys()):
		retstr = scarabclassify(cur, scarab_list[cur], curvals)
		if retstr:
			curval += '\t"1 {},\n'.format(retstr)

	curval += '\t"7 scarab default": {"base": "Scarab", "class": "Map Fragments", "type": "map yellow"}\n}\n'

	name = convertname(league)

	with open('auto_gen\\{}scarab.py'.format(name), 'w', encoding='utf-8') as f:
		f.write(curval)


# Find all keys that have other keys which are substrings
def find_substrings(source_dict):
	names = list(source_dict.keys())
	substringmatches = {}
	for index in range(len(names) - 1):
		for name in names[index + 1:]:
			if names[index] in name or name in names[index]:
				if name in names[index]:
					sub, full = name, names[index]
				else:
					sub, full = names[index], name
				if sub not in substringmatches:
					substringmatches[sub] = [full]
				else:
					substringmatches[sub].append(full)

	badnames = [badname for substring in substringmatches for badname in substringmatches[substring]]
	# distinct values by converting to a set
	# sort based on descending length so that any additional substrings are at the end of the list
	return sorted(set(badnames), reverse=True, key=lambda s: len(s))


# Convert a div card value to string.  returns a string
def divclassify(cur, val, curvals, lowcards, badcards):
	if cur in lowcards:
		tier = 'divination low'
	elif cur in badcards:
		tier = 'hide'
	elif val >= curvals['extremely']:
		tier = 'divination extremely high'
	elif val > curvals['very']:
		tier = 'divination very high'
	elif val > curvals['high']:
		tier = 'divination high'
	elif val < curvals['high'] / 2:
		tier = 'divination low'
	else:
		return

	return '{0}": {{"base": "{0}", "class": "Divination Card", "type": "{1}"}}'.format(cur, tier)


def gen_div(div_list, league, curvals):
	fixmissing(div_list, divdefaults, league, 'Divination cards')

	substringcards = find_substrings(div_list)

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

	curval = '{}\ndesc = "Divination Card"\n\n# Base type : settings pair\nitems = {{\n'.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

	for c, cur in enumerate(substringcards):
		retstr = divclassify(cur, div_list[cur], curvals, lowcards, badcards)
		if not retstr:
			retstr = '{0}": {{"base": "{0}", "class": "Divination Card", "type": "divination normal"}}'.format(cur)
		curval += '\t"{:03d} {},\n'.format(c, retstr)
		del div_list[cur]
	for cur in sorted(div_list.keys()):
		retstr = divclassify(cur, div_list[cur], curvals, lowcards, badcards)
		if retstr:
			curval += '\t"1 {},\n'.format(retstr)

	curval += u'\t"9 Other Divination Cards": {"class": "Divination Card", "type": "divination normal"}\n}\n'

	name = convertname(league)
	with open('auto_gen\\{}divination.py'.format(name), 'w', encoding='utf-8') as f:
		f.write(curval)


# Convert a unique value to string.  returns a string
def uniqueclassify(cur, vals, curvals):
	val = min(vals)
	if max(vals) > curvals['very'] > min(vals):
		tier = 'unique special'
	elif val >= curvals['extremely']:
		tier = 'unique extremely high'
	elif val > curvals['very']:
		tier = 'unique very high'
	elif val > curvals['high']:
		tier = 'unique high'
	elif val < curvals['high'] / 2:
		tier = 'unique low'
	else:
		return

	return "{0}\": {{\"base\": \"{0}\", \"type\": \"{1}\"}}".format(cur, tier)


def gen_unique(unique_list, league, curvals):
	fixmissing(unique_list, uniquedefaults, league, 'uniques')

	for invalid in ['Torture Chamber Map', 'Catacombs Map']:
		if invalid in unique_list:
			del unique_list[invalid]

	substringunique = find_substrings(unique_list)

	curval = '{}\ndesc = "Unique"\n\n# Base type : settings pair\nitems = {{\n'.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

	for c, cur in enumerate(substringunique):
		retstr = uniqueclassify(cur, unique_list[cur], curvals)
		if not retstr:
			retstr = '{0}": {{"base": "{0}", "type": "unique normal"}}'.format(cur)
		curval += '\t"{:03d} {},\n'.format(c, retstr)
		del unique_list[cur]
	for cur in sorted(unique_list.keys()):
		retstr = uniqueclassify(cur, unique_list[cur], curvals)
		if retstr:
			curval += '\t"1 {},\n'.format(retstr)

	curval += u'\t"9 Other uniques": {"type": "unique normal"}\n}\n'

	name = convertname(league)
	with open('auto_gen\\{}uniques.py'.format(name), 'w', encoding='utf-8') as f:
		f.write(curval)


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
	outbuff = ''
	# bases[ii['levelRequired']][ii['variant']][ii['baseType']] = ii['chaosValue']
	with open('auto_gen\\{}bases.py'.format(name), 'w', encoding='utf-8') as f:
		outbuff += '''{}\ndesc = "Bases"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))
		count = 0
		for level in sorted(bases_list, reverse=True):
			for variant in ['Shaper', 'Elder', None]:
				if variant in bases_list[level]:
					for ignoreilvl in ['Cobalt Jewel', 'Crimson Jewel', 'Viridian Jewel']:
						if ignoreilvl in bases_list[level][variant]:
							del bases_list[level][variant][ignoreilvl]
					for baseType in sorted(bases_list[level][variant]):
						value = baseclassify(bases_list[level][variant][baseType], curvals)
						if value:
							if level == 86:
								outbuff += '\t"{4} {2}{0}": {{"base": "{0}", "other": [{1}"ItemLevel >= {3}"], "type": "{5}"}},\n'.format(baseType, '"{}Item True", '.format(variant) if variant else '', variant + ' ' if variant else '', level, count, value)
							else:
								outbuff += '\t"{4} {2}{0}": {{"base": "{0}", "other": [{1}"ItemLevel {3}"], "type": "{5}"}},\n'.format(baseType, '"{}Item True", '.format(variant) if variant else '', variant + ' ' if variant else '', level, count, value)
			count += 1
		outbuff += '\n}\n'
	with open('auto_gen\\{}bases.py'.format(name), 'w', encoding='utf-8') as f:
		f.write(outbuff)

# Entry point for getting price data from poe.ninja
def scrape_ninja(leagues=('Standard', 'Hardcore', 'tmpstandard', 'tmphardcore')):
	# list of all uniques that can only be acquired through upgrades or vendor recipes to remove them from unique price consideration
	upgradeded = [
		# Fated Uniques
		'Kaltensoul', 'Thirst for Horrors', 'Atziri\'s Reflection', 'The Oak', 'Ezomyte Hold', 'Frostferno', 'Martyr\'s Crown', 'Asenath\'s Chant', 'Deidbellow',
		'Malachai\'s Awakening', 'Wall of Brambles', 'Wildwrap', 'Fox\'s Fortune', 'Crystal Vault', 'Windshriek', 'Greedtrap', 'Shavronne\'s Gambit', 'Duskblight',
		'Sunspite', 'Hrimburn', 'Doedre\'s Malevolence', 'Amplification Rod', 'Corona Solaris', 'Sanguine Gambol', 'The Gryphon', 'Dreadsurge', 'Dreadbeak', 'Cameria\'s Avarice',
		'Silverbough', 'The Tempest', 'Doomfletch\'s Prism', 'Death\'s Opus', 'Mirebough', 'Realm Ender', 'The Stormwall', 'The Cauteriser', 'Queen\'s Escape', 'The Dancing Duo',
		'Hrimnor\'s Dirge', 'Panquetzaliztli', 'Geofri\'s Devotion', 'Voidheart', 'Kaom\'s Way', 'Winterweave', 'Timetwist', 'Ngamahu Tiki', 'Karui Charge', 'The Effigon',
		'The Tactician', 'The Nomad', 'The Signal Fire', 'Cragfall', 'Hyrri\'s Demise', 'Chaber Cairn', 'Geofri\'s Legacy', 'The Iron Fortress', 'Whakatutuki o Matua',
		# Incursion Vial upgrades
		'Transcendent Flesh', 'Transcendent Mind', 'Transcendent Spirit', 'Soul Ripper', 'Slavedriver\'s Hand', 'Coward\'s Legacy', 'Omeyocan', 'Fate of the Vaal',
		'Mask of the Stitched Demon', 'Apep\'s Supremacy', 'Zerphi\'s Heart', 'Shadowstitch',
		# Vendor recipes
		'The Anima Stone', 'Arborix', 'Duskdawn', 'The Goddess Scorned', 'The Goddess Unleashed', 'Kingmaker', 'Magna Eclipsis', 'The Retch', 'Star of Wraeclast', 'The Taming',
		'The Vinktar Square', 'Loreweave',
		# Upgraded Breach Uniques
		'Xoph\'s Nurture', 'The Formless Inferno', 'Xoph\'s Blood', 'Tulfall', 'The Perfect Form', 'The Pandemonius', 'Hand of Wisdom and Action', 'Esh\'s Visage', 'Choir of the Storm',
		'Uul-Netol\'s Embrace', 'The Red Trail', 'The Surrender', 'United in Dream', 'Skin of the Lords', 'Presence of Chayula', 'The Red Nightmare', 'The Green Nightmare', 'The Blue Nightmare',
	]

	# TODO: scarab tiers when poe.ninja has data
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
		'fossil': 'https://poe.ninja/api/data/itemoverview?league={}&type=Fossil',
		'prophecy': 'https://poe.ninja/api/data/itemoverview?league={}&type=Prophecy',
		'scarab': 'https://poe.ninja/api/data/itemoverview?league={}&type=Scarab'
	}

	os.environ['NO_PROXY'] = 'poe.ninja'
	requester = requests.session()

	# Minimum number of item that must exist on poe.ninja for it to be considered
	mincount = 8

	for league in leagues:
		currency = {}
		divs = {}
		essences = {}
		bases = {}
		prophecy = {}
		scarab = {}
		uniques = defaultdict(list)

		for key in paths:
			req = requester.get(paths[key].format(league))
			data = req.json(encoding='utf-8')
			if key == 'currency':
				for i in data:
					for ii in data[i]:
						if 'chaosEquivalent' in ii:
							pc = ii['pay']['count'] if ii['pay'] else 0
							rc = ii['receive']['count'] if ii['receive'] else 0
							if pc + rc < mincount:
								continue
							currency[ii['currencyTypeName']] = ii['chaosEquivalent']

			elif key == 'bases':
				for i in data:
					for ii in data[i]:
						if ii['baseType'].startswith('Superior ') or ii['count'] < mincount:
							continue
						if ii['levelRequired'] not in bases:
							bases[ii['levelRequired']] = {}
						if ii['variant'] not in bases[ii['levelRequired']]:
							bases[ii['levelRequired']][ii['variant']] = {}
						bases[ii['levelRequired']][ii['variant']][ii['baseType']] = ii['chaosValue']

			elif key in ['resonator', 'fossil']:
				for i in data:
					for ii in data[i]:
						if ii['count'] < mincount:
							continue
						currency[ii['name']] = ii['chaosValue']

			elif key == 'prophecy':
				for i in data:
					for ii in data[i]:
						if ii['count'] < mincount:
							continue
						prophecy[ii['name']] = ii['chaosValue']

			elif key == 'div':
				for i in data:
					for ii in data[i]:
						if ii['count'] < mincount:
							continue
						divs[ii['name']] = ii['chaosValue']
			elif key == 'essence':
				for i in data:
					for ii in data[i]:
						if ii['count'] < mincount:
							continue
						essences[ii['name']] = ii['chaosValue']

			elif key == 'scarab':
				for i in data:
					for ii in data[i]:
						if ii['count'] < mincount:
							continue
						scarab[ii['name']] = ii['chaosValue']

			elif 'unique' in key:
					for i in data:
						for ii in data[i]:
							if ii['count'] < mincount:
								continue
							if 'links' in ii and ii['links'] or ii['name'] in upgradeded or 'relic' in ii['icon']:
								continue
							uniques[ii['baseType']].append(ii['chaosValue'])

			else:
				print('Unhandled key: "{}"'.format(key))

		curvals = gen_currency(currency, league)
		gen_div(divs, league, curvals)
		gen_bases(bases, league, curvals)
		gen_essence(essences, league, curvals)
		gen_prophecy(prophecy, league, curvals)
		gen_scarab(scarab, league, curvals)
		gen_unique(uniques, league, curvals)


if __name__ == '__main__':
	scrape_ninja()