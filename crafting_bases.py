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

desc = "Crafting Bases"

# Text settings for various categories
settings = {
    "very high": ["Rarity Normal",
                  "SetFontSize 35",
                  "SetBorderColor 200 200 200"],
    "high": ["Rarity Normal"],
    "normal": ["Rarity Normal",
               "SetFontSize 28"],
    "low": ["Rarity Normal"],
    "ignore": [""],
    "hide": ["Rarity Normal"]
}

# Base type : settings pair
items = {
    "0 Ilvl 75+ Amulet": {"class": "Amulet", "other": ["ItemLevel >= 75"], "type": "normal"},
    "0 Ilvl 75+ Ring": {"class": "Ring", "other": ["ItemLevel >= 75"], "type": "normal"},
    "0 Ilvl 75+ Belt": {"class": "Belt", "other": ["ItemLevel >= 75"], "type": "normal"},
    "9 Other bases": {"type": "ignore"}
}