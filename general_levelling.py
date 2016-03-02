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

desc = "leveling items that are worth seeing"

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
	"01 Quartz/Crystal/Opal Sceptre": {"base": "Quartz\" \"Crystal\" \"Opal", "class": "Sceptres", "other": ["ItemLevel <= 20", "Rarity <= Magic", "LinkedSockets >= 3"], "type": "very high"},
	"02 Quartz/Crystal/Opal Sceptre": {"base": "Quartz\" \"Crystal\" \"Opal", "class": "Sceptres", "other": ["ItemLevel <= 50", "Rarity <= Magic", "LinkedSockets >= 3"], "type": "high"},

	"0 Boots (Movespeed)": {"class": "Boots", "other": ["Rarity Magic"], "type": "ignore"},

	"1 linked 0-20": {"other": ["Rarity <= Magic", "DropLevel >= 0", "ItemLevel <= 20", "LinkedSockets >= 3"], "type": "high"},
	"1 linked 15-40": {"other": ["Rarity <= Magic", "DropLevel >= 15", "ItemLevel <= 40", "LinkedSockets > 3"], "type": "high"},
	"1 linked 25-50": {"other": ["Rarity <= Magic", "DropLevel >= 25", "ItemLevel <= 50", "LinkedSockets > 3"], "type": "high"},
	"1 linked 40-65": {"other": ["Rarity <= Magic", "DropLevel >= 40", "ItemLevel <= 65", "LinkedSockets > 3"], "type": "high"},
}
