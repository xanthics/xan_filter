#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "gems"

# Base type : settings pair
items = {
	"0 Leveled Gem ": {"class": "Gems", "other": ["GemLevel >= 19"], "type": "ignore"},
	"01 Quality Gem 20": {"class": "Gems", "other": ["Quality >= 20"], "type": "ignore"},
	"02 Quality Gem High": {"class": "Gems", "other": ["Quality >= 10"], "type": "gem normal"},
	"03 Quality Gem": {"class": "Gems", "other": ["Quality >= 1"], "type": "ignore"},
	"04 Leveled Gem ": {"class": "Gems", "other": ["GemLevel >= 2"], "type": "gem low"},
	"1 Portal": {"baseexact": "Portal", "class": "Gems", "type": "gem normal"},
	"1 Empower": {"baseexact": "Empower Support", "class": "Gems", "type": "ignore"},
	"1 Enhance": {"baseexact": "Enhance Support", "class": "Gems", "type": "ignore"},
	"1 Enlighten": {"baseexact": "Enlighten Support", "class": "Gems", "type": "ignore"},
	"6 Awakened Gems": {"base": 'Awakened', "class": "Gems", "type": "gem high"},
	"7 Vaal Gems": {"base": "Vaal", "class": "Gems", "type": "ignore"},
	"8 Other Gems Leveling": {"class": "Gems", "other": ["AreaLevel < 68"], "type": "gem low"},
	"9 Other Gems": {"class": "Gems", "type": "ignore"},
}