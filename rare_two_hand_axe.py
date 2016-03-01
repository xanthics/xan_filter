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
	"Stone Axe": {"base": "Stone Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 9"], "type": "normal"},
	"Jade Chopper": {"base": "Jade Chopper", "class": "Two Hand Axe", "other": ["ItemLevel <= 14"], "type": "normal"},
	"Woodsplitter": {"base": "Woodsplitter", "class": "Two Hand Axe", "other": ["ItemLevel <= 18"], "type": "normal"},
	"Poleaxe": {"base": "Poleaxe", "class": "Two Hand Axe", "other": ["ItemLevel <= 23"], "type": "normal"},
	"Double Axe": {"base": "Double Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 28"], "type": "normal"},
	"Gilded Axe": {"base": "Gilded Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 33"], "type": "normal"},
	"Shadow Axe": {"base": "Shadow Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 38"], "type": "normal"},
	"Dagger Axe": {"base": "Dagger Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 41"], "type": "normal"},
	"Jasper Chopper": {"base": "Jasper Chopper", "class": "Two Hand Axe", "other": ["ItemLevel <= 42"], "type": "normal"},
	"Timber Axe": {"base": "Timber Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 46"], "type": "normal"},
	"Headsman Axe": {"base": "Headsman Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 50"], "type": "normal"},
	"Labrys": {"base": "Labrys", "class": "Two Hand Axe", "other": ["ItemLevel <= 54"], "type": "normal"},
	"Noble Axe": {"base": "Noble Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 57"], "type": "normal"},
	"Abyssal Axe": {"base": "Abyssal Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 60"], "type": "normal"},
	"Karui Chopper": {"base": "Karui Chopper", "class": "Two Hand Axe", "other": ["ItemLevel <= 63"], "type": "normal"},
	"Talon Axe": {"base": "Talon Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 64"], "type": "normal"},
	"Sundering Axe": {"base": "Sundering Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 65"], "type": "normal"},
	"Ezomyte Axe": {"base": "Ezomyte Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 67"], "type": "normal"},
	"Vaal Axe": {"base": "Vaal Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 69"], "type": "normal"},
	"Despot Axe": {"base": "Despot Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 71"], "type": "normal"},
	"Void Axe": {"base": "Void Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 73"], "type": "normal"},
	"Fleshripper": {"base": "Fleshripper", "class": "Two Hand Axe", "other": ["ItemLevel <= 75"], "type": "normal"}
}
