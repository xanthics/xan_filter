#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Converts the json that was gathered from poe.ninja into usable filter rules
import json
from collections import defaultdict


# placeholder
def unique_preprocess(data, val, base_sound, currency_val, tiers, minval, auto_ah, ret):
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
		"Ngamahu's Sign", "Tasalio's Sign", "Tasalio's Sign",
		# Blight League
		"Badge of the Brotherhood", "Breathstealer", "Cowl of the Ceraunophile", "Cowl of the Cryophile", "Cowl of the Thermophile", "Icefang", "Machina Mitts", "Rotting Legion", "Sporeguard", "The Stampede", "Venopuncture",
		# Metamorph
		'Astral Projector', 'Fury Valve', "Mother's Embrace", "Warrior's Legacy",
		# Conqueror
		'Booming Populace', 'Hands of the High Templar', 'Irresistable Temptation', 'Leash of Oblation', 'Manastorm', 'Misinformation', 'Stalwart Defenders', 'Territories Unknown', 'Terror', 'The Black Cane', 'The Ivory Tower', 'The Saviour', 'Thread of Hope', 'War Among the Stars',
		# Delirium
		'Algor Mortis', 'Assailum', 'Beacon of Madness', 'One With Nothing', 'Perfidy', 'The Interrogation', "Kitava's Teachings", 'Voices',
		# Harvest
		'Abhorrent Interrogation', "Bear's Girdle", "Doryani's Prototype", "Emperor's Vigilance", 'Forbidden Shako', 'Law of the Wilds', 'Plume of Pursuit', 'Storm Secret', 'The Felbog Fang', 'The Immortal Will', 'The Shattered Divinity', 'The Surging Thoughts', "The Tempest's Liberation", "The Torrent's Reclamation", 'The Yielding Mortality', "Witchhunter's Judgment",
	]
	unique_list = defaultdict(list)
	unique_list_limited = defaultdict(list)
	set_of_bases = set()
	unique_cleaned = {}

	for item in data:
		if 'other' in data[item]:
			unique_cleaned[item] = data[item]
		else:
			set_of_bases.add(data[item]['baseexact'])
			if item.strip('*') in limiteddrop:
				unique_list_limited[data[item]['baseexact']].append(data[item]['value'])
			else:
				unique_list[data[item]['baseexact']].append(data[item]['value'])

	for base in set_of_bases:
		if base in unique_list and max(unique_list[base]) >= currency_val['high'] > min(unique_list[base]):
			unique_cleaned[base] = {'baseexact': base, 'value': -1}
		elif base in unique_list_limited and base in unique_list and (max(unique_list_limited[base]) >= currency_val['high'] > min(unique_list[base])
																	  or max(unique_list_limited[base]) >= currency_val['high'] > min(unique_list_limited[base])):
			unique_cleaned[base] = {'baseexact': base, 'value': -2}
		elif base in unique_list and base in unique_list_limited:
			unique_cleaned[base] = {'baseexact': base, 'value': min(unique_list[base] + unique_list_limited[base])}
		elif base in unique_list:
			unique_cleaned[base] = {'baseexact': base, 'value': min(unique_list[base])}
		else:
			unique_cleaned[base] = {'baseexact': base, 'value': min(unique_list_limited[base])}
	price_currency(unique_cleaned, val, base_sound, currency_val, tiers, minval, auto_ah, ret)


def price_currency(data, val, base_sound, currency_val, tiers, minval, auto_ah, ret):
	ah_list = ['Fossil', 'Resonator', 'Deafening', 'Shrieking', 'Screaming', 'Catalyst', "Delerium Orb", 'Splinter']
	stackable = ['Orb', 'Splinter', 'Chisel', 'Coin', 'Bauble', 'Sextant', 'Shard', 'Whetstone', 'Scroll', 'Scrap', "Essence", 'Fossil', 'Resonator', 'Primal', 'Vivid', 'Wild', 'Oil']
	for item in data:
		rule = True
		if item[0].isdigit() and item.split(' ', maxsplit=1)[0].isdigit():
			tval = int(item.split(' ', maxsplit=1)[0])
		else:
			tval = val
		# special rule for uniques with a low value drop and
		# -1 high value drop that is unrestricted
		# -2 high value drop that is limited
		if data[item]['value'] in [-1, -2]:
			data[item]['type'] = 'unique special' if data[item]['value'] == -1 else "unique limited"

		else:
			for ch in tiers:
				if data[item]['value'] >= currency_val[ch]:
					if ch == 'normal' and base_sound not in ['challenge']:
						rule = False
					if ch == 'low' and (item in auto_ah or (base_sound in ['currency', 'divination'] and any(substring in item for substring in ah_list))):
						data[item]['type'] = f'{base_sound} show'
					else:
						data[item]['type'] = ch if ch == 'mirror' else f'{base_sound} {ch}'
					break
			else:
				if item in auto_ah or (base_sound in ['currency', 'divination'] and any(substring in item for substring in ah_list)):
					data[item]['type'] = f'{base_sound} show'
				elif minval == 'hide':
					if 'currency' == base_sound:
						ret[f'{tval - 1} {item}'] = data[item].copy()
						ret[f'{tval - 1} {item}']['type'] = 'show level'
						ret[f'{tval - 1} {item}']['other'] = ["AreaLevel <= 67"]
					data[item]['type'] = 'hide'
				elif minval == 'show':
					data[item]['type'] = f'{base_sound} {tiers[-1]}'
				elif minval == 'ignore':
					continue
			# A stackable item.  Generate all valid stack breakpoints
			# This won't get called if minval for currency is ignore
			if base_sound in ['currency', 'challenge'] and val == 1 and any(stack in item for stack in stackable) and tiers[0] not in data[item]['type']:
				counter = 9999
				prev = data[item]['type'].split(' ', maxsplit=1)[1] if " " in data[item]['type'] else data[item]['type']
				idx = len(tiers) - 2 if prev not in tiers else tiers.index(prev) - 1
				maxval = 20
				if item == "Perandus Coin":
					maxval = 1000
				elif any([x in item for x in ['Primal', 'Vivid', 'Wild']]):
					maxval = 100
				elif "Splinter" in item:
					maxval = 99
				elif "Essence" in item:
					maxval = 9
				elif "Fossil" in item:
					maxval = 20
				elif any([x in item for x in ["Resonator", "Delirium Orb", "Oil"]]):
					maxval = 10
				elif item in ["Orb of Transmutation", "Scroll of Wisdom", "Portal Scroll", "Armourer's Scrap", "Orb of Regret"]:
					maxval = 40
				elif item in ["Orb of Augmentation", "Orb of Scouring", "Silver Coin"]:
					maxval = 30
				elif item in ["Chaos Orb", "Orb of Alchemy", "Regal Orb", "Divine Orb", "Vaal Orb", "Simple Sextant", "Prime Sextant", "Awakened Sextant"]:
					maxval = 10
				for i in range(2, maxval+1):
					if data[item]['value'] * i >= currency_val[tiers[idx]]:
						ret[f'{tval - 1}{counter-i} {item}'] = data[item].copy()
						if idx == 0:
							ret[f'{tval - 1}{counter-i} {item}']['type'] = f'mirror'
						else:
							ret[f'{tval - 1}{counter-i} {item}']['type'] = f'{base_sound} {tiers[idx]}'
						if 'other' in []:
							ret[f'{tval - 1}{counter - i} {item}']['other'].extend([f"StackSize >= {i}"])
						else:
							ret[f'{tval - 1}{counter-i} {item}']['other'] = [f"StackSize >= {i}"]
						idx -= 1
					if idx <= 0:
						break

		# del data[item]['value']  # unused later, delete makes a smaller object, but unnecessary.
		if rule:
			ret[f'{tval} {item}'] = data[item]


def convert_json_to_filter():
	ret = {}
	packs = [
		# json blob, priority, filter base rules, pricing funct, acceptable tiers, hide/ignore/show below min
		# Following classes have defaults for normal in show_catchall:
		# Map Fragments, Currency(also prophecy, oil, etc), Divination Card, Incubator, Unique, Helm Enchant, Misc Map Items
		['currency', 1, 'currency', price_currency, ['mirror', 'extremely high', 'very high', 'high', 'normal', 'low'], 'hide'],
		['currency_strict', 1, 'currency', price_currency, ['mirror', 'extremely high', 'very high', 'high', 'normal'], 'hide'],
		['incubator', 7, 'currency', price_currency, ['mirror', 'extremely high', 'very high', 'high', 'normal'], 'hide'],
		['div', 2, 'divination', price_currency, ['mirror', 'extremely high', 'very high', 'high', 'normal', 'low'], 'show'],
		['fragment', 5, 'fragment', price_currency, ['mirror', 'extremely high', 'very high', 'high', 'normal', 'low'], 'show'],
		['prophecy', 8, 'currency', price_currency, ['mirror', 'extremely high', 'very high', 'high', 'normal', 'low'], 'show'],
		['enchant', 3, 'base', price_currency, ['mirror', 'extremely high', 'very high'], 'ignore'],
		['base', 4, 'base', price_currency, ['mirror', 'extremely high', 'very high'], 'ignore'],
		['gems', 6, 'gem', price_currency, ['mirror', 'extremely high', 'very high', 'high'], 'ignore'],
		['unique', 9, 'unique', unique_preprocess, ['mirror', 'extremely high', 'very high', 'high', 'normal', 'low'], 'show'],
		['challenge_stack', 1, 'challenge', price_currency, ['mirror', 'extremely high', 'very high', 'high', 'normal', 'low'], 'show'],
	]
	# initialize pricing tiers
	with open(f'autogen/currency.json', 'r') as f:
		data = json.load(f)
	currency_val = {
		'mirror': data['Mirror of Kalandra']['value'] // 20,
		'extremely high': data['Exalted Orb']['value'],
		'very high': data['Exalted Orb']['value'] // 10,
		'high': 5,
		'normal': 7 / 8,
		'low': 1 / 8,
	}
	# initialize always highlight list
	with open(f'autogen/always_highlight.json', 'r') as f:
		auto_ah = json.load(f)

	for blob, val, base_sound, funct, tiers, minval in packs:
		with open(f'autogen/{blob}.json', 'r') as f:
			data = json.load(f)
		funct(data, val, base_sound, currency_val, tiers, minval, auto_ah, ret)
	return ret
