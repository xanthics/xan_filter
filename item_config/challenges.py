#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher

desc = "challenge item"


# Base type : settings pair
items = {
	"1 Small Cluster Jewel": {"baseexact": "Small Cluster Jewel", "class": "Jewel", "type": "show normal"},
	"1 Medium Cluster Jewel": {"baseexact": "Medium Cluster Jewel", "class": "Jewel", "other": ['EnchantmentPassiveNum <= 5'], "type": "show normal"},
	"1 Large Cluster Jewel": {"baseexact": "Large Cluster Jewel", "class": "Jewel", "other": ['EnchantmentPassiveNum <= 8'], "type": "show normal"},
	"2 Any Cluster Jewel": {"base": "Cluster Jewel", "class": "Jewel", "type": "show low"},

	# initial Heist highlighting
	"1 Heist Any 83+": {"class": "Heist", "other": ["ItemLevel >= 83"], "type": "challenge normal"},
	"2 Heist Any": {"class": "Heist", "type": "challenge low"},
	"1 Trinket": {"class": "Trinket", "type": "challenge high"},
	"1 Blueprint": {"class": "Blueprint", "type": "challenge high"},

#	"0 Contract": {"other": ["ItemLevel >= 83"], "class": "Contract", "type": "challenge high"},
#	"1 Contract": {"other": ["ItemLevel >= 75"], "class": "Contract", "type": "challenge normal"},
#	"2 Contract": {"class": "Contract", "type": "challenge low"},
}
