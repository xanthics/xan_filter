#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 03/07/2018(m/d/y) 08:06:05 UTC from "tmphardcore" data

desc = "Unique"

# Base type : settings pair
items = {
	"0 Assassin's Boots": {"base": "Assassin's Boots", "type": "unique very high"},
	"0 Cardinal Round Shield": {"base": "Cardinal Round Shield", "type": "unique very high"},
	"0 Carnal Sceptre": {"base": "Carnal Sceptre", "type": "unique very high"},
	"0 Crusader Boots": {"base": "Crusader Boots", "type": "unique very high"},
	"0 Deicide Mask": {"base": "Deicide Mask", "type": "unique very high"},
	"0 Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "type": "unique very high"},
	"0 Full Wyrmscale": {"base": "Full Wyrmscale", "type": "unique very high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"0 Grand Mana Flask": {"base": "Grand Mana Flask", "type": "unique very high"},
	"0 Hydrascale Gauntlets": {"base": "Hydrascale Gauntlets", "type": "unique very high"},
	"0 Imperial Maul": {"base": "Imperial Maul", "type": "unique very high"},
	"0 Moon Temple Map": {"base": "Moon Temple Map", "type": "unique very high"},
	"0 Museum Map": {"base": "Museum Map", "type": "unique very high"},
	"0 Necromancer Silks": {"base": "Necromancer Silks", "type": "unique very high"},
	"0 Nubuck Gloves": {"base": "Nubuck Gloves", "type": "unique very high"},
	"0 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique very high"},
	"0 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique very high"},
	"0 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique very high"},
	"0 Rawhide Tower Shield": {"base": "Rawhide Tower Shield", "type": "unique very high"},
	"0 Ruby Amulet": {"base": "Ruby Amulet", "type": "unique very high"},
	"0 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "unique very high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique very high"},
	"0 Siege Axe": {"base": "Siege Axe", "type": "unique very high"},
	"0 Void Axe": {"base": "Void Axe", "type": "unique very high"},
	"1 Abyssal Axe": {"base": "Abyssal Axe", "type": "unique high"},
	"1 Arcanist Gloves": {"base": "Arcanist Gloves", "type": "unique high"},
	"1 Blood Raiment": {"base": "Blood Raiment", "type": "unique high"},
	"1 Blue Pearl Amulet": {"base": "Blue Pearl Amulet", "type": "unique high"},
	"1 Bone Crypt Map": {"base": "Bone Crypt Map", "type": "unique high"},
	"1 Cemetery Map": {"base": "Cemetery Map", "type": "unique high"},
	"1 Champion Kite Shield": {"base": "Champion Kite Shield", "type": "unique high"},
	"1 Close Helmet": {"base": "Close Helmet", "type": "unique high"},
	"1 Coronal Leather": {"base": "Coronal Leather", "type": "unique high"},
	"1 Corsair Sword": {"base": "Corsair Sword", "type": "unique high"},
	"1 Courtyard Map": {"base": "Courtyard Map", "type": "unique high"},
	"1 Cursed Crypt Map": {"base": "Cursed Crypt Map", "type": "unique high"},
	"1 Demon Dagger": {"base": "Demon Dagger", "type": "unique high"},
	"1 Destiny Leather": {"base": "Destiny Leather", "type": "unique high"},
	"1 Exquisite Leather": {"base": "Exquisite Leather", "type": "unique high"},
	"1 Granite Flask": {"base": "Granite Flask", "type": "unique high"},
	"1 Highborn Staff": {"base": "Highborn Staff", "type": "unique high"},
	"1 Hydrascale Boots": {"base": "Hydrascale Boots", "type": "unique high"},
	"1 Jewelled Foil": {"base": "Jewelled Foil", "type": "unique high"},
	"1 Karui Sceptre": {"base": "Karui Sceptre", "type": "unique high"},
	"1 Leather Cap": {"base": "Leather Cap", "type": "unique high"},
	"1 Magistrate Crown": {"base": "Magistrate Crown", "type": "unique high"},
	"1 Meatgrinder": {"base": "Meatgrinder", "type": "unique high"},
	"1 Midnight Blade": {"base": "Midnight Blade", "type": "unique high"},
	"1 Opal Ring": {"base": "Opal Ring", "type": "unique high"},
	"1 Overgrown Shrine Map": {"base": "Overgrown Shrine Map", "type": "unique high"},
	"1 Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "type": "unique high"},
	"1 Raven Mask": {"base": "Raven Mask", "type": "unique high"},
	"1 Reef Map": {"base": "Reef Map", "type": "unique high"},
	"1 Ritual Sceptre": {"base": "Ritual Sceptre", "type": "unique high"},
	"1 Ruby Flask": {"base": "Ruby Flask", "type": "unique high"},
	"1 Serpentscale Gauntlets": {"base": "Serpentscale Gauntlets", "type": "unique high"},
	"1 Sorcerer Gloves": {"base": "Sorcerer Gloves", "type": "unique high"},
	"1 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique high"},
	"1 Temple Map": {"base": "Temple Map", "type": "unique high"},
	"1 Thorium Spirit Shield": {"base": "Thorium Spirit Shield", "type": "unique high"},
	"1 Titan Greaves": {"base": "Titan Greaves", "type": "unique high"},
	"1 Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "type": "unique high"},
	"1 Topaz Flask": {"base": "Topaz Flask", "type": "unique high"},
	"1 Torture Chamber Map": {"base": "Torture Chamber Map", "type": "unique high"},
	"1 Underground River Map": {"base": "Underground River Map", "type": "unique high"},
	"1 Vaal Mask": {"base": "Vaal Mask", "type": "unique high"},
	"1 Vaal Pyramid Map": {"base": "Vaal Pyramid Map", "type": "unique high"},
	"1 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique high"},
	"1 Vanguard Belt": {"base": "Vanguard Belt", "type": "unique high"},
	"1 Varnished Coat": {"base": "Varnished Coat", "type": "unique high"},
	"1 Wyrmscale Doublet": {"base": "Wyrmscale Doublet", "type": "unique high"},
	"1 Zealot Gloves": {"base": "Zealot Gloves", "type": "unique high"},
	"6 Agate Amulet": {"base": "Agate Amulet", "type": "unique special"},
	"6 Amber Amulet": {"base": "Amber Amulet", "type": "unique special"},
	"6 Carnal Armour": {"base": "Carnal Armour", "type": "unique special"},
	"6 Carnal Mitts": {"base": "Carnal Mitts", "type": "unique special"},
	"6 Carved Wand": {"base": "Carved Wand", "type": "unique special"},
	"6 Chain Belt": {"base": "Chain Belt", "type": "unique special"},
	"6 Citrine Amulet": {"base": "Citrine Amulet", "type": "unique special"},
	"6 Cleaver": {"base": "Cleaver", "type": "unique special"},
	"6 Cobalt Jewel": {"base": "Cobalt Jewel", "type": "unique special"},
	"6 Coral Amulet": {"base": "Coral Amulet", "type": "unique special"},
	"6 Coral Ring": {"base": "Coral Ring", "type": "unique special"},
	"6 Crimson Jewel": {"base": "Crimson Jewel", "type": "unique special"},
	"6 Death Bow": {"base": "Death Bow", "type": "unique special"},
	"6 Diamond Ring": {"base": "Diamond Ring", "type": "unique special"},
	"6 Ebony Tower Shield": {"base": "Ebony Tower Shield", "type": "unique special"},
	"6 Eternal Sword": {"base": "Eternal Sword", "type": "unique special"},
	"6 Fire Arrow Quiver": {"base": "Fire Arrow Quiver", "type": "unique special"},
	"6 Gavel": {"base": "Gavel", "type": "unique special"},
	"6 Gilded Sallet": {"base": "Gilded Sallet", "type": "unique special"},
	"6 Gnarled Branch": {"base": "Gnarled Branch", "type": "unique special"},
	"6 Goathide Boots": {"base": "Goathide Boots", "type": "unique special"},
	"6 Goathide Gloves": {"base": "Goathide Gloves", "type": "unique special"},
	"6 Gold Amulet": {"base": "Gold Amulet", "type": "unique special"},
	"6 Gold Ring": {"base": "Gold Ring", "type": "unique special"},
	"6 Golden Plate": {"base": "Golden Plate", "type": "unique special"},
	"6 Goliath Greaves": {"base": "Goliath Greaves", "type": "unique special"},
	"6 Great Crown": {"base": "Great Crown", "type": "unique special"},
	"6 Great Mallet": {"base": "Great Mallet", "type": "unique special"},
	"6 Harbinger Bow": {"base": "Harbinger Bow", "type": "unique special"},
	"6 Harlequin Mask": {"base": "Harlequin Mask", "type": "unique special"},
	"6 Hubris Circlet": {"base": "Hubris Circlet", "type": "unique special"},
	"6 Imperial Bow": {"base": "Imperial Bow", "type": "unique special"},
	"6 Imperial Claw": {"base": "Imperial Claw", "type": "unique special"},
	"6 Imperial Skean": {"base": "Imperial Skean", "type": "unique special"},
	"6 Infernal Sword": {"base": "Infernal Sword", "type": "unique special"},
	"6 Iron Circlet": {"base": "Iron Circlet", "type": "unique special"},
	"6 Iron Ring": {"base": "Iron Ring", "type": "unique special"},
	"6 Jade Amulet": {"base": "Jade Amulet", "type": "unique special"},
	"6 Jade Hatchet": {"base": "Jade Hatchet", "type": "unique special"},
	"6 Jagged Maul": {"base": "Jagged Maul", "type": "unique special"},
	"6 Judgement Staff": {"base": "Judgement Staff", "type": "unique special"},
	"6 Lacquered Garb": {"base": "Lacquered Garb", "type": "unique special"},
	"6 Lapis Amulet": {"base": "Lapis Amulet", "type": "unique special"},
	"6 Leather Belt": {"base": "Leather Belt", "type": "unique special"},
	"6 Leather Hood": {"base": "Leather Hood", "type": "unique special"},
	"6 Long Bow": {"base": "Long Bow", "type": "unique special"},
	"6 Mind Cage": {"base": "Mind Cage", "type": "unique special"},
	"6 Moonstone Ring": {"base": "Moonstone Ring", "type": "unique special"},
	"6 Murder Boots": {"base": "Murder Boots", "type": "unique special"},
	"6 Necromancer Circlet": {"base": "Necromancer Circlet", "type": "unique special"},
	"6 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique special"},
	"6 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique special"},
	"6 Ornate Sword": {"base": "Ornate Sword", "type": "unique special"},
	"6 Paua Ring": {"base": "Paua Ring", "type": "unique special"},
	"6 Plank Kite Shield": {"base": "Plank Kite Shield", "type": "unique special"},
	"6 Plate Vest": {"base": "Plate Vest", "type": "unique special"},
	"6 Praetor Crown": {"base": "Praetor Crown", "type": "unique special"},
	"6 Prismatic Ring": {"base": "Prismatic Ring", "type": "unique special"},
	"6 Prophet Crown": {"base": "Prophet Crown", "type": "unique special"},
	"6 Royal Bow": {"base": "Royal Bow", "type": "unique special"},
	"6 Royal Staff": {"base": "Royal Staff", "type": "unique special"},
	"6 Rusted Sword": {"base": "Rusted Sword", "type": "unique special"},
	"6 Rustic Sash": {"base": "Rustic Sash", "type": "unique special"},
	"6 Sage Wand": {"base": "Sage Wand", "type": "unique special"},
	"6 Sharktooth Arrow Quiver": {"base": "Sharktooth Arrow Quiver", "type": "unique special"},
	"6 Skinning Knife": {"base": "Skinning Knife", "type": "unique special"},
	"6 Soldier Gloves": {"base": "Soldier Gloves", "type": "unique special"},
	"6 Spine Bow": {"base": "Spine Bow", "type": "unique special"},
	"6 Stealth Boots": {"base": "Stealth Boots", "type": "unique special"},
	"6 Steelscale Gauntlets": {"base": "Steelscale Gauntlets", "type": "unique special"},
	"6 Studded Belt": {"base": "Studded Belt", "type": "unique special"},
	"6 Terror Claw": {"base": "Terror Claw", "type": "unique special"},
	"6 Titan Gauntlets": {"base": "Titan Gauntlets", "type": "unique special"},
	"6 Tornado Wand": {"base": "Tornado Wand", "type": "unique special"},
	"6 Two-Point Arrow Quiver": {"base": "Two-Point Arrow Quiver", "type": "unique special"},
	"6 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique special"},
	"6 Unset Ring": {"base": "Unset Ring", "type": "unique special"},
	"6 Vaal Axe": {"base": "Vaal Axe", "type": "unique special"},
	"6 Vaal Blade": {"base": "Vaal Blade", "type": "unique special"},
	"6 Vaal Gauntlets": {"base": "Vaal Gauntlets", "type": "unique special"},
	"6 Viridian Jewel": {"base": "Viridian Jewel", "type": "unique special"},
	"6 War Hammer": {"base": "War Hammer", "type": "unique special"},
	"6 Widowsilk Robe": {"base": "Widowsilk Robe", "type": "unique special"},
	"6 Woodsplitter": {"base": "Woodsplitter", "type": "unique special"},
	"7 Ambusher": {"base": "Ambusher", "type": "unique low"},
	"7 Amethyst Ring": {"base": "Amethyst Ring", "type": "unique low"},
	"7 Assassin Bow": {"base": "Assassin Bow", "type": "unique low"},
	"7 Assassin's Mitts": {"base": "Assassin's Mitts", "type": "unique low"},
	"7 Awl": {"base": "Awl", "type": "unique low"},
	"7 Baroque Round Shield": {"base": "Baroque Round Shield", "type": "unique low"},
	"7 Bastard Sword": {"base": "Bastard Sword", "type": "unique low"},
	"7 Blunt Arrow Quiver": {"base": "Blunt Arrow Quiver", "type": "unique low"},
	"7 Bone Circlet": {"base": "Bone Circlet", "type": "unique low"},
	"7 Boot Blade": {"base": "Boot Blade", "type": "unique low"},
	"7 Boot Knife": {"base": "Boot Knife", "type": "unique low"},
	"7 Brass Maul": {"base": "Brass Maul", "type": "unique low"},
	"7 Broadhead Arrow Quiver": {"base": "Broadhead Arrow Quiver", "type": "unique low"},
	"7 Bronze Gauntlets": {"base": "Bronze Gauntlets", "type": "unique low"},
	"7 Bronzescale Boots": {"base": "Bronzescale Boots", "type": "unique low"},
	"7 Bronzescale Gauntlets": {"base": "Bronzescale Gauntlets", "type": "unique low"},
	"7 Buckskin Tunic": {"base": "Buckskin Tunic", "type": "unique low"},
	"7 Burnished Spiked Shield": {"base": "Burnished Spiked Shield", "type": "unique low"},
	"7 Chain Gloves": {"base": "Chain Gloves", "type": "unique low"},
	"7 Clasped Boots": {"base": "Clasped Boots", "type": "unique low"},
	"7 Cloth Belt": {"base": "Cloth Belt", "type": "unique low"},
	"7 Compound Spiked Shield": {"base": "Compound Spiked Shield", "type": "unique low"},
	"7 Conjurer Gloves": {"base": "Conjurer Gloves", "type": "unique low"},
	"7 Conquest Chainmail": {"base": "Conquest Chainmail", "type": "unique low"},
	"7 Copper Plate": {"base": "Copper Plate", "type": "unique low"},
	"7 Crude Bow": {"base": "Crude Bow", "type": "unique low"},
	"7 Crusader Plate": {"base": "Crusader Plate", "type": "unique low"},
	"7 Crystal Wand": {"base": "Crystal Wand", "type": "unique low"},
	"7 Cutthroat's Garb": {"base": "Cutthroat's Garb", "type": "unique low"},
	"7 Decimation Bow": {"base": "Decimation Bow", "type": "unique low"},
	"7 Deerskin Boots": {"base": "Deerskin Boots", "type": "unique low"},
	"7 Deerskin Gloves": {"base": "Deerskin Gloves", "type": "unique low"},
	"7 Demon's Horn": {"base": "Demon's Horn", "type": "unique low"},
	"7 Despot Axe": {"base": "Despot Axe", "type": "unique low"},
	"7 Diamond Flask": {"base": "Diamond Flask", "type": "unique low"},
	"7 Dragonscale Boots": {"base": "Dragonscale Boots", "type": "unique low"},
	"7 Dragonscale Gauntlets": {"base": "Dragonscale Gauntlets", "type": "unique low"},
	"7 Dread Maul": {"base": "Dread Maul", "type": "unique low"},
	"7 Dream Mace": {"base": "Dream Mace", "type": "unique low"},
	"7 Elegant Sword": {"base": "Elegant Sword", "type": "unique low"},
	"7 Estoc": {"base": "Estoc", "type": "unique low"},
	"7 Ezomyte Staff": {"base": "Ezomyte Staff", "type": "unique low"},
	"7 Fiend Dagger": {"base": "Fiend Dagger", "type": "unique low"},
	"7 Flaying Knife": {"base": "Flaying Knife", "type": "unique low"},
	"7 Full Dragonscale": {"base": "Full Dragonscale", "type": "unique low"},
	"7 Goat's Horn": {"base": "Goat's Horn", "type": "unique low"},
	"7 Golden Buckler": {"base": "Golden Buckler", "type": "unique low"},
	"7 Golden Mask": {"base": "Golden Mask", "type": "unique low"},
	"7 Goliath Gauntlets": {"base": "Goliath Gauntlets", "type": "unique low"},
	"7 Great Helmet": {"base": "Great Helmet", "type": "unique low"},
	"7 Greater Mana Flask": {"base": "Greater Mana Flask", "type": "unique low"},
	"7 Harmonic Spirit Shield": {"base": "Harmonic Spirit Shield", "type": "unique low"},
	"7 Highland Blade": {"base": "Highland Blade", "type": "unique low"},
	"7 Holy Chainmail": {"base": "Holy Chainmail", "type": "unique low"},
	"7 Imbued Wand": {"base": "Imbued Wand", "type": "unique low"},
	"7 Iron Hat": {"base": "Iron Hat", "type": "unique low"},
	"7 Iron Mask": {"base": "Iron Mask", "type": "unique low"},
	"7 Iron Staff": {"base": "Iron Staff", "type": "unique low"},
	"7 Ironscale Boots": {"base": "Ironscale Boots", "type": "unique low"},
	"7 Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "type": "unique low"},
	"7 Ivory Spirit Shield": {"base": "Ivory Spirit Shield", "type": "unique low"},
	"7 Jagged Foil": {"base": "Jagged Foil", "type": "unique low"},
	"7 Karui Maul": {"base": "Karui Maul", "type": "unique low"},
	"7 Lacquered Helmet": {"base": "Lacquered Helmet", "type": "unique low"},
	"7 Latticed Ringmail": {"base": "Latticed Ringmail", "type": "unique low"},
	"7 Legion Boots": {"base": "Legion Boots", "type": "unique low"},
	"7 Long Staff": {"base": "Long Staff", "type": "unique low"},
	"7 Lunaris Circlet": {"base": "Lunaris Circlet", "type": "unique low"},
	"7 Mesh Boots": {"base": "Mesh Boots", "type": "unique low"},
	"7 Military Staff": {"base": "Military Staff", "type": "unique low"},
	"7 Nailed Fist": {"base": "Nailed Fist", "type": "unique low"},
	"7 Ornate Mace": {"base": "Ornate Mace", "type": "unique low"},
	"7 Ornate Ringmail": {"base": "Ornate Ringmail", "type": "unique low"},
	"7 Painted Buckler": {"base": "Painted Buckler", "type": "unique low"},
	"7 Paua Amulet": {"base": "Paua Amulet", "type": "unique low"},
	"7 Plated Greaves": {"base": "Plated Greaves", "type": "unique low"},
	"7 Platinum Kris": {"base": "Platinum Kris", "type": "unique low"},
	"7 Poleaxe": {"base": "Poleaxe", "type": "unique low"},
	"7 Primordial Staff": {"base": "Primordial Staff", "type": "unique low"},
	"7 Quartz Flask": {"base": "Quartz Flask", "type": "unique low"},
	"7 Quartz Wand": {"base": "Quartz Wand", "type": "unique low"},
	"7 Quicksilver Flask": {"base": "Quicksilver Flask", "type": "unique low"},
	"7 Reaver Sword": {"base": "Reaver Sword", "type": "unique low"},
	"7 Recurve Bow": {"base": "Recurve Bow", "type": "unique low"},
	"7 Riveted Boots": {"base": "Riveted Boots", "type": "unique low"},
	"7 Rotted Round Shield": {"base": "Rotted Round Shield", "type": "unique low"},
	"7 Ruby Ring": {"base": "Ruby Ring", "type": "unique low"},
	"7 Sage's Robe": {"base": "Sage's Robe", "type": "unique low"},
	"7 Samite Gloves": {"base": "Samite Gloves", "type": "unique low"},
	"7 Samite Helmet": {"base": "Samite Helmet", "type": "unique low"},
	"7 Scholar Boots": {"base": "Scholar Boots", "type": "unique low"},
	"7 Scholar's Robe": {"base": "Scholar's Robe", "type": "unique low"},
	"7 Sentinel Jacket": {"base": "Sentinel Jacket", "type": "unique low"},
	"7 Serpentine Staff": {"base": "Serpentine Staff", "type": "unique low"},
	"7 Serpentscale Boots": {"base": "Serpentscale Boots", "type": "unique low"},
	"7 Serrated Arrow Quiver": {"base": "Serrated Arrow Quiver", "type": "unique low"},
	"7 Shadow Sceptre": {"base": "Shadow Sceptre", "type": "unique low"},
	"7 Shagreen Boots": {"base": "Shagreen Boots", "type": "unique low"},
	"7 Sharkskin Boots": {"base": "Sharkskin Boots", "type": "unique low"},
	"7 Short Bow": {"base": "Short Bow", "type": "unique low"},
	"7 Silk Gloves": {"base": "Silk Gloves", "type": "unique low"},
	"7 Simple Robe": {"base": "Simple Robe", "type": "unique low"},
	"7 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique low"},
	"7 Sledgehammer": {"base": "Sledgehammer", "type": "unique low"},
	"7 Soldier Boots": {"base": "Soldier Boots", "type": "unique low"},
	"7 Soldier Helmet": {"base": "Soldier Helmet", "type": "unique low"},
	"7 Spidersilk Robe": {"base": "Spidersilk Robe", "type": "unique low"},
	"7 Spiked Club": {"base": "Spiked Club", "type": "unique low"},
	"7 Stiletto": {"base": "Stiletto", "type": "unique low"},
	"7 Strapped Boots": {"base": "Strapped Boots", "type": "unique low"},
	"7 Strapped Leather": {"base": "Strapped Leather", "type": "unique low"},
	"7 Studded Round Shield": {"base": "Studded Round Shield", "type": "unique low"},
	"7 Sulphur Flask": {"base": "Sulphur Flask", "type": "unique low"},
	"7 Sundering Axe": {"base": "Sundering Axe", "type": "unique low"},
	"7 Supreme Spiked Shield": {"base": "Supreme Spiked Shield", "type": "unique low"},
	"7 Tarnished Spirit Shield": {"base": "Tarnished Spirit Shield", "type": "unique low"},
	"7 Thresher Claw": {"base": "Thresher Claw", "type": "unique low"},
	"7 Throat Stabber": {"base": "Throat Stabber", "type": "unique low"},
	"7 Timeworn Claw": {"base": "Timeworn Claw", "type": "unique low"},
	"7 Tribal Circlet": {"base": "Tribal Circlet", "type": "unique low"},
	"7 Tricorne": {"base": "Tricorne", "type": "unique low"},
	"7 Turquoise Amulet": {"base": "Turquoise Amulet", "type": "unique low"},
	"7 Vaal Buckler": {"base": "Vaal Buckler", "type": "unique low"},
	"7 Vaal Claw": {"base": "Vaal Claw", "type": "unique low"},
	"7 Velvet Gloves": {"base": "Velvet Gloves", "type": "unique low"},
	"7 Velvet Slippers": {"base": "Velvet Slippers", "type": "unique low"},
	"7 Vile Staff": {"base": "Vile Staff", "type": "unique low"},
	"7 Vine Circlet": {"base": "Vine Circlet", "type": "unique low"},
	"7 Visored Sallet": {"base": "Visored Sallet", "type": "unique low"},
	"7 War Buckler": {"base": "War Buckler", "type": "unique low"},
	"7 Wild Leather": {"base": "Wild Leather", "type": "unique low"},
	"7 Wool Gloves": {"base": "Wool Gloves", "type": "unique low"},
	"7 Wrapped Mitts": {"base": "Wrapped Mitts", "type": "unique low"},
	"7 Wyrmscale Gauntlets": {"base": "Wyrmscale Gauntlets", "type": "unique low"},
	"7 Zealot Helmet": {"base": "Zealot Helmet", "type": "unique low"},
	"9 Other uniques": {"type": "unique normal"}
}
