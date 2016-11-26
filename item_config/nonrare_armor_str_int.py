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
	"Chainmail Vest": {"base": "Chainmail Vest", "other": ["Rarity <= Magic", "ItemLevel <= 9"], "type": "leveling low"},
	"Chainmail Tunic": {"base": "Chainmail Tunic", "other": ["Rarity <= Magic", "ItemLevel <= 13"], "type": "leveling low"},
	"Ringmail Coat": {"base": "Ringmail Coat", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "leveling low"},
	"Chainmail Doublet": {"base": "Chainmail Doublet", "other": ["Rarity <= Magic", "ItemLevel <= 26"], "type": "leveling low"},
	"Full Ringmail": {"base": "Full Ringmail", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "leveling low"},
	"Full Chainmail": {"base": "Full Chainmail", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "leveling low"},
	"Holy Chainmail": {"base": "Holy Chainmail", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Latticed Ringmail": {"base": "Latticed Ringmail", "other": ["Rarity <= Magic", "ItemLevel <= 44"], "type": "leveling low"},
	"Crusader Chainmail": {"base": "Crusader Chainmail", "other": ["Rarity <= Magic", "ItemLevel <= 48"], "type": "leveling low"},
	"Ornate Ringmail": {"base": "Ornate Ringmail", "other": ["Rarity <= Magic", "ItemLevel <= 52"], "type": "ignore"},
	"Chain Hauberk": {"base": "Chain Hauberk", "other": ["Rarity <= Magic", "ItemLevel <= 56"], "type": "ignore"},
	"Devout Chainmail": {"base": "Devout Chainmail", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Loricated Ringmail": {"base": "Loricated Ringmail", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Conquest Chainmail": {"base": "Conquest Chainmail", "other": ["Rarity <= Magic", "ItemLevel <= 66"], "type": "ignore"},
	"Elegant Ringmail": {"base": "Elegant Ringmail", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "ignore"},
	"Saint's Hauberk": {"base": "Saint's Hauberk", "other": ["Rarity <= Magic", "ItemLevel <= 72"], "type": "ignore"},
	"Saintly Chainmail": {"base": "Saintly Chainmail", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"},
	"Chain Boots": {"base": "Chain Boots", "other": ["Rarity <= Magic", "ItemLevel <= 10"], "type": "leveling low"},
	"Ringmail Boots": {"base": "Ringmail Boots", "other": ["Rarity <= Magic", "ItemLevel <= 18"], "type": "leveling low"},
	"Mesh Boots": {"base": "Mesh Boots", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "leveling low"},
	"Riveted Boots": {"base": "Riveted Boots", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "leveling low"},
	"Zealot Boots": {"base": "Zealot Boots", "other": ["Rarity <= Magic", "ItemLevel <= 45"], "type": "leveling low"},
	"Soldier Boots": {"base": "Soldier Boots", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "ignore"},
	"Legion Boots": {"base": "Legion Boots", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Crusader Boots": {"base": "Crusader Boots", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "ignore"},
	"Chain Gloves": {"base": "Chain Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 12"], "type": "leveling low"},
	"Ringmail Gloves": {"base": "Ringmail Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 24"], "type": "leveling low"},
	"Mesh Gloves": {"base": "Mesh Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "leveling low"},
	"Riveted Gloves": {"base": "Riveted Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "leveling low"},
	"Zealot Gloves": {"base": "Zealot Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 48"], "type": "leveling low"},
	"Soldier Gloves": {"base": "Soldier Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 56"], "type": "ignore"},
	"Legion Gloves": {"base": "Legion Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "ignore"},
	"Crusader Gloves": {"base": "Crusader Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "ignore"},
	"Rusted Coif": {"base": "Rusted Coif", "other": ["Rarity <= Magic", "ItemLevel <= 10"], "type": "leveling low"},
	"Soldier Helmet": {"base": "Soldier Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "leveling low"},
	"Great Helmet": {"base": "Great Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 27"], "type": "leveling low"},
	"Crusader Helmet": {"base": "Crusader Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 36"], "type": "leveling low"},
	"Aventail Helmet": {"base": "Aventail Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "leveling low"},
	"Zealot Helmet": {"base": "Zealot Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 49"], "type": "leveling low"},
	"Great Crown": {"base": "Great Crown", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "ignore"},
	"Magistrate Crown": {"base": "Magistrate Crown", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Prophet Crown": {"base": "Prophet Crown", "other": ["Rarity <= Magic", "ItemLevel <= 68"], "type": "ignore"},
	"Praetor Crown": {"base": "Praetor Crown", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"},
	"Plank Kite Shield": {"base": "Plank Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 12"], "type": "leveling low"},
	"Linden Kite Shield": {"base": "Linden Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 18"], "type": "leveling low"},
	"Reinforced Kite Shield": {"base": "Reinforced Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 25"], "type": "leveling low"},
	"Layered Kite Shield": {"base": "Layered Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 32"], "type": "leveling low"},
	"Ceremonial Kite Shield": {"base": "Ceremonial Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "leveling low"},
	"Etched Kite Shield": {"base": "Etched Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 45"], "type": "leveling low"},
	"Steel Kite Shield": {"base": "Steel Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 51"], "type": "ignore"},
	"Laminated Kite Shield": {"base": "Laminated Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 55"], "type": "ignore"},
	"Angelic Kite Shield": {"base": "Angelic Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Branded Kite Shield": {"base": "Branded Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "ignore"},
	"Champion Kite Shield": {"base": "Champion Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Mosaic Kite Shield": {"base": "Mosaic Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "ignore"},
	"Archon Kite Shield": {"base": "Archon Kite Shield", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"}
}
