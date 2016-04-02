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
	"Rusted Sword": {"base": "Rusted Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 6"], "type": "levelling rare normal"},
	"Copper Sword": {"base": "Copper Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 10"], "type": "levelling rare normal"},
	"Sabre": {"base": "Sabre", "class": "One Hand Sword", "other": ["ItemLevel <= 15"], "type": "levelling rare normal"},
	"Broad Sword": {"base": "Broad Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 20"], "type": "levelling rare normal"},
	"War Sword": {"base": "War Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 25"], "type": "levelling rare normal"},
	"Ancient Sword": {"base": "Ancient Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 29"], "type": "levelling rare normal"},
	"Elegant Sword": {"base": "Elegant Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 33"], "type": "levelling rare normal"},
	"Dusk Blade": {"base": "Dusk Blade", "class": "One Hand Sword", "other": ["ItemLevel <= 37"], "type": "levelling rare normal"},
	"Hook Sword": {"base": "Hook Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 39"], "type": "levelling rare normal"},
	"Variscite Blade": {"base": "Variscite Blade", "class": "One Hand Sword", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Cutlass": {"base": "Cutlass", "class": "One Hand Sword", "other": ["ItemLevel <= 43"], "type": "levelling rare normal"},
	"Baselard": {"base": "Baselard", "class": "One Hand Sword", "other": ["ItemLevel <= 46"], "type": "levelling rare normal"},
	"Battle Sword": {"base": "Battle Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 49"], "type": "levelling rare normal"},
	"Elder Sword": {"base": "Elder Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 52"], "type": "levelling rare normal"},
	"Graceful Sword": {"base": "Graceful Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 55"], "type": "levelling rare normal"},
	"Twilight Blade": {"base": "Twilight Blade", "class": "One Hand Sword", "other": ["ItemLevel <= 58"], "type": "levelling rare normal"},
	"Grappler": {"base": "Grappler", "class": "One Hand Sword", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Gemstone Sword": {"base": "Gemstone Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 61"], "type": "levelling rare normal"},
	"Corsair Sword": {"base": "Corsair Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 63"], "type": "levelling rare normal"},
	"Gladius": {"base": "Gladius", "class": "One Hand Sword", "other": ["ItemLevel <= 65"], "type": "levelling rare normal"},
	"Legion Sword": {"base": "Legion Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Vaal Blade": {"base": "Vaal Blade", "class": "One Hand Sword", "other": ["ItemLevel <= 69"], "type": "levelling rare normal"},
	"Eternal Sword": {"base": "Eternal Sword", "class": "One Hand Sword", "other": ["ItemLevel <= 71"], "type": "levelling rare normal"},
	"Midnight Blade": {"base": "Midnight Blade", "class": "One Hand Sword", "other": ["ItemLevel <= 73"], "type": "levelling rare normal"},
	"Tiger Hook": {"base": "Tiger Hook", "class": "One Hand Sword", "other": ["ItemLevel <= 75"], "type": "levelling rare normal"}
}
