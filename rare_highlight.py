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

desc = "Always show"

# Text settings for various categories
settings = {
    "regal": ["Rarity Rare",
              "ItemLevel >= 75",
              "SetFontSize 35",
              "SetBorderColor 0 0 150"],
    "chaos": ["Rarity Rare",
              "ItemLevel >= 60",
              "SetFontSize 35",
              "SetBorderColor 150 0 0"],
    "very high": ["Rarity Rare"],
    "high": ["Rarity Rare",
             "SetBorderColor 255 255 119",
             "SetFontSize 34"],
    "normal": ["Rarity Rare"],
    "low": ["Rarity Rare",
            "SetFontSize 24"],
    "ignore": [""],
    "hide": ["Rarity Rare"]
}

# Base type : settings pair
items = {
    "0 Great White Claw": {"base": "Great White Claw", "class": "Claw", "type": "high"},
    "0 Eye Gouger": {"base": "Eye Gouger", "class": "Claw", "type": "high"},
    "0 Imperial Claw": {"base": "Imperial Claw", "class": "Claw", "type": "high"},
    "0 Gemini Claw": {"base": "Gemini Claw", "class": "Claw", "type": "high"},

    "0 Ambusher": {"base": "Ambusher", "class": "Dagger", "type": "high"},
    "0 Ezomyte Dagger": {"base": "Ezomyte Dagger", "class": "Dagger", "type": "high"},
    "0 Imperial Skean": {"base": "Imperial Skean", "class": "Dagger", "type": "high"},

    "0 Corsair Sword": {"base": "Corsair Sword", "class": "One Hand Sword", "type": "high"},
    "0 Tiger Hook": {"base": "Tiger Hook", "class": "One Hand Sword", "type": "high"},

    "0 Dragoon Sword": {"base": "Dragoon Sword", "class": "Thrusting One Hand Sword", "type": "high"},
    "0 Harpy Rapier": {"base": "Harpy Rapier", "class": "Thrusting One Hand Sword", "type": "high"},
    "0 Jewelled Foil": {"base": "Jewelled Foil", "class": "Thrusting One Hand Sword", "type": "high"},
    "0 Spiraled Foil": {"base": "Spiraled Foil", "class": "Thrusting One Hand Sword", "type": "high"},
    "0 Vaal Rapier": {"base": "Vaal Rapier", "class": "Thrusting One Hand Sword", "type": "high"},

    "0 Siege Axe": {"base": "Siege Axe", "class": "One Hand Axe", "type": "high"},
    "0 Vaal Hatchet": {"base": "Vaal Hatchet", "class": "One Hand Axe", "type": "high"},
    "0 Runic Hatchet": {"base": "Runic Hatchet", "class": "One Hand Axe", "type": "high"},

    "0 Harbinger Bow": {"base": "Harbinger Bow", "class": "Bow", "type": "high"},
    "0 Decimation Bow": {"base": "Decimation Bow", "class": "Bow", "type": "high"},

    "0 Eclipse Staff": {"base": "Eclipse Staff", "class": "Staves", "type": "high"},
    "0 Maelström Staff": {"base": "Maelström Staff", "class": "Staves", "type": "high"},
    "0 Imperial Staff": {"base": "Imperial Staff", "class": "Staves", "type": "high"},

    "0 Exquisite Blade": {"base": "Exquisite Blade", "class": "Two Hand Swords", "type": "high"},
    "0 Reaver Sword": {"base": "Reaver Sword", "class": "Two Hand Swords", "type": "high"},

    "0 Void Axe": {"base": "Void Axe", "class": "Two Hand Axes", "type": "high"},
    "0 Fleshripper": {"base": "Fleshripper", "class": "Two Hand Axes", "type": "high"},

    "0 Karui Maul": {"base": "Karui Maul", "class": "Two Hand Maces", "type": "high"},
    "0 Colossus Mallet": {"base": "Colossus Mallet", "class": "Two Hand Maces", "type": "high"},
    "0 Piledriver": {"base": "Piledriver", "class": "Two Hand Maces", "type": "high"},
    "0 Coronal Maul": {"base": "Coronal Maul", "class": "Two Hand Maces", "type": "high"},

    "0 Opal Sceptre": {"base": "Opal Sceptre", "class": "Sceptres", "type": "high"},
    "0 Void Sceptre": {"base": "Void Sceptre", "class": "Sceptres", "type": "high"},

    "0 Gloves": {"other": ["DropLevel >= 53"], "class": "Gloves", "type": "high"},
    "0 Boots": {"other": ["DropLevel >= 53"], "class": "Boots", "type": "high"},
    "0 Body Armours": {"other": ["DropLevel >= 62"], "class": "Body Armours", "type": "high"},
    "0 Helmets": {"other": ["DropLevel >= 53"], "class": "Helmets", "type": "high"},

    "0 Tower Shield": {"base": "Tower Shield", "other": ["DropLevel >= 62"], "class": "Shields", "type": "high"},
    "0 Buckler": {"base": "Buckler", "other": ["DropLevel >= 58"], "class": "Shields", "type": "high"},
    "0 Spirit Shield": {"base": "Spirit Shield", "other": ["DropLevel >= 57"], "class": "Shields", "type": "high"},
    "0 Round Shield": {"base": "Round Shield", "other": ["DropLevel >= 59"], "class": "Shields", "type": "high"},
    "0 Kite Shield": {"base": "Kite Shield", "other": ["DropLevel >= 51"], "class": "Shields", "type": "high"},
    "0 Spiked Shield": {"base": "Spiked Shield", "other": ["DropLevel >= 55"], "class": "Shields", "type": "high"},

    "0 Jewel": {"class": "Jewel", "type": "high"},

    "0 Wand": {"class": "Wand", "type": "high"},

    "0 Spike-Point Arrow Quiver": {"base": "Spike-Point Arrow Quiver", "class": "Quivers", "type": "high"},
    "0 Broadhead Arrow Quiver": {"base": "Broadhead Arrow Quiver", "class": "Quivers", "type": "high"},

    "01 regal amulet": {"class": "Amulets", "type": "regal"},
    "01 regal ring": {"class": "Rings", "type": "regal"},
    "01 regal belt": {"class": "Belts", "type": "regal"},
    "02 chaos amulet": {"class": "Amulets", "type": "chaos"},
    "02 chaos ring": {"class": "Rings", "type": "chaos"},
    "02 chaos belt": {"class": "Belts", "type": "chaos"},

    "7 5": {"other": ["DropLevel <= 5", "ItemLevel >= 15"], "type": "low"},
    "7 10": {"other": ["DropLevel <= 10", "ItemLevel >= 20"], "type": "low"},
    "7 15": {"other": ["DropLevel <= 15", "ItemLevel >= 25"], "type": "low"},
    "7 20": {"other": ["DropLevel <= 20", "ItemLevel >= 30"], "type": "low"},
    "7 25": {"other": ["DropLevel <= 25", "ItemLevel >= 35"], "type": "low"},
    "7 30": {"other": ["DropLevel <= 30", "ItemLevel >= 40"], "type": "low"},
    "7 35": {"other": ["DropLevel <= 35", "ItemLevel >= 45"], "type": "low"},
    "7 40": {"other": ["DropLevel <= 40", "ItemLevel >= 50"], "type": "low"},
    "7 45": {"other": ["DropLevel <= 45", "ItemLevel >= 55"], "type": "low"},

}