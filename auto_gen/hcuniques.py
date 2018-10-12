#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 10/12/2018(m/d/y) 23:52:25 UTC from "Hardcore" data

desc = "Unique"

# Base type : settings pair
items = {
	"0 Blinder": {"base": "Blinder", "type": "unique extremely high"},
	"0 Callous Mask": {"base": "Callous Mask", "type": "unique extremely high"},
	"0 Callous Mask Piece": {"base": "Callous Mask Piece", "type": "unique extremely high"},
	"0 Cedar Tower Shield": {"base": "Cedar Tower Shield", "type": "unique extremely high"},
	"0 Chiming Spirit Shield": {"base": "Chiming Spirit Shield", "type": "unique extremely high"},
	"0 Cutthroat's Garb": {"base": "Cutthroat's Garb", "type": "unique extremely high"},
	"0 Deicide Mask": {"base": "Deicide Mask", "type": "unique extremely high"},
	"0 Desert Brigandine": {"base": "Desert Brigandine", "type": "unique extremely high"},
	"0 Destiny Leather": {"base": "Destiny Leather", "type": "unique extremely high"},
	"0 Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "type": "unique extremely high"},
	"0 Gladiator Plate": {"base": "Gladiator Plate", "type": "unique extremely high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique extremely high"},
	"0 Goathide Boots": {"base": "Goathide Boots", "type": "unique extremely high"},
	"0 Grand Mana Flask": {"base": "Grand Mana Flask", "type": "unique extremely high"},
	"0 Imperial Skean": {"base": "Imperial Skean", "type": "unique extremely high"},
	"0 Imperial Staff": {"base": "Imperial Staff", "type": "unique extremely high"},
	"0 Lacquered Garb": {"base": "Lacquered Garb", "type": "unique extremely high"},
	"0 Large Hybrid Flask": {"base": "Large Hybrid Flask", "type": "unique extremely high"},
	"0 Leather Hood": {"base": "Leather Hood", "type": "unique extremely high"},
	"0 Long Bow": {"base": "Long Bow", "type": "unique extremely high"},
	"0 Maelström Staff": {"base": "Maelström Staff", "type": "unique extremely high"},
	"0 Mind Cage": {"base": "Mind Cage", "type": "unique extremely high"},
	"0 Murder Boots": {"base": "Murder Boots", "type": "unique extremely high"},
	"0 Necromancer Silks": {"base": "Necromancer Silks", "type": "unique extremely high"},
	"0 Nubuck Boots": {"base": "Nubuck Boots", "type": "unique extremely high"},
	"0 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique extremely high"},
	"0 Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "type": "unique extremely high"},
	"0 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique extremely high"},
	"0 Ranger Bow": {"base": "Ranger Bow", "type": "unique extremely high"},
	"0 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique extremely high"},
	"0 Ruby Flask": {"base": "Ruby Flask", "type": "unique extremely high"},
	"0 Sadist Garb": {"base": "Sadist Garb", "type": "unique extremely high"},
	"0 Sanctified Mana Flask": {"base": "Sanctified Mana Flask", "type": "unique extremely high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique extremely high"},
	"0 Scholar Boots": {"base": "Scholar Boots", "type": "unique extremely high"},
	"0 Sharkskin Boots": {"base": "Sharkskin Boots", "type": "unique extremely high"},
	"0 Shore Map": {"base": "Shore Map", "type": "unique extremely high"},
	"0 Silken Hood": {"base": "Silken Hood", "type": "unique extremely high"},
	"0 Spike-Point Arrow Quiver": {"base": "Spike-Point Arrow Quiver", "type": "unique extremely high"},
	"0 Stealth Boots": {"base": "Stealth Boots", "type": "unique extremely high"},
	"0 Steelscale Gauntlets": {"base": "Steelscale Gauntlets", "type": "unique extremely high"},
	"0 Tornado Wand": {"base": "Tornado Wand", "type": "unique extremely high"},
	"0 Tricorne": {"base": "Tricorne", "type": "unique extremely high"},
	"0 Vaal Axe": {"base": "Vaal Axe", "type": "unique extremely high"},
	"0 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique extremely high"},
	"0 Zodiac Leather": {"base": "Zodiac Leather", "type": "unique extremely high"},
	"1 Amethyst Flask": {"base": "Amethyst Flask", "type": "unique very high"},
	"1 Ancient Greaves": {"base": "Ancient Greaves", "type": "unique very high"},
	"1 Archon Kite Shield": {"base": "Archon Kite Shield", "type": "unique very high"},
	"1 Assassin's Garb": {"base": "Assassin's Garb", "type": "unique very high"},
	"1 Astral Plate": {"base": "Astral Plate", "type": "unique very high"},
	"1 Bismuth Flask": {"base": "Bismuth Flask", "type": "unique very high"},
	"1 Citrine Amulet": {"base": "Citrine Amulet", "type": "unique very high"},
	"1 Clasped Boots": {"base": "Clasped Boots", "type": "unique very high"},
	"1 Corrugated Buckler": {"base": "Corrugated Buckler", "type": "unique very high"},
	"1 Corsair Sword": {"base": "Corsair Sword", "type": "unique very high"},
	"1 Crusader Gloves": {"base": "Crusader Gloves", "type": "unique very high"},
	"1 Crusader Plate": {"base": "Crusader Plate", "type": "unique very high"},
	"1 Crystal Wand": {"base": "Crystal Wand", "type": "unique very high"},
	"1 Deerskin Gloves": {"base": "Deerskin Gloves", "type": "unique very high"},
	"1 Despot Axe": {"base": "Despot Axe", "type": "unique very high"},
	"1 Diamond Ring": {"base": "Diamond Ring", "type": "unique very high"},
	"1 Dragonscale Boots": {"base": "Dragonscale Boots", "type": "unique very high"},
	"1 Ebony Tower Shield": {"base": "Ebony Tower Shield", "type": "unique very high"},
	"1 Etched Greatsword": {"base": "Etched Greatsword", "type": "unique very high"},
	"1 Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "type": "unique very high"},
	"1 Fiend Dagger": {"base": "Fiend Dagger", "type": "unique very high"},
	"1 Full Dragonscale": {"base": "Full Dragonscale", "type": "unique very high"},
	"1 Gold Ring": {"base": "Gold Ring", "type": "unique very high"},
	"1 Golden Plate": {"base": "Golden Plate", "type": "unique very high"},
	"1 Granite Flask": {"base": "Granite Flask", "type": "unique very high"},
	"1 Grinning Fetish": {"base": "Grinning Fetish", "type": "unique very high"},
	"1 Gut Ripper": {"base": "Gut Ripper", "type": "unique very high"},
	"1 Imperial Claw": {"base": "Imperial Claw", "type": "unique very high"},
	"1 Infernal Sword": {"base": "Infernal Sword", "type": "unique very high"},
	"1 Jewelled Foil": {"base": "Jewelled Foil", "type": "unique very high"},
	"1 Laminated Kite Shield": {"base": "Laminated Kite Shield", "type": "unique very high"},
	"1 Lathi": {"base": "Lathi", "type": "unique very high"},
	"1 Leather Cap": {"base": "Leather Cap", "type": "unique very high"},
	"1 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique very high"},
	"1 Opal Wand": {"base": "Opal Wand", "type": "unique very high"},
	"1 Painted Tower Shield": {"base": "Painted Tower Shield", "type": "unique very high"},
	"1 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique very high"},
	"1 Polished Spiked Shield": {"base": "Polished Spiked Shield", "type": "unique very high"},
	"1 Rotted Round Shield": {"base": "Rotted Round Shield", "type": "unique very high"},
	"1 Royal Skean": {"base": "Royal Skean", "type": "unique very high"},
	"1 Rustic Sash": {"base": "Rustic Sash", "type": "unique very high"},
	"1 Serpentscale Boots": {"base": "Serpentscale Boots", "type": "unique very high"},
	"1 Silver Flask": {"base": "Silver Flask", "type": "unique very high"},
	"1 Sinner Tricorne": {"base": "Sinner Tricorne", "type": "unique very high"},
	"1 Sorcerer Gloves": {"base": "Sorcerer Gloves", "type": "unique very high"},
	"1 Steel Gauntlets": {"base": "Steel Gauntlets", "type": "unique very high"},
	"1 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique very high"},
	"1 Tiger Sword": {"base": "Tiger Sword", "type": "unique very high"},
	"1 Titan Gauntlets": {"base": "Titan Gauntlets", "type": "unique very high"},
	"1 Titan Greaves": {"base": "Titan Greaves", "type": "unique very high"},
	"1 Tomahawk": {"base": "Tomahawk", "type": "unique very high"},
	"1 Topaz Ring": {"base": "Topaz Ring", "type": "unique very high"},
	"1 Triumphant Lamellar": {"base": "Triumphant Lamellar", "type": "unique very high"},
	"1 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique very high"},
	"1 Ursine Pelt": {"base": "Ursine Pelt", "type": "unique very high"},
	"1 Vaal Regalia": {"base": "Vaal Regalia", "type": "unique very high"},
	"1 Void Sceptre": {"base": "Void Sceptre", "type": "unique very high"},
	"1 War Sword": {"base": "War Sword", "type": "unique very high"},
	"1 Wyrmscale Gauntlets": {"base": "Wyrmscale Gauntlets", "type": "unique very high"},
	"2 Ambusher": {"base": "Ambusher", "type": "unique high"},
	"2 Amethyst Ring": {"base": "Amethyst Ring", "type": "unique high"},
	"2 Antique Rapier": {"base": "Antique Rapier", "type": "unique high"},
	"2 Assassin's Mitts": {"base": "Assassin's Mitts", "type": "unique high"},
	"2 Basket Rapier": {"base": "Basket Rapier", "type": "unique high"},
	"2 Blunt Arrow Quiver": {"base": "Blunt Arrow Quiver", "type": "unique high"},
	"2 Bone Circlet": {"base": "Bone Circlet", "type": "unique high"},
	"2 Boot Blade": {"base": "Boot Blade", "type": "unique high"},
	"2 Boot Knife": {"base": "Boot Knife", "type": "unique high"},
	"2 Branded Kite Shield": {"base": "Branded Kite Shield", "type": "unique high"},
	"2 Brass Maul": {"base": "Brass Maul", "type": "unique high"},
	"2 Bronzescale Boots": {"base": "Bronzescale Boots", "type": "unique high"},
	"2 Carnal Mitts": {"base": "Carnal Mitts", "type": "unique high"},
	"2 Chain Belt": {"base": "Chain Belt", "type": "unique high"},
	"2 Cleaver": {"base": "Cleaver", "type": "unique high"},
	"2 Cloth Belt": {"base": "Cloth Belt", "type": "unique high"},
	"2 Conquest Chainmail": {"base": "Conquest Chainmail", "type": "unique high"},
	"2 Copper Plate": {"base": "Copper Plate", "type": "unique high"},
	"2 Coral Ring": {"base": "Coral Ring", "type": "unique high"},
	"2 Crude Bow": {"base": "Crude Bow", "type": "unique high"},
	"2 Decimation Bow": {"base": "Decimation Bow", "type": "unique high"},
	"2 Decorative Axe": {"base": "Decorative Axe", "type": "unique high"},
	"2 Deerskin Boots": {"base": "Deerskin Boots", "type": "unique high"},
	"2 Demon's Horn": {"base": "Demon's Horn", "type": "unique high"},
	"2 Diamond Flask": {"base": "Diamond Flask", "type": "unique high"},
	"2 Driftwood Wand": {"base": "Driftwood Wand", "type": "unique high"},
	"2 Dusk Blade": {"base": "Dusk Blade", "type": "unique high"},
	"2 Elegant Sword": {"base": "Elegant Sword", "type": "unique high"},
	"2 Estoc": {"base": "Estoc", "type": "unique high"},
	"2 Ezomyte Axe": {"base": "Ezomyte Axe", "type": "unique high"},
	"2 Ezomyte Blade": {"base": "Ezomyte Blade", "type": "unique high"},
	"2 Ezomyte Staff": {"base": "Ezomyte Staff", "type": "unique high"},
	"2 Flaying Knife": {"base": "Flaying Knife", "type": "unique high"},
	"2 Fright Claw": {"base": "Fright Claw", "type": "unique high"},
	"2 Gilded Sallet": {"base": "Gilded Sallet", "type": "unique high"},
	"2 Gladius": {"base": "Gladius", "type": "unique high"},
	"2 Goathide Gloves": {"base": "Goathide Gloves", "type": "unique high"},
	"2 Golden Buckler": {"base": "Golden Buckler", "type": "unique high"},
	"2 Golden Mask": {"base": "Golden Mask", "type": "unique high"},
	"2 Great Mallet": {"base": "Great Mallet", "type": "unique high"},
	"2 Greater Mana Flask": {"base": "Greater Mana Flask", "type": "unique high"},
	"2 Headsman Axe": {"base": "Headsman Axe", "type": "unique high"},
	"2 Holy Chainmail": {"base": "Holy Chainmail", "type": "unique high"},
	"2 Infernal Axe": {"base": "Infernal Axe", "type": "unique high"},
	"2 Iron Gauntlets": {"base": "Iron Gauntlets", "type": "unique high"},
	"2 Iron Ring": {"base": "Iron Ring", "type": "unique high"},
	"2 Jade Hatchet": {"base": "Jade Hatchet", "type": "unique high"},
	"2 Jagged Foil": {"base": "Jagged Foil", "type": "unique high"},
	"2 Karui Chopper": {"base": "Karui Chopper", "type": "unique high"},
	"2 Karui Maul": {"base": "Karui Maul", "type": "unique high"},
	"2 Military Staff": {"base": "Military Staff", "type": "unique high"},
	"2 Murder Mitts": {"base": "Murder Mitts", "type": "unique high"},
	"2 Ornate Mace": {"base": "Ornate Mace", "type": "unique high"},
	"2 Paua Ring": {"base": "Paua Ring", "type": "unique high"},
	"2 Pine Buckler": {"base": "Pine Buckler", "type": "unique high"},
	"2 Plague Mask": {"base": "Plague Mask", "type": "unique high"},
	"2 Plank Kite Shield": {"base": "Plank Kite Shield", "type": "unique high"},
	"2 Poleaxe": {"base": "Poleaxe", "type": "unique high"},
	"2 Prismatic Ring": {"base": "Prismatic Ring", "type": "unique high"},
	"2 Prophet Crown": {"base": "Prophet Crown", "type": "unique high"},
	"2 Quartz Wand": {"base": "Quartz Wand", "type": "unique high"},
	"2 Recurve Bow": {"base": "Recurve Bow", "type": "unique high"},
	"2 Reinforced Greaves": {"base": "Reinforced Greaves", "type": "unique high"},
	"2 Rock Breaker": {"base": "Rock Breaker", "type": "unique high"},
	"2 Royal Staff": {"base": "Royal Staff", "type": "unique high"},
	"2 Ruby Ring": {"base": "Ruby Ring", "type": "unique high"},
	"2 Rusted Sword": {"base": "Rusted Sword", "type": "unique high"},
	"2 Sabre": {"base": "Sabre", "type": "unique high"},
	"2 Sage's Robe": {"base": "Sage's Robe", "type": "unique high"},
	"2 Secutor Helm": {"base": "Secutor Helm", "type": "unique high"},
	"2 Sentinel Jacket": {"base": "Sentinel Jacket", "type": "unique high"},
	"2 Shadow Axe": {"base": "Shadow Axe", "type": "unique high"},
	"2 Shagreen Boots": {"base": "Shagreen Boots", "type": "unique high"},
	"2 Short Bow": {"base": "Short Bow", "type": "unique high"},
	"2 Skinning Knife": {"base": "Skinning Knife", "type": "unique high"},
	"2 Soldier Boots": {"base": "Soldier Boots", "type": "unique high"},
	"2 Soldier Helmet": {"base": "Soldier Helmet", "type": "unique high"},
	"2 Spiked Club": {"base": "Spiked Club", "type": "unique high"},
	"2 Spiraled Wand": {"base": "Spiraled Wand", "type": "unique high"},
	"2 Strapped Boots": {"base": "Strapped Boots", "type": "unique high"},
	"2 Strapped Leather": {"base": "Strapped Leather", "type": "unique high"},
	"2 Strapped Mitts": {"base": "Strapped Mitts", "type": "unique high"},
	"2 Studded Belt": {"base": "Studded Belt", "type": "unique high"},
	"2 Sulphur Flask": {"base": "Sulphur Flask", "type": "unique high"},
	"2 Sundering Axe": {"base": "Sundering Axe", "type": "unique high"},
	"2 Throat Stabber": {"base": "Throat Stabber", "type": "unique high"},
	"2 Twilight Blade": {"base": "Twilight Blade", "type": "unique high"},
	"2 Vaal Buckler": {"base": "Vaal Buckler", "type": "unique high"},
	"2 Velvet Slippers": {"base": "Velvet Slippers", "type": "unique high"},
	"2 Vile Staff": {"base": "Vile Staff", "type": "unique high"},
	"2 Visored Sallet": {"base": "Visored Sallet", "type": "unique high"},
	"2 Widowsilk Robe": {"base": "Widowsilk Robe", "type": "unique high"},
	"2 Wool Gloves": {"base": "Wool Gloves", "type": "unique high"},
	"2 Wool Shoes": {"base": "Wool Shoes", "type": "unique high"},
	"6 Agate Amulet": {"base": "Agate Amulet", "type": "unique special"},
	"6 Amber Amulet": {"base": "Amber Amulet", "type": "unique special"},
	"6 Carved Wand": {"base": "Carved Wand", "type": "unique special"},
	"6 Cobalt Jewel": {"base": "Cobalt Jewel", "type": "unique special"},
	"6 Crimson Jewel": {"base": "Crimson Jewel", "type": "unique special"},
	"6 Death Bow": {"base": "Death Bow", "type": "unique special"},
	"6 Gold Amulet": {"base": "Gold Amulet", "type": "unique special"},
	"6 Great Crown": {"base": "Great Crown", "type": "unique special"},
	"6 Heavy Belt": {"base": "Heavy Belt", "type": "unique special"},
	"6 Jade Amulet": {"base": "Jade Amulet", "type": "unique special"},
	"6 Leather Belt": {"base": "Leather Belt", "type": "unique special"},
	"6 Legion Sword": {"base": "Legion Sword", "type": "unique special"},
	"6 Long Staff": {"base": "Long Staff", "type": "unique special"},
	"6 Moonstone Ring": {"base": "Moonstone Ring", "type": "unique special"},
	"6 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique special"},
	"6 Praetor Crown": {"base": "Praetor Crown", "type": "unique special"},
	"6 Sapphire Ring": {"base": "Sapphire Ring", "type": "unique special"},
	"6 Shadow Sceptre": {"base": "Shadow Sceptre", "type": "unique special"},
	"6 Soldier Gloves": {"base": "Soldier Gloves", "type": "unique special"},
	"6 Turquoise Amulet": {"base": "Turquoise Amulet", "type": "unique special"},
	"6 Two-Point Arrow Quiver": {"base": "Two-Point Arrow Quiver", "type": "unique special"},
	"6 Unset Ring": {"base": "Unset Ring", "type": "unique special"},
	"6 Vaal Blade": {"base": "Vaal Blade", "type": "unique special"},
	"6 Viridian Jewel": {"base": "Viridian Jewel", "type": "unique special"},
	"6 War Hammer": {"base": "War Hammer", "type": "unique special"},
	"7 Awl": {"base": "Awl", "type": "unique low"},
	"7 Buckskin Tunic": {"base": "Buckskin Tunic", "type": "unique low"},
	"7 Chain Gloves": {"base": "Chain Gloves", "type": "unique low"},
	"7 Dream Mace": {"base": "Dream Mace", "type": "unique low"},
	"7 Fire Arrow Quiver": {"base": "Fire Arrow Quiver", "type": "unique low"},
	"7 Gnarled Branch": {"base": "Gnarled Branch", "type": "unique low"},
	"7 Goat's Horn": {"base": "Goat's Horn", "type": "unique low"},
	"7 Great Helmet": {"base": "Great Helmet", "type": "unique low"},
	"7 Sage Wand": {"base": "Sage Wand", "type": "unique low"},
	"7 Serrated Arrow Quiver": {"base": "Serrated Arrow Quiver", "type": "unique low"},
	"7 Sledgehammer": {"base": "Sledgehammer", "type": "unique low"},
	"7 Studded Round Shield": {"base": "Studded Round Shield", "type": "unique low"},
	"7 Woodsplitter": {"base": "Woodsplitter", "type": "unique low"},
	"7 Wrapped Mitts": {"base": "Wrapped Mitts", "type": "unique low"},
	"9 Other uniques": {"type": "unique normal"}
}
