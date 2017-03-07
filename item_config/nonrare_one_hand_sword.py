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
	"Rusted Sword": {"base": "Rusted Sword", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 6"], "type": "leveling low"},
	"Copper Sword": {"base": "Copper Sword", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 10"], "type": "leveling low"},
	"Sabre": {"base": "Sabre", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 15"], "type": "leveling low"},
	"Broad Sword": {"base": "Broad Sword", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 20"], "type": "leveling low"},
	"War Sword": {"base": "War Sword", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 25"], "type": "leveling low"},
	"Ancient Sword": {"base": "Ancient Sword", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 29"], "type": "leveling low"},
	"Elegant Sword": {"base": "Elegant Sword", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "leveling low"},
	"Dusk Blade": {"base": "Dusk Blade", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "leveling low"},
	"Hook Sword": {"base": "Hook Sword", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "leveling low"},
	"Variscite Blade": {"base": "Variscite Blade", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Cutlass": {"base": "Cutlass", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 43"], "type": "leveling low"},
	"Baselard": {"base": "Baselard", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "leveling low"},
	"Battle Sword": {"base": "Battle Sword", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 49"], "type": "leveling low"},
	"Elder Sword": {"base": "Elder Sword", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 52"], "type": "ignore"},
	"Graceful Sword": {"base": "Graceful Sword", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 55"], "type": "ignore"},
	"Twilight Blade": {"base": "Twilight Blade", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "ignore"},
	"Grappler": {"base": "Grappler", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Gemstone Sword": {"base": "Gemstone Sword", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "ignore"},
	"Corsair Sword": {"base": "Corsair Sword", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Gladius": {"base": "Gladius", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "ignore"},
	"Legion Sword": {"base": "Legion Sword", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Vaal Blade": {"base": "Vaal Blade", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "ignore"},
	"Eternal Sword": {"base": "Eternal Sword", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "ignore"},
	"Midnight Blade": {"base": "Midnight Blade", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"},
	"Tiger Hook": {"base": "Tiger Hook", "class": "One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"}
}
