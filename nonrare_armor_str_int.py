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
				  "Sockets > 2",
				  "SetBackgroundColor 0 0 0 100",
				  "SetBorderColor 255 40 0"],
	"high": ["SetFontSize 24",
			 "Sockets > 2",
			 "SetBackgroundColor 0 0 0 100",
			 "SetBorderColor 0 100 150"],
	"normal": ["SetFontSize 18",
			   "Sockets > 2",
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
	"Chainmail Vest": {"base": "Chainmail Vest", "other": ["Rarity <= Magic", "ItemLevel <= 9"], "type": "normal"},
	"Chainmail Tunic": {"base": "Chainmail Tunic", "other": ["Rarity <= Magic", "ItemLevel <= 13"], "type": "normal"},
	"Ringmail Coat": {"base": "Ringmail Coat", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "normal"},
	"Chainmail Doublet": {"base": "Chainmail Doublet", "other": ["Rarity <= Magic", "ItemLevel <= 26"], "type": "normal"},
	"Full Ringmail": {"base": "Full Ringmail", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "normal"},
	"Full Chainmail": {"base": "Full Chainmail", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "normal"},
	"Holy Chainmail": {"base": "Holy Chainmail", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "normal"},
	"Latticed Ringmail": {"base": "Latticed Ringmail", "other": ["Rarity <= Magic", "ItemLevel <= 44"], "type": "normal"},
	"Crusader Chainmail": {"base": "Crusader Chainmail", "other": ["Rarity <= Magic", "ItemLevel <= 48"], "type": "normal"},
	"Ornate Ringmail": {"base": "Ornate Ringmail", "other": ["Rarity <= Magic", "ItemLevel <= 52"], "type": "normal"},
	"Chain Hauberk": {"base": "Chain Hauberk", "other": ["Rarity <= Magic", "ItemLevel <= 56"], "type": "normal"},
	"Devout Chainmail": {"base": "Devout Chainmail", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "normal"},
	"Loricated Ringmail": {"base": "Loricated Ringmail", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "normal"},
	"Conquest Chainmail": {"base": "Conquest Chainmail", "other": ["Rarity <= Magic", "ItemLevel <= 66"], "type": "normal"},
	"Elegant Ringmail": {"base": "Elegant Ringmail", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "normal"},
	"Saint's Hauberk": {"base": "Saint's Hauberk", "other": ["Rarity <= Magic", "ItemLevel <= 72"], "type": "normal"},
	"Saintly Chainmail": {"base": "Saintly Chainmail", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "normal"},
	"Chain Boots": {"base": "Chain Boots", "other": ["Rarity <= Magic", "ItemLevel <= 10"], "type": "normal"},
	"Ringmail Boots": {"base": "Ringmail Boots", "other": ["Rarity <= Magic", "ItemLevel <= 18"], "type": "normal"},
	"Mesh Boots": {"base": "Mesh Boots", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "normal"},
	"Riveted Boots": {"base": "Riveted Boots", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "normal"},
	"Zealot Boots": {"base": "Zealot Boots", "other": ["Rarity <= Magic", "ItemLevel <= 45"], "type": "normal"},
	"Soldier Boots": {"base": "Soldier Boots", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "normal"},
	"Legion Boots": {"base": "Legion Boots", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "normal"},
	"Crusader Boots": {"base": "Crusader Boots", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "normal"},
	"Chain Gloves": {"base": "Chain Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 12"], "type": "normal"},
	"Ringmail Gloves": {"base": "Ringmail Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 24"], "type": "normal"},
	"Mesh Gloves": {"base": "Mesh Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "normal"},
	"Riveted Gloves": {"base": "Riveted Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "normal"},
	"Zealot Gloves": {"base": "Zealot Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 48"], "type": "normal"},
	"Soldier Gloves": {"base": "Soldier Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 56"], "type": "normal"},
	"Legion Gloves": {"base": "Legion Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "normal"},
	"Crusader Gloves": {"base": "Crusader Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "normal"},
	"Rusted Coif": {"base": "Rusted Coif", "other": ["Rarity <= Magic", "ItemLevel <= 10"], "type": "normal"},
	"Soldier Helmet": {"base": "Soldier Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "normal"},
	"Great Helmet": {"base": "Great Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 27"], "type": "normal"},
	"Crusader Helmet": {"base": "Crusader Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 36"], "type": "normal"},
	"Aventail Helmet": {"base": "Aventail Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "normal"},
	"Zealot Helmet": {"base": "Zealot Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 49"], "type": "normal"},
	"Great Crown": {"base": "Great Crown", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "normal"},
	"Magistrate Crown": {"base": "Magistrate Crown", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "normal"},
	"Prophet Crown": {"base": "Prophet Crown", "other": ["Rarity <= Magic", "ItemLevel <= 68"], "type": "normal"},
	"Praetor Crown": {"base": "Praetor Crown", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "normal"},
	"Plank Kite Shield": {"base": "Plank Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 12"], "type": "normal"},
	"Linden Kite Shield": {"base": "Linden Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 18"], "type": "normal"},
	"Reinforced Kite Shield": {"base": "Reinforced Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 25"], "type": "normal"},
	"Layered Kite Shield": {"base": "Layered Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 32"], "type": "normal"},
	"Ceremonial Kite Shield": {"base": "Ceremonial Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "normal"},
	"Etched Kite Shield": {"base": "Etched Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 45"], "type": "normal"},
	"Steel Kite Shield": {"base": "Steel Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 51"], "type": "normal"},
	"Laminated Kite Shield": {"base": "Laminated Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 55"], "type": "normal"},
	"Angelic Kite Shield": {"base": "Angelic Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "normal"},
	"Branded Kite Shield": {"base": "Branded Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "normal"},
	"Champion Kite Shield": {"base": "Champion Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "normal"},
	"Mosaic Kite Shield": {"base": "Mosaic Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "normal"},
	"Archon Kite Shield": {"base": "Archon Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "normal"}
}
