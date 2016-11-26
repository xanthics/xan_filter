"""
* Copyright (c) 2016 Jeremy Parks. All rights reserved.
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
	"Crude Bow": {"base": "Crude Bow", "class": "Bow", "other": ["ItemLevel <= 6"], "type": "levelling rare normal"},
	"Short Bow": {"base": "Short Bow", "class": "Bow", "other": ["ItemLevel <= 10"], "type": "levelling rare normal"},
	"Long Bow": {"base": "Long Bow", "class": "Bow", "other": ["ItemLevel <= 14"], "type": "levelling rare normal"},
	"Composite Bow": {"base": "Composite Bow", "class": "Bow", "other": ["ItemLevel <= 19"], "type": "levelling rare normal"},
	"Recurve Bow": {"base": "Recurve Bow", "class": "Bow", "other": ["ItemLevel <= 23"], "type": "levelling rare normal"},
	"Bone Bow": {"base": "Bone Bow", "class": "Bow", "other": ["ItemLevel <= 28"], "type": "levelling rare normal"},
	"Royal Bow": {"base": "Royal Bow", "class": "Bow", "other": ["ItemLevel <= 33"], "type": "levelling rare normal"},
	"Death Bow": {"base": "Death Bow", "class": "Bow", "other": ["ItemLevel <= 37"], "type": "levelling rare high"},
	"Grove Bow": {"base": "Grove Bow", "class": "Bow", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Reflex Bow": {"base": "Reflex Bow", "class": "Bow", "other": ["ItemLevel <= 41"], "type": "levelling rare normal"},
	"Decurve Bow": {"base": "Decurve Bow", "class": "Bow", "other": ["ItemLevel <= 43"], "type": "levelling rare normal"},
	"Compound Bow": {"base": "Compound Bow", "class": "Bow", "other": ["ItemLevel <= 46"], "type": "levelling rare normal"},
	"Sniper Bow": {"base": "Sniper Bow", "class": "Bow", "other": ["ItemLevel <= 49"], "type": "levelling rare normal"},
	"Ivory Bow": {"base": "Ivory Bow", "class": "Bow", "other": ["ItemLevel <= 52"], "type": "levelling rare normal"},
	"Highborn Bow": {"base": "Highborn Bow", "class": "Bow", "other": ["ItemLevel <= 55"], "type": "levelling rare normal"},
	"Decimation Bow": {"base": "Decimation Bow", "class": "Bow", "other": ["ItemLevel <= 58"], "type": "levelling rare high"},
	"Thicket Bow": {"base": "Thicket Bow", "class": "Bow", "other": ["ItemLevel <= 61"], "type": "levelling rare normal"},
	"Steelwood Bow": {"base": "Steelwood Bow", "class": "Bow", "other": ["ItemLevel <= 62"], "type": "levelling rare normal"},
	"Citadel Bow": {"base": "Citadel Bow", "class": "Bow", "other": ["ItemLevel <= 63"], "type": "levelling rare normal"},
	"Ranger Bow": {"base": "Ranger Bow", "class": "Bow", "other": ["ItemLevel <= 65"], "type": "levelling rare normal"},
	"Assassin Bow": {"base": "Assassin Bow", "class": "Bow", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Spine Bow": {"base": "Spine Bow", "class": "Bow", "other": ["ItemLevel <= 69"], "type": "ignore"},
	"Imperial Bow": {"base": "Imperial Bow", "class": "Bow", "other": ["ItemLevel <= 71"], "type": "ignore"},
	"Harbinger Bow": {"base": "Harbinger Bow", "class": "Bow", "other": ["ItemLevel <= 73"], "type": "ignore"},
	"Maraketh Bow": {"base": "Maraketh Bow", "class": "Bow", "other": ["ItemLevel <= 76"], "type": "ignore"}
}
