#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Always show"

# Base type : settings pair
items = {
	"01 Tabula Exception": {"base": "Simple Robe", "other": ["Rarity Unique", "SocketGroup WWWWWW"], "type": "unique high"},
	"02 6L": {"other": ["LinkedSockets 6"], "type": "show very high"},
	"03 6S": {"other": ["Sockets 6", 'CustomAlertSound "45_show.wav"'], "type": "show high"},
	"04 5L": {"other": ["Rarity < Unique", "LinkedSockets 5", 'CustomAlertSound "20_show.wav"'], "type": "show high"},
	"04 Incursion Item": {"other": ['CustomAlertSound "45_show.wav"'], "class": "Incursion Item", "type": "show high"},
	"04 Timeworn Reliquary Key": {"base": "Timeworn Reliquary Key", "class": "Misc Map Items", "type": "map very good"},
	# High value atlas bases.  Show and make noise at any rarity
	"0 Fishing Rod": {"base": "Fishing Rod", "type": "show very high"},
	"0 Hideout Doodads": {"class": "Hideout Doodads", "type": "show low"},
	"0 Microtransactions": {"class": "Microtransactions", "type": "show low"},
	"0 Quest": {"class": "Quest", "type": "quest"},
	"0 Thaumaturgical Net": {"base": "Thaumaturgical Net", "class": "Currency", "type": "show normal"},
	"0 Necromancy Net": {"other": ['CustomAlertSound "45_show.wav"'], "base": "Necromancy Net", "class": "Currency", "type": "show high"},
	"0 Strong Steel Net": {"base": "Strong Steel Net", "class": "Currency", "type": "ignore"},
	# TODO: Fix this so it is only nets again -- clashes with uul-netol shards
	"1 Net": {"base": "Net", "class": "Currency", "type": "ignore"},

	"9 Starter weapon": {"other": ["Class Dagger Wand \"One Hand\" Bow Stave \"Two Hand\" Sceptre Claws", "ItemLevel < 2"], "type": "show normal"},

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
