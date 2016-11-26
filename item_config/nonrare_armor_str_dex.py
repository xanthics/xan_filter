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
	"Scale Vest": {"base": "Scale Vest", "other": ["Rarity <= Magic", "ItemLevel <= 9"], "type": "leveling low"},
	"Light Brigandine": {"base": "Light Brigandine", "other": ["Rarity <= Magic", "ItemLevel <= 13"], "type": "leveling low"},
	"Scale Doublet": {"base": "Scale Doublet", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "leveling low"},
	"Infantry Brigandine": {"base": "Infantry Brigandine", "other": ["Rarity <= Magic", "ItemLevel <= 26"], "type": "leveling low"},
	"Full Scale Armour": {"base": "Full Scale Armour", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "leveling low"},
	"Soldier's Brigandine": {"base": "Soldier's Brigandine", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "leveling low"},
	"Field Lamellar": {"base": "Field Lamellar", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Wyrmscale Doublet": {"base": "Wyrmscale Doublet", "other": ["Rarity <= Magic", "ItemLevel <= 43"], "type": "leveling low"},
	"Hussar Brigandine": {"base": "Hussar Brigandine", "other": ["Rarity <= Magic", "ItemLevel <= 47"], "type": "leveling low"},
	"Full Wyrmscale": {"base": "Full Wyrmscale", "other": ["Rarity <= Magic", "ItemLevel <= 51"], "type": "ignore"},
	"Commander's Brigandine": {"base": "Commander's Brigandine", "other": ["Rarity <= Magic", "ItemLevel <= 55"], "type": "ignore"},
	"Battle Lamellar": {"base": "Battle Lamellar", "other": ["Rarity <= Magic", "ItemLevel <= 59"], "type": "ignore"},
	"Dragonscale Doublet": {"base": "Dragonscale Doublet", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "ignore"},
	"Desert Brigandine": {"base": "Desert Brigandine", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "ignore"},
	"Full Dragonscale": {"base": "Full Dragonscale", "other": ["Rarity <= Magic", "ItemLevel <= 68"], "type": "ignore"},
	"General's Brigandine": {"base": "General's Brigandine", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "ignore"},
	"Triumphant Lamellar": {"base": "Triumphant Lamellar", "other": ["Rarity <= Magic", "ItemLevel <= 74"], "type": "ignore"},
	"Leatherscale Boots": {"base": "Leatherscale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 11"], "type": "leveling low"},
	"Ironscale Boots": {"base": "Ironscale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 23"], "type": "leveling low"},
	"Bronzescale Boots": {"base": "Bronzescale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 35"], "type": "leveling low"},
	"Steelscale Boots": {"base": "Steelscale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "leveling low"},
	"Serpentscale Boots": {"base": "Serpentscale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 47"], "type": "leveling low"},
	"Wyrmscale Boots": {"base": "Wyrmscale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 56"], "type": "ignore"},
	"Hydrascale Boots": {"base": "Hydrascale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "ignore"},
	"Dragonscale Boots": {"base": "Dragonscale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "ignore"},
	"Fishscale Gauntlets": {"base": "Fishscale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 9"], "type": "leveling low"},
	"Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 20"], "type": "leveling low"},
	"Bronzescale Gauntlets": {"base": "Bronzescale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 32"], "type": "leveling low"},
	"Steelscale Gauntlets": {"base": "Steelscale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "leveling low"},
	"Serpentscale Gauntlets": {"base": "Serpentscale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 48"], "type": "leveling low"},
	"Wyrmscale Gauntlets": {"base": "Wyrmscale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "ignore"},
	"Hydrascale Gauntlets": {"base": "Hydrascale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "ignore"},
	"Dragonscale Gauntlets": {"base": "Dragonscale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 72"], "type": "ignore"},
	"Battered Helm": {"base": "Battered Helm", "other": ["Rarity <= Magic", "ItemLevel <= 9"], "type": "leveling low"},
	"Sallet": {"base": "Sallet", "other": ["Rarity <= Magic", "ItemLevel <= 18"], "type": "leveling low"},
	"Visored Sallet": {"base": "Visored Sallet", "other": ["Rarity <= Magic", "ItemLevel <= 28"], "type": "leveling low"},
	"Gilded Sallet": {"base": "Gilded Sallet", "other": ["Rarity <= Magic", "ItemLevel <= 38"], "type": "leveling low"},
	"Secutor Helm": {"base": "Secutor Helm", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "leveling low"},
	"Fencer Helm": {"base": "Fencer Helm", "other": ["Rarity <= Magic", "ItemLevel <= 48"], "type": "leveling low"},
	"Lacquered Helmet": {"base": "Lacquered Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 56"], "type": "ignore"},
	"Fluted Bascinet": {"base": "Fluted Bascinet", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Pig-Faced Bascinet": {"base": "Pig-Faced Bascinet", "other": ["Rarity <= Magic", "ItemLevel <= 68"], "type": "ignore"},
	"Nightmare Bascinet": {"base": "Nightmare Bascinet", "other": ["Rarity <= Magic", "ItemLevel <= 72"], "type": "ignore"},
	"Rotted Round Shield": {"base": "Rotted Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 10"], "type": "leveling low"},
	"Fir Round Shield": {"base": "Fir Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "leveling low"},
	"Studded Round Shield": {"base": "Studded Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 25"], "type": "leveling low"},
	"Scarlet Round Shield": {"base": "Scarlet Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 32"], "type": "leveling low"},
	"Splendid Round Shield": {"base": "Splendid Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 38"], "type": "leveling low"},
	"Maple Round Shield": {"base": "Maple Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 44"], "type": "leveling low"},
	"Spiked Round Shield": {"base": "Spiked Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "leveling low"},
	"Crimson Round Shield": {"base": "Crimson Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "ignore"},
	"Baroque Round Shield": {"base": "Baroque Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 59"], "type": "ignore"},
	"Teak Round Shield": {"base": "Teak Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Spiny Round Shield": {"base": "Spiny Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Cardinal Round Shield": {"base": "Cardinal Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "ignore"},
	"Elegant Round Shield": {"base": "Elegant Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"}
}
