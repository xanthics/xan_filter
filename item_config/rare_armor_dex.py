#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Rare item for leveling or crafting"

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Shabby Jerkin": {"base": "Shabby Jerkin", "other": ["ItemLevel <= 7"], "type": "levelling rare normal"},
	"Strapped Leather": {"base": "Strapped Leather", "other": ["ItemLevel <= 14"], "type": "levelling rare normal"},
	"Buckskin Tunic": {"base": "Buckskin Tunic", "other": ["ItemLevel <= 22"], "type": "levelling rare normal"},
	"Wild Leather": {"base": "Wild Leather", "other": ["ItemLevel <= 30"], "type": "levelling rare normal"},
	"Full Leather": {"base": "Full Leather", "other": ["ItemLevel <= 33"], "type": "levelling rare normal"},
	"Sun Leather": {"base": "Sun Leather", "other": ["ItemLevel <= 37"], "type": "levelling rare normal"},
	"Thief's Garb": {"base": "Thief's Garb", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Eelskin Tunic": {"base": "Eelskin Tunic", "other": ["ItemLevel <= 42"], "type": "levelling rare normal"},
	"Frontier Leather": {"base": "Frontier Leather", "other": ["ItemLevel <= 46"], "type": "levelling rare normal"},
	"Glorious Leather": {"base": "Glorious Leather", "other": ["ItemLevel <= 50"], "type": "levelling rare normal"},
	"Coronal Leather": {"base": "Coronal Leather", "other": ["ItemLevel <= 54"], "type": "levelling rare normal"},
	"Cutthroat's Garb": {"base": "Cutthroat's Garb", "other": ["ItemLevel <= 58"], "type": "levelling rare normal"},
	"Sharkskin Tunic": {"base": "Sharkskin Tunic", "other": ["ItemLevel <= 61"], "type": "levelling rare normal"},
	"Destiny Leather": {"base": "Destiny Leather", "other": ["ItemLevel <= 64"], "type": "levelling rare normal"},
	"Exquisite Leather": {"base": "Exquisite Leather", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Zodiac Leather": {"base": "Zodiac Leather", "other": ["ItemLevel <= 70"], "type": "ignore"},
	"Assassin's Garb": {"base": "Assassin's Garb", "other": ["ItemLevel <= 73"], "type": "ignore"},
	"Rawhide Boots": {"base": "Rawhide Boots", "other": ["ItemLevel <= 8"], "type": "levelling rare normal"},
	"Goathide Boots": {"base": "Goathide Boots", "other": ["ItemLevel <= 17"], "type": "levelling rare normal"},
	"Deerskin Boots": {"base": "Deerskin Boots", "other": ["ItemLevel <= 27"], "type": "levelling rare normal"},
	"Nubuck Boots": {"base": "Nubuck Boots", "other": ["ItemLevel <= 39"], "type": "levelling rare normal"},
	"Eelskin Boots": {"base": "Eelskin Boots", "other": ["ItemLevel <= 44"], "type": "levelling rare normal"},
	"Sharkskin Boots": {"base": "Sharkskin Boots", "other": ["ItemLevel <= 49"], "type": "levelling rare normal"},
	"Shagreen Boots": {"base": "Shagreen Boots", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Stealth Boots": {"base": "Stealth Boots", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Slink Boots": {"base": "Slink Boots", "other": ["ItemLevel <= 74"], "type": "ignore"},
	"Rawhide Gloves": {"base": "Rawhide Gloves", "other": ["ItemLevel <= 8"], "type": "levelling rare normal"},
	"Goathide Gloves": {"base": "Goathide Gloves", "other": ["ItemLevel <= 14"], "type": "levelling rare normal"},
	"Deerskin Gloves": {"base": "Deerskin Gloves", "other": ["ItemLevel <= 26"], "type": "levelling rare normal"},
	"Nubuck Gloves": {"base": "Nubuck Gloves", "other": ["ItemLevel <= 38"], "type": "levelling rare normal"},
	"Eelskin Gloves": {"base": "Eelskin Gloves", "other": ["ItemLevel <= 43"], "type": "levelling rare normal"},
	"Sharkskin Gloves": {"base": "Sharkskin Gloves", "other": ["ItemLevel <= 50"], "type": "levelling rare normal"},
	"Shagreen Gloves": {"base": "Shagreen Gloves", "other": ["ItemLevel <= 59"], "type": "levelling rare normal"},
	"Stealth Gloves": {"base": "Stealth Gloves", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Slink Gloves": {"base": "Slink Gloves", "other": ["ItemLevel <= 75"], "type": "ignore"},
	"Leather Cap": {"base": "Leather Cap", "other": ["ItemLevel <= 8"], "type": "levelling rare normal"},
	"Tricorne": {"base": "Tricorne", "other": ["ItemLevel <= 15"], "type": "levelling rare normal"},
	"Leather Hood": {"base": "Leather Hood", "other": ["ItemLevel <= 25"], "type": "levelling rare normal"},
	"Wolf Pelt": {"base": "Wolf Pelt", "other": ["ItemLevel <= 35"], "type": "levelling rare normal"},
	"Hunter Hood": {"base": "Hunter Hood", "other": ["ItemLevel <= 46"], "type": "levelling rare normal"},
	"Noble Tricorne": {"base": "Noble Tricorne", "other": ["ItemLevel <= 52"], "type": "levelling rare normal"},
	"Ursine Pelt": {"base": "Ursine Pelt", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Silken Hood": {"base": "Silken Hood", "other": ["ItemLevel <= 65"], "type": "levelling rare normal"},
	"Sinner Tricorne": {"base": "Sinner Tricorne", "other": ["ItemLevel <= 69"], "type": "ignore"},
	"Lion Pelt": {"base": "Lion Pelt", "other": ["ItemLevel <= 75"], "type": "ignore"},
	"Goathide Buckler": {"base": "Goathide Buckler", "other": ["ItemLevel <= 7"], "type": "levelling rare normal"},
	"Pine Buckler": {"base": "Pine Buckler", "other": ["ItemLevel <= 13"], "type": "levelling rare normal"},
	"Painted Buckler": {"base": "Painted Buckler", "other": ["ItemLevel <= 21"], "type": "levelling rare normal"},
	"Hammered Buckler": {"base": "Hammered Buckler", "other": ["ItemLevel <= 28"], "type": "levelling rare normal"},
	"War Buckler": {"base": "War Buckler", "other": ["ItemLevel <= 34"], "type": "levelling rare normal"},
	"Gilded Buckler": {"base": "Gilded Buckler", "other": ["ItemLevel <= 39"], "type": "levelling rare normal"},
	"Oak Buckler": {"base": "Oak Buckler", "other": ["ItemLevel <= 43"], "type": "levelling rare normal"},
	"Enameled Buckler": {"base": "Enameled Buckler", "other": ["ItemLevel <= 47"], "type": "levelling rare normal"},
	"Corrugated Buckler": {"base": "Corrugated Buckler", "other": ["ItemLevel <= 51"], "type": "levelling rare normal"},
	"Battle Buckler": {"base": "Battle Buckler", "other": ["ItemLevel <= 55"], "type": "levelling rare normal"},
	"Golden Buckler": {"base": "Golden Buckler", "other": ["ItemLevel <= 59"], "type": "levelling rare normal"},
	"Ironwood Buckler": {"base": "Ironwood Buckler", "other": ["ItemLevel <= 62"], "type": "levelling rare normal"},
	"Lacquered Buckler": {"base": "Lacquered Buckler", "other": ["ItemLevel <= 65"], "type": "levelling rare normal"},
	"Vaal Buckler": {"base": "Vaal Buckler", "other": ["ItemLevel <= 68"], "type": "ignore"},
	"Crusader Buckler": {"base": "Crusader Buckler", "other": ["ItemLevel <= 71"], "type": "ignore"},
	"Imperial Buckler": {"base": "Imperial Buckler", "other": ["ItemLevel <= 74"], "type": "ignore"}
}
