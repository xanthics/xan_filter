#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.7.x or higher
# Given a json price blob from poe.ninja, removes unnecessary data and cleans up values
import json


# removes low count items, imports missing data from cache
def clean(price_val):
	# list of flat price data
	# gems and base are nested, need special handling
	base_items = ['currency', 'currency_strict', 'div', 'enchant', 'fragment', 'incubator', 'prophecy', 'unique', 'base', 'gems']
	# The minimum amount of an item that must exist in poe.ninja data to be considered a valid price
	min_thres = 10
	# load defaults
	with open('autogen/defaults.json', 'r') as f:
		defaults = json.load(f)

	for base in base_items:
		if base not in defaults:
			defaults[base] = {}
		default_keys = list(defaults[base])
		# queue for items to delete if the are < count and not in default
		del_ = []
		def_ = []
		for item in price_val[base]:
			if price_val[base][item]['count'] < min_thres:
				if item in default_keys:
					default_keys.remove(item)
					def_.append(item)
					price_val[base][item] = defaults[base][item]
				else:
					del_.append(item)
			else:
				del price_val[base][item]['count']
				defaults[base][item] = price_val[base][item]
#		if del_:
#			print(f'Discarding values for {base}: {del_}')
#		if def_:
#			print(f'Using default *{base}* value for: {def_}\n')
		for k in del_:
			del price_val[base][k]

	shards = {'Binding Shard': 'Orb of Binding', 'Horizon Shard': 'Orb of Horizons', 'Harbinger\'s Shard': 'Harbinger\'s Orb', 'Engineer\'s Shard': 'Engineer\'s Orb', 'Ancient Shard': 'Ancient Orb',
			  'Regal Shard': 'Regal Orb', 'Alchemy Shard': 'Orb of Alchemy', 'Alteration Shard': 'Orb of Alteration', 'Transmutation Shard': 'Orb of Transmutation',  # 'Scroll Fragment': 'Scroll of Wisdom',
			  'Chaos Shard': 'Chaos Orb', 'Exalted Shard': 'Exalted Orb', 'Annulment Shard': 'Orb of Annulment', 'Mirror Shard': 'Mirror of Kalandra'}

	for s in shards:
		if s not in price_val['currency'] and shards[s] in price_val['currency']:
			price_val['currency'][s] = {'baseexact': s, 'value': price_val['currency'][shards[s]]['value'] / 20}

	# save defaults
	with open('autogen/defaults.json', 'w') as f:
		json.dump(defaults, f, sort_keys=True, indent=2)


# TODO: Preprocess div cards (eg the gambler) so they can never make noise
# (sum-val)/sum*val -- to normalize
# sets the value of some divination cards based on their output
def fix_divs(price_val):
	# Lookup table for cards that produce specific items so that we can set their values manually
	# Used because cards for cheap items, such as The Witch, are typically "valued" several times higher than the actual item
	# Will not contain items that give multiple possible rewards, such as Jack in the Box.  Or highly variable items such as Ventor's Gamble
	cardlookup = {
		"uniqueitem": {
			"A Dab of Ink": {"lookup": "The Poet's Pen", "factor": 1 / 9},
			"A Mother's Parting Gift": {"lookup": "Fertile Mind", "factor": 1 / 6},
			"Anarchy's Price": {"lookup": "Voltaxic Rift", "factor": 1 / 13},
			"Audacity": {"lookup": "Doryani's Fist", "factor": 1 / 5},
			"Burning Blood": {"lookup": "Xoph's Blood", "factor": 1 / 6},
			"Dark Temptation": {"lookup": "Obliteration", "factor": 1 / 5},
			"Death": {"lookup": "Mon'tregul's Grasp", "factor": 1 / 4},
			"Echoes of Love": {"lookup": "Fidelitas' Spike", "factor": 1 / 3},
			"Forbidden Power": {"lookup": "Balefire", "factor": 1 / 4},
			"Humility": {"lookup": "Tabula Rasa", "factor": 1 / 9},
			"Hunter's Reward": {"lookup": "The Taming", "factor": 1 / 3},
	#		"Mawr Blaidd": {"lookup": "Eyes of the Greatwolf", "factor": 1/16},
			"Might is Right": {"lookup": "Trypanon", "factor": 1 / 9},
			"Pride Before the Fall": {"lookup": "Kaom's Heart", "factor": 1 / 8},
			"Pride of the First Ones": {"lookup": "Farrul's Fur", "factor": 1 / 7},
			"Rats": {"lookup": "Rat's Nest", "factor": 1 / 8},
#			"Scholar of the Seas": {"lookup": "Mao Kun", "factor": 1 / 7},
			"The Army of Blood": {"lookup": "Bloodbond", "factor": 1 / 6},
			"The Avenger": {"lookup": "Mjölner", "factor": 1 / 12},
			"The Beast": {"lookup": "Belly of the Beast", "factor": 1 / 6},
			"The Betrayal": {"lookup": "Maligaro's Virtuosity", "factor": 1 / 9},
			"The Blazing Fire": {"lookup": "Chin Sol", "factor": 1 / 6},
			"The Brittle Emperor": {"lookup": "Voll's Devotion", "factor": 1 / 8},
			"The Coming Storm": {"lookup": "Lightning Coil", "factor": 1 / 8},
			"The Conduit": {"lookup": "Doryani's Fist", "factor": 1 / 9},
	#		"The Cursed King": {"lookup": "Rigwald's Curse", "factor": 1/8},
			"The Darkest Dream": {"lookup": "Severed in Sleep", "factor": 1 / 6},
			"The Deceiver": {"lookup": "Belt of the Deceiver", "factor": 1 / 4},
			"The Deep Ones": {"lookup": "Tidebreaker", "factor": 1 / 5},
			"The Demoness": {"lookup": "Death's Hand", "factor": 1 / 5},
			"The Doctor": {"lookup": "Headhunter", "factor": 1 / 8},
			"The Dragon": {"lookup": "Coruscating Elixir", "factor": 1 / 4},
#			"The Dreamland": {"lookup": "Poorjoy's Asylum", "factor": 1 / 8},
			"The Drunken Aristocrat": {"lookup": "Divination Distillate", "factor": 1 / 8},
			"The Endless Darkness": {"lookup": "Voidforge", "factor": 1 / 9},
			"The Fathomless Depths": {"lookup": "Lightpoacher", "factor": 1 / 8},
			"The Feast": {"lookup": "Romira's Banquet", "factor": 1 / 5},
			"The Fiend": {"lookup": "Headhunter", "factor": 1 / 11},
			"The Fletcher": {"lookup": "Drillneck", "factor": 1 / 5},
			"The Formless Sea": {"lookup": "Varunastra", "factor": 1 / 7},
			"The Forsaken": {"lookup": "Umbilicus Immortalis", "factor": 1 / 7},
			"The Harvester": {"lookup": "The Harvest", "factor": 1 / 11},
			"The Hermit": {"lookup": "Lifesprig", "factor": 1 / 9},
			"The Hunger": {"lookup": "Taste of Hate", "factor": 1 / 9},
			"The Incantation": {"lookup": "The Whispering Ice", "factor": 1 / 4},
			"The Insatiable": {"lookup": "The Harvest", "factor": 1 / 3},
			"The King's Heart": {"lookup": "Kaom's Heart", "factor": 1 / 8},
			"The Last One Standing": {"lookup": "Atziri's Disfavour", "factor": 1 / 10},
			"The Lich": {"lookup": "Midnight Bargain", "factor": 1 / 12},
			"The Life Thief": {"lookup": "Zerphi's Heart", "factor": 1 / 6},
			"The Lunaris Priestess": {"lookup": "Sire of Shards", "factor": 1 / 5},
			"The Master": {"lookup": "Bisco's Collar", "factor": 1 / 4},
#			"The Mayor": {"lookup": "The Perandus Manor", "factor": 1 / 5},
			"The Oath": {"lookup": "Death's Oath", "factor": 1 / 6},
			"The Offering": {"lookup": "Shavronne's Wrappings", "factor": 1 / 8},
			"The One With All": {"lookup": "Le Heup of All", "factor": 1 / 6},
			"The Pack Leader": {"lookup": "Alpha's Howl", "factor": 1 / 6},
			"The Pact": {"lookup": "Pledge of Hands", "factor": 1 / 9},
	#		"The Poet": {"lookup": "Blood of Corruption", "factor": 1/9},
			"The Polymath": {"lookup": "Astramentis", "factor": 1 / 3},
#			"The Professor": {"lookup": "The Putrid Cloister", "factor": 1 / 4},
			"The Queen": {"lookup": "Atziri's Acuity", "factor": 1 / 16},
			"The Risk": {"lookup": "Ventor's Gamble", "factor": 1 / 3},
			"The Ruthless Ceinture": {"lookup": "Meginord's Girdle", "factor": 1 / 7},
			"The Scarred Meadow": {"lookup": "Wake of Destruction", "factor": 1 / 9},
			"The Scavenger": {"lookup": "Carcass Jack", "factor": 1 / 8},
			"The Siren": {"lookup": "The Whispering Ice", "factor": 1 / 7},
			"The Soul": {"lookup": "Soul Taker", "factor": 1 / 9},
			"The Spark and the Flame": {"lookup": "Berek's Respite", "factor": 1 / 2},
			"The Sun": {"lookup": "Rise of the Phoenix", "factor": 1 / 7},
			"The Sword King's Salute": {"lookup": "Daresso's Salute", "factor": 1 / 7},
			"The Thaumaturgist": {"lookup": "Shavronne's Revelation", "factor": 1 / 8},
			"The Throne": {"lookup": "Kaom's Roots", "factor": 1 / 2},
			"The Twilight Moon": {"lookup": "The Twilight Temple", "factor": 1 / 6},
			"The Visionary": {"lookup": "Lioneye's Vision", "factor": 1 / 6},
			"The Watcher": {"lookup": "Crown of Eyes", "factor": 1 / 12},
			"The Wind": {"lookup": "Windripper", "factor": 1 / 7},
			"The Witch": {"lookup": "Kiara's Determination", "factor": 1 / 8},
			"The Wolf's Shadow": {"lookup": "Hyaon's Fury", "factor": 1 / 3},
			"The Wolven King's Bite": {"lookup": "Rigwald's Quills", "factor": 1 / 8},
			"The World Eater": {"lookup": "Starforge", "factor": 1 / 8},
			"Thirst for Knowledge": {"lookup": "Gluttony", "factor": 1 / 5},
			"Thunderous Skies": {"lookup": "Storm Cloud", "factor": 1 / 5},
			"Tranquillity": {"lookup": "Voltaxic Rift", "factor": 1 / 7},
#			"Treasure Hunter": {"lookup": "Vaults of Atziri", "factor": 1 / 7},
			"Turn the Other Cheek": {"lookup": "Pacifism", "factor": 1 / 3},
			"Vanity": {"lookup": "Tabula Rasa", "factor": 1 / 9},
#			"The Wolf's Legacy": {"lookup": "Vaults of Atziri", "factor": 1 / 4},
			'Remembrance': {"lookup": "Precursor's Emblem", "factor": 1 / 8},
	#		'The Price of Loyalty': {"lookup": "Skin of the Loyal", "factor": 1/4},
			'The Demon': {"lookup": "Headhunter", "factor": 1 / 10},
			'The Damned': {"lookup": "Soul Ripper", "factor": 1 / 6},
			"Etched in Blood": {"lookup": "Rigwald's Quills", "factor": 2 / 9},  # double corrupted
#			"Squandered Prosperity": {"lookup": "The Perandus Manor", "factor": 1 / 5},  # Corrupted
			"The Craving": {"lookup": "Unending Hunger", "factor": 1 / 4},
			"Succor of the Sinless": {"lookup": "Bottled Faith", "factor": 1 / 6},
			"The Escape": {"lookup": "Seven-League Step", "factor": 1 / 5},
		},
		# TODO: NYI
		"uniqueitemgroup": {
			"Alone in the Darkness": {"lookup": "Delve Item", "factor": 1 / 5},
			"Arrogance of the Vaal": {"lookup": "Item", "factor": 1 / 8},
			"Assassin's Favour": {"lookup": "Dagger", "factor": 1 / 9},
			"Atziri's Arsenal": {"lookup": "Weapon", "factor": 1 / 4},
			"Blind Venture": {"lookup": "Ring", "factor": 1 / 7},
			"Boon of the First Ones": {"lookup": "Bestiary Item", "factor": 1 / 6},
			"Doedre's Madness": {"lookup": "Doedre Item", "factor": 1 / 9},
			"Earth Drinker": {"lookup": "Granite Flask", "factor": 1 / 5},
			"Glimmer of Hope": {"lookup": "Gold Ring", "factor": 1 / 8},
			"Heterochromia": {"lookup": "Two-Stone Ring", "factor": 1 / 2},
			"Hope": {"lookup": "Prismatic Ring", "factor": 1 / 5},
			"Hubris": {"lookup": "Ring", "factor": 1 / 5},
			"Hunter's Resolve": {"lookup": "Bow", "factor": 1 / 8},
			"Jack in the Box": {"lookup": "Item", "factor": 1 / 4},
			"Light and Truth": {"lookup": "Crystal Sceptre", "factor": 1 / 2},
			"Lysah's Respite": {"lookup": "Agate Amulet", "factor": 1 / 6},
			"Mitts": {"lookup": "Gloves", "factor": 1 / 5},
			"The Admirer": {"lookup": "Atziri Item", "factor": 1 / 9},
			"The Aesthete": {"lookup": "Shavronne Item", "factor": 1 / 8},
			"The Battle Born": {"lookup": "Axe", "factor": 1 / 5},
			"The Body": {"lookup": "Body Armour", "factor": 1 / 4},
			"The Breach": {"lookup": "Breach Item", "factor": 1 / 4},
			"The Calling": {"lookup": "Beyond Item", "factor": 1 / 6},
			"The Dreamer": {"lookup": "Chayula Item", "factor": 1 / 6},
			"The Encroaching Darkness": {"lookup": "Map", "factor": 1 / 8},
			"The Eye of the Dragon": {"lookup": "Jewel", "factor": 1 / 10},
			"The Garish Power": {"lookup": "Jewel", "factor": 1 / 4},
			"The Gentleman": {"lookup": "Sword", "factor": 1 / 4},
			"The Gladiator": {"lookup": "Nightmare Bascinet", "factor": 1 / 5},
			"The Lion": {"lookup": "Lioneye Item", "factor": 1 / 5},
			"The Mercenary": {"lookup": "Shield", "factor": 1 / 5},
			"The Messenger": {"lookup": "Harbinger Fragment", "factor": 1 / 4},
			"The Penitent": {"lookup": "Unset Ring", "factor": 1 / 5},
			"The Primordial": {"lookup": "Jewel", "factor": 1 / 5},
			"The Samurai's Eye": {"lookup": "Watcher's Eye", "factor": 1 / 3},
			"The Stormcaller": {"lookup": "Agnerod Staff", "factor": 1 / 4},
			"The Tower": {"lookup": "Staff", "factor": 1 / 6},
			"The Traitor": {"lookup": "Wand", "factor": 1 / 4},
			"The Undaunted": {"lookup": "Nemesis Item", "factor": 1 / 5},
			"The Valkyrie": {"lookup": "Nemesis Item", "factor": 1 / 8},
			"The Wolf": {"lookup": "Rigwald Item", "factor": 1 / 5},
			"The Wolverine": {"lookup": "Claw", "factor": 1 / 4},
			"The Wretched": {"lookup": "Belt", "factor": 1 / 6},
			"Time-Lost Relic": {"lookup": "League-Specific Item", "factor": 1 / 10},
		},
		# TODO: NYI
		"currencyitemgroup": {
			"Emperor's Luck": {"lookup": "5x Currency", "factor": 1 / 5},  # 5x Currency
			"Harmony of Souls": {"lookup": "9x Shrieking Essence", "factor": 1 / 9},  # 9x Shrieking Essence
			"Monochrome": {"lookup": "10x Cartographer's Sextant", "factor": 1 / 3},  # 10x Cartographer's Sextant
			"The Cacophony": {"lookup": "3x Deafening Essence", "factor": 1 / 8},  # 3x Deafening Essence
			"The Master Artisan": {"lookup": "20x Quality Currency", "factor": 1 / 5},  # 20x Quality Currency
			"The Puzzle": {"lookup": "5x Breachstone Splinter", "factor": 1 / 5},  # 5x Breachstone Splinter
			"Three Voices": {"lookup": "3x Essence", "factor": 1 / 3},  # 3x Essence
		},
		"currencyitem": {
			"Abandoned Wealth": {"lookup": "Exalted Orb", "factor": 3 / 5},  # 3x Exalted Orb
			"Alluring Bounty": {"lookup": "Exalted Orb", "factor": 10 / 7},  # 10x Exalted Orb
			"Chaotic Disposition": {"lookup": "Chaos Orb", "factor": 5},  # 5x Chaos Orb
			"Coveted Possession": {"lookup": "Regal Orb", "factor": 5 / 9},  # 5x Regal Orb
			"Demigod's Wager": {"lookup": "Orb of Annulment", "factor": 1 / 7},  # Orb of Annulment
			"House of Mirrors": {"lookup": "Mirror of Kalandra", "factor": 1 / 9},  # Mirror of Kalandra
			"Loyalty": {"lookup": "Orb of Fusing", "factor": 3 / 5},  # 3x Orb of Fusing
			"Lucky Connections": {"lookup": "Orb of Fusing", "factor": 20 / 7},  # 20x Orb of Fusing
			"Lucky Deck": {"lookup": "Stacked Deck", "factor": 10 / 9},  # 10x Stacked Deck
			"No Traces": {"lookup": "Orb of Scouring", "factor": 30 / 9},  # 30x Orb of Scouring
			"Rain of Chaos": {"lookup": "Chaos Orb", "factor": 1 / 8},  # Chaos Orb
			"Seven Years Bad Luck": {"lookup": "Mirror Shard", "factor": 1 / 13},  # Mirror Shard
			"The Cartographer": {"lookup": "Cartographer's Chisel", "factor": 10},  # 10x Cartographer's Chisel
			"The Catalyst": {"lookup": "Vaal Orb", "factor": 1 / 3},  # Vaal Orb
			"The Fool": {"lookup": "Orb of Chance", "factor": 20 / 4},  # 20x Orb of Chance
			"The Gemcutter": {"lookup": "Gemcutter's Prism", "factor": 1 / 3},  # Gemcutter's Prism
			"The Hoarder": {"lookup": "Exalted Orb", "factor": 1 / 12},  # Exalted Orb
			"The Innocent": {"lookup": "Orb of Regret", "factor": 40 / 10},  # 40x Orb of Regret
			"The Inventor": {"lookup": "Vaal Orb", "factor": 10 / 6},  # 10x Vaal Orb
			"The Journey": {"lookup": "Harbinger's Orb", "factor": 1 / 3},  # Harbinger's Orb
			"The Saint's Treasure": {"lookup": "Exalted Orb", "factor": 2 / 10},  # 2x Exalted Orb
			"The Scholar": {"lookup": "Scroll of Wisdom", "factor": 40 / 3},  # 40x Scroll of Wisdom
			"The Seeker": {"lookup": "Orb of Annulment", "factor": 3 / 9},  # 3x Orb of Annulment
			"The Sephirot": {"lookup": "Divine Orb", "factor": 10 / 11},  # 10x Divine Orb
			"The Survivalist": {"lookup": "Orb of Alchemy", "factor": 7 / 3},  # 7x Orb of Alchemy
			"The Union": {"lookup": "Gemcutter's Prism", "factor": 10 / 7},  # 10x Gemcutter's Prism
			"The Wrath": {"lookup": "Chaos Orb", "factor": 10 / 8},  # 10x Chaos Orb
			"Three Faces in the Dark": {"lookup": "Chaos Orb", "factor": 3 / 7},  # 3x Chaos Orb
			"Vinia's Token": {"lookup": "Orb of Regret", "factor": 10 / 5},  # 10x Orb of Regret
			'The Heroic Shot': {"lookup": "Chromatic Orb", "factor": 17},  # 17x Chromatic Orb
			'Underground Forest': {"lookup": "Awakened Sextant", "factor": 1 / 10},  # 10x Awakened Sextant
		},
		"divination": {
			"The Immortal": {"lookup": "House of Mirrors", "factor": 1 / 10},
			"The Nurse": {"lookup": "The Doctor", "factor": 1 / 8},
		},
		"prophecy": {
			"Beauty Through Death": {"lookup": "The Queen's Sacrifice", "factor": 1 / 5},
			"Immortal Resolve": {"lookup": "Fated Connections", "factor": 1 / 6},
			"The Iron Bard": {"lookup": "Trash to Treasure", "factor": 1 / 9},
			"The Jeweller's Boon": {"lookup": "The Jeweller's Touch", "factor": 1 / 5},
			"The Mad King": {"lookup": "The King's Path", "factor": 1 / 7},
			"The Valley of Steel Boxes": {"lookup": "Monstrous Treasure", "factor": 1 / 9},
			'Vile Power': {"lookup": "Ancient Doom", "factor": 1 / 5},
			'The Side Quest': {"lookup": "A Master Seeks Help", "factor": 1 / 5},
		},
	}

	# Overwrite values for some cards based on what they give
	for typ, table in [("uniqueitem", price_val['unique']), ("currencyitem", price_val['currency']), ("prophecy", price_val['prophecy']), ("divination", price_val['div'])]:
		for card in cardlookup[typ]:
			current = cardlookup[typ][card]
			if current['lookup'] in table and card in price_val['div']:
				price_val['div'][card]['value'] = table[current['lookup']]['value'] * current['factor']


# Remove uniques that can not normally drop
# This should be ran last
def trim_uniques(uniques):
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

	for u in upgraded:
		if u in uniques:
			del uniques[u]


def validate_data(price_val):
	# Add missing value for chaos
	price_val['currency']['Chaos Orb'] = {'base': 'Chaos Orb', 'value': 1, 'count': 200}
	if "Perandus Coin" not in price_val['currency']:
		price_val['currency']['Perandus Coin'] = {'base': 'Perandus Coin', 'value': 1/200, 'count': 200}
	if "Rogue's Marker" not in price_val['currency']:
		price_val['currency']['Rogue\'s Marker'] = {'base': 'Rogue\'s Marker', 'value': 1/200, 'count': 200}
	# Remove low reliability data and load defaults where needed
	clean(price_val)
	fix_divs(price_val)
	# remove uniques that cannot normally drop
	trim_uniques(price_val['unique'])
	pass
