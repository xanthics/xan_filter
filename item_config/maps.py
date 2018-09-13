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
	
	"0 Divine Vessel": {"other": ["PlayAlertSoundPositional 9 50"], "base": "Divine Vessel", "class": "Map Fragments", "type": "show high"},

	"112 Normal": {"class": "Maps", "other": ["MapTier >= 16"], "type": "map very good"},
	"113 Normal": {"class": "Maps", "other": ["ItemLevel <= 84", "MapTier = 15"], "type": "map red good"},
	"114 Normal": {"class": "Maps", "other": ["ItemLevel <= 83", "MapTier = 14"], "type": "map red good"},
	"115 Normal": {"class": "Maps", "other": ["ItemLevel <= 82", "MapTier = 13"], "type": "map red good"},
	"116 Normal": {"class": "Maps", "other": ["ItemLevel <= 81", "MapTier = 12"], "type": "map red good"},
	"117 Normal": {"class": "Maps", "other": ["ItemLevel <= 80", "MapTier = 11"], "type": "map red good"},
	"118 Normal": {"class": "Maps", "other": ["ItemLevel <= 79", "MapTier = 10"], "type": "map yellow good"},
	"119 Normal": {"class": "Maps", "other": ["ItemLevel <= 78", "MapTier = 9"], "type": "map yellow good"},
	"120 Normal": {"class": "Maps", "other": ["ItemLevel <= 77", "MapTier = 8"], "type": "map yellow good"},
	"121 Normal": {"class": "Maps", "other": ["ItemLevel <= 76", "MapTier = 7"], "type": "map yellow good"},
	"122 Normal": {"class": "Maps", "other": ["ItemLevel <= 75", "MapTier = 6"], "type": "map yellow good"},
	"123 Normal": {"class": "Maps", "other": ["ItemLevel <= 74", "MapTier = 5"], "type": "map white good"},
	"124 Normal": {"class": "Maps", "other": ["ItemLevel <= 73", "MapTier = 4"], "type": "map white good"},
	"125 Normal": {"class": "Maps", "other": ["ItemLevel <= 72", "MapTier = 3"], "type": "map white good"},
	"126 Normal": {"class": "Maps", "other": ["ItemLevel <= 71", "MapTier = 2"], "type": "map white good"},
	"127 Normal": {"class": "Maps", "other": ["ItemLevel <= 70", "MapTier = 1"], "type": "map white good"},

	"128 Normal": {"class": "Maps", "other": ["MapTier >= 11"], "type": "map red"},
	"129 Normal": {"class": "Maps", "other": ["MapTier <= 5"], "type": "map white"},
	"130 Normal": {"class": "Maps", "type": "map yellow"},

	"74 Map Fragments": {"class": "Map Fragments", "type": "map white"},
	"75 Misc map items": {"class": "Misc Map Items", 'other': ['CustomAlertSound "100_show.wav"'], "type": "show high"},
}
