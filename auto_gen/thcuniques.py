#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 10/12/2018(m/d/y) 04:59:39 UTC from "tmphardcore" data

desc = "Unique"

# Base type : settings pair
items = {
	"0 Callous Mask": {"base": "Callous Mask", "type": "unique extremely high"},
	"0 Carnal Boots": {"base": "Carnal Boots", "type": "unique extremely high"},
	"0 Chateau Map": {"base": "Chateau Map", "type": "unique extremely high"},
	"0 Crusader Boots": {"base": "Crusader Boots", "type": "unique extremely high"},
	"0 Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "type": "unique extremely high"},
	"0 Gladiator Plate": {"base": "Gladiator Plate", "type": "unique extremely high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique extremely high"},
	"0 Golden Mantle": {"base": "Golden Mantle", "type": "unique extremely high"},
	"0 Grand Mana Flask": {"base": "Grand Mana Flask", "type": "unique extremely high"},
	"0 Legion Gloves": {"base": "Legion Gloves", "type": "unique extremely high"},
	"0 Magistrate Crown": {"base": "Magistrate Crown", "type": "unique extremely high"},
	"0 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique extremely high"},
	"0 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique extremely high"},
	"0 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique extremely high"},
	"0 Riveted Gloves": {"base": "Riveted Gloves", "type": "unique extremely high"},
	"0 Rotfeather Talisman": {"base": "Rotfeather Talisman", "type": "unique extremely high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique extremely high"},
	"0 Shackled Boots": {"base": "Shackled Boots", "type": "unique extremely high"},
	"0 Variscite Blade": {"base": "Variscite Blade", "type": "unique extremely high"},
	"1 Arcanist Gloves": {"base": "Arcanist Gloves", "type": "unique very high"},
	"1 Assassin's Boots": {"base": "Assassin's Boots", "type": "unique very high"},
	"1 Bismuth Flask": {"base": "Bismuth Flask", "type": "unique very high"},
	"1 Black Maw Talisman": {"base": "Black Maw Talisman", "type": "unique very high"},
	"1 Callous Mask Piece": {"base": "Callous Mask Piece", "type": "unique very high"},
	"1 Carnal Sceptre": {"base": "Carnal Sceptre", "type": "unique very high"},
	"1 Citrine Amulet": {"base": "Citrine Amulet", "type": "unique very high"},
	"1 Cloth Belt Piece": {"base": "Cloth Belt Piece", "type": "unique very high"},
	"1 Courtyard Map": {"base": "Courtyard Map", "type": "unique very high"},
	"1 Deicide Mask": {"base": "Deicide Mask", "type": "unique very high"},
	"1 Full Wyrmscale": {"base": "Full Wyrmscale", "type": "unique very high"},
	"1 Granite Flask": {"base": "Granite Flask", "type": "unique very high"},
	"1 Greatwolf Talisman": {"base": "Greatwolf Talisman", "type": "unique very high"},
	"1 Harbinger Map": {"base": "Harbinger Map", "type": "unique very high"},
	"1 Hydrascale Boots": {"base": "Hydrascale Boots", "type": "unique very high"},
	"1 Imperial Maul": {"base": "Imperial Maul", "type": "unique very high"},
	"1 Maze Map": {"base": "Maze Map", "type": "unique very high"},
	"1 Moon Temple Map": {"base": "Moon Temple Map", "type": "unique very high"},
	"1 Museum Map": {"base": "Museum Map", "type": "unique very high"},
	"1 Nightmare Mace": {"base": "Nightmare Mace", "type": "unique very high"},
	"1 Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "type": "unique very high"},
	"1 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique very high"},
	"1 Raven Mask": {"base": "Raven Mask", "type": "unique very high"},
	"1 Rawhide Tower Shield": {"base": "Rawhide Tower Shield", "type": "unique very high"},
	"1 Ritual Sceptre": {"base": "Ritual Sceptre", "type": "unique very high"},
	"1 Ruby Amulet": {"base": "Ruby Amulet", "type": "unique very high"},
	"1 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "unique very high"},
	"1 Sanctified Life Flask": {"base": "Sanctified Life Flask", "type": "unique very high"},
	"1 Sanctified Mana Flask": {"base": "Sanctified Mana Flask", "type": "unique very high"},
	"1 Savant's Robe": {"base": "Savant's Robe", "type": "unique very high"},
	"1 Shore Map": {"base": "Shore Map", "type": "unique very high"},
	"1 Siege Axe": {"base": "Siege Axe", "type": "unique very high"},
	"1 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique very high"},
	"1 Vaal Mask": {"base": "Vaal Mask", "type": "unique very high"},
	"1 Vaal Spirit Shield": {"base": "Vaal Spirit Shield", "type": "unique very high"},
	"1 Void Axe": {"base": "Void Axe", "type": "unique very high"},
	"1 Wereclaw Talisman": {"base": "Wereclaw Talisman", "type": "unique very high"},
	"1 Wyrmscale Doublet": {"base": "Wyrmscale Doublet", "type": "unique very high"},
	"2 Abyssal Axe": {"base": "Abyssal Axe", "type": "unique high"},
	"2 Amethyst Flask": {"base": "Amethyst Flask", "type": "unique high"},
	"2 Amethyst Ring": {"base": "Amethyst Ring", "type": "unique high"},
	"2 Ancient Greaves": {"base": "Ancient Greaves", "type": "unique high"},
	"2 Arcanist Slippers": {"base": "Arcanist Slippers", "type": "unique high"},
	"2 Assassin's Garb": {"base": "Assassin's Garb", "type": "unique high"},
	"2 Astral Plate": {"base": "Astral Plate", "type": "unique high"},
	"2 Atoll Map": {"base": "Atoll Map", "type": "unique high"},
	"2 Blinder": {"base": "Blinder", "type": "unique high"},
	"2 Blood Sceptre": {"base": "Blood Sceptre", "type": "unique high"},
	"2 Bone Armour": {"base": "Bone Armour", "type": "unique high"},
	"2 Bone Bow": {"base": "Bone Bow", "type": "unique high"},
	"2 Bone Crypt Map": {"base": "Bone Crypt Map", "type": "unique high"},
	"2 Branded Kite Shield": {"base": "Branded Kite Shield", "type": "unique high"},
	"2 Cardinal Round Shield": {"base": "Cardinal Round Shield", "type": "unique high"},
	"2 Cedar Tower Shield": {"base": "Cedar Tower Shield", "type": "unique high"},
	"2 Cemetery Map": {"base": "Cemetery Map", "type": "unique high"},
	"2 Champion Kite Shield": {"base": "Champion Kite Shield", "type": "unique high"},
	"2 Citadel Bow": {"base": "Citadel Bow", "type": "unique high"},
	"2 Clasped Mitts": {"base": "Clasped Mitts", "type": "unique high"},
	"2 Close Helmet": {"base": "Close Helmet", "type": "unique high"},
	"2 Coiled Staff": {"base": "Coiled Staff", "type": "unique high"},
	"2 Colossal Tower Shield": {"base": "Colossal Tower Shield", "type": "unique high"},
	"2 Conjurer Boots": {"base": "Conjurer Boots", "type": "unique high"},
	"2 Coral Ring": {"base": "Coral Ring", "type": "unique high"},
	"2 Coronal Leather": {"base": "Coronal Leather", "type": "unique high"},
	"2 Corsair Sword": {"base": "Corsair Sword", "type": "unique high"},
	"2 Crystal Belt": {"base": "Crystal Belt", "type": "unique high"},
	"2 Cursed Crypt Map": {"base": "Cursed Crypt Map", "type": "unique high"},
	"2 Demon Dagger": {"base": "Demon Dagger", "type": "unique high"},
	"2 Desert Brigandine": {"base": "Desert Brigandine", "type": "unique high"},
	"2 Destiny Leather": {"base": "Destiny Leather", "type": "unique high"},
	"2 Destroyer Regalia": {"base": "Destroyer Regalia", "type": "unique high"},
	"2 Driftwood Wand": {"base": "Driftwood Wand", "type": "unique high"},
	"2 Dunes Map": {"base": "Dunes Map", "type": "unique high"},
	"2 Elegant Foil": {"base": "Elegant Foil", "type": "unique high"},
	"2 Etched Greatsword": {"base": "Etched Greatsword", "type": "unique high"},
	"2 Exquisite Leather": {"base": "Exquisite Leather", "type": "unique high"},
	"2 Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "type": "unique high"},
	"2 Festival Mask": {"base": "Festival Mask", "type": "unique high"},
	"2 Full Scale Armour": {"base": "Full Scale Armour", "type": "unique high"},
	"2 Gold Ring": {"base": "Gold Ring", "type": "unique high"},
	"2 Goliath Greaves": {"base": "Goliath Greaves", "type": "unique high"},
	"2 Hallowed Hybrid Flask": {"base": "Hallowed Hybrid Flask", "type": "unique high"},
	"2 Hellion's Paw": {"base": "Hellion's Paw", "type": "unique high"},
	"2 Highborn Staff": {"base": "Highborn Staff", "type": "unique high"},
	"2 Iron Gauntlets": {"base": "Iron Gauntlets", "type": "unique high"},
	"2 Iron Ring": {"base": "Iron Ring", "type": "unique high"},
	"2 Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "type": "unique high"},
	"2 Jasper Chopper": {"base": "Jasper Chopper", "type": "unique high"},
	"2 Jewelled Foil": {"base": "Jewelled Foil", "type": "unique high"},
	"2 Jingling Spirit Shield": {"base": "Jingling Spirit Shield", "type": "unique high"},
	"2 Karui Sceptre": {"base": "Karui Sceptre", "type": "unique high"},
	"2 Labrys": {"base": "Labrys", "type": "unique high"},
	"2 Large Hybrid Flask": {"base": "Large Hybrid Flask", "type": "unique high"},
	"2 Leather Cap": {"base": "Leather Cap", "type": "unique high"},
	"2 Lion Pelt": {"base": "Lion Pelt", "type": "unique high"},
	"2 Meatgrinder": {"base": "Meatgrinder", "type": "unique high"},
	"2 Midnight Blade": {"base": "Midnight Blade", "type": "unique high"},
	"2 Necromancer Silks": {"base": "Necromancer Silks", "type": "unique high"},
	"2 Necropolis Map": {"base": "Necropolis Map", "type": "unique high"},
	"2 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique high"},
	"2 Nubuck Boots": {"base": "Nubuck Boots", "type": "unique high"},
	"2 Nubuck Gloves": {"base": "Nubuck Gloves", "type": "unique high"},
	"2 Opal Sceptre": {"base": "Opal Sceptre", "type": "unique high"},
	"2 Overgrown Shrine Map": {"base": "Overgrown Shrine Map", "type": "unique high"},
	"2 Painted Tower Shield": {"base": "Painted Tower Shield", "type": "unique high"},
	"2 Platinum Sceptre": {"base": "Platinum Sceptre", "type": "unique high"},
	"2 Promenade Map": {"base": "Promenade Map", "type": "unique high"},
	"2 Reinforced Greaves": {"base": "Reinforced Greaves", "type": "unique high"},
	"2 Royal Burgonet": {"base": "Royal Burgonet", "type": "unique high"},
	"2 Sabre": {"base": "Sabre", "type": "unique high"},
	"2 Saintly Chainmail": {"base": "Saintly Chainmail", "type": "unique high"},
	"2 Serpentscale Gauntlets": {"base": "Serpentscale Gauntlets", "type": "unique high"},
	"2 Sharkskin Tunic": {"base": "Sharkskin Tunic", "type": "unique high"},
	"2 Sharktooth Arrow Quiver": {"base": "Sharktooth Arrow Quiver", "type": "unique high"},
	"2 Short Bow": {"base": "Short Bow", "type": "unique high"},
	"2 Siege Helmet": {"base": "Siege Helmet", "type": "unique high"},
	"2 Sinner Tricorne": {"base": "Sinner Tricorne", "type": "unique high"},
	"2 Steel Ring": {"base": "Steel Ring", "type": "unique high"},
	"2 Steelhead": {"base": "Steelhead", "type": "unique high"},
	"2 Strand Map": {"base": "Strand Map", "type": "unique high"},
	"2 Stygian Vise": {"base": "Stygian Vise", "type": "unique high"},
	"2 Temple Map": {"base": "Temple Map", "type": "unique high"},
	"2 Thorium Spirit Shield": {"base": "Thorium Spirit Shield", "type": "unique high"},
	"2 Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "type": "unique high"},
	"2 Tornado Wand": {"base": "Tornado Wand", "type": "unique high"},
	"2 Torture Chamber Map": {"base": "Torture Chamber Map", "type": "unique high"},
	"2 Underground River Map": {"base": "Underground River Map", "type": "unique high"},
	"2 Vaal Pyramid Map": {"base": "Vaal Pyramid Map", "type": "unique high"},
	"2 War Sword": {"base": "War Sword", "type": "unique high"},
	"2 Wool Shoes": {"base": "Wool Shoes", "type": "unique high"},
	"2 Zealot Gloves": {"base": "Zealot Gloves", "type": "unique high"},
	"6 Agate Amulet": {"base": "Agate Amulet", "type": "unique special"},
	"6 Amber Amulet": {"base": "Amber Amulet", "type": "unique special"},
	"6 Archon Kite Shield": {"base": "Archon Kite Shield", "type": "unique special"},
	"6 Archon Kite Shield Piece": {"base": "Archon Kite Shield Piece", "type": "unique special"},
	"6 Assassin Bow": {"base": "Assassin Bow", "type": "unique special"},
	"6 Blunt Arrow Quiver": {"base": "Blunt Arrow Quiver", "type": "unique special"},
	"6 Blunt Arrow Quiver Piece": {"base": "Blunt Arrow Quiver Piece", "type": "unique special"},
	"6 Carnal Armour": {"base": "Carnal Armour", "type": "unique special"},
	"6 Carnal Mitts": {"base": "Carnal Mitts", "type": "unique special"},
	"6 Carved Wand": {"base": "Carved Wand", "type": "unique special"},
	"6 Cloth Belt": {"base": "Cloth Belt", "type": "unique special"},
	"6 Cobalt Jewel": {"base": "Cobalt Jewel", "type": "unique special"},
	"6 Crimson Jewel": {"base": "Crimson Jewel", "type": "unique special"},
	"6 Crusader Gloves": {"base": "Crusader Gloves", "type": "unique special"},
	"6 Cutlass": {"base": "Cutlass", "type": "unique special"},
	"6 Diamond Ring": {"base": "Diamond Ring", "type": "unique special"},
	"6 Ebony Tower Shield": {"base": "Ebony Tower Shield", "type": "unique special"},
	"6 Elegant Ringmail": {"base": "Elegant Ringmail", "type": "unique special"},
	"6 Elegant Sword": {"base": "Elegant Sword", "type": "unique special"},
	"6 Gavel": {"base": "Gavel", "type": "unique special"},
	"6 Goathide Boots": {"base": "Goathide Boots", "type": "unique special"},
	"6 Gold Amulet": {"base": "Gold Amulet", "type": "unique special"},
	"6 Golden Plate": {"base": "Golden Plate", "type": "unique special"},
	"6 Harlequin Mask": {"base": "Harlequin Mask", "type": "unique special"},
	"6 Heavy Belt": {"base": "Heavy Belt", "type": "unique special"},
	"6 Hubris Circlet": {"base": "Hubris Circlet", "type": "unique special"},
	"6 Imperial Bow": {"base": "Imperial Bow", "type": "unique special"},
	"6 Imperial Claw": {"base": "Imperial Claw", "type": "unique special"},
	"6 Imperial Staff": {"base": "Imperial Staff", "type": "unique special"},
	"6 Infernal Sword": {"base": "Infernal Sword", "type": "unique special"},
	"6 Jade Amulet": {"base": "Jade Amulet", "type": "unique special"},
	"6 Lacquered Garb": {"base": "Lacquered Garb", "type": "unique special"},
	"6 Lapis Amulet": {"base": "Lapis Amulet", "type": "unique special"},
	"6 Leather Belt": {"base": "Leather Belt", "type": "unique special"},
	"6 Legion Sword": {"base": "Legion Sword", "type": "unique special"},
	"6 Maelström Staff": {"base": "Maelström Staff", "type": "unique special"},
	"6 Moonstone Ring": {"base": "Moonstone Ring", "type": "unique special"},
	"6 Murder Boots": {"base": "Murder Boots", "type": "unique special"},
	"6 Necromancer Circlet": {"base": "Necromancer Circlet", "type": "unique special"},
	"6 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique special"},
	"6 Opal Ring": {"base": "Opal Ring", "type": "unique special"},
	"6 Paua Ring": {"base": "Paua Ring", "type": "unique special"},
	"6 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique special"},
	"6 Prismatic Ring": {"base": "Prismatic Ring", "type": "unique special"},
	"6 Quartz Flask": {"base": "Quartz Flask", "type": "unique special"},
	"6 Ruby Flask": {"base": "Ruby Flask", "type": "unique special"},
	"6 Ruby Ring": {"base": "Ruby Ring", "type": "unique special"},
	"6 Rustic Sash": {"base": "Rustic Sash", "type": "unique special"},
	"6 Sadist Garb": {"base": "Sadist Garb", "type": "unique special"},
	"6 Sapphire Ring": {"base": "Sapphire Ring", "type": "unique special"},
	"6 Silken Hood": {"base": "Silken Hood", "type": "unique special"},
	"6 Slink Boots": {"base": "Slink Boots", "type": "unique special"},
	"6 Soldier Gloves": {"base": "Soldier Gloves", "type": "unique special"},
	"6 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique special"},
	"6 Steelscale Gauntlets": {"base": "Steelscale Gauntlets", "type": "unique special"},
	"6 Terror Claw": {"base": "Terror Claw", "type": "unique special"},
	"6 Titan Gauntlets": {"base": "Titan Gauntlets", "type": "unique special"},
	"6 Titan Greaves": {"base": "Titan Greaves", "type": "unique special"},
	"6 Topaz Flask": {"base": "Topaz Flask", "type": "unique special"},
	"6 Topaz Ring": {"base": "Topaz Ring", "type": "unique special"},
	"6 Triumphant Lamellar": {"base": "Triumphant Lamellar", "type": "unique special"},
	"6 Two-Point Arrow Quiver": {"base": "Two-Point Arrow Quiver", "type": "unique special"},
	"6 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique special"},
	"6 Unset Ring": {"base": "Unset Ring", "type": "unique special"},
	"6 Vaal Axe": {"base": "Vaal Axe", "type": "unique special"},
	"6 Vaal Blade": {"base": "Vaal Blade", "type": "unique special"},
	"6 Vaal Gauntlets": {"base": "Vaal Gauntlets", "type": "unique special"},
	"6 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique special"},
	"6 Viridian Jewel": {"base": "Viridian Jewel", "type": "unique special"},
	"6 Zodiac Leather": {"base": "Zodiac Leather", "type": "unique special"},
	"7 Ambusher": {"base": "Ambusher", "type": "unique low"},
	"7 Antique Rapier": {"base": "Antique Rapier", "type": "unique low"},
	"7 Assassin's Mitts": {"base": "Assassin's Mitts", "type": "unique low"},
	"7 Awl": {"base": "Awl", "type": "unique low"},
	"7 Baroque Round Shield": {"base": "Baroque Round Shield", "type": "unique low"},
	"7 Bastard Sword": {"base": "Bastard Sword", "type": "unique low"},
	"7 Boot Blade": {"base": "Boot Blade", "type": "unique low"},
	"7 Boot Knife": {"base": "Boot Knife", "type": "unique low"},
	"7 Bronze Gauntlets": {"base": "Bronze Gauntlets", "type": "unique low"},
	"7 Buckskin Tunic": {"base": "Buckskin Tunic", "type": "unique low"},
	"7 Burnished Spiked Shield": {"base": "Burnished Spiked Shield", "type": "unique low"},
	"7 Chain Gloves": {"base": "Chain Gloves", "type": "unique low"},
	"7 Chiming Spirit Shield": {"base": "Chiming Spirit Shield", "type": "unique low"},
	"7 Compound Spiked Shield": {"base": "Compound Spiked Shield", "type": "unique low"},
	"7 Coral Amulet": {"base": "Coral Amulet", "type": "unique low"},
	"7 Crystal Wand": {"base": "Crystal Wand", "type": "unique low"},
	"7 Death Bow": {"base": "Death Bow", "type": "unique low"},
	"7 Decimation Bow": {"base": "Decimation Bow", "type": "unique low"},
	"7 Demon's Horn": {"base": "Demon's Horn", "type": "unique low"},
	"7 Dread Maul": {"base": "Dread Maul", "type": "unique low"},
	"7 Estoc": {"base": "Estoc", "type": "unique low"},
	"7 Fire Arrow Quiver": {"base": "Fire Arrow Quiver", "type": "unique low"},
	"7 Gnarled Branch": {"base": "Gnarled Branch", "type": "unique low"},
	"7 Goat's Horn": {"base": "Goat's Horn", "type": "unique low"},
	"7 Great Helmet": {"base": "Great Helmet", "type": "unique low"},
	"7 Greater Mana Flask": {"base": "Greater Mana Flask", "type": "unique low"},
	"7 Harbinger Bow": {"base": "Harbinger Bow", "type": "unique low"},
	"7 Harmonic Spirit Shield": {"base": "Harmonic Spirit Shield", "type": "unique low"},
	"7 Headsman Axe": {"base": "Headsman Axe", "type": "unique low"},
	"7 Highland Blade": {"base": "Highland Blade", "type": "unique low"},
	"7 Holy Chainmail": {"base": "Holy Chainmail", "type": "unique low"},
	"7 Imbued Wand": {"base": "Imbued Wand", "type": "unique low"},
	"7 Imperial Skean": {"base": "Imperial Skean", "type": "unique low"},
	"7 Iron Hat": {"base": "Iron Hat", "type": "unique low"},
	"7 Iron Mask": {"base": "Iron Mask", "type": "unique low"},
	"7 Iron Staff": {"base": "Iron Staff", "type": "unique low"},
	"7 Ironscale Boots": {"base": "Ironscale Boots", "type": "unique low"},
	"7 Ivory Spirit Shield": {"base": "Ivory Spirit Shield", "type": "unique low"},
	"7 Jagged Foil": {"base": "Jagged Foil", "type": "unique low"},
	"7 Jagged Maul": {"base": "Jagged Maul", "type": "unique low"},
	"7 Leather Hood": {"base": "Leather Hood", "type": "unique low"},
	"7 Legion Boots": {"base": "Legion Boots", "type": "unique low"},
	"7 Long Staff": {"base": "Long Staff", "type": "unique low"},
	"7 Military Staff": {"base": "Military Staff", "type": "unique low"},
	"7 Mind Cage": {"base": "Mind Cage", "type": "unique low"},
	"7 Ornate Ringmail": {"base": "Ornate Ringmail", "type": "unique low"},
	"7 Painted Buckler": {"base": "Painted Buckler", "type": "unique low"},
	"7 Plague Mask": {"base": "Plague Mask", "type": "unique low"},
	"7 Plated Greaves": {"base": "Plated Greaves", "type": "unique low"},
	"7 Platinum Kris": {"base": "Platinum Kris", "type": "unique low"},
	"7 Poleaxe": {"base": "Poleaxe", "type": "unique low"},
	"7 Primordial Staff": {"base": "Primordial Staff", "type": "unique low"},
	"7 Prophet Crown": {"base": "Prophet Crown", "type": "unique low"},
	"7 Quartz Wand": {"base": "Quartz Wand", "type": "unique low"},
	"7 Recurve Bow": {"base": "Recurve Bow", "type": "unique low"},
	"7 Rotted Round Shield": {"base": "Rotted Round Shield", "type": "unique low"},
	"7 Royal Bow": {"base": "Royal Bow", "type": "unique low"},
	"7 Royal Staff": {"base": "Royal Staff", "type": "unique low"},
	"7 Sage Wand": {"base": "Sage Wand", "type": "unique low"},
	"7 Samite Gloves": {"base": "Samite Gloves", "type": "unique low"},
	"7 Scholar Boots": {"base": "Scholar Boots", "type": "unique low"},
	"7 Scholar's Robe": {"base": "Scholar's Robe", "type": "unique low"},
	"7 Sentinel Jacket": {"base": "Sentinel Jacket", "type": "unique low"},
	"7 Serrated Arrow Quiver": {"base": "Serrated Arrow Quiver", "type": "unique low"},
	"7 Shadow Sceptre": {"base": "Shadow Sceptre", "type": "unique low"},
	"7 Shagreen Boots": {"base": "Shagreen Boots", "type": "unique low"},
	"7 Skinning Knife": {"base": "Skinning Knife", "type": "unique low"},
	"7 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique low"},
	"7 Sledgehammer": {"base": "Sledgehammer", "type": "unique low"},
	"7 Soldier Helmet": {"base": "Soldier Helmet", "type": "unique low"},
	"7 Spiked Club": {"base": "Spiked Club", "type": "unique low"},
	"7 Spiraled Wand": {"base": "Spiraled Wand", "type": "unique low"},
	"7 Stiletto": {"base": "Stiletto", "type": "unique low"},
	"7 Strapped Leather": {"base": "Strapped Leather", "type": "unique low"},
	"7 Studded Round Shield": {"base": "Studded Round Shield", "type": "unique low"},
	"7 Sulphur Flask": {"base": "Sulphur Flask", "type": "unique low"},
	"7 Sundering Axe": {"base": "Sundering Axe", "type": "unique low"},
	"7 Tarnished Spirit Shield": {"base": "Tarnished Spirit Shield", "type": "unique low"},
	"7 Thresher Claw": {"base": "Thresher Claw", "type": "unique low"},
	"7 Tricorne": {"base": "Tricorne", "type": "unique low"},
	"7 Turquoise Amulet": {"base": "Turquoise Amulet", "type": "unique low"},
	"7 Vaal Buckler": {"base": "Vaal Buckler", "type": "unique low"},
	"7 Velvet Slippers": {"base": "Velvet Slippers", "type": "unique low"},
	"7 Vile Staff": {"base": "Vile Staff", "type": "unique low"},
	"7 Visored Sallet": {"base": "Visored Sallet", "type": "unique low"},
	"7 War Buckler": {"base": "War Buckler", "type": "unique low"},
	"7 War Hammer": {"base": "War Hammer", "type": "unique low"},
	"7 Widowsilk Robe": {"base": "Widowsilk Robe", "type": "unique low"},
	"7 Wyrmscale Gauntlets": {"base": "Wyrmscale Gauntlets", "type": "unique low"},
	"9 Other uniques": {"type": "unique normal"}
}
