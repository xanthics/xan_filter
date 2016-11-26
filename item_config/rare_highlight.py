#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
* Copyright (c) 2016 Jeremy Parks. All rights reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a
* copy of this software and associated documentation files (the "Software"),
* to deal in the Software without restriction, including without limitation
* the rights to use, copy, modify, merge, publish, distribute, sublicense,
* and/or sell copies of the Software, and to permit persons to whom the
* Software is furnished to do so, subject to the folrare lowing conditions:
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

desc = "Endgame Rare Bases"

# Base type : settings pair
items = {
    "0 Great White Claw": {"base": "Great White Claw", "class": "Claw", "type": "rare high"},
    "0 Eye Gouger": {"base": "Eye Gouger", "class": "Claw", "type": "rare high"},
    "0 Imperial Claw": {"base": "Imperial Claw", "class": "Claw", "type": "rare high"},
    "0 Gemini Claw": {"base": "Gemini Claw", "class": "Claw", "type": "rare high"},

    "0 Ambusher": {"base": "Ambusher", "class": "Dagger", "type": "rare high"},
    "0 Ezomyte Dagger": {"base": "Ezomyte Dagger", "class": "Dagger", "type": "rare high"},
    "0 Imperial Skean": {"base": "Imperial Skean", "class": "Dagger", "type": "rare high"},

    "0 Corsair Sword": {"base": "Corsair Sword", "class": "One Hand Sword", "type": "rare high"},
    "0 Tiger Hook": {"base": "Tiger Hook", "class": "One Hand Sword", "type": "rare high"},

    "0 Dragoon Sword": {"base": "Dragoon Sword", "class": "Thrusting One Hand Sword", "type": "rare high"},
    "0 Harpy Rapier": {"base": "Harpy Rapier", "class": "Thrusting One Hand Sword", "type": "rare high"},
    "0 Jewelled Foil": {"base": "Jewelled Foil", "class": "Thrusting One Hand Sword", "type": "rare high"},
    "0 Spiraled Foil": {"base": "Spiraled Foil", "class": "Thrusting One Hand Sword", "type": "rare high"},
    "0 Vaal Rapier": {"base": "Vaal Rapier", "class": "Thrusting One Hand Sword", "type": "rare high"},

    "0 Siege Axe": {"base": "Siege Axe", "class": "One Hand Axe", "type": "rare high"},
    "0 Vaal Hatchet": {"base": "Vaal Hatchet", "class": "One Hand Axe", "type": "rare high"},
    "0 Runic Hatchet": {"base": "Runic Hatchet", "class": "One Hand Axe", "type": "rare high"},

    "0 Harbinger Bow": {"base": "Harbinger Bow", "class": "Bow", "type": "rare high"},
    "0 Decimation Bow": {"base": "Decimation Bow", "class": "Bow", "type": "rare high"},

    "0 Eclipse Staff": {"base": "Eclipse Staff", "class": "Staves", "type": "rare high"},
    "0 Maelström Staff": {"base": "Maelström Staff", "class": "Staves", "type": "rare high"},
    "0 Imperial Staff": {"base": "Imperial Staff", "class": "Staves", "type": "rare high"},

    "0 Exquisite Blade": {"base": "Exquisite Blade", "class": "Two Hand Swords", "type": "rare high"},
    "0 Reaver Sword": {"base": "Reaver Sword", "class": "Two Hand Swords", "type": "rare high"},

    #"0 2h Axe": {"class": "Two Hand Axes", "other": ["DropLevel >= 62"], "type": "rare high"},
    #"0 2h Mace": {"class": "Two Hand Maces", "other": ["DropLevel >= 61"], "type": "rare high"},
    "0 Void Axe": {"base": "Void Axe", "class": "Two Hand Axes", "type": "rare high"},
    "0 Fleshripper": {"base": "Fleshripper", "class": "Two Hand Axes", "type": "rare high"},

    "0 Karui Maul": {"base": "Karui Maul", "class": "Two Hand Maces", "type": "rare high"},
    "0 Colossus Mallet": {"base": "Colossus Mallet", "class": "Two Hand Maces", "type": "rare high"},
    "0 Piledriver": {"base": "Piledriver", "class": "Two Hand Maces", "type": "rare high"},
    "0 Coronal Maul": {"base": "Coronal Maul", "class": "Two Hand Maces", "type": "rare high"},

    "0 Gloves": {"other": ["DropLevel >= 53"], "class": "Gloves", "type": "rare high"},
    "0 Boots": {"other": ["DropLevel >= 53"], "class": "Boots", "type": "rare high"},
    "0 Body Armours": {"other": ["DropLevel >= 62"], "class": "Body Armours", "type": "rare high"},
    "0 Helmets": {"other": ["DropLevel >= 53"], "class": "Helmets", "type": "rare high"},

    "0 Tower Shield": {"base": "Tower Shield", "other": ["DropLevel >= 62"], "class": "Shields", "type": "rare high"},
    "0 Buckler": {"base": "Buckler", "other": ["DropLevel >= 58"], "class": "Shields", "type": "rare high"},
    "0 Spirit Shield": {"base": "Spirit Shield", "other": ["DropLevel >= 57"], "class": "Shields", "type": "rare high"},
    "0 Round Shield": {"base": "Round Shield", "other": ["DropLevel >= 59"], "class": "Shields", "type": "rare high"},
    "0 Kite Shield": {"base": "Kite Shield", "other": ["DropLevel >= 51"], "class": "Shields", "type": "rare high"},
    "0 Spiked Shield": {"base": "Spiked Shield", "other": ["DropLevel >= 55"], "class": "Shields", "type": "rare high"},

    "0 Jewel": {"class": "Jewel", "type": "rare high"},

    # Caster bases
    "0 Imbued Wand": {"base": "Imbued Wand", "class": "Wand", "type": "rare high"},
    "0 Opal Wand": {"base": "Opal Wand", "class": "Wand", "type": "rare high"},
    "0 Tornado Wand": {"base": "Tornado Wand", "class": "Wand", "type": "rare high"},
    "0 Prophecy Wand": {"base": "Prophecy Wand", "class": "Wand", "type": "rare high"},
    "0 Profane Wand": {"base": "Profane Wand", "class": "Wand", "type": "rare high"},
    "0 Opal Sceptre": {"base": "Opal Sceptre", "class": "Sceptres", "type": "rare high"},
    "0 Vaal Sceptre": {"base": "Vaal Sceptre", "class": "Sceptres", "type": "rare high"},
    "0 Carnal Sceptre": {"base": "Carnal Sceptre", "class": "Sceptres", "type": "rare high"},
    "0 Void Sceptre": {"base": "Void Sceptre", "class": "Sceptres", "type": "rare high"},
    "0 Sambar Sceptre": {"base": "Sambar Sceptre", "class": "Sceptres", "type": "rare high"},

    "0 Copper Kris": {"base": "Copper Kris", "class": "Dagger", "type": "rare high"},
    "0 Imp Dagger": {"base": "Imp Dagger", "class": "Dagger", "type": "rare high"},
    "0 Golden Kris": {"base": "Golden Kris", "class": "Dagger", "type": "rare high"},
    "0 Fiend Dagger": {"base": "Fiend Dagger", "class": "Dagger", "type": "rare high"},
    "0 Platinum Kris": {"base": "Platinum Kris", "class": "Dagger", "type": "rare high"},
    "0 Demon Dagger": {"base": "Ambusher", "class": "Dagger", "type": "rare high"},

    "0 Spike-Point Arrow Quiver": {"base": "Spike-Point Arrow Quiver", "class": "Quivers", "type": "rare high"},
    "0 Broadhead Arrow Quiver": {"base": "Broadhead Arrow Quiver", "class": "Quivers", "type": "rare high"},

    "02 60+ amulet": {"class": "Amulets", "other": ["ItemLevel >= 60"], "type": "rare high"},
    "02 60+ ring": {"class": "Rings", "other": ["ItemLevel >= 60"], "type": "rare high"},
    "02 60+ belt": {"class": "Belts", "other": ["ItemLevel >= 60"], "type": "rare high"},
    "03 amulet": {"class": "Amulets", "type": "levelling rare high"},
    "03 ring": {"class": "Rings", "type": "levelling rare high"},
    "03 belt": {"class": "Belts", "type": "levelling rare high"},
}
