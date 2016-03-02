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
	"Scale Vest": {"base": "Scale Vest", "other": ["Rarity <= Magic", "ItemLevel <= 9"], "type": "normal"},
	"Light Brigandine": {"base": "Light Brigandine", "other": ["Rarity <= Magic", "ItemLevel <= 13"], "type": "normal"},
	"Scale Doublet": {"base": "Scale Doublet", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "normal"},
	"Infantry Brigandine": {"base": "Infantry Brigandine", "other": ["Rarity <= Magic", "ItemLevel <= 26"], "type": "normal"},
	"Full Scale Armour": {"base": "Full Scale Armour", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "normal"},
	"Soldier's Brigandine": {"base": "Soldier's Brigandine", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "normal"},
	"Field Lamellar": {"base": "Field Lamellar", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "normal"},
	"Wyrmscale Doublet": {"base": "Wyrmscale Doublet", "other": ["Rarity <= Magic", "ItemLevel <= 43"], "type": "normal"},
	"Hussar Brigandine": {"base": "Hussar Brigandine", "other": ["Rarity <= Magic", "ItemLevel <= 47"], "type": "normal"},
	"Full Wyrmscale": {"base": "Full Wyrmscale", "other": ["Rarity <= Magic", "ItemLevel <= 51"], "type": "ignore"},
	"Commander's Brigandine": {"base": "Commander's Brigandine", "other": ["Rarity <= Magic", "ItemLevel <= 55"], "type": "ignore"},
	"Battle Lamellar": {"base": "Battle Lamellar", "other": ["Rarity <= Magic", "ItemLevel <= 59"], "type": "ignore"},
	"Dragonscale Doublet": {"base": "Dragonscale Doublet", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "ignore"},
	"Desert Brigandine": {"base": "Desert Brigandine", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "ignore"},
	"Full Dragonscale": {"base": "Full Dragonscale", "other": ["Rarity <= Magic", "ItemLevel <= 68"], "type": "ignore"},
	"General's Brigandine": {"base": "General's Brigandine", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "ignore"},
	"Triumphant Lamellar": {"base": "Triumphant Lamellar", "other": ["Rarity <= Magic", "ItemLevel <= 74"], "type": "ignore"},
	"Leatherscale Boots": {"base": "Leatherscale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 11"], "type": "normal"},
	"Ironscale Boots": {"base": "Ironscale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 23"], "type": "normal"},
	"Bronzescale Boots": {"base": "Bronzescale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 35"], "type": "normal"},
	"Steelscale Boots": {"base": "Steelscale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "normal"},
	"Serpentscale Boots": {"base": "Serpentscale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 47"], "type": "normal"},
	"Wyrmscale Boots": {"base": "Wyrmscale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 56"], "type": "ignore"},
	"Hydrascale Boots": {"base": "Hydrascale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "ignore"},
	"Dragonscale Boots": {"base": "Dragonscale Boots", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "ignore"},
	"Fishscale Gauntlets": {"base": "Fishscale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 9"], "type": "normal"},
	"Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 20"], "type": "normal"},
	"Bronzescale Gauntlets": {"base": "Bronzescale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 32"], "type": "normal"},
	"Steelscale Gauntlets": {"base": "Steelscale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "normal"},
	"Serpentscale Gauntlets": {"base": "Serpentscale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 48"], "type": "normal"},
	"Wyrmscale Gauntlets": {"base": "Wyrmscale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "ignore"},
	"Hydrascale Gauntlets": {"base": "Hydrascale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "ignore"},
	"Dragonscale Gauntlets": {"base": "Dragonscale Gauntlets", "other": ["Rarity <= Magic", "ItemLevel <= 72"], "type": "ignore"},
	"Battered Helm": {"base": "Battered Helm", "other": ["Rarity <= Magic", "ItemLevel <= 9"], "type": "normal"},
	"Sallet": {"base": "Sallet", "other": ["Rarity <= Magic", "ItemLevel <= 18"], "type": "normal"},
	"Visored Sallet": {"base": "Visored Sallet", "other": ["Rarity <= Magic", "ItemLevel <= 28"], "type": "normal"},
	"Gilded Sallet": {"base": "Gilded Sallet", "other": ["Rarity <= Magic", "ItemLevel <= 38"], "type": "normal"},
	"Secutor Helm": {"base": "Secutor Helm", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "normal"},
	"Fencer Helm": {"base": "Fencer Helm", "other": ["Rarity <= Magic", "ItemLevel <= 48"], "type": "normal"},
	"Lacquered Helmet": {"base": "Lacquered Helmet", "other": ["Rarity <= Magic", "ItemLevel <= 56"], "type": "ignore"},
	"Fluted Bascinet": {"base": "Fluted Bascinet", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Pig-Faced Bascinet": {"base": "Pig-Faced Bascinet", "other": ["Rarity <= Magic", "ItemLevel <= 68"], "type": "ignore"},
	"Nightmare Bascinet": {"base": "Nightmare Bascinet", "other": ["Rarity <= Magic", "ItemLevel <= 72"], "type": "ignore"},
	"Rotted Round Shield": {"base": "Rotted Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 10"], "type": "normal"},
	"Fir Round Shield": {"base": "Fir Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "normal"},
	"Studded Round Shield": {"base": "Studded Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 25"], "type": "normal"},
	"Scarlet Round Shield": {"base": "Scarlet Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 32"], "type": "normal"},
	"Splendid Round Shield": {"base": "Splendid Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 38"], "type": "normal"},
	"Maple Round Shield": {"base": "Maple Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 44"], "type": "normal"},
	"Spiked Round Shield": {"base": "Spiked Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "normal"},
	"Crimson Round Shield": {"base": "Crimson Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "ignore"},
	"Baroque Round Shield": {"base": "Baroque Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 59"], "type": "ignore"},
	"Teak Round Shield": {"base": "Teak Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Spiny Round Shield": {"base": "Spiny Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Cardinal Round Shield": {"base": "Cardinal Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "ignore"},
	"Elegant Round Shield": {"base": "Elegant Round Shield", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"}
}
