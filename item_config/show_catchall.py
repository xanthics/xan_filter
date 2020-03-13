#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Always show catchall"

# Base type : settings pair
items = {
	# High value veiled mods, so that they still show after removing them from itemmod.py when finished
	"05 Abyss Jewel": {"class": "Abyss Jewel", "other": ["Rarity <= Magic"], "type": "normal"},
	"0 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "show normal"},
	"2 Magic Jewel": {"class": "Jewel", "other": ["Rarity <= Magic", "AreaLevel <= 70"], "type": "normal"},
	"1 Cluster Jewel": {"base": "Cluster Jewel", "class": "Jewel", "type": "show normal"},

	# Corrupted white items for lead to gold darkshrine
	#"0 corrupted amulet": {"class": "Amulets", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "show normal"},
	#"0 corrupted ring": {"class": "Rings", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "ignore"},
	#"0 corrupted belt": {"class": "Belts", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "show normal"},
	#"0 corrupted quiver": {"class": "Quivers", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "ignore"},
	#"0 corrupted gloves": {"class": "Gloves", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "ignore"},
	#"0 corrupted boots": {"class": "Boots", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "ignore"},
	#"0 corrupted shield": {"class": "Shield", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "ignore"},
	#"0 Crafting helm": {"class": "Helmets", "other": ["Rarity Normal", "ItemLevel >= 84"], "type": "show normal"},

	"7 Influenced Item": {'other': ["HasInfluence Elder Shaper Crusader Hunter Redeemer Warlord"], "type": "rare low"},
	"7 Fractured Item": {'other': ["FracturedItem True"], "type": "rare low"},
	"7 Synthesised Item": {'other': ["SynthesisedItem True"], "type": "rare low"},

	"74 Map Fragments": {"class": "Map Fragments", "type": "map white"},

	"8 5": {"other": ["DropLevel <= 5", "AreaLevel >= 15", "AreaLevel <= 67"], "type": "rare low"},
	"8 10": {"other": ["DropLevel <= 10", "AreaLevel >= 20", "AreaLevel <= 67"], "type": "rare low"},
	"8 15": {"other": ["DropLevel <= 15", "AreaLevel >= 25", "AreaLevel <= 67"], "type": "rare low"},
	"8 20": {"other": ["DropLevel <= 20", "AreaLevel >= 30", "AreaLevel <= 67"], "type": "rare low"},
	"8 25": {"other": ["DropLevel <= 25", "AreaLevel >= 35", "AreaLevel <= 67"], "type": "rare low"},
	"8 30": {"other": ["DropLevel <= 30", "AreaLevel >= 40", "AreaLevel <= 67"], "type": "rare low"},
	"8 35": {"other": ["DropLevel <= 35", "AreaLevel >= 45", "AreaLevel <= 67"], "type": "rare low"},
	"8 40": {"other": ["DropLevel <= 40", "AreaLevel >= 50", "AreaLevel <= 67"], "type": "rare low"},
	"8 45": {"other": ["DropLevel <= 45", "AreaLevel >= 55", "AreaLevel <= 67"], "type": "rare low"},
	"8 50": {"other": ["DropLevel <= 50", "AreaLevel >= 60", "AreaLevel <= 67"], "type": "rare low"},
	"8 55": {"other": ["DropLevel <= 55", "AreaLevel >= 65", "AreaLevel <= 67"], "type": "rare low"},

	"91 Other rares": {"other": ["AreaLevel <= 67"], "type": "rare normal"},
	"92 corrupted rares": {"other": ["Corrupted True", "CorruptedMods > 0"], "type": "rare corrupted"},
#	"93 identified rares": {"other": ["Identified True"], "type": "rare low"},

}
