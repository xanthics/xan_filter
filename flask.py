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
    "very high": ["SetBorderColor 0 255 0",
                  "SetFontSize 35"],
    "high": ["SetBorderColor 0 150 0",
             "SetFontSize 30"],
    "normal": ["SetFontSize 28"],
    "low": [""],
    "ignore": [""],
    "hide": [""]
}

# Base type : settings pair
items = {
    "01 Qual Flask": {"base": "Flask", "other": ["Quality >= 10"], "type": "very high"},
    "02 Qual Flask": {"base": "Flask", "other": ["Quality >= 5"], "type": "ignore"},
    "1 Diamond Flask": {"base": "Diamond Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Granite Flask": {"base": "Granite Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Jade Flask": {"base": "Jade Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Topaz Flask": {"base": "Topaz Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Sapphire Flask": {"base": "Sapphire Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Ruby Flask": {"base": "Ruby Flask", "other": ["Rarity Normal"], "type": "normal"},
    "11 Quicksilver Flask <= 25": {"base": "Quicksilver Flask", "other": ["ItemLevel <= 25"], "type": "normal"},
    "12 Quicksilver Flask": {"base": "Quicksilver Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Amethyst Flask": {"base": "Amethyst Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Basalt Flask": {"base": "Basalt Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Aquamarine  Flask": {"base": "Aquamarine Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Stibnite  Flask": {"base": "Stibnite Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Sulphur  Flask": {"base": "Sulphur Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Bismuth  Flask": {"base": "Bismuth Flask", "other": ["Rarity Normal"], "type": "normal"},

    "1 Small Flasks": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 0", "ItemLevel <= 3"], "type": "normal"},
    "1 Medium Flasks": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 3", "ItemLevel <= 6"], "type": "normal"},
    "1 Large Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 6", "ItemLevel <= 12"], "type": "normal"},
    "1 Greater Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 12", "ItemLevel <= 18"], "type": "normal"},
    "1 Grand Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 18", "ItemLevel <= 24"], "type": "normal"},
    "1 Giant Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 24", "ItemLevel <= 30"], "type": "normal"},
    "1 Colossal Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 30", "ItemLevel <= 36"], "type": "normal"},
    "1 Sacred Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 36", "ItemLevel <= 42"], "type": "normal"},
    "1 Hallowed Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 42", "ItemLevel <= 60"], "type": "normal"},
    "1 Sanctified Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 50", "ItemLevel <= 60"], "type": "normal"},
    "1 Divine Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 60", "ItemLevel <= 65"], "type": "normal"},
    "1 Eternal Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 65", "ItemLevel <= 70"], "type": "normal"},

    "2 Small Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 10", "ItemLevel <= 20"], "type": "normal"},
    "2 medium Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 20", "ItemLevel <= 30"], "type": "normal"},
    "2 large Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 30", "ItemLevel <= 40"], "type": "normal"},
    "2 Colossal Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 40", "ItemLevel <= 50"], "type": "normal"},
    "2 Sacred Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 50", "ItemLevel <= 60"], "type": "normal"},
    "2 Hallowed Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 60", "ItemLevel <= 70"], "type": "normal"},

    "9 Other Flasks": {"base": "Flask", "type": "ignore"}
}