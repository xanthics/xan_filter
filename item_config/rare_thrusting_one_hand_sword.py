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
	"Rusted Spike": {"base": "Rusted Spike", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 8"], "type": "levelling rare normal"},
	"Whalebone Rapier": {"base": "Whalebone Rapier", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 12"], "type": "levelling rare normal"},
	"Battered Foil": {"base": "Battered Foil", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 17"], "type": "levelling rare normal"},
	"Basket Rapier": {"base": "Basket Rapier", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 22"], "type": "levelling rare normal"},
	"Jagged Foil": {"base": "Jagged Foil", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 27"], "type": "levelling rare normal"},
	"Antique Rapier": {"base": "Antique Rapier", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 31"], "type": "levelling rare normal"},
	"Elegant Foil": {"base": "Elegant Foil", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 35"], "type": "levelling rare normal"},
	"Thorn Rapier": {"base": "Thorn Rapier", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 39"], "type": "levelling rare normal"},
	"Smallsword": {"base": "Smallsword", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 41"], "type": "levelling rare normal"},
	"Wyrmbone Rapier": {"base": "Wyrmbone Rapier", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 42"], "type": "levelling rare normal"},
	"Burnished Foil": {"base": "Burnished Foil", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 45"], "type": "levelling rare normal"},
	"Estoc": {"base": "Estoc", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 48"], "type": "levelling rare normal"},
	"Serrated Foil": {"base": "Serrated Foil", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 51"], "type": "levelling rare normal"},
	"Primeval Rapier": {"base": "Primeval Rapier", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 54"], "type": "levelling rare normal"},
	"Fancy Foil": {"base": "Fancy Foil", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 57"], "type": "levelling rare normal"},
	"Apex Rapier": {"base": "Apex Rapier", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Courtesan Sword": {"base": "Courtesan Sword", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 62"], "type": "levelling rare normal"},
	"Dragonbone Rapier": {"base": "Dragonbone Rapier", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 63"], "type": "levelling rare normal"},
	"Tempered Foil": {"base": "Tempered Foil", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 65"], "type": "levelling rare normal"},
	"Pecoraro": {"base": "Pecoraro", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Spiraled Foil": {"base": "Spiraled Foil", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 69"], "type": "levelling rare normal"},
	"Vaal Rapier": {"base": "Vaal Rapier", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 71"], "type": "levelling rare normal"},
	"Jewelled Foil": {"base": "Jewelled Foil", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 73"], "type": "levelling rare normal"},
	"Harpy Rapier": {"base": "Harpy Rapier", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 75"], "type": "levelling rare normal"},
	"Dragoon Sword": {"base": "Dragoon Sword", "class": "Thrusting One Hand Sword", "other": ["ItemLevel <= 77"], "type": "levelling rare normal"}}
