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

desc = "Flasks"

# Text settings for various categories
settings = {
    "very high": [""],
    "high": ["SetBorderColor 0 255 0",
             "SetFontSize 32"],
    "normal": ["SetFontSize 28"],
    "low": [""],
    "hide": [""]
}

# Base type : settings pair
items = {
    "01 Qual Flask": {"base": "Flask", "other": ["Quality >= 1"], "type": "high"},
    "02 Diamond Flask": {"base": "Diamond Flask", "other": ["Rarity Normal"], "type": "normal"},
    "03 Granite Flask": {"base": "Granite Flask", "other": ["Rarity Normal"], "type": "normal"},
    "04 Jade Flask": {"base": "Jade Flask", "other": ["Rarity Normal"], "type": "hide"},
    "05 Topaz Flask": {"base": "Topaz Flask", "other": ["Rarity Normal"], "type": "normal"},
    "06 Sapphire Flask": {"base": "Sapphire Flask", "other": ["Rarity Normal"], "type": "normal"},
    "07 Ruby Flask": {"base": "Ruby Flask", "other": ["Rarity Normal"], "type": "normal"},
    "08 Quicksilver Flask": {"base": "Quicksilver Flask", "other": ["ItemLevel <= 25"], "type": "normal"},
    "09 Quicksilver Flask": {"base": "Quicksilver Flask", "other": ["Rarity Normal"], "type": "normal"},
    "10 Amethyst Flask": {"base": "Amethyst Flask", "other": ["Rarity Normal"], "type": "normal"},
    "11 Small Flasks": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 0", "ItemLevel <= 3"], "type": "normal"},
    "12 Medium Flasks": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 3", "ItemLevel <= 6"], "type": "normal"},
    "13 Large Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 6", "ItemLevel <= 12"], "type": "normal"},
    "14 Greater Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 12", "ItemLevel <= 18"], "type": "normal"},
    "15 Grand Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 18", "ItemLevel <= 24"], "type": "normal"},
    "16 Giant Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 24", "ItemLevel <= 30"], "type": "normal"},
    "17 Colossal Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 30", "ItemLevel <= 36"], "type": "normal"},
    "18 Sacred Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 36", "ItemLevel <= 42"], "type": "normal"},
    "19 Hallowed Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 42", "ItemLevel <= 60"], "type": "normal"},
    "20 Sanctified Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 50", "ItemLevel <= 60"], "type": "normal"},
    "21 Divine Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 60", "ItemLevel <= 65"], "type": "normal"},
    "22 Eternal Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 65", "ItemLevel <= 70"], "type": "normal"},
#    "98 Other Flasks": {"base": "Flask", "type": "hide"},
}