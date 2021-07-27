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

	"1 Exotic Coinage": {"baseexact": "Exotic Coinage", "class": "Currency", "type": "challenge normal"},
	"1 Scrap Metal": {"baseexact": "Scrap Metal", "class": "Currency", "type": "challenge normal"},
	"1 Astragali": {"baseexact": "Astragali", "class": "Currency", "type": "challenge normal"},
	"1 Burial Medallion": {"baseexact": "Burial Medallion", "class": "Currency", "type": "challenge normal"},
	"1 Lesser Broken Circle Artifact": {"baseexact": "Lesser Broken Circle Artifact", "class": "Currency", "type": "challenge normal"},
	"1 Common Broken Circle Artifact": {"baseexact": "Common Broken Circle Artifact", "class": "Currency", "type": "challenge normal"},
	"1 Greater Broken Circle Artifact": {"baseexact": "Greater Broken Circle Artifact", "class": "Currency", "type": "challenge normal"},
	"1 Grand Broken Circle Artifact": {"baseexact": "Grand Broken Circle Artifact", "class": "Currency", "type": "challenge normal"},
	"1 Lesser Black Scythe Artifact": {"baseexact": "Lesser Black Scythe Artifact", "class": "Currency", "type": "challenge normal"},
	"1 Common Black Scythe Artifact": {"baseexact": "Common Black Scythe Artifact", "class": "Currency", "type": "challenge normal"},
	"1 Greater Black Scythe Artifact": {"baseexact": "Greater Black Scythe Artifact", "class": "Currency", "type": "challenge normal"},
	"1 Grand Black Scythe Artifact": {"baseexact": "Grand Black Scythe Artifact", "class": "Currency", "type": "challenge normal"},
	"1 Lesser Order Artifact": {"baseexact": "Lesser Order Artifact", "class": "Currency", "type": "challenge normal"},
	"1 Common Order Artifact": {"baseexact": "Common Order Artifact", "class": "Currency", "type": "challenge normal"},
	"1 Greater Order Artifact": {"baseexact": "Greater Order Artifact", "class": "Currency", "type": "challenge normal"},
	"1 Grand Order Artifact": {"baseexact": "Grand Order Artifact", "class": "Currency", "type": "challenge normal"},
	"1 Lesser Sun Artifact": {"baseexact": "Lesser Sun Artifact", "class": "Currency", "type": "challenge normal"},
	"1 Common Sun Artifact": {"baseexact": "Common Sun Artifact", "class": "Currency", "type": "challenge normal"},
	"1 Greater Sun Artifact": {"baseexact": "Greater Sun Artifact", "class": "Currency", "type": "challenge normal"},
	"1 Grand Sun Artifact": {"baseexact": "Grand Sun Artifact", "class": "Currency", "type": "challenge normal"},

	# initial Heist highlighting
	"1 Heist Any 83+": {"class": "Heist", "other": ["ItemLevel >= 83"], "type": "challenge normal"},
	"2 Heist Any": {"class": "Heist", "type": "challenge low"},
	"1 Trinket": {"class": "Trinket", "type": "challenge high"},
	"1 Blueprint": {"class": "Blueprint", "type": "challenge high"},
	"1 Expedition Logbook": {"class": "Expedition Logbook", "type": "challenge high"},

	#	"0 Contract": {"other": ["ItemLevel >= 83"], "class": "Contract", "type": "challenge high"},
#	"1 Contract": {"other": ["ItemLevel >= 75"], "class": "Contract", "type": "challenge normal"},
	"2 Contract": {"class": "Contract", "type": "challenge low"},
}
