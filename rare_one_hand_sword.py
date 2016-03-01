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
	"Rusted Sword": {"base": "Rusted Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 6"], "type": "normal"},
	"Copper Sword": {"base": "Copper Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 10"], "type": "normal"},
	"Sabre": {"base": "Sabre", "class": "One Hand Sword", "other": ["ItemLevel <= 15"], "type": "normal"},
	"Broad Sword": {"base": "Broad Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 20"], "type": "normal"},
	"War Sword": {"base": "War Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 25"], "type": "normal"},
	"Ancient Sword": {"base": "Ancient Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 29"], "type": "normal"},
	"Elegant Sword": {"base": "Elegant Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 33"], "type": "normal"},
	"Dusk Blade": {"base": "Dusk Blade", "class": "One Hand Sword", "other": ["ItemLevel <= 37"], "type": "normal"},
	"Hook Sword": {"base": "Hook Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 39"], "type": "normal"},
	"Variscite Blade": {"base": "Variscite Blade", "class": "One Hand Sword", "other": ["ItemLevel <= 40"], "type": "normal"},
	"Cutlass": {"base": "Cutlass", "class": "One Hand Sword", "other": ["ItemLevel <= 43"], "type": "normal"},
	"Baselard": {"base": "Baselard", "class": "One Hand Sword", "other": ["ItemLevel <= 46"], "type": "normal"},
	"Battle Sword": {"base": "Battle Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 49"], "type": "normal"},
	"Elder Sword": {"base": "Elder Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 52"], "type": "normal"},
	"Graceful Sword": {"base": "Graceful Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 55"], "type": "normal"},
	"Twilight Blade": {"base": "Twilight Blade", "class": "One Hand Sword", "other": ["ItemLevel <= 58"], "type": "normal"},
	"Grappler": {"base": "Grappler", "class": "One Hand Sword", "other": ["ItemLevel <= 60"], "type": "normal"},
	"Gemstone Sword": {"base": "Gemstone Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 61"], "type": "normal"},
	"Corsair Sword": {"base": "Corsair Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 63"], "type": "normal"},
	"Gladius": {"base": "Gladius", "class": "One Hand Sword", "other": ["ItemLevel <= 65"], "type": "normal"},
	"Legion Sword": {"base": "Legion Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 67"], "type": "normal"},
	"Vaal Blade": {"base": "Vaal Blade", "class": "One Hand Sword", "other": ["ItemLevel <= 69"], "type": "normal"},
	"Eternal Sword": {"base": "Eternal Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 71"], "type": "normal"},
	"Midnight Blade": {"base": "Midnight Blade", "class": "One Hand Sword", "other": ["ItemLevel <= 73"], "type": "normal"},
	"Tiger Hook": {"base": "Tiger Hook", "class": "One Hand Sword", "other": ["ItemLevel <= 75"], "type": "normal"}
}
