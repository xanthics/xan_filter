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
	"Nailed Fist": {"base": "Nailed Fist", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "leveling low"},
	"Sharktooth Claw": {"base": "Sharktooth Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 12"], "type": "leveling low"},
	"Awl": {"base": "Awl", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "leveling low"},
	"Cat's Paw": {"base": "Cat's Paw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "leveling low"},
	"Blinder": {"base": "Blinder", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 27"], "type": "leveling low"},
	"Timeworn Claw": {"base": "Timeworn Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 31"], "type": "leveling low"},
	"Sparkling Claw": {"base": "Sparkling Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 35"], "type": "leveling low"},
	"Fright Claw": {"base": "Fright Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "leveling low"},
	"Double Claw": {"base": "Double Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "leveling low"},
	"Thresher Claw": {"base": "Thresher Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "leveling low"},
	"Gouger": {"base": "Gouger", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 45"], "type": "leveling low"},
	"Tiger's Paw": {"base": "Tiger's Paw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 48"], "type": "leveling low"},
	"Gut Ripper": {"base": "Gut Ripper", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 51"], "type": "ignore"},
	"Prehistoric Claw": {"base": "Prehistoric Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "ignore"},
	"Noble Claw": {"base": "Noble Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 57"], "type": "ignore"},
	"Eagle Claw": {"base": "Eagle Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Twin Claw": {"base": "Twin Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "ignore"},
	"Great White Claw": {"base": "Great White Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Throat Stabber": {"base": "Throat Stabber", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "ignore"},
	"Hellion's Paw": {"base": "Hellion's Paw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Eye Gouger": {"base": "Eye Gouger", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "ignore"},
	"Vaal Claw": {"base": "Vaal Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "ignore"},
	"Imperial Claw": {"base": "Imperial Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"},
	"Terror Claw": {"base": "Terror Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"},
	"Gemini Claw": {"base": "Gemini Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 77"], "type": "ignore"}
}
