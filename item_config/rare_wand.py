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

desc = "Rare item for leveling or crafting"

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Driftwood Wand": {"base": "Driftwood Wand", "class": "Wand", "other": ["ItemLevel <= 6"], "type": "levelling rare normal"},
	"Goat's Horn": {"base": "Goat's Horn", "class": "Wand", "other": ["ItemLevel <= 11"], "type": "levelling rare normal"},
	"Carved Wand": {"base": "Carved Wand", "class": "Wand", "other": ["ItemLevel <= 17"], "type": "levelling rare normal"},
	"Quartz Wand": {"base": "Quartz Wand", "class": "Wand", "other": ["ItemLevel <= 23"], "type": "levelling rare normal"},
	"Spiraled Wand": {"base": "Spiraled Wand", "class": "Wand", "other": ["ItemLevel <= 29"], "type": "levelling rare normal"},
	"Sage Wand": {"base": "Sage Wand", "class": "Wand", "other": ["ItemLevel <= 35"], "type": "levelling rare normal"},
	"Pagan Wand": {"base": "Pagan Wand", "class": "Wand", "other": ["ItemLevel <= 39"], "type": "levelling rare normal"},
	"Faun's Horn": {"base": "Faun's Horn", "class": "Wand", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Engraved Wand": {"base": "Engraved Wand", "class": "Wand", "other": ["ItemLevel <= 45"], "type": "levelling rare normal"},
	"Crystal Wand": {"base": "Crystal Wand", "class": "Wand", "other": ["ItemLevel <= 50"], "type": "levelling rare normal"},
	"Serpent Wand": {"base": "Serpent Wand", "class": "Wand", "other": ["ItemLevel <= 54"], "type": "levelling rare normal"},
	"Omen Wand": {"base": "Omen Wand", "class": "Wand", "other": ["ItemLevel <= 58"], "type": "levelling rare normal"},
	"Heathen Wand": {"base": "Heathen Wand", "class": "Wand", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Demon's Horn": {"base": "Demon's Horn", "class": "Wand", "other": ["ItemLevel <= 61"], "type": "levelling rare normal"},
	"Imbued Wand": {"base": "Imbued Wand", "class": "Wand", "other": ["ItemLevel <= 64"], "type": "levelling rare normal"},
	"Opal Wand": {"base": "Opal Wand", "class": "Wand", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Tornado Wand": {"base": "Tornado Wand", "class": "Wand", "other": ["ItemLevel <= 70"], "type": "ignore"},
	"Prophecy Wand": {"base": "Prophecy Wand", "class": "Wand", "other": ["ItemLevel <= 73"], "type": "ignore"},
	"Profane Wand": {"base": "Profane Wand", "class": "Wand", "other": ["ItemLevel <= 75"], "type": "ignore"}
}
