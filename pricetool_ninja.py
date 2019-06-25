#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher

import os
import requests
from datetime import datetime
from collections import defaultdict
from ninja_defaults import currencydefaults, essencedefaults, prophecydefaults, divdefaults, uniquedefaults, scarabdefaults, helmenchantsdefaults, basedefaults, fragmentdefaults, incubatordefaults
from ninja_helm_lookup import helmnames

header = '''#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: {} UTC from "{}" data
'''


# Helper function to tier items based on value of ex
def gentierval(currencies):
	maxval = max(currencies['Exalted Orb'], 50)
	minval = 1/4  # min(currencies['Orb of Alchemy'], currencies["Orb of Scouring"], currencies["Cartographer's Chisel"], 1/4)
	ret = {'extremely': maxval,
		   'very': maxval // 10,
		   'high': 1,
		   'normal': minval,
		   'low': minval / 2,
		   'min': minval / 4}
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
		missing = ', '.join(['"{}": {}'.format(x, ninja_list[x]) for x in sorted(set(ninja_list.keys()) - set(defaults.keys()))])
		print(f"{league} Missing defaults for {name}: \n{missing}")
	# add missing items to ninja_list
	for v in set(defaults.keys()) - set(ninja_list.keys()):
		ninja_list[v] = defaults[v]


# Helper function to fix missing base data
def fixmissingbases(bases, league):
	if set(bases.keys()) - set(basedefaults.keys()):
		joinstr = ': {\n\t"Elder": {},\n\t"Shaper": {},\n\t"Normal": {}\n},\n'
		vals = joinstr.join([str(x) for x in sorted(set(bases.keys()) - set(basedefaults.keys()), reverse=True)])
		vals += joinstr
		print(f"{league} missing default base tiers:\n{vals}")
	# add missing items to ninja_list
	for v in set(basedefaults.keys()) - set(bases.keys()):
		bases[v] = {}

	for level in sorted(bases, reverse=True):
		for variant in ['Elder', 'Shaper', None]:
			if variant not in basedefaults[level]:
				print(f'Missing base default for {level}\n"{variant}": {{}}')
			if variant not in bases[level]:
				bases[level][variant] = {}
			fixmissing(bases[level][variant], basedefaults[level][variant], league, f"bases ({level}-{variant})")


# Add missing values to data returned by poe.ninja
def fixallmissing(league, currency, divs, bases, essences, prophecy, scarab, uniques, helmenchants, fragments, incubator):
	# Add chaos and Scroll of Wisdom to the default list as poe.ninja does not include them
	currencydefaults["Chaos Orb"] = 1
	currencydefaults["Scroll of Wisdom"] = 1 / 100
	fixmissing(currency, currencydefaults, league, "currency")

	currency["Vial of Awakening"] = currency['Exalted Orb'] * 2
	currency["Vial of Consequence"] = 3
	currency["Vial of Dominance"] = 1
	currency["Vial of Fate"] = 1/5
	currency["Vial of Summoning"] = 1/5
	currency["Vial of the Ritual"] = 1/4
	currency["Vial of Transcendence"] = 1/2
	currency["Vial of the Ghost"] = currency['Exalted Orb'] * 8
	currency["Vial of Sacrifice"] = currency['Exalted Orb'] * 18

	fixmissing(incubator, incubatordefaults, league, 'incubator')

	fixmissing(essences, essencedefaults, league, 'essences')

	fixmissing(prophecy, prophecydefaults, league, 'prophecy')

	fixmissing(scarab, scarabdefaults, league, 'scarab')

	fixmissing(divs, divdefaults, league, 'Divination cards')

	fixmissing(uniques, uniquedefaults, league, 'uniques')

	fixmissing(helmenchants, helmenchantsdefaults, league, "helmet enchants")

	fixmissing(fragments, fragmentdefaults, league, "Fragments")


# Convert a currency shorthand to full name.  returns a string
def currencyclassify(cur, val, curvals, stacks=1):
	# list of currency to always give a border to if their price is low
	ah = [
		"Splinter of Chayula", "Splinter of Xoph", "Splinter of Uul-Netol", "Splinter of Tul", "Splinter of Esh",
		"Perandus Coin", "Orb of Fusing", "Silver Coin",
		"Chromatic Orb",
		"Alchemy Shard",
		"Orb of Alteration", "Alteration Shard",
		#"Orb of Augmentation",
		#"Jeweller's Orb",
		#"Orb of Transmutation",
		"Orb of Chance",
		"Glassblower's Bauble",
		"Horizon Orb", "Horizon Shard",
		"Chaos Shard",
		"Engineer's Orb", "Engineer's Shard",
		"Orb of Binding", "Binding Shard",
		"Regal Orb", "Regal Shard",
		"Blessed Orb",
		"Timeless Eternal Empire Splinter", "Timeless Karui Splinter", "Timeless Maraketh Splinter", "Timeless Templar Splinter", "Timeless Vaal Splinter"
	]
	# list of currencies to always make sound if their value is low
	ahn = [
		'Orb of Alchemy',
		"Orb of Scouring",
		"Cartographer's Chisel"
	]
	if ((cur in ah) or 'Fossil' in cur) and val < curvals['normal']:
		tier = 'currency show'
	elif cur in ahn and val < curvals['normal']:
		tier = 'currency normal'
#	elif 'Alchemical Resonator' in cur and 'Prime' not in cur:
#		tier = 'currency very low'
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

	shards = {'Binding Shard': 'Orb of Binding', 'Horizon Shard': 'Orb of Horizons', 'Harbinger\'s Shard': 'Harbinger\'s Orb', 'Engineer\'s Shard': 'Engineer\'s Orb', 'Ancient Shard': 'Ancient Orb',
	          'Regal Shard': 'Regal Orb', 'Alchemy Shard': 'Orb of Alchemy', 'Alteration Shard': 'Orb of Alteration', 'Transmutation Shard': 'Orb of Transmutation', 'Scroll Fragment': 'Scroll of Wisdom',
			  'Chaos Shard': 'Chaos Orb', 'Exalted Shard': 'Exalted Orb', 'Annulment Shard': 'Orb of Annulment', 'Mirror Shard': 'Mirror of Kalandra'}

	for s in shards:
		if s not in currency_list:
			currency_list[s] = currency_list[shards[s]] / 20
	#	substringunique = find_substrings(currency_list)

	curval = '''{}\ndesc = "Currency Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

	curvals = gentierval(currency_list)

	for cur in sorted(currency_list):
		if any(stack in cur for stack in stackable):
			val = currency_list[cur]
			retstr = currencyclassify(cur, val, curvals)
			curval += '\t"{},\n'.format(retstr)

			prevval = retstr[-20:]
			count = 9
			maxval = 20
			if cur == "Perandus Coin":
				maxval = 1000
			elif "Splinter" in cur:
				maxval = 99
			elif cur in ["Orb of Transmutation", "Scroll of Wisdom", "Portal Scroll", "Armourer's Scrap", "Orb of Regret"]:
				maxval = 40
			elif cur in ["Orb of Augmentation", "Orb of Scouring", "Silver Coin"]:
				maxval = 30
			elif cur in ["Chaos Orb", "Orb of Alchemy", "Regal Orb", "Divine Orb", "Vaal Orb", "Apprentice Cartographer's Sextant", "Journeyman Cartographer's Sextant", "Master Cartographer's Sextant"]:
				maxval = 10
			for i in range(2, maxval+1):
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


# Convert a currency shorthand to full name.  returns a string
def fragmentclassify(cur, val, curvals, stacks=1):
	if val >= curvals['extremely']:
		tier = 'map very good'
	elif val >= curvals['very']:
		tier = 'map yellow good'
	elif val >= curvals['high']:
		tier = 'map white good'
	else:
		tier = 'map white'

	if stacks > 1:
		return "$ {0}\": {{\"base\": \"{0}\", 'other': ['StackSize >= {2}'], \"class\": \"Map Fragments\", \"type\": \"{1}\"}}".format(cur, tier, stacks)
	return "1 {0}\": {{\"base\": \"{0}\", \"class\": \"Map Fragments\", \"type\": \"{1}\"}}".format(cur, tier)


# given a league grouped list of currency determine all unique entries and then output for each league
def gen_fragments(fragment_list, league, curvals):

	stackable = []

	#	substringunique = find_substrings(currency_list)

	curval = '''{}\ndesc = "Fragment Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

	for frag in sorted(fragment_list):
		if any(stack in frag for stack in stackable):
			val = fragment_list[frag]
			retstr = fragmentclassify(frag, val, curvals)
			curval += '\t"{},\n'.format(retstr)

			prevval = retstr[-20:]
			count = 9
			for i in range(2, 21):
				retstr = fragmentclassify(frag, fragment_list[frag] * i, curvals, i)
				if prevval != retstr[-20:]:
					curval += '\t"{},\n'.format(retstr.replace('$', '{:02}'.format(count)))
					count -= 1
					prevval = retstr[-20:]

		else:
			retstr = fragmentclassify(frag, fragment_list[frag], curvals)
			curval += '\t"{},\n'.format(retstr)

	curval += u'}\n'

	name = convertname(league)

	with open('auto_gen\\{}fragment.py'.format(name), 'w', encoding='utf-8') as f:
		f.write(curval)

	return curvals


# Convert a essence value to string.  returns a string
def incubatorclassify(cur, val, curvals):
	if val >= curvals['extremely']:
		tier = 'currency extremely high'
	elif val > curvals['very']:
		tier = 'currency very high'
	elif val > curvals['high']:
		tier = 'currency high'
	elif val < curvals['normal']:
		tier = 'currency low'
	else:
		return

	return "0 {0}\": {{\"base\": \"{0}\", \"class\": \"Incubator\", \"type\": \"{1}\"}}".format(cur, tier)


# given a league grouped list of essences determine all unique entries and then output for each league
def gen_incubator(incubator_list, league, curvals):
	curval = '''{}\ndesc = "Incubator Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

	for cur in sorted(incubator_list.keys()):
		retstr = incubatorclassify(cur, incubator_list[cur], curvals)
		if retstr:
			curval += '\t"{},\n'.format(retstr)

	curval += '\t"7 incubator default": {"base": "Incubator", "class": "Incubator", "type": "currency normal"}'
	curval += u'}\n'

	name = convertname(league)

	with open('auto_gen\\{}incubator.py'.format(name), 'w', encoding='utf-8') as f:
		f.write(curval)


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
# Convert a scarab value to string.  returns a string
def enchantclassify(cur, val, curvals):
	if val >= curvals['extremely']:
		tier = 'currency extremely high'
	elif val >= curvals['very']:
		tier = 'currency very high'
	else:
		return

	return [f"{cur}\": {{\"enchant\": \"{val}\", \"type\": \"{tier}\"}}" for val in helmnames[cur]]


# given a league grouped list of prophecies determine all unique entries and then output for each league
def gen_enchants(helmenchant_list, league, curvals):
	substringhelmenchant = find_substrings(helmenchant_list)

	curval = '''{}\ndesc = "Helm Enchant Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

	for c, cur in enumerate(substringhelmenchant):
		retstr = enchantclassify(cur, helmenchant_list[cur], curvals)
		if not retstr:
			retstr = []
			for val in helmnames[cur]:
				retstr.append('{0}": {{"enchant": "{0}", "type": "ignore"}}'.format(val))
		if len(retstr) > 1:
			for count, val in enumerate(retstr):
				curval += f'\t"1 {count} {val},\n'
		else:
			curval += f'\t"{c:03d} {retstr[0]},\n'
		del helmenchant_list[cur]
	for cur in sorted(helmenchant_list.keys()):
		retstr = enchantclassify(cur, helmenchant_list[cur], curvals)
		if retstr:
			if len(retstr) > 1:
				for count, val in enumerate(retstr):
					curval += f'\t"1 {count} {val},\n'
			else:
				curval += f'\t"1 {retstr[0]},\n'

	curval += '\t"7 enchant default": {"other": ["AnyEnchantment True"], "type": "item mod"}\n}\n'

	name = convertname(league)

	with open('auto_gen\\{}helmenchant.py'.format(name), 'w', encoding='utf-8') as f:
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
def divclassify(cur, val, curvals):
	# divination cards that should always show an icon
	ah = [
		"Three Faces in the Dark", "Hubris", "Loyalty", "Rain of Chaos", "The Catalyst", "The Doppelganger", "The Gambler", "The Gemcutter", "The Master Artisan", "Emperor's Luck", "Jack in the Box", "Her Mask", "The Scholar"
		"House of Mirrors", "Alluring Bounty", "Abandoned Wealth", "Seven Years Bad Luck", "The Saint's Treasure", "The Hoarder", "The Sephirot", "Chaotic Disposition", "The Cartographer", "Monochrome", "The Seeker", "The Journey",
		"Lucky Connections", "Lucky Deck", "The Innocent", "The Wrath", "Emperor's Luck", "Loyalty", "The Inventor", "The Scholar", "The Survivalist", "The Union", "Vinia's Token", "The Puzzle", "Demigod's Wager", "No Traces", "Three Faces in the Dark",
		"The Master Artisan", "The Fool", "Coveted Possession", "Rain of Chaos", "The Catalyst", "The Gemcutter",
		"The Doctor", "The Fiend", "The World Eater", "Pride of the First Ones", "The Last One Standing", "The Wolven King's Bite", "The Samurai's Eye", "Pride Before the Fall", "The Life Thief", "Burning Blood", "The King's Heart",
		"The Queen", "The Undaunted", "The Mayor", "The Endless Darkness", "The Professor", "The Valkyrie", "Humility", "Time-Lost Relic", "Jack in the Box", "The Twilight Moon", "Arrogance of the Vaal", "Vanity", "The Dreamland",
		"The Nurse", "The Immortal", "Immortal Resolve", "Beauty Through Death", "The Dragon's Heart", "The Iron Bard", "Wealth and Power", "The Celestial Justicar", "The Enlightened", "The Celestial Stone", "The Sacrifice",
		"The Porcupine", "Last Hope", "The Artist", "The Dapper Prodigy", "Sambodhi's Vow", "Buried Treasure", "The Jeweller's Boon", "Bowyer's Dream", "Emperor of Purity", "The Chains that Bind", "The Ethereal",
		"Perfection", "The Warlord", "The Dark Mage", "The Valley of Steel Boxes", "Lingering Remnants", "The Realm", "The Obscured", "The Price of Protection", "Imperial Legacy", "The Flora's Gift",
	]
	# Cards that will never be displayed
	badcards = [
		"The Twins", "Destined to Crumble", "The Rabid Rhoa", "Thunderous Skies", "The Carrion Crow", "The King's Blade", "The Inoculated", "Struck by Lightning", 'The Sigil', 'The Surgeon', 'Prosperity',
		'The Metalsmith\'s Gift', 'The Road to Power', 'The Lord in Black', 'The Tyrant', 'Merciless Armament', 'The Jester', 'The Spoiled Prince', 'The Undisputed', 'Blessing of God', 'The Scarred Meadow',
		'Rain Tempter', 'The Lover', 'Lantador\'s Lost Love', 'The Opulent', "Death"
	]
	# Cards that will never make a drop noise
	lowcards = [
		'The Web', 'The Incantation', 'Shard of Fate', 'The Endurance', 'Anarchy\'s Price', "The Dragon"
	]

	if cur in ah and val < curvals['high'] / 2:
		tier = 'divination show'
	elif cur in lowcards:
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
	substringcards = find_substrings(div_list)

	curval = '{}\ndesc = "Divination Card"\n\n# Base type : settings pair\nitems = {{\n'.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

	for c, cur in enumerate(substringcards):
		retstr = divclassify(cur, div_list[cur], curvals)
		if not retstr:
			retstr = '{0}": {{"base": "{0}", "class": "Divination Card", "type": "divination normal"}}'.format(cur)
		curval += '\t"{:03d} {},\n'.format(c, retstr)
		del div_list[cur]
	for cur in sorted(div_list.keys()):
		retstr = divclassify(cur, div_list[cur], curvals)
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
	elif val > curvals['high']*2:
		tier = 'unique high'
	elif val < curvals['high'] / 2:
		tier = 'unique low'
	else:
		return

	return "{0}\": {{\"base\": \"{0}\", \"type\": \"{1}\"}}".format(cur, tier)


# Given a list of all uniques, reformat in to a base:value list
def compact_uniques(unique_full_list):
	unique_list = defaultdict(list)
	for name in unique_full_list:
		unique_list[unique_full_list[name]['baseType']].append(unique_full_list[name]['chaosValue'])
	return unique_list


def gen_unique(unique_full_list, league, curvals):
	unique_list = compact_uniques(unique_full_list)

	for invalid in ['Torture Chamber Map', 'Catacombs Map']:
		if invalid in unique_list:
			del unique_list[invalid]

	substringunique = find_substrings(unique_list)

	curval = '{}\ndesc = "Unique"\n\n# Base type : settings pair\nitems = {{\n'.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

	retstr = uniqueclassify('Reinforced Tower Shield', unique_list['Rawhide Tower Shield'], curvals)
	curval += '\t"000 {},\n'.format(retstr.replace('"base"', '"other": ["ItemLevel <= 60"], "base"'))

	for c, cur in enumerate(substringunique, 1):
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
def scrape_ninja(leagues=('tmpstandard',)):
	#leagues = ["Synthesis Event (SRE001)"]
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
		# Harbinger Uniques -- Currently only drops as pieces
		"The Flow Untethered", "The Fracturing Spinner", "The Tempest's Binding", "The Rippling Thoughts", "The Enmity Divine", "The Unshattered Will",
	]

	keys = [
		'Currency',
		'Fragment',
		'Scarab',
		'Fossil',
		'Resonator',
		"Incubator",
		'Essence',
		'DivinationCard',
		'Prophecy',
		'BaseType',
		'HelmetEnchant',
		'UniqueMap',
		'UniqueJewel',
		'UniqueFlask',
		'UniqueWeapon',
		'UniqueArmour',
		'UniqueAccessory'
	]

	leaguelookup = {
		"Standard": "Standard",
		"Hardcore": "Hardcore",
		"tmpstandard": "Legion",
		"tmphardcore": "Hardcore Legion",
	}

	os.environ['NO_PROXY'] = 'poe.ninja'
	requester = requests.session()

	# Minimum number of item that must exist on poe.ninja for it to be considered
	mincount = 8

	for league in leagues:
		currency = {}
		fragments = {}
		divs = {}
		incubator = {}
		essences = {}
		bases = {}
		prophecy = {}
		scarab = {}
		uniques = {}
		helmenchants = {}

		for key in keys:
			if key in ['Currency', 'Fragment']:
				request = f'https://poe.ninja/api/data/currencyoverview?league={leaguelookup[league]}&type={key}'
			else:
				request = f'https://poe.ninja/api/data/itemoverview?league={leaguelookup[league]}&type={key}'
			req = requester.get(request)
			print(f"Status code: {req.status_code}")
			if req.status_code == 204:
				print("No {} data for {}".format(key, league))
				continue
			data = req.json(encoding='utf-8')

			if key == 'Currency':
				for i in data:
					for ii in data[i]:
						if 'chaosEquivalent' in ii:
							pc = ii['pay']['count'] if ii['pay'] else 0
							rc = ii['receive']['count'] if ii['receive'] else 0
							if pc + rc < mincount:
								continue
							currency[ii['currencyTypeName']] = ii['chaosEquivalent']

			elif key == 'Fragment':
				for i in data:
					for ii in data[i]:
						if 'chaosEquivalent' in ii and ii['currencyTypeName'] != 'Offering to the Goddess':
							pc = ii['pay']['count'] if ii['pay'] else 0
							rc = ii['receive']['count'] if ii['receive'] else 0
							if pc + rc < mincount:
								continue
							if "Splinter" in ii['currencyTypeName']:
								currency[ii['currencyTypeName']] = ii['chaosEquivalent']
							else:
								fragments[ii['currencyTypeName']] = ii['chaosEquivalent']

			elif key == 'BaseType':
				for i in data:
					for ii in data[i]:
						if ii['baseType'].startswith('Superior ') or ii['count'] < mincount \
								or (not ii['variant'] and ii['baseType'] not in ['Searching Eye Jewel', 'Murderous Eye Jewel', 'Hypnotic Eye Jewel', 'Ghastly Eye Jewel', 'Opal Ring', 'Steel Ring', 'Crystal Belt', 'Marble Amulet']):
							continue
						if ii['levelRequired'] not in bases:
							bases[ii['levelRequired']] = {}
						if ii['variant'] not in bases[ii['levelRequired']]:
							bases[ii['levelRequired']][ii['variant']] = {}
						bases[ii['levelRequired']][ii['variant']][ii['baseType']] = ii['chaosValue']

			elif key in ['Resonator', 'Fossil']:
				for i in data:
					for ii in data[i]:
						if ii['count'] < mincount:
							continue
						currency[ii['name']] = ii['chaosValue']

			elif key == 'HelmetEnchant':
				for i in data:
					for ii in data[i]:
						if ii['count'] < mincount or ii['name'] not in helmnames:
#							if ii['name'] not in helmnames:
#								print(repr(ii['name']))
							continue
						helmenchants[ii['name']] = ii['chaosValue']

			elif key == 'Prophecy':
				for i in data:
					for ii in data[i]:
						if ii['count'] < mincount:
							continue
						prophecy[ii['name']] = ii['chaosValue']

			elif key == 'DivinationCard':
				for i in data:
					for ii in data[i]:
						if ii['count'] < mincount:
							continue
						divs[ii['name']] = ii['chaosValue']

			elif key == 'Incubator':
				for i in data:
					for ii in data[i]:
						if ii['count'] < mincount:
							continue
						incubator[ii['name']] = ii['chaosValue']

			elif key == 'Essence':
				for i in data:
					for ii in data[i]:
						if ii['count'] < mincount:
							continue
						essences[ii['name']] = ii['chaosValue']

			elif key == 'Scarab':
				for i in data:
					for ii in data[i]:
						if ii['count'] < mincount:
							continue
						scarab[ii['name']] = ii['chaosValue']

			elif 'Unique' in key:
					for i in data:
						for ii in data[i]:
							if ii['count'] < mincount:
								continue
							if ('links' in ii and ii['links']) or ii['name'] in upgradeded or 'relic' in ii['icon'] or ('variant' in ii and ii['variant'] and '2 Jewels' in ii['variant']):
								continue
							uniques[ii['name']] = {'baseType': ii['baseType'], 'chaosValue': ii['chaosValue']}

			else:
				print('Unhandled key: "{}"'.format(key))

		# Add all missing values to poe.ninja data
		fixallmissing(league, currency, divs, bases, essences, prophecy, scarab, uniques, helmenchants, fragments, incubator)
		fixmissingbases(bases, league)

		curvals = gen_currency(currency, league)
		gen_div(divs, league, curvals)
		gen_bases(bases, league, curvals)
		gen_incubator(incubator, league, curvals)
		gen_essence(essences, league, curvals)
		gen_prophecy(prophecy, league, curvals)
		gen_scarab(scarab, league, curvals)
		gen_unique(uniques, league, curvals)
		gen_enchants(helmenchants, league, curvals)
		gen_fragments(fragments, league, curvals)


if __name__ == '__main__':
	scrape_ninja()