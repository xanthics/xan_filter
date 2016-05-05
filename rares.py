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

desc = "General Rares"

# Base type : settings pair
items = {
	"1 Quiver": {"class": "Quivers", "type": "rare low"},

	"7 5": {"other": ["DropLevel <= 5", "ItemLevel >= 15"], "type": "rare low"},
    "7 10": {"other": ["DropLevel <= 10", "ItemLevel >= 20"], "type": "rare low"},
    "7 15": {"other": ["DropLevel <= 15", "ItemLevel >= 25"], "type": "rare low"},
    "7 20": {"other": ["DropLevel <= 20", "ItemLevel >= 30"], "type": "rare low"},
    "7 25": {"other": ["DropLevel <= 25", "ItemLevel >= 35"], "type": "rare low"},
    "7 30": {"other": ["DropLevel <= 30", "ItemLevel >= 40"], "type": "rare low"},
    "7 35": {"other": ["DropLevel <= 35", "ItemLevel >= 45"], "type": "rare low"},
    "7 40": {"other": ["DropLevel <= 40", "ItemLevel >= 50"], "type": "rare low"},
    "7 45": {"other": ["DropLevel <= 45", "ItemLevel >= 55"], "type": "rare low"},

    "9 Other rares": {"type": "rare low"}
}