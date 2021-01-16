#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher

desc = "challenge item"


# Base type : settings pair
items = {
	"1 Cluster Jewel": {"base": "Cluster Jewel", "class": "Jewel", "type": "show high"},

	# initial Heist highlighting
	"1 Heist Any 83+": {"class": "Heist", "other": ["ItemLevel >= 83"], "type": "challenge normal"},
	"2 Heist Any": {"class": "Heist", "type": "challenge low"},
	"1 Trinket": {"class": "Trinket", "type": "challenge high"},
	"1 Blueprint": {"class": "Blueprint", "type": "challenge high"},
	"1 Prime Regrading Lens": {"baseexact": "Prime Regrading Lens", "class": "Currency", "type": "challenge normal"},
	"1 Secondary Regrading Lens": {"baseexact": "Secondary Regrading Lens", "class": "Currency", "type": "challenge normal"},
	"1 Tempering Orb": {"baseexact": "Tempering Orb", "class": "Currency", "type": "challenge normal"},
	"1 Tailoring Orb": {"baseexact": "Tailoring Orb", "class": "Currency", "type": "challenge normal"},

	"0 Contract": {"other": ["ItemLevel >= 83"], "class": "Contract", "type": "challenge high"},
	"1 Contract": {"other": ["ItemLevel >= 75"], "class": "Contract", "type": "challenge normal"},
	"2 Contract": {"class": "Contract", "type": "challenge low"},
}
