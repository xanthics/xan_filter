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
	"Crude Bow": {"base": "Crude Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 6"], "type": "leveling low"},
	"Short Bow": {"base": "Short Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 10"], "type": "leveling low"},
	"Long Bow": {"base": "Long Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 14"], "type": "leveling low"},
	"Composite Bow": {"base": "Composite Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 19"], "type": "leveling low"},
	"Recurve Bow": {"base": "Recurve Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 23"], "type": "leveling low"},
	"Bone Bow": {"base": "Bone Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 28"], "type": "leveling low"},
	"Royal Bow": {"base": "Royal Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "leveling low"},
	"Death Bow": {"base": "Death Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "leveling high"},
	"Grove Bow": {"base": "Grove Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Reflex Bow": {"base": "Reflex Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "leveling low"},
	"Decurve Bow": {"base": "Decurve Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 43"], "type": "leveling low"},
	"Compound Bow": {"base": "Compound Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "leveling low"},
	"Sniper Bow": {"base": "Sniper Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 49"], "type": "leveling low"},
	"Ivory Bow": {"base": "Ivory Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 52"], "type": "ignore"},
	"Highborn Bow": {"base": "Highborn Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 55"], "type": "ignore"},
	"Decimation Bow": {"base": "Decimation Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "ignore"},
	"Thicket Bow": {"base": "Thicket Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "ignore"},
	"Steelwood Bow": {"base": "Steelwood Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "ignore"},
	"Citadel Bow": {"base": "Citadel Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Ranger Bow": {"base": "Ranger Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "ignore"},
	"Assassin Bow": {"base": "Assassin Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Spine Bow": {"base": "Spine Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "ignore"},
	"Imperial Bow": {"base": "Imperial Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "ignore"},
	"Harbinger Bow": {"base": "Harbinger Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"},
	"Maraketh Bow": {"base": "Maraketh Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 76"], "type": "ignore"}
}
