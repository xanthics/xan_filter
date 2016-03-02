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

desc = "Unique"

# Text settings for various categories
settings = {
    "very high": ["Rarity Unique",
                  "SetBorderColor 175 96 37",
                  "SetFontSize 45",
                  "PlayAlertSound 3 300"],
    "high": ["Rarity Unique",
             "SetFontSize 37",
             "SetBorderColor 175 96 37",
             "PlayAlertSound 3 75"],
    "normal": ["Rarity Unique",
               "PlayAlertSound 3 50"],
    "low": ["Rarity Unique",
            "SetFontSize 24",
            "SetBackgroundColor 0 0 0 100"],
    "ignore": [""],
    "hide": ["Rarity Unique"]
}

# Base type : settings pair
items = {
    "0 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "very high"},
    "0 Glorious Plate": {"base": "Glorious Plate", "type": "very high"},
    "0 Prophecy Wand": {"base": "Prophecy Wand", "type": "very high"},
    "0 Desert Brigandine": {"base": "Desert Brigandine", "type": "very high"},
    "0 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "very high"},
    "0 Legion Gloves": {"base": "Legion Gloves", "type": "very high"},
    "0 Ancient Greaves": {"base": "Ancient Greaves", "type": "very high"},
    "0 Vaal Axe": {"base": "Vaal Axe", "type": "very high"},
    "0 Fishing Rod": {"base": "Fishing Rod", "type": "very high"},
    "0 Sapphire Flask": {"base": "Sapphire Flask", "type": "very high"},
    "0 Citrine Amulet": {"base": "Citrine Amulet", "type": "very high"},
    "0 Jasper Chopper": {"base": "Jasper Chopper", "type": "very high"},
    "0 Crusader Gloves": {"base": "Crusader Gloves", "type": "very high"},
    "0 Despot Axe": {"base": "Despot Axe", "type": "very high"},

    "1 Champion Kite Shield": {"base": "Champion Kite Shield", "type": "high"},
    "1 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "high"},
    "1 Serpentscale Boots": {"base": "Serpentscale Boots", "type": "high"},
    "1 Siege Axe": {"base": "Siege Axe", "type": "high"},
    "1 Slaughter Knife": {"base": "Slaughter Knife", "type": "high"},
    "1 Spine Bow": {"base": "Spine Bow", "type": "high"},
    "1 Trapper Boots": {"base": "Trapper Boots", "type": "high"},

    "9 Other uniques": {"type": "normal"},
}