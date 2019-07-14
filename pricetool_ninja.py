#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher

import os
import requests
from datetime import datetime
from collections import defaultdict
from theme_config.min_w_highlight import volume
from item_config.gen_item_lists import highbases
from ninja_helm_lookup import helmnames
from ninja_sanitizer import fixallmissing, fixmissingbases

header = '''#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: {} UTC from "{}" data
'''


# Helper function to convert a league name to a file prefix
def convertname(league):
	if league == 'Standard':
		return ""
	elif league == 'Hardcore':
		return "hc"
	elif 'tmphardcore' in league:
		return "thc"
	else:
		return "t"

# Convert a currency shorthand to full name.  returns a string
def currencyclassify(cur, val, curvals, stacks=1):
	# list of currency to always give a border to if their price is low
	ah = [
		"Splinter of Chayula", "Splinter of Xoph", "Splinter of Uul-Netol", "Splinter of Tul", "Splinter of Esh",
		"Perandus Coin", "Orb of Fusing",
		#"Silver Coin",
		#"Blacksmith's Whetstone",
		#"Armourer's Scrap",
		"Chromatic Orb",
		"Alchemy Shard",
		"Orb of Alteration", "Alteration Shard",
		#"Orb of Augmentation",
		#"Jeweller's Orb",
		#"Orb of Transmutation",
		#"Orb of Chance",
		#"Glassblower's Bauble",
		"Horizon Orb", "Horizon Shard",
		"Chaos Shard",
		"Engineer's Orb", "Engineer's Shard",
		"Binding Shard",
		"Regal Orb", "Regal Shard",
		#"Blessed Orb",
		"Timeless Eternal Empire Splinter", "Timeless Karui Splinter", "Timeless Maraketh Splinter", "Timeless Templar Splinter", "Timeless Vaal Splinter"
	]
	# list of currencies to always make sound if their value is low
	ahn = [
		'Orb of Alchemy',
		"Orb of Scouring",
		"Cartographer's Chisel"
	]
	if cur in ["Mirror of Kalandra", "Mirror Shard"]:
		tier = 'currency mirror'
	elif ((cur in ah) or 'Fossil' in cur) and val < curvals['normal']:
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
def gen_currency(currency_list, league, curvals):

	stackable = ['Orb', 'Splinter', 'Chisel', 'Coin', 'Bauble', 'Sextant', 'Shard', 'Whetstone', 'Scroll', 'Scrap']

	shards = {'Binding Shard': 'Orb of Binding', 'Horizon Shard': 'Orb of Horizons', 'Harbinger\'s Shard': 'Harbinger\'s Orb', 'Engineer\'s Shard': 'Engineer\'s Orb', 'Ancient Shard': 'Ancient Orb',
	          'Regal Shard': 'Regal Orb', 'Alchemy Shard': 'Orb of Alchemy', 'Alteration Shard': 'Orb of Alteration', 'Transmutation Shard': 'Orb of Transmutation', 'Scroll Fragment': 'Scroll of Wisdom',
			  'Chaos Shard': 'Chaos Orb', 'Exalted Shard': 'Exalted Orb', 'Annulment Shard': 'Orb of Annulment', 'Mirror Shard': 'Mirror of Kalandra'}

	for s in shards:
		if s not in currency_list:
			currency_list[s] = currency_list[shards[s]] / 20
	#	substringunique = find_substrings(currency_list)

	curval = '''{}\ndesc = "Currency Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

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


# Convert a currency shorthand to full name.  returns a string
def challengeclassify(cur, val, curvals, base, stacks=1):
	from random import randint  # for random moos

	if val >= curvals['extremely']:
		tier = 'challenge extremely high'
		other = 'CustomAlertSound "{}_challenge{}.wav"'.format(volume['max'], randint(11, 15))
	elif val >= curvals['very']:
		tier = 'challenge very high'
		other = 'CustomAlertSound "{}_challenge{}.wav"'.format(volume['high'], randint(11, 15))
	elif val >= curvals['high']:
		tier = 'challenge high'
		other = 'CustomAlertSound "{}_challenge{}.wav"'.format(volume['normal'], randint(11, 15))
	elif val >= curvals['normal']:
		tier = 'challenge normal'
		other = 'CustomAlertSound "{}_challenge{}.wav"'.format(volume['medium'], randint(5, 10))
	else:
		tier = 'challenge show'
		other = 'CustomAlertSound "{}_challenge{}.wav"'.format(volume['low'], randint(1, 4))

	if stacks > 1:
		return f"$ {cur}\": {{\"base\": \"{cur}\", 'other': ['StackSize >= {stacks}', '{other}'], \"class\": \"{base}\", \"type\": \"{tier}\"}}"
	return f"1 {cur}\": {{\"base\": \"{cur}\", 'other': ['{other}'], \"class\": \"{base}\", \"type\": \"{tier}\"}}"


# given a league grouped list of currency determine all unique entries and then output for each league
def gen_challenge(challenge_list, league, curvals):

	stackable = ['Splinter']

	#	substringunique = find_substrings(currency_list)

	curval = '''{}\ndesc = "Challenge Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

	for cur in sorted(challenge_list):
		if "Incubator" in cur:
			base = "Incubator"
		elif 'Emblem' in cur:
			base = "Map Fragments"
		else:
			base = "Currency"
		if any(stack in cur for stack in stackable):
			val = challenge_list[cur]
			retstr = challengeclassify(cur, val, curvals, base)
			curval += '\t"{},\n'.format(retstr)

			prevval = retstr[-20:]
			count = 9
			maxval = 20
			if "Splinter" in cur:
				maxval = 99
			for i in range(2, maxval+1):
				retstr = challengeclassify(cur, challenge_list[cur] * i, curvals, base, i)
				if prevval != retstr[-20:]:
					curval += '\t"{},\n'.format(retstr.replace('$', '{:02}'.format(count)))
					count -= 1
					prevval = retstr[-20:]

		else:
			retstr = challengeclassify(cur, challenge_list[cur], curvals, base)
			curval += '\t"{},\n'.format(retstr)

	curval += u'}\n'

	name = convertname(league)

	with open('auto_gen\\{}challenge.py'.format(name), 'w', encoding='utf-8') as f:
		f.write(curval)


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
	elif val > curvals['high']*2:
		tier = 'currency high'
	elif val < curvals['normal']:
		tier = 'currency very low'
	else:
		tier = 'currency low'

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

	curval += '}\n'

	name = convertname(league)

	with open('auto_gen\\{}prophecy.py'.format(name), 'w', encoding='utf-8') as f:
		f.write(curval)


# Convert a prophecy value to string.  returns a string
def gemclassify(cur, val, curvals, level, qual, corrupt):
	if val >= curvals['extremely']:
		tier = 'gem extremely high'
	elif val > curvals['very']:
		tier = 'gem very high'
	elif val > curvals['high']:
		tier = 'gem high'
	elif (level > 1 and qual < 10) or cur in ["Enlighten Support", "Empower Support"]:
		tier = 'gem low'
	else:
		return

	return f'{cur}\": {{\"base\": \"{cur}\", \"class\": \"Gems\", "other": ["GemLevel >= {level}", "Quality >= {qual}", "Corrupted {corrupt}"], \"type\": \"{tier}\"}}'


# given a league grouped list of prophecies determine all unique entries and then output for each league
def gen_gems(gem_list, league, curvals):

	curval = '''{}\ndesc = "Skill Gems Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))

	for cl, level in enumerate(sorted(gem_list, reverse=True)):
		for cq, qual in enumerate(sorted(gem_list[level], reverse=True)):
			for corrupt in gem_list[level][qual]:
				substringgem = find_substrings(gem_list[level][qual][corrupt])

				for c, cur in enumerate(substringgem):
					retstr = gemclassify(cur, gem_list[level][qual][corrupt][cur], curvals, level, qual, corrupt)
					if not retstr:
						if level > 1 and qual < 10:
							retstr = f'{cur}": {{"base": "{cur}", "class": "Gems", "other": ["GemLevel >= {level}", "Quality >= {qual}", "Corrupted {corrupt}"], "type": "gem low"}}'
						elif qual >= 10:
							retstr = f'{cur}": {{"base": "{cur}", "class": "Gems", "other": ["GemLevel >= {level}", "Quality >= {qual}", "Corrupted {corrupt}"], "type": "gem normal"}}'
						else:
							retstr = f'{cur}": {{"base": "{cur}", "class": "Gems", "other": ["GemLevel >= {level}", "Quality >= {qual}", "Corrupted {corrupt}"], "type": "hide"}}'
					curval += f'\t"{cl}{cq} {corrupt} {c:03d} {retstr},\n'
					del gem_list[level][qual][corrupt][cur]
				for cur in sorted(gem_list[level][qual][corrupt].keys()):
					retstr = gemclassify(cur, gem_list[level][qual][corrupt][cur], curvals, level, qual, corrupt)
					if retstr:
						curval += f'\t"{cl}{cq} {corrupt} 1 {retstr},\n'

	curval += '}\n'

	name = convertname(league)

	with open('auto_gen\\{}skillgem.py'.format(name), 'w', encoding='utf-8') as f:
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

	curval += '\t"7 enchant default": {"class": "Helmet", "other": ["AnyEnchantment True"], "type": "item mod"}\n}\n'

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
		"Three Faces in the Dark", "Hubris", "Loyalty", "Rain of Chaos", "The Catalyst", "The Doppelganger", "The Gambler", "The Gemcutter", "The Master Artisan", "Emperor's Luck", "Jack in the Box", "The Scholar",  # "Her Mask",
		"House of Mirrors", "Alluring Bounty", "Abandoned Wealth", "Seven Years Bad Luck", "The Saint's Treasure", "The Hoarder", "The Sephirot", "Chaotic Disposition", "The Cartographer", "Monochrome", "The Seeker", "The Journey",
		"Lucky Connections", "Lucky Deck", "The Innocent", "The Wrath", "Emperor's Luck", "Loyalty", "The Inventor", "The Survivalist", "The Union", "Vinia's Token", "The Puzzle", "Demigod's Wager", "No Traces", "Three Faces in the Dark",
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
	if cur in ["House of Mirrors"]:
		tier = 'currency mirror'
	elif cur in badcards:
		tier = 'hide'
	elif val >= curvals['extremely']:
		tier = 'divination extremely high'
	elif val > curvals['very']:
		tier = 'divination very high'
	elif val > curvals['high']:
		tier = 'divination high'
	elif cur in ah and val < curvals['high'] / 2:
		tier = 'divination show'
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
def scrape_ninja(leagues=('Standard', 'Hardcore', 'tmpstandard', 'tmphardcore')):
	#leagues = ["Synthesis Event (SRE001)"]

	keys = [
		'SkillGem',
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
	# items that always show for elder/shaper and can show for normal
	goodbases = highbases()

	for league in leagues:
		currency = {}
		skillgem = {}
		challenges = {}
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
			print(f"{league} {key} Status code: {req.status_code}")
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
							if "Timeless" in ii['currencyTypeName']:
								challenges[ii['currencyTypeName']] = ii['chaosEquivalent']
							else:
								fragments[ii['currencyTypeName']] = ii['chaosEquivalent']

			elif key == 'SkillGem':
				for i in data['lines']:
					if i['count'] < mincount:
						continue
					if i['name'] in ['Enlighten Support', 'Enhance Support', 'Empower Support']:
						i['gemQuality'] = 0
					if i['gemLevel'] not in skillgem:
						skillgem[i['gemLevel']] = {}
					if i['gemQuality'] not in skillgem[i['gemLevel']]:
						skillgem[i['gemLevel']][i['gemQuality']] = {}
					if i['corrupted'] not in skillgem[i['gemLevel']][i['gemQuality']]:
						skillgem[i['gemLevel']][i['gemQuality']][i['corrupted']] = {}
					skillgem[i['gemLevel']][i['gemQuality']][i['corrupted']][i['name']] = i['chaosValue']

			elif key == 'BaseType':
				for i in data:
					for ii in data[i]:
						if ii['baseType'].startswith('Superior ') or \
								(ii['count'] < mincount and ii['variant'] and ii['baseType'] not in goodbases[ii['variant']]) or \
								(not ii['variant'] and ii['baseType'] not in goodbases[ii['variant']]):
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
#						incubator[ii['name']] = ii['chaosValue']
						challenges[ii['name']] = ii['chaosValue']

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
						# Special rule so that there is a value for tabula when calculating certain div card values
						if ii['name'] == 'Tabula Rasa':
							uniques[ii['name']] = {'baseType': ii['baseType'], 'chaosValue': ii['chaosValue']}
							continue
						if ii['count'] < mincount:
							continue
						if ('links' in ii and ii['links']) or 'relic' in ii['icon'] or ('variant' in ii and ii['variant'] and '2 Jewels' in ii['variant']):
							continue
						uniques[ii['name']] = {'baseType': ii['baseType'], 'chaosValue': ii['chaosValue']}

			else:
				print('Unhandled key: "{}"'.format(key))

		# Add all missing values to poe.ninja data
		fixmissingbases(bases, league)
		curvals = fixallmissing(league, currency, divs, essences, prophecy, scarab, uniques, helmenchants, fragments, challenges)

		gen_currency(currency, league, curvals)
		gen_gems(skillgem, league, curvals)
		gen_div(divs, league, curvals)
		gen_bases(bases, league, curvals)
#		gen_incubator(incubator, league, curvals)
		gen_essence(essences, league, curvals)
		gen_challenge(challenges, league, curvals)
		gen_prophecy(prophecy, league, curvals)
		gen_scarab(scarab, league, curvals)
		gen_unique(uniques, league, curvals)
		gen_enchants(helmenchants, league, curvals)
		gen_fragments(fragments, league, curvals)


if __name__ == '__main__':
	scrape_ninja()