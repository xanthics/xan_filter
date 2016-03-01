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
	"high": ["Rarity Rare",
             "SetBorderColor 255 255 119",
             "SetFontSize 34"],
	"normal": ["Rarity Rare",
             "SetBorderColor 255 255 119"],
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
	"Driftwood Maul": {"base": "Driftwood Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 8"], "type": "normal"},
	"Tribal Maul": {"base": "Tribal Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 13"], "type": "normal"},
	"Mallet": {"base": "Mallet", "class": "Two Hand Mace", "other": ["ItemLevel <= 17"], "type": "normal"},
	"Sledgehammer": {"base": "Sledgehammer", "class": "Two Hand Mace", "other": ["ItemLevel <= 22"], "type": "normal"},
	"Jagged Maul": {"base": "Jagged Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 27"], "type": "normal"},
	"Brass Maul": {"base": "Brass Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 32"], "type": "normal"},
	"Fright Maul": {"base": "Fright Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 37"], "type": "normal"},
	"Morning Star": {"base": "Morning Star", "class": "Two Hand Mace", "other": ["ItemLevel <= 39"], "type": "normal"},
	"Totemic Maul": {"base": "Totemic Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 41"], "type": "normal"},
	"Great Mallet": {"base": "Great Mallet", "class": "Two Hand Mace", "other": ["ItemLevel <= 45"], "type": "normal"},
	"Steelhead": {"base": "Steelhead", "class": "Two Hand Mace", "other": ["ItemLevel <= 49"], "type": "normal"},
	"Spiny Maul": {"base": "Spiny Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 53"], "type": "normal"},
	"Plated Maul": {"base": "Plated Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 56"], "type": "normal"},
	"Dread Maul": {"base": "Dread Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 59"], "type": "normal"},
	"Solar Maul": {"base": "Solar Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 61"], "type": "normal"},
	"Karui Maul": {"base": "Karui Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 62"], "type": "normal"},
	"Colossus Mallet": {"base": "Colossus Mallet", "class": "Two Hand Mace", "other": ["ItemLevel <= 64"], "type": "normal"},
	"Piledriver": {"base": "Piledriver", "class": "Two Hand Mace", "other": ["ItemLevel <= 66"], "type": "normal"},
	"Meatgrinder": {"base": "Meatgrinder", "class": "Two Hand Mace", "other": ["ItemLevel <= 68"], "type": "normal"},
	"Imperial Maul": {"base": "Imperial Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 70"], "type": "normal"},
	"Terror Maul": {"base": "Terror Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 72"], "type": "normal"},
	"Coronal Maul": {"base": "Coronal Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 74"], "type": "normal"}
}
