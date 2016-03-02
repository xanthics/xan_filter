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
				  "ItemLevel <= 50",
				  "SetBackgroundColor 0 0 0 100",
				  "SetBorderColor 255 40 0"],
	"high": ["SetFontSize 24",
			 "ItemLevel <= 50",
			 "SetBackgroundColor 0 0 0 100",
			 "SetBorderColor 0 100 150"],
	"normal": ["SetFontSize 18",
			   "ItemLevel <= 50",
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
	"Paua Amulet": {"base": "Paua Amulet", "other": ["Rarity Normal"], "type": "ignore"},
	"Coral Amulet": {"base": "Coral Amulet", "other": ["Rarity Normal"], "type": "ignore"},
	"Jade Amulet": {"base": "Jade Amulet", "other": ["Rarity Normal"], "type": "normal"},
	"Amber Amulet": {"base": "Amber Amulet", "other": ["Rarity Normal"], "type": "normal"},
	"Lapis Amulet": {"base": "Lapis Amulet", "other": ["Rarity Normal"], "type": "normal"},
	"Gold Amulet": {"base": "Gold Amulet", "other": ["Rarity Normal"], "type": "normal"},
	"Agate Amulet": {"base": "Agate Amulet", "other": ["Rarity Normal"], "type": "normal"},
	"Citrine Amulet": {"base": "Citrine Amulet", "other": ["Rarity Normal"], "type": "normal"},
	"Turquoise Amulet": {"base": "Turquoise Amulet", "other": ["Rarity Normal"], "type": "normal"},
	"Onyx Amulet": {"base": "Onyx Amulet", "other": ["Rarity Normal"], "type": "normal"},
	"Ruby Amulet": {"base": "Ruby Amulet", "other": ["Rarity Normal"], "type": "normal"},
	"Chain Belt": {"base": "Chain Belt", "other": ["Rarity Normal"], "type": "normal"},
	"Rustic Sash": {"base": "Rustic Sash", "other": ["Rarity Normal"], "type": "normal"},
	"Leather Belt": {"base": "Leather Belt", "other": ["Rarity Normal"], "type": "normal"},
	"Heavy Belt": {"base": "Heavy Belt", "other": ["Rarity Normal"], "type": "normal"},
	"Cloth Belt": {"base": "Cloth Belt", "other": ["Rarity Normal"], "type": "ignore"},
	"Studded Belt": {"base": "Studded Belt", "other": ["Rarity Normal"], "type": "ignore"},
	"Iron Ring": {"base": "Iron Ring", "other": ["Rarity Normal"], "type": "normal"},
	"Coral Ring": {"base": "Coral Ring", "other": ["Rarity Normal"], "type": "normal"},
	"Paua Ring": {"base": "Paua Ring", "other": ["Rarity Normal"], "type": "ignore"},
	"Sapphire Ring": {"base": "Sapphire Ring", "other": ["Rarity Normal"], "type": "normal"},
	"Topaz Ring": {"base": "Topaz Ring", "other": ["Rarity Normal"], "type": "normal"},
	"Ruby Ring": {"base": "Ruby Ring", "other": ["Rarity Normal"], "type": "normal"},
	"Gold Ring": {"base": "Gold Ring", "other": ["Rarity Normal"], "type": "normal"},
	"Two-Stone Ring": {"base": "Two-Stone Ring", "other": ["Rarity Normal"], "type": "normal"},
	"Diamond Ring": {"base": "Diamond Ring", "other": ["Rarity Normal"], "type": "normal"},
	"Moonstone Ring": {"base": "Moonstone Ring", "other": ["Rarity Normal"], "type": "normal"},
	"Prismatic Ring": {"base": "Prismatic Ring", "other": ["Rarity Normal"], "type": "normal"},
	"Amethyst Ring": {"base": "Amethyst Ring", "other": ["Rarity Normal"], "type": "normal"},
	"Unset Ring": {"base": "Unset Ring", "other": ["Rarity Normal"], "type": "normal"}
}
