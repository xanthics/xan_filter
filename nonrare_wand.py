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
	"Driftwood Wand": {"base": "Driftwood Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 6"], "type": "normal"},
	"Goat's Horn": {"base": "Goat's Horn", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 11"], "type": "normal"},
	"Carved Wand": {"base": "Carved Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "normal"},
	"Quartz Wand": {"base": "Quartz Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 23"], "type": "normal"},
	"Spiraled Wand": {"base": "Spiraled Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 29"], "type": "normal"},
	"Sage Wand": {"base": "Sage Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 35"], "type": "normal"},
	"Pagan Wand": {"base": "Pagan Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "normal"},
	"Faun's Horn": {"base": "Faun's Horn", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "normal"},
	"Engraved Wand": {"base": "Engraved Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 45"], "type": "normal"},
	"Crystal Wand": {"base": "Crystal Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "normal"},
	"Serpent Wand": {"base": "Serpent Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "normal"},
	"Omen Wand": {"base": "Omen Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "normal"},
	"Heathen Wand": {"base": "Heathen Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "normal"},
	"Demon's Horn": {"base": "Demon's Horn", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "normal"},
	"Imbued Wand": {"base": "Imbued Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "normal"},
	"Opal Wand": {"base": "Opal Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "normal"},
	"Tornado Wand": {"base": "Tornado Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "normal"},
	"Prophecy Wand": {"base": "Prophecy Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "normal"},
	"Profane Wand": {"base": "Profane Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "normal"}
}
