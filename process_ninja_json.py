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
	limiteddrop = {
		# Quest Items
		"Survival Instincts", "Survival Secrets", "Survival Skills", "Conqueror's Longevity", "Conqueror's Potency", "Conqueror's Efficiency",
		"Assassin's Haste", "Poacher's Aim", "Warlord's Reach",
		# Corruption only
		"Ancient Waystones", "Atziri's Reign", "Blood Sacrifice", "Brittle Barrier", "Chill of Corruption", "Combustibles", "Corrupted Energy",
		"Fragility", "Hungry Abyss", "Mutated Growth", "Pacifism", "Powerlessness", "Sacrificial Harvest", "Self-Flagellation", "Vaal Sentencing",
		"Weight of Sin", "Fevered Mind", 'Blood of Corruption', "Malachai's Vision",
		# Divination card only item
		'Maw of Mischief',
		# Fated Uniques
		"Amplification Rod", "Asenath's Chant", "Atziri's Reflection", "Cameria's Avarice", "Chaber Cairn", "Cragfall", "Death's Opus", "Doedre's Malevolence", "Doomfletch's Prism",
		"Dreadbeak", "Duskblight", "Frostferno", "Geofri's Devotion", "Geofri's Legacy", "Hrimburn", "Hyrri's Demise", "Kaom's Way", "Malachai's Awakening", "Queen's Escape",
		"The Cauteriser", "The Dancing Duo", "The Iron Fortress", "The Nomad", "The Signal Fire", "The Stormwall", "The Tactician", "The Tempest", "Thirst for Horrors", "Timetwist",
		"Whakatutuki o Matua", "Wildwrap", "Windshriek", "Winterweave",
		# Vendor recipes
		'The Anima Stone', 'Arborix', 'Duskdawn', 'The Goddess Scorned', 'The Goddess Unleashed', 'Kingmaker', 'Magna Eclipsis', 'The Retch', 'Star of Wraeclast', 'The Taming',
		'The Vinktar Square', 'Loreweave',
		# incursion uniques from upgrades
		'Transcendent Flesh', 'Transcendent Mind', 'Transcendent Spirit', 'Soul Ripper', 'Slavedriver\'s Hand', 'Coward\'s Legacy', 'Omeyocan', 'Fate of the Vaal', 'Mask of the Stitched Demon',
		'Apep\'s Supremacy', 'Zerphi\'s Heart',
		# incursion uniques
		'Sacrificial Heart', 'String of Servitude', 'Tempered Flesh', 'Tempered Mind', 'Tempered Spirit',
		'Shadowstitch', "Apep's Slumber", "Architect's Hand", "Coward's Chains", 'Dance of the Offered', 'Mask of the Spirit Drinker', 'Story of the Vaal',
		# Breach Uniques
		'Xoph\'s Nurture', 'The Formless Inferno', 'Xoph\'s Blood', 'Tulfall', 'The Perfect Form', 'The Pandemonius', 'Hand of Wisdom and Action', 'Esh\'s Visage', 'Choir of the Storm',
		'Uul-Netol\'s Embrace', 'The Red Trail', 'The Surrender', 'United in Dream', 'Skin of the Lords', 'Presence of Chayula', 'The Red Nightmare', 'The Green Nightmare', 'The Blue Nightmare',
		# Harbinger Uniques -- Currently only drops as pieces
		"The Flow Untethered", "The Fracturing Spinner", "The Tempest's Binding", "The Rippling Thoughts", "The Enmity Divine", "The Unshattered Will",
		# Harbinger Pieces
		"First Piece of Focus", "Second Piece of Focus", "Third Piece of Focus", "Fourth Piece of Focus",
		"First Piece of Directions", "Second Piece of Directions", "Third Piece of Directions",
		"First Piece of Storms", "Second Piece of Storms", "Third Piece of Storms",
		"First Piece of Time", "Second Piece of Time",
		"First Piece of Brutality", "Second Piece of Brutality", "Third Piece of Brutality",
		"First Piece of the Arcane", "Second Piece of the Arcane", "Third Piece of the Arcane",
		# upgraded harbinger uniques
		"The Torrent's Reclamation", "The Shattered Divinity", "The Tempest's Liberation", "The Surging Thoughts", "The Yielding Mortality", "The Immortal Will",
		# Guardians, Shaper, and Elder
		"Voidwalker", "Shaper's Touch", "Starforge", "Dying Sun", 'Solstice Vigil',
		"Blasphemer's Grasp", "Shimmeron", "Nebuloch", "Hopeshredder", "Impresence", "Cyclopean Coil",
		"Indigon", "The Eternity Shroud", "Disintegrator", "Voidforge", "Mark of the Elder", "Mark of the Shaper", "Voidfletcher", "Watcher's Eye",
		# Atziri
		"Atziri's Step", "Doryani's Catalyst", "Doryani's Invitation", "Atziri's Promise", "Atziri's Reflection",
		"The Vertex", "Atziri's Splendour", "Atziri's Acuity", "Atziri's Disfavour", "Pledge of Hands",
		# Maven
		"Arn's Anguish", "Graven's Secret", "Olesya's Delight", "Viridi's Veil", 'The Walls', 'The Claim', 'The Closest Peak', 'Atop the Atlas', 'The Vast Horizon', 'The Builder', 'Restless Cycles', 'The False Hope', 'Legacy of Fury',  'Doppelgänger Guise',
		# Bestiary League
		"Saqawal's Flock", "Saqawal's Nest", "Saqawal's Talons", "Saqawal's Winds",
		"Fenumus' Toxins", "Fenumus' Shroud", "Fenumus' Spinnerets", "Fenumus' Weave",
		"Craiceann's Chitin", "Craiceann's Carapace", "Craiceann's Tracks", "Craiceann's Pincers",
		"Farrul's Bite", "Farrul's Fur", "Farrul's Chase", "Farrul's Pounce",
		# Pillars of Arun
		"Gorgon's Gaze",
		# Doryani's Machinarium
		"Doryani's Delusion",
		# Synthesis League
		"Bottled Faith", "Perepiteia", "Mask of the Tribunal", "Garb of the Ephemeral", "Offering to the Serpent", "Storm's Gift", "Nebulis", "Circle of Guilt", "Circle of Regret", "Circle of Fear", "Circle of Anguish", "Circle of Nostalgia",
		# Labyrinth
		"Glitterdisc", "Viper's Scales", "Death's Door", "Winds of Change", "Izaro's Dilemma", "Chitus' Needle", "Spine of the First Claimant", "Xirgil's Crank", "Izaro's Turmoil",
		"Emperor's Might", "Emperor's Cunning", "Emperor's Wit", "Emperor's Mastery",
		# Breach League
		"The Anticipation", "Esh's Mirror", "The Formless Flame", "Skin of the Loyal", "The Snowblind Grace", "The Infinite Pursuit", "Hand of Thought and Motion", "Severed in Sleep", "Xoph's Inception", "Uul-Netol's Kiss", "Xoph's Heart", "The Halcyon", "Voice of the Storm",
		"The Red Dream", "The Green Dream", "The Blue Dream",
		# Abyss League
		"Lightpoacher", "Shroud of the Lightless", "Bubonic Trail", "Tombfist", "Darkness Enthroned",
		# Delve League
		"Command of the Pit", "Crown of the Tyrant", "Cerberus Limb", "Aul's Uprising", "Doryani's Machinarium", 'Hale Negator',
		"Putembo's Valley", "Putembo's Mountain", "Putembo's Meadow",
		"Uzaza's Meadow", "Uzaza's Mountain", "Uzaza's Valley",
		"Ahkeli's Mountain", "Ahkeli's Meadow", "Ahkeli's Valley",
		"Precursor's Emblem",
		# Betrayal League
		"Bitterbind Point", "The Devouring Diadem", "The Queen's Hunger", "Cinderswallow", "Paradoxica", "The Crimson Storm", "Hyperboreus", 'Vivinsect', "Cloak of Tawm'r Isley",
		# Blight League
		"Breathstealer", "Cowl of the Ceraunophile", "Cowl of the Cryophile", "Cowl of the Thermophile", "Sporeguard", "The Stampede",
		# Conqueror
		'Booming Populace', 'Hands of the High Templar', 'Irresistable Temptation', 'Misinformation', 'Stalwart Defenders', 'Territories Unknown', 'Terror', 'The Saviour', 'Thread of Hope', 'War Among the Stars',
		# Delirium
		'One With Nothing', 'The Interrogation', "Kitava's Teachings", 'Voices', 'Split Personality',
		# Harvest
		'Abhorrent Interrogation', "Bear's Girdle", 'Forbidden Shako', 'Law of the Wilds', 'Plume of Pursuit', 'The Felbog Fang',
		"Witchhunter's Judgment",
		# Heist
		'Fated End', "Leadership's Price", "The Admiral", "Chains of Emancipation", "The Fledgling", "Nadir Mode", "Apex Mode", "Font of Thunder", "Actum", "The Iron Mass", "The Hidden Blade", "The Fulcrum", "Expedition's End", "Crest of Desire", "Shattershard",
		# Warbands League
		"Brinerot Flag", "Brinerot Mark", "Brinerot Whalers", "Broken Faith", "Mutewind Pennant", "Mutewind Seal", "Mutewind Whispersteps", "Redblade Band", "Redblade Banner", "Redblade Tramplers", "Steppan Eard", "The Pariah",
		# Ritual
		"Blackflame", "Qotra's Regulator", "Rotblood Promise", "Survivor's Guilt", "Hands of the Fervent",
		# Ultimatum
		"Atziri's Rule", "Cane of Kulemak", "Glimpse of Chaos", "Hateforge", "Mahuxotl's Machination", "Relic of the Pact", "Steelworm", "Temptation Step", "The Scales of Justice", "Triumvirate Authority", "Yaomac's Accord",
		# Scourge
		"Stranglegasp", "Uul-Netol's Vow", "Stasis Prison",
		# Archnemesis
		# Seige of the Atlas
	}

	unique_list = defaultdict(list)
	unique_list_limited = defaultdict(list)
	unique_list_replica = defaultdict(list)
	set_of_bases = set()
	unique_cleaned = {}
	unique_cleaned_replica = {}

	for item in data:
		if 'other' in data[item]:
			unique_cleaned[item] = data[item]
		else:
			if item.startswith('Replica'):
				unique_list_replica[data[item]['baseexact']].append(data[item]['value'])
			else:
				set_of_bases.add(data[item]['baseexact'])
				if item.strip('*') in limiteddrop:
					unique_list_limited[data[item]['baseexact']].append(data[item]['value'])
				else:
					unique_list[data[item]['baseexact']].append(data[item]['value'])

	for base in set_of_bases:
		if base in unique_list and max(unique_list[base]) >= currency_val['high'] > min(unique_list[base]):
			unique_cleaned[base] = {'baseexact': base, 'value': -1}
		elif base in unique_list_limited and ((base in unique_list and max(unique_list_limited[base]) >= currency_val['high'] > max(unique_list[base])) or
											  (base not in unique_list and max(unique_list_limited[base]) >= currency_val['high'] > min(unique_list_limited[base]))):
			unique_cleaned[base] = {'baseexact': base, 'value': -2}
		elif base in unique_list and base in unique_list_limited:
			unique_cleaned[base] = {'baseexact': base, 'value': min(unique_list[base] + unique_list_limited[base])}
		elif base in unique_list:
			unique_cleaned[base] = {'baseexact': base, 'value': min(unique_list[base])}
		else:
			unique_cleaned[base] = {'baseexact': base, 'value': min(unique_list_limited[base])}
		unique_cleaned[base]['other'] = ['Replica False']

	for base in unique_list_replica:
		if max(unique_list_replica[base]) >= currency_val['high'] > min(unique_list_replica[base]):
			unique_cleaned_replica[base] = {'baseexact': base, 'value': -1}
		else:
			unique_cleaned_replica[base] = {'baseexact': base, 'value': min(unique_list_replica[base])}
		unique_cleaned_replica[base]['other'] = ['Replica True']

	price_currency(unique_cleaned, val, base_sound, currency_val, tiers, minval, auto_ah, ret)
	price_currency(unique_cleaned_replica, val, base_sound, currency_val, tiers, minval, auto_ah, ret)


def price_currency(data, val, base_sound, currency_val, tiers, minval, auto_ah, ret):
	ah_list = ['Fossil', 'Resonator', 'Deafening', 'Shrieking', 'Screaming', 'Catalyst', "Delerium Orb", 'Splinter']
	stackable = ['Orb', 'Splinter', 'Chisel', 'Coin', 'Bauble', 'Sextant', 'Shard', 'Whetstone', 'Scroll', 'Scrap', "Essence", 'Fossil', 'Resonator', 'Primal', 'Vivid', 'Wild', 'Oil', 'Marker']
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
						data[item]['type'] = f'{base_sound} {ch}'
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
				elif item == "Rogue's Marker":
					maxval = 50000
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
						ret[f'{tval - 1}{counter-i} {item}']['type'] = f'{base_sound} {tiers[idx]}'
						if 'other' in []:
							ret[f'{tval - 1}{counter - i} {item}']['other'].extend([f"StackSize >= {i}"])
						else:
							ret[f'{tval - 1}{counter-i} {item}']['other'] = [f"StackSize >= {i}"]
						idx -= 1
					if idx <= 0:
						break

		# del data[item]['value']  # unused later, delete makes a smaller object, but unnecessary.
		# We don't want rules for replica to overwrite non-replica
		if 'other' in data[item] and any(data[item]['other'][x] == 'Replica True' for x in range(len(data[item]['other']))):
			tval += 1
		if rule:
			ret[f'{tval} {item}'] = data[item]


def convert_json_to_filter():
	ret = {}
	packs = [
		# json blob, priority, filter base rules, pricing funct, acceptable tiers, hide/ignore/show below min
		# Following classes have defaults for normal in show_catchall:
		# Map Fragments, Currency(also oil, etc), Divination Card, Incubator, Unique, Helm Enchant, Misc Map Items
		['currency', 1, 'currency', price_currency, ['mirror', 'extremely high', 'very high', 'high', 'normal', 'low'], 'hide'],
		['currency_strict', 1, 'currency', price_currency, ['mirror', 'extremely high', 'very high', 'high', 'normal'], 'hide'],
		['incubator', 7, 'currency', price_currency, ['mirror', 'extremely high', 'very high', 'high', 'normal'], 'hide'],
		['div', 2, 'divination', price_currency, ['mirror', 'extremely high', 'very high', 'high', 'normal', 'low'], 'show'],
		['fragment', 5, 'fragment', price_currency, ['mirror', 'extremely high', 'very high', 'high', 'normal', 'low'], 'show'],
		['enchant', 3, 'show', price_currency, ['mirror', 'extremely high', 'very high'], 'ignore'],
		['base', 4, 'base', price_currency, ['mirror', 'extremely high', 'very high'], 'ignore'],
		['gems', 6, 'gem', price_currency, ['mirror', 'extremely high', 'very high', 'high'], 'ignore'],
		['unique', 9, 'unique', unique_preprocess, ['mirror', 'extremely high', 'very high', 'high', 'normal', 'low'], 'show'],
		['challenge_stack', 1, 'challenge', price_currency, ['mirror', 'extremely high', 'very high', 'high', 'normal', 'low'], 'show'],
	]
	# initialize pricing tiers
	with open(f'autogen/currency.json', 'r') as f:
		data = json.load(f)

	currency_val = {
		'mirror': data['Mirror of Kalandra']['value'] / 20,
		'extremely high': data['Exalted Orb']['value'],
		'very high': data['Exalted Orb']['value'] / 5 if data['Exalted Orb']['value'] / 5 >= 10 else 10,
		'high': data['Exalted Orb']['value'] / 10 if data['Exalted Orb']['value'] / 10 >= 5 else 5,
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
