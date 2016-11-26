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

# Base type : settings pair
items = {
	"0 Void Sceptre": {"base": "Void Sceptre", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Opal Sceptre": {"base": "Opal Sceptre", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Profane Wand": {"base": "Profane Wand", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Prophecy Wand": {"base": "Prophecy Wand", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Opal Wand": {"base": "Opal Wand", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Sambar Sceptre": {"base": "Sambar Sceptre", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Imbued Wand": {"base": "Imbued Wand", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Vaal Regalia": {"base": "Vaal Regalia", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Sorcerer Boots": {"base": "Sorcerer Boots", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Sorcerer Gloves": {"base": "Sorcerer Gloves", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Hubris Circlet": {"base": "Hubris Circlet", "other": ["ItemLevel >= 84"], "type": "t1 ilvl83/84 crafting"},
	"0 Saintly Chainmail": {"base": "Saintly Chainmail", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Harmonic Spirit Shield": {"base": "Harmonic Spirit Shield", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Fossilised Spirit Shield": {"base": "Fossilised Spirit Shield", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Titan Gauntlets": {"base": "Titan Gauntlets", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Slink Gloves": {"base": "Slink Gloves", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Eternal Burgonet": {"base": "Eternal Burgonet", "other": ["ItemLevel >= 84"], "type": "t1 ilvl83/84 crafting"},
	"0 Lion Pelt": {"base": "Lion Pelt", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Titan Greaves": {"base": "Titan Greaves", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Slink Boots": {"base": "Slink Boots", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Bone Helmet": {"base": "Bone Helmet", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Two-Toned Boots": {"base": "Two-Toned Boots", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Spiked Gloves": {"base": "Spiked Gloves", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Gripped Gloves": {"base": "Gripped Gloves", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Fingerless Silk Gloves": {"base": "Fingerless Silk Gloves", "other": ["ItemLevel >= 84"], "type": "ignore"},

	"0 Coral Ring": {"base": "Coral Ring", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Ruby Ring": {"base": "Ruby Ring", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Sapphire Ring": {"base": "Sapphire Ring", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Topaz Ring": {"base": "Topaz Ring", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Two-Stone Ring": {"base": "Two-Stone Ring", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Diamond Ring": {"base": "Diamond Ring", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Prismatic Ring": {"base": "Prismatic Ring", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Unset Ring": {"base": "Unset Ring", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Gold Ring": {"base": "Gold Ring", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Moonstone Ring": {"base": "Moonstone Ring", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Onyx Amulet": {"base": "Onyx Amulet", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Gold Amulet": {"base": "Gold Amulet", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Citrine Amulet": {"base": "Citrine Amulet", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Turquoise Amulet": {"base": "Turquoise Amulet", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Agate Amulet": {"base": "Agate Amulet", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Amber Amulet": {"base": "Amber Amulet", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Jade Amulet": {"base": "Jade Amulet", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Lapis Amulet": {"base": "Lapis Amulet", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Leather Belt": {"base": "Leather Belt", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Heavy Belt": {"base": "Heavy Belt", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Rustic Sash": {"base": "Rustic Sash", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Steel Ring": {"base": "Steel Ring", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Opal Ring": {"base": "Opal Ring", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Blue Pearl Amulet": {"base": "Blue Pearl Amulet", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Marble Amulet": {"base": "Marble Amulet", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Vanguard Belt": {"base": "Vanguard Belt", "other": ["ItemLevel >= 84"], "type": "ignore"},
	"0 Crystal Belt": {"base": "Crystal Belt", "other": ["ItemLevel >= 84"], "type": "ignore"},

	"0 Lion Sword": {"base": "Lion Sword", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Vaal Greatsword": {"base": "Vaal Greatsword", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Vaal Axe": {"base": "Vaal Axe", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Coronal Maul": {"base": "Coronal Maul", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Exquisite Blade": {"base": "Exquisite Blade", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Fleshripper": {"base": "Fleshripper", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Harbinger Bow": {"base": "Harbinger Bow", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Gemini Claw": {"base": "Gemini Claw", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Ambusher": {"base": "Ambusher", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Platinum Kris": {"base": "Platinum Kris", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Demon Dagger": {"base": "Demon Dagger", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Imperial Skean": {"base": "Imperial Skean", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Vaal Hatchet": {"base": "Vaal Hatchet", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Runic Hatchet": {"base": "Runic Hatchet", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Behemoth Mace": {"base": "Behemoth Mace", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Eternal Sword": {"base": "Eternal Sword", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Tiger Hook": {"base": "Tiger Hook", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Eclipse Staff": {"base": "Eclipse Staff", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Maelström Staff": {"base": "Maelström Staff", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Judgement Staff": {"base": "Judgement Staff", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Jewelled Foil": {"base": "Jewelled Foil", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Dragoon Sword": {"base": "Dragoon Sword", "other": ["ItemLevel >= 83"], "type": "ignore"},
	"0 Sai": {"base": "Sai", "class": "Dagger", "other": ["ItemLevel >= 83"], "type": "ignore"},

	"8 Ilvl 75+ Amulet": {"class": "Amulet", "other": ["Rarity Normal", "ItemLevel >= 77"], "type": "ignore"},
	"8 Ilvl 75+ Ring": {"class": "Ring", "other": ["ItemLevel >= 75"], "type": "ignore"},
	"8 Ilvl 75+ Belt": {"class": "Belt", "other": ["ItemLevel >= 75"], "type": "ignore"},

	"9 Other bases": {"type": "ignore"}
}