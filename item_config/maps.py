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
	"0 Divine Vessel": {"base": "Divine Vessel", "class": "Map Fragments", "type": "map red"},

	"000 Shaped": {"class": "Maps", "other": ["ShapedMap True", "ItemLevel <= 85", "DropLevel = 77"], "type": "map red good"},
	"001 Shaped": {"class": "Maps", "other": ["ShapedMap True", "ItemLevel <= 84", "DropLevel = 76"], "type": "map red good"},
	"002 Shaped": {"class": "Maps", "other": ["ShapedMap True", "ItemLevel <= 83", "DropLevel = 75"], "type": "map red good"},
	"003 Shaped": {"class": "Maps", "other": ["ShapedMap True", "ItemLevel <= 82", "DropLevel = 74"], "type": "map red good"},
	"004 Shaped": {"class": "Maps", "other": ["ShapedMap True", "ItemLevel <= 81", "DropLevel = 73"], "type": "map red good"},
	"005 Shaped": {"class": "Maps", "other": ["ShapedMap True", "ItemLevel <= 80", "DropLevel = 72"], "type": "map yellow good"},
	"006 Shaped": {"class": "Maps", "other": ["ShapedMap True", "ItemLevel <= 79", "DropLevel = 71"], "type": "map yellow good"},
	"007 Shaped": {"class": "Maps", "other": ["ShapedMap True", "ItemLevel <= 78", "DropLevel = 70"], "type": "map yellow good"},
	"008 Shaped": {"class": "Maps", "other": ["ShapedMap True", "ItemLevel <= 77", "DropLevel = 69"], "type": "map yellow good"},
	"009 Shaped": {"class": "Maps", "other": ["ShapedMap True", "ItemLevel <= 76", "DropLevel < 69"], "type": "map yellow good"},

	"010 Shaped": {"class": "Maps", "other": ["ShapedMap True", "DropLevel >= 73"], "type": "map red"},
	"011 Shaped": {"class": "Maps", "other": ["ShapedMap True"], "type": "map yellow"},

	"012 Normal": {"class": "Maps", "other": ["ItemLevel <= 85", "DropLevel = 83"], "type": "map red good"},
	"013 Normal": {"class": "Maps", "other": ["ItemLevel <= 84", "DropLevel = 82"], "type": "map red good"},
	"014 Normal": {"class": "Maps", "other": ["ItemLevel <= 83", "DropLevel = 81"], "type": "map red good"},
	"015 Normal": {"class": "Maps", "other": ["ItemLevel <= 82", "DropLevel = 80"], "type": "map red good"},
	"016 Normal": {"class": "Maps", "other": ["ItemLevel <= 81", "DropLevel = 79"], "type": "map red good"},
	"017 Normal": {"class": "Maps", "other": ["ItemLevel <= 80", "DropLevel = 78"], "type": "map red good"},
	"018 Normal": {"class": "Maps", "other": ["ItemLevel <= 79", "DropLevel = 77"], "type": "map yellow good"},
	"019 Normal": {"class": "Maps", "other": ["ItemLevel <= 78", "DropLevel = 76"], "type": "map yellow good"},
	"020 Normal": {"class": "Maps", "other": ["ItemLevel <= 77", "DropLevel = 75"], "type": "map yellow good"},
	"021 Normal": {"class": "Maps", "other": ["ItemLevel <= 76", "DropLevel = 74"], "type": "map yellow good"},
	"022 Normal": {"class": "Maps", "other": ["ItemLevel <= 75", "DropLevel = 73"], "type": "map yellow good"},
	"023 Normal": {"class": "Maps", "other": ["ItemLevel <= 74", "DropLevel = 72"], "type": "map white good"},
	"024 Normal": {"class": "Maps", "other": ["ItemLevel <= 73", "DropLevel = 71"], "type": "map white good"},
	"025 Normal": {"class": "Maps", "other": ["ItemLevel <= 72", "DropLevel = 70"], "type": "map white good"},
	"026 Normal": {"class": "Maps", "other": ["ItemLevel <= 71", "DropLevel = 69"], "type": "map white good"},
	"027 Normal": {"class": "Maps", "other": ["ItemLevel <= 70", "DropLevel < 69"], "type": "map white good"},

	"028 Normal": {"class": "Maps", "other": ["DropLevel >= 78"], "type": "map red"},
	"029 Normal": {"class": "Maps", "other": ["DropLevel <= 72"], "type": "map white"},
	"030 Normal": {"class": "Maps", "type": "map yellow"},

	"74 Map Fragments": {"class": "Map Fragments", "type": "map white"},
	"75 Misc map items": {"class": "Misc Map Items", 'other': ["PlayAlertSound 2 100"], "type": "show high"},
}
