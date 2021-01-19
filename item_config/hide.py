#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Always Hide"

# Base type : settings pair
items = {
	# bad currency
	"0 Scroll Fragment": {"baseexact": "Scroll Fragment", "class": "Currency", "type": "hide"},
	"1 Muttering Essence": {"base": "Muttering Essence", 'other': ['AreaLevel > 67'], "class": "Currency", "type": "hide"},
	"1 Wailing Essence": {"base": "Wailing Essence", 'other': ['AreaLevel > 67'], "class": "Currency", "type": "hide"},
	"1 Weeping Essence": {"base": "Weeping Essence", 'other': ['AreaLevel > 67'], "class": "Currency", "type": "hide"},
	"1 Whispering Essence": {"base": "Whispering Essence", 'other': ['AreaLevel > 67'], "class": "Currency", "type": "hide"},

	# bad div cards
	"1 Blessing of God": {"baseexact": "Blessing of God", "class": "Divination Card", "type": "hide"},
	"1 Death": {"baseexact": "Death", "class": "Divination Card", "type": "hide"},
	"1 Destined to Crumble": {"baseexact": "Destined to Crumble", "class": "Divination Card", "type": "hide"},
	"1 Lantador's Lost Love": {"baseexact": "Lantador's Lost Love", "class": "Divination Card", "type": "hide"},
	"1 Merciless Armament": {"baseexact": "Merciless Armament", "class": "Divination Card", "type": "hide"},
	"1 Prosperity": {"baseexact": "Prosperity", "class": "Divination Card", "type": "hide"},
	"1 Rain Tempter": {"baseexact": "Rain Tempter", "class": "Divination Card", "type": "hide"},
	"1 Struck by Lightning": {"baseexact": "Struck by Lightning", "class": "Divination Card", "type": "hide"},
	"1 The Carrion Crow": {"baseexact": "The Carrion Crow", "class": "Divination Card", "type": "hide"},
	"1 The Inoculated": {"baseexact": "The Inoculated", "class": "Divination Card", "type": "hide"},
	"1 The Jester": {"baseexact": "The Jester", "class": "Divination Card", "type": "hide"},
	"1 The King's Blade": {"baseexact": "The King's Blade", "class": "Divination Card", "type": "hide"},
	"1 The Lord in Black": {"baseexact": "The Lord in Black", "class": "Divination Card", "type": "hide"},
	"1 The Lover": {"baseexact": "The Lover", "class": "Divination Card", "type": "hide"},
	"1 The Metalsmith's Gift": {"baseexact": "The Metalsmith's Gift", "class": "Divination Card", "type": "hide"},
	"1 The Mountain": {"baseexact": "The Mountain", "class": "Divination Card", "type": "hide"},
	"1 The Opulent": {"baseexact": "The Opulent", "class": "Divination Card", "type": "hide"},
	"1 The Rabid Rhoa": {"baseexact": "The Rabid Rhoa", "class": "Divination Card", "type": "hide"},
	"1 The Road to Power": {"baseexact": "The Road to Power", "class": "Divination Card", "type": "hide"},
	"1 The Scarred Meadow": {"baseexact": "The Scarred Meadow", "class": "Divination Card", "type": "hide"},
	"1 The Sigil": {"baseexact": "The Sigil", "class": "Divination Card", "type": "hide"},
	"1 The Spoiled Prince": {"baseexact": "The Spoiled Prince", "class": "Divination Card", "type": "hide"},
	"1 The Surgeon": {"baseexact": "The Surgeon", "class": "Divination Card", "type": "hide"},
	"1 The Twins": {"baseexact": "The Twins", "class": "Divination Card", "type": "hide"},
	"1 The Tyrant": {"baseexact": "The Tyrant", "class": "Divination Card", "type": "hide"},
	"1 The Undisputed": {"baseexact": "The Undisputed", "class": "Divination Card", "type": "hide"},
	"1 Thunderous Skies": {"baseexact": "Thunderous Skies", "class": "Divination Card", "type": "hide"},
	"1 Vile Power": {"baseexact": "Vile Power", "class": "Divination Card", "type": "hide"},
	"1 Her Mask": {"baseexact": "Her Mask", "class": "Divination Card", "type": "hide"},
	"1 The Gambler": {"baseexact": "The Gambler", "class": "Divination Card", "type": "hide"},
	"1 The Warden": {"baseexact": "The Warden", "class": "Divination Card", "type": "hide"},

	# bad incubators
	"1 Whispering Incubator": {"base": "Whispering Incubator", "class": "Incubator", "type": "hide"},
	"1 Primal Incubator": {"base": "Primal Incubator", "class": "Incubator", "type": "hide"},
	"1 Abyssal Incubator": {"base": "Abyssal Incubator", "class": "Incubator", "type": "hide"},
	# bad incubators at low ilvl
	"1 Celestial Jeweller's Incubator": {"base": "Celestial Jeweller's Incubator", 'other': ['ItemLevel < 73'], "class": "Incubator", "type": "hide"},
	"1 Celestial Blacksmith's Incubator": {"base": "Celestial Blacksmith's Incubator", 'other': ['ItemLevel < 84'], "class": "Incubator", "type": "hide"},
	"1 Celestial Armoursmith's Incubator": {"base": "Celestial Armoursmith's Incubator", 'other': ['ItemLevel < 83'], "class": "Incubator", "type": "hide"},
}
