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
	"Nailed Fist": {"base": "Nailed Fist", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "normal"},
	"Sharktooth Claw": {"base": "Sharktooth Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 12"], "type": "normal"},
	"Awl": {"base": "Awl", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "normal"},
	"Cat's Paw": {"base": "Cat's Paw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "normal"},
	"Blinder": {"base": "Blinder", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 27"], "type": "normal"},
	"Timeworn Claw": {"base": "Timeworn Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 31"], "type": "normal"},
	"Sparkling Claw": {"base": "Sparkling Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 35"], "type": "normal"},
	"Fright Claw": {"base": "Fright Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "normal"},
	"Double Claw": {"base": "Double Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "normal"},
	"Thresher Claw": {"base": "Thresher Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "normal"},
	"Gouger": {"base": "Gouger", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 45"], "type": "normal"},
	"Tiger's Paw": {"base": "Tiger's Paw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 48"], "type": "normal"},
	"Gut Ripper": {"base": "Gut Ripper", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 51"], "type": "ignore"},
	"Prehistoric Claw": {"base": "Prehistoric Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "ignore"},
	"Noble Claw": {"base": "Noble Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 57"], "type": "ignore"},
	"Eagle Claw": {"base": "Eagle Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Twin Claw": {"base": "Twin Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "ignore"},
	"Great White Claw": {"base": "Great White Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "ignore"},
	"Throat Stabber": {"base": "Throat Stabber", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "ignore"},
	"Hellion's Paw": {"base": "Hellion's Paw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Eye Gouger": {"base": "Eye Gouger", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "ignore"},
	"Vaal Claw": {"base": "Vaal Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "ignore"},
	"Imperial Claw": {"base": "Imperial Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"},
	"Terror Claw": {"base": "Terror Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"},
	"Gemini Claw": {"base": "Gemini Claw", "class": "Claw", "other": ["Rarity <= Magic", "ItemLevel <= 77"], "type": "ignore"}
}
