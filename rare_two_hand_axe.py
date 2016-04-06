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
	"Stone Axe": {"base": "Stone Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 9"], "type": "levelling rare normal"},
	"Jade Chopper": {"base": "Jade Chopper", "class": "Two Hand Axe", "other": ["ItemLevel <= 14"], "type": "levelling rare normal"},
	"Woodsplitter": {"base": "Woodsplitter", "class": "Two Hand Axe", "other": ["ItemLevel <= 18"], "type": "levelling rare normal"},
	"Poleaxe": {"base": "Poleaxe", "class": "Two Hand Axe", "other": ["ItemLevel <= 23"], "type": "levelling rare normal"},
	"Double Axe": {"base": "Double Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 28"], "type": "levelling rare normal"},
	"Gilded Axe": {"base": "Gilded Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 33"], "type": "levelling rare normal"},
	"Shadow Axe": {"base": "Shadow Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 38"], "type": "levelling rare normal"},
	"Dagger Axe": {"base": "Dagger Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 41"], "type": "levelling rare normal"},
	"Jasper Chopper": {"base": "Jasper Chopper", "class": "Two Hand Axe", "other": ["ItemLevel <= 42"], "type": "levelling rare normal"},
	"Timber Axe": {"base": "Timber Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 46"], "type": "levelling rare normal"},
	"Headsman Axe": {"base": "Headsman Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 50"], "type": "levelling rare normal"},
	"Labrys": {"base": "Labrys", "class": "Two Hand Axe", "other": ["ItemLevel <= 54"], "type": "levelling rare normal"},
	"Noble Axe": {"base": "Noble Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 57"], "type": "levelling rare normal"},
	"Abyssal Axe": {"base": "Abyssal Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Karui Chopper": {"base": "Karui Chopper", "class": "Two Hand Axe", "other": ["ItemLevel <= 63"], "type": "levelling rare normal"},
	"Talon Axe": {"base": "Talon Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 64"], "type": "levelling rare normal"},
	"Sundering Axe": {"base": "Sundering Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 65"], "type": "levelling rare normal"},
	"Ezomyte Axe": {"base": "Ezomyte Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Vaal Axe": {"base": "Vaal Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 69"], "type": "ignore"},
	"Despot Axe": {"base": "Despot Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 71"], "type": "ignore"},
	"Void Axe": {"base": "Void Axe", "class": "Two Hand Axe", "other": ["ItemLevel <= 73"], "type": "ignore"},
	"Fleshripper": {"base": "Fleshripper", "class": "Two Hand Axe", "other": ["ItemLevel <= 75"], "type": "ignore"}
}
