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

desc = "Rare item for leveling or crafting"

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Chainmail Vest": {"base": "Chainmail Vest", "other": ["ItemLevel <= 9"], "type": "levelling rare normal"},
	"Chainmail Tunic": {"base": "Chainmail Tunic", "other": ["ItemLevel <= 13"], "type": "levelling rare normal"},
	"Ringmail Coat": {"base": "Ringmail Coat", "other": ["ItemLevel <= 22"], "type": "levelling rare normal"},
	"Chainmail Doublet": {"base": "Chainmail Doublet", "other": ["ItemLevel <= 26"], "type": "levelling rare normal"},
	"Full Ringmail": {"base": "Full Ringmail", "other": ["ItemLevel <= 33"], "type": "levelling rare normal"},
	"Full Chainmail": {"base": "Full Chainmail", "other": ["ItemLevel <= 37"], "type": "levelling rare normal"},
	"Holy Chainmail": {"base": "Holy Chainmail", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Latticed Ringmail": {"base": "Latticed Ringmail", "other": ["ItemLevel <= 44"], "type": "levelling rare normal"},
	"Crusader Chainmail": {"base": "Crusader Chainmail", "other": ["ItemLevel <= 48"], "type": "levelling rare normal"},
	"Ornate Ringmail": {"base": "Ornate Ringmail", "other": ["ItemLevel <= 52"], "type": "levelling rare normal"},
	"Chain Hauberk": {"base": "Chain Hauberk", "other": ["ItemLevel <= 56"], "type": "levelling rare normal"},
	"Devout Chainmail": {"base": "Devout Chainmail", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Loricated Ringmail": {"base": "Loricated Ringmail", "other": ["ItemLevel <= 63"], "type": "levelling rare normal"},
	"Conquest Chainmail": {"base": "Conquest Chainmail", "other": ["ItemLevel <= 66"], "type": "levelling rare normal"},
	"Elegant Ringmail": {"base": "Elegant Ringmail", "other": ["ItemLevel <= 69"], "type": "ignore"},
	"Saint's Hauberk": {"base": "Saint's Hauberk", "other": ["ItemLevel <= 72"], "type": "ignore"},
	"Saintly Chainmail": {"base": "Saintly Chainmail", "other": ["ItemLevel <= 75"], "type": "ignore"},
	"Chain Boots": {"base": "Chain Boots", "other": ["ItemLevel <= 10"], "type": "levelling rare normal"},
	"Ringmail Boots": {"base": "Ringmail Boots", "other": ["ItemLevel <= 18"], "type": "levelling rare normal"},
	"Mesh Boots": {"base": "Mesh Boots", "other": ["ItemLevel <= 33"], "type": "levelling rare normal"},
	"Riveted Boots": {"base": "Riveted Boots", "other": ["ItemLevel <= 41"], "type": "levelling rare normal"},
	"Zealot Boots": {"base": "Zealot Boots", "other": ["ItemLevel <= 45"], "type": "levelling rare normal"},
	"Soldier Boots": {"base": "Soldier Boots", "other": ["ItemLevel <= 54"], "type": "levelling rare normal"},
	"Legion Boots": {"base": "Legion Boots", "other": ["ItemLevel <= 63"], "type": "levelling rare normal"},
	"Crusader Boots": {"base": "Crusader Boots", "other": ["ItemLevel <= 69"], "type": "ignore"},
	"Chain Gloves": {"base": "Chain Gloves", "other": ["ItemLevel <= 12"], "type": "levelling rare normal"},
	"Ringmail Gloves": {"base": "Ringmail Gloves", "other": ["ItemLevel <= 24"], "type": "levelling rare normal"},
	"Mesh Gloves": {"base": "Mesh Gloves", "other": ["ItemLevel <= 37"], "type": "levelling rare normal"},
	"Riveted Gloves": {"base": "Riveted Gloves", "other": ["ItemLevel <= 42"], "type": "levelling rare normal"},
	"Zealot Gloves": {"base": "Zealot Gloves", "other": ["ItemLevel <= 48"], "type": "levelling rare normal"},
	"Soldier Gloves": {"base": "Soldier Gloves", "other": ["ItemLevel <= 56"], "type": "levelling rare normal"},
	"Legion Gloves": {"base": "Legion Gloves", "other": ["ItemLevel <= 62"], "type": "levelling rare normal"},
	"Crusader Gloves": {"base": "Crusader Gloves", "other": ["ItemLevel <= 71"], "type": "ignore"},
	"Rusted Coif": {"base": "Rusted Coif", "other": ["ItemLevel <= 10"], "type": "levelling rare normal"},
	"Soldier Helmet": {"base": "Soldier Helmet", "other": ["ItemLevel <= 17"], "type": "levelling rare normal"},
	"Great Helmet": {"base": "Great Helmet", "other": ["ItemLevel <= 27"], "type": "levelling rare normal"},
	"Crusader Helmet": {"base": "Crusader Helmet", "other": ["ItemLevel <= 36"], "type": "levelling rare normal"},
	"Aventail Helmet": {"base": "Aventail Helmet", "other": ["ItemLevel <= 42"], "type": "levelling rare normal"},
	"Zealot Helmet": {"base": "Zealot Helmet", "other": ["ItemLevel <= 49"], "type": "levelling rare normal"},
	"Great Crown": {"base": "Great Crown", "other": ["ItemLevel <= 58"], "type": "levelling rare normal"},
	"Magistrate Crown": {"base": "Magistrate Crown", "other": ["ItemLevel <= 63"], "type": "levelling rare normal"},
	"Prophet Crown": {"base": "Prophet Crown", "other": ["ItemLevel <= 68"], "type": "ignore"},
	"Praetor Crown": {"base": "Praetor Crown", "other": ["ItemLevel <= 73"], "type": "ignore"},
	"Plank Kite Shield": {"base": "Plank Kite Shield", "other": ["ItemLevel <= 12"], "type": "levelling rare normal"},
	"Linden Kite Shield": {"base": "Linden Kite Shield", "other": ["ItemLevel <= 18"], "type": "levelling rare normal"},
	"Reinforced Kite Shield": {"base": "Reinforced Kite Shield", "other": ["ItemLevel <= 25"], "type": "levelling rare normal"},
	"Layered Kite Shield": {"base": "Layered Kite Shield", "other": ["ItemLevel <= 32"], "type": "levelling rare normal"},
	"Ceremonial Kite Shield": {"base": "Ceremonial Kite Shield", "other": ["ItemLevel <= 39"], "type": "levelling rare normal"},
	"Etched Kite Shield": {"base": "Etched Kite Shield", "other": ["ItemLevel <= 45"], "type": "levelling rare normal"},
	"Steel Kite Shield": {"base": "Steel Kite Shield", "other": ["ItemLevel <= 51"], "type": "levelling rare normal"},
	"Laminated Kite Shield": {"base": "Laminated Kite Shield", "other": ["ItemLevel <= 55"], "type": "levelling rare normal"},
	"Angelic Kite Shield": {"base": "Angelic Kite Shield", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Branded Kite Shield": {"base": "Branded Kite Shield", "other": ["ItemLevel <= 64"], "type": "levelling rare normal"},
	"Champion Kite Shield": {"base": "Champion Kite Shield", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Mosaic Kite Shield": {"base": "Mosaic Kite Shield", "other": ["ItemLevel <= 70"], "type": "ignore"},
	"Archon Kite Shield": {"base": "Archon Kite Shield", "other": ["ItemLevel <= 73"], "type": "ignore"}
}
