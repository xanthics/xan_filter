#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "leveling items that are worth seeing"

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"0 Boots (Movespeed)": {"class": "Boots", "other": ["Rarity Magic", "ItemLevel <= 20"], "type": "leveling normal"},

	"1 linked 0-20": {"other": ["Rarity <= Magic", "DropLevel >= 0", "ItemLevel <= 20", "LinkedSockets >= 3"], "type": "leveling normal"},
	"1 linked 15-40": {"other": ["Rarity <= Magic", "DropLevel >= 15", "ItemLevel <= 40", "LinkedSockets > 3"], "type": "leveling normal"},
	"1 linked 25-50": {"other": ["Rarity <= Magic", "DropLevel >= 25", "ItemLevel <= 50", "LinkedSockets > 3"], "type": "leveling normal"},
	"1 linked 40-65": {"other": ["Rarity <= Magic", "DropLevel >= 40", "ItemLevel <= 65", "LinkedSockets > 3"], "type": "leveling normal"},

	"1 Sceptre/Wand linked 15-40": {"class": "Sceptres\" \"Wands", "other": ["Rarity <= Magic", "ItemLevel <= 40", "LinkedSockets >= 3"], "type": "leveling normal"},

#	"1 Sceptre/Wand linked 15-40": {"class": "Sceptres\" \"Wands", "other": ["Rarity <= Magic", "DropLevel >= 15", "ItemLevel <= 40", "LinkedSockets >= 3"], "type": "leveling normal"},
#	"1 Sceptre/Wand linked 25-50": {"class": "Sceptres\" \"Wands", "other": ["Rarity <= Magic", "DropLevel >= 25", "ItemLevel <= 50", "LinkedSockets >= 3"], "type": "leveling normal"},
#	"1 Sceptre/Wand linked 40-65": {"class": "Sceptres\" \"Wands", "other": ["Rarity <= Magic", "DropLevel >= 40", "ItemLevel <= 65", "LinkedSockets >= 3"], "type": "leveling normal"},
}
