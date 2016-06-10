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
	"Plate Vest": {"base": "Plate Vest", "other": ["Rarity <= Magic", "ItemLevel <= 6"], "type": "leveling low"},
	"Chestplate": {"base": "Chestplate", "other": ["Rarity <= Magic", "ItemLevel <= 11"], "type": "leveling low"},
	"Copper Plate": {"base": "Copper Plate", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "leveling low"},
	"War Plate": {"base": "War Plate", "other": ["Rarity <= Magic", "ItemLevel <= 26"], "type": "leveling low"},
	"Full Plate": {"base": "Full Plate", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "leveling low"},
	"Arena Plate": {"base": "Arena Plate", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "leveling low"},
	"Lordly Plate": {"base": "Lordly Plate", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Bronze Plate": {"base": "Bronze Plate", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "leveling low"},
	"Battle Plate": {"base": "Battle Plate", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "leveling low"},
	"Sun Plate": {"base": "Sun Plate", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "leveling low"},
	"Colosseum Plate": {"base": "Colosseum Plate", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "ignore"},
	"Majestic Plate": {"base": "Majestic Plate", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "ignore"},
	"Golden Plate": {"base": "Golden Plate", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "ignore"},
	"Crusader Plate": {"base": "Crusader Plate", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "ignore"},
	"Astral Plate": {"base": "Astral Plate", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Gladiator Plate": {"base": "Gladiator Plate", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "ignore"},
	"Glorious Plate": {"base": "Glorious Plate", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"},
	"Iron Greaves": {"base": "Iron Greaves", "other": ["Rarity <= Magic", "ItemLevel <= 6"], "type": "leveling low"},
	"Steel Greaves": {"base": "Steel Greaves", "other": ["Rarity <= Magic", "ItemLevel <= 14"], "type": "leveling low"},
	"Plated Greaves": {"base": "Plated Greaves", "other": ["Rarity <= Magic", "ItemLevel <= 28"], "type": "leveling low"},
	"Reinforced Greaves": {"base": "Reinforced Greaves", "other": ["Rarity <= Magic", "ItemLevel <= 38"], "type": "leveling low"},
	"Antique Greaves": {"base": "Antique Greaves", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "leveling low"},
	"Ancient Greaves": {"base": "Ancient Greaves", "other": ["Rarity <= Magic", "ItemLevel <= 51"], "type": "ignore"},
	"Goliath Greaves": {"base": "Goliath Greaves", "other": ["Rarity <= Magic", "ItemLevel <= 59"], "type": "ignore"},
	"Vaal Greaves": {"base": "Vaal Greaves", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Titan Greaves": {"base": "Titan Greaves", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"},
	"Iron Gauntlets": {"base": "Iron Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 6"], "type": "leveling low"},
	"Plated Gauntlets": {"base": "Plated Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 16"], "type": "leveling low"},
	"Bronze Gauntlets": {"base": "Bronze Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 28"], "type": "leveling low"},
	"Steel Gauntlets": {"base": "Steel Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Antique Gauntlets": {"base": "Antique Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 44"], "type": "leveling low"},
	"Ancient Gauntlets": {"base": "Ancient Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 52"], "type": "ignore"},
	"Goliath Gauntlets": {"base": "Goliath Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "ignore"},
	"Vaal Gauntlets": {"base": "Vaal Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 68"], "type": "ignore"},
	"Titan Gauntlets": {"base": "Titan Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 74"], "type": "ignore"},
	"Iron Hat": {"base": "Iron Hat", "other": ["Rarity <= Magic", "ItemLevel <= 6"], "type": "leveling low"},
	"Cone Helmet": {"base": "Cone Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 12"], "type": "leveling low"},
	"Barbute Helmet": {"base": "Barbute Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 23"], "type": "leveling low"},
	"Close Helmet": {"base": "Close Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 31"], "type": "leveling low"},
	"Gladiator Helmet": {"base": "Gladiator Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Reaver Helmet": {"base": "Reaver Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 45"], "type": "leveling low"},
	"Siege Helmet": {"base": "Siege Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 53"], "type": "ignore"},
	"Samite Helmet": {"base": "Samite Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "ignore"},
	"Royal Burgonet": {"base": "Royal Burgonet", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "ignore"},
	"Eternal Burgonet": {"base": "Eternal Burgonet", "other": ["Rarity <= Magic", "ItemLevel <= 74"], "type": "ignore"},
	"Splintered Tower Shield": {"base": "Splintered Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 6"], "type": "leveling low"},
	"Corroded Tower Shield": {"base": "Corroded Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 10"], "type": "leveling low"},
	"Rawhide Tower Shield": {"base": "Rawhide Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 16"], "type": "leveling low"},
	"Cedar Tower Shield": {"base": "Cedar Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "leveling low"},
	"Copper Tower Shield": {"base": "Copper Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 29"], "type": "leveling low"},
	"Reinforced Tower Shield": {"base": "Reinforced Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 35"], "type": "leveling low"},
	"Painted Tower Shield": {"base": "Painted Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Buckskin Tower Shield": {"base": "Buckskin Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 44"], "type": "leveling low"},
	"Mahogany Tower Shield": {"base": "Mahogany Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 48"], "type": "leveling low"},
	"Bronze Tower Shield": {"base": "Bronze Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 52"], "type": "ignore"},
	"Girded Tower Shield": {"base": "Girded Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 56"], "type": "ignore"},
	"Crested Tower Shield": {"base": "Crested Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Shagreen Tower Shield": {"base": "Shagreen Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Ebony Tower Shield": {"base": "Ebony Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 66"], "type": "ignore"},
	"Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "ignore"},
	"Colossal Tower Shield": {"base": "Colossal Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 72"], "type": "ignore"},
	"Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"}
}
