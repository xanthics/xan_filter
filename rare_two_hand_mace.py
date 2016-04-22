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
	"Driftwood Maul": {"base": "Driftwood Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 8"], "type": "levelling rare normal"},
	"Tribal Maul": {"base": "Tribal Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 13"], "type": "levelling rare normal"},
	"Mallet": {"base": "Mallet", "class": "Two Hand Mace", "other": ["ItemLevel <= 17"], "type": "levelling rare normal"},
	"Sledgehammer": {"base": "Sledgehammer", "class": "Two Hand Mace", "other": ["ItemLevel <= 22"], "type": "levelling rare normal"},
	"Jagged Maul": {"base": "Jagged Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 27"], "type": "levelling rare normal"},
	"Brass Maul": {"base": "Brass Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 32"], "type": "levelling rare normal"},
	"Fright Maul": {"base": "Fright Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 37"], "type": "levelling rare normal"},
	"Morning Star": {"base": "Morning Star", "class": "Two Hand Mace", "other": ["ItemLevel <= 39"], "type": "levelling rare normal"},
	"Totemic Maul": {"base": "Totemic Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 41"], "type": "levelling rare normal"},
	"Great Mallet": {"base": "Great Mallet", "class": "Two Hand Mace", "other": ["ItemLevel <= 45"], "type": "levelling rare normal"},
	"Steelhead": {"base": "Steelhead", "class": "Two Hand Mace", "other": ["ItemLevel <= 49"], "type": "levelling rare normal"},
	"Spiny Maul": {"base": "Spiny Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 53"], "type": "levelling rare normal"},
	"Plated Maul": {"base": "Plated Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 56"], "type": "levelling rare normal"},
	"Dread Maul": {"base": "Dread Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 59"], "type": "levelling rare normal"},
	"Solar Maul": {"base": "Solar Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 61"], "type": "levelling rare normal"},
	"Karui Maul": {"base": "Karui Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 62"], "type": "levelling rare normal"},
	"Colossus Mallet": {"base": "Colossus Mallet", "class": "Two Hand Mace", "other": ["ItemLevel <= 64"], "type": "levelling rare normal"},
	"Piledriver": {"base": "Piledriver", "class": "Two Hand Mace", "other": ["ItemLevel <= 66"], "type": "levelling rare normal"},
	"Meatgrinder": {"base": "Meatgrinder", "class": "Two Hand Mace", "other": ["ItemLevel <= 68"], "type": "ignore"},
	"Imperial Maul": {"base": "Imperial Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 70"], "type": "ignore"},
	"Terror Maul": {"base": "Terror Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 72"], "type": "ignore"},
	"Coronal Maul": {"base": "Coronal Maul", "class": "Two Hand Mace", "other": ["ItemLevel <= 74"], "type": "ignore"}
}
