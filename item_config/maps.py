#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "maps"

# Base type : settings pair
items = {
	# Maps that have hideouts to unlock :: suggest "map highlight" style to make them stand out
	"0 Dig Map": {"base": "Dig Map", "class": "Maps", "type": "ignore"},
	"0 Iceberg Map": {"base": "Iceberg Map", "class": "Maps", "type": "ignore"},
	"0 Sunken City Map": {"base": "Sunken City Map", "class": "Maps", "type": "ignore"},
	"0 Tower Map": {"base": "Tower Map", "class": "Maps", "type": "ignore"},
	"0 Terrace Map": {"base": "Terrace Map", "class": "Maps", "type": "ignore"},
	"0 Summit Map": {"base": "Summit Map", "class": "Maps", "type": "ignore"},
	"0 Haunted Mansion Map": {"base": "Haunted Mansion Map", "class": "Maps", "type": "ignore"},
	"0 Crimson Temple Map": {"base": "Crimson Temple Map", "class": "Maps", "type": "ignore"},

	# If you are shaped for a specific map drop, put it here so you don't miss it
#	"0 Burial Chambers Map": {"base": "Burial Chambers Map", "class": "Maps", "type": "map highlight"},
#	"0 Glacier Map": {"base": "Glacier Map", "class": "Maps", "type": "map highlight"},

	"001 Delirium Map": {"class": "Maps", "other": ["AnyEnchantment True", "MapTier >= 16"], "type": "challenge very high"},
	"002 Delirium Map": {"class": "Maps", "other": ["AnyEnchantment True", "MapTier >= 11"], "type": "challenge high"},
	"003 Delirium Map": {"class": "Maps", "other": ["AnyEnchantment True", "MapTier <= 5"], "type": "challenge normal"},
	"004 Delirium Map": {"class": "Maps", "other": ["AnyEnchantment True"], "type": "challenge normal"},

	"011 Blighted": {"class": "Maps", "other": ["BlightedMap True", "MapTier >= 16"], "type": "challenge very high"},
	"012 Blighted": {"class": "Maps", "other": ["BlightedMap True", "MapTier >= 11"], "type": "challenge high"},
	"013 Blighted": {"class": "Maps", "other": ["BlightedMap True", "MapTier <= 5"], "type": "challenge normal"},
	"014 Blighted": {"class": "Maps", "other": ["BlightedMap True"], "type": "challenge normal"},

	"112 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "MapTier >= 16"], "type": "influenced map very good"},
	"113 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "MapTier = 15"], "type": "influenced map red good"},
	"114 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "AreaLevel <= 83", "MapTier = 14"], "type": "influenced map red good"},
	"115 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "AreaLevel <= 82", "MapTier = 13"], "type": "influenced map red good"},
	"116 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "AreaLevel <= 81", "MapTier = 12"], "type": "influenced map red good"},
	"117 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "AreaLevel <= 80", "MapTier = 11"], "type": "influenced map red good"},
	"118 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "AreaLevel <= 79", "MapTier = 10"], "type": "influenced map yellow good"},
	"119 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "AreaLevel <= 78", "MapTier = 9"], "type": "influenced map yellow good"},
	"120 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "AreaLevel <= 77", "MapTier = 8"], "type": "influenced map yellow good"},
	"121 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "AreaLevel <= 76", "MapTier = 7"], "type": "influenced map yellow good"},
	"122 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "AreaLevel <= 75", "MapTier = 6"], "type": "influenced map yellow good"},
	"123 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "AreaLevel <= 74", "MapTier = 5"], "type": "influenced map white good"},
	"124 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "AreaLevel <= 73", "MapTier = 4"], "type": "influenced map white good"},
	"125 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "AreaLevel <= 72", "MapTier = 3"], "type": "influenced map white good"},
	"126 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "AreaLevel <= 71", "MapTier = 2"], "type": "influenced map white good"},
	"127 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "AreaLevel <= 70", "MapTier = 1"], "type": "influenced map white good"},

	"128 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "MapTier >= 11"], "type": "influenced map red"},
	"129 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper", "MapTier <= 5"], "type": "influenced map white"},
	"130 Influenced": {"class": "Maps", "other": ["HasInfluence Elder Shaper"], "type": "influenced map yellow"},

	"212 Normal": {"class": "Maps", "other": ["MapTier >= 16"], "type": "map very good"},
	"213 Normal": {"class": "Maps", "other": ["MapTier = 15"], "type": "map red good"},
	"214 Normal": {"class": "Maps", "other": ["AreaLevel <= 83", "MapTier = 14"], "type": "map red good"},
	"215 Normal": {"class": "Maps", "other": ["AreaLevel <= 82", "MapTier = 13"], "type": "map red good"},
	"216 Normal": {"class": "Maps", "other": ["AreaLevel <= 81", "MapTier = 12"], "type": "map red good"},
	"217 Normal": {"class": "Maps", "other": ["AreaLevel <= 80", "MapTier = 11"], "type": "map red good"},
	"218 Normal": {"class": "Maps", "other": ["AreaLevel <= 79", "MapTier = 10"], "type": "map yellow good"},
	"219 Normal": {"class": "Maps", "other": ["AreaLevel <= 78", "MapTier = 9"], "type": "map yellow good"},
	"220 Normal": {"class": "Maps", "other": ["AreaLevel <= 77", "MapTier = 8"], "type": "map yellow good"},
	"221 Normal": {"class": "Maps", "other": ["AreaLevel <= 76", "MapTier = 7"], "type": "map yellow good"},
	"222 Normal": {"class": "Maps", "other": ["AreaLevel <= 75", "MapTier = 6"], "type": "map yellow good"},
	"223 Normal": {"class": "Maps", "other": ["AreaLevel <= 74", "MapTier = 5"], "type": "map white good"},
	"224 Normal": {"class": "Maps", "other": ["AreaLevel <= 73", "MapTier = 4"], "type": "map white good"},
	"225 Normal": {"class": "Maps", "other": ["AreaLevel <= 72", "MapTier = 3"], "type": "map white good"},
	"226 Normal": {"class": "Maps", "other": ["AreaLevel <= 71", "MapTier = 2"], "type": "map white good"},
	"227 Normal": {"class": "Maps", "other": ["AreaLevel <= 70", "MapTier = 1"], "type": "map white good"},

	"228 Normal": {"class": "Maps", "other": ["MapTier >= 11"], "type": "map red"},
	"229 Normal": {"class": "Maps", "other": ["MapTier <= 5"], "type": "map white"},
	"230 Normal": {"class": "Maps", "type": "map yellow"},
}
