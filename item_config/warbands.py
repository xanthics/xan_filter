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

desc = "Warbands"

# Base type : settings pair
items = {
    "0 Brinerot magic item": {"class": "Gloves", "other": ["Rarity Magic", "SetBorderColor 255 215 0", "Identified True"], "type": "normal"},
    "0 Mutewind magic item": {"class": "Boots", "other": ["Rarity Magic", "SetBorderColor 54 100 146", "Identified True"], "type": "normal"},
    "0 Redblade magic item": {"class": "Helm", "other": ["Rarity Magic", "SetBorderColor 150 0 0", "Identified True"], "type": "normal"},
    "0 Renegade magic item": {"other": ["Class Dagger Wand \"One Hand\" Bow Stave \"Two Hand\" Sceptre Claws", "Rarity Magic", "SetBorderColor 208 32 144", "Identified True"], "type": "normal"},
}
