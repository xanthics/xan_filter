#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Animate Weapon target"

# types intended for this is "animate melee" and "animate range"

# Base type : settings pair
items = {
	"0 animate melee white 4x1": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Normal", "Height 4", "Width 1"], "type": "animate melee b"},
	"0 animate range white 4x1": {"other": ["Class Wand Bow", "Rarity Normal", "Height 4", "Width 1"], "type": "ignore"},
	"0 animate melee magic 4x1": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Magic", "Height 4", "Width 1", "Identified True"], "type": "animate melee b"},
	"0 animate range magic 4x1": {"other": ["Class Wand Bow", "Rarity Magic", "Height 4", "Width 1", "Identified True"], "type": "ignore"},

	"0 animate melee white 3x1": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Normal", "Height 3", "Width 1"], "type": "animate melee b"},
	"0 animate range white 3x1": {"other": ["Class Wand Bow", "Rarity Normal", "Height 3", "Width 1"], "type": "ignore"},
	"0 animate melee magic 3x1": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Magic", "Height 3", "Width 1", "Identified True"], "type": "animate melee b"},
	"0 animate range magic 3x1": {"other": ["Class Wand Bow", "Rarity Magic", "Height 3", "Width 1", "Identified True"], "type": "ignore"},

	"0 animate melee white 2x2": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Normal", "Height 2", "Width 2"], "type": "animate melee b"},
	"0 animate range white 2x2": {"other": ["Class Wand Bow", "Rarity Normal", "Height 2", "Width 2"], "type": "ignore"},
	"0 animate melee magic 2x2": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Magic", "Height 2", "Width 2", "Identified True"], "type": "animate melee b"},
	"0 animate range magic 2x2": {"other": ["Class Wand Bow", "Rarity Magic", "Height 2", "Width 2", "Identified True"], "type": "ignore"},

	"1 animate melee white": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Normal"], "type": "animate melee"},
	"1 animate range white": {"other": ["Class Wand Bow", "Rarity Normal"], "type": "ignore"},
	"1 animate melee magic": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Magic", "Identified True"], "type": "animate melee"},
	"1 animate range magic": {"other": ["Class Wand Bow", "Rarity Magic", "Identified True"], "type": "ignore"},
}