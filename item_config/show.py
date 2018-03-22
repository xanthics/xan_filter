#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Always show"

# Base type : settings pair
items = {
	"01 Tabula Exception": {"base": "Simple Robe", "other": ["Rarity Unique", "SocketGroup WWWWWW"], "type": "unique high"},
	"02 6L": {"other": ["LinkedSockets 6"], "type": "show very high"},
	"03 5L": {"other": ["Rarity < Unique", "Sockets 5", "LinkedSockets 5", "PlayAlertSound 2 15"], "type": "show high"},
	"04 6S": {"other": ["Sockets 6", "PlayAlertSound 2 50"], "type": "show high"},
	# High value atlas bases.  Show and make noise at any rarity
	"04 Steel Ring": {"other": ["PlayAlertSound 2 50"], "base": "Steel Ring", "type": "show high"},
	"04 Crystal Belt": {"base": "Crystal Belt", "type": "ignore"},
	"04 Stygian Vise": {"other": ["PlayAlertSound 2 50"], "base": "Stygian Vise", "type": "show high"},
	"04 Opal Ring": {"other": ["PlayAlertSound 2 50"], "base": "Opal Ring", "type": "show high"},
	"04 84+ Ghastly Abyss Jewel": {"base": "Ghastly", "other": ["ItemLevel >= 84"], "class": "Abyss Jewel", "type": "show normal"},
	"04 84+ Hypnotic Abyss Jewel": {"base": "Hypnotic", "other": ["ItemLevel >= 84"], "class": "Abyss Jewel", "type": "show normal"},
	"04 82+ Murderous Abyss Jewel": {"base": "Murderous", "other": ["ItemLevel >= 82"], "class": "Abyss Jewel", "type": "show high"},
	"04 82+ Searching Eye Abyss Jewel": {"base": "Searching Eye", "other": ["ItemLevel >= 82"], "class": "Abyss Jewel", "type": "show high"},
	"04 Abyss Jewel": {"class": "Abyss Jewel", "type": "normal"},
	"10 Talisman": {"class": "Amulets", 'other': ["Rarity >= Rare", "ItemLevel >= 70"], "base": "Talisman", "type": "show high"},
	"11 Talisman": {"class": "Amulets", 'other': ["ItemLevel >= 70"], "base": "Talisman", "type": "show high"},
	"12 Talisman": {"class": "Amulets", "base": "Talisman", "type": "show low"},
	"0 Fishing Rod": {"base": "Fishing Rod", "type": "show very high"},
	"0 Hideout Doodads": {"class": "Hideout Doodads", "type": "show low"},
	"0 Microtransactions": {"class": "Microtransactions", "type": "show low"},
	"0 Quest": {"class": "Quest", "type": "quest"},
	"0 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "show normal"},
	"1 Jewel": {"class": "Jewel", "other": ["Rarity <= Magic"], "type": "ignore"},
	"0 Strong Steel Net": {"base": "Strong Steel Net", "class": "Currency", "type": "currency low"},
	"0 Thaumaturgical Net": {"base": "Thaumaturgical Net", "class": "Currency", "type": "show normal"},
	"0 Necromancy Net": {"other": ["PlayAlertSound 2 50"], "base": "Necromancy Net", "class": "Currency", "type": "show high"},
	"1 Rope Net": {"base": "Rope Net", "class": "Currency", "type": "hide"},
	"1 Iron Net": {"base": "Iron Net", "class": "Currency", "type": "hide"},
	"1 Steel Net": {"base": "Steel Net", "class": "Currency", "type": "hide"},

	"9 Starter weapon": {"other": ["Class Dagger Wand \"One Hand\" Bow Stave \"Two Hand\" Sceptre Claws", "ItemLevel < 2"], "type": "show normal"},

	# Corrupted white items for lead to gold darkshrine
	#"0 corrupted amulet": {"class": "Amulets", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "show normal"},
	#"0 corrupted ring": {"class": "Rings", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "ignore"},
	#"0 corrupted belt": {"class": "Belts", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "show normal"},
	#"0 corrupted quiver": {"class": "Quivers", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "ignore"},
	#"0 corrupted gloves": {"class": "Gloves", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "ignore"},
	#"0 corrupted boots": {"class": "Boots", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "ignore"},
	#"0 corrupted shield": {"class": "Shield", "other": ["Corrupted True", "Rarity Normal", "ItemLevel >= 60"], "type": "ignore"},

	# Rare highlighting for currency recipes.  change 'ignore' to 'high' or back as needed
	"0 Rare Two Hand": {"class": "Two Hand\" \"Staves\" \"Bow", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},
	"0 Rare Helm": {"class": "Helmets", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},
	"0 Rare Body": {"class": "Body Armours", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},
	"0 Rare Glove": {"class": "Gloves", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},
	"0 Rare Boot": {"class": "Boots", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},

	"02 60+ amulet": {"class": "Amulets", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},
	"02 60+ ring": {"class": "Rings", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},
	"02 60+ belt": {"class": "Belts", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},

}
