#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Nonrare item for leveling or crafting"

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Driftwood Sceptre": {"base": "Driftwood Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 6"], "type": "leveling low"},
	"Darkwood Sceptre": {"base": "Darkwood Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 10"], "type": "leveling low"},
	"Bronze Sceptre": {"base": "Bronze Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 15"], "type": "leveling low"},
	"Quartz Sceptre": {"base": "Quartz Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 20"], "type": "leveling low"},
	"Iron Sceptre": {"base": "Iron Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 25"], "type": "leveling low"},
	"Ochre Sceptre": {"base": "Ochre Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 29"], "type": "leveling low"},
	"Ritual Sceptre": {"base": "Ritual Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "leveling low"},
	"Shadow Sceptre": {"base": "Shadow Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "leveling low"},
	"Grinning Fetish": {"base": "Grinning Fetish", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Horned Sceptre": {"base": "Horned Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "leveling low"},
	"Sekhem": {"base": "Sekhem", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 43"], "type": "leveling low"},
	"Crystal Sceptre": {"base": "Crystal Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "leveling low"},
	"Lead Sceptre": {"base": "Lead Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 49"], "type": "leveling low"},
	"Blood Sceptre": {"base": "Blood Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 52"], "type": "ignore"},
	"Royal Sceptre": {"base": "Royal Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 55"], "type": "ignore"},
	"Abyssal Sceptre": {"base": "Abyssal Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "ignore"},
	"Stag Sceptre": {"base": "Stag Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Karui Sceptre": {"base": "Karui Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "ignore"},
	"Tyrant's Sekhem": {"base": "Tyrant's Sekhem", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Opal Sceptre": {"base": "Opal Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "ignore"},
	"Platinum Sceptre": {"base": "Platinum Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Vaal Sceptre": {"base": "Vaal Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "ignore"},
	"Carnal Sceptre": {"base": "Carnal Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "ignore"},
	"Void Sceptre": {"base": "Void Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"},
	"Sambar Sceptre": {"base": "Sambar Sceptre", "class": "Sceptre", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"}
}
