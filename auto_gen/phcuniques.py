#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 09/06/2016(m/d/y) 23:05:33 UTC from "Hardcore Essence" data
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
	"0 Cedar Tower Shield": {"base": "Cedar Tower Shield", "type": "unique very high"},
	"0 Champion Kite Shield": {"base": "Champion Kite Shield", "type": "unique very high"},
	"0 Clasped Mitts": {"base": "Clasped Mitts", "type": "unique very high"},
	"0 Courtyard Map": {"base": "Courtyard Map", "type": "unique very high"},
	"0 Crypt Map": {"base": "Crypt Map", "type": "unique very high"},
	"0 Deicide Mask": {"base": "Deicide Mask", "type": "unique very high"},
	"0 Desert Brigandine": {"base": "Desert Brigandine", "type": "unique very high"},
	"0 Exquisite Leather": {"base": "Exquisite Leather", "type": "unique very high"},
	"0 Fishing Rod": {"base": "Fishing Rod", "type": "unique very high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"0 Imperial Skean": {"base": "Imperial Skean", "type": "unique very high"},
	"0 Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "type": "unique very high"},
	"0 Jewelled Foil": {"base": "Jewelled Foil", "type": "unique very high"},
	"0 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique very high"},
	"0 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique very high"},
	"0 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique very high"},
	"0 Ruby Flask": {"base": "Ruby Flask", "type": "unique very high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique very high"},
	"0 Siege Axe": {"base": "Siege Axe", "type": "unique very high"},
	"0 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique very high"},
	"0 Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "type": "unique very high"},
	"0 Underground River Map": {"base": "Underground River Map", "type": "unique very high"},
	"0 Vaal Regalia": {"base": "Vaal Regalia", "type": "unique very high"},
	"0 Varnished Coat": {"base": "Varnished Coat", "type": "unique very high"},
	"1 Ancient Gauntlets": {"base": "Ancient Gauntlets", "type": "unique high"},
	"1 Archon Kite Shield": {"base": "Archon Kite Shield", "type": "unique high"},
	"1 Atoll Map": {"base": "Atoll Map", "type": "unique high"},
	"1 Broadhead Arrow Quiver": {"base": "Broadhead Arrow Quiver", "type": "unique high"},
	"1 Conjurer Boots": {"base": "Conjurer Boots", "type": "unique high"},
	"1 Crusader Plate": {"base": "Crusader Plate", "type": "unique high"},
	"1 Etched Greatsword": {"base": "Etched Greatsword", "type": "unique high"},
	"1 Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "type": "unique high"},
	"1 Fiend Dagger": {"base": "Fiend Dagger", "type": "unique high"},
	"1 Full Wyrmscale": {"base": "Full Wyrmscale", "type": "unique high"},
	"1 Golden Plate": {"base": "Golden Plate", "type": "unique high"},
	"1 Granite Flask": {"base": "Granite Flask", "type": "unique high"},
	"1 Graveyard Map": {"base": "Graveyard Map", "type": "unique high"},
	"1 Hubris Circlet": {"base": "Hubris Circlet", "type": "unique high"},
	"1 Imperial Staff": {"base": "Imperial Staff", "type": "unique high"},
	"1 Judgement Staff": {"base": "Judgement Staff", "type": "unique high"},
	"1 Karui Maul": {"base": "Karui Maul", "type": "unique high"},
	"1 Karui Sceptre": {"base": "Karui Sceptre", "type": "unique high"},
	"1 Laminated Kite Shield": {"base": "Laminated Kite Shield", "type": "unique high"},
	"1 Necromancer Silks": {"base": "Necromancer Silks", "type": "unique high"},
	"1 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique high"},
	"1 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique high"},
	"1 Promenade Map": {"base": "Promenade Map", "type": "unique high"},
	"1 Sharkskin Boots": {"base": "Sharkskin Boots", "type": "unique high"},
	"1 Silver Flask": {"base": "Silver Flask", "type": "unique high"},
	"1 Sinner Tricorne": {"base": "Sinner Tricorne", "type": "unique high"},
	"1 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique high"},
	"1 Slink Boots": {"base": "Slink Boots", "type": "unique high"},
	"1 Spine Bow": {"base": "Spine Bow", "type": "unique high"},
	"1 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique high"},
	"1 Strand Map": {"base": "Strand Map", "type": "unique high"},
	"1 Strapped Mitts": {"base": "Strapped Mitts", "type": "unique high"},
	"1 Terror Claw": {"base": "Terror Claw", "type": "unique high"},
	"1 Terror Maul": {"base": "Terror Maul", "type": "unique high"},
	"1 Topaz Flask": {"base": "Topaz Flask", "type": "unique high"},
	"1 Torture Chamber Map": {"base": "Torture Chamber Map", "type": "unique high"},
	"1 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique high"},
	"1 Ursine Pelt": {"base": "Ursine Pelt", "type": "unique high"},
	"1 Vaal Axe": {"base": "Vaal Axe", "type": "unique high"},
	"1 Vaal Pyramid Map": {"base": "Vaal Pyramid Map", "type": "unique high"},
	"1 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique high"},
	"9 Other uniques": {"type": "unique normal"}
}
