#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Always show"

# Base type : settings pair
items = {
	# Personal Highlights for farming goals
#	"01 City Square": {"other": ['CustomAlertSound "45_show.wav"', 'PlayEffect White'], "base": "City Square", "class": "Map", "type": "show high"},
#	"01 Plague Mask": {"base": "Plague Mask", "type": "show high"},
	# "00 Crafting base": {'class': 'Helmet', "other": ["Rarity Normal", "DropLevel >= 50"], "type": "leveling low"},

	# High value atlas bases.  Show and make noise at any rarity
	"04 Stygian Vise": {"other": ['CustomAlertSound "45_show.wav"', "Rarity <= Magic"], "base": "Stygian Vise", "type": "show high"},
	"05 Abyss Jewel": {"class": "Abyss Jewel", "other": ["Rarity <= Magic"], "type": "normal"},
	"10 Talisman": {"class": "Amulets", 'other': ["Rarity >= Rare", "ItemLevel >= 70"], "base": "Talisman", "type": "show high"},
	"11 Talisman": {"class": "Amulets", 'other': ["ItemLevel >= 70"], "base": "Talisman", "type": "show high"},
	"12 Talisman": {"class": "Amulets", "base": "Talisman", "type": "show low"},
	"0 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "show normal"},
	"1 Magic Jewel": {"class": "Jewel", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "normal"},

	# Corrupted white items for lead to gold darkshrine
	#"0 corrupted amulet": {"class": "Amulets", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "show normal"},
	#"0 corrupted ring": {"class": "Rings", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "ignore"},
	#"0 corrupted belt": {"class": "Belts", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "show normal"},
	#"0 corrupted quiver": {"class": "Quivers", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "ignore"},
	#"0 corrupted gloves": {"class": "Gloves", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "ignore"},
	#"0 corrupted boots": {"class": "Boots", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "ignore"},
	#"0 corrupted shield": {"class": "Shield", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "ignore"},
	#"0 Crafting helm": {"class": "Helmets", "other": ["Rarity Normal", "ItemLevel >= 84"], "type": "show normal"},

	# Rare highlighting for currency recipes.  change 'ignore' to 'high' or back as needed

	"6 Elder amulet": {"class": "Amulets", 'other': ["ElderItem True"], "type": "rare highlight"},
	"6 Shaper amulet": {"class": "Amulets", 'other': ["ShaperItem True"], "type": "rare highlight"},
	"6 Elder ring": {"class": "Rings", 'other': ["ElderItem True"], "type": "rare highlight"},
	"6 Shaper ring": {"class": "Rings", 'other': ["ShaperItem True"], "type": "rare highlight"},
	"6 Elder belt": {"class": "Belts", 'other': ["ElderItem True"], "type": "rare highlight"},
	"6 Shaper belt": {"class": "Belts", 'other': ["ShaperItem True"], "type": "rare highlight"},
	"7 Elder Item": {'other': ["ElderItem True"], "type": "rare low"},
	"7 Shaper Item": {'other': ["ShaperItem True"], "type": "rare low"},
	"7 Fractured Item": {'other': ["FracturedItem True"], "type": "rare low"},
	"7 Synthesised Item": {'other': ["SynthesisedItem True"], "type": "rare low"},

	"8 5": {"other": ["DropLevel <= 5", "ItemLevel >= 15", "ItemLevel <= 74"], "type": "rare low"},
	"8 10": {"other": ["DropLevel <= 10", "ItemLevel >= 20", "ItemLevel <= 74"], "type": "rare low"},
	"8 15": {"other": ["DropLevel <= 15", "ItemLevel >= 25", "ItemLevel <= 74"], "type": "rare low"},
	"8 20": {"other": ["DropLevel <= 20", "ItemLevel >= 30", "ItemLevel <= 74"], "type": "rare low"},
	"8 25": {"other": ["DropLevel <= 25", "ItemLevel >= 35", "ItemLevel <= 74"], "type": "rare low"},
	"8 30": {"other": ["DropLevel <= 30", "ItemLevel >= 40", "ItemLevel <= 74"], "type": "rare low"},
	"8 35": {"other": ["DropLevel <= 35", "ItemLevel >= 45", "ItemLevel <= 74"], "type": "rare low"},
	"8 40": {"other": ["DropLevel <= 40", "ItemLevel >= 50", "ItemLevel <= 74"], "type": "rare low"},
	"8 45": {"other": ["DropLevel <= 45", "ItemLevel >= 55", "ItemLevel <= 74"], "type": "rare low"},
	"8 50": {"other": ["DropLevel <= 50", "ItemLevel >= 60", "ItemLevel <= 74"], "type": "rare low"},
	"8 55": {"other": ["DropLevel <= 55", "ItemLevel >= 65", "ItemLevel <= 74"], "type": "rare low"},

	"91 Other rares": {"other": ["ItemLevel <= 74"], "type": "rare normal"},
	"92 identified rares": {"other": ["Identified True"], "type": "rare low"},

}
