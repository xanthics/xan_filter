#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "maps"

# Base type : settings pair
items = {
	"0 Sacrifice at Dusk": {"base": "Sacrifice at Dusk", "class": "Map Fragments", "type": "ignore"},
	"0 Sacrifice at Midnight": {"base": "Sacrifice at Midnight", "class": "Map Fragments", "type": "map white good"},
	"0 Sacrifice at Dawn": {"base": "Sacrifice at Dawn", "class": "Map Fragments", "type": "ignore"},
	"0 Sacrifice at Noon": {"base": "Sacrifice at Noon", "class": "Map Fragments", "type": "ignore"},

	"0 Mortal Grief": {"base": "Mortal Grief", "class": "Map Fragments", "type": "map yellow"},
	"0 Mortal Rage": {"base": "Mortal Rage", "class": "Map Fragments", "type": "map yellow"},
	"0 Mortal Hope": {"base": "Mortal Hope", "class": "Map Fragments", "type": "map yellow good"},
	"0 Mortal Ignorance": {"base": "Mortal Ignorance", "class": "Map Fragments", "type": "map yellow"},

	"0 Eber's Key": {"base": "Eber's Key", "class": "Map Fragments", "type": "map yellow good"},
	"0 Yriel's Key": {"base": "Yriel's Key", "class": "Map Fragments", "type": "map yellow good"},
	"0 Inya's Key": {"base": "Inya's Key", "class": "Map Fragments", "type": "map yellow good"},
	"0 Volkuur's Key": {"base": "Volkuur's Key", "class": "Map Fragments", "type": "map yellow good"},

	"0 Fragment of the Phoenix": {"base": "Fragment of the Phoenix", "class": "Map Fragments", "type": "map red"},
	"0 Fragment of the Minotaur": {"base": "Fragment of the Minotaur", "class": "Map Fragments", "type": "map red"},
	"0 Fragment of the Chimera": {"base": "Fragment of the Chimera", "class": "Map Fragments", "type": "map red"},
	"0 Fragment of the Hydra": {"base": "Fragment of the Hydra", "class": "Map Fragments", "type": "map red"},
	"0 Divine Vessel": {"base": "Divine Vessel", "class": "Map Fragments", "type": "map red good"},

	"41 Maps >= 78 good": {"class": "Maps", "other": ["ShapedMap True", "ItemLevel <= 85", "DropLevel >= 73"], "type": "map red good"},
	"42 Maps <= 72 good": {"class": "Maps", "other": ["ShapedMap True", "ItemLevel <= 74"], "type": "map yellow good"},
	"51 Maps >= 78": {"class": "Maps", "other": ["ShapedMap True", "DropLevel >= 73"], "type": "map red"},
	"53 Other maps": {"class": "Maps", "other": ["ShapedMap True"], "type": "map yellow"},

	"61 Maps >= 78 good": {"class": "Maps", "other": ["ItemLevel <= 85", "DropLevel >= 78"], "type": "map red good"},
	"62 Maps <= 72 good": {"class": "Maps", "other": ["ItemLevel <= 74", "DropLevel <= 72"], "type": "map white good"},
	"63 Other maps good": {"class": "Maps", "other": ["ItemLevel <= 80", "DropLevel > 72", "DropLevel < 78"], "type": "map yellow good"},
	"71 Maps >= 78": {"class": "Maps", "other": ["DropLevel >= 78"], "type": "map red"},
	"72 Maps <= 72": {"class": "Maps", "other": ["DropLevel <= 72"], "type": "map white"},
	"73 Other maps": {"class": "Maps", "type": "map yellow"},
	"74 Map Fragments": {"class": "Map Fragments", "type": "map white"},
	"75 Misc map items": {"class": "Misc Map Items", 'other': ["PlayAlertSound 2 100"], "type": "show high"},
}
