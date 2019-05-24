#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "maps"

# Base type : settings pair
items = {
	# Maps that have hideouts to unlock :: suggest "challenge high" style to make them stand out
	"0 Dig Map": {"base": "Dig Map", "class": "Maps", "type": "ignore"},
	"0 Iceberg Map": {"base": "Iceberg Map", "class": "Maps", "type": "ignore"},
	"0 Sunken City Map": {"base": "Sunken City Map", "class": "Maps", "type": "ignore"},
	"0 Tower Map": {"base": "Tower Map", "class": "Maps", "type": "ignore"},
	"0 Terrace Map": {"base": "Terrace Map", "class": "Maps", "type": "ignore"},
	"0 Summit Map": {"base": "Summit Map", "class": "Maps", "type": "ignore"},
	"0 Haunted Mansion Map": {"base": "Haunted Mansion Map", "class": "Maps", "type": "ignore"},
	"0 Crimson Temple Map": {"base": "Crimson Temple Map", "class": "Maps", "type": "ignore"},

	"212 Normal": {"class": "Maps", "other": ["MapTier >= 16"], "type": "map very good"},
	"213 Normal": {"class": "Maps", "other": ["MapTier = 15"], "type": "map red good"},
	"214 Normal": {"class": "Maps", "other": ["ItemLevel <= 83", "MapTier = 14"], "type": "map red good"},
	"215 Normal": {"class": "Maps", "other": ["ItemLevel <= 82", "MapTier = 13"], "type": "map red good"},
	"216 Normal": {"class": "Maps", "other": ["ItemLevel <= 81", "MapTier = 12"], "type": "map red good"},
	"217 Normal": {"class": "Maps", "other": ["ItemLevel <= 80", "MapTier = 11"], "type": "map red good"},
	"218 Normal": {"class": "Maps", "other": ["ItemLevel <= 79", "MapTier = 10"], "type": "map yellow good"},
	"219 Normal": {"class": "Maps", "other": ["ItemLevel <= 78", "MapTier = 9"], "type": "map yellow good"},
	"220 Normal": {"class": "Maps", "other": ["ItemLevel <= 77", "MapTier = 8"], "type": "map yellow good"},
	"221 Normal": {"class": "Maps", "other": ["ItemLevel <= 76", "MapTier = 7"], "type": "map yellow good"},
	"222 Normal": {"class": "Maps", "other": ["ItemLevel <= 75", "MapTier = 6"], "type": "map yellow good"},
	"223 Normal": {"class": "Maps", "other": ["ItemLevel <= 74", "MapTier = 5"], "type": "map white good"},
	"224 Normal": {"class": "Maps", "other": ["ItemLevel <= 73", "MapTier = 4"], "type": "map white good"},
	"225 Normal": {"class": "Maps", "other": ["ItemLevel <= 72", "MapTier = 3"], "type": "map white good"},
	"226 Normal": {"class": "Maps", "other": ["ItemLevel <= 71", "MapTier = 2"], "type": "map white good"},
	"227 Normal": {"class": "Maps", "other": ["ItemLevel <= 70", "MapTier = 1"], "type": "map white good"},

	"228 Normal": {"class": "Maps", "other": ["MapTier >= 11"], "type": "map red"},
	"229 Normal": {"class": "Maps", "other": ["MapTier <= 5"], "type": "map white"},
	"230 Normal": {"class": "Maps", "type": "map yellow"},

	"75 Misc map items": {"class": "Misc Map Items", 'other': ['CustomAlertSound "100_show.wav"'], "type": "show high"},
}
