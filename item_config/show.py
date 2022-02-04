#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Always show"

# Base type : settings pair
items = {
	"0 Leaguestone": {"class": "Leaguestone", "type": "show high"},
	"01 Tabula Exception": {"baseexact": "Simple Robe", "other": ["SocketGroup WWWWWW"], "type": "unique high"},
	"01 The Squire Exception": {"baseexact": "Elegant Round Shield", "other": ["Sockets WWW"], "type": "unique extremely high"},
	"02 6L": {"other": ["Rarity < Unique", "LinkedSockets 6"], "type": "show high"},
	"03 6S": {"other": ["Rarity < Unique", "Sockets 6"], "type": "show normal quiet"},
	"04 5L": {"other": ["Rarity < Unique", "LinkedSockets 5", 'CustomAlertSound "high_5link"'], "type": "normal border"},
	"04 Incursion Item": {"class": "Incursion Item", "type": "show high"},
	"04 Reliquary Key": {"base": "Reliquary Key", "class": "Misc Map Items", "type": "show high"},
	"04 Chronicle of Atzoatl": {"baseexact": "Chronicle of Atzoatl", "class": "Misc Map Items", "type": "show high"},
	"04 Inscribed Ultimatum": {"baseexact": "Inscribed Ultimatum", "class": "Misc Map Items", "type": "show high"},
	"0 Fishing Rod": {"baseexact": "Fishing Rod", "type": "show very high"},
	"0 Quest": {"class": "Quest", "type": "quest"},
	"1 Voidstone": {"base": "Voidstone", "type": "quest"},

	"9 Starter weapon": {"other": ["Class Dagger Wand \"One Hand\" Bow Stave \"Two Hand\" Sceptre Claws", "ItemLevel < 2"], "type": "show normal quiet"},
}
