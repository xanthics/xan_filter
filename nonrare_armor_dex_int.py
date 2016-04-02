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

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Padded Vest": {"base": "Padded Vest", "other": ["Rarity <= Magic", "ItemLevel <= 9"], "type": "leveling low"},
	"Oiled Vest": {"base": "Oiled Vest", "other": ["Rarity <= Magic", "ItemLevel <= 14"], "type": "leveling low"},
	"Padded Jacket": {"base": "Padded Jacket", "other": ["Rarity <= Magic", "ItemLevel <= 23"], "type": "leveling low"},
	"Oiled Coat": {"base": "Oiled Coat", "other": ["Rarity <= Magic", "ItemLevel <= 27"], "type": "leveling low"},
	"Scarlet Raiment": {"base": "Scarlet Raiment", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "leveling low"},
	"Waxed Garb": {"base": "Waxed Garb", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "leveling low"},
	"Bone Armour": {"base": "Bone Armour", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Quilted Jacket": {"base": "Quilted Jacket", "other": ["Rarity <= Magic", "ItemLevel <= 45"], "type": "leveling low"},
	"Sleek Coat": {"base": "Sleek Coat", "other": ["Rarity <= Magic", "ItemLevel <= 49"], "type": "leveling low"},
	"Crimson Raiment": {"base": "Crimson Raiment", "other": ["Rarity <= Magic", "ItemLevel <= 53"], "type": "ignore"},
	"Lacquered Garb": {"base": "Lacquered Garb", "other": ["Rarity <= Magic", "ItemLevel <= 57"], "type": "ignore"},
	"Crypt Armour": {"base": "Crypt Armour", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "ignore"},
	"Sentinel Jacket": {"base": "Sentinel Jacket", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "ignore"},
	"Varnished Coat": {"base": "Varnished Coat", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Blood Raiment": {"base": "Blood Raiment", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "ignore"},
	"Sadist Garb": {"base": "Sadist Garb", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"},
	"Carnal Armour": {"base": "Carnal Armour", "other": ["Rarity <= Magic", "ItemLevel <= 76"], "type": "ignore"},
	"Wrapped Boots": {"base": "Wrapped Boots", "other": ["Rarity <= Magic", "ItemLevel <= 11"], "type": "leveling low"},
	"Strapped Boots": {"base": "Strapped Boots", "other": ["Rarity <= Magic", "ItemLevel <= 21"], "type": "leveling low"},
	"Clasped Boots": {"base": "Clasped Boots", "other": ["Rarity <= Magic", "ItemLevel <= 32"], "type": "leveling low"},
	"Shackled Boots": {"base": "Shackled Boots", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "leveling low"},
	"Trapper Boots": {"base": "Trapper Boots", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "leveling low"},
	"Ambush Boots": {"base": "Ambush Boots", "other": ["Rarity <= Magic", "ItemLevel <= 52"], "type": "ignore"},
	"Carnal Boots": {"base": "Carnal Boots", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Assassin's Boots": {"base": "Assassin's Boots", "other": ["Rarity <= Magic", "ItemLevel <= 68"], "type": "ignore"},
	"Murder Boots": {"base": "Murder Boots", "other": ["Rarity <= Magic", "ItemLevel <= 74"], "type": "ignore"},
	"Wrapped Mitts": {"base": "Wrapped Mitts", "other": ["Rarity <= Magic", "ItemLevel <= 10"], "type": "leveling low"},
	"Strapped Mitts": {"base": "Strapped Mitts", "other": ["Rarity <= Magic", "ItemLevel <= 21"], "type": "leveling low"},
	"Clasped Mitts": {"base": "Clasped Mitts", "other": ["Rarity <= Magic", "ItemLevel <= 36"], "type": "leveling low"},
	"Trapper Mitts": {"base": "Trapper Mitts", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "leveling low"},
	"Ambush Mitts": {"base": "Ambush Mitts", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "leveling low"},
	"Carnal Mitts": {"base": "Carnal Mitts", "other": ["Rarity <= Magic", "ItemLevel <= 55"], "type": "ignore"},
	"Assassin's Mitts": {"base": "Assassin's Mitts", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Murder Mitts": {"base": "Murder Mitts", "other": ["Rarity <= Magic", "ItemLevel <= 72"], "type": "ignore"},
	"Scare Mask": {"base": "Scare Mask", "other": ["Rarity <= Magic", "ItemLevel <= 9"], "type": "leveling low"},
	"Plague Mask": {"base": "Plague Mask", "other": ["Rarity <= Magic", "ItemLevel <= 15"], "type": "leveling low"},
	"Iron Mask": {"base": "Iron Mask", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "leveling low"},
	"Festival Mask": {"base": "Festival Mask", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "leveling low"},
	"Golden Mask": {"base": "Golden Mask", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Raven Mask": {"base": "Raven Mask", "other": ["Rarity <= Magic", "ItemLevel <= 43"], "type": "leveling low"},
	"Callous Mask": {"base": "Callous Mask", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "leveling low"},
	"Regicide Mask": {"base": "Regicide Mask", "other": ["Rarity <= Magic", "ItemLevel <= 57"], "type": "ignore"},
	"Harlequin Mask": {"base": "Harlequin Mask", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "ignore"},
	"Vaal Mask": {"base": "Vaal Mask", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Deicide Mask": {"base": "Deicide Mask", "other": ["Rarity <= Magic", "ItemLevel <= 72"], "type": "ignore"},
	"Spiked Bundle": {"base": "Spiked Bundle", "other": ["Rarity <= Magic", "ItemLevel <= 10"], "type": "leveling low"},
	"Driftwood Spiked Shield": {"base": "Driftwood Spiked Shield", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "leveling low"},
	"Alloyed Spiked Shield": {"base": "Alloyed Spiked Shield", "other": ["Rarity <= Magic", "ItemLevel <= 25"], "type": "leveling low"},
	"Burnished Spiked Shield": {"base": "Burnished Spiked Shield", "other": ["Rarity <= Magic", "ItemLevel <= 32"], "type": "leveling low"},
	"Ornate Spiked Shield": {"base": "Ornate Spiked Shield", "other": ["Rarity <= Magic", "ItemLevel <= 38"], "type": "leveling low"},
	"Redwood Spiked Shield": {"base": "Redwood Spiked Shield", "other": ["Rarity <= Magic", "ItemLevel <= 44"], "type": "leveling low"},
	"Compound Spiked Shield": {"base": "Compound Spiked Shield", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "leveling low"},
	"Polished Spiked Shield": {"base": "Polished Spiked Shield", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "ignore"},
	"Sovereign Spiked Shield": {"base": "Sovereign Spiked Shield", "other": ["Rarity <= Magic", "ItemLevel <= 59"], "type": "ignore"},
	"Alder Spiked Shield": {"base": "Alder Spiked Shield", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Ezomyte Spiked Shield": {"base": "Ezomyte Spiked Shield", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Mirrored Spiked Shield": {"base": "Mirrored Spiked Shield", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "ignore"},
	"Supreme Spiked Shield": {"base": "Supreme Spiked Shield", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"}
}
