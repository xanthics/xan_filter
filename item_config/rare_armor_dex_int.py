#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Rare item for leveling or crafting"

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Padded Vest": {"base": "Padded Vest", "other": ["ItemLevel <= 9"], "type": "levelling rare normal"},
	"Oiled Vest": {"base": "Oiled Vest", "other": ["ItemLevel <= 14"], "type": "levelling rare normal"},
	"Padded Jacket": {"base": "Padded Jacket", "other": ["ItemLevel <= 23"], "type": "levelling rare normal"},
	"Oiled Coat": {"base": "Oiled Coat", "other": ["ItemLevel <= 27"], "type": "levelling rare normal"},
	"Scarlet Raiment": {"base": "Scarlet Raiment", "other": ["ItemLevel <= 33"], "type": "levelling rare normal"},
	"Waxed Garb": {"base": "Waxed Garb", "other": ["ItemLevel <= 37"], "type": "levelling rare normal"},
	"Bone Armour": {"base": "Bone Armour", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Quilted Jacket": {"base": "Quilted Jacket", "other": ["ItemLevel <= 45"], "type": "levelling rare normal"},
	"Sleek Coat": {"base": "Sleek Coat", "other": ["ItemLevel <= 49"], "type": "levelling rare normal"},
	"Crimson Raiment": {"base": "Crimson Raiment", "other": ["ItemLevel <= 53"], "type": "levelling rare normal"},
	"Lacquered Garb": {"base": "Lacquered Garb", "other": ["ItemLevel <= 57"], "type": "levelling rare normal"},
	"Crypt Armour": {"base": "Crypt Armour", "other": ["ItemLevel <= 61"], "type": "levelling rare normal"},
	"Sentinel Jacket": {"base": "Sentinel Jacket", "other": ["ItemLevel <= 64"], "type": "levelling rare normal"},
	"Varnished Coat": {"base": "Varnished Coat", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Blood Raiment": {"base": "Blood Raiment", "other": ["ItemLevel <= 70"], "type": "ignore"},
	"Sadist Garb": {"base": "Sadist Garb", "other": ["ItemLevel <= 73"], "type": "ignore"},
	"Carnal Armour": {"base": "Carnal Armour", "other": ["ItemLevel <= 76"], "type": "ignore"},
	"Wrapped Boots": {"base": "Wrapped Boots", "other": ["ItemLevel <= 11"], "type": "levelling rare normal"},
	"Strapped Boots": {"base": "Strapped Boots", "other": ["ItemLevel <= 21"], "type": "levelling rare normal"},
	"Clasped Boots": {"base": "Clasped Boots", "other": ["ItemLevel <= 32"], "type": "levelling rare normal"},
	"Shackled Boots": {"base": "Shackled Boots", "other": ["ItemLevel <= 39"], "type": "levelling rare normal"},
	"Trapper Boots": {"base": "Trapper Boots", "other": ["ItemLevel <= 46"], "type": "levelling rare normal"},
	"Ambush Boots": {"base": "Ambush Boots", "other": ["ItemLevel <= 52"], "type": "levelling rare normal"},
	"Carnal Boots": {"base": "Carnal Boots", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Assassin's Boots": {"base": "Assassin's Boots", "other": ["ItemLevel <= 68"], "type": "ignore"},
	"Murder Boots": {"base": "Murder Boots", "other": ["ItemLevel <= 74"], "type": "ignore"},
	"Wrapped Mitts": {"base": "Wrapped Mitts", "other": ["ItemLevel <= 10"], "type": "levelling rare normal"},
	"Strapped Mitts": {"base": "Strapped Mitts", "other": ["ItemLevel <= 21"], "type": "levelling rare normal"},
	"Clasped Mitts": {"base": "Clasped Mitts", "other": ["ItemLevel <= 36"], "type": "levelling rare normal"},
	"Trapper Mitts": {"base": "Trapper Mitts", "other": ["ItemLevel <= 41"], "type": "levelling rare normal"},
	"Ambush Mitts": {"base": "Ambush Mitts", "other": ["ItemLevel <= 50"], "type": "levelling rare normal"},
	"Carnal Mitts": {"base": "Carnal Mitts", "other": ["ItemLevel <= 55"], "type": "levelling rare normal"},
	"Assassin's Mitts": {"base": "Assassin's Mitts", "other": ["ItemLevel <= 63"], "type": "levelling rare normal"},
	"Murder Mitts": {"base": "Murder Mitts", "other": ["ItemLevel <= 72"], "type": "ignore"},
	"Scare Mask": {"base": "Scare Mask", "other": ["ItemLevel <= 9"], "type": "levelling rare normal"},
	"Plague Mask": {"base": "Plague Mask", "other": ["ItemLevel <= 15"], "type": "levelling rare normal"},
	"Iron Mask": {"base": "Iron Mask", "other": ["ItemLevel <= 22"], "type": "levelling rare normal"},
	"Festival Mask": {"base": "Festival Mask", "other": ["ItemLevel <= 33"], "type": "levelling rare normal"},
	"Golden Mask": {"base": "Golden Mask", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Raven Mask": {"base": "Raven Mask", "other": ["ItemLevel <= 43"], "type": "levelling rare normal"},
	"Callous Mask": {"base": "Callous Mask", "other": ["ItemLevel <= 50"], "type": "levelling rare normal"},
	"Regicide Mask": {"base": "Regicide Mask", "other": ["ItemLevel <= 57"], "type": "levelling rare normal"},
	"Harlequin Mask": {"base": "Harlequin Mask", "other": ["ItemLevel <= 62"], "type": "levelling rare normal"},
	"Vaal Mask": {"base": "Vaal Mask", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Deicide Mask": {"base": "Deicide Mask", "other": ["ItemLevel <= 72"], "type": "ignore"},
	"Spiked Bundle": {"base": "Spiked Bundle", "other": ["ItemLevel <= 10"], "type": "levelling rare normal"},
	"Driftwood Spiked Shield": {"base": "Driftwood Spiked Shield", "other": ["ItemLevel <= 17"], "type": "levelling rare normal"},
	"Alloyed Spiked Shield": {"base": "Alloyed Spiked Shield", "other": ["ItemLevel <= 25"], "type": "levelling rare normal"},
	"Burnished Spiked Shield": {"base": "Burnished Spiked Shield", "other": ["ItemLevel <= 32"], "type": "levelling rare normal"},
	"Ornate Spiked Shield": {"base": "Ornate Spiked Shield", "other": ["ItemLevel <= 38"], "type": "levelling rare normal"},
	"Redwood Spiked Shield": {"base": "Redwood Spiked Shield", "other": ["ItemLevel <= 44"], "type": "levelling rare normal"},
	"Compound Spiked Shield": {"base": "Compound Spiked Shield", "other": ["ItemLevel <= 50"], "type": "levelling rare normal"},
	"Polished Spiked Shield": {"base": "Polished Spiked Shield", "other": ["ItemLevel <= 54"], "type": "levelling rare normal"},
	"Sovereign Spiked Shield": {"base": "Sovereign Spiked Shield", "other": ["ItemLevel <= 59"], "type": "levelling rare normal"},
	"Alder Spiked Shield": {"base": "Alder Spiked Shield", "other": ["ItemLevel <= 63"], "type": "levelling rare normal"},
	"Ezomyte Spiked Shield": {"base": "Ezomyte Spiked Shield", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Mirrored Spiked Shield": {"base": "Mirrored Spiked Shield", "other": ["ItemLevel <= 71"], "type": "levelling rare normal"},
	"Supreme Spiked Shield": {"base": "Supreme Spiked Shield", "other": ["ItemLevel <= 75"], "type": "levelling rare normal"}
}
