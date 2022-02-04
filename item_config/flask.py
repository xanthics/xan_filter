#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Flasks"

# Base type : settings pair
items = {
	"01 Qual Flask": {"base": "Flask", "other": ["Quality = 20", "Rarity Normal"], "type": "show normal quiet"},
	"02 Qual Flask": {"base": "Flask", "other": ["Quality >= 10"], "type": "ignore"},
	"03 Qual Flask": {"base": "Flask", "other": ["Quality >= 1", "AreaLevel <= 78"], "type": "ignore"},
	"04 Quicksilver Flask <= 25": {"base": "Quicksilver Flask", "other": ["AreaLevel <= 25"], "type": "normal"},

	"1 Small Flasks": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 0", "AreaLevel <= 3"], "type": "normal"},
	"1 Medium Flasks": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 3", "AreaLevel <= 6"], "type": "normal"},
	"1 Large Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 6", "AreaLevel <= 12"], "type": "normal"},
	"1 Greater Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 12", "AreaLevel <= 18"], "type": "normal"},
	"1 Grand Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 18", "AreaLevel <= 24"], "type": "normal"},
	"1 Giant Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 24", "AreaLevel <= 30"], "type": "normal"},
	"1 Colossal Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 30", "AreaLevel <= 36"], "type": "normal"},
	"1 Sacred Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 36", "AreaLevel <= 42"], "type": "normal"},
	"1 Hallowed Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 42", "AreaLevel <= 60"], "type": "normal"},
	"1 Sanctified Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 50", "AreaLevel <= 60"], "type": "normal"},
	"1 Divine Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 60", "AreaLevel <= 65"], "type": "normal"},
	"1 Eternal Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 65", "AreaLevel <= 68"], "type": "normal"},

	"2 Divine Flask": {"class": "Life Flasks", "other": ["DropLevel = 60", "ItemLevel >= 83"], "type": "normal border"},
	"2 Eternal Flask": {"class": "Mana Flasks", "other": ["DropLevel = 65", "ItemLevel >= 83"], "type": "normal border"},

	"2 Small Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 10", "AreaLevel <= 20"], "type": "ignore"},
	"2 medium Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 20", "AreaLevel <= 30"], "type": "ignore"},
	"2 large Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 30", "AreaLevel <= 40"], "type": "ignore"},
	"2 Colossal Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 40", "AreaLevel <= 50"], "type": "ignore"},
	"2 Sacred Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 50", "AreaLevel <= 60"], "type": "ignore"},
	"2 Hallowed Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 60", "AreaLevel <= 70"], "type": "ignore"},

	"9 Other Flasks": {"base": "Flask", "type": "ignore"}
}

util_flasks = [
	"Diamond Flask",
	"Granite Flask",
	"Basalt Flask",
	"Jade Flask",
	"Stibnite Flask",
	"Topaz Flask",
	"Sapphire Flask",
	"Ruby Flask",
	"Amethyst Flask",
	"Quicksilver Flask",
	"Silver Flask",
	"Quartz Flask",
	"Gold Flask",
	"Corundum Flask",
	"Aquamarine Flask",
	"Sulphur Flask",
	"Bismuth Flask",
	"Iron Flask"
]

# 	"1 Quartz Flask": {"base": "Quartz Flask", "other": ["Rarity Normal", "AreaLevel <= 78"], "type": "normal"},
for flask in util_flasks:
	for c, lvl in enumerate([
		(85, 'show normal quiet'),
		(76, 'normal border'),
		(0, 'normal')
	], start=1):
		items[f"{c} {flask}"] = {"base": flask, "other": [f"ItemLevel >= {lvl[0]}"], "type": lvl[1]}
