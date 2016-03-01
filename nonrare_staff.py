#!/usr/bin/python
# -*- coding: utf-8 -*-
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
	"high": ["SetFontSize 24",
			 "SetBackgroundColor 0 0 0 100",
			 "SetBorderColor 0 100 150"],
	"normal": ["SetFontSize 18",
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
	"Gnarled Branch": {"base": "Gnarled Branch", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 9"], "type": "normal"},
	"Primitive Staff": {"base": "Primitive Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 14"], "type": "normal"},
	"Long Staff": {"base": "Long Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 18"], "type": "normal"},
	"Iron Staff": {"base": "Iron Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 23"], "type": "normal"},
	"Coiled Staff": {"base": "Coiled Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 28"], "type": "normal"},
	"Royal Staff": {"base": "Royal Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "normal"},
	"Vile Staff": {"base": "Vile Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 38"], "type": "normal"},
	"Crescent Staff": {"base": "Crescent Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "normal"},
	"Woodful Staff": {"base": "Woodful Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "normal"},
	"Quarterstaff": {"base": "Quarterstaff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "normal"},
	"Military Staff": {"base": "Military Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "normal"},
	"Serpentine Staff": {"base": "Serpentine Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "normal"},
	"Highborn Staff": {"base": "Highborn Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 57"], "type": "normal"},
	"Foul Staff": {"base": "Foul Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "normal"},
	"Moon Staff": {"base": "Moon Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "normal"},
	"Primordial Staff": {"base": "Primordial Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "normal"},
	"Lathi": {"base": "Lathi", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "normal"},
	"Ezomyte Staff": {"base": "Ezomyte Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "normal"},
	"Maelström Staff": {"base": "Maelström Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "normal"},
	"Imperial Staff": {"base": "Imperial Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "normal"},
	"Judgement Staff": {"base": "Judgement Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "normal"},
	"Eclipse Staff": {"base": "Eclipse Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "normal"}
}
