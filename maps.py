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

desc = "maps"

# Base type : settings pair
items = {
	"0 Crypt Map": {"base": "Crypt Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Desert Map": {"base": "Desert Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Dunes Map": {"base": "Dunes Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Dungeon Map": {"base": "Dungeon Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Grotto Map": {"base": "Grotto Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Pit Map": {"base": "Pit Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Tropical Island Map": {"base": "Tropical Island Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},

	"0 Arcade Map": {"base": "Arcade Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Cemetery Map": {"base": "Cemetery Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Channel Map": {"base": "Channel Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Mountain Ledge Map": {"base": "Mountain Ledge Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Sewer Map": {"base": "Sewer Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Thicket Map": {"base": "Thicket Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Wharf Map": {"base": "Wharf Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},

	"0 Ghetto Map": {"base": "Ghetto Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Mud Geyser Map": {"base": "Mud Geyser Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Museum Map": {"base": "Museum Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Quarry Map": {"base": "Quarry Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Reef Map": {"base": "Reef Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Spider Lair Map": {"base": "Spider Lair Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Vaal Pyramid Map": {"base": "Vaal Pyramid Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},

	"0 Arena Map": {"base": "Arena Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Overgrown Shrine Map": {"base": "Overgrown Shrine Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Promenade Map": {"base": "Promenade Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Phantasmagoria Map": {"base": "Phantasmagoria Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Shore Map": {"base": "Shore Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Spider Forest Map": {"base": "Spider Forest Ma", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Tunnel Map": {"base": "Tunnel Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},

	"0 Bog Map": {"base": "Bog Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Coves Map": {"base": "Coves Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Graveyard Map": {"base": "Graveyard Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Pier Map": {"base": "Pier Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Underground Sea Map": {"base": "Underground Sea Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Villa Map": {"base": "Villa Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},

	"0 Arachnid Nest Map": {"base": "Arachnid Nest Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Catacomb Map": {"base": "Catacomb Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Colonnade Map": {"base": "Colonnade Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Dry Woods Map": {"base": "Dry Woods Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Strand Map": {"base": "Strand Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Temple Map": {"base": "Temple Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},

	"0 Jungle Valley Map": {"base": "Jungle Valley Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Terrace Map": {"base": "Terrace Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Abandoned Cavern Map": {"base": "Abandoned Cavern Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Torture Chamber Map": {"base": "Torture Chamber Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Waste Pool Map": {"base": "Waste Pool Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},

	"0 Canyon Map": {"base": "Canyon Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Cells Map": {"base": "Cells Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Dark Forest Map": {"base": "Dark Forest Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Dry Peninsula Map": {"base": "Dry Peninsula Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Orchard Map": {"base": "Orchard Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},

	"0 Arid Lake Map": {"base": "Arid Lake Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Gorge Map": {"base": "Gorge Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Malformation Map": {"base": "Malformation Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Residence Map": {"base": "Residence Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Underground River Map": {"base": "Underground River Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},

	"0 Bazaar Map": {"base": "Bazaar Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Chateau Map": {"base": "Chateau Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Necropolis Map": {"base": "Necropolis Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Plateau Map": {"base": "Plateau Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Volcano Map": {"base": "Volcano Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},

	"0 Academy Map": {"base": "Academy Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Crematorium Map": {"base": "Crematorium Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Precinct Map": {"base": "Precinct Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Springs Map": {"base": "Springs Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},

	"0 Arsenal Map": {"base": "Arsenal Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Overgrown Ruin Map": {"base": "Overgrown Ruin Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Shipyard Map": {"base": "Shipyard Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Village Ruin Map": {"base": "Village Ruin Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},

	"0 Courtyard Map": {"base": "Courtyard Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Excavation Map": {"base": "Excavation Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Wasteland Map": {"base": "Wasteland Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Waterways Map": {"base": "Waterways Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},

	"0 Conservatory Map": {"base": "Conservatory Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Palace Map": {"base": "Palace Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Shrine Map": {"base": "Shrine Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Vaal Temple Map": {"base": "Vaal Temple Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},

	"0 Abyss Map": {"base": "Abyss Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Colosseum Map": {"base": "Colosseum Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},
	"0 Core Map": {"base": "Core Map", "class": "Maps", "other": ["ItemLevel <= 67"], "type": "ignore"},


    "71 Maps >= 79": {"class": "Maps", "other": ["DropLevel >= 79"], "type": "map red"},
    "72 Maps <= 73": {"class": "Maps", "other": ["DropLevel <= 73"], "type": "map white"},
    "73 Other maps": {"class": "Maps", "type": "map yellow"},
    "74 Map Fragments": {"class": "Map Fragments", "type": "map white"},
}