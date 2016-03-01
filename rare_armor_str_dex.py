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
	"Scale Vest": {"base": "Scale Vest", "other": ["ItemLevel <= 9"], "type": "normal"},
	"Light Brigandine": {"base": "Light Brigandine", "other": ["ItemLevel <= 13"], "type": "normal"},
	"Scale Doublet": {"base": "Scale Doublet", "other": ["ItemLevel <= 22"], "type": "normal"},
	"Infantry Brigandine": {"base": "Infantry Brigandine", "other": ["ItemLevel <= 26"], "type": "normal"},
	"Full Scale Armour": {"base": "Full Scale Armour", "other": ["ItemLevel <= 33"], "type": "normal"},
	"Soldier's Brigandine": {"base": "Soldier's Brigandine", "other": ["ItemLevel <= 37"], "type": "normal"},
	"Field Lamellar": {"base": "Field Lamellar", "other": ["ItemLevel <= 40"], "type": "normal"},
	"Wyrmscale Doublet": {"base": "Wyrmscale Doublet", "other": ["ItemLevel <= 43"], "type": "normal"},
	"Hussar Brigandine": {"base": "Hussar Brigandine", "other": ["ItemLevel <= 47"], "type": "normal"},
	"Full Wyrmscale": {"base": "Full Wyrmscale", "other": ["ItemLevel <= 51"], "type": "normal"},
	"Commander's Brigandine": {"base": "Commander's Brigandine", "other": ["ItemLevel <= 55"], "type": "normal"},
	"Battle Lamellar": {"base": "Battle Lamellar", "other": ["ItemLevel <= 59"], "type": "normal"},
	"Dragonscale Doublet": {"base": "Dragonscale Doublet", "other": ["ItemLevel <= 62"], "type": "normal"},
	"Desert Brigandine": {"base": "Desert Brigandine", "other": ["ItemLevel <= 65"], "type": "normal"},
	"Full Dragonscale": {"base": "Full Dragonscale", "other": ["ItemLevel <= 68"], "type": "normal"},
	"General's Brigandine": {"base": "General's Brigandine", "other": ["ItemLevel <= 71"], "type": "normal"},
	"Triumphant Lamellar": {"base": "Triumphant Lamellar", "other": ["ItemLevel <= 74"], "type": "normal"},
	"Leatherscale Boots": {"base": "Leatherscale Boots", "other": ["ItemLevel <= 11"], "type": "normal"},
	"Ironscale Boots": {"base": "Ironscale Boots", "other": ["ItemLevel <= 23"], "type": "normal"},
	"Bronzescale Boots": {"base": "Bronzescale Boots", "other": ["ItemLevel <= 35"], "type": "normal"},
	"Steelscale Boots": {"base": "Steelscale Boots", "other": ["ItemLevel <= 41"], "type": "normal"},
	"Serpentscale Boots": {"base": "Serpentscale Boots", "other": ["ItemLevel <= 47"], "type": "normal"},
	"Wyrmscale Boots": {"base": "Wyrmscale Boots", "other": ["ItemLevel <= 56"], "type": "normal"},
	"Hydrascale Boots": {"base": "Hydrascale Boots", "other": ["ItemLevel <= 64"], "type": "normal"},
	"Dragonscale Boots": {"base": "Dragonscale Boots", "other": ["ItemLevel <= 70"], "type": "normal"},
	"Fishscale Gauntlets": {"base": "Fishscale Gauntlets", "other": ["ItemLevel <= 9"], "type": "normal"},
	"Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "other": ["ItemLevel <= 20"], "type": "normal"},
	"Bronzescale Gauntlets": {"base": "Bronzescale Gauntlets", "other": ["ItemLevel <= 32"], "type": "normal"},
	"Steelscale Gauntlets": {"base": "Steelscale Gauntlets", "other": ["ItemLevel <= 41"], "type": "normal"},
	"Serpentscale Gauntlets": {"base": "Serpentscale Gauntlets", "other": ["ItemLevel <= 48"], "type": "normal"},
	"Wyrmscale Gauntlets": {"base": "Wyrmscale Gauntlets", "other": ["ItemLevel <= 54"], "type": "normal"},
	"Hydrascale Gauntlets": {"base": "Hydrascale Gauntlets", "other": ["ItemLevel <= 64"], "type": "normal"},
	"Dragonscale Gauntlets": {"base": "Dragonscale Gauntlets", "other": ["ItemLevel <= 72"], "type": "normal"},
	"Battered Helm": {"base": "Battered Helm", "other": ["ItemLevel <= 9"], "type": "normal"},
	"Sallet": {"base": "Sallet", "other": ["ItemLevel <= 18"], "type": "normal"},
	"Visored Sallet": {"base": "Visored Sallet", "other": ["ItemLevel <= 28"], "type": "normal"},
	"Gilded Sallet": {"base": "Gilded Sallet", "other": ["ItemLevel <= 38"], "type": "normal"},
	"Secutor Helm": {"base": "Secutor Helm", "other": ["ItemLevel <= 41"], "type": "normal"},
	"Fencer Helm": {"base": "Fencer Helm", "other": ["ItemLevel <= 48"], "type": "normal"},
	"Lacquered Helmet": {"base": "Lacquered Helmet", "other": ["ItemLevel <= 56"], "type": "normal"},
	"Fluted Bascinet": {"base": "Fluted Bascinet", "other": ["ItemLevel <= 63"], "type": "normal"},
	"Pig-Faced Bascinet": {"base": "Pig-Faced Bascinet", "other": ["ItemLevel <= 68"], "type": "normal"},
	"Nightmare Bascinet": {"base": "Nightmare Bascinet", "other": ["ItemLevel <= 72"], "type": "normal"},
	"Rotted Round Shield": {"base": "Rotted Round Shield", "other": ["ItemLevel <= 10"], "type": "normal"},
	"Fir Round Shield": {"base": "Fir Round Shield", "other": ["ItemLevel <= 17"], "type": "normal"},
	"Studded Round Shield": {"base": "Studded Round Shield", "other": ["ItemLevel <= 25"], "type": "normal"},
	"Scarlet Round Shield": {"base": "Scarlet Round Shield", "other": ["ItemLevel <= 32"], "type": "normal"},
	"Splendid Round Shield": {"base": "Splendid Round Shield", "other": ["ItemLevel <= 38"], "type": "normal"},
	"Maple Round Shield": {"base": "Maple Round Shield", "other": ["ItemLevel <= 44"], "type": "normal"},
	"Spiked Round Shield": {"base": "Spiked Round Shield", "other": ["ItemLevel <= 50"], "type": "normal"},
	"Crimson Round Shield": {"base": "Crimson Round Shield", "other": ["ItemLevel <= 54"], "type": "normal"},
	"Baroque Round Shield": {"base": "Baroque Round Shield", "other": ["ItemLevel <= 59"], "type": "normal"},
	"Teak Round Shield": {"base": "Teak Round Shield", "other": ["ItemLevel <= 63"], "type": "normal"},
	"Spiny Round Shield": {"base": "Spiny Round Shield", "other": ["ItemLevel <= 67"], "type": "normal"},
	"Cardinal Round Shield": {"base": "Cardinal Round Shield", "other": ["ItemLevel <= 71"], "type": "normal"},
	"Elegant Round Shield": {"base": "Elegant Round Shield", "other": ["ItemLevel <= 75"], "type": "normal"}
}
