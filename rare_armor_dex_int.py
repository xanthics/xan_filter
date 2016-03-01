"""
* Copyright (c) 2015 Jeremy Parks. All rights reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a
* copy of this software and associated documentation files (the "Software"),
* to deal in the Software without restriction, including without limitation
* the rights to use, copy, modify, merge, publish, distribute, sublicense,
* and/or sell copies of the Software, and to permit persons to whom the
* Software is furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
* DEALINGS IN THE SOFTWARE.

Author: Jeremy Parks
Purpose: Create an item filter based on config files
Note: Requires Python 3.4.x
"""

desc = "Nonrare item for leveling or crafting"

# Text settings for various categories
# This is where you would define general settings for a category, such as PlayAlertSound.
# Each config should be its own array element.  Parsing will handle tabs/etc.
# ignore and hide have special meaning(see comment) everything else is local to file
settings = {
	"very high": ["SetFontSize 28",
				  "SetBackgroundColor 0 0 0 100",
				  "SetBorderColor 255 40 0"],
	"high": ["Rarity Rare",
             "SetBorderColor 255 255 119",
             "SetFontSize 34"],
	"normal": ["Rarity Rare",
             "SetBorderColor 255 255 119"],
	"low": [""],
	"ignore": [""],  # will have no styling applied and will use the default set at the end
	"hide": [""]  # Will be explicitly hidden with applied styling
}

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Padded Vest": {"base": "Padded Vest", "other": ["ItemLevel <= 9"], "type": "normal"},
	"Oiled Vest": {"base": "Oiled Vest", "other": ["ItemLevel <= 14"], "type": "normal"},
	"Padded Jacket": {"base": "Padded Jacket", "other": ["ItemLevel <= 23"], "type": "normal"},
	"Oiled Coat": {"base": "Oiled Coat", "other": ["ItemLevel <= 27"], "type": "normal"},
	"Scarlet Raiment": {"base": "Scarlet Raiment", "other": ["ItemLevel <= 33"], "type": "normal"},
	"Waxed Garb": {"base": "Waxed Garb", "other": ["ItemLevel <= 37"], "type": "normal"},
	"Bone Armour": {"base": "Bone Armour", "other": ["ItemLevel <= 40"], "type": "normal"},
	"Quilted Jacket": {"base": "Quilted Jacket", "other": ["ItemLevel <= 45"], "type": "normal"},
	"Sleek Coat": {"base": "Sleek Coat", "other": ["ItemLevel <= 49"], "type": "normal"},
	"Crimson Raiment": {"base": "Crimson Raiment", "other": ["ItemLevel <= 53"], "type": "normal"},
	"Lacquered Garb": {"base": "Lacquered Garb", "other": ["ItemLevel <= 57"], "type": "normal"},
	"Crypt Armour": {"base": "Crypt Armour", "other": ["ItemLevel <= 61"], "type": "normal"},
	"Sentinel Jacket": {"base": "Sentinel Jacket", "other": ["ItemLevel <= 64"], "type": "normal"},
	"Varnished Coat": {"base": "Varnished Coat", "other": ["ItemLevel <= 67"], "type": "normal"},
	"Blood Raiment": {"base": "Blood Raiment", "other": ["ItemLevel <= 70"], "type": "normal"},
	"Sadist Garb": {"base": "Sadist Garb", "other": ["ItemLevel <= 73"], "type": "normal"},
	"Carnal Armour": {"base": "Carnal Armour", "other": ["ItemLevel <= 76"], "type": "normal"},
	"Wrapped Boots": {"base": "Wrapped Boots", "other": ["ItemLevel <= 11"], "type": "normal"},
	"Strapped Boots": {"base": "Strapped Boots", "other": ["ItemLevel <= 21"], "type": "normal"},
	"Clasped Boots": {"base": "Clasped Boots", "other": ["ItemLevel <= 32"], "type": "normal"},
	"Shackled Boots": {"base": "Shackled Boots", "other": ["ItemLevel <= 39"], "type": "normal"},
	"Trapper Boots": {"base": "Trapper Boots", "other": ["ItemLevel <= 46"], "type": "normal"},
	"Ambush Boots": {"base": "Ambush Boots", "other": ["ItemLevel <= 52"], "type": "normal"},
	"Carnal Boots": {"base": "Carnal Boots", "other": ["ItemLevel <= 60"], "type": "normal"},
	"Assassin's Boots": {"base": "Assassin's Boots", "other": ["ItemLevel <= 68"], "type": "normal"},
	"Murder Boots": {"base": "Murder Boots", "other": ["ItemLevel <= 74"], "type": "normal"},
	"Wrapped Mitts": {"base": "Wrapped Mitts", "other": ["ItemLevel <= 10"], "type": "normal"},
	"Strapped Mitts": {"base": "Strapped Mitts", "other": ["ItemLevel <= 21"], "type": "normal"},
	"Clasped Mitts": {"base": "Clasped Mitts", "other": ["ItemLevel <= 36"], "type": "normal"},
	"Trapper Mitts": {"base": "Trapper Mitts", "other": ["ItemLevel <= 41"], "type": "normal"},
	"Ambush Mitts": {"base": "Ambush Mitts", "other": ["ItemLevel <= 50"], "type": "normal"},
	"Carnal Mitts": {"base": "Carnal Mitts", "other": ["ItemLevel <= 55"], "type": "normal"},
	"Assassin's Mitts": {"base": "Assassin's Mitts", "other": ["ItemLevel <= 63"], "type": "normal"},
	"Murder Mitts": {"base": "Murder Mitts", "other": ["ItemLevel <= 72"], "type": "normal"},
	"Scare Mask": {"base": "Scare Mask", "other": ["ItemLevel <= 9"], "type": "normal"},
	"Plague Mask": {"base": "Plague Mask", "other": ["ItemLevel <= 15"], "type": "normal"},
	"Iron Mask": {"base": "Iron Mask", "other": ["ItemLevel <= 22"], "type": "normal"},
	"Festival Mask": {"base": "Festival Mask", "other": ["ItemLevel <= 33"], "type": "normal"},
	"Golden Mask": {"base": "Golden Mask", "other": ["ItemLevel <= 40"], "type": "normal"},
	"Raven Mask": {"base": "Raven Mask", "other": ["ItemLevel <= 43"], "type": "normal"},
	"Callous Mask": {"base": "Callous Mask", "other": ["ItemLevel <= 50"], "type": "normal"},
	"Regicide Mask": {"base": "Regicide Mask", "other": ["ItemLevel <= 57"], "type": "normal"},
	"Harlequin Mask": {"base": "Harlequin Mask", "other": ["ItemLevel <= 62"], "type": "normal"},
	"Vaal Mask": {"base": "Vaal Mask", "other": ["ItemLevel <= 67"], "type": "normal"},
	"Deicide Mask": {"base": "Deicide Mask", "other": ["ItemLevel <= 72"], "type": "normal"},
	"Spiked Bundle": {"base": "Spiked Bundle", "other": ["ItemLevel <= 10"], "type": "normal"},
	"Driftwood Spiked Shield": {"base": "Driftwood Spiked Shield", "other": ["ItemLevel <= 17"], "type": "normal"},
	"Alloyed Spiked Shield": {"base": "Alloyed Spiked Shield", "other": ["ItemLevel <= 25"], "type": "normal"},
	"Burnished Spiked Shield": {"base": "Burnished Spiked Shield", "other": ["ItemLevel <= 32"], "type": "normal"},
	"Ornate Spiked Shield": {"base": "Ornate Spiked Shield", "other": ["ItemLevel <= 38"], "type": "normal"},
	"Redwood Spiked Shield": {"base": "Redwood Spiked Shield", "other": ["ItemLevel <= 44"], "type": "normal"},
	"Compound Spiked Shield": {"base": "Compound Spiked Shield", "other": ["ItemLevel <= 50"], "type": "normal"},
	"Polished Spiked Shield": {"base": "Polished Spiked Shield", "other": ["ItemLevel <= 54"], "type": "normal"},
	"Sovereign Spiked Shield": {"base": "Sovereign Spiked Shield", "other": ["ItemLevel <= 59"], "type": "normal"},
	"Alder Spiked Shield": {"base": "Alder Spiked Shield", "other": ["ItemLevel <= 63"], "type": "normal"},
	"Ezomyte Spiked Shield": {"base": "Ezomyte Spiked Shield", "other": ["ItemLevel <= 67"], "type": "normal"},
	"Mirrored Spiked Shield": {"base": "Mirrored Spiked Shield", "other": ["ItemLevel <= 71"], "type": "normal"},
	"Supreme Spiked Shield": {"base": "Supreme Spiked Shield", "other": ["ItemLevel <= 75"], "type": "normal"}
}
