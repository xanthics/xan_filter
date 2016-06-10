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
	"Corroded Blade": {"base": "Corroded Blade", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "leveling low"},
	"Longsword": {"base": "Longsword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 13"], "type": "leveling low"},
	"Bastard Sword": {"base": "Bastard Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "leveling low"},
	"Two-Handed Sword": {"base": "Two-Handed Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "leveling low"},
	"Etched Greatsword": {"base": "Etched Greatsword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 27"], "type": "leveling low"},
	"Ornate Sword": {"base": "Ornate Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 32"], "type": "leveling low"},
	"Spectral Sword": {"base": "Spectral Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "leveling low"},
	"Curved Blade": {"base": "Curved Blade", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Butcher Sword": {"base": "Butcher Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "leveling low"},
	"Footman Sword": {"base": "Footman Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 45"], "type": "leveling low"},
	"Highland Blade": {"base": "Highland Blade", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 49"], "type": "leveling low"},
	"Engraved Greatsword": {"base": "Engraved Greatsword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 53"], "type": "ignore"},
	"Tiger Sword": {"base": "Tiger Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 56"], "type": "ignore"},
	"Wraith Sword": {"base": "Wraith Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 59"], "type": "ignore"},
	"Lithe Blade": {"base": "Lithe Blade", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "ignore"},
	"Headman's Sword": {"base": "Headman's Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "ignore"},
	"Reaver Sword": {"base": "Reaver Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "ignore"},
	"Ezomyte Blade": {"base": "Ezomyte Blade", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 66"], "type": "ignore"},
	"Vaal Greatsword": {"base": "Vaal Greatsword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 68"], "type": "ignore"},
	"Lion Sword": {"base": "Lion Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "ignore"},
	"Infernal Sword": {"base": "Infernal Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 72"], "type": "ignore"},
	"Exquisite Blade": {"base": "Exquisite Blade", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"}
}
