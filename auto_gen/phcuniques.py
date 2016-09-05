#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 09/05/2016(m/d/y) 00:16:15 UTC from "Hardcore Essence" data
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

desc = "Unique"

# Base type : settings pair
items = {
	"0 Assassin's Garb": {"base": "Assassin's Garb", "type": "unique very high"},
	"0 Deicide Mask": {"base": "Deicide Mask", "type": "unique very high"},
	"0 Desert Brigandine": {"base": "Desert Brigandine", "type": "unique very high"},
	"0 Eternal Sword": {"base": "Eternal Sword", "type": "unique very high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"0 Hubris Circlet": {"base": "Hubris Circlet", "type": "unique very high"},
	"0 Imperial Skean": {"base": "Imperial Skean", "type": "unique very high"},
	"0 Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "type": "unique very high"},
	"0 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique very high"},
	"0 Painted Tower Shield": {"base": "Painted Tower Shield", "type": "unique very high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique very high"},
	"0 Siege Axe": {"base": "Siege Axe", "type": "unique very high"},
	"0 Terror Maul": {"base": "Terror Maul", "type": "unique very high"},
	"0 Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "type": "unique very high"},
	"0 Topaz Flask": {"base": "Topaz Flask", "type": "unique very high"},
	"0 Vaal Regalia": {"base": "Vaal Regalia", "type": "unique very high"},
	"0 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique very high"},
	"0 Varnished Coat": {"base": "Varnished Coat", "type": "unique very high"},
	"1 Amethyst Flask": {"base": "Amethyst Flask", "type": "unique high"},
	"1 Ancient Gauntlets": {"base": "Ancient Gauntlets", "type": "unique high"},
	"1 Conjurer Boots": {"base": "Conjurer Boots", "type": "unique high"},
	"1 Conjurer Gloves": {"base": "Conjurer Gloves", "type": "unique high"},
	"1 Corrugated Buckler": {"base": "Corrugated Buckler", "type": "unique high"},
	"1 Crusader Gloves": {"base": "Crusader Gloves", "type": "unique high"},
	"1 Crusader Plate": {"base": "Crusader Plate", "type": "unique high"},
	"1 Destiny Leather": {"base": "Destiny Leather", "type": "unique high"},
	"1 Ezomyte Blade": {"base": "Ezomyte Blade", "type": "unique high"},
	"1 Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "type": "unique high"},
	"1 Fiend Dagger": {"base": "Fiend Dagger", "type": "unique high"},
	"1 Fishing Rod": {"base": "Fishing Rod", "type": "unique high"},
	"1 Full Wyrmscale": {"base": "Full Wyrmscale", "type": "unique high"},
	"1 Gold Ring": {"base": "Gold Ring", "type": "unique high"},
	"1 Golden Plate": {"base": "Golden Plate", "type": "unique high"},
	"1 Granite Flask": {"base": "Granite Flask", "type": "unique high"},
	"1 Graveyard Map": {"base": "Graveyard Map", "type": "unique high"},
	"1 Jewelled Foil": {"base": "Jewelled Foil", "type": "unique high"},
	"1 Judgement Staff": {"base": "Judgement Staff", "type": "unique high"},
	"1 Karui Chopper": {"base": "Karui Chopper", "type": "unique high"},
	"1 Karui Maul": {"base": "Karui Maul", "type": "unique high"},
	"1 Laminated Kite Shield": {"base": "Laminated Kite Shield", "type": "unique high"},
	"1 Lathi": {"base": "Lathi", "type": "unique high"},
	"1 Lion Sword": {"base": "Lion Sword", "type": "unique high"},
	"1 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique high"},
	"1 Nubuck Boots": {"base": "Nubuck Boots", "type": "unique high"},
	"1 Paua Ring": {"base": "Paua Ring", "type": "unique high"},
	"1 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique high"},
	"1 Promenade Map": {"base": "Promenade Map", "type": "unique high"},
	"1 Scholar's Robe": {"base": "Scholar's Robe", "type": "unique high"},
	"1 Sharkskin Boots": {"base": "Sharkskin Boots", "type": "unique high"},
	"1 Silver Flask": {"base": "Silver Flask", "type": "unique high"},
	"1 Simple Robe": {"base": "Simple Robe", "type": "unique high"},
	"1 Sinner Tricorne": {"base": "Sinner Tricorne", "type": "unique high"},
	"1 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique high"},
	"1 Slink Boots": {"base": "Slink Boots", "type": "unique high"},
	"1 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique high"},
	"1 Spine Bow": {"base": "Spine Bow", "type": "unique high"},
	"1 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique high"},
	"1 Strapped Mitts": {"base": "Strapped Mitts", "type": "unique high"},
	"1 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique high"},
	"1 Vaal Axe": {"base": "Vaal Axe", "type": "unique high"},
	"1 Vaal Pyramid Map": {"base": "Vaal Pyramid Map", "type": "unique high"},
	"1 Vile Staff": {"base": "Vile Staff", "type": "unique high"},
	"9 Other uniques": {"type": "unique normal"}
}
