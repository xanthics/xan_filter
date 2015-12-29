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

desc = "template"

# Text settings for various categories
settings = {
    "regal": ["Rarity Rare",
              "ItemLevel >= 75",
              "SetFontSize 40",
              "SetBorderColor 0 0 255"],
    "chaos": ["Rarity Rare",
              "ItemLevel >= 60",
              "SetFontSize 40",
              "SetBorderColor 255 0 0"],
    "very high": ["Rarity Rare"],
    "high": ["Rarity Rare"],
    "normal": ["Rarity Rare",
               "SetFontSize 30"],
    "low": ["Rarity Rare"],
    "hide": ["Rarity Rare"]
}

# Base type : settings pair
items = {
    "01 regal jewellery": {"class": "Rings\" \"Amulets\" \"Belts", "type": "regal"},
    "02 chaos jewellery": {"class": "Rings\" \"Amulets\" \"Belts", "type": "chaos"},
    "99 Other rares": {"type": "normal"}
}