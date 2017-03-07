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
	"Driftwood Club": {"base": "Driftwood Club", "class": "One Hand Mace", "other": ["ItemLevel <= 6"], "type": "levelling rare normal"},
	"Tribal Club": {"base": "Tribal Club", "class": "One Hand Mace", "other": ["ItemLevel <= 10"], "type": "levelling rare normal"},
	"Spiked Club": {"base": "Spiked Club", "class": "One Hand Mace", "other": ["ItemLevel <= 15"], "type": "levelling rare normal"},
	"Stone Hammer": {"base": "Stone Hammer", "class": "One Hand Mace", "other": ["ItemLevel <= 20"], "type": "levelling rare normal"},
	"War Hammer": {"base": "War Hammer", "class": "One Hand Mace", "other": ["ItemLevel <= 25"], "type": "levelling rare normal"},
	"Bladed Mace": {"base": "Bladed Mace", "class": "One Hand Mace", "other": ["ItemLevel <= 29"], "type": "levelling rare normal"},
	"Ceremonial Mace": {"base": "Ceremonial Mace", "class": "One Hand Mace", "other": ["ItemLevel <= 33"], "type": "levelling rare normal"},
	"Dream Mace": {"base": "Dream Mace", "class": "One Hand Mace", "other": ["ItemLevel <= 37"], "type": "levelling rare normal"},
	"Wyrm Mace": {"base": "Wyrm Mace", "class": "One Hand Mace", "other": ["ItemLevel <= 39"], "type": "levelling rare normal"},
	"Petrified Club": {"base": "Petrified Club", "class": "One Hand Mace", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Barbed Club": {"base": "Barbed Club", "class": "One Hand Mace", "other": ["ItemLevel <= 43"], "type": "levelling rare normal"},
	"Rock Breaker": {"base": "Rock Breaker", "class": "One Hand Mace", "other": ["ItemLevel <= 46"], "type": "levelling rare normal"},
	"Battle Hammer": {"base": "Battle Hammer", "class": "One Hand Mace", "other": ["ItemLevel <= 49"], "type": "levelling rare normal"},
	"Flanged Mace": {"base": "Flanged Mace", "class": "One Hand Mace", "other": ["ItemLevel <= 52"], "type": "levelling rare normal"},
	"Ornate Mace": {"base": "Ornate Mace", "class": "One Hand Mace", "other": ["ItemLevel <= 55"], "type": "levelling rare normal"},
	"Phantom Mace": {"base": "Phantom Mace", "class": "One Hand Mace", "other": ["ItemLevel <= 58"], "type": "levelling rare normal"},
	"Dragon Mace": {"base": "Dragon Mace", "class": "One Hand Mace", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Ancestral Club": {"base": "Ancestral Club", "class": "One Hand Mace", "other": ["ItemLevel <= 61"], "type": "levelling rare normal"},
	"Tenderizer": {"base": "Tenderizer", "class": "One Hand Mace", "other": ["ItemLevel <= 63"], "type": "levelling rare normal"},
	"Gavel": {"base": "Gavel", "class": "One Hand Mace", "other": ["ItemLevel <= 65"], "type": "levelling rare normal"},
	"Legion Hammer": {"base": "Legion Hammer", "class": "One Hand Mace", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Pernarch": {"base": "Pernarch", "class": "One Hand Mace", "other": ["ItemLevel <= 69"], "type": "ignore"},
	"Auric Mace": {"base": "Auric Mace", "class": "One Hand Mace", "other": ["ItemLevel <= 71"], "type": "ignore"},
	"Nightmare Mace": {"base": "Nightmare Mace", "class": "One Hand Mace", "other": ["ItemLevel <= 73"], "type": "ignore"},
	"Behemoth Mace": {"base": "Behemoth Mace", "class": "One Hand Mace", "other": ["ItemLevel <= 75"], "type": "ignore"}
}
