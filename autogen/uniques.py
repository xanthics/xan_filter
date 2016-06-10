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

desc = "Unique"

# Base type : settings pair
items = {
	"0 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique very high"},
	"0 Clasped Mitts": {"base": "Clasped Mitts", "type": "unique very high"},
	"0 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique very high"},
	"0 Crusader Boots": {"base": "Crusader Boots", "type": "unique very high"},
	"0 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique very high"},
	"0 Deicide Mask": {"base": "Deicide Mask", "type": "unique very high"},
	"0 Wereclaw Talisman": {"base": "Wereclaw Talisman", "type": "unique very high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"0 Assassin's Garb": {"base": "Assassin's Garb", "type": "unique very high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique very high"},
	"0 Varnished Coat": {"base": "Varnished Coat", "type": "unique very high"},
	"0 Champion Kite Shield": {"base": "Champion Kite Shield", "type": "unique very high"},
	"0 Raven Mask": {"base": "Raven Mask", "type": "unique very high"},
	"0 Vaal Regalia": {"base": "Vaal Regalia", "type": "unique very high"},
	"0 Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "type": "unique very high"},
	"0 Hubris Circlet": {"base": "Hubris Circlet", "type": "unique very high"},
	"0 Siege Axe": {"base": "Siege Axe", "type": "unique very high"},
	"0 Desert Brigandine": {"base": "Desert Brigandine", "type": "unique very high"},
	"0 Imperial Skean": {"base": "Imperial Skean", "type": "unique very high"},
	"0 Sanctified Life Flask": {"base": "Sanctified Life Flask", "type": "unique very high"},
	"0 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique very high"},
	"0 Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "type": "unique very high"},
	"0 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique very high"},
	"0 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique very high"},
	"0 Ursine Pelt": {"base": "Ursine Pelt", "type": "unique very high"},
	"0 Courtyard Map": {"base": "Courtyard Map", "type": "unique very high"},
	"0 Topaz Flask": {"base": "Topaz Flask", "type": "unique very high"},
	"1 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "unique high"},
	"1 Vaal Mask": {"base": "Vaal Mask", "type": "unique high"},
	"1 Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "type": "unique high"},
	"1 Fishing Rod": {"base": "Fishing Rod", "type": "unique high"},
	"1 Gold Ring": {"base": "Gold Ring", "type": "unique high"},
	"1 Granite Flask": {"base": "Granite Flask", "type": "unique high"},
	"1 Corrugated Buckler": {"base": "Corrugated Buckler", "type": "unique high"},
	"1 Ruby Amulet": {"base": "Ruby Amulet", "type": "unique high"},
	"1 Silver Flask": {"base": "Silver Flask", "type": "unique high"},
	"1 Etched Greatsword": {"base": "Etched Greatsword", "type": "unique high"},
	"1 Sharkskin Tunic": {"base": "Sharkskin Tunic", "type": "unique high"},
	"1 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique high"},
	"1 Conjurer Gloves": {"base": "Conjurer Gloves", "type": "unique high"},
	"1 Nubuck Boots": {"base": "Nubuck Boots", "type": "unique high"},
	"1 Spine Bow": {"base": "Spine Bow", "type": "unique high"},
	"1 Unset Ring": {"base": "Unset Ring", "type": "unique high"},
	"1 Terror Maul": {"base": "Terror Maul", "type": "unique high"},
	"1 Sinner Tricorne": {"base": "Sinner Tricorne", "type": "unique high"},
	"1 Fiend Dagger": {"base": "Fiend Dagger", "type": "unique high"},
	"1 Simple Robe": {"base": "Simple Robe", "type": "unique high"},
	"1 Imperial Staff": {"base": "Imperial Staff", "type": "unique high"},
	"1 Regicide Mask": {"base": "Regicide Mask", "type": "unique high"},
	"1 Reef Map": {"base": "Reef Map", "type": "unique high"},
	"1 Carnal Sceptre": {"base": "Carnal Sceptre", "type": "unique high"},
	"1 Karui Sceptre": {"base": "Karui Sceptre", "type": "unique high"},
	"1 Sharkskin Boots": {"base": "Sharkskin Boots", "type": "unique high"},
	"2 Judgement Staff": {"base": "Judgement Staff", "type": "unique normal"},
	"2 Large Hybrid Flask": {"base": "Large Hybrid Flask", "type": "unique normal"},
	"2 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique normal"},
	"2 Vaal Pyramid Map": {"base": "Vaal Pyramid Map", "type": "unique normal"},
	"2 Imperial Bow": {"base": "Imperial Bow", "type": "unique normal"},
	"2 Paua Ring": {"base": "Paua Ring", "type": "unique normal"},
	"2 Temple Map": {"base": "Temple Map", "type": "unique normal"},
	"2 Full Wyrmscale": {"base": "Full Wyrmscale", "type": "unique normal"},
	"2 Lathi": {"base": "Lathi", "type": "unique normal"},
	"2 Steelscale Gauntlets": {"base": "Steelscale Gauntlets", "type": "unique normal"},
	"2 Archon Kite Shield": {"base": "Archon Kite Shield", "type": "unique normal"},
	"2 Exquisite Leather": {"base": "Exquisite Leather", "type": "unique normal"},
	"2 Hallowed Hybrid Flask": {"base": "Hallowed Hybrid Flask", "type": "unique normal"},
	"2 Karui Maul": {"base": "Karui Maul", "type": "unique normal"},
	"2 Ruby Flask": {"base": "Ruby Flask", "type": "unique normal"},
	"2 Torture Chamber Map": {"base": "Torture Chamber Map", "type": "unique normal"},
	"2 Underground Sea Map": {"base": "Underground Sea Map", "type": "unique normal"},
	"2 Vaal Hatchet": {"base": "Vaal Hatchet", "type": "unique normal"},
	"2 Ancient Greaves": {"base": "Ancient Greaves", "type": "unique normal"},
	"2 Broadhead Arrow Quiver": {"base": "Broadhead Arrow Quiver", "type": "unique normal"},
	"2 Catacomb Map": {"base": "Catacomb Map", "type": "unique normal"},
	"2 Golden Plate": {"base": "Golden Plate", "type": "unique normal"},
	"2 Imperial Claw": {"base": "Imperial Claw", "type": "unique normal"},
	"2 Laminated Kite Shield": {"base": "Laminated Kite Shield", "type": "unique normal"},
	"2 Necromancer Silks": {"base": "Necromancer Silks", "type": "unique normal"},
	"2 Ritual Sceptre": {"base": "Ritual Sceptre", "type": "unique normal"},
	"2 Sapphire Ring": {"base": "Sapphire Ring", "type": "unique normal"},
	"2 Strapped Mitts": {"base": "Strapped Mitts", "type": "unique normal"},
	"2 Trapper Boots": {"base": "Trapper Boots", "type": "unique normal"},
	"2 Arcanist Gloves": {"base": "Arcanist Gloves", "type": "unique normal"},
	"2 Crusader Plate": {"base": "Crusader Plate", "type": "unique normal"},
	"2 Deerskin Gloves": {"base": "Deerskin Gloves", "type": "unique normal"},
	"2 Harlequin Mask": {"base": "Harlequin Mask", "type": "unique normal"},
	"2 Necropolis Map": {"base": "Necropolis Map", "type": "unique normal"},
	"2 Reinforced Greaves": {"base": "Reinforced Greaves", "type": "unique normal"},
	"2 Short Bow": {"base": "Short Bow", "type": "unique normal"},
	"2 Slink Boots": {"base": "Slink Boots", "type": "unique normal"},
	"2 Vine Circlet": {"base": "Vine Circlet", "type": "unique normal"},
	"2 Scholar's Robe": {"base": "Scholar's Robe", "type": "unique normal"},
	"2 Amethyst Flask": {"base": "Amethyst Flask", "type": "unique normal"},
	"2 Ancient Gauntlets": {"base": "Ancient Gauntlets", "type": "unique normal"},
	"2 Conjurer Boots": {"base": "Conjurer Boots", "type": "unique normal"},
	"2 Crusader Gloves": {"base": "Crusader Gloves", "type": "unique normal"},
	"2 Crypt Map": {"base": "Crypt Map", "type": "unique normal"},
	"2 Flaying Knife": {"base": "Flaying Knife", "type": "unique normal"},
	"2 Full Dragonscale": {"base": "Full Dragonscale", "type": "unique normal"},
	"2 Gladius": {"base": "Gladius", "type": "unique normal"},
	"2 Goliath Gauntlets": {"base": "Goliath Gauntlets", "type": "unique normal"},
	"2 Greater Mana Flask": {"base": "Greater Mana Flask", "type": "unique normal"},
	"2 Heavy Belt": {"base": "Heavy Belt", "type": "unique normal"},
	"2 Leather Cap": {"base": "Leather Cap", "type": "unique normal"},
	"2 Maelström Staff": {"base": "Maelström Staff", "type": "unique normal"},
	"2 Mosaic Kite Shield": {"base": "Mosaic Kite Shield", "type": "unique normal"},
	"2 Mountain Ledge Map": {"base": "Mountain Ledge Map", "type": "unique normal"},
	"2 Overgrown Shrine Map": {"base": "Overgrown Shrine Map", "type": "unique normal"},
	"2 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique normal"},
	"2 Platinum Sceptre": {"base": "Platinum Sceptre", "type": "unique normal"},
	"2 Promenade Map": {"base": "Promenade Map", "type": "unique normal"},
	"2 Strand Map": {"base": "Strand Map", "type": "unique normal"},
	"2 Terror Claw": {"base": "Terror Claw", "type": "unique normal"},
	"2 Zodiac Leather": {"base": "Zodiac Leather", "type": "unique normal"},
	"2 Triumphant Lamellar": {"base": "Triumphant Lamellar", "type": "unique normal"},
	"2 Opal Wand": {"base": "Opal Wand", "type": "unique normal"},
	"2 Scholar Boots": {"base": "Scholar Boots", "type": "unique normal"},
	"2 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique normal"},
	"2 Demon's Horn": {"base": "Demon's Horn", "type": "unique normal"},
	"9 Other uniques": {"type": "unique low"}
}
