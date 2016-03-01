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
	"Rusted Hatchet": {"base": "Rusted Hatchet", "class": "One Hand Axe", "other": ["ItemLevel <= 7"], "type": "normal"},
	"Jade Hatchet": {"base": "Jade Hatchet", "class": "One Hand Axe", "other": ["ItemLevel <= 11"], "type": "normal"},
	"Boarding Axe": {"base": "Boarding Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 16"], "type": "normal"},
	"Cleaver": {"base": "Cleaver", "class": "One Hand Axe", "other": ["ItemLevel <= 21"], "type": "normal"},
	"Broad Axe": {"base": "Broad Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 26"], "type": "normal"},
	"Arming Axe": {"base": "Arming Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 30"], "type": "normal"},
	"Decorative Axe": {"base": "Decorative Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 34"], "type": "normal"},
	"Spectral Axe": {"base": "Spectral Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 38"], "type": "normal"},
	"Etched Hatchet": {"base": "Etched Hatchet", "class": "One Hand Axe", "other": ["ItemLevel <= 40"], "type": "normal"},
	"Jasper Axe": {"base": "Jasper Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 41"], "type": "normal"},
	"Tomahawk": {"base": "Tomahawk", "class": "One Hand Axe", "other": ["ItemLevel <= 44"], "type": "normal"},
	"Wrist Chopper": {"base": "Wrist Chopper", "class": "One Hand Axe", "other": ["ItemLevel <= 47"], "type": "normal"},
	"War Axe": {"base": "War Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 50"], "type": "normal"},
	"Chest Splitter": {"base": "Chest Splitter", "class": "One Hand Axe", "other": ["ItemLevel <= 53"], "type": "normal"},
	"Ceremonial Axe": {"base": "Ceremonial Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 56"], "type": "normal"},
	"Wraith Axe": {"base": "Wraith Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 59"], "type": "normal"},
	"Engraved Hatchet": {"base": "Engraved Hatchet", "class": "One Hand Axe", "other": ["ItemLevel <= 61"], "type": "normal"},
	"Karui Axe": {"base": "Karui Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 62"], "type": "normal"},
	"Siege Axe": {"base": "Siege Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 64"], "type": "normal"},
	"Reaver Axe": {"base": "Reaver Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 66"], "type": "normal"},
	"Butcher Axe": {"base": "Butcher Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 68"], "type": "normal"},
	"Vaal Hatchet": {"base": "Vaal Hatchet", "class": "One Hand Axe", "other": ["ItemLevel <= 70"], "type": "normal"},
	"Royal Axe": {"base": "Royal Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 72"], "type": "normal"},
	"Infernal Axe": {"base": "Infernal Axe", "class": "One Hand Axe", "other": ["ItemLevel <= 74"], "type": "normal"},
	"Runic Hatchet": {"base": "Runic Hatchet", "class": "One Hand Axe", "other": ["ItemLevel <= 76"], "type": "normal"}
}
