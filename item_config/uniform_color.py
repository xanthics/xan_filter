#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Text color rules"


# Base type : settings pair
items = {
	"0 Default Background": {"type": "black background"},
	"1 Weapon 83+": {"class": 'Bow" "Staff" "Two Hand" "Claw" "Dagger" "Wand" "One Hand" "Sceptre" "Quiver', "other": ["ItemLevel >= 83"], "type": "premiumdgrey background"},
	"1 Armour 84+": {"class": 'Shield" "Gloves" "Boots" "Body Armour" "Helmet', "other": ["ItemLevel >= 84"], "type": "premiumdgrey background"},
	"1 Jewelry 84+": {"class": 'Amulet" "Ring" "Belt', "other": ["ItemLevel >= 84"], "type": "premiumdgrey background"},
	"2 Armour 86+": {"class": 'Shield" "Gloves" "Boots" "Body Armour" "Helmet', "other": ["ItemLevel >= 88"], "type": "grey background"},
}


