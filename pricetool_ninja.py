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
		tier = 'currency very low'
		#tier = 'hide'

	if stacks > 1:
		return "$ {0}\": {{\"base\": \"{0}\", 'other': ['StackSize >= {2}'], \"class\": \"Currency\", \"type\": \"{1}\"}}".format(cur, tier, stacks)
	return "1 {0}\": {{\"base\": \"{0}\", \"class\": \"Currency\", \"type\": \"{1}\"}}".format(cur, tier)


# given a league grouped list of currency determine all unique entries and then output for each league
def gen_currency(currency_list, league):
	stackable = ['Orb', 'Splinter', 'Chisel', 'Coin', 'Bauble', 'Sextant', 'Shard', 'Whetstone', 'Scroll', 'Scrap']

	defaults = {"Mirror of Kalandra": 28558.18, "Blessing of Chayula": 179.76, "Exalted Orb": 119.03, "Ancient Orb": 30.5, "Harbinger's Orb": 27.0, "Divine Orb": 19.68, "Orb of Annulment": 11.5, "Blessing of Uul-Netol": 6.0,
				"Blessing of Esh": 5.0, "Master Cartographer's Sextant": 4.0, "Blessing of Xoph": 3.0, "Journeyman Cartographer's Sextant": 2.9, "Blessing of Tul": 2.0, "Vaal Orb": 1.73,
				"Apprentice Cartographer's Sextant": 1.37, "Gemcutter's Prism": 1.34, "Splinter of Chayula": 1.32, "Orb of Horizons": 0.9, "Orb of Regret": 0.75, "Engineer's Orb": 0.66,
				"Orb of Alchemy": 0.57, "Regal Orb": 0.53, "Cartographer's Chisel": 0.46, "Orb of Scouring": 0.43, "Splinter of Xoph": 0.42, "Orb of Fusing": 0.38, "Orb of Binding": 0.38, "Silver Coin": 0.19,
				"Blessed Orb": 0.16, "Chromatic Orb": 0.14, "Splinter of Uul-Netol": 0.13, "Perandus Coin": 0.12, "Splinter of Esh": 0.12, "Orb of Chance": 0.1, "Orb of Alteration": 0.09, "Jeweller's Orb": 0.09,
				"Glassblower's Bauble": 0.08, "Splinter of Tul": 0.08, "Orb of Augmentation": 0.04, "Blacksmith's Whetstone": 0.03, "Armourer's Scrap": 0.03, "Orb of Transmutation": 0.02, "Portal Scroll": 0.02,
				"Prime Chaotic Resonator": 334.79, "Prime Alchemical Resonator": 330.29, "Potent Chaotic Resonator": 1.27, "Powerful Chaotic Resonator": 1.0, "Primitive Chaotic Resonator": 0.5, "Potent Alchemical Resonator": 0.5,
				"Primitive Alchemical Resonator": 0.39, "Powerful Alchemical Resonator": 0.38, "Faceted Fossil": 180.0, "Glyphic Fossil": 180.0, "Bloodstained Fossil": 176.68, "Hollow Fossil": 170.0, "Fractured Fossil ": 169.0,
				"Tangled Fossil": 166.64, "Sanctified Fossil": 30.27, "Encrusted Fossil": 29.99, "Gilded Fossil": 19.0, "Shuddering Fossil": 7.0, "Enchanted Fossil": 4.0, "Serrated Fossil": 4.0, "Perfect Fossil": 3.0,
				"Prismatic Fossil": 2.97, "Jagged Fossil": 2.65, "Dense Fossil": 2.0, "Lucent Fossil": 2.0, "Aetheric Fossil": 1.81, "Pristine Fossil": 1.58, "Bound Fossil": 1.0, "Metallic Fossil": 1.0,
				"Corroded Fossil": 1.0, "Scorched Fossil": 0.35, "Frigid Fossil": 0.23, "Aberrant Fossil": 0.18, "Scroll of Wisdom": 1 / 100, }

	shards = {'Binding Shard': 'Orb of Binding', 'Horizon Shard': 'Orb of Horizons', 'Harbinger\'s Shard': 'Harbinger\'s Orb', 'Engineer\'s Shard': 'Engineer\'s Orb', 'Ancient Shard': 'Ancient Orb',
	          'Regal Shard': 'Regal Orb', 'Alchemy Shard': 'Orb of Alchemy', 'Alteration Shard': 'Orb of Alteration', 'Transmutation Shard': 'Orb of Transmutation', 'Scroll Fragment': 'Scroll of Wisdom',
			  'Exalted Shard': 'Exalted Orb', 'Annulment Shard': 'Orb of Annulment', 'Mirror Shard': 'Mirror of Kalandra'}

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
			elif cur in shards:
				val = (currency_list[shards[cur]] if shards[cur] in currency_list else defaults[shards[cur]]) / 20
			else:
				val = defaults[cur]

			retstr = currencyclassify(cur, val, curvals)
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
		if v not in c_list:
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
	defaults = {"House of Mirrors": 3145.43, "Beauty Through Death": 881.51, "The Doctor": 583.25, "The Fiend": 368.99, "The Immortal": 286.14, "The Spark and the Flame": 159.04,
				"Hunter's Reward": 141.25, "The Samurai's Eye": 100.0, "Immortal Resolve": 83.37, "The Queen": 81.58, "The Wolven King's Bite": 80.0, "Abandoned Wealth": 70.0,
				"The Iron Bard": 65.0, "Mawr Blaidd": 61.44, "The Celestial Stone": 50.0, "The Mayor": 44.0, "Wealth and Power": 40.24, "The Dragon's Heart": 37.83, "The Vast": 27.82,
				"The Undaunted": 24.61, "The Saint's Treasure": 22.63, "Boon of the First Ones": 20.82, "The Professor": 20.0, "The Sephirot": 18.0, "Pride Before the Fall": 17.81,
				"The King's Heart": 15.0, "The Wolf": 15.0, "The Hunger": 14.28, "The Artist": 12.34, "Heterochromia": 10.0, "The Hoarder": 9.0, "The Master": 9.0,
				"The Celestial Justicar": 8.0, "The Hale Heart": 8.0, "The Enlightened": 7.64, "The Breach": 7.0, "The Valkyrie": 6.85, "The Undisputed": 6.65, "The Void": 6.38,
				"The Valley of Steel Boxes": 6.0, "Perfection": 6.0, "Chaotic Disposition": 5.45, "The Last One Standing": 5.19, "The Polymath": 5.0, "Left to Fate": 5.0,
				"The Ethereal": 4.66, "The Thaumaturgist": 4.05, "Bowyer's Dream": 4.0, "Last Hope": 4.0, "The Cartographer": 4.0, "The Risk": 4.0, "The Throne": 4.0, "The Wind": 4.0,
				"The Porcupine": 4.0, "The Dreamer": 4.0, "Time-Lost Relic": 3.75, "Lucky Deck": 3.0, "The Dapper Prodigy": 3.0, "The Inventor": 3.0, "The Warlord": 3.0, "Rebirth": 3.0,
				"The Obscured": 3.0, "The World Eater": 3.0, "The Twilight Moon": 3.0, "The Endless Darkness": 3.0, "The Price of Protection": 3.0, "The Innocent": 2.98,
				"Emperor of Purity": 2.0, "Humility": 2.0, "Scholar of the Seas": 2.0, "The Brittle Emperor": 2.0, "The Dark Mage": 2.0, "The Jester": 2.0, "The Wretched": 2.0,
				"Lingering Remnants": 2.0, "The Jeweller's Boon": 2.0, "The Wilted Rose": 2.0, "The Chains that Bind": 1.95, "The Offering": 1.82, "The Traitor": 1.71, "The Standoff": 1.5}

	for u in set(defaults.keys()) - set(div_list.keys()):
		div_list[u] = defaults[u]

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
							if level == 86:
								f.write(u'\t"{4} {2}{0}": {{"base": "{0}", "other": [{1}"ItemLevel >= {3}"], "type": "{5}"}},\n'.format(baseType, '"{}Item True", '.format(variant) if variant else '', variant + ' ' if variant else '', level, count, value))
							else:
								f.write(u'\t"{4} {2}{0}": {{"base": "{0}", "other": [{1}"ItemLevel {3}"], "type": "{5}"}},\n'.format(baseType, '"{}Item True", '.format(variant) if variant else '', variant + ' ' if variant else '', level, count, value))
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

	# Minimum number of item that must exist on poe.ninja for it to be considered
	mincount = 8

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

			else:
				for i in data:
					for ii in data[i]:
						if ii['count'] < mincount:
							continue
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