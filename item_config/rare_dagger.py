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
	"Glass Shank": {"base": "Glass Shank", "class": "Dagger", "other": ["ItemLevel <= 6"], "type": "levelling rare normal"},
	"Skinning Knife": {"base": "Skinning Knife", "class": "Dagger", "other": ["ItemLevel <= 10"], "type": "levelling rare normal"},
	"Carving Knife": {"base": "Carving Knife", "class": "Dagger", "other": ["ItemLevel <= 15"], "type": "levelling rare normal"},
	"Stiletto": {"base": "Stiletto", "class": "Dagger", "other": ["ItemLevel <= 20"], "type": "levelling rare normal"},
	"Boot Knife": {"base": "Boot Knife", "class": "Dagger", "other": ["ItemLevel <= 25"], "type": "levelling rare normal"},
	"Copper Kris": {"base": "Copper Kris", "class": "Dagger", "other": ["ItemLevel <= 29"], "type": "levelling rare normal"},
	"Skean": {"base": "Skean", "class": "Dagger", "other": ["ItemLevel <= 33"], "type": "levelling rare normal"},
	"Imp Dagger": {"base": "Imp Dagger", "class": "Dagger", "other": ["ItemLevel <= 37"], "type": "levelling rare normal"},
	"Flaying Knife": {"base": "Flaying Knife", "class": "Dagger", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Prong Dagger": {"base": "Prong Dagger", "class": "Dagger", "other": ["ItemLevel <= 41"], "type": "levelling rare normal"},
	"Butcher Knife": {"base": "Butcher Knife", "class": "Dagger", "other": ["ItemLevel <= 43"], "type": "levelling rare normal"},
	"Poignard": {"base": "Poignard", "class": "Dagger", "other": ["ItemLevel <= 46"], "type": "levelling rare normal"},
	"Boot Blade": {"base": "Boot Blade", "class": "Dagger", "other": ["ItemLevel <= 49"], "type": "levelling rare normal"},
	"Golden Kris": {"base": "Golden Kris", "class": "Dagger", "other": ["ItemLevel <= 52"], "type": "levelling rare normal"},
	"Royal Skean": {"base": "Royal Skean", "class": "Dagger", "other": ["ItemLevel <= 55"], "type": "levelling rare normal"},
	"Fiend Dagger": {"base": "Fiend Dagger", "class": "Dagger", "other": ["ItemLevel <= 58"], "type": "levelling rare normal"},
	"Trisula": {"base": "Trisula", "class": "Dagger", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Gutting Knife": {"base": "Gutting Knife", "class": "Dagger", "other": ["ItemLevel <= 61"], "type": "levelling rare normal"},
	"Slaughter Knife": {"base": "Slaughter Knife", "class": "Dagger", "other": ["ItemLevel <= 63"], "type": "levelling rare normal"},
	"Ambusher": {"base": "Ambusher", "class": "Dagger", "other": ["ItemLevel <= 65"], "type": "levelling rare normal"},
	"Ezomyte Dagger": {"base": "Ezomyte Dagger", "class": "Dagger", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Platinum Kris": {"base": "Platinum Kris", "class": "Dagger", "other": ["ItemLevel <= 69"], "type": "ignore"},
	"Imperial Skean": {"base": "Imperial Skean", "class": "Dagger", "other": ["ItemLevel <= 71"], "type": "ignore"},
	"Demon Dagger": {"base": "Demon Dagger", "class": "Dagger", "other": ["ItemLevel <= 73"], "type": "ignore"},
	"Sai": {"base": "Sai", "class": "Dagger", "other": ["ItemLevel <= 75"], "type": "ignore"}
}
