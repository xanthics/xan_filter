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
	"Corroded Blade": {"base": "Corroded Blade", "class": "Two Hand Sword", "other": ["ItemLevel <= 8"], "type": "levelling rare normal"},
	"Longsword": {"base": "Longsword", "class": "Two Hand Sword", "other": ["ItemLevel <= 13"], "type": "levelling rare normal"},
	"Bastard Sword": {"base": "Bastard Sword", "class": "Two Hand Sword", "other": ["ItemLevel <= 17"], "type": "levelling rare normal"},
	"Two-Handed Sword": {"base": "Two-Handed Sword", "class": "Two Hand Sword", "other": ["ItemLevel <= 22"], "type": "levelling rare normal"},
	"Etched Greatsword": {"base": "Etched Greatsword", "class": "Two Hand Sword", "other": ["ItemLevel <= 27"], "type": "levelling rare normal"},
	"Ornate Sword": {"base": "Ornate Sword", "class": "Two Hand Sword", "other": ["ItemLevel <= 32"], "type": "levelling rare normal"},
	"Spectral Sword": {"base": "Spectral Sword", "class": "Two Hand Sword", "other": ["ItemLevel <= 37"], "type": "levelling rare normal"},
	"Curved Blade": {"base": "Curved Blade", "class": "Two Hand Sword", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Butcher Sword": {"base": "Butcher Sword", "class": "Two Hand Sword", "other": ["ItemLevel <= 41"], "type": "levelling rare normal"},
	"Footman Sword": {"base": "Footman Sword", "class": "Two Hand Sword", "other": ["ItemLevel <= 45"], "type": "levelling rare normal"},
	"Highland Blade": {"base": "Highland Blade", "class": "Two Hand Sword", "other": ["ItemLevel <= 49"], "type": "levelling rare normal"},
	"Engraved Greatsword": {"base": "Engraved Greatsword", "class": "Two Hand Sword", "other": ["ItemLevel <= 53"], "type": "levelling rare normal"},
	"Tiger Sword": {"base": "Tiger Sword", "class": "Two Hand Sword", "other": ["ItemLevel <= 56"], "type": "levelling rare normal"},
	"Wraith Sword": {"base": "Wraith Sword", "class": "Two Hand Sword", "other": ["ItemLevel <= 59"], "type": "levelling rare normal"},
	"Lithe Blade": {"base": "Lithe Blade", "class": "Two Hand Sword", "other": ["ItemLevel <= 61"], "type": "levelling rare normal"},
	"Headman's Sword": {"base": "Headman's Sword", "class": "Two Hand Sword", "other": ["ItemLevel <= 62"], "type": "levelling rare normal"},
	"Reaver Sword": {"base": "Reaver Sword", "class": "Two Hand Sword", "other": ["ItemLevel <= 64"], "type": "levelling rare normal"},
	"Ezomyte Blade": {"base": "Ezomyte Blade", "class": "Two Hand Sword", "other": ["ItemLevel <= 66"], "type": "levelling rare normal"},
	"Vaal Greatsword": {"base": "Vaal Greatsword", "class": "Two Hand Sword", "other": ["ItemLevel <= 68"], "type": "levelling rare normal"},
	"Lion Sword": {"base": "Lion Sword", "class": "Two Hand Sword", "other": ["ItemLevel <= 70"], "type": "levelling rare normal"},
	"Infernal Sword": {"base": "Infernal Sword", "class": "Two Hand Sword", "other": ["ItemLevel <= 72"], "type": "levelling rare normal"},
	"Exquisite Blade": {"base": "Exquisite Blade", "class": "Two Hand Sword", "other": ["ItemLevel <= 75"], "type": "levelling rare normal"}
}
