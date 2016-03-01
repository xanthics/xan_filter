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
	"Chainmail Vest": {"base": "Chainmail Vest", "other": ["ItemLevel <= 9"], "type": "normal"},
	"Chainmail Tunic": {"base": "Chainmail Tunic", "other": ["ItemLevel <= 13"], "type": "normal"},
	"Ringmail Coat": {"base": "Ringmail Coat", "other": ["ItemLevel <= 22"], "type": "normal"},
	"Chainmail Doublet": {"base": "Chainmail Doublet", "other": ["ItemLevel <= 26"], "type": "normal"},
	"Full Ringmail": {"base": "Full Ringmail", "other": ["ItemLevel <= 33"], "type": "normal"},
	"Full Chainmail": {"base": "Full Chainmail", "other": ["ItemLevel <= 37"], "type": "normal"},
	"Holy Chainmail": {"base": "Holy Chainmail", "other": ["ItemLevel <= 40"], "type": "normal"},
	"Latticed Ringmail": {"base": "Latticed Ringmail", "other": ["ItemLevel <= 44"], "type": "normal"},
	"Crusader Chainmail": {"base": "Crusader Chainmail", "other": ["ItemLevel <= 48"], "type": "normal"},
	"Ornate Ringmail": {"base": "Ornate Ringmail", "other": ["ItemLevel <= 52"], "type": "normal"},
	"Chain Hauberk": {"base": "Chain Hauberk", "other": ["ItemLevel <= 56"], "type": "normal"},
	"Devout Chainmail": {"base": "Devout Chainmail", "other": ["ItemLevel <= 60"], "type": "normal"},
	"Loricated Ringmail": {"base": "Loricated Ringmail", "other": ["ItemLevel <= 63"], "type": "normal"},
	"Conquest Chainmail": {"base": "Conquest Chainmail", "other": ["ItemLevel <= 66"], "type": "normal"},
	"Elegant Ringmail": {"base": "Elegant Ringmail", "other": ["ItemLevel <= 69"], "type": "normal"},
	"Saint's Hauberk": {"base": "Saint's Hauberk", "other": ["ItemLevel <= 72"], "type": "normal"},
	"Saintly Chainmail": {"base": "Saintly Chainmail", "other": ["ItemLevel <= 75"], "type": "normal"},
	"Chain Boots": {"base": "Chain Boots", "other": ["ItemLevel <= 10"], "type": "normal"},
	"Ringmail Boots": {"base": "Ringmail Boots", "other": ["ItemLevel <= 18"], "type": "normal"},
	"Mesh Boots": {"base": "Mesh Boots", "other": ["ItemLevel <= 33"], "type": "normal"},
	"Riveted Boots": {"base": "Riveted Boots", "other": ["ItemLevel <= 41"], "type": "normal"},
	"Zealot Boots": {"base": "Zealot Boots", "other": ["ItemLevel <= 45"], "type": "normal"},
	"Soldier Boots": {"base": "Soldier Boots", "other": ["ItemLevel <= 54"], "type": "normal"},
	"Legion Boots": {"base": "Legion Boots", "other": ["ItemLevel <= 63"], "type": "normal"},
	"Crusader Boots": {"base": "Crusader Boots", "other": ["ItemLevel <= 69"], "type": "normal"},
	"Chain Gloves": {"base": "Chain Gloves", "other": ["ItemLevel <= 12"], "type": "normal"},
	"Ringmail Gloves": {"base": "Ringmail Gloves", "other": ["ItemLevel <= 24"], "type": "normal"},
	"Mesh Gloves": {"base": "Mesh Gloves", "other": ["ItemLevel <= 37"], "type": "normal"},
	"Riveted Gloves": {"base": "Riveted Gloves", "other": ["ItemLevel <= 42"], "type": "normal"},
	"Zealot Gloves": {"base": "Zealot Gloves", "other": ["ItemLevel <= 48"], "type": "normal"},
	"Soldier Gloves": {"base": "Soldier Gloves", "other": ["ItemLevel <= 56"], "type": "normal"},
	"Legion Gloves": {"base": "Legion Gloves", "other": ["ItemLevel <= 62"], "type": "normal"},
	"Crusader Gloves": {"base": "Crusader Gloves", "other": ["ItemLevel <= 71"], "type": "normal"},
	"Rusted Coif": {"base": "Rusted Coif", "other": ["ItemLevel <= 10"], "type": "normal"},
	"Soldier Helmet": {"base": "Soldier Helmet", "other": ["ItemLevel <= 17"], "type": "normal"},
	"Great Helmet": {"base": "Great Helmet", "other": ["ItemLevel <= 27"], "type": "normal"},
	"Crusader Helmet": {"base": "Crusader Helmet", "other": ["ItemLevel <= 36"], "type": "normal"},
	"Aventail Helmet": {"base": "Aventail Helmet", "other": ["ItemLevel <= 42"], "type": "normal"},
	"Zealot Helmet": {"base": "Zealot Helmet", "other": ["ItemLevel <= 49"], "type": "normal"},
	"Great Crown": {"base": "Great Crown", "other": ["ItemLevel <= 58"], "type": "normal"},
	"Magistrate Crown": {"base": "Magistrate Crown", "other": ["ItemLevel <= 63"], "type": "normal"},
	"Prophet Crown": {"base": "Prophet Crown", "other": ["ItemLevel <= 68"], "type": "normal"},
	"Praetor Crown": {"base": "Praetor Crown", "other": ["ItemLevel <= 73"], "type": "normal"},
	"Plank Kite Shield": {"base": "Plank Kite Shield", "other": ["ItemLevel <= 12"], "type": "normal"},
	"Linden Kite Shield": {"base": "Linden Kite Shield", "other": ["ItemLevel <= 18"], "type": "normal"},
	"Reinforced Kite Shield": {"base": "Reinforced Kite Shield", "other": ["ItemLevel <= 25"], "type": "normal"},
	"Layered Kite Shield": {"base": "Layered Kite Shield", "other": ["ItemLevel <= 32"], "type": "normal"},
	"Ceremonial Kite Shield": {"base": "Ceremonial Kite Shield", "other": ["ItemLevel <= 39"], "type": "normal"},
	"Etched Kite Shield": {"base": "Etched Kite Shield", "other": ["ItemLevel <= 45"], "type": "normal"},
	"Steel Kite Shield": {"base": "Steel Kite Shield", "other": ["ItemLevel <= 51"], "type": "normal"},
	"Laminated Kite Shield": {"base": "Laminated Kite Shield", "other": ["ItemLevel <= 55"], "type": "normal"},
	"Angelic Kite Shield": {"base": "Angelic Kite Shield", "other": ["ItemLevel <= 60"], "type": "normal"},
	"Branded Kite Shield": {"base": "Branded Kite Shield", "other": ["ItemLevel <= 64"], "type": "normal"},
	"Champion Kite Shield": {"base": "Champion Kite Shield", "other": ["ItemLevel <= 67"], "type": "normal"},
	"Mosaic Kite Shield": {"base": "Mosaic Kite Shield", "other": ["ItemLevel <= 70"], "type": "normal"},
	"Archon Kite Shield": {"base": "Archon Kite Shield", "other": ["ItemLevel <= 73"], "type": "normal"}
}
