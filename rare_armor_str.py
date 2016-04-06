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

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Plate Vest": {"base": "Plate Vest", "other": ["ItemLevel <= 6"], "type": "levelling rare normal"},
	"Chestplate": {"base": "Chestplate", "other": ["ItemLevel <= 11"], "type": "levelling rare normal"},
	"Copper Plate": {"base": "Copper Plate", "other": ["ItemLevel <= 22"], "type": "levelling rare normal"},
	"War Plate": {"base": "War Plate", "other": ["ItemLevel <= 26"], "type": "levelling rare normal"},
	"Full Plate": {"base": "Full Plate", "other": ["ItemLevel <= 33"], "type": "levelling rare normal"},
	"Arena Plate": {"base": "Arena Plate", "other": ["ItemLevel <= 37"], "type": "levelling rare normal"},
	"Lordly Plate": {"base": "Lordly Plate", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Bronze Plate": {"base": "Bronze Plate", "other": ["ItemLevel <= 42"], "type": "levelling rare normal"},
	"Battle Plate": {"base": "Battle Plate", "other": ["ItemLevel <= 46"], "type": "levelling rare normal"},
	"Sun Plate": {"base": "Sun Plate", "other": ["ItemLevel <= 50"], "type": "levelling rare normal"},
	"Colosseum Plate": {"base": "Colosseum Plate", "other": ["ItemLevel <= 54"], "type": "levelling rare normal"},
	"Majestic Plate": {"base": "Majestic Plate", "other": ["ItemLevel <= 58"], "type": "levelling rare normal"},
	"Golden Plate": {"base": "Golden Plate", "other": ["ItemLevel <= 61"], "type": "levelling rare normal"},
	"Crusader Plate": {"base": "Crusader Plate", "other": ["ItemLevel <= 64"], "type": "levelling rare normal"},
	"Astral Plate": {"base": "Astral Plate", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Gladiator Plate": {"base": "Gladiator Plate", "other": ["ItemLevel <= 70"], "type": "ignore"},
	"Glorious Plate": {"base": "Glorious Plate", "other": ["ItemLevel <= 73"], "type": "ignore"},
	"Iron Greaves": {"base": "Iron Greaves", "other": ["ItemLevel <= 6"], "type": "levelling rare normal"},
	"Steel Greaves": {"base": "Steel Greaves", "other": ["ItemLevel <= 14"], "type": "levelling rare normal"},
	"Plated Greaves": {"base": "Plated Greaves", "other": ["ItemLevel <= 28"], "type": "levelling rare normal"},
	"Reinforced Greaves": {"base": "Reinforced Greaves", "other": ["ItemLevel <= 38"], "type": "levelling rare normal"},
	"Antique Greaves": {"base": "Antique Greaves", "other": ["ItemLevel <= 42"], "type": "levelling rare normal"},
	"Ancient Greaves": {"base": "Ancient Greaves", "other": ["ItemLevel <= 51"], "type": "levelling rare normal"},
	"Goliath Greaves": {"base": "Goliath Greaves", "other": ["ItemLevel <= 59"], "type": "levelling rare normal"},
	"Vaal Greaves": {"base": "Vaal Greaves", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Titan Greaves": {"base": "Titan Greaves", "other": ["ItemLevel <= 73"], "type": "ignore"},
	"Iron Gauntlets": {"base": "Iron Gauntlets", "other": ["ItemLevel <= 6"], "type": "levelling rare normal"},
	"Plated Gauntlets": {"base": "Plated Gauntlets", "other": ["ItemLevel <= 16"], "type": "levelling rare normal"},
	"Bronze Gauntlets": {"base": "Bronze Gauntlets", "other": ["ItemLevel <= 28"], "type": "levelling rare normal"},
	"Steel Gauntlets": {"base": "Steel Gauntlets", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Antique Gauntlets": {"base": "Antique Gauntlets", "other": ["ItemLevel <= 44"], "type": "levelling rare normal"},
	"Ancient Gauntlets": {"base": "Ancient Gauntlets", "other": ["ItemLevel <= 52"], "type": "levelling rare normal"},
	"Goliath Gauntlets": {"base": "Goliath Gauntlets", "other": ["ItemLevel <= 58"], "type": "levelling rare normal"},
	"Vaal Gauntlets": {"base": "Vaal Gauntlets", "other": ["ItemLevel <= 68"], "type": "ignore"},
	"Titan Gauntlets": {"base": "Titan Gauntlets", "other": ["ItemLevel <= 74"], "type": "ignore"},
	"Iron Hat": {"base": "Iron Hat", "other": ["ItemLevel <= 6"], "type": "levelling rare normal"},
	"Cone Helmet": {"base": "Cone Helmet", "other": ["ItemLevel <= 12"], "type": "levelling rare normal"},
	"Barbute Helmet": {"base": "Barbute Helmet", "other": ["ItemLevel <= 23"], "type": "levelling rare normal"},
	"Close Helmet": {"base": "Close Helmet", "other": ["ItemLevel <= 31"], "type": "levelling rare normal"},
	"Gladiator Helmet": {"base": "Gladiator Helmet", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Reaver Helmet": {"base": "Reaver Helmet", "other": ["ItemLevel <= 45"], "type": "levelling rare normal"},
	"Siege Helmet": {"base": "Siege Helmet", "other": ["ItemLevel <= 53"], "type": "levelling rare normal"},
	"Samite Helmet": {"base": "Samite Helmet", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "other": ["ItemLevel <= 65"], "type": "levelling rare normal"},
	"Royal Burgonet": {"base": "Royal Burgonet", "other": ["ItemLevel <= 70"], "type": "ignore"},
	"Eternal Burgonet": {"base": "Eternal Burgonet", "other": ["ItemLevel <= 74"], "type": "ignore"},
	"Splintered Tower Shield": {"base": "Splintered Tower Shield", "other": ["ItemLevel <= 6"], "type": "levelling rare normal"},
	"Corroded Tower Shield": {"base": "Corroded Tower Shield", "other": ["ItemLevel <= 10"], "type": "levelling rare normal"},
	"Rawhide Tower Shield": {"base": "Rawhide Tower Shield", "other": ["ItemLevel <= 16"], "type": "levelling rare normal"},
	"Cedar Tower Shield": {"base": "Cedar Tower Shield", "other": ["ItemLevel <= 22"], "type": "levelling rare normal"},
	"Copper Tower Shield": {"base": "Copper Tower Shield", "other": ["ItemLevel <= 29"], "type": "levelling rare normal"},
	"Reinforced Tower Shield": {"base": "Reinforced Tower Shield", "other": ["ItemLevel <= 35"], "type": "levelling rare normal"},
	"Painted Tower Shield": {"base": "Painted Tower Shield", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Buckskin Tower Shield": {"base": "Buckskin Tower Shield", "other": ["ItemLevel <= 44"], "type": "levelling rare normal"},
	"Mahogany Tower Shield": {"base": "Mahogany Tower Shield", "other": ["ItemLevel <= 48"], "type": "levelling rare normal"},
	"Bronze Tower Shield": {"base": "Bronze Tower Shield", "other": ["ItemLevel <= 52"], "type": "levelling rare normal"},
	"Girded Tower Shield": {"base": "Girded Tower Shield", "other": ["ItemLevel <= 56"], "type": "levelling rare normal"},
	"Crested Tower Shield": {"base": "Crested Tower Shield", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Shagreen Tower Shield": {"base": "Shagreen Tower Shield", "other": ["ItemLevel <= 63"], "type": "levelling rare normal"},
	"Ebony Tower Shield": {"base": "Ebony Tower Shield", "other": ["ItemLevel <= 66"], "type": "levelling rare normal"},
	"Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "other": ["ItemLevel <= 69"], "type": "ignore"},
	"Colossal Tower Shield": {"base": "Colossal Tower Shield", "other": ["ItemLevel <= 72"], "type": "ignore"},
	"Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "other": ["ItemLevel <= 75"], "type": "ignore"}
}
