#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
from random import randint  # for random moos
from theme_config.min_w_highlight import volume


desc = "challenge item"


def gen_moo(val):
	if val == 'extremely':
		return 'CustomAlertSound "{}_challenge{}.wav"'.format(volume['max'], randint(11, 15))
	elif val == 'very':
		return 'CustomAlertSound "{}_challenge{}.wav"'.format(volume['high'], randint(11, 15))
	elif val == 'high':
		return 'CustomAlertSound "{}_challenge{}.wav"'.format(volume['normal'], randint(11, 15))
	elif val == 'normal':
		return 'CustomAlertSound "{}_challenge{}.wav"'.format(volume['medium'], randint(5, 10))
	else:
		return 'CustomAlertSound "{}_challenge{}.wav"'.format(volume['low'], randint(1, 4))
	
	
# Base type : settings pair
items = {
	"1 Cluster Jewel": {"base": "Cluster Jewel", "class": "Jewel", "type": "show high"},
#	"1 Simulacrum Splinter": {"base": "Simulacrum Splinter", "type": "show high"},

	"212 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("very"), "MapTier >= 16"], "type": "challenge very high"},
	"213 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("high"), "MapTier = 15"], "type": "challenge high"},
	"214 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("high"), "ItemLevel <= 83", "MapTier = 14"], "type": "challenge high"},
	"215 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("high"), "ItemLevel <= 82", "MapTier = 13"], "type": "challenge high"},
	"216 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("high"), "ItemLevel <= 81", "MapTier = 12"], "type": "challenge high"},
	"217 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("high"), "ItemLevel <= 80", "MapTier = 11"], "type": "challenge high"},
	"218 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("high"), "ItemLevel <= 79", "MapTier = 10"], "type": "challenge high"},
	"219 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("high"), "ItemLevel <= 78", "MapTier = 9"], "type": "challenge high"},
	"220 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("high"), "ItemLevel <= 77", "MapTier = 8"], "type": "challenge high"},
	"221 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("high"), "ItemLevel <= 76", "MapTier = 7"], "type": "challenge high"},
	"222 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("high"), "ItemLevel <= 75", "MapTier = 6"], "type": "challenge high"},
	"223 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("high"), "ItemLevel <= 74", "MapTier = 5"], "type": "challenge high"},
	"224 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("high"), "ItemLevel <= 73", "MapTier = 4"], "type": "challenge high"},
	"225 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("high"), "ItemLevel <= 72", "MapTier = 3"], "type": "challenge high"},
	"226 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("high"), "ItemLevel <= 71", "MapTier = 2"], "type": "challenge high"},
	"227 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("high"), "ItemLevel <= 70", "MapTier = 1"], "type": "challenge high"},

	"228 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("normal"), "MapTier >= 11"], "type": "challenge normal"},
	"229 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("normal"), "MapTier <= 5"], "type": "challenge normal"},
	"230 Normal": {"class": "Maps", "other": ["BlightedMap True", gen_moo("normal")], "type": "challenge normal"}
}