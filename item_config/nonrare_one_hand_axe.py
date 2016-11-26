"""
* Copyright (c) 2016 Jeremy Parks. All rights reserved.
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
	"Rusted Hatchet": {"base": "Rusted Hatchet", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 7"], "type": "leveling low"},
	"Jade Hatchet": {"base": "Jade Hatchet", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 11"], "type": "leveling low"},
	"Boarding Axe": {"base": "Boarding Axe", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 16"], "type": "leveling low"},
	"Cleaver": {"base": "Cleaver", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 21"], "type": "leveling low"},
	"Broad Axe": {"base": "Broad Axe", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 26"], "type": "leveling low"},
	"Arming Axe": {"base": "Arming Axe", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 30"], "type": "leveling low"},
	"Decorative Axe": {"base": "Decorative Axe", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 34"], "type": "leveling low"},
	"Spectral Axe": {"base": "Spectral Axe", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 38"], "type": "leveling low"},
	"Etched Hatchet": {"base": "Etched Hatchet", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Jasper Axe": {"base": "Jasper Axe", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "leveling low"},
	"Tomahawk": {"base": "Tomahawk", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 44"], "type": "leveling low"},
	"Wrist Chopper": {"base": "Wrist Chopper", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 47"], "type": "leveling low"},
	"War Axe": {"base": "War Axe", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "leveling low"},
	"Chest Splitter": {"base": "Chest Splitter", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 53"], "type": "ignore"},
	"Ceremonial Axe": {"base": "Ceremonial Axe", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 56"], "type": "ignore"},
	"Wraith Axe": {"base": "Wraith Axe", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 59"], "type": "ignore"},
	"Engraved Hatchet": {"base": "Engraved Hatchet", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "ignore"},
	"Karui Axe": {"base": "Karui Axe", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "ignore"},
	"Siege Axe": {"base": "Siege Axe", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "ignore"},
	"Reaver Axe": {"base": "Reaver Axe", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 66"], "type": "ignore"},
	"Butcher Axe": {"base": "Butcher Axe", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 68"], "type": "ignore"},
	"Vaal Hatchet": {"base": "Vaal Hatchet", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "ignore"},
	"Royal Axe": {"base": "Royal Axe", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 72"], "type": "ignore"},
	"Infernal Axe": {"base": "Infernal Axe", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 74"], "type": "ignore"},
	"Runic Hatchet": {"base": "Runic Hatchet", "class": "One Hand Axe", "other": ["Rarity <= Magic", "ItemLevel <= 76"], "type": "ignore"}
}
