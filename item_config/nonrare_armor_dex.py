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
	"Shabby Jerkin": {"base": "Shabby Jerkin", "other": ["Rarity <= Magic", "ItemLevel <= 7"], "type": "leveling low"},
	"Strapped Leather": {"base": "Strapped Leather", "other": ["Rarity <= Magic", "ItemLevel <= 14"], "type": "leveling low"},
	"Buckskin Tunic": {"base": "Buckskin Tunic", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "leveling low"},
	"Wild Leather": {"base": "Wild Leather", "other": ["Rarity <= Magic", "ItemLevel <= 30"], "type": "leveling low"},
	"Full Leather": {"base": "Full Leather", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "leveling low"},
	"Sun Leather": {"base": "Sun Leather", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "leveling low"},
	"Thief's Garb": {"base": "Thief's Garb", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Eelskin Tunic": {"base": "Eelskin Tunic", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "leveling low"},
	"Frontier Leather": {"base": "Frontier Leather", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "leveling low"},
	"Glorious Leather": {"base": "Glorious Leather", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "leveling low"},
	"Coronal Leather": {"base": "Coronal Leather", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "ignore"},
	"Cutthroat's Garb": {"base": "Cutthroat's Garb", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "ignore"},
	"Sharkskin Tunic": {"base": "Sharkskin Tunic", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "ignore"},
	"Destiny Leather": {"base": "Destiny Leather", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "ignore"},
	"Exquisite Leather": {"base": "Exquisite Leather", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Zodiac Leather": {"base": "Zodiac Leather", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "ignore"},
	"Assassin's Garb": {"base": "Assassin's Garb", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"},
	"Rawhide Boots": {"base": "Rawhide Boots", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "leveling low"},
	"Goathide Boots": {"base": "Goathide Boots", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "leveling low"},
	"Deerskin Boots": {"base": "Deerskin Boots", "other": ["Rarity <= Magic", "ItemLevel <= 27"], "type": "leveling low"},
	"Nubuck Boots": {"base": "Nubuck Boots", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "leveling low"},
	"Eelskin Boots": {"base": "Eelskin Boots", "other": ["Rarity <= Magic", "ItemLevel <= 44"], "type": "leveling low"},
	"Sharkskin Boots": {"base": "Sharkskin Boots", "other": ["Rarity <= Magic", "ItemLevel <= 49"], "type": "leveling low"},
	"Shagreen Boots": {"base": "Shagreen Boots", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Stealth Boots": {"base": "Stealth Boots", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Slink Boots": {"base": "Slink Boots", "other": ["Rarity <= Magic", "ItemLevel <= 74"], "type": "ignore"},
	"Rawhide Gloves": {"base": "Rawhide Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "leveling low"},
	"Goathide Gloves": {"base": "Goathide Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 14"], "type": "leveling low"},
	"Deerskin Gloves": {"base": "Deerskin Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 26"], "type": "leveling low"},
	"Nubuck Gloves": {"base": "Nubuck Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 38"], "type": "leveling low"},
	"Eelskin Gloves": {"base": "Eelskin Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 43"], "type": "leveling low"},
	"Sharkskin Gloves": {"base": "Sharkskin Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "leveling low"},
	"Shagreen Gloves": {"base": "Shagreen Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 59"], "type": "ignore"},
	"Stealth Gloves": {"base": "Stealth Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Slink Gloves": {"base": "Slink Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"},
	"Leather Cap": {"base": "Leather Cap", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "leveling low"},
	"Tricorne": {"base": "Tricorne", "other": ["Rarity <= Magic", "ItemLevel <= 15"], "type": "leveling low"},
	"Leather Hood": {"base": "Leather Hood", "other": ["Rarity <= Magic", "ItemLevel <= 25"], "type": "leveling low"},
	"Wolf Pelt": {"base": "Wolf Pelt", "other": ["Rarity <= Magic", "ItemLevel <= 35"], "type": "leveling low"},
	"Hunter Hood": {"base": "Hunter Hood", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "leveling low"},
	"Noble Tricorne": {"base": "Noble Tricorne", "other": ["Rarity <= Magic", "ItemLevel <= 52"], "type": "ignore"},
	"Ursine Pelt": {"base": "Ursine Pelt", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Silken Hood": {"base": "Silken Hood", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "ignore"},
	"Sinner Tricorne": {"base": "Sinner Tricorne", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "ignore"},
	"Lion Pelt": {"base": "Lion Pelt", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"},
	"Goathide Buckler": {"base": "Goathide Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 7"], "type": "leveling low"},
	"Pine Buckler": {"base": "Pine Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 13"], "type": "leveling low"},
	"Painted Buckler": {"base": "Painted Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 21"], "type": "leveling low"},
	"Hammered Buckler": {"base": "Hammered Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 28"], "type": "leveling low"},
	"War Buckler": {"base": "War Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 34"], "type": "leveling low"},
	"Gilded Buckler": {"base": "Gilded Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "leveling low"},
	"Oak Buckler": {"base": "Oak Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 43"], "type": "leveling low"},
	"Enameled Buckler": {"base": "Enameled Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 47"], "type": "leveling low"},
	"Corrugated Buckler": {"base": "Corrugated Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 51"], "type": "ignore"},
	"Battle Buckler": {"base": "Battle Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 55"], "type": "ignore"},
	"Golden Buckler": {"base": "Golden Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 59"], "type": "ignore"},
	"Ironwood Buckler": {"base": "Ironwood Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "ignore"},
	"Lacquered Buckler": {"base": "Lacquered Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "ignore"},
	"Vaal Buckler": {"base": "Vaal Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 68"], "type": "ignore"},
	"Crusader Buckler": {"base": "Crusader Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "ignore"},
	"Imperial Buckler": {"base": "Imperial Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 74"], "type": "ignore"}
}
