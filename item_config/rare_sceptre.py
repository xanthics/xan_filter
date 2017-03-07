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
	"Driftwood Sceptre": {"base": "Driftwood Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 6"], "type": "levelling rare normal"},
	"Darkwood Sceptre": {"base": "Darkwood Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 10"], "type": "levelling rare normal"},
	"Bronze Sceptre": {"base": "Bronze Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 15"], "type": "levelling rare normal"},
	"Quartz Sceptre": {"base": "Quartz Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 20"], "type": "levelling rare high"},
	"Iron Sceptre": {"base": "Iron Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 25"], "type": "levelling rare normal"},
	"Ochre Sceptre": {"base": "Ochre Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 29"], "type": "levelling rare normal"},
	"Ritual Sceptre": {"base": "Ritual Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 33"], "type": "levelling rare normal"},
	"Shadow Sceptre": {"base": "Shadow Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 37"], "type": "levelling rare high"},
	"Grinning Fetish": {"base": "Grinning Fetish", "class": "Sceptre", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Horned Sceptre": {"base": "Horned Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 41"], "type": "levelling rare normal"},
	"Sekhem": {"base": "Sekhem", "class": "Sceptre", "other": ["ItemLevel <= 43"], "type": "levelling rare normal"},
	"Crystal Sceptre": {"base": "Crystal Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 46"], "type": "levelling rare high"},
	"Lead Sceptre": {"base": "Lead Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 49"], "type": "levelling rare normal"},
	"Blood Sceptre": {"base": "Blood Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 52"], "type": "levelling rare normal"},
	"Royal Sceptre": {"base": "Royal Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 55"], "type": "levelling rare normal"},
	"Abyssal Sceptre": {"base": "Abyssal Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 58"], "type": "levelling rare high"},
	"Stag Sceptre": {"base": "Stag Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Karui Sceptre": {"base": "Karui Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 61"], "type": "levelling rare normal"},
	"Tyrant's Sekhem": {"base": "Tyrant's Sekhem", "class": "Sceptre", "other": ["ItemLevel <= 63"], "type": "levelling rare normal"},
	"Opal Sceptre": {"base": "Opal Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 65"], "type": "levelling rare high"},
	"Platinum Sceptre": {"base": "Platinum Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Vaal Sceptre": {"base": "Vaal Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 69"], "type": "ignore"},
	"Carnal Sceptre": {"base": "Carnal Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 71"], "type": "ignore"},
	"Void Sceptre": {"base": "Void Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 73"], "type": "ignore"},
	"Sambar Sceptre": {"base": "Sambar Sceptre", "class": "Sceptre", "other": ["ItemLevel <= 75"], "type": "ignore"}
}
