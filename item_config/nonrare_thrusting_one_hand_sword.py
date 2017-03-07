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
	"Rusted Spike": {"base": "Rusted Spike", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "leveling low"},
	"Whalebone Rapier": {"base": "Whalebone Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 12"], "type": "leveling low"},
	"Battered Foil": {"base": "Battered Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "leveling low"},
	"Basket Rapier": {"base": "Basket Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "leveling low"},
	"Jagged Foil": {"base": "Jagged Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 27"], "type": "leveling low"},
	"Antique Rapier": {"base": "Antique Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 31"], "type": "leveling low"},
	"Elegant Foil": {"base": "Elegant Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 35"], "type": "leveling low"},
	"Thorn Rapier": {"base": "Thorn Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "leveling low"},
	"Smallsword": {"base": "Smallsword", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "leveling low"},
	"Wyrmbone Rapier": {"base": "Wyrmbone Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "leveling low"},
	"Burnished Foil": {"base": "Burnished Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 45"], "type": "leveling low"},
	"Estoc": {"base": "Estoc", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 48"], "type": "leveling low"},
	"Serrated Foil": {"base": "Serrated Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 51"], "type": "ignore"},
	"Primeval Rapier": {"base": "Primeval Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "ignore"},
	"Fancy Foil": {"base": "Fancy Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 57"], "type": "ignore"},
	"Apex Rapier": {"base": "Apex Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Courtesan Sword": {"base": "Courtesan Sword", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "ignore"},
	"Dragonbone Rapier": {"base": "Dragonbone Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Tempered Foil": {"base": "Tempered Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "ignore"},
	"Pecoraro": {"base": "Pecoraro", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Spiraled Foil": {"base": "Spiraled Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "ignore"},
	"Vaal Rapier": {"base": "Vaal Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "ignore"},
	"Jewelled Foil": {"base": "Jewelled Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"},
	"Harpy Rapier": {"base": "Harpy Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"},
	"Dragoon Sword": {"base": "Dragoon Sword", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 77"], "type": "ignore"}}
