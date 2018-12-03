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
				"Corroded Fossil": 1.0, "Scorched Fossil": 0.35, "Frigid Fossil": 0.23, "Aberrant Fossil": 0.18, "Scroll of Wisdom": 1 / 100, "Eternal Orb": 19323.88}

	shards = {'Binding Shard': 'Orb of Binding', 'Horizon Shard': 'Orb of Horizons', 'Harbinger\'s Shard': 'Harbinger\'s Orb', 'Engineer\'s Shard': 'Engineer\'s Orb', 'Ancient Shard': 'Ancient Orb',
	          'Regal Shard': 'Regal Orb', 'Alchemy Shard': 'Orb of Alchemy', 'Alteration Shard': 'Orb of Alteration', 'Transmutation Shard': 'Orb of Transmutation', 'Scroll Fragment': 'Scroll of Wisdom',
			  'Exalted Shard': 'Exalted Orb', 'Annulment Shard': 'Orb of Annulment', 'Mirror Shard': 'Mirror of Kalandra'}

	for s in shards:
		defaults[s] = defaults[shards[s]] / 20

	fixmissing(currency_list, defaults, league, "currency")

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
	defaults = {"Deafening Essence of Anguish": 1.0, "Screaming Essence of Loathing": 0.68, "Wailing Essence of Suffering": 0.55, "Deafening Essence of Woe": 4.0,
				"Weeping Essence of Contempt": 0.65, "Muttering Essence of Sorrow": 0.43, "Shrieking Essence of Contempt": 2.0, "Deafening Essence of Spite": 6.0,
				"Shrieking Essence of Zeal": 3.0, "Weeping Essence of Hatred": 0.55, "Deafening Essence of Fear": 4.0, "Shrieking Essence of Loathing": 1.0,
				"Wailing Essence of Contempt": 0.51, "Shrieking Essence of Woe": 1.0, "Deafening Essence of Rage": 4.0, "Deafening Essence of Greed": 7.0,
				"Screaming Essence of Scorn": 0.55, "Deafening Essence of Doubt": 1.0, "Deafening Essence of Wrath": 4.0, "Deafening Essence of Suffering": 1.0,
				"Screaming Essence of Envy": 1.0, "Screaming Essence of Suffering": 0.43, "Weeping Essence of Wrath": 0.38, "Muttering Essence of Woe": 0.38,
				"Wailing Essence of Woe": 0.63, "Shrieking Essence of Wrath": 1.0, "Shrieking Essence of Misery": 1.0, "Weeping Essence of Anger": 0.55,
				"Wailing Essence of Zeal": 0.38, "Shrieking Essence of Doubt": 1.0, "Screaming Essence of Anger": 1.0, "Essence of Hysteria": 19.0,
				"Wailing Essence of Greed": 0.47, "Deafening Essence of Sorrow": 2.0, "Deafening Essence of Hatred": 2.0, "Deafening Essence of Contempt": 10.0,
				"Wailing Essence of Anger": 0.54, "Essence of Insanity": 18.0, "Shrieking Essence of Scorn": 3.0, "Shrieking Essence of Envy": 2.0,
				"Screaming Essence of Sorrow": 0.59, "Screaming Essence of Hatred": 0.87, "Wailing Essence of Loathing": 0.68, "Deafening Essence of Dread": 6.0,
				"Deafening Essence of Misery": 4.0, "Deafening Essence of Envy": 9.0, "Screaming Essence of Spite": 0.55, "Shrieking Essence of Suffering": 0.92,
				"Muttering Essence of Torment": 0.38, "Muttering Essence of Hatred": 0.38, "Wailing Essence of Doubt": 0.38, "Muttering Essence of Anger": 0.48,
				"Weeping Essence of Suffering": 0.38, "Screaming Essence of Dread": 0.97, "Remnant of Corruption": 4.0, "Screaming Essence of Anguish": 0.55,
				"Deafening Essence of Scorn": 8.08, "Muttering Essence of Fear": 0.38, "Weeping Essence of Greed": 0.53, "Deafening Essence of Loathing": 3.0,
				"Shrieking Essence of Dread": 4.92, "Screaming Essence of Zeal": 0.53, "Wailing Essence of Torment": 0.55, "Shrieking Essence of Rage": 1.32,
				"Screaming Essence of Greed": 0.85, "Shrieking Essence of Anguish": 1.0, "Wailing Essence of Wrath": 0.55, "Screaming Essence of Misery": 0.55,
				"Screaming Essence of Woe": 0.55, "Wailing Essence of Spite": 0.38, "Wailing Essence of Anguish": 0.5, "Shrieking Essence of Hatred": 1.0,
				"Screaming Essence of Rage": 0.53, "Wailing Essence of Fear": 0.38, "Muttering Essence of Greed": 0.55, "Weeping Essence of Torment": 0.83,
				"Screaming Essence of Fear": 0.46, "Screaming Essence of Contempt": 0.55, "Shrieking Essence of Anger": 3.0, "Deafening Essence of Anger": 7.0,
				"Screaming Essence of Torment": 0.43, "Shrieking Essence of Greed": 2.0, "Wailing Essence of Sorrow": 0.55, "Weeping Essence of Rage": 0.55,
				"Screaming Essence of Wrath": 0.57, "Wailing Essence of Rage": 0.42, "Deafening Essence of Torment": 2.0, "Weeping Essence of Sorrow": 0.38,
				"Shrieking Essence of Torment": 1.0, "Whispering Essence of Woe": 0.38, "Whispering Essence of Greed": 0.55, "Weeping Essence of Fear": 0.38,
				"Whispering Essence of Contempt": 0.38, "Weeping Essence of Doubt": 0.55, "Whispering Essence of Hatred": 0.5, "Wailing Essence of Hatred": 0.38,
				"Essence of Delirium": 9.0, "Deafening Essence of Zeal": 8.0, "Shrieking Essence of Sorrow": 1.0, "Shrieking Essence of Fear": 1.0,
				"Essence of Horror": 69.0, "Weeping Essence of Woe": 0.4, "Shrieking Essence of Spite": 1.99, "Screaming Essence of Doubt": 0.55,
				"Muttering Essence of Contempt": 0.38}

	fixmissing(essence_list, defaults, league, 'essences')

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
	# sort based on descending length so that any additional substrings are at the end of the list
	return sorted(set(badcards), reverse=True, key=lambda s: len(s))


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
	defaults = {"House of Mirrors": 3276.71, "Beauty Through Death": 903.92, "The Doctor": 564.95, "The Fiend": 406.76, "The Spark and the Flame": 225.98,
				"Hunter's Reward": 208.13, "Mawr Blaidd": 191.83, "The Immortal": 169.27, "The Wolven King's Bite": 156.35, "The Samurai's Eye": 141.98,
				"Immortal Resolve": 102.27, "The Queen": 80.0, "The Iron Bard": 75.0, "Abandoned Wealth": 64.74, "The Celestial Stone": 59.04, "Wealth and Power": 49.33,
				"The Vast": 40.0, "The Dragon's Heart": 33.46, "Chaotic Disposition": 30.0, "The Hale Heart": 30.0, "The Mayor": 30.0, "The Wolf": 24.76,
				"The Professor": 24.26, "Boon of the First Ones": 24.0, "The Saint's Treasure": 22.0, "Perfection": 22.0, "The Sephirot": 19.27, "The Endless Darkness": 18.71,
				"The Undaunted": 18.0, "The Undisputed": 17.08, "The Wind": 15.22, "The Jester": 14.55, "The Artist": 14.2, "Heterochromia": 14.0, "The Master": 13.2,
				"Pride Before the Fall": 13.0, "The Thaumaturgist": 12.0, "The World Eater": 12.0, "The King's Heart": 11.76, "The Last One Standing": 10.0, "The Valkyrie": 10.0,
				"Time-Lost Relic": 10.0, "The Hoarder": 9.89, "The Polymath": 9.25, "Last Hope": 9.0, "The Celestial Justicar": 9.0, "The Brittle Emperor": 8.23,
				"The Dreamer": 8.0, "Left to Fate": 7.72, "The Wilted Rose": 7.1, "The Enlightened": 7.03, "The Hunger": 7.0, "The Void": 6.6, "Merciless Armament": 6.38,
				"Blessing of God": 6.17, "The Cartographer": 6.1, "The Risk": 6.0, "The Valley of Steel Boxes": 5.63, "Bowyer's Dream": 5.25, "The Ethereal": 5.0,
				"The Formless Sea": 5.0, "The Standoff": 5.0, "The Porcupine": 5.0, "The Breach": 5.0, "The Price of Protection": 4.67, "The Dapper Prodigy": 4.6,
				"Lucky Deck": 4.59, "The Innocent": 4.0, "Harmony of Souls": 3.9, "Birth of the Three": 3.0, "Emperor of Purity": 3.0, "The Dark Mage": 3.0, "The Admirer": 3.0,
				"The Twilight Moon": 2.93, "Humility": 2.82, "The Offering": 2.63, "The Spoiled Prince": 2.33, "The Throne": 2.04, "Scholar of the Seas": 2.0, "The Avenger": 2.0,
				"The Body": 2.0, "The Chains that Bind": 2.0, "The Conduit": 2.0, "The Fletcher": 2.0, "The Inventor": 2.0, "The Penitent": 2.0, "The Soul": 2.0, "The Surveyor": 2.0,
				"The Traitor": 2.0, "The Tyrant": 2.0, "The Wrath": 2.0, "Treasure Hunter": 2.0, "Vinia's Token": 2.0, "The Wretched": 2.0, "Lingering Remnants": 2.0,
				"Atziri's Arsenal": 2.0, "Rebirth": 2.0, "The Obscured": 2.0, "The Dreamland": 2.0, "Gemcutter's Promise": 1.94, "The Union": 1.85, "The Jeweller's Boon": 1.78,
				"No Traces": 1.74, "The Cursed King": 1.58, "Jack in the Box": 1.57, "The Sword King's Salute": 1.31, "Lysah's Respite": 1.16, "The Rite of Elements": 1.06,
				"Glimmer of Hope": 1.01, "Assassin's Favour": 1.0, "Audacity": 1.0, "Blind Venture": 1.0, "Boundless Realms": 1.0, "Coveted Possession": 1.0,
				"Dialla's Subjugation": 1.0, "Doedre's Madness": 1.0, "Earth Drinker": 1.0, "Emperor's Luck": 1.0, "Gift of the Gemling Queen": 1.0, "Hope": 1.0, "Hubris": 1.0,
				"Hunter's Resolve": 1.0, "Light and Truth": 1.0, "Lost Worlds": 1.0, "Lucky Connections": 1.0, "Rain Tempter": 1.0, "Rats": 1.0, "The Aesthete": 1.0,
				"The Calling": 1.0, "The Cataclysm": 1.0, "The Demoness": 1.0, "The Drunken Aristocrat": 1.0, "The Encroaching Darkness": 1.0, "The Explorer": 1.0, "The Fox": 1.0,
				"The Gambler": 1.0, "The Gemcutter": 1.0, "The Gentleman": 1.0, "The Gladiator": 1.0, "The Harvester": 1.0, "The Lion": 1.0, "The Lord in Black": 1.0,
				"The Mercenary": 1.0, "The Oath": 1.0, "The One With All": 1.0, "The Pack Leader": 1.0, "The Pact": 1.0, "The Poet": 1.0, "The Rabid Rhoa": 1.0, "The Road to Power": 1.0,
				"The Scavenger": 1.0, "The Siren": 1.0, "The Stormcaller": 1.0, "The Sun": 1.0, "The Survivalist": 1.0, "The Tower": 1.0, "The Trial": 1.0, "The Visionary": 1.0,
				"The Warlord": 1.0, "Tranquillity": 1.0, "Mitts": 1.0, "Call to the First Ones": 1.0, "The Wolverine": 1.0, "The Garish Power": 1.0, "The Forsaken": 1.0,
				"The Blazing Fire": 1.0, "The Realm": 1.0, "The Deceiver": 1.0, "Forbidden Power": 1.0, "Three Voices": 1.0, "The Army of Blood": 1.0, "The Beast": 1.0,
				"The Fathomless Depths": 1.0, "The Witch": 1.0, "The Darkest Dream": 1.0, "The Cacophony": 1.0, "The Dragon": 0.96, "The Eye of the Dragon": 0.96, "The Catalyst": 0.95,
				"The Coming Storm": 0.91, "The Arena Champion": 0.9, "The Battle Born": 0.89, "The Puzzle": 0.87, "The Insatiable": 0.87, "The Inoculated": 0.86, "Might is Right": 0.84,
				"The Surgeon": 0.78, "The Watcher": 0.77, "The Feast": 0.75, "The Twins": 0.68, "Dying Anguish": 0.62, "Struck by Lightning": 0.62, "Three Faces in the Dark": 0.6,
				"The Endurance": 0.58, "Grave Knowledge": 0.56, "Volatile Power": 0.49, "Shard of Fate": 0.4, "The Summoner": 0.4, "The Web": 0.4, "The Wolf's Shadow": 0.4,
				"The King's Blade": 0.39, "Turn the Other Cheek": 0.39, "Her Mask": 0.38, "Rain of Chaos": 0.38, "The Sigil": 0.38, "The Ruthless Ceinture": 0.38, "Prosperity": 0.37,
				"The Doppelganger": 0.37, "The Incantation": 0.36, "The Lunaris Priestess": 0.36, "The Warden": 0.35, "A Mother's Parting Gift": 0.34, "Anarchy's Price": 0.34,
				"Cartographer's Delight": 0.34, "Death": 0.34, "Destined to Crumble": 0.34, "Lantador's Lost Love": 0.34, "Loyalty": 0.34, "The Betrayal": 0.34, "The Carrion Crow": 0.34,
				"The Flora's Gift": 0.34, "The Hermit": 0.34, "The Lich": 0.34, "The Lover": 0.34, "The Metalsmith's Gift": 0.34, "The Scarred Meadow": 0.34, "The Scholar": 0.34,
				"Thunderous Skies": 0.34, "The Opulent": 0.34,
				'The Nurse': 70.61, 'A Dab of Ink': 10.0, 'The Sacrifice': 5.0, 'The Life Thief': 107.86, 'The Master Artisan': 0.5}

	fixmissing(div_list, defaults, league, 'Divination cards')

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
	defaults = {"Overgrown Shrine Map": [2.28], "Woodsplitter": [0.34], "Titan Gauntlets": [61.1, 0.75], "Golden Hoop": [4343.43], "Blue Pearl Amulet": [1.0], "Gavel": [35.0, 0.34],
				"Opal Sceptre": [1.0], "Sanctified Life Flask": [49.22], "Karui Maul": [0.34], "Enameled Buckler": [0.66], "Iron Ring": [7.41, 1.0, 1.0], "Elegant Ringmail": [44.77, 2.0],
				"Grand Mana Flask": [225.98], "Widowsilk Robe": [103.99, 1.02, 0.34], "Agate Amulet": [76.0, 0.95, 0.38, 0.34], "Hallowed Hybrid Flask": [3.0], "Torture Chamber Map": [3.72],
				"Royal Axe": [677.94], "Sage Wand": [9.1, 0.34], "Wyrmscale Doublet": [37.41], "Shore Map": [17.0], "Gold Ring": [19.0, 3.0], "Slink Boots": [112.99, 1.0],
				"Crusader Boots": [436.68], "Archon Kite Shield Piece": [19.9, 9.79, 9.5, 3.89], "Topaz Flask": [35.0, 17.06, 15.0, 12.38], "Supreme Spiked Shield": [0.34],
				"Exquisite Leather": [47.02, 24.17, 22.44, 1.0], "Titanium Spirit Shield": [1.15], "Bone Bow": [1.0], "Opal Wand": [1.0], "Chain Belt": [225.98, 15.54, 5.0, 4.72, 1.0, 0.34],
				"Conjurer Gloves": [1.0], "Dunes Map": [1.0], "Scholar Boots": [0.34], "Coiled Staff": [2.0, 1.0], "Strapped Mitts": [10.63, 0.34], "Ebony Tower Shield": [112.99, 0.34],
				"Spiked Club": [0.34], "Siege Axe": [19.1], "Midnight Blade": [90.4, 5.0, 3.0], "Quartz Wand": [0.34], "Fright Claw": [0.34], "Citadel Bow": [3.2],
				"Carnal Armour": [10397.43, 162.34, 0.34], "Ambusher": [0.68], "Despot Axe": [45.0, 0.34], "Antique Rapier": [0.34], "Hydrascale Gauntlets": [112.99], "Plague Mask": [0.34],
				"Stygian Vise": [1.0], "Headsman Axe": [0.34], "Gnarled Branch": [0.34, 0.21], "Callous Mask Piece": [40.0, 30.18, 8.91], "Deerskin Gloves": [0.68], "Tomahawk": [0.34],
				"Gilded Sallet": [0.34], "Sorcerer Boots": [677.94, 1.0], "Scholar's Robe": [0.34], "Sledgehammer": [0.34], "Blinder": [1.0], "Harbinger Bow": [2.0, 0.34],
				"Vaal Spirit Shield": [896.59, 7.09], "Prophecy Wand": [276.94], "Platinum Kris": [0.34], "Vaal Gauntlets": [1807.84, 1.0], "Ornate Mace": [0.34], "Boot Blade": [0.34],
				"Mosaic Kite Shield": [1.0], "Ambush Mitts": [102.63], "Sapphire Flask": [59.99], "Sinner Tricorne": [1.0], "Opal Ring": [50.0, 3.0], "Legion Boots": [0.44],
				"Shadow Axe": [0.39], "Long Bow": [0.53], "Bronze Sceptre": [0.34], "Dread Maul": [0.3], "Great Mallet": [5.93, 0.34], "Arcanist Slippers": [60.0], "Spiraled Wand": [0.68, 0.34],
				"Engraved Wand": [1.0], "Jasper Chopper": [4.59], "Royal Staff": [0.34], "Basket Rapier": [0.34], "Great Helmet": [0.34], "Sharkskin Tunic": [19.33],
				"Jade Amulet": [66.6, 40.0, 1.0, 0.34], "Etched Greatsword": [1.0], "Coronal Leather": [1.0], "Compound Spiked Shield": [0.34], "Buckskin Tunic": [0.33],
				"Corrugated Buckler": [1.0], "Primordial Staff": [0.34], "Saintly Chainmail": [4.81, 0.96], "Painted Tower Shield": [1.0], "Ancient Spirit Shield": [19.79], "Leather Cap": [1.08],
				"Desert Brigandine": [0.75], "Iron Sceptre": [1.0], "Boot Knife": [0.34], "Hubris Circlet": [135.7, 111.99, 2.97, 2.0], "Silken Hood": [76.0, 3.96], "Ritual Sceptre": [30.0],
				"Temple Map": [12.6], "Promenade Map": [8.69], "Plank Kite Shield": [0.34], "Carnal Boots": [338.97], "Diamond Flask": [1.0], "Throat Stabber": [1.0], "Short Bow": [1.0],
				"Ranger Bow": [3.0, 0.63], "Wool Gloves": [0.68], "Reinforced Greaves": [1.0], "Dream Mace": [0.34], "Serpentine Staff": [0.36], "Gut Ripper": [0.34, 0.34], "Golden Buckler": [0.56],
				"Velvet Slippers": [0.34], "Iron Circlet": [0.34], "Goat's Horn": [0.34], "War Hammer": [1.0, 0.34], "Rotfeather Talisman": [156.17], "Shadow Sceptre": [1.0, 0.22],
				"Spidersilk Robe": [0.69, 0.34], "Silk Gloves": [0.34], "Quartz Flask": [2902.9, 2818.5, 1.9, 0.34], "Triumphant Lamellar": [1.0], "Wyrmscale Gauntlets": [0.34], "Bismuth Flask": [10.0],
				"Iron Hat": [0.34], "Stealth Boots": [25.0, 0.37], "Reaver Sword": [0.96, 0.35], "Lacquered Garb": [15.0, 1.0], "Rotted Round Shield": [0.34], "Cleaver": [0.34],
				"Brass Spirit Shield": [0.71], "Judgement Staff": [4.0, 1.0], "Blunt Arrow Quiver": [30.0, 1.0], "Bronze Gauntlets": [0.34], "Plate Vest": [0.34], "Stiletto": [0.34],
				"Turquoise Amulet": [8.58, 1.0, 0.65, 0.34], "Destiny Leather": [3.0], "Ezomyte Staff": [131.35, 0.34], "Flaying Knife": [0.34], "Assassin's Garb": [1.0], "Harlequin Mask": [451.96, 112.99],
				"Carnal Mitts": [338.97, 0.47], "War Sword": [1.0], "Ornate Ringmail": [0.34], "Ezomyte Axe": [0.34], "Conjurer Boots": [1.0], "Marble Amulet": [0.84], "Vaal Axe": [158.66, 10.0, 0.39],
				"Goliath Gauntlets": [1.0], "Cloth Belt": [169.48, 0.4, 0.34, 0.34, 0.34], "Hydrascale Boots": [25.26], "Magistrate Crown": [97.29, 54.8], "Steel Ring": [19.18], "Golden Mantle": [1694.85],
				"Steel Gauntlets": [1.0], "Steelscale Gauntlets": [146.89, 7.99, 1.0], "Auric Mace": [0.85], "Rawhide Boots": [318.97],
				"Viridian Jewel": [3137.53, 523.21, 399.31, 302.36, 70.0, 60.0, 50.0, 28.0, 18.61, 16.22, 7.67, 4.8, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.8, 0.8, 0.77, 0.42, 0.39, 0.34, 0.34, 0.34, 0.34, 0.34, 0.34, 0.34, 0.34, 0.34, 0.34, 0.34, 0.34, 0.34, 0.34],
				"Iron Mask": [0.34], "Chain Gloves": [0.4], "Praetor Crown": [2.0, 1.0, 0.34], "Destroyer Regalia": [2.31], "Two-Point Arrow Quiver": [1388.65, 0.99, 0.34], "Maelström Staff": [36.57, 1.0],
				"Paua Amulet": [7317.91, 4.34, 1.0, 0.34], "Coral Amulet": [267.91, 0.34], "Astral Plate": [2.3], "Steelhead": [5.05], "Broadhead Arrow Quiver": [1.0], "Full Scale Armour": [1.0],
				"Golden Plate": [225.98, 1.0], "Ironscale Gauntlets": [2.0], "Callous Mask": [112.99], "Paua Ring": [35.41, 1.0, 1.0], "Holy Chainmail": [0.18], "Decimation Bow": [0.34], "Death Bow": [0.36, 0.34],
				"Assassin Bow": [19.34, 3.0, 0.34], "Royal Skean": [0.34], "Conquest Chainmail": [0.34], "Spike-Point Arrow Quiver": [1.0, 0.68], "Pinnacle Tower Shield": [18.61, 2.0], "Visored Sallet": [0.34],
				"Crusader Chainmail": [0.34], "Ancient Greaves": [1.0], "Samite Helmet": [0.34], "Cedar Tower Shield": [5.0], "Imperial Staff": [12.6, 2.0, 2.0, 2.0, 1.97], "Ivory Spirit Shield": [0.34],
				"Demon Dagger": [1.0], "Reinforced Tower Shield": [0.34], "Lapis Amulet": [112.99, 45.14, 0.86, 0.34, 0.34], "Deicide Mask": [10.0], "Pine Buckler": [0.34], "Bastard Sword": [0.34], "Estoc": [0.34],
				"Eternal Sword": [5.15, 4.0, 2.35], "Ornate Sword": [0.34], "Murder Mitts": [1.32, 1.0], "Karui Sceptre": [1.0], "Occultist's Vestment": [22.64, 20.0], "Strapped Boots": [0.34], "War Buckler": [0.34],
				"Ironscale Boots": [0.34], "Wool Shoes": [1.0], "Void Axe": [30.0], "Baroque Round Shield": [0.34], "Museum Map": [125.44], "Wrapped Mitts": [0.34], "Diamond Ring": [10.0, 1.0],
				"Crusader Plate": [0.98, 0.91], "Sharkskin Boots": [1.0], "Samite Gloves": [0.34], "Coral Ring": [1.0, 1.0, 0.99], "Vaal Claw": [1.0, 0.77],
				"Onyx Amulet": [338.97, 325.86, 225.98, 69.76, 51.46, 40.0, 28.62, 28.13, 20.58, 6.51, 1.0], "Slaughter Knife": [1.0], "Nubuck Gloves": [10.0], "Bone Crypt Map": [1.82], "Goathide Boots": [115.6, 1.0],
				"Ezomyte Blade": [0.34], "Savant's Robe": [5.0], "Imbued Wand": [0.34], "Titan Greaves": [16.38, 5.0], "Rusted Sword": [0.34], "Strapped Leather": [0.28], "Burnished Spiked Shield": [1.0],
				"Nightmare Bascinet": [4.97, 1.0], "Studded Belt": [3.0, 0.34], "Heavy Quiver": [112.99], "Sulphur Flask": [0.4, 0.34], "Legion Gloves": [130.28], "Lion Sword": [1.0], "Dusk Blade": [0.37],
				"Murder Boots": [626.73, 3.0, 1.0], "Glorious Plate": [100.96], "Carved Wand": [112.99, 0.34], "Amethyst Ring": [3.66, 1.67], "Strand Map": [1.0], "Serpentscale Boots": [0.81],
				"Vaal Hatchet": [1.0], "Full Wyrmscale": [5.9], "Vine Circlet": [0.34], "Blood Raiment": [40.0], "Dragonscale Gauntlets": [0.34], "Bronzescale Gauntlets": [1.0, 0.34],
				"Amber Amulet": [564.95, 535.26, 19.48, 0.34], "Royal Burgonet": [6.36], "Silk Slippers": [0.32], "Raven Mask": [4.21], "Fiend Dagger": [5.0, 1.0], "Goliath Greaves": [44.46, 1.0],
				"Varnished Coat": [2.0], "Terror Maul": [1.0], "Prismatic Jewel": [509.02, 122.39, 108.57], "Skinning Knife": [0.22], "Poleaxe": [0.34], "Vanguard Belt": [2.0], "Arcanist Gloves": [22.68],
				"Soldier Boots": [0.87], "Royal Bow": [0.34], "Vaal Pyramid Map": [10.0], "Grinning Fetish": [0.87], "Imperial Claw": [8.18, 2.65, 1.0], "Jade Hatchet": [0.34], "Cemetery Map": [4.0],
				"Mesh Boots": [0.34], "Prophet Crown": [5.0, 0.34, 0.34], "Unset Ring": [124.68, 16.4, 8.61, 5.0, 4.95, 4.0, 4.0, 2.0, 1.0], "Ezomyte Tower Shield": [169.19, 78.07], "Highland Blade": [0.34],
				"Elegant Sword": [20.0, 0.72], "Riveted Boots": [0.34], "Soldier Helmet": [0.34], "Penetrating Arrow Quiver": [16.57, 5.0], "Harmonic Spirit Shield": [0.4], "Cardinal Round Shield": [3.0],
				"Void Sceptre": [3.0, 0.34], "Tornado Wand": [16.11, 3.0, 1.36], "Meatgrinder": [1.0], "Rock Breaker": [1.0], "Vaal Sceptre": [20.0, 3.0], "Infernal Sword": [196.75, 112.99, 1.0], "Full Dragonscale": [0.34],
				"Greatwolf Talisman": [824.11], "Military Staff": [0.34], "Festival Mask": [1.0], "Courtyard Map": [23.5], "Tarnished Spirit Shield": [1.0, 0.34], "Long Staff": [27.23, 0.34], "Labrys": [2.0],
				"Tiger Sword": [1.0], "Iron Staff": [1.0, 0.32], "Crusader Helmet": [13.82], "Dragonscale Boots": [0.71], "Chiming Spirit Shield": [0.34], "Serpentscale Gauntlets": [4.0], "Deerskin Boots": [0.34],
				"Great Crown": [25.0, 1.0, 0.34], "Gemstone Sword": [83.79], "Variscite Blade": [23.89], "Spine Bow": [2.0, 1.0], "Sorcerer Gloves": [1.0], "Cloth Belt Piece": [27.68, 4.75], "Lacquered Helmet": [0.4],
				"Simple Robe": [0.34], "Cutthroat's Garb": [0.68], "Twilight Blade": [0.34], "Jagged Maul": [0.34], "Granite Flask": [4.0, 2.0], "Sage's Robe": [1.0, 0.34], "Siege Helmet": [1.0], "Gladius": [0.93],
				"Whalebone Rapier": [1.0], "Karui Chopper": [0.34], "Brass Maul": [0.34], "Vaal Mask": [20.0], "Gladiator Plate": [9.53], "Aventail Helmet": [0.48], "Topaz Ring": [100.0, 1.66], "Jewelled Foil": [20.0],
				"Shackled Boots": [9.47], "Lunaris Circlet": [0.34], "Bronzescale Boots": [0.34], "Lion Pelt": [2.0], "Prismatic Ring": [564.95, 7.33, 1.0], "Jagged Foil": [0.34], "Abyssal Axe": [2.95],
				"Moonstone Ring": [204.38, 1.0, 1.0, 1.0], "Quicksilver Flask": [0.34], "Clasped Boots": [0.34], "Clasped Mitts": [29.24], "Studded Round Shield": [0.3], "Stibnite Flask": [189.74, 2.27],
				"Leather Belt": [4632.59, 1.0, 1.0, 1.0, 0.62, 0.34], "Citrine Amulet": [25.0, 10.0], "Sundering Axe": [0.34], "Polished Spiked Shield": [1.0], "Harbinger Map": [108.63], "Nailed Fist": [0.34],
				"Nubuck Boots": [5.0], "Trapper Boots": [1.0], "Crude Bow": [0.34], "Painted Buckler": [0.33], "Underground River Map": [1.76], "Platinum Sceptre": [2.0], "Sadist Garb": [25.0, 1.0], "Close Helmet": [3.0],
				"Nightmare Mace": [50.0], "Demon's Horn": [0.34], "Hellion's Paw": [8.8], "Ancient Gauntlets": [2.0], "Zodiac Leather": [5.0, 1.0], "Iron Gauntlets": [2.0], "Cutlass": [451.96, 5.0], "Terror Claw": [5.0, 1.0],
				"Infernal Axe": [0.34], "Vaal Regalia": [1.0], "Sharktooth Arrow Quiver": [0.34], "Necropolis Map": [2.0], "Golden Mask": [0.34], "Vaal Buckler": [0.34], "Fire Arrow Quiver": [0.34], "Moon Temple Map": [27.66],
				"Necromancer Silks": [1.0], "Regicide Mask": [3.0, 0.41], "Velvet Gloves": [0.34], "Colossal Tower Shield": [0.89], "Corsair Sword": [4.2], "Assassin's Mitts": [0.34, 0.34], "Necromancer Circlet": [59.36, 0.34],
				"Elder Sword": [1.0], "Rawhide Tower Shield": [35.0], "Serrated Arrow Quiver": [0.34], "Thresher Claw": [0.34], "Sanctified Mana Flask": [29.03], "Copper Plate": [0.34], "Atoll Map": [0.98], "Elegant Foil": [1.0],
				"Wild Leather": [0.34], "Ruby Flask": [130.0, 1.0], "Clutching Talisman": [96.53], "Cursed Crypt Map": [4.0], "Legion Sword": [56.44, 0.39], "Recurve Bow": [0.34], "Gold Amulet": [68.37, 10.0, 2.1, 1.26, 0.34],
				"Crimson Jewel": [650.75, 338.97, 184.26, 112.99, 73.68, 65.36, 58.0, 25.24, 24.0, 19.0, 15.53, 8.0, 5.0, 1.73, 1.23, 1.01, 1.0, 1.0, 1.0, 1.0, 0.91, 0.87, 0.82, 0.8, 0.68, 0.68, 0.68, 0.66, 0.46, 0.4, 0.38, 0.34, 0.34, 0.34, 0.34, 0.34, 0.34, 0.34],
				"Archon Kite Shield": [28.88, 10.0, 5.39, 5.0, 3.31], "Laminated Kite Shield": [1.0], "Wereclaw Talisman": [36.33], "Lathi": [0.79], "Heavy Belt": [5.0, 4.81, 1.37, 1.0, 1.0, 1.0, 1.0, 1.0, 0.79],
				"Assassin's Boots": [112.99], "Champion Kite Shield": [5.7], "Vaal Blade": [20.0, 0.34], "Imperial Skean": [10.0, 0.34], "Ezomyte Burgonet": [10.0], "Leather Hood": [1.0], "Ruby Amulet": [65.05],
				"Bone Circlet": [0.29], "Branded Kite Shield": [0.78], "Bone Armour": [2.0], "Secutor Helm": [0.34], "Zealot Gloves": [51.07, 31.96, 25.6], "Black Maw Talisman": [1.64], "Latticed Ringmail": [0.34],
				"Silver Flask": [2.0], "Greater Mana Flask": [0.34], "Two-Stone Ring": [528.93, 32.74, 30.0, 7.83, 3.7], "Sapphire Ring": [4.28, 3.02, 2.0, 1.0], "Satin Gloves": [30.93], "Sentinel Jacket": [0.34],
				"Decorative Axe": [0.34], "Thorium Spirit Shield": [5.0], "Ursine Pelt": [3.0], "Mind Cage": [18.96, 0.34], "Vile Staff": [0.34], "Zealot Helmet": [1.0], "Tribal Circlet": [0.34], "Imperial Bow": [130.0, 1.0],
				"Tricorne": [0.34], "Goathide Gloves": [1.0], "Eye Gouger": [0.96], "Blunt Arrow Quiver Piece": [30.0, 9.75], "Driftwood Wand": [1.0], "Sacrificial Garb": [20.25, 20.0, 20.0, 19.54, 15.79, 15.77],
				"Cobalt Jewel": [198.35, 112.99, 112.99, 50.74, 47.8, 24.79, 15.89, 15.0, 6.08, 3.56, 3.38, 2.0, 1.78, 1.76, 1.6, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.92, 0.88, 0.82, 0.71, 0.57, 0.34, 0.34, 0.34, 0.34, 0.34, 0.34, 0.34, 0.34],
				"Crusader Gloves": [15.0, 0.62], "Crystal Wand": [0.39], "Plated Greaves": [0.34], "Amethyst Flask": [1.0], "Jingling Spirit Shield": [8.0], "Timeworn Claw": [0.34], "Chateau Map": [190.86],
				"Carnal Sceptre": [40.0], "Imperial Maul": [30.0], "Highborn Staff": [6.34], "Sabre": [0.34], "Crystal Belt": [4.92], "Awl": [0.34], "Mirrored Spiked Shield": [0.9], "Large Hybrid Flask": [3.0],
				"Crystal Sceptre": [1.0, 0.34], "Ruby Ring": [8.0, 1.0, 1.0], "Shagreen Boots": [0.34], "Rustic Sash": [78.85, 25.0, 23.92, 0.34], "Soldier Gloves": [25.0, 1.0], "Blood Sceptre": [3.0], "Maze Map": [179.06],
				"Riveted Gloves": [40.0], "Golden Bracers": [12635.67], "Golden Wreath": [3954.65], "Golden Obi": [8128.36], "Cured Quiver": [0.72], "Jet Amulet": [4915.06], "Leatherscale Boots": [0.1]}

	fixmissing(unique_list, defaults, league, 'uniques')

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
		elif unique_list[u] > curvals['high']:
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