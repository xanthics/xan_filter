#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Always show"

# Base type : settings pair
items = {
	"0 Leaguestone": {"class": "Leaguestone", "type": "show high"},
	"01 Tabula Exception": {"baseexact": "Simple Robe", "other": ["SocketGroup WWWWWW"], "type": "unique high"},
	"02 6L": {"other": ["LinkedSockets 6"], "type": "show high"},
	"03 6S": {"other": ["Sockets 6"], "type": "currency normal"},
	"04 5L": {"other": ["Rarity < Unique", "LinkedSockets 5", 'CustomAlertSound "high_5link"'], "type": "show normal"},
	"04 Incursion Item": {"class": "Incursion Item", "type": "show high"},
	"04 Timeworn Reliquary Key": {"baseexact": "Timeworn Reliquary Key", "class": "Misc Map Items", "type": "show high"},
	# High value atlas bases.  Show and make noise at any rarity
	"0 Fishing Rod": {"baseexact": "Fishing Rod", "type": "show very high"},
	"0 Hideout Doodads": {"class": "Hideout Doodads", "type": "show low"},
	"0 Microtransactions": {"class": "Microtransactions", "type": "show low"},
	"0 Quest": {"class": "Quest", "type": "quest"},
	"1 Cobalt Watchstone": {"baseexact": "Cobalt Watchstone", "type": "quest"},
	"1 Crimson Watchstone": {"baseexact": "Crimson Watchstone", "type": "quest"},
	"1 Golden Watchstone": {"baseexact": "Golden Watchstone", "type": "quest"},
	"1 Viridian Watchstone": {"baseexact": "Viridian Watchstone", "type": "quest"},

	"9 Starter weapon": {"other": ["Class Dagger Wand \"One Hand\" Bow Stave \"Two Hand\" Sceptre Claws", "ItemLevel < 2"], "type": "show normal"},
}
