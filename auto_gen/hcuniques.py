#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 10/22/2018(m/d/y) 04:25:18 UTC from "Hardcore" data

desc = "Unique"

# Base type : settings pair
items = {
	"0 Abyssal Axe": {"base": "Abyssal Axe", "type": "unique extremely high"},
	"0 Carnal Sceptre": {"base": "Carnal Sceptre", "type": "unique extremely high"},
	"0 Corrugated Buckler": {"base": "Corrugated Buckler", "type": "unique extremely high"},
	"0 Crusader Boots": {"base": "Crusader Boots", "type": "unique extremely high"},
	"0 Deicide Mask": {"base": "Deicide Mask", "type": "unique extremely high"},
	"0 Destiny Leather": {"base": "Destiny Leather", "type": "unique extremely high"},
	"0 Elegant Ringmail": {"base": "Elegant Ringmail", "type": "unique extremely high"},
	"0 Etched Greatsword": {"base": "Etched Greatsword", "type": "unique extremely high"},
	"0 Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "type": "unique extremely high"},
	"0 Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "type": "unique extremely high"},
	"0 Full Wyrmscale": {"base": "Full Wyrmscale", "type": "unique extremely high"},
	"0 Gavel": {"base": "Gavel", "type": "unique extremely high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique extremely high"},
	"0 Golden Buckler": {"base": "Golden Buckler", "type": "unique extremely high"},
	"0 Grand Mana Flask": {"base": "Grand Mana Flask", "type": "unique extremely high"},
	"0 Great Mallet": {"base": "Great Mallet", "type": "unique extremely high"},
	"0 Imperial Claw": {"base": "Imperial Claw", "type": "unique extremely high"},
	"0 Jet Amulet": {"base": "Jet Amulet", "type": "unique extremely high"},
	"0 Nightmare Mace": {"base": "Nightmare Mace", "type": "unique extremely high"},
	"0 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique extremely high"},
	"0 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique extremely high"},
	"0 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique extremely high"},
	"0 Quicksilver Flask": {"base": "Quicksilver Flask", "type": "unique extremely high"},
	"0 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique extremely high"},
	"0 Rawhide Tower Shield": {"base": "Rawhide Tower Shield", "type": "unique extremely high"},
	"0 Ruby Ring": {"base": "Ruby Ring", "type": "unique extremely high"},
	"0 Slink Boots": {"base": "Slink Boots", "type": "unique extremely high"},
	"0 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique extremely high"},
	"0 Titan Greaves": {"base": "Titan Greaves", "type": "unique extremely high"},
	"0 Turquoise Amulet": {"base": "Turquoise Amulet", "type": "unique extremely high"},
	"0 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique extremely high"},
	"0 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique extremely high"},
	"0 Vile Staff": {"base": "Vile Staff", "type": "unique extremely high"},
	"1 Basket Rapier": {"base": "Basket Rapier", "type": "unique very high"},
	"1 Bone Armour": {"base": "Bone Armour", "type": "unique very high"},
	"1 Broadhead Arrow Quiver": {"base": "Broadhead Arrow Quiver", "type": "unique very high"},
	"1 Bronzescale Boots": {"base": "Bronzescale Boots", "type": "unique very high"},
	"1 Bronzescale Gauntlets": {"base": "Bronzescale Gauntlets", "type": "unique very high"},
	"1 Burnished Spiked Shield": {"base": "Burnished Spiked Shield", "type": "unique very high"},
	"1 Chiming Spirit Shield": {"base": "Chiming Spirit Shield", "type": "unique very high"},
	"1 Clasped Boots": {"base": "Clasped Boots", "type": "unique very high"},
	"1 Close Helmet": {"base": "Close Helmet", "type": "unique very high"},
	"1 Coiled Staff": {"base": "Coiled Staff", "type": "unique very high"},
	"1 Conjurer Boots": {"base": "Conjurer Boots", "type": "unique very high"},
	"1 Conjurer Gloves": {"base": "Conjurer Gloves", "type": "unique very high"},
	"1 Corsair Sword": {"base": "Corsair Sword", "type": "unique very high"},
	"1 Crusader Plate": {"base": "Crusader Plate", "type": "unique very high"},
	"1 Death Bow": {"base": "Death Bow", "type": "unique very high"},
	"1 Deerskin Gloves": {"base": "Deerskin Gloves", "type": "unique very high"},
	"1 Diamond Ring": {"base": "Diamond Ring", "type": "unique very high"},
	"1 Dunes Map": {"base": "Dunes Map", "type": "unique very high"},
	"1 Ezomyte Axe": {"base": "Ezomyte Axe", "type": "unique very high"},
	"1 Gladius": {"base": "Gladius", "type": "unique very high"},
	"1 Goathide Gloves": {"base": "Goathide Gloves", "type": "unique very high"},
	"1 Granite Flask": {"base": "Granite Flask", "type": "unique very high"},
	"1 Greater Mana Flask": {"base": "Greater Mana Flask", "type": "unique very high"},
	"1 Imperial Bow": {"base": "Imperial Bow", "type": "unique very high"},
	"1 Imperial Skean": {"base": "Imperial Skean", "type": "unique very high"},
	"1 Imperial Staff": {"base": "Imperial Staff", "type": "unique very high"},
	"1 Iron Gauntlets": {"base": "Iron Gauntlets", "type": "unique very high"},
	"1 Iron Ring": {"base": "Iron Ring", "type": "unique very high"},
	"1 Ironscale Boots": {"base": "Ironscale Boots", "type": "unique very high"},
	"1 Lacquered Helmet": {"base": "Lacquered Helmet", "type": "unique very high"},
	"1 Large Hybrid Flask": {"base": "Large Hybrid Flask", "type": "unique very high"},
	"1 Lathi": {"base": "Lathi", "type": "unique very high"},
	"1 Leather Cap": {"base": "Leather Cap", "type": "unique very high"},
	"1 Maelström Staff": {"base": "Maelström Staff", "type": "unique very high"},
	"1 Marble Amulet": {"base": "Marble Amulet", "type": "unique very high"},
	"1 Midnight Blade": {"base": "Midnight Blade", "type": "unique very high"},
	"1 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique very high"},
	"1 Nubuck Boots": {"base": "Nubuck Boots", "type": "unique very high"},
	"1 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique very high"},
	"1 Opal Sceptre": {"base": "Opal Sceptre", "type": "unique very high"},
	"1 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique very high"},
	"1 Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "type": "unique very high"},
	"1 Platinum Kris": {"base": "Platinum Kris", "type": "unique very high"},
	"1 Prismatic Ring": {"base": "Prismatic Ring", "type": "unique very high"},
	"1 Quartz Flask": {"base": "Quartz Flask", "type": "unique very high"},
	"1 Reinforced Greaves": {"base": "Reinforced Greaves", "type": "unique very high"},
	"1 Riveted Boots": {"base": "Riveted Boots", "type": "unique very high"},
	"1 Rock Breaker": {"base": "Rock Breaker", "type": "unique very high"},
	"1 Royal Skean": {"base": "Royal Skean", "type": "unique very high"},
	"1 Ruby Flask": {"base": "Ruby Flask", "type": "unique very high"},
	"1 Sage Wand": {"base": "Sage Wand", "type": "unique very high"},
	"1 Samite Gloves": {"base": "Samite Gloves", "type": "unique very high"},
	"1 Shackled Boots": {"base": "Shackled Boots", "type": "unique very high"},
	"1 Shore Map": {"base": "Shore Map", "type": "unique very high"},
	"1 Silk Slippers": {"base": "Silk Slippers", "type": "unique very high"},
	"1 Sinner Tricorne": {"base": "Sinner Tricorne", "type": "unique very high"},
	"1 Soldier Gloves": {"base": "Soldier Gloves", "type": "unique very high"},
	"1 Spidersilk Robe": {"base": "Spidersilk Robe", "type": "unique very high"},
	"1 Spike-Point Arrow Quiver": {"base": "Spike-Point Arrow Quiver", "type": "unique very high"},
	"1 Spine Bow": {"base": "Spine Bow", "type": "unique very high"},
	"1 Spiraled Wand": {"base": "Spiraled Wand", "type": "unique very high"},
	"1 Stealth Boots": {"base": "Stealth Boots", "type": "unique very high"},
	"1 Strapped Mitts": {"base": "Strapped Mitts", "type": "unique very high"},
	"1 Studded Round Shield": {"base": "Studded Round Shield", "type": "unique very high"},
	"1 Throat Stabber": {"base": "Throat Stabber", "type": "unique very high"},
	"1 Tiger Sword": {"base": "Tiger Sword", "type": "unique very high"},
	"1 Titan Gauntlets": {"base": "Titan Gauntlets", "type": "unique very high"},
	"1 Topaz Ring": {"base": "Topaz Ring", "type": "unique very high"},
	"1 Triumphant Lamellar": {"base": "Triumphant Lamellar", "type": "unique very high"},
	"1 Ursine Pelt": {"base": "Ursine Pelt", "type": "unique very high"},
	"1 Vaal Axe": {"base": "Vaal Axe", "type": "unique very high"},
	"1 Vaal Pyramid Map": {"base": "Vaal Pyramid Map", "type": "unique very high"},
	"1 Vaal Regalia": {"base": "Vaal Regalia", "type": "unique very high"},
	"1 Varnished Coat": {"base": "Varnished Coat", "type": "unique very high"},
	"1 Void Sceptre": {"base": "Void Sceptre", "type": "unique very high"},
	"1 Wyrmscale Gauntlets": {"base": "Wyrmscale Gauntlets", "type": "unique very high"},
	"2 Basket Rapier": {"base": "Basket Rapier", "type": "unique high"},
	"2 Bone Armour": {"base": "Bone Armour", "type": "unique high"},
	"2 Broadhead Arrow Quiver": {"base": "Broadhead Arrow Quiver", "type": "unique high"},
	"2 Bronzescale Boots": {"base": "Bronzescale Boots", "type": "unique high"},
	"2 Bronzescale Gauntlets": {"base": "Bronzescale Gauntlets", "type": "unique high"},
	"2 Burnished Spiked Shield": {"base": "Burnished Spiked Shield", "type": "unique high"},
	"2 Chiming Spirit Shield": {"base": "Chiming Spirit Shield", "type": "unique high"},
	"2 Clasped Boots": {"base": "Clasped Boots", "type": "unique high"},
	"2 Close Helmet": {"base": "Close Helmet", "type": "unique high"},
	"2 Coiled Staff": {"base": "Coiled Staff", "type": "unique high"},
	"2 Conjurer Boots": {"base": "Conjurer Boots", "type": "unique high"},
	"2 Conjurer Gloves": {"base": "Conjurer Gloves", "type": "unique high"},
	"2 Corsair Sword": {"base": "Corsair Sword", "type": "unique high"},
	"2 Crusader Plate": {"base": "Crusader Plate", "type": "unique high"},
	"2 Death Bow": {"base": "Death Bow", "type": "unique high"},
	"2 Deerskin Gloves": {"base": "Deerskin Gloves", "type": "unique high"},
	"2 Diamond Ring": {"base": "Diamond Ring", "type": "unique high"},
	"2 Dunes Map": {"base": "Dunes Map", "type": "unique high"},
	"2 Ezomyte Axe": {"base": "Ezomyte Axe", "type": "unique high"},
	"2 Gladius": {"base": "Gladius", "type": "unique high"},
	"2 Goathide Gloves": {"base": "Goathide Gloves", "type": "unique high"},
	"2 Granite Flask": {"base": "Granite Flask", "type": "unique high"},
	"2 Greater Mana Flask": {"base": "Greater Mana Flask", "type": "unique high"},
	"2 Imperial Bow": {"base": "Imperial Bow", "type": "unique high"},
	"2 Imperial Skean": {"base": "Imperial Skean", "type": "unique high"},
	"2 Imperial Staff": {"base": "Imperial Staff", "type": "unique high"},
	"2 Iron Gauntlets": {"base": "Iron Gauntlets", "type": "unique high"},
	"2 Iron Ring": {"base": "Iron Ring", "type": "unique high"},
	"2 Ironscale Boots": {"base": "Ironscale Boots", "type": "unique high"},
	"2 Lacquered Helmet": {"base": "Lacquered Helmet", "type": "unique high"},
	"2 Large Hybrid Flask": {"base": "Large Hybrid Flask", "type": "unique high"},
	"2 Lathi": {"base": "Lathi", "type": "unique high"},
	"2 Leather Cap": {"base": "Leather Cap", "type": "unique high"},
	"2 Maelström Staff": {"base": "Maelström Staff", "type": "unique high"},
	"2 Marble Amulet": {"base": "Marble Amulet", "type": "unique high"},
	"2 Midnight Blade": {"base": "Midnight Blade", "type": "unique high"},
	"2 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique high"},
	"2 Nubuck Boots": {"base": "Nubuck Boots", "type": "unique high"},
	"2 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique high"},
	"2 Opal Sceptre": {"base": "Opal Sceptre", "type": "unique high"},
	"2 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique high"},
	"2 Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "type": "unique high"},
	"2 Platinum Kris": {"base": "Platinum Kris", "type": "unique high"},
	"2 Prismatic Ring": {"base": "Prismatic Ring", "type": "unique high"},
	"2 Quartz Flask": {"base": "Quartz Flask", "type": "unique high"},
	"2 Reinforced Greaves": {"base": "Reinforced Greaves", "type": "unique high"},
	"2 Riveted Boots": {"base": "Riveted Boots", "type": "unique high"},
	"2 Rock Breaker": {"base": "Rock Breaker", "type": "unique high"},
	"2 Royal Skean": {"base": "Royal Skean", "type": "unique high"},
	"2 Ruby Flask": {"base": "Ruby Flask", "type": "unique high"},
	"2 Sage Wand": {"base": "Sage Wand", "type": "unique high"},
	"2 Samite Gloves": {"base": "Samite Gloves", "type": "unique high"},
	"2 Shackled Boots": {"base": "Shackled Boots", "type": "unique high"},
	"2 Shore Map": {"base": "Shore Map", "type": "unique high"},
	"2 Silk Slippers": {"base": "Silk Slippers", "type": "unique high"},
	"2 Sinner Tricorne": {"base": "Sinner Tricorne", "type": "unique high"},
	"2 Soldier Gloves": {"base": "Soldier Gloves", "type": "unique high"},
	"2 Spidersilk Robe": {"base": "Spidersilk Robe", "type": "unique high"},
	"2 Spike-Point Arrow Quiver": {"base": "Spike-Point Arrow Quiver", "type": "unique high"},
	"2 Spine Bow": {"base": "Spine Bow", "type": "unique high"},
	"2 Spiraled Wand": {"base": "Spiraled Wand", "type": "unique high"},
	"2 Stealth Boots": {"base": "Stealth Boots", "type": "unique high"},
	"2 Strapped Mitts": {"base": "Strapped Mitts", "type": "unique high"},
	"2 Studded Round Shield": {"base": "Studded Round Shield", "type": "unique high"},
	"2 Throat Stabber": {"base": "Throat Stabber", "type": "unique high"},
	"2 Tiger Sword": {"base": "Tiger Sword", "type": "unique high"},
	"2 Titan Gauntlets": {"base": "Titan Gauntlets", "type": "unique high"},
	"2 Topaz Ring": {"base": "Topaz Ring", "type": "unique high"},
	"2 Triumphant Lamellar": {"base": "Triumphant Lamellar", "type": "unique high"},
	"2 Ursine Pelt": {"base": "Ursine Pelt", "type": "unique high"},
	"2 Vaal Axe": {"base": "Vaal Axe", "type": "unique high"},
	"2 Vaal Pyramid Map": {"base": "Vaal Pyramid Map", "type": "unique high"},
	"2 Vaal Regalia": {"base": "Vaal Regalia", "type": "unique high"},
	"2 Varnished Coat": {"base": "Varnished Coat", "type": "unique high"},
	"2 Void Sceptre": {"base": "Void Sceptre", "type": "unique high"},
	"2 Wyrmscale Gauntlets": {"base": "Wyrmscale Gauntlets", "type": "unique high"},
	"6 Amber Amulet": {"base": "Amber Amulet", "type": "unique special"},
	"6 Chain Belt": {"base": "Chain Belt", "type": "unique special"},
	"6 Cloth Belt": {"base": "Cloth Belt", "type": "unique special"},
	"6 Cobalt Jewel": {"base": "Cobalt Jewel", "type": "unique special"},
	"6 Coral Ring": {"base": "Coral Ring", "type": "unique special"},
	"6 Crimson Jewel": {"base": "Crimson Jewel", "type": "unique special"},
	"6 Gold Amulet": {"base": "Gold Amulet", "type": "unique special"},
	"6 Gold Ring": {"base": "Gold Ring", "type": "unique special"},
	"6 Great Crown": {"base": "Great Crown", "type": "unique special"},
	"6 Heavy Belt": {"base": "Heavy Belt", "type": "unique special"},
	"6 Iron Staff": {"base": "Iron Staff", "type": "unique special"},
	"6 Lapis Amulet": {"base": "Lapis Amulet", "type": "unique special"},
	"6 Leather Belt": {"base": "Leather Belt", "type": "unique special"},
	"6 Paua Amulet": {"base": "Paua Amulet", "type": "unique special"},
	"6 Paua Ring": {"base": "Paua Ring", "type": "unique special"},
	"6 Prophet Crown": {"base": "Prophet Crown", "type": "unique special"},
	"6 Rustic Sash": {"base": "Rustic Sash", "type": "unique special"},
	"6 Sapphire Ring": {"base": "Sapphire Ring", "type": "unique special"},
	"6 Shadow Sceptre": {"base": "Shadow Sceptre", "type": "unique special"},
	"6 Unset Ring": {"base": "Unset Ring", "type": "unique special"},
	"6 Viridian Jewel": {"base": "Viridian Jewel", "type": "unique special"},
	"7 Chain Gloves": {"base": "Chain Gloves", "type": "unique low"},
	"7 Compound Spiked Shield": {"base": "Compound Spiked Shield", "type": "unique low"},
	"7 Scholar's Robe": {"base": "Scholar's Robe", "type": "unique low"},
	"9 Other uniques": {"type": "unique normal"}
}
