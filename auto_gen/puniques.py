#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 12/25/2016(m/d/y) 00:40:54 UTC from "Breach" data
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
	"0 Chateau Map": {"base": "Chateau Map", "type": "unique very high"},
	"0 Clasped Mitts": {"base": "Clasped Mitts", "type": "unique very high"},
	"0 Clutching Talisman": {"base": "Clutching Talisman", "type": "unique very high"},
	"0 Courtyard Map": {"base": "Courtyard Map", "type": "unique very high"},
	"0 Crusader Boots": {"base": "Crusader Boots", "type": "unique very high"},
	"0 Deicide Mask": {"base": "Deicide Mask", "type": "unique very high"},
	"0 Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "type": "unique very high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"0 Golden Bracers": {"base": "Golden Bracers", "type": "unique very high"},
	"0 Golden Caligae": {"base": "Golden Caligae", "type": "unique very high"},
	"0 Golden Flame": {"base": "Golden Flame", "type": "unique very high"},
	"0 Golden Hoop": {"base": "Golden Hoop", "type": "unique very high"},
	"0 Golden Mantle": {"base": "Golden Mantle", "type": "unique very high"},
	"0 Golden Obi": {"base": "Golden Obi", "type": "unique very high"},
	"0 Golden Wreath": {"base": "Golden Wreath", "type": "unique very high"},
	"0 Greatwolf Talisman": {"base": "Greatwolf Talisman", "type": "unique very high"},
	"0 Jet Amulet": {"base": "Jet Amulet", "type": "unique very high"},
	"0 Jewelled Foil": {"base": "Jewelled Foil", "type": "unique very high"},
	"0 Legion Gloves": {"base": "Legion Gloves", "type": "unique very high"},
	"0 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique very high"},
	"0 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique very high"},
	"0 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique very high"},
	"0 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique very high"},
	"0 Rotfeather Talisman": {"base": "Rotfeather Talisman", "type": "unique very high"},
	"0 Royal Axe": {"base": "Royal Axe", "type": "unique very high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique very high"},
	"0 Savant's Robe": {"base": "Savant's Robe", "type": "unique very high"},
	"0 Sharkskin Tunic": {"base": "Sharkskin Tunic", "type": "unique very high"},
	"0 Silver Flask": {"base": "Silver Flask", "type": "unique very high"},
	"0 Topaz Flask": {"base": "Topaz Flask", "type": "unique very high"},
	"0 Void Axe": {"base": "Void Axe", "type": "unique very high"},
	"1 Abyssal Axe": {"base": "Abyssal Axe", "type": "unique high"},
	"1 Champion Kite Shield": {"base": "Champion Kite Shield", "type": "unique high"},
	"1 Citrine Amulet": {"base": "Citrine Amulet", "type": "unique high"},
	"1 Cutlass": {"base": "Cutlass", "type": "unique high"},
	"1 Despot Axe": {"base": "Despot Axe", "type": "unique high"},
	"1 Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "type": "unique high"},
	"1 Fishing Rod": {"base": "Fishing Rod", "type": "unique high"},
	"1 Full Wyrmscale": {"base": "Full Wyrmscale", "type": "unique high"},
	"1 Gladiator Plate": {"base": "Gladiator Plate", "type": "unique high"},
	"1 Grand Mana Flask": {"base": "Grand Mana Flask", "type": "unique high"},
	"1 Imperial Staff": {"base": "Imperial Staff", "type": "unique high"},
	"1 Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "type": "unique high"},
	"1 Jasper Chopper": {"base": "Jasper Chopper", "type": "unique high"},
	"1 Karui Sceptre": {"base": "Karui Sceptre", "type": "unique high"},
	"1 Museum Map": {"base": "Museum Map", "type": "unique high"},
	"1 Ruby Amulet": {"base": "Ruby Amulet", "type": "unique high"},
	"1 Sanctified Mana Flask": {"base": "Sanctified Mana Flask", "type": "unique high"},
	"1 Siege Axe": {"base": "Siege Axe", "type": "unique high"},
	"1 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique high"},
	"1 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique high"},
	"1 Steelhead": {"base": "Steelhead", "type": "unique high"},
	"1 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique high"},
	"1 Temple Map": {"base": "Temple Map", "type": "unique high"},
	"1 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique high"},
	"1 Vaal Regalia": {"base": "Vaal Regalia", "type": "unique high"},
	"1 Varnished Coat": {"base": "Varnished Coat", "type": "unique high"},
	"1 Wereclaw Talisman": {"base": "Wereclaw Talisman", "type": "unique high"},
	"7 Agate Amulet": {"base": "Agate Amulet", "type": "unique low"},
	"7 Antique Rapier": {"base": "Antique Rapier", "type": "unique low"},
	"7 Assassin Bow": {"base": "Assassin Bow", "type": "unique low"},
	"7 Auric Mace": {"base": "Auric Mace", "type": "unique low"},
	"7 Aventail Helmet": {"base": "Aventail Helmet", "type": "unique low"},
	"7 Awl": {"base": "Awl", "type": "unique low"},
	"7 Baroque Round Shield": {"base": "Baroque Round Shield", "type": "unique low"},
	"7 Basket Rapier": {"base": "Basket Rapier", "type": "unique low"},
	"7 Bastard Sword": {"base": "Bastard Sword", "type": "unique low"},
	"7 Blunt Arrow Quiver": {"base": "Blunt Arrow Quiver", "type": "unique low"},
	"7 Boot Blade": {"base": "Boot Blade", "type": "unique low"},
	"7 Boot Knife": {"base": "Boot Knife", "type": "unique low"},
	"7 Branded Kite Shield": {"base": "Branded Kite Shield", "type": "unique low"},
	"7 Brass Maul": {"base": "Brass Maul", "type": "unique low"},
	"7 Brass Spirit Shield": {"base": "Brass Spirit Shield", "type": "unique low"},
	"7 Bronzescale Boots": {"base": "Bronzescale Boots", "type": "unique low"},
	"7 Bronzescale Gauntlets": {"base": "Bronzescale Gauntlets", "type": "unique low"},
	"7 Buckskin Tunic": {"base": "Buckskin Tunic", "type": "unique low"},
	"7 Burnished Spiked Shield": {"base": "Burnished Spiked Shield", "type": "unique low"},
	"7 Carnal Armour": {"base": "Carnal Armour", "type": "unique low"},
	"7 Carved Wand": {"base": "Carved Wand", "type": "unique low"},
	"7 Chain Gloves": {"base": "Chain Gloves", "type": "unique low"},
	"7 Clasped Boots": {"base": "Clasped Boots", "type": "unique low"},
	"7 Cleaver": {"base": "Cleaver", "type": "unique low"},
	"7 Cloth Belt": {"base": "Cloth Belt", "type": "unique low"},
	"7 Cobalt Jewel": {"base": "Cobalt Jewel", "type": "unique low"},
	"7 Compound Spiked Shield": {"base": "Compound Spiked Shield", "type": "unique low"},
	"7 Conquest Chainmail": {"base": "Conquest Chainmail", "type": "unique low"},
	"7 Copper Plate": {"base": "Copper Plate", "type": "unique low"},
	"7 Coral Amulet": {"base": "Coral Amulet", "type": "unique low"},
	"7 Coral Ring": {"base": "Coral Ring", "type": "unique low"},
	"7 Corsair Sword": {"base": "Corsair Sword", "type": "unique low"},
	"7 Crimson Jewel": {"base": "Crimson Jewel", "type": "unique low"},
	"7 Crude Bow": {"base": "Crude Bow", "type": "unique low"},
	"7 Crusader Chainmail": {"base": "Crusader Chainmail", "type": "unique low"},
	"7 Crystal Sceptre": {"base": "Crystal Sceptre", "type": "unique low"},
	"7 Crystal Wand": {"base": "Crystal Wand", "type": "unique low"},
	"7 Cured Quiver": {"base": "Cured Quiver", "type": "unique low"},
	"7 Decimation Bow": {"base": "Decimation Bow", "type": "unique low"},
	"7 Decorative Axe": {"base": "Decorative Axe", "type": "unique low"},
	"7 Deerskin Boots": {"base": "Deerskin Boots", "type": "unique low"},
	"7 Dragonscale Gauntlets": {"base": "Dragonscale Gauntlets", "type": "unique low"},
	"7 Dread Maul": {"base": "Dread Maul", "type": "unique low"},
	"7 Dream Mace": {"base": "Dream Mace", "type": "unique low"},
	"7 Dusk Blade": {"base": "Dusk Blade", "type": "unique low"},
	"7 Ebony Tower Shield": {"base": "Ebony Tower Shield", "type": "unique low"},
	"7 Elegant Ringmail": {"base": "Elegant Ringmail", "type": "unique low"},
	"7 Elegant Sword": {"base": "Elegant Sword", "type": "unique low"},
	"7 Enameled Buckler": {"base": "Enameled Buckler", "type": "unique low"},
	"7 Estoc": {"base": "Estoc", "type": "unique low"},
	"7 Ezomyte Blade": {"base": "Ezomyte Blade", "type": "unique low"},
	"7 Fire Arrow Quiver": {"base": "Fire Arrow Quiver", "type": "unique low"},
	"7 Fright Claw": {"base": "Fright Claw", "type": "unique low"},
	"7 Gavel": {"base": "Gavel", "type": "unique low"},
	"7 Gilded Sallet": {"base": "Gilded Sallet", "type": "unique low"},
	"7 Gnarled Branch": {"base": "Gnarled Branch", "type": "unique low"},
	"7 Goat's Horn": {"base": "Goat's Horn", "type": "unique low"},
	"7 Goathide Boots": {"base": "Goathide Boots", "type": "unique low"},
	"7 Goathide Gloves": {"base": "Goathide Gloves", "type": "unique low"},
	"7 Gold Amulet": {"base": "Gold Amulet", "type": "unique low"},
	"7 Golden Buckler": {"base": "Golden Buckler", "type": "unique low"},
	"7 Golden Mask": {"base": "Golden Mask", "type": "unique low"},
	"7 Great Crown": {"base": "Great Crown", "type": "unique low"},
	"7 Great Helmet": {"base": "Great Helmet", "type": "unique low"},
	"7 Great Mallet": {"base": "Great Mallet", "type": "unique low"},
	"7 Gut Ripper": {"base": "Gut Ripper", "type": "unique low"},
	"7 Harbinger Bow": {"base": "Harbinger Bow", "type": "unique low"},
	"7 Harmonic Spirit Shield": {"base": "Harmonic Spirit Shield", "type": "unique low"},
	"7 Headsman Axe": {"base": "Headsman Axe", "type": "unique low"},
	"7 Highland Blade": {"base": "Highland Blade", "type": "unique low"},
	"7 Holy Chainmail": {"base": "Holy Chainmail", "type": "unique low"},
	"7 Imbued Wand": {"base": "Imbued Wand", "type": "unique low"},
	"7 Infernal Axe": {"base": "Infernal Axe", "type": "unique low"},
	"7 Iron Hat": {"base": "Iron Hat", "type": "unique low"},
	"7 Iron Mask": {"base": "Iron Mask", "type": "unique low"},
	"7 Iron Sceptre": {"base": "Iron Sceptre", "type": "unique low"},
	"7 Iron Staff": {"base": "Iron Staff", "type": "unique low"},
	"7 Ironscale Boots": {"base": "Ironscale Boots", "type": "unique low"},
	"7 Ivory Spirit Shield": {"base": "Ivory Spirit Shield", "type": "unique low"},
	"7 Jagged Maul": {"base": "Jagged Maul", "type": "unique low"},
	"7 Lacquered Garb": {"base": "Lacquered Garb", "type": "unique low"},
	"7 Latticed Ringmail": {"base": "Latticed Ringmail", "type": "unique low"},
	"7 Leather Belt": {"base": "Leather Belt", "type": "unique low"},
	"7 Leather Hood": {"base": "Leather Hood", "type": "unique low"},
	"7 Lion Sword": {"base": "Lion Sword", "type": "unique low"},
	"7 Long Bow": {"base": "Long Bow", "type": "unique low"},
	"7 Long Staff": {"base": "Long Staff", "type": "unique low"},
	"7 Lunaris Circlet": {"base": "Lunaris Circlet", "type": "unique low"},
	"7 Maelström Staff": {"base": "Maelström Staff", "type": "unique low"},
	"7 Mesh Boots": {"base": "Mesh Boots", "type": "unique low"},
	"7 Military Staff": {"base": "Military Staff", "type": "unique low"},
	"7 Mind Cage": {"base": "Mind Cage", "type": "unique low"},
	"7 Moonstone Ring": {"base": "Moonstone Ring", "type": "unique low"},
	"7 Nailed Fist": {"base": "Nailed Fist", "type": "unique low"},
	"7 Necromancer Circlet": {"base": "Necromancer Circlet", "type": "unique low"},
	"7 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique low"},
	"7 Ornate Mace": {"base": "Ornate Mace", "type": "unique low"},
	"7 Ornate Ringmail": {"base": "Ornate Ringmail", "type": "unique low"},
	"7 Ornate Sword": {"base": "Ornate Sword", "type": "unique low"},
	"7 Painted Buckler": {"base": "Painted Buckler", "type": "unique low"},
	"7 Paua Amulet": {"base": "Paua Amulet", "type": "unique low"},
	"7 Pine Buckler": {"base": "Pine Buckler", "type": "unique low"},
	"7 Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "type": "unique low"},
	"7 Plank Kite Shield": {"base": "Plank Kite Shield", "type": "unique low"},
	"7 Plate Vest": {"base": "Plate Vest", "type": "unique low"},
	"7 Platinum Kris": {"base": "Platinum Kris", "type": "unique low"},
	"7 Poleaxe": {"base": "Poleaxe", "type": "unique low"},
	"7 Primordial Staff": {"base": "Primordial Staff", "type": "unique low"},
	"7 Prismatic Ring": {"base": "Prismatic Ring", "type": "unique low"},
	"7 Prophet Crown": {"base": "Prophet Crown", "type": "unique low"},
	"7 Quartz Flask": {"base": "Quartz Flask", "type": "unique low"},
	"7 Quartz Wand": {"base": "Quartz Wand", "type": "unique low"},
	"7 Quicksilver Flask": {"base": "Quicksilver Flask", "type": "unique low"},
	"7 Ranger Bow": {"base": "Ranger Bow", "type": "unique low"},
	"7 Reaver Sword": {"base": "Reaver Sword", "type": "unique low"},
	"7 Recurve Bow": {"base": "Recurve Bow", "type": "unique low"},
	"7 Reinforced Tower Shield": {"base": "Reinforced Tower Shield", "type": "unique low"},
	"7 Rotted Round Shield": {"base": "Rotted Round Shield", "type": "unique low"},
	"7 Royal Bow": {"base": "Royal Bow", "type": "unique low"},
	"7 Royal Skean": {"base": "Royal Skean", "type": "unique low"},
	"7 Royal Staff": {"base": "Royal Staff", "type": "unique low"},
	"7 Ruby Ring": {"base": "Ruby Ring", "type": "unique low"},
	"7 Rusted Sword": {"base": "Rusted Sword", "type": "unique low"},
	"7 Rustic Sash": {"base": "Rustic Sash", "type": "unique low"},
	"7 Sabre": {"base": "Sabre", "type": "unique low"},
	"7 Sage Wand": {"base": "Sage Wand", "type": "unique low"},
	"7 Sage's Robe": {"base": "Sage's Robe", "type": "unique low"},
	"7 Saintly Chainmail": {"base": "Saintly Chainmail", "type": "unique low"},
	"7 Samite Helmet": {"base": "Samite Helmet", "type": "unique low"},
	"7 Secutor Helm": {"base": "Secutor Helm", "type": "unique low"},
	"7 Serpentine Staff": {"base": "Serpentine Staff", "type": "unique low"},
	"7 Serrated Arrow Quiver": {"base": "Serrated Arrow Quiver", "type": "unique low"},
	"7 Shadow Sceptre": {"base": "Shadow Sceptre", "type": "unique low"},
	"7 Shagreen Boots": {"base": "Shagreen Boots", "type": "unique low"},
	"7 Sharktooth Arrow Quiver": {"base": "Sharktooth Arrow Quiver", "type": "unique low"},
	"7 Silk Gloves": {"base": "Silk Gloves", "type": "unique low"},
	"7 Silk Slippers": {"base": "Silk Slippers", "type": "unique low"},
	"7 Skinning Knife": {"base": "Skinning Knife", "type": "unique low"},
	"7 Sledgehammer": {"base": "Sledgehammer", "type": "unique low"},
	"7 Soldier Boots": {"base": "Soldier Boots", "type": "unique low"},
	"7 Soldier Helmet": {"base": "Soldier Helmet", "type": "unique low"},
	"7 Spidersilk Robe": {"base": "Spidersilk Robe", "type": "unique low"},
	"7 Spiked Club": {"base": "Spiked Club", "type": "unique low"},
	"7 Spiraled Wand": {"base": "Spiraled Wand", "type": "unique low"},
	"7 Stealth Boots": {"base": "Stealth Boots", "type": "unique low"},
	"7 Steel Gauntlets": {"base": "Steel Gauntlets", "type": "unique low"},
	"7 Stiletto": {"base": "Stiletto", "type": "unique low"},
	"7 Strapped Boots": {"base": "Strapped Boots", "type": "unique low"},
	"7 Strapped Leather": {"base": "Strapped Leather", "type": "unique low"},
	"7 Studded Belt": {"base": "Studded Belt", "type": "unique low"},
	"7 Studded Round Shield": {"base": "Studded Round Shield", "type": "unique low"},
	"7 Sulphur Flask": {"base": "Sulphur Flask", "type": "unique low"},
	"7 Sundering Axe": {"base": "Sundering Axe", "type": "unique low"},
	"7 Supreme Spiked Shield": {"base": "Supreme Spiked Shield", "type": "unique low"},
	"7 Tarnished Spirit Shield": {"base": "Tarnished Spirit Shield", "type": "unique low"},
	"7 Thresher Claw": {"base": "Thresher Claw", "type": "unique low"},
	"7 Tiger Sword": {"base": "Tiger Sword", "type": "unique low"},
	"7 Timeworn Claw": {"base": "Timeworn Claw", "type": "unique low"},
	"7 Titan Greaves": {"base": "Titan Greaves", "type": "unique low"},
	"7 Tomahawk": {"base": "Tomahawk", "type": "unique low"},
	"7 Topaz Ring": {"base": "Topaz Ring", "type": "unique low"},
	"7 Tornado Wand": {"base": "Tornado Wand", "type": "unique low"},
	"7 Tricorne": {"base": "Tricorne", "type": "unique low"},
	"7 Turquoise Amulet": {"base": "Turquoise Amulet", "type": "unique low"},
	"7 Twilight Blade": {"base": "Twilight Blade", "type": "unique low"},
	"7 Two-Point Arrow Quiver": {"base": "Two-Point Arrow Quiver", "type": "unique low"},
	"7 Vaal Blade": {"base": "Vaal Blade", "type": "unique low"},
	"7 Vaal Buckler": {"base": "Vaal Buckler", "type": "unique low"},
	"7 Vaal Gauntlets": {"base": "Vaal Gauntlets", "type": "unique low"},
	"7 Velvet Gloves": {"base": "Velvet Gloves", "type": "unique low"},
	"7 Velvet Slippers": {"base": "Velvet Slippers", "type": "unique low"},
	"7 Vine Circlet": {"base": "Vine Circlet", "type": "unique low"},
	"7 Viridian Jewel": {"base": "Viridian Jewel", "type": "unique low"},
	"7 Visored Sallet": {"base": "Visored Sallet", "type": "unique low"},
	"7 Void Sceptre": {"base": "Void Sceptre", "type": "unique low"},
	"7 War Buckler": {"base": "War Buckler", "type": "unique low"},
	"7 Wild Leather": {"base": "Wild Leather", "type": "unique low"},
	"7 Wool Gloves": {"base": "Wool Gloves", "type": "unique low"},
	"7 Wrapped Mitts": {"base": "Wrapped Mitts", "type": "unique low"},
	"7 Wyrmscale Gauntlets": {"base": "Wyrmscale Gauntlets", "type": "unique low"},
	"9 Other uniques": {"type": "unique normal"}
}
