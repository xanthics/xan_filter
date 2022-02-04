#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher

desc = "challenge item"


# Base type : settings pair
items = {
	"1 Exotic Coinage": {"baseexact": "Exotic Coinage", "class": "Currency", "type": "challenge normal"},
	"1 Scrap Metal": {"baseexact": "Scrap Metal", "class": "Currency", "type": "challenge normal"},
	"1 Astragali": {"baseexact": "Astragali", "class": "Currency", "type": "challenge normal"},
	"1 Burial Medallion": {"baseexact": "Burial Medallion", "class": "Currency", "type": "challenge normal"},

	"1 Archnemesis Items": {"class": "Archnemesis Mod", "type": "challenge normal"},
	# initial Heist highlighting
	"2 Heist Any": {"class": "Heist", "type": "challenge low"},
	"1 Trinket": {"class": "Trinket", "type": "challenge high"},
	"1 Blueprint": {"class": "Blueprint", "type": "challenge high"},

	"1 Expedition Logbook": {"class": "Expedition Logbook", "type": "challenge high"},

	"0 Contract": {"other": ["ItemLevel >= 83"], "class": "Contract", "type": "challenge high"},
#	"1 Contract": {"other": ["ItemLevel >= 75"], "class": "Contract", "type": "challenge normal"},
	"2 Contract": {"class": "Contract", "type": "challenge low"},
}

for base in [
	'Sharpening Stone', 'Arrowhead', 'Focal Stone', 'Conduit Line', 'Aggregator Charm', 'Burst Band',
	'Lockpick',  # Karst
	'Bracers',  # Tibbs
	'Drill',  # Isla
	'Sole',  # Tullina
	'Ward',  # Niles
	'Sensing Charm',  # Nenet
	'Flashpowder',  # Vinderi
	'Keyring',  # Vinderi
	'Disguise Kit',  # Gianna
	'Cloak',
	'Brooch'
]:
	items[f"1 Heist {base} 83+"] = {'base': base, "class": "Heist", "other": ["ItemLevel >= 83"], "type": "challenge normal"}
