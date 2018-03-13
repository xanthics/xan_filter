#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 03/13/2018(m/d/y) 06:57:25 UTC from "Hardcore" data

desc = "Unique"

# Base type : settings pair
items = {
	"0 Abyssal Axe": {"base": "Abyssal Axe", "type": "unique very high"},
	"0 Ancient Gauntlets": {"base": "Ancient Gauntlets", "type": "unique very high"},
	"0 Archon Kite Shield": {"base": "Archon Kite Shield", "type": "unique very high"},
	"0 Bastard Sword": {"base": "Bastard Sword", "type": "unique very high"},
	"0 Carnal Armour": {"base": "Carnal Armour", "type": "unique very high"},
	"0 Carnal Sceptre": {"base": "Carnal Sceptre", "type": "unique very high"},
	"0 Clasped Mitts": {"base": "Clasped Mitts", "type": "unique very high"},
	"0 Close Helmet": {"base": "Close Helmet", "type": "unique very high"},
	"0 Conjurer Boots": {"base": "Conjurer Boots", "type": "unique very high"},
	"0 Crusader Gloves": {"base": "Crusader Gloves", "type": "unique very high"},
	"0 Crusader Plate": {"base": "Crusader Plate", "type": "unique very high"},
	"0 Deerskin Gloves": {"base": "Deerskin Gloves", "type": "unique very high"},
	"0 Desert Brigandine": {"base": "Desert Brigandine", "type": "unique very high"},
	"0 Destiny Leather": {"base": "Destiny Leather", "type": "unique very high"},
	"0 Diamond Flask": {"base": "Diamond Flask", "type": "unique very high"},
	"0 Elegant Foil": {"base": "Elegant Foil", "type": "unique very high"},
	"0 Etched Greatsword": {"base": "Etched Greatsword", "type": "unique very high"},
	"0 Eternal Sword": {"base": "Eternal Sword", "type": "unique very high"},
	"0 Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "type": "unique very high"},
	"0 Fire Arrow Quiver": {"base": "Fire Arrow Quiver", "type": "unique very high"},
	"0 Gavel": {"base": "Gavel", "type": "unique very high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"0 Golden Obi": {"base": "Golden Obi", "type": "unique very high"},
	"0 Golden Wreath": {"base": "Golden Wreath", "type": "unique very high"},
	"0 Goliath Gauntlets": {"base": "Goliath Gauntlets", "type": "unique very high"},
	"0 Grand Mana Flask": {"base": "Grand Mana Flask", "type": "unique very high"},
	"0 Granite Flask": {"base": "Granite Flask", "type": "unique very high"},
	"0 Imperial Maul": {"base": "Imperial Maul", "type": "unique very high"},
	"0 Judgement Staff": {"base": "Judgement Staff", "type": "unique very high"},
	"0 Large Hybrid Flask": {"base": "Large Hybrid Flask", "type": "unique very high"},
	"0 Maelström Staff": {"base": "Maelström Staff", "type": "unique very high"},
	"0 Midnight Blade": {"base": "Midnight Blade", "type": "unique very high"},
	"0 Necromancer Silks": {"base": "Necromancer Silks", "type": "unique very high"},
	"0 Praetor Crown": {"base": "Praetor Crown", "type": "unique very high"},
	"0 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique very high"},
	"0 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique very high"},
	"0 Prophet Crown": {"base": "Prophet Crown", "type": "unique very high"},
	"0 Ranger Bow": {"base": "Ranger Bow", "type": "unique very high"},
	"0 Ritual Sceptre": {"base": "Ritual Sceptre", "type": "unique very high"},
	"0 Royal Burgonet": {"base": "Royal Burgonet", "type": "unique very high"},
	"0 Shadow Axe": {"base": "Shadow Axe", "type": "unique very high"},
	"0 Sharkskin Boots": {"base": "Sharkskin Boots", "type": "unique very high"},
	"0 Siege Axe": {"base": "Siege Axe", "type": "unique very high"},
	"0 Silver Flask": {"base": "Silver Flask", "type": "unique very high"},
	"0 Sinner Tricorne": {"base": "Sinner Tricorne", "type": "unique very high"},
	"0 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique very high"},
	"0 Slink Boots": {"base": "Slink Boots", "type": "unique very high"},
	"0 Sorcerer Gloves": {"base": "Sorcerer Gloves", "type": "unique very high"},
	"0 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique very high"},
	"0 Stygian Vise": {"base": "Stygian Vise", "type": "unique very high"},
	"0 Thresher Claw": {"base": "Thresher Claw", "type": "unique very high"},
	"0 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique very high"},
	"0 Vaal Blade": {"base": "Vaal Blade", "type": "unique very high"},
	"0 Varnished Coat": {"base": "Varnished Coat", "type": "unique very high"},
	"0 Zodiac Leather": {"base": "Zodiac Leather", "type": "unique very high"},
	"1 Amber Amulet": {"base": "Amber Amulet", "type": "unique high"},
	"1 Amethyst Flask": {"base": "Amethyst Flask", "type": "unique high"},
	"1 Amethyst Ring": {"base": "Amethyst Ring", "type": "unique high"},
	"1 Assassin's Mitts": {"base": "Assassin's Mitts", "type": "unique high"},
	"1 Astral Plate": {"base": "Astral Plate", "type": "unique high"},
	"1 Aventail Helmet": {"base": "Aventail Helmet", "type": "unique high"},
	"1 Bismuth Flask": {"base": "Bismuth Flask", "type": "unique high"},
	"1 Black Maw Talisman": {"base": "Black Maw Talisman", "type": "unique high"},
	"1 Bone Bow": {"base": "Bone Bow", "type": "unique high"},
	"1 Brass Spirit Shield": {"base": "Brass Spirit Shield", "type": "unique high"},
	"1 Broadhead Arrow Quiver": {"base": "Broadhead Arrow Quiver", "type": "unique high"},
	"1 Bronze Gauntlets": {"base": "Bronze Gauntlets", "type": "unique high"},
	"1 Bronzescale Gauntlets": {"base": "Bronzescale Gauntlets", "type": "unique high"},
	"1 Carved Wand": {"base": "Carved Wand", "type": "unique high"},
	"1 Chain Belt": {"base": "Chain Belt", "type": "unique high"},
	"1 Clasped Boots": {"base": "Clasped Boots", "type": "unique high"},
	"1 Ebony Tower Shield": {"base": "Ebony Tower Shield", "type": "unique high"},
	"1 Elegant Ringmail": {"base": "Elegant Ringmail", "type": "unique high"},
	"1 Exquisite Leather": {"base": "Exquisite Leather", "type": "unique high"},
	"1 Ezomyte Blade": {"base": "Ezomyte Blade", "type": "unique high"},
	"1 Fiend Dagger": {"base": "Fiend Dagger", "type": "unique high"},
	"1 Full Dragonscale": {"base": "Full Dragonscale", "type": "unique high"},
	"1 Gold Ring": {"base": "Gold Ring", "type": "unique high"},
	"1 Great Crown": {"base": "Great Crown", "type": "unique high"},
	"1 Hallowed Hybrid Flask": {"base": "Hallowed Hybrid Flask", "type": "unique high"},
	"1 Headsman Axe": {"base": "Headsman Axe", "type": "unique high"},
	"1 Hellion's Paw": {"base": "Hellion's Paw", "type": "unique high"},
	"1 Imbued Wand": {"base": "Imbued Wand", "type": "unique high"},
	"1 Imperial Bow": {"base": "Imperial Bow", "type": "unique high"},
	"1 Imperial Claw": {"base": "Imperial Claw", "type": "unique high"},
	"1 Imperial Skean": {"base": "Imperial Skean", "type": "unique high"},
	"1 Iron Gauntlets": {"base": "Iron Gauntlets", "type": "unique high"},
	"1 Iron Ring": {"base": "Iron Ring", "type": "unique high"},
	"1 Karui Maul": {"base": "Karui Maul", "type": "unique high"},
	"1 Laminated Kite Shield": {"base": "Laminated Kite Shield", "type": "unique high"},
	"1 Leather Cap": {"base": "Leather Cap", "type": "unique high"},
	"1 Legion Boots": {"base": "Legion Boots", "type": "unique high"},
	"1 Legion Sword": {"base": "Legion Sword", "type": "unique high"},
	"1 Lion Sword": {"base": "Lion Sword", "type": "unique high"},
	"1 Lunaris Circlet": {"base": "Lunaris Circlet", "type": "unique high"},
	"1 Marble Amulet": {"base": "Marble Amulet", "type": "unique high"},
	"1 Mirrored Spiked Shield": {"base": "Mirrored Spiked Shield", "type": "unique high"},
	"1 Mosaic Kite Shield": {"base": "Mosaic Kite Shield", "type": "unique high"},
	"1 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique high"},
	"1 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique high"},
	"1 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique high"},
	"1 Platinum Sceptre": {"base": "Platinum Sceptre", "type": "unique high"},
	"1 Prismatic Ring": {"base": "Prismatic Ring", "type": "unique high"},
	"1 Quicksilver Flask": {"base": "Quicksilver Flask", "type": "unique high"},
	"1 Samite Helmet": {"base": "Samite Helmet", "type": "unique high"},
	"1 Sapphire Ring": {"base": "Sapphire Ring", "type": "unique high"},
	"1 Sentinel Jacket": {"base": "Sentinel Jacket", "type": "unique high"},
	"1 Shadow Sceptre": {"base": "Shadow Sceptre", "type": "unique high"},
	"1 Silken Hood": {"base": "Silken Hood", "type": "unique high"},
	"1 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique high"},
	"1 Spidersilk Robe": {"base": "Spidersilk Robe", "type": "unique high"},
	"1 Spine Bow": {"base": "Spine Bow", "type": "unique high"},
	"1 Steel Gauntlets": {"base": "Steel Gauntlets", "type": "unique high"},
	"1 Sulphur Flask": {"base": "Sulphur Flask", "type": "unique high"},
	"1 Sundering Axe": {"base": "Sundering Axe", "type": "unique high"},
	"1 Tarnished Spirit Shield": {"base": "Tarnished Spirit Shield", "type": "unique high"},
	"1 Tiger Sword": {"base": "Tiger Sword", "type": "unique high"},
	"1 Titan Gauntlets": {"base": "Titan Gauntlets", "type": "unique high"},
	"1 Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "type": "unique high"},
	"1 Tomahawk": {"base": "Tomahawk", "type": "unique high"},
	"1 Topaz Ring": {"base": "Topaz Ring", "type": "unique high"},
	"1 Tornado Wand": {"base": "Tornado Wand", "type": "unique high"},
	"1 Triumphant Lamellar": {"base": "Triumphant Lamellar", "type": "unique high"},
	"1 Turquoise Amulet": {"base": "Turquoise Amulet", "type": "unique high"},
	"1 Unset Ring": {"base": "Unset Ring", "type": "unique high"},
	"1 Vaal Gauntlets": {"base": "Vaal Gauntlets", "type": "unique high"},
	"1 Vaal Hatchet": {"base": "Vaal Hatchet", "type": "unique high"},
	"1 War Hammer": {"base": "War Hammer", "type": "unique high"},
	"6 Agate Amulet": {"base": "Agate Amulet", "type": "unique special"},
	"6 Assassin Bow": {"base": "Assassin Bow", "type": "unique special"},
	"6 Cobalt Jewel": {"base": "Cobalt Jewel", "type": "unique special"},
	"6 Crimson Jewel": {"base": "Crimson Jewel", "type": "unique special"},
	"6 Crude Bow": {"base": "Crude Bow", "type": "unique special"},
	"6 Crystal Sceptre": {"base": "Crystal Sceptre", "type": "unique special"},
	"6 Death Bow": {"base": "Death Bow", "type": "unique special"},
	"6 Goathide Boots": {"base": "Goathide Boots", "type": "unique special"},
	"6 Gold Amulet": {"base": "Gold Amulet", "type": "unique special"},
	"6 Heavy Belt": {"base": "Heavy Belt", "type": "unique special"},
	"6 Imperial Staff": {"base": "Imperial Staff", "type": "unique special"},
	"6 Leather Belt": {"base": "Leather Belt", "type": "unique special"},
	"6 Moonstone Ring": {"base": "Moonstone Ring", "type": "unique special"},
	"6 Plate Vest": {"base": "Plate Vest", "type": "unique special"},
	"6 Reaver Sword": {"base": "Reaver Sword", "type": "unique special"},
	"6 Ruby Ring": {"base": "Ruby Ring", "type": "unique special"},
	"6 Spike-Point Arrow Quiver": {"base": "Spike-Point Arrow Quiver", "type": "unique special"},
	"6 Stealth Boots": {"base": "Stealth Boots", "type": "unique special"},
	"6 Viridian Jewel": {"base": "Viridian Jewel", "type": "unique special"},
	"6 Woodsplitter": {"base": "Woodsplitter", "type": "unique special"},
	"7 Antique Rapier": {"base": "Antique Rapier", "type": "unique low"},
	"7 Awl": {"base": "Awl", "type": "unique low"},
	"7 Boot Knife": {"base": "Boot Knife", "type": "unique low"},
	"7 Coral Ring": {"base": "Coral Ring", "type": "unique low"},
	"7 Gnarled Branch": {"base": "Gnarled Branch", "type": "unique low"},
	"7 Goat's Horn": {"base": "Goat's Horn", "type": "unique low"},
	"7 Iron Circlet": {"base": "Iron Circlet", "type": "unique low"},
	"7 Iron Staff": {"base": "Iron Staff", "type": "unique low"},
	"7 Ironscale Boots": {"base": "Ironscale Boots", "type": "unique low"},
	"7 Lacquered Garb": {"base": "Lacquered Garb", "type": "unique low"},
	"7 Leather Hood": {"base": "Leather Hood", "type": "unique low"},
	"7 Long Bow": {"base": "Long Bow", "type": "unique low"},
	"7 Paua Ring": {"base": "Paua Ring", "type": "unique low"},
	"7 Plank Kite Shield": {"base": "Plank Kite Shield", "type": "unique low"},
	"7 Platinum Kris": {"base": "Platinum Kris", "type": "unique low"},
	"7 Recurve Bow": {"base": "Recurve Bow", "type": "unique low"},
	"7 Scholar Boots": {"base": "Scholar Boots", "type": "unique low"},
	"7 Scholar's Robe": {"base": "Scholar's Robe", "type": "unique low"},
	"7 Serpentine Staff": {"base": "Serpentine Staff", "type": "unique low"},
	"7 Serrated Arrow Quiver": {"base": "Serrated Arrow Quiver", "type": "unique low"},
	"7 Soldier Helmet": {"base": "Soldier Helmet", "type": "unique low"},
	"7 Spiked Club": {"base": "Spiked Club", "type": "unique low"},
	"7 Strapped Boots": {"base": "Strapped Boots", "type": "unique low"},
	"7 Tricorne": {"base": "Tricorne", "type": "unique low"},
	"7 Velvet Gloves": {"base": "Velvet Gloves", "type": "unique low"},
	"7 Visored Sallet": {"base": "Visored Sallet", "type": "unique low"},
	"7 Void Sceptre": {"base": "Void Sceptre", "type": "unique low"},
	"7 War Buckler": {"base": "War Buckler", "type": "unique low"},
	"7 War Sword": {"base": "War Sword", "type": "unique low"},
	"7 Wool Gloves": {"base": "Wool Gloves", "type": "unique low"},
	"7 Wrapped Mitts": {"base": "Wrapped Mitts", "type": "unique low"},
	"9 Other uniques": {"type": "unique normal"}
}
