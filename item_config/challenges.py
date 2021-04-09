#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher

desc = "challenge item"


# Base type : settings pair
items = {
	"1 Cluster Jewel": {"base": "Cluster Jewel", "class": "Jewel", "type": "show normal"},
	# ritual bases for challenge
#	"1 Archdemon Crown": {"baseexact": "Archdemon Crown", "type": "show normal"},
	"1 Blizzard Crown": {"baseexact": "Blizzard Crown", "type": "show normal"},
#	"1 Brimstone Treads": {"baseexact": "Brimstone Treads", "type": "show normal"},
#	"1 Debilitation Gauntlets": {"baseexact": "Debilitation Gauntlets", "type": "show normal"},
	"1 Dreamquest Slippers": {"baseexact": "Dreamquest Slippers", "type": "show normal"},
#	"1 Nexus Gloves": {"baseexact": "Nexus Gloves", "type": "show normal"},
#	"1 Penitent Mask": {"baseexact": "Penitent Mask", "type": "show normal"},
#	"1 Sinistral Gloves": {"baseexact": "Sinistral Gloves", "type": "show normal"},
#	"1 Stormrider Boots": {"baseexact": "Stormrider Boots", "type": "show normal"},

	# initial Heist highlighting
	"1 Heist Any 83+": {"class": "Heist", "other": ["ItemLevel >= 83"], "type": "challenge normal"},
	"2 Heist Any": {"class": "Heist", "type": "challenge low"},
	"1 Trinket": {"class": "Trinket", "type": "challenge high"},
	"1 Blueprint": {"class": "Blueprint", "type": "challenge high"},

#	"0 Contract": {"other": ["ItemLevel >= 83"], "class": "Contract", "type": "challenge high"},
#	"1 Contract": {"other": ["ItemLevel >= 75"], "class": "Contract", "type": "challenge normal"},
#	"2 Contract": {"class": "Contract", "type": "challenge low"},
}
