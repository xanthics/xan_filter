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
	# Tier 1
	"1 Arcade Map": {"base": "Arcade Map", "class": "Maps", "other": ["ItemLevel <= 70"], "type": "map white good"},
	"1 Crystal Ore Map": {"base": "Crystal Ore Map", "class": "Maps", "other": ["ItemLevel <= 70"], "type": "map white good"},
	"1 Desert Map": {"base": "Desert Map", "class": "Maps", "other": ["ItemLevel <= 70"], "type": "map white good"},
	"1 Jungle Valley Map": {"base": "Jungle Valley Map", "class": "Maps", "other": ["ItemLevel <= 70"], "type": "map white good"},

	# Tier 2
	"1 Beach Map": {"base": "Beach Map", "class": "Maps", "other": ["ItemLevel <= 71", "DropLevel 69"], "type": "map white good"},
	"1 Factory Map": {"base": "Factory Map", "class": "Maps", "other": ["ItemLevel <= 71", "DropLevel 69"], "type": "map white good"},
	"1 Ghetto Map": {"base": "Ghetto Map", "class": "Maps", "other": ["ItemLevel <= 71", "DropLevel 69"], "type": "map white good"},
	"1 Oasis Map": {"base": "Oasis Map", "class": "Maps", "other": ["ItemLevel <= 71", "DropLevel 69"], "type": "map white good"},

	# Tier 3
	"1 Arid Lake Map": {"base": "Arid Lake Map", "class": "Maps", "other": ["ItemLevel <= 72", "DropLevel 70"], "type": "map white good"},
	"1 Cavern Map": {"base": "Cavern Map", "class": "Maps", "other": ["ItemLevel <= 72", "DropLevel 70"], "type": "map white good"},
	"1 Channel Map": {"base": "Channel Map", "class": "Maps", "other": ["ItemLevel <= 72", "DropLevel 70"], "type": "map white good"},
	"1 Grotto Map": {"base": "Grotto Map", "class": "Maps", "other": ["ItemLevel <= 72", "DropLevel 70"], "type": "map white good"},
	"1 Marshes Map": {"base": "Marshes Map", "class": "Maps", "other": ["ItemLevel <= 72", "DropLevel 70"], "type": "map white good"},
	"1 Sewer Map": {"base": "Sewer Map", "class": "Maps", "other": ["ItemLevel <= 72", "DropLevel 70"], "type": "map white good"},
	"1 Vaal Pyramid Map": {"base": "Vaal Pyramid Map", "class": "Maps", "other": ["ItemLevel <= 72", "DropLevel 70"], "type": "map white good"},

	# Tier 4
	"1 Academy Map": {"base": "Academy Map", "class": "Maps", "other": ["ItemLevel <= 73", "DropLevel 71"], "type": "map white good"},
	"1 Acid Lakes Map": {"base": "Acid Lakes Map", "class": "Maps", "other": ["ItemLevel <= 73", "DropLevel 71"], "type": "map white good"},
	"1 Dungeon Map": {"base": "Dungeon Map", "class": "Maps", "other": ["ItemLevel <= 73", "DropLevel 71"], "type": "map white good"},
	"1 Graveyard Map": {"base": "Graveyard Map", "class": "Maps", "other": ["ItemLevel <= 73", "DropLevel 71"], "type": "map white good"},
	"1 Phantasmagoria Map": {"base": "Phantasmagoria Map", "class": "Maps", "other": ["ItemLevel <= 73", "DropLevel 71"], "type": "map white good"},
	"1 Villa Map": {"base": "Villa Map", "class": "Maps", "other": ["ItemLevel <= 73", "DropLevel 71"], "type": "map white good"},
	"1 Waste Pool Map": {"base": "Waste Pool Map", "class": "Maps", "other": ["ItemLevel <= 73", "DropLevel 71"], "type": "map white good"},

	# Tier 5
	"1 Burial Chambers Map": {"base": "Burial Chambers Map", "class": "Maps", "other": ["ItemLevel <= 74", "DropLevel 72"], "type": "map white good"},
	"1 Peninsula Map": {"base": "Peninsula Map", "class": "Maps", "other": ["ItemLevel <= 74", "DropLevel 72"], "type": "map white good"},
	"1 Dunes Map": {"base": "Dunes Map", "class": "Maps", "other": ["ItemLevel <= 74", "DropLevel 72"], "type": "map white good"},
	"1 Mesa Map": {"base": "Mesa Map", "class": "Maps", "other": ["ItemLevel <= 74", "DropLevel 72"], "type": "map white good"},
	"1 Pit Map": {"base": "Pit Map", "class": "Maps", "other": ["ItemLevel <= 74", "DropLevel 72"], "type": "map white good"},
	"1 Primordial Pool Map": {"base": "Primordial Pool Map", "class": "Maps", "other": ["ItemLevel <= 74", "DropLevel 72"], "type": "map white good"},
	"1 Spider Lair Map": {"base": "Spider Lair Map", "class": "Maps", "other": ["ItemLevel <= 74", "DropLevel 72"], "type": "map white good"},
	"1 Tower Map": {"base": "Tower Map", "class": "Maps", "other": ["ItemLevel <= 74", "DropLevel 72"], "type": "map white good"},

	# Tier 6
	"0 Shaped Arcade Map": {"base": "Shaped Arcade Map", "class": "Maps", "other": ["ItemLevel <= 75", "DropLevel 73"], "type": "map yellow good"},
	"0 Shaped Crystal Ore Map": {"base": "Shaped Crystal Ore Map", "class": "Maps", "other": ["ItemLevel <= 75", "DropLevel 73"], "type": "map yellow good"},
	"0 Shaped Desert Map": {"base": "Shaped Desert Map", "class": "Maps", "other": ["ItemLevel <= 75", "DropLevel 73"], "type": "map yellow good"},
	"0 Shaped Jungle Valley Map": {"base": "Shaped Jungle Valley Map", "class": "Maps", "other": ["ItemLevel <= 75", "DropLevel 73"], "type": "map yellow good"},
	"1 Canyon Map": {"base": "Canyon Map", "class": "Maps", "other": ["ItemLevel <= 75", "DropLevel 73"], "type": "map yellow good"},
	"1 Quarry Map": {"base": "Quarry Map", "class": "Maps", "other": ["ItemLevel <= 75", "DropLevel 73"], "type": "map yellow good"},
	"1 Racecourse Map": {"base": "Racecourse Map", "class": "Maps", "other": ["ItemLevel <= 75", "DropLevel 73"], "type": "map yellow good"},
	"1 Ramparts Map": {"base": "Ramparts Map", "class": "Maps", "other": ["ItemLevel <= 75", "DropLevel 73"], "type": "map yellow good"},
	"1 Spider Forest Map": {"base": "Spider Forest Map", "class": "Maps", "other": ["ItemLevel <= 75", "DropLevel 73"], "type": "map yellow good"},
	"1 Strand Map": {"base": "Strand Map", "class": "Maps", "other": ["ItemLevel <= 75", "DropLevel 73"], "type": "map yellow good"},
	"1 Thicket Map": {"base": "Thicket Map", "class": "Maps", "other": ["ItemLevel <= 75", "DropLevel 73"], "type": "map yellow good"},
	"1 Vaal City Map": {"base": "Vaal City Map", "class": "Maps", "other": ["ItemLevel <= 75", "DropLevel 73"], "type": "map yellow good"},
	"1 Wharf Map": {"base": "Wharf Map", "class": "Maps", "other": ["ItemLevel <= 75", "DropLevel 73"], "type": "map yellow good"},

	# Tier 7
	"0 Shaped Beach Map": {"base": "Shaped Beach Map", "class": "Maps", "other": ["ItemLevel <= 76", "DropLevel 74"], "type": "map yellow good"},
	"0 Shaped Factory Map": {"base": "Shaped Factory Map", "class": "Maps", "other": ["ItemLevel <= 76", "DropLevel 74"], "type": "map yellow good"},
	"0 Shaped Ghetto Map": {"base": "Shaped Ghetto Map", "class": "Maps", "other": ["ItemLevel <= 76", "DropLevel 74"], "type": "map yellow good"},
	"0 Shaped Oasis Map": {"base": "Shaped Oasis Map", "class": "Maps", "other": ["ItemLevel <= 76", "DropLevel 74"], "type": "map yellow good"},
	"1 Arachnid Tomb Map": {"base": "Arachnid Tomb Map", "class": "Maps", "other": ["ItemLevel <= 76", "DropLevel 74"], "type": "map yellow good"},
	"1 Castle Ruins Map": {"base": "Castle Ruins Map", "class": "Maps", "other": ["ItemLevel <= 76", "DropLevel 74"], "type": "map yellow good"},
	"1 Catacombs Map": {"base": "Catacombs Map", "class": "Maps", "other": ["ItemLevel <= 76", "DropLevel 74"], "type": "map yellow good"},
	"1 Cells Map": {"base": "Cells Map", "class": "Maps", "other": ["ItemLevel <= 76", "DropLevel 74"], "type": "map yellow good"},
	"1 Armoury Map": {"base": "Armoury Map", "class": "Maps", "other": ["ItemLevel <= 76", "DropLevel 74"], "type": "map yellow good"},
	"1 Ashen Wood Map": {"base": "Ashen Wood Map", "class": "Maps", "other": ["ItemLevel <= 76", "DropLevel 74"], "type": "map yellow good"},
	"1 Mud Geyser Map": {"base": "Mud Geyser Map", "class": "Maps", "other": ["ItemLevel <= 76", "DropLevel 74"], "type": "map yellow good"},

	# Tier 8
	"0 Shaped Arid Lake Map": {"base": "Shaped Arid Lake Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},
	"0 Shaped Cavern Map": {"base": "Shaped Cavern Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},
	"0 Shaped Channel Map": {"base": "Shaped Channel Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},
	"0 Shaped Grotto Map": {"base": "Shaped Grotto Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},
	"0 Shaped Marshes Map": {"base": "Shaped Marshes Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},
	"0 Shaped Sewer Map": {"base": "Shaped Sewer Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},
	"0 Shaped Vaal Pyramid Map": {"base": "Shaped Vaal Pyramid Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},
	"1 Arachnid Nest Map": {"base": "Arachnid Nest Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},
	"1 Arena Map": {"base": "Arena Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},
	"1 Bog Map": {"base": "Bog Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},
	"1 Cemetery Map": {"base": "Cemetery Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},
	"1 Barrows Map": {"base": "Barrows Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},
	"1 Atoll Map": {"base": "Atoll Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},
	"1 Pier Map": {"base": "Pier Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},
	"1 Shore Map": {"base": "Shore Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},
	"1 Tropical Island Map": {"base": "Tropical Island Map", "class": "Maps", "other": ["ItemLevel <= 77", "DropLevel 75"], "type": "map yellow good"},

	# Tier 9
	"0 Shaped Academy Map": {"base": "Shaped Academy Map", "class": "Maps", "other": ["ItemLevel <= 78", "DropLevel 76"], "type": "map yellow good"},
	"0 Shaped Acid Lakes Map": {"base": "Shaped Acid Lakes Map", "class": "Maps", "other": ["ItemLevel <= 78", "DropLevel 76"], "type": "map yellow good"},
	"0 Shaped Dungeon Map": {"base": "Shaped Dungeon Map", "class": "Maps", "other": ["ItemLevel <= 78", "DropLevel 76"], "type": "map yellow good"},
	"0 Shaped Graveyard Map": {"base": "Shaped Graveyard Map", "class": "Maps", "other": ["ItemLevel <= 78", "DropLevel 76"], "type": "map yellow good"},
	"0 Shaped Phantasmagoria Map": {"base": "Shaped Phantasmagoria Map", "class": "Maps", "other": ["ItemLevel <= 78", "DropLevel 76"], "type": "map yellow good"},
	"0 Shaped Villa Map": {"base": "Shaped Villa Map", "class": "Maps", "other": ["ItemLevel <= 78", "DropLevel 76"], "type": "map yellow good"},
	"0 Shaped Waste Pool Map": {"base": "Shaped Waste Pool Map", "class": "Maps", "other": ["ItemLevel <= 78", "DropLevel 76"], "type": "map yellow good"},
	"1 Coves Map": {"base": "Coves Map", "class": "Maps", "other": ["ItemLevel <= 78", "DropLevel 76"], "type": "map yellow good"},
	"1 Crypt Map": {"base": "Crypt Map", "class": "Maps", "other": ["ItemLevel <= 78", "DropLevel 76"], "type": "map yellow good"},
	"1 Museum Map": {"base": "Museum Map", "class": "Maps", "other": ["ItemLevel <= 78", "DropLevel 76"], "type": "map yellow good"},
	"1 Orchard Map": {"base": "Orchard Map", "class": "Maps", "other": ["ItemLevel <= 78", "DropLevel 76"], "type": "map yellow good"},
	"1 Overgrown Shrine Map": {"base": "Overgrown Shrine Map", "class": "Maps", "other": ["ItemLevel <= 78", "DropLevel 76"], "type": "map yellow good"},
	"1 Promenade Map": {"base": "Promenade Map", "class": "Maps", "other": ["ItemLevel <= 78", "DropLevel 76"], "type": "map yellow good"},
	"1 Reef Map": {"base": "Reef Map", "class": "Maps", "other": ["ItemLevel <= 78", "DropLevel 76"], "type": "map yellow good"},
	"1 Temple Map": {"base": "Temple Map", "class": "Maps", "other": ["ItemLevel <= 78", "DropLevel 76"], "type": "map yellow good"},

	# Tier 10
	"0 Shaped Burial Chambers Map": {"base": "Shaped Burial Chambers Map", "class": "Maps", "other": ["ItemLevel <= 79", "DropLevel 77"], "type": "map yellow good"},
	"0 Shaped Peninsula Map": {"base": "Shaped Peninsula Map", "class": "Maps", "other": ["ItemLevel <= 79", "DropLevel 77"], "type": "map yellow good"},
	"0 Shaped Dunes Map": {"base": "Shaped Dunes Map", "class": "Maps", "other": ["ItemLevel <= 79", "DropLevel 77"], "type": "map yellow good"},
	"0 Shaped Mesa Map": {"base": "Shaped Mesa Map", "class": "Maps", "other": ["ItemLevel <= 79", "DropLevel 77"], "type": "map yellow good"},
	"0 Shaped Pit Map": {"base": "Shaped Pit Map", "class": "Maps", "other": ["ItemLevel <= 79", "DropLevel 77"], "type": "map yellow good"},
	"0 Shaped Primordial Pool Map": {"base": "Shaped Primordial Pool Map", "class": "Maps", "other": ["ItemLevel <= 79", "DropLevel 77"], "type": "map yellow good"},
	"0 Shaped Spider Lair Map": {"base": "Shaped Spider Lair Map", "class": "Maps", "other": ["ItemLevel <= 79", "DropLevel 77"], "type": "map yellow good"},
	"0 Shaped Tower Map": {"base": "Shaped Tower Map", "class": "Maps", "other": ["ItemLevel <= 79", "DropLevel 77"], "type": "map yellow good"},
	"1 Colonnade Map": {"base": "Colonnade Map", "class": "Maps", "other": ["ItemLevel <= 79", "DropLevel 77"], "type": "map yellow good"},
	"1 Arsenal Map": {"base": "Arsenal Map", "class": "Maps", "other": ["ItemLevel <= 79", "DropLevel 77"], "type": "map yellow good"},
	"1 Courtyard Map": {"base": "Courtyard Map", "class": "Maps", "other": ["ItemLevel <= 79", "DropLevel 77"], "type": "map yellow good"},
	"1 Malformation Map": {"base": "Malformation Map", "class": "Maps", "other": ["ItemLevel <= 79", "DropLevel 77"], "type": "map yellow good"},
	"1 Quay Map": {"base": "Quay Map", "class": "Maps", "other": ["ItemLevel <= 79", "DropLevel 77"], "type": "map yellow good"},
	"1 Terrace Map": {"base": "Terrace Map", "class": "Maps", "other": ["ItemLevel <= 79", "DropLevel 77"], "type": "map yellow good"},
	"1 Underground River Map": {"base": "Underground River Map", "class": "Maps", "other": ["ItemLevel <= 79", "DropLevel 77"], "type": "map yellow good"},

	# Tier 11
	"0 Shaped Canyon Map": {"base": "Shaped Canyon Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},
	"0 Shaped Quarry Map": {"base": "Shaped Quarry Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},
	"0 Shaped Racecourse Map": {"base": "Shaped Racecourse Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},
	"0 Shaped Ramparts Map": {"base": "Shaped Ramparts Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},
	"0 Shaped Spider Forest Map": {"base": "Shaped Spider Forest Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},
	"0 Shaped Strand Map": {"base": "Shaped Strand Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},
	"0 Shaped Thicket Map": {"base": "Shaped Thicket Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},
	"0 Shaped Vaal City Map": {"base": "Shaped Vaal City Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},
	"0 Shaped Wharf Map": {"base": "Shaped Wharf Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},
	"1 Bazaar Map": {"base": "Bazaar Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},
	"1 Chateau Map": {"base": "Chateau Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},
	"1 Excavation Map": {"base": "Excavation Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},
	"1 Precinct Map": {"base": "Precinct Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},
	"1 Torture Chamber Map": {"base": "Torture Chamber Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},
	"1 Underground Sea Map": {"base": "Underground Sea Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},
	"1 Wasteland Map": {"base": "Wasteland Map", "class": "Maps", "other": ["ItemLevel <= 80", "DropLevel 78"], "type": "map red good"},

	# Tier 12
	"0 Shaped Arachnid Tomb Map": {"base": "Shaped Arachnid Tomb Map", "class": "Maps", "other": ["ItemLevel <= 81", "DropLevel 79"], "type": "map red good"},
	"0 Shaped Castle Ruins Map": {"base": "Shaped Castle Ruins Map", "class": "Maps", "other": ["ItemLevel <= 81", "DropLevel 79"], "type": "map red good"},
	"0 Shaped Catacombs Map": {"base": "Shaped Catacombs Map", "class": "Maps", "other": ["ItemLevel <= 81", "DropLevel 79"], "type": "map red good"},
	"0 Shaped Cells Map": {"base": "Shaped Cells Map", "class": "Maps", "other": ["ItemLevel <= 81", "DropLevel 79"], "type": "map red good"},
	"0 Shaped Armoury Map": {"base": "Shaped Armoury Map", "class": "Maps", "other": ["ItemLevel <= 81", "DropLevel 79"], "type": "map red good"},
	"0 Shaped Ashen Wood Map": {"base": "Shaped Ashen Wood Map", "class": "Maps", "other": ["ItemLevel <= 81", "DropLevel 79"], "type": "map red good"},
	"0 Shaped Mud Geyser Map": {"base": "Shaped Mud Geyser Map", "class": "Maps", "other": ["ItemLevel <= 81", "DropLevel 79"], "type": "map red good"},
	"1 Crematorium Map": {"base": "Crematorium Map", "class": "Maps", "other": ["ItemLevel <= 81", "DropLevel 79"], "type": "map red good"},
	"1 Estuary Map": {"base": "Estuary Map", "class": "Maps", "other": ["ItemLevel <= 81", "DropLevel 79"], "type": "map red good"},
	"1 Necropolis Map": {"base": "Necropolis Map", "class": "Maps", "other": ["ItemLevel <= 81", "DropLevel 79"], "type": "map red good"},
	"1 Plateau Map": {"base": "Plateau Map", "class": "Maps", "other": ["ItemLevel <= 81", "DropLevel 79"], "type": "map red good"},
	"1 Ivory Temple Map": {"base": "Ivory Temple Map", "class": "Maps", "other": ["ItemLevel <= 81", "DropLevel 79"], "type": "map red good"},
	"1 Residence Map": {"base": "Residence Map", "class": "Maps", "other": ["ItemLevel <= 81", "DropLevel 79"], "type": "map red good"},
	"1 Shipyard Map": {"base": "Shipyard Map", "class": "Maps", "other": ["ItemLevel <= 81", "DropLevel 79"], "type": "map red good"},
	"1 Vault Map": {"base": "Vault Map", "class": "Maps", "other": ["ItemLevel <= 81", "DropLevel 79"], "type": "map red good"},

	# Tier 13
	"0 Shaped Arachnid Nest Map": {"base": "Shaped Arachnid Nest Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"0 Shaped Arena Map": {"base": "Shaped Arena Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"0 Shaped Bog Map": {"base": "Shaped Bog Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"0 Shaped Cemetery Map": {"base": "Shaped Cemetery Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"0 Shaped Barrows Map": {"base": "Shaped Barrows Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"0 Shaped Atoll Map": {"base": "Shaped Atoll Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"0 Shaped Pier Map": {"base": "Shaped Pier Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"0 Shaped Shore Map": {"base": "Shaped Shore Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"0 Shaped Tropical Island Map": {"base": "Shaped Tropical Island Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"1 Lair Map": {"base": "Lair Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"1 Beacon Map": {"base": "Beacon Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"1 Gorge Map": {"base": "Gorge Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"1 High Gardens Map": {"base": "High Gardens Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"1 Plaza Map": {"base": "Plaza Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"1 Scriptorium Map": {"base": "Scriptorium Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"1 Sulphur Wastes Map": {"base": "Sulphur Wastes Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},
	"1 Waterways Map": {"base": "Waterways Map", "class": "Maps", "other": ["ItemLevel <= 82", "DropLevel 80"], "type": "map red good"},

	# Tier 14
	"0 Shaped Coves Map": {"base": "Shaped Coves Map", "class": "Maps", "other": ["ItemLevel <= 83", "DropLevel 81"], "type": "map red good"},
	"0 Shaped Crypt Map": {"base": "Shaped Crypt Map", "class": "Maps", "other": ["ItemLevel <= 83", "DropLevel 81"], "type": "map red good"},
	"0 Shaped Museum Map": {"base": "Shaped Museum Map", "class": "Maps", "other": ["ItemLevel <= 83", "DropLevel 81"], "type": "map red good"},
	"0 Shaped Orchard Map": {"base": "Shaped Orchard Map", "class": "Maps", "other": ["ItemLevel <= 83", "DropLevel 81"], "type": "map red good"},
	"0 Shaped Overgrown Shrine Map": {"base": "Shaped Overgrown Shrine Map", "class": "Maps", "other": ["ItemLevel <= 83", "DropLevel 81"], "type": "map red good"},
	"0 Shaped Promenade Map": {"base": "Shaped Promenade Map", "class": "Maps", "other": ["ItemLevel <= 83", "DropLevel 81"], "type": "map red good"},
	"0 Shaped Reef Map": {"base": "Shaped Reef Map", "class": "Maps", "other": ["ItemLevel <= 83", "DropLevel 81"], "type": "map red good"},
	"0 Shaped Temple Map": {"base": "Shaped Temple Map", "class": "Maps", "other": ["ItemLevel <= 83", "DropLevel 81"], "type": "map red good"},
	"1 Maze Map": {"base": "Maze Map", "class": "Maps", "other": ["ItemLevel <= 83", "DropLevel 81"], "type": "map red good"},
	"1 Mineral Pools Map": {"base": "Mineral Pools Map", "class": "Maps", "other": ["ItemLevel <= 83", "DropLevel 81"], "type": "map red good"},
	"1 Palace Map": {"base": "Palace Map", "class": "Maps", "other": ["ItemLevel <= 83", "DropLevel 81"], "type": "map red good"},
	"1 Shrine Map": {"base": "Shrine Map", "class": "Maps", "other": ["ItemLevel <= 83", "DropLevel 81"], "type": "map red good"},
	"1 Springs Map": {"base": "Springs Map", "class": "Maps", "other": ["ItemLevel <= 83", "DropLevel 81"], "type": "map red good"},
	"1 Volcano Map": {"base": "Volcano Map", "class": "Maps", "other": ["ItemLevel <= 83", "DropLevel 81"], "type": "map red good"},

	# Tier 15
	"0 Shaped Colonnade Map": {"base": "Shaped Colonnade Map", "class": "Maps", "other": ["ItemLevel <= 84", "DropLevel 82"], "type": "map red good"},
	"0 Shaped Arsenal Map": {"base": "Shaped Arsenal Map", "class": "Maps", "other": ["ItemLevel <= 84", "DropLevel 82"], "type": "map red good"},
	"0 Shaped Courtyard Map": {"base": "Shaped Courtyard Map", "class": "Maps", "other": ["ItemLevel <= 84", "DropLevel 82"], "type": "map red good"},
	"0 Shaped Malformation Map": {"base": "Shaped Malformation Map", "class": "Maps", "other": ["ItemLevel <= 84", "DropLevel 82"], "type": "map red good"},
	"0 Shaped Quay Map": {"base": "Shaped Quay Map", "class": "Maps", "other": ["ItemLevel <= 84", "DropLevel 82"], "type": "map red good"},
	"0 Shaped Terrace Map": {"base": "Shaped Terrace Map", "class": "Maps", "other": ["ItemLevel <= 84", "DropLevel 82"], "type": "map red good"},
	"0 Shaped Underground River Map": {"base": "Shaped Underground River Map", "class": "Maps", "other": ["ItemLevel <= 84", "DropLevel 82"], "type": "map red good"},
	"1 Abyss Map": {"base": "Abyss Map", "class": "Maps", "other": ["ItemLevel <= 84", "DropLevel 82"], "type": "map red good"},
	"1 Colosseum Map": {"base": "Colosseum Map", "class": "Maps", "other": ["ItemLevel <= 84", "DropLevel 82"], "type": "map red good"},
	"1 Core Map": {"base": "Core Map", "class": "Maps", "other": ["ItemLevel <= 84", "DropLevel 82"], "type": "map red good"},
	"1 Dark Forest Map": {"base": "Dark Forest Map", "class": "Maps", "other": ["ItemLevel <= 84", "DropLevel 82"], "type": "map red good"},
	"1 Overgrown Ruin Map": {"base": "Overgrown Ruin Map", "class": "Maps", "other": ["ItemLevel <= 84", "DropLevel 82"], "type": "map red good"},

	# Tier 16
	"1 Pit of the Chimera Map": {"base": "Pit of the Chimera Map", "class": "Maps", "other": ["ItemLevel <= 85", "DropLevel 83"], "type": "map red good"},
	"1 Lair of the Hydra Map": {"base": "Lair of the Hydra Map", "class": "Maps", "other": ["ItemLevel <= 85", "DropLevel 83"], "type": "map red good"},
	"1 Maze of the Minotaur Map": {"base": "Maze of the Minotaur Map", "class": "Maps", "other": ["ItemLevel <= 85", "DropLevel 83"], "type": "map red good"},
	"1 Forge of the Phoenix Map": {"base": "Forge of the Phoenix Map", "class": "Maps", "other": ["ItemLevel <= 85", "DropLevel 83"], "type": "map red good"},
	"1 Vaal Temple Map": {"base": "Vaal Temple Map", "class": "Maps", "other": ["ItemLevel <= 85", "DropLevel 83"], "type": "map red good"},

	"0 Sacrifice at Dusk": {"base": "Sacrifice at Dusk", "class": "Map Fragments", "type": "ignore"},
	"0 Sacrifice at Midnight": {"base": "Sacrifice at Midnight", "class": "Map Fragments", "type": "map white good"},
	"0 Sacrifice at Dawn": {"base": "Sacrifice at Dawn", "class": "Map Fragments", "type": "ignore"},
	"0 Sacrifice at Noon": {"base": "Sacrifice at Noon", "class": "Map Fragments", "type": "ignore"},

	"0 Mortal Grief": {"base": "Mortal Grief", "class": "Map Fragments", "type": "map yellow"},
	"0 Mortal Rage": {"base": "Mortal Rage", "class": "Map Fragments", "type": "map yellow"},
	"0 Mortal Hope": {"base": "Mortal Hope", "class": "Map Fragments", "type": "map yellow good"},
	"0 Mortal Ignorance": {"base": "Mortal Ignorance", "class": "Map Fragments", "type": "map yellow"},

	"0 Eber's Key": {"base": "Eber's Key", "class": "Map Fragments", "type": "map yellow good"},
	"0 Yriel's Key": {"base": "Yriel's Key", "class": "Map Fragments", "type": "map yellow good"},
	"0 Inya's Key": {"base": "Inya's Key", "class": "Map Fragments", "type": "map yellow good"},
	"0 Volkuur's Key": {"base": "Volkuur's Key", "class": "Map Fragments", "type": "map yellow good"},

	"0 Fragment of the Phoenix": {"base": "Fragment of the Phoenix", "class": "Map Fragments", "type": "map red good"},
	"0 Fragment of the Minotaur": {"base": "Fragment of the Minotaur", "class": "Map Fragments", "type": "map red good"},
	"0 Fragment of the Chimera": {"base": "Fragment of the Chimera", "class": "Map Fragments", "type": "map red good"},
	"0 Fragment of the Hydra": {"base": "Fragment of the Hydra", "class": "Map Fragments", "type": "map red good"},

	"71 Maps >= 78": {"class": "Maps", "other": ["DropLevel >= 78"], "type": "map red"},
	"72 Maps <= 72": {"class": "Maps", "other": ["DropLevel <= 72"], "type": "map white"},
	"73 Other maps": {"class": "Maps", "type": "map yellow"},
	"74 Map Fragments": {"class": "Map Fragments", "type": "map white"},
}
