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
	"high": ["SetFontSize 24",
			 "SetBackgroundColor 0 0 0 100",
			 "SetBorderColor 0 100 150"],
	"normal": ["SetFontSize 18",
			   "SetBackgroundColor 0 0 0 100",
			   "SetBorderColor 100 100 100"],
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
	"Shabby Jerkin": {"base": "Shabby Jerkin", "other": ["Rarity <= Magic", "ItemLevel <= 7"], "type": "normal"},
	"Strapped Leather": {"base": "Strapped Leather", "other": ["Rarity <= Magic", "ItemLevel <= 14"], "type": "normal"},
	"Buckskin Tunic": {"base": "Buckskin Tunic", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "normal"},
	"Wild Leather": {"base": "Wild Leather", "other": ["Rarity <= Magic", "ItemLevel <= 30"], "type": "normal"},
	"Full Leather": {"base": "Full Leather", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "normal"},
	"Sun Leather": {"base": "Sun Leather", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "normal"},
	"Thief's Garb": {"base": "Thief's Garb", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "normal"},
	"Eelskin Tunic": {"base": "Eelskin Tunic", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "normal"},
	"Frontier Leather": {"base": "Frontier Leather", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "normal"},
	"Glorious Leather": {"base": "Glorious Leather", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "normal"},
	"Coronal Leather": {"base": "Coronal Leather", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "normal"},
	"Cutthroat's Garb": {"base": "Cutthroat's Garb", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "normal"},
	"Sharkskin Tunic": {"base": "Sharkskin Tunic", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "normal"},
	"Destiny Leather": {"base": "Destiny Leather", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "normal"},
	"Exquisite Leather": {"base": "Exquisite Leather", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "normal"},
	"Zodiac Leather": {"base": "Zodiac Leather", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "normal"},
	"Assassin's Garb": {"base": "Assassin's Garb", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "normal"},
	"Rawhide Boots": {"base": "Rawhide Boots", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "normal"},
	"Goathide Boots": {"base": "Goathide Boots", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "normal"},
	"Deerskin Boots": {"base": "Deerskin Boots", "other": ["Rarity <= Magic", "ItemLevel <= 27"], "type": "normal"},
	"Nubuck Boots": {"base": "Nubuck Boots", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "normal"},
	"Eelskin Boots": {"base": "Eelskin Boots", "other": ["Rarity <= Magic", "ItemLevel <= 44"], "type": "normal"},
	"Sharkskin Boots": {"base": "Sharkskin Boots", "other": ["Rarity <= Magic", "ItemLevel <= 49"], "type": "normal"},
	"Shagreen Boots": {"base": "Shagreen Boots", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "normal"},
	"Stealth Boots": {"base": "Stealth Boots", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "normal"},
	"Slink Boots": {"base": "Slink Boots", "other": ["Rarity <= Magic", "ItemLevel <= 74"], "type": "normal"},
	"Rawhide Gloves": {"base": "Rawhide Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "normal"},
	"Goathide Gloves": {"base": "Goathide Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 14"], "type": "normal"},
	"Deerskin Gloves": {"base": "Deerskin Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 26"], "type": "normal"},
	"Nubuck Gloves": {"base": "Nubuck Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 38"], "type": "normal"},
	"Eelskin Gloves": {"base": "Eelskin Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 43"], "type": "normal"},
	"Sharkskin Gloves": {"base": "Sharkskin Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "normal"},
	"Shagreen Gloves": {"base": "Shagreen Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 59"], "type": "normal"},
	"Stealth Gloves": {"base": "Stealth Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "normal"},
	"Slink Gloves": {"base": "Slink Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "normal"},
	"Leather Cap": {"base": "Leather Cap", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "normal"},
	"Tricorne": {"base": "Tricorne", "other": ["Rarity <= Magic", "ItemLevel <= 15"], "type": "normal"},
	"Leather Hood": {"base": "Leather Hood", "other": ["Rarity <= Magic", "ItemLevel <= 25"], "type": "normal"},
	"Wolf Pelt": {"base": "Wolf Pelt", "other": ["Rarity <= Magic", "ItemLevel <= 35"], "type": "normal"},
	"Hunter Hood": {"base": "Hunter Hood", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "normal"},
	"Noble Tricorne": {"base": "Noble Tricorne", "other": ["Rarity <= Magic", "ItemLevel <= 52"], "type": "normal"},
	"Ursine Pelt": {"base": "Ursine Pelt", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "normal"},
	"Silken Hood": {"base": "Silken Hood", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "normal"},
	"Sinner Tricorne": {"base": "Sinner Tricorne", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "normal"},
	"Lion Pelt": {"base": "Lion Pelt", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "normal"},
	"Goathide Buckler": {"base": "Goathide Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 7"], "type": "normal"},
	"Pine Buckler": {"base": "Pine Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 13"], "type": "normal"},
	"Painted Buckler": {"base": "Painted Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 21"], "type": "normal"},
	"Hammered Buckler": {"base": "Hammered Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 28"], "type": "normal"},
	"War Buckler": {"base": "War Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 34"], "type": "normal"},
	"Gilded Buckler": {"base": "Gilded Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "normal"},
	"Oak Buckler": {"base": "Oak Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 43"], "type": "normal"},
	"Enameled Buckler": {"base": "Enameled Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 47"], "type": "normal"},
	"Corrugated Buckler": {"base": "Corrugated Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 51"], "type": "normal"},
	"Battle Buckler": {"base": "Battle Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 55"], "type": "normal"},
	"Golden Buckler": {"base": "Golden Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 59"], "type": "normal"},
	"Ironwood Buckler": {"base": "Ironwood Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "normal"},
	"Lacquered Buckler": {"base": "Lacquered Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "normal"},
	"Vaal Buckler": {"base": "Vaal Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 68"], "type": "normal"},
	"Crusader Buckler": {"base": "Crusader Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "normal"},
	"Imperial Buckler": {"base": "Imperial Buckler", "other": ["Rarity <= Magic", "ItemLevel <= 74"], "type": "normal"}
}
