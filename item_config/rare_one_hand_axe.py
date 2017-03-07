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
	"Rusted Hatchet": {"base": "Rusted Hatchet", "class": "One Hand Axe", "other": ["ItemLevel <= 7"], "type": "levelling rare normal"},
	"Jade Hatchet": {"base": "Jade Hatchet", "class": "One Hand Axe", "other": ["ItemLevel <= 11"], "type": "levelling rare normal"},
	"Boarding Axe": {"base": "Boarding Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 16"], "type": "levelling rare normal"},
	"Cleaver": {"base": "Cleaver", "class": "One Hand Axe", "other": ["ItemLevel <= 21"], "type": "levelling rare normal"},
	"Broad Axe": {"base": "Broad Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 26"], "type": "levelling rare normal"},
	"Arming Axe": {"base": "Arming Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 30"], "type": "levelling rare normal"},
	"Decorative Axe": {"base": "Decorative Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 34"], "type": "levelling rare normal"},
	"Spectral Axe": {"base": "Spectral Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 38"], "type": "levelling rare normal"},
	"Etched Hatchet": {"base": "Etched Hatchet", "class": "One Hand Axe", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Jasper Axe": {"base": "Jasper Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 41"], "type": "levelling rare normal"},
	"Tomahawk": {"base": "Tomahawk", "class": "One Hand Axe", "other": ["ItemLevel <= 44"], "type": "levelling rare normal"},
	"Wrist Chopper": {"base": "Wrist Chopper", "class": "One Hand Axe", "other": ["ItemLevel <= 47"], "type": "levelling rare normal"},
	"War Axe": {"base": "War Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 50"], "type": "levelling rare normal"},
	"Chest Splitter": {"base": "Chest Splitter", "class": "One Hand Axe", "other": ["ItemLevel <= 53"], "type": "levelling rare normal"},
	"Ceremonial Axe": {"base": "Ceremonial Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 56"], "type": "levelling rare normal"},
	"Wraith Axe": {"base": "Wraith Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 59"], "type": "levelling rare normal"},
	"Engraved Hatchet": {"base": "Engraved Hatchet", "class": "One Hand Axe", "other": ["ItemLevel <= 61"], "type": "levelling rare normal"},
	"Karui Axe": {"base": "Karui Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 62"], "type": "levelling rare normal"},
	"Siege Axe": {"base": "Siege Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 64"], "type": "levelling rare normal"},
	"Reaver Axe": {"base": "Reaver Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 66"], "type": "levelling rare normal"},
	"Butcher Axe": {"base": "Butcher Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 68"], "type": "ignore"},
	"Vaal Hatchet": {"base": "Vaal Hatchet", "class": "One Hand Axe", "other": ["ItemLevel <= 70"], "type": "ignore"},
	"Royal Axe": {"base": "Royal Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 72"], "type": "ignore"},
	"Infernal Axe": {"base": "Infernal Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 74"], "type": "ignore"},
	"Runic Hatchet": {"base": "Runic Hatchet", "class": "One Hand Axe", "other": ["ItemLevel <= 76"], "type": "ignore"}
}
