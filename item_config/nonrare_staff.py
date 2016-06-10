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

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Gnarled Branch": {"base": "Gnarled Branch", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 9"], "type": "leveling low"},
	"Primitive Staff": {"base": "Primitive Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 14"], "type": "leveling low"},
	"Long Staff": {"base": "Long Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 18"], "type": "leveling low"},
	"Iron Staff": {"base": "Iron Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 23"], "type": "leveling low"},
	"Coiled Staff": {"base": "Coiled Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 28"], "type": "leveling low"},
	"Royal Staff": {"base": "Royal Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "leveling low"},
	"Vile Staff": {"base": "Vile Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 38"], "type": "leveling low"},
	"Crescent Staff": {"base": "Crescent Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "leveling low"},
	"Woodful Staff": {"base": "Woodful Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "leveling low"},
	"Quarterstaff": {"base": "Quarterstaff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "leveling low"},
	"Military Staff": {"base": "Military Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "leveling low"},
	"Serpentine Staff": {"base": "Serpentine Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "ignore"},
	"Highborn Staff": {"base": "Highborn Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 57"], "type": "ignore"},
	"Foul Staff": {"base": "Foul Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Moon Staff": {"base": "Moon Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "ignore"},
	"Primordial Staff": {"base": "Primordial Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Lathi": {"base": "Lathi", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "ignore"},
	"Ezomyte Staff": {"base": "Ezomyte Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Maelström Staff": {"base": "Maelström Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "ignore"},
	"Imperial Staff": {"base": "Imperial Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "ignore"},
	"Judgement Staff": {"base": "Judgement Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"},
	"Eclipse Staff": {"base": "Eclipse Staff", "class": "Staves", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"}
}
