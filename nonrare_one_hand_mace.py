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
	"Driftwood Club": {"base": "Driftwood Club", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 6"], "type": "leveling low"},
	"Tribal Club": {"base": "Tribal Club", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 10"], "type": "leveling low"},
	"Spiked Club": {"base": "Spiked Club", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 15"], "type": "leveling low"},
	"Stone Hammer": {"base": "Stone Hammer", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 20"], "type": "leveling low"},
	"War Hammer": {"base": "War Hammer", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 25"], "type": "leveling low"},
	"Bladed Mace": {"base": "Bladed Mace", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 29"], "type": "leveling low"},
	"Ceremonial Mace": {"base": "Ceremonial Mace", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "leveling low"},
	"Dream Mace": {"base": "Dream Mace", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "leveling low"},
	"Wyrm Mace": {"base": "Wyrm Mace", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "leveling low"},
	"Petrified Club": {"base": "Petrified Club", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Barbed Club": {"base": "Barbed Club", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 43"], "type": "leveling low"},
	"Rock Breaker": {"base": "Rock Breaker", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "leveling low"},
	"Battle Hammer": {"base": "Battle Hammer", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 49"], "type": "leveling low"},
	"Flanged Mace": {"base": "Flanged Mace", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 52"], "type": "ignore"},
	"Ornate Mace": {"base": "Ornate Mace", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 55"], "type": "ignore"},
	"Phantom Mace": {"base": "Phantom Mace", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "ignore"},
	"Dragon Mace": {"base": "Dragon Mace", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Ancestral Club": {"base": "Ancestral Club", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "ignore"},
	"Tenderizer": {"base": "Tenderizer", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Gavel": {"base": "Gavel", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "ignore"},
	"Legion Hammer": {"base": "Legion Hammer", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Pernarch": {"base": "Pernarch", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "ignore"},
	"Auric Mace": {"base": "Auric Mace", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "ignore"},
	"Nightmare Mace": {"base": "Nightmare Mace", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"},
	"Behemoth Mace": {"base": "Behemoth Mace", "class": "One Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"}
}
