#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Always show catchall"

# Base type : settings pair
items = {
	# High value veiled mods, so that they still show after removing them from itemmod.py when finished
	"2 Magic Jewel": {"class": "Jewel", "other": ["Rarity <= Magic", "AreaLevel <= 70"], "type": "normal"},

	"77 Influenced Item": {'other': ["HasInfluence Elder Shaper Crusader Hunter Redeemer Warlord"], "type": "rare low"},
	"77 Fractured Item": {'other': ["FracturedItem True"], "type": "rare low"},
	"77 Synthesised Item": {'other': ["SynthesisedItem True"], "type": "rare low"},

	"11 Map Fragments": {"class": "Map Fragments", "type": "fragment normal"},
	"11 Misc Map Items": {"class": "Misc Map Items", "type": "fragment normal"},
	"12 Currency": {"class": "Currency", "type": "currency normal"},
	"13 Divination Cards": {"class": "Divination Card", "type": "divination normal"},
	"14 Incubators": {"class": "Incubator", "type": "currency normal"},
	"16 unique": {"type": "unique normal"},
	"17 enchant": {"class": "Helmet", "other": ["AnyEnchantment True"], "type": "item mod"},
	"18 Misc map items": {"class": "Misc Map Items", "type": "show high"},
#	"1 Alternate Gems": {"other": ["AlternateQuality True"], "type": "challenge normal"},
#	"1 Replica Unique": {"other": ["Replica True"], "type": "challenge normal"},
#	"1 Rogue's Marker": {"baseexact": "Rogue's Marker", "class": "Currency", "type": "challenge normal"},

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
	"92 Talisman rares": {"base": "Talisman", "type": "rare corrupted"},
	"1 Watchstone": {"base": "Watchstone", "type": "show normal"},
	#	"93 identified rares": {"other": ["Identified True"], "type": "rare low"},

}
