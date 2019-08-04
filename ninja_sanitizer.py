#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
# Enforces certain rules on prices returned from poe.ninja, such as divinations being capped at a fraction of the price of their output item (I'm looking at you "The Witch" and "Kiara's Determination")
# Also adds missing values

from item_config.gen_item_lists import highbases
from ninja_defaults import currencydefaults, essencedefaults, prophecydefaults, divdefaults, uniquedefaults, scarabdefaults, helmenchantsdefaults, basedefaults, fragmentdefaults, challengesdefaults, cardlookup, knowncards


# Helper function to find missing items and print a list of them
def fixmissing(ninja_list, defaults, league, name):
	# Print all items that were returned by poe.ninja that don't have a default set
	if set(ninja_list.keys()) - set(defaults.keys()):
		missing = ', '.join(['"{}": {}'.format(x, ninja_list[x]) for x in sorted(set(ninja_list.keys()) - set(defaults.keys()))])
		print(f"{league} Missing defaults for {name}: \n{missing}\n")
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
	goodbases = highbases()
	missingstr = ""
	for level in sorted(bases, reverse=True):
		for variant in ['Elder', 'Shaper', None]:
			if variant not in basedefaults[level]:
				print(f'Missing base default for {level}\n"{variant}": {{}}')
			if variant not in bases[level]:
				bases[level][variant] = {}
			if not set(goodbases[variant]).issubset(set(basedefaults[level][variant].keys())):
				missingstr += f"bases ({level}-{variant}) missing values for {set(goodbases[variant]) - set(basedefaults[level][variant].keys())}\n"
			fixmissing(bases[level][variant], basedefaults[level][variant], league, f"bases ({level}-{variant})")
	if missingstr:
		print(missingstr)


def lessthan(a, b):
	return a < b


def greaterthanequal(a, b):
	return a >= b


# Sanity check for item prices
# Will be updated as I notice discrepancies
def price_sanity(item_list, curvals):
	lessthanmin = ['The Web', 'The Incantation', 'Shard of Fate', 'The Endurance', "Anarchy's Price", "The Dragon", "Doedre's Madness", "The Wolverine"]
	lessthanlow = ["Blacksmith's Whetstone", "Armourer's Scrap", "Orb of Chance", "Orb of Transmutation", "The Hermit"]
	lessthannormal = ["The Scholar", "Her Mask", "The Gambler", "Jeweller's Orb", "Silver Coin", "Chromatic Orb", "Blessed Orb"]
	lessthanhigh = []
	lessthanvery = []
	lessthanextremely = []

	atleastnormal = ["Orb of Alteration", 'Orb of Alchemy', "Orb of Scouring", "Cartographer's Chisel", "Orb of Binding"]
	atleasthigh = ["Ancient Orb", "Exalted Shard", "Master Cartographer's Sextant", "Journeyman Cartographer's Sextant", "Apprentice Cartographer's Sextant"]
	atleastvery = ["Divine Orb", "Orb of Annulment", "Harbinger's Orb"]
	atleastextremely = ["Mirror of Kalandra", "Mirror Shard", "The Doctor", "House of Mirrors", "The Fiend", "The Nurse", "Alluring Bounty", "The Spark and the Flame", "Pride of the First Ones", "Beauty Through Death", "Immortal Resolve", "The Immortal"]

	lookupmapping = [
		(lessthanmin, curvals['min'] * .95, lessthan),
		(lessthanlow, curvals['low'] * .95, lessthan),
		(lessthannormal, curvals['normal'] * .95, lessthan),
		(lessthanhigh, curvals['high'] * .95, lessthan),
		(lessthanvery, curvals['very'] * .95, lessthan),
		(lessthanextremely, curvals['extremely'] * .95, lessthan),

		(atleastnormal, curvals['normal'], greaterthanequal),
		(atleasthigh, curvals['high'], greaterthanequal),
		(atleastvery, curvals['very'], greaterthanequal),
		(atleastextremely, curvals['extremely'], greaterthanequal),
	]

	for item in item_list:
		for items, val, funct in lookupmapping:
			if not items:
				continue
			if item in items and not funct(item_list[item], val):
				item_list[item] = val
				break


# Helper function to tier items based on value of ex
def gentierval(currencies):
	ret = {'extremely': currencies['Exalted Orb'],
		   'very': currencies['Exalted Orb'] // 10,
		   'show high': 5,  # Used for uniques, essences, divination, fragments, incubators, prophecy, scarabs
		   'high': 1,
		   'normal': 1/4,
		   'low': 1/8,
		   'min': 1/16}
	return ret


# Collapse uniques list so that it is base:value pairs, with -1 for "special" bases and -2 for "only boss drop is valuable" bases
def compact_uniques(unique_full_list, curvals):
	# drops that are restricted to specific areas or leagues
	# limited highlighting is only used if the only high drops are limited and there is at least 1 low drop
	limiteddrop = [
		# Guardians, Shaper, and Elder
		"Obscurantis", "The Brass Dome", "The Scourge", "Razor of the Seventh Sun", "Slivertongue", "Brain Rattler", "Snakepit", "Eye of Innocence",
		"Voidwalker", "Shaper's Touch", "Starforge", "Dying Sun",
		"Leper's Alms", "Memory Vault", "Vulconus", "Beltimber Blade", "Grelwood Shank", "Augyre", "Yoke of Suffering", "Gloomfang",
		"Blasphemer's Grasp", "Shimmeron", "Nebuloch", "Hopeshredder", "Impresence", "Cyclopean Coil",
		"Indigon", "The Eternity Shroud", "Disintegrator", "Voidforge", "Mark of the Elder", "Mark of the Shaper", "Voidfletcher",
		"Watcher's Eye",
		# Atziri
		"Atziri's Step", "Doryani's Catalyst", "Doryani's Invitation", "Atziri's Promise",
		"The Vertex", "Atziri's Splendour", "Atziri's Acuity", "Atziri's Disfavour",
		# Bestiary League
		"Saqawal's Flock", "Saqawal's Nest", "Saqawal's Talons", "Saqawal's Winds",
		"Fenumus' Toxins", "Fenumus' Shroud", "Fenumus' Spinnerets", "Fenumus' Weave",
		"Craiceann's Chitin", "Craiceann's Carapace", "Craiceann's Tracks", "Craiceann's Pincers",
		"Farrul's Bite", "Farrul's Fur", "Farrul's Chase", "Farrul's Pounce",
		# Pale Court
		"Mind of the Council", "Grip of the Council", "Breath of the Council", "Reach of the Council",
		"Eber's Unification", "Yriel's Fostering", "Inya's Epiphany", "Volkuur's Guidance",
		# Pillars of Arun
		"Gorgon's Gaze",
		# Doryani's Machinarium
		"Doryani's Delusion",
		# Talisman League
		"Rigwald's Savagery", "Rigwald's Command", "Rigwald's Crest", "Rigwald's Quills", "Night's Hold", "Rigwald's Curse", "Blightwell", "Natural Hierarchy", "Eyes of the Greatwolf", "Feastbind", "Faminebind",
		# Incursion League
		"String of Servitude", "Apep's Slumber", "Mask of the Spirit Drinker", "Dance of the Offered", "Architect's Hand", "Story of the Vaal", "Sacrificial Heart", "Coward's Chains", "Soul Catcher", "Tempered Flesh", "Tempered Spirit", "Tempered Mind",
		# Synthesis League
		"Bottled Faith", "Perepiteia", "Mask of the Tribunal", "Garb of the Ephemeral", "Offering to the Serpent", "Storm's Gift", "Nebulis", "Circle of Guilt", "Circle of Regret", "Circle of Fear", "Circle of Anguish", "Circle of Nostalgia", "Maloney's Mechanism",
		# Labyrinth
		"Glitterdisc", "Viper's Scales", "Death's Door", "Winds of Change", "Izaro's Dilemma", "Chitus' Needle", "Spine of the First Claimant", "Xirgil's Crank", "Izaro's Turmoil",
		# Breach League
		"The Anticipation", "Esh's Mirror", "The Formless Flame", "Skin of the Loyal", "The Snowblind Grace", "The Infinite Pursuit", "The Infinite Pursuit", "	Hand of Thought and Motion", "Severed in Sleep", "Xoph's Inception", "Uul-Netol's Kiss", "Xoph's Heart", "The Halcyon", "Voice of the Storm",
		"The Red Dream", "The Green Dream", "The Blue Dream",
		# Legion League
		"Rathpith Globe", "Wreath of Phrecia", "Maw of Conquest", "Honourhome", "Voll's Protector", "Lioneye's Paws", "March of the Legion", "Maligaro's Virtuosity", "Asenath's Gentle Touch", "Aukuna's Will", "Divinarius", "Al Dhih", "Rebuke of the Vaal", "Lavianga's Wisdom", "Sign of the Sin Eater", "Darkscorn", "Pledge of Hands", "Kaom's Primacy",
		"Marohi Erqi", "Tavukai", "The Sorrow of the Divine", "Glorious Vanity", "Militant Faith", "Brutal Restraint", "Elegant Hubris", "Lethal Pride",
		# Abyss League
		"Lightpoacher", "Shroud of the Lightless", "Bubonic Trail", "Tombfist", "Darkness Enthroned",
		# Delve League
		"Hale Negator", "Crown of the Tyrant", "Command of the Pit", "Cerberus Limb", "Aul's Uprising", "Doryani's Machinarium",
		"Putembo's Valley", "Putembo's Mountain", "Putembo's Meadow",
		"Uzaza's Meadow", "Uzaza's Mountain", "Uzaza's Valley",
		"Ahkeli's Mountain", "Ahkeli's Meadow", "Ahkeli's Valley",
		# Domination & Nemesis League
		"Berek's Grip", "Berek's Pass", "Berek's Respite", "Blood of the Karui", "Lavianga's Spirit",
		# Domination League
		"The Gull",
		# Nemesis League
		"Headhunter",
		# Ambush & Invasion League
		"Vaal Caress", "Voideye",
		# Anarchy & Onslaught League
		"Shavronne's Revelation", "Voll's Devotion",
		# Anarchy League
		"Gifts from Above", "Daresso's Salute",
		# Onslaught League
		"Death Rush", "Victario's Acuity",
		# Tempest League
		"Shadows and Dust", "Crown of the Pale King", "Trolltimber Spire", "Ylfeban's Trickery",
		# Warbands League
		"Brinerot Flag", "Brinerot Mark", "Brinerot Whalers", "Broken Faith", "Mutewind Pennant", "Mutewind Seal", "Mutewind Whispersteps", "Redblade Band", "Redblade Banner", "Redblade Tramplers", "Steppan Eard", "The Pariah",
		# Betrayal League
		"Bitterbind Point", "The Devouring Diadem", "The Queen's Hunger", "Cinderswallow", "Paradoxica", "The Crimson Storm", "The Crimson Storm", "Hyperboreus",
		# Torment League
		"Brutus' Lead Sprinkler", "Scold's Bridle", "The Rat Cage",
		# Perandus League
		"Seven-League Step", "Trypanon", "Umbilicus Immortalis", "Varunastra", "Zerphi's Last Breath",
		# Rampage League
		"Flesh and Spirit", "Null and Void", "Shadows and Dust",
		# Beyond League
		"Edge of Madness", "The Dark Seer", "The Harvest",
		# Bloodlines League
		"Ngamahu's Sign", "Tasalio's Sign", "Tasalio's Sign"
	]
	from collections import defaultdict
	unique_list = defaultdict(list)
	unique_list_limited = defaultdict(list)
	unique_clean = {}
	for name in unique_full_list:
		if name in limiteddrop:
			unique_list_limited[unique_full_list[name]['baseType']].append(unique_full_list[name]['chaosValue'])
		else:
			unique_list[unique_full_list[name]['baseType']].append(unique_full_list[name]['chaosValue'])
	for base in unique_list:
		# If map < show high or there is a high value base that is non-restricted that shares a base with any low value unique
		if ("Map" in base and min(unique_list[base]) < curvals['show high']) or min(unique_list[base]) < curvals['show high'] <= max(unique_list[base]) or (base in unique_list_limited and min(unique_list_limited[base]) < curvals['show high'] <= max(unique_list[base])):
			unique_clean[base] = -1
		# High value drop restricted unique that shares a base with a low value unrestricted base
		elif base in unique_list_limited and min(unique_list[base]) < curvals['show high'] <= max(unique_list_limited[base]):
			unique_clean[base] = -2
		else:
			unique_clean[base] = min(unique_list[base] + unique_list_limited[base]) if base in unique_list_limited else min(unique_list[base])

	for base in set(unique_list_limited.keys()) - set(unique_list.keys()):
		# High value drop restricted unique that shares a base with a low value unrestricted base
		if min(unique_list_limited[base]) < curvals['show high'] <= max(unique_list_limited[base]):
			unique_clean[base] = -2
		else:
			unique_clean[base] = min(unique_list_limited[base])

	return unique_clean


# Add missing values to data returned by poe.ninja
def fixallmissing(league, currency, divs, essences, prophecy, scarab, uniques, helmenchants, fragments, challenges):
	# Add chaos and Scroll of Wisdom to the default list as poe.ninja does not include them
	currencydefaults["Chaos Orb"] = 1
	currencydefaults["Scroll of Wisdom"] = 1 / 100
	fixmissing(currency, currencydefaults, league, "currency")
	fixmissing(challenges, challengesdefaults, league, 'challenges')
	fixmissing(essences, essencedefaults, league, 'essences')
	fixmissing(prophecy, prophecydefaults, league, 'prophecy')
	fixmissing(scarab, scarabdefaults, league, 'scarab')
	fixmissing(divs, divdefaults, league, 'Divination cards')
	fixmissing(uniques, uniquedefaults, league, 'uniques')
	# reverse engineer vial values based on difference from uniques + "opportunity cost"
	op_cost = 5
	currency["Vial of Awakening"] = uniques["Apep's Supremacy"]['chaosValue'] - uniques["Apep's Slumber"]['chaosValue'] - op_cost  # currency['Exalted Orb'] * 2
	currency["Vial of Consequence"] = uniques["Coward's Legacy"]['chaosValue'] - uniques["Coward's Chains"]['chaosValue'] - op_cost  # 3
	currency["Vial of Dominance"] = uniques["Slavedriver's Hand"]['chaosValue'] - uniques["Architect's Hand"]['chaosValue'] - op_cost  # 1
	currency["Vial of Fate"] = uniques["Fate of the Vaal"]['chaosValue'] - uniques["Story of the Vaal"]['chaosValue'] - op_cost  # 1/5
	currency["Vial of Summoning"] = uniques["Mask of the Stitched Demon"]['chaosValue'] - uniques["Mask of the Spirit Drinker"]['chaosValue'] - op_cost  # 1/5
	currency["Vial of the Ritual"] = uniques["Omeyocan"]['chaosValue'] - uniques["Dance of the Offered"]['chaosValue'] - op_cost  # 1/4

	currency["Vial of Transcendence"] = (uniques["Transcendent Mind"]['chaosValue'] + uniques["Transcendent Flesh"]['chaosValue'] + uniques["Transcendent Spirit"]['chaosValue'])/3 - \
										(uniques["Tempered Mind"]['chaosValue'] + uniques["Tempered Flesh"]['chaosValue'] + uniques["Tempered Spirit"]['chaosValue'])/3 - op_cost  # 1/2

	currency["Vial of the Ghost"] = uniques["Soul Ripper"]['chaosValue'] - uniques["Soul Catcher"]['chaosValue'] - op_cost  # currency['Exalted Orb'] * 8
	currency["Vial of Sacrifice"] = uniques["Zerphi's Heart"]['chaosValue'] - uniques["Sacrificial Heart"]['chaosValue'] - op_cost  # currency['Exalted Orb'] * 18

	for vial in ["Vial of Awakening", "Vial of Consequence", "Vial of Dominance", "Vial of Fate", "Vial of Summoning", "Vial of the Ritual", "Vial of Transcendence", "Vial of the Ghost", "Vial of Sacrifice"]:
		currency[vial] = currency[vial] if currency[vial] > 0 else 0

	fixmissing(helmenchants, helmenchantsdefaults, league, "helmet enchants")
	fixmissing(fragments, fragmentdefaults, league, "Fragments")

	# Sanity check for ex value
	currency['Exalted Orb'] = 80 if currency['Exalted Orb'] < 80 else currency['Exalted Orb']
	curvals = gentierval(currency)
	for item_list in [currency, divs]:
		price_sanity(item_list, curvals)

	# Overwrite values for some cards based on what they give
	for typ, table in [("uniqueitem", uniques)]:
		for card in cardlookup[typ]:
			current = cardlookup[typ][card]
			divs[card] = table[current['lookup']]['chaosValue'] * current['factor']

	for typ, table in [("currencyitem", currency), ("prophecy", prophecy), ("divination", divs)]:
		for card in cardlookup[typ]:
			current = cardlookup[typ][card]
			divs[card] = table[current['lookup']] * current['factor']

	# Check for new cards in poe.ninja data
	missingcards = set(divs.keys()) - set(knowncards)
	if missingcards:
		print(f"New cards found without default mappings: {missingcards}")

	# list of all uniques that can only be acquired through upgrades or vendor recipes to remove them from unique price consideration
	upgraded = [
		# Fated Uniques
		'Kaltensoul', 'Thirst for Horrors', 'Atziri\'s Reflection', 'The Oak', 'Ezomyte Hold', 'Frostferno', 'Martyr\'s Crown', 'Asenath\'s Chant', 'Deidbellow',
		'Malachai\'s Awakening', 'Wall of Brambles', 'Wildwrap', 'Fox\'s Fortune', 'Crystal Vault', 'Windshriek', 'Greedtrap', 'Shavronne\'s Gambit', 'Duskblight',
		'Sunspite', 'Hrimburn', 'Doedre\'s Malevolence', 'Amplification Rod', 'Corona Solaris', 'Sanguine Gambol', 'The Gryphon', 'Dreadsurge', 'Dreadbeak', 'Cameria\'s Avarice',
		'Silverbough', 'The Tempest', 'Doomfletch\'s Prism', 'Death\'s Opus', 'Mirebough', 'Realm Ender', 'The Stormwall', 'The Cauteriser', 'Queen\'s Escape', 'The Dancing Duo',
		'Hrimnor\'s Dirge', 'Panquetzaliztli', 'Geofri\'s Devotion', 'Voidheart', 'Kaom\'s Way', 'Winterweave', 'Timetwist', 'Ngamahu Tiki', 'Karui Charge', 'The Effigon',
		'The Tactician', 'The Nomad', 'The Signal Fire', 'Cragfall', 'Hyrri\'s Demise', 'Chaber Cairn', 'Geofri\'s Legacy', 'The Iron Fortress', 'Whakatutuki o Matua',
		# Vendor recipes
		'The Anima Stone', 'Arborix', 'Duskdawn', 'The Goddess Scorned', 'The Goddess Unleashed', 'Kingmaker', 'Magna Eclipsis', 'The Retch', 'Star of Wraeclast', 'The Taming',
		'The Vinktar Square', 'Loreweave',
		#  incursion uniques from upgrades
		'Transcendent Flesh', 'Transcendent Mind', 'Transcendent Spirit', 'Soul Ripper', 'Slavedriver\'s Hand', 'Coward\'s Legacy', 'Omeyocan', 'Fate of the Vaal', 'Mask of the Stitched Demon',
		'Apep\'s Supremacy', 'Zerphi\'s Heart', 'Shadowstitch',
		# Upgraded Breach Uniques
		'Xoph\'s Nurture', 'The Formless Inferno', 'Xoph\'s Blood', 'Tulfall', 'The Perfect Form', 'The Pandemonius', 'Hand of Wisdom and Action', 'Esh\'s Visage', 'Choir of the Storm',
		'Uul-Netol\'s Embrace', 'The Red Trail', 'The Surrender', 'United in Dream', 'Skin of the Lords', 'Presence of Chayula', 'The Red Nightmare', 'The Green Nightmare', 'The Blue Nightmare',
		# Harbinger Uniques -- Currently only drops as pieces
		"The Flow Untethered", "The Fracturing Spinner", "The Tempest's Binding", "The Rippling Thoughts", "The Enmity Divine", "The Unshattered Will",
		# Special uniques that would skew their basetype value and are handled elsewhere in show.py
		'Tabula Rasa'
	]
	for uni in upgraded:
		if uni in uniques:
			del uniques[uni]

	return curvals, compact_uniques(uniques, curvals)
