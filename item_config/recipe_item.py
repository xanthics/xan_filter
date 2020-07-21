#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Recipe Item"

# Base type : settings pair
items = {
	# toogle between 'ignore' or 'recipe item normal'
	"0 rare hammers q>=16": {"base": "Stone Hammer\" \"Rock Breaker\" \"Gavel", "other": ["Rarity Rare", "Quality >= 16"], "type": "ignore"},
	"0 magic hammers q>=12": {"base": "Stone Hammer\" \"Rock Breaker\" \"Gavel", "other": ["Rarity Magic", "Quality >= 12"], "type": "ignore"},
	"0 normal hammers": {"base": "Stone Hammer\" \"Rock Breaker\" \"Gavel", "other": ["Rarity Normal"], "type": "ignore"},

	# Rare highlighting for currency recipes.  change 'ignore' to 'recipe item rare' or back as needed
#	"1 Chaos Rare Two Hand": {"class": "Two Hand\" \"Staves\" \"Bow", "other": ["Height 4", "Width 2", "Rarity Rare", "ItemLevel >= 60", "ItemLevel <= 74", "Identified False"], "type": "recipe item rare"},
#	"1 Chaos Rare Helm": {"class": "Helmets", "other": ["Rarity Rare", "ItemLevel >= 60", "ItemLevel <= 74", "Identified False"], "type": "recipe item rare small"},
#	"1 Chaos Rare Body": {"class": "Body Armours", "other": ["Rarity Rare", "ItemLevel >= 60", "ItemLevel <= 74", "Identified False"], "type": "recipe item rare"},
#	"1 Chaos Rare Glove": {"class": "Gloves", "other": ["Rarity Rare", "ItemLevel >= 60", "ItemLevel <= 74", "Identified False"], "type": "recipe item rare small"},
#	"1 Chaos Rare Boot": {"class": "Boots", "other": ["Rarity Rare", "ItemLevel >= 60", "ItemLevel <= 74", "Identified False"], "type": "recipe item rare small"},
#	"1 Chaos Rare Amulet": {"class": "Amulet", "other": ["Rarity Rare", "ItemLevel >= 60", "ItemLevel <= 74", "Identified False"], "type": "recipe item rare small"},
#	"1 Chaos Rare Ring": {"class": "Ring", "other": ["Rarity Rare", "ItemLevel >= 60", "ItemLevel <= 74", "Identified False"], "type": "recipe item rare small"},
#	"1 Chaos Rare Belt": {"class": "Belt", "other": ["Rarity Rare", "ItemLevel >= 60", "ItemLevel <= 74", "Identified False"], "type": "recipe item rare small"},

	# Rare highlighting for currency recipes.  change 'ignore' to 'recipe item rare' or back as needed
#	"1 Regal Rare Two Hand": {"class": "Two Hand\" \"Staves\" \"Bow", "other": ["Height 4", "Width 2", "Rarity Rare", "ItemLevel >= 75", "Identified False"], "type": "recipe item rare"},
#	"1 Regal Rare Helm": {"class": "Helmets", "other": ["Rarity Rare", "ItemLevel >= 75", "Identified False"], "type": "recipe item rare small"},
#	"1 Regal Rare Body": {"class": "Body Armours", "other": ["Rarity Rare", "ItemLevel >= 75", "Identified False"], "type": "recipe item rare"},
#	"1 Regal Rare Glove": {"class": "Gloves", "other": ["Rarity Rare", "ItemLevel >= 75", "Identified False"], "type": "recipe item rare small"},
#	"1 Regal Rare Boot": {"class": "Boots", "other": ["Rarity Rare", "ItemLevel >= 75", "Identified False"], "type": "recipe item rare small"},
#	"1 Regal Rare Amulet": {"class": "Amulet", "other": ["Rarity Rare", "ItemLevel >= 75", "Identified False"], "type": "recipe item rare small"},
#	"1 Regal Rare Ring": {"class": "Ring", "other": ["Rarity Rare", "ItemLevel >= 75", "Identified False"], "type": "recipe item rare small"},
#	"1 Regal Rare Belt": {"class": "Belt", "other": ["Rarity Rare", "ItemLevel >= 75", "Identified False"], "type": "recipe item rare small"},
}