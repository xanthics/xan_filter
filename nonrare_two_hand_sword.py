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
	"Corroded Blade": {"base": "Corroded Blade", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "normal"},
	"Longsword": {"base": "Longsword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 13"], "type": "normal"},
	"Bastard Sword": {"base": "Bastard Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "normal"},
	"Two-Handed Sword": {"base": "Two-Handed Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "normal"},
	"Etched Greatsword": {"base": "Etched Greatsword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 27"], "type": "normal"},
	"Ornate Sword": {"base": "Ornate Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 32"], "type": "normal"},
	"Spectral Sword": {"base": "Spectral Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "normal"},
	"Curved Blade": {"base": "Curved Blade", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "normal"},
	"Butcher Sword": {"base": "Butcher Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "normal"},
	"Footman Sword": {"base": "Footman Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 45"], "type": "normal"},
	"Highland Blade": {"base": "Highland Blade", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 49"], "type": "normal"},
	"Engraved Greatsword": {"base": "Engraved Greatsword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 53"], "type": "normal"},
	"Tiger Sword": {"base": "Tiger Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 56"], "type": "normal"},
	"Wraith Sword": {"base": "Wraith Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 59"], "type": "normal"},
	"Lithe Blade": {"base": "Lithe Blade", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "normal"},
	"Headman's Sword": {"base": "Headman's Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "normal"},
	"Reaver Sword": {"base": "Reaver Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "normal"},
	"Ezomyte Blade": {"base": "Ezomyte Blade", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 66"], "type": "normal"},
	"Vaal Greatsword": {"base": "Vaal Greatsword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 68"], "type": "normal"},
	"Lion Sword": {"base": "Lion Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "normal"},
	"Infernal Sword": {"base": "Infernal Sword", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 72"], "type": "normal"},
	"Exquisite Blade": {"base": "Exquisite Blade", "class": "Two Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "normal"}
}
