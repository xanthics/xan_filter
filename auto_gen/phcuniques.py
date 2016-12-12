#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 12/10/2016(m/d/y) 01:15:14 UTC from "Hardcore Breach" data
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
	"0 Carnal Sceptre": {"base": "Carnal Sceptre", "type": "unique very high"},
	"0 Champion Kite Shield": {"base": "Champion Kite Shield", "type": "unique very high"},
	"0 Chateau Map": {"base": "Chateau Map", "type": "unique very high"},
	"0 Citrine Amulet": {"base": "Citrine Amulet", "type": "unique very high"},
	"0 Clasped Mitts": {"base": "Clasped Mitts", "type": "unique very high"},
	"0 Clutching Talisman": {"base": "Clutching Talisman", "type": "unique very high"},
	"0 Crusader Boots": {"base": "Crusader Boots", "type": "unique very high"},
	"0 Cutlass": {"base": "Cutlass", "type": "unique very high"},
	"0 Deicide Mask": {"base": "Deicide Mask", "type": "unique very high"},
	"0 Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "type": "unique very high"},
	"0 Gladiator Plate": {"base": "Gladiator Plate", "type": "unique very high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"0 Golden Bracers": {"base": "Golden Bracers", "type": "unique very high"},
	"0 Golden Caligae": {"base": "Golden Caligae", "type": "unique very high"},
	"0 Golden Flame": {"base": "Golden Flame", "type": "unique very high"},
	"0 Golden Hoop": {"base": "Golden Hoop", "type": "unique very high"},
	"0 Golden Mantle": {"base": "Golden Mantle", "type": "unique very high"},
	"0 Golden Obi": {"base": "Golden Obi", "type": "unique very high"},
	"0 Golden Wreath": {"base": "Golden Wreath", "type": "unique very high"},
	"0 Grand Mana Flask": {"base": "Grand Mana Flask", "type": "unique very high"},
	"0 Greatwolf Talisman": {"base": "Greatwolf Talisman", "type": "unique very high"},
	"0 Jasper Chopper": {"base": "Jasper Chopper", "type": "unique very high"},
	"0 Jet Amulet": {"base": "Jet Amulet", "type": "unique very high"},
	"0 Jewelled Foil": {"base": "Jewelled Foil", "type": "unique very high"},
	"0 Legion Gloves": {"base": "Legion Gloves", "type": "unique very high"},
	"0 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique very high"},
	"0 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique very high"},
	"0 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique very high"},
	"0 Ritual Sceptre": {"base": "Ritual Sceptre", "type": "unique very high"},
	"0 Rotfeather Talisman": {"base": "Rotfeather Talisman", "type": "unique very high"},
	"0 Royal Axe": {"base": "Royal Axe", "type": "unique very high"},
	"0 Ruby Amulet": {"base": "Ruby Amulet", "type": "unique very high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique very high"},
	"0 Steelhead": {"base": "Steelhead", "type": "unique very high"},
	"0 Void Axe": {"base": "Void Axe", "type": "unique very high"},
	"1 Abyssal Axe": {"base": "Abyssal Axe", "type": "unique high"},
	"1 Arcanist Gloves": {"base": "Arcanist Gloves", "type": "unique high"},
	"1 Cedar Tower Shield": {"base": "Cedar Tower Shield", "type": "unique high"},
	"1 Citadel Bow": {"base": "Citadel Bow", "type": "unique high"},
	"1 Corrugated Buckler": {"base": "Corrugated Buckler", "type": "unique high"},
	"1 Courtyard Map": {"base": "Courtyard Map", "type": "unique high"},
	"1 Desert Brigandine": {"base": "Desert Brigandine", "type": "unique high"},
	"1 Despot Axe": {"base": "Despot Axe", "type": "unique high"},
	"1 Eternal Sword": {"base": "Eternal Sword", "type": "unique high"},
	"1 Exquisite Leather": {"base": "Exquisite Leather", "type": "unique high"},
	"1 Fiend Dagger": {"base": "Fiend Dagger", "type": "unique high"},
	"1 Fishing Rod": {"base": "Fishing Rod", "type": "unique high"},
	"1 Full Wyrmscale": {"base": "Full Wyrmscale", "type": "unique high"},
	"1 Granite Flask": {"base": "Granite Flask", "type": "unique high"},
	"1 Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "type": "unique high"},
	"1 Karui Sceptre": {"base": "Karui Sceptre", "type": "unique high"},
	"1 Lion Pelt": {"base": "Lion Pelt", "type": "unique high"},
	"1 Meatgrinder": {"base": "Meatgrinder", "type": "unique high"},
	"1 Midnight Blade": {"base": "Midnight Blade", "type": "unique high"},
	"1 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique high"},
	"1 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique high"},
	"1 Raven Mask": {"base": "Raven Mask", "type": "unique high"},
	"1 Regicide Mask": {"base": "Regicide Mask", "type": "unique high"},
	"1 Royal Burgonet": {"base": "Royal Burgonet", "type": "unique high"},
	"1 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "unique high"},
	"1 Sanctified Mana Flask": {"base": "Sanctified Mana Flask", "type": "unique high"},
	"1 Sharkskin Tunic": {"base": "Sharkskin Tunic", "type": "unique high"},
	"1 Siege Axe": {"base": "Siege Axe", "type": "unique high"},
	"1 Silver Flask": {"base": "Silver Flask", "type": "unique high"},
	"1 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique high"},
	"1 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique high"},
	"1 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique high"},
	"1 Temple Map": {"base": "Temple Map", "type": "unique high"},
	"1 Terror Maul": {"base": "Terror Maul", "type": "unique high"},
	"1 Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "type": "unique high"},
	"1 Topaz Flask": {"base": "Topaz Flask", "type": "unique high"},
	"1 Vaal Mask": {"base": "Vaal Mask", "type": "unique high"},
	"1 Vaal Regalia": {"base": "Vaal Regalia", "type": "unique high"},
	"1 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique high"},
	"1 Vaal Spirit Shield": {"base": "Vaal Spirit Shield", "type": "unique high"},
	"1 Vanguard Belt": {"base": "Vanguard Belt", "type": "unique high"},
	"1 Varnished Coat": {"base": "Varnished Coat", "type": "unique high"},
	"1 Wereclaw Talisman": {"base": "Wereclaw Talisman", "type": "unique high"},
	"7 Aventail Helmet": {"base": "Aventail Helmet", "type": "unique low"},
	"7 Awl": {"base": "Awl", "type": "unique low"},
	"7 Buckskin Tunic": {"base": "Buckskin Tunic", "type": "unique low"},
	"7 Chain Gloves": {"base": "Chain Gloves", "type": "unique low"},
	"7 Compound Spiked Shield": {"base": "Compound Spiked Shield", "type": "unique low"},
	"7 Gnarled Branch": {"base": "Gnarled Branch", "type": "unique low"},
	"7 Goathide Boots": {"base": "Goathide Boots", "type": "unique low"},
	"7 Golden Buckler": {"base": "Golden Buckler", "type": "unique low"},
	"7 Great Helmet": {"base": "Great Helmet", "type": "unique low"},
	"7 Iron Mask": {"base": "Iron Mask", "type": "unique low"},
	"7 Ironscale Boots": {"base": "Ironscale Boots", "type": "unique low"},
	"7 Leather Hood": {"base": "Leather Hood", "type": "unique low"},
	"7 Lunaris Circlet": {"base": "Lunaris Circlet", "type": "unique low"},
	"7 Moonstone Ring": {"base": "Moonstone Ring", "type": "unique low"},
	"7 Ornate Ringmail": {"base": "Ornate Ringmail", "type": "unique low"},
	"7 Painted Buckler": {"base": "Painted Buckler", "type": "unique low"},
	"7 Prophet Crown": {"base": "Prophet Crown", "type": "unique low"},
	"7 Quartz Flask": {"base": "Quartz Flask", "type": "unique low"},
	"7 Serrated Arrow Quiver": {"base": "Serrated Arrow Quiver", "type": "unique low"},
	"7 Timeworn Claw": {"base": "Timeworn Claw", "type": "unique low"},
	"7 Tricorne": {"base": "Tricorne", "type": "unique low"},
	"7 Velvet Slippers": {"base": "Velvet Slippers", "type": "unique low"},
	"7 War Buckler": {"base": "War Buckler", "type": "unique low"},
	"9 Other uniques": {"type": "unique normal"}
}
