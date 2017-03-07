#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Warbands"

# Base type : settings pair
items = {
	# Brinerot: Your Flasks grant 30% increased Rarity of Items found while using a Flask (gloves)
	"0 Brinerot magic item": {"class": "Gloves", "other": ["Rarity Magic", "SetBorderColor 255 215 0", "Identified True"], "type": "hide"},
	# Mutewind: Cannot Be Frozen (boots)
	"0 Mutewind magic item": {"class": "Boots", "other": ["Rarity Magic", "SetBorderColor 54 100 146", "Identified True"], "type": "hide"},
	# Redblade: 10% of Physical Damage taken as Fire Damage (helmets)
	"0 Redblade magic item": {"class": "Helm", "other": ["Rarity Magic", "SetBorderColor 150 0 0", "Identified True"], "type": "hide"},
	# Renegades: Betrayer's: Damage Penetrates (6 to 10)% Fire Resistance (weapons)
	# Renegades: Deceiver's: Damage Penetrates (6 to 10)% Cold Resistance (weapons)
	# Renegades: Turncoat's: Damage Penetrates (6 to 10)% Lightning Resistance (weapons)
	"0 Renegade magic item": {"other": ["Class Dagger Wand \"One Hand\" Bow Stave \"Two Hand\" Sceptre Claws", "Rarity Magic", "SetBorderColor 208 32 144", "Identified True"], "type": "hide"},
}
