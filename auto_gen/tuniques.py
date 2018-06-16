#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 06/16/2018(m/d/y) 04:56:29 UTC from "tmpstandard" data

desc = "Unique"

# Base type : settings pair
items = {
	"0 Callous Mask": {"base": "Callous Mask", "type": "unique very high"},
	"0 Chateau Map": {"base": "Chateau Map", "type": "unique very high"},
	"0 Crusader Boots": {"base": "Crusader Boots", "type": "unique very high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"0 Grand Mana Flask": {"base": "Grand Mana Flask", "type": "unique very high"},
	"0 Greatwolf Talisman": {"base": "Greatwolf Talisman", "type": "unique very high"},
	"0 Harlequin Mask": {"base": "Harlequin Mask", "type": "unique very high"},
	"0 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique very high"},
	"0 Royal Axe": {"base": "Royal Axe", "type": "unique very high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique very high"},
	"1 Ambush Mitts": {"base": "Ambush Mitts", "type": "unique high"},
	"1 Arcanist Gloves": {"base": "Arcanist Gloves", "type": "unique high"},
	"1 Arcanist Slippers": {"base": "Arcanist Slippers", "type": "unique high"},
	"1 Callous Mask Piece": {"base": "Callous Mask Piece", "type": "unique high"},
	"1 Cloth Belt Piece": {"base": "Cloth Belt Piece", "type": "unique high"},
	"1 Courtyard Map": {"base": "Courtyard Map", "type": "unique high"},
	"1 Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "type": "unique high"},
	"1 Gemstone Sword": {"base": "Gemstone Sword", "type": "unique high"},
	"1 Harbinger Map": {"base": "Harbinger Map", "type": "unique high"},
	"1 Highborn Staff": {"base": "Highborn Staff", "type": "unique high"},
	"1 Legion Gloves": {"base": "Legion Gloves", "type": "unique high"},
	"1 Moon Temple Map": {"base": "Moon Temple Map", "type": "unique high"},
	"1 Museum Map": {"base": "Museum Map", "type": "unique high"},
	"1 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique high"},
	"1 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique high"},
	"1 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique high"},
	"1 Rawhide Tower Shield": {"base": "Rawhide Tower Shield", "type": "unique high"},
	"1 Ruby Amulet": {"base": "Ruby Amulet", "type": "unique high"},
	"1 Sanctified Life Flask": {"base": "Sanctified Life Flask", "type": "unique high"},
	"1 Sanctified Mana Flask": {"base": "Sanctified Mana Flask", "type": "unique high"},
	"1 Shore Map": {"base": "Shore Map", "type": "unique high"},
	"1 Temple Map": {"base": "Temple Map", "type": "unique high"},
	"1 Thorium Spirit Shield": {"base": "Thorium Spirit Shield", "type": "unique high"},
	"1 Vaal Spirit Shield": {"base": "Vaal Spirit Shield", "type": "unique high"},
	"1 Void Axe": {"base": "Void Axe", "type": "unique high"},
	"1 Wereclaw Talisman": {"base": "Wereclaw Talisman", "type": "unique high"},
	"6 Agate Amulet": {"base": "Agate Amulet", "type": "unique special"},
	"6 Amber Amulet": {"base": "Amber Amulet", "type": "unique special"},
	"6 Archon Kite Shield": {"base": "Archon Kite Shield", "type": "unique special"},
	"6 Archon Kite Shield Piece": {"base": "Archon Kite Shield Piece", "type": "unique special"},
	"6 Blunt Arrow Quiver": {"base": "Blunt Arrow Quiver", "type": "unique special"},
	"6 Carnal Armour": {"base": "Carnal Armour", "type": "unique special"},
	"6 Carved Wand": {"base": "Carved Wand", "type": "unique special"},
	"6 Chain Belt": {"base": "Chain Belt", "type": "unique special"},
	"6 Cloth Belt": {"base": "Cloth Belt", "type": "unique special"},
	"6 Cobalt Jewel": {"base": "Cobalt Jewel", "type": "unique special"},
	"6 Coral Ring": {"base": "Coral Ring", "type": "unique special"},
	"6 Crimson Jewel": {"base": "Crimson Jewel", "type": "unique special"},
	"6 Cutlass": {"base": "Cutlass", "type": "unique special"},
	"6 Despot Axe": {"base": "Despot Axe", "type": "unique special"},
	"6 Ebony Tower Shield": {"base": "Ebony Tower Shield", "type": "unique special"},
	"6 Elegant Ringmail": {"base": "Elegant Ringmail", "type": "unique special"},
	"6 Goathide Boots": {"base": "Goathide Boots", "type": "unique special"},
	"6 Goathide Gloves": {"base": "Goathide Gloves", "type": "unique special"},
	"6 Gold Amulet": {"base": "Gold Amulet", "type": "unique special"},
	"6 Golden Buckler": {"base": "Golden Buckler", "type": "unique special"},
	"6 Great Crown": {"base": "Great Crown", "type": "unique special"},
	"6 Hubris Circlet": {"base": "Hubris Circlet", "type": "unique special"},
	"6 Imperial Bow": {"base": "Imperial Bow", "type": "unique special"},
	"6 Imperial Staff": {"base": "Imperial Staff", "type": "unique special"},
	"6 Infernal Sword": {"base": "Infernal Sword", "type": "unique special"},
	"6 Iron Mask": {"base": "Iron Mask", "type": "unique special"},
	"6 Jade Amulet": {"base": "Jade Amulet", "type": "unique special"},
	"6 Lapis Amulet": {"base": "Lapis Amulet", "type": "unique special"},
	"6 Leather Belt": {"base": "Leather Belt", "type": "unique special"},
	"6 Leather Hood": {"base": "Leather Hood", "type": "unique special"},
	"6 Legion Sword": {"base": "Legion Sword", "type": "unique special"},
	"6 Long Bow": {"base": "Long Bow", "type": "unique special"},
	"6 Maelström Staff": {"base": "Maelström Staff", "type": "unique special"},
	"6 Midnight Blade": {"base": "Midnight Blade", "type": "unique special"},
	"6 Moonstone Ring": {"base": "Moonstone Ring", "type": "unique special"},
	"6 Murder Boots": {"base": "Murder Boots", "type": "unique special"},
	"6 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique special"},
	"6 Opal Ring": {"base": "Opal Ring", "type": "unique special"},
	"6 Paua Amulet": {"base": "Paua Amulet", "type": "unique special"},
	"6 Paua Ring": {"base": "Paua Ring", "type": "unique special"},
	"6 Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "type": "unique special"},
	"6 Prismatic Ring": {"base": "Prismatic Ring", "type": "unique special"},
	"6 Quartz Flask": {"base": "Quartz Flask", "type": "unique special"},
	"6 Reinforced Greaves": {"base": "Reinforced Greaves", "type": "unique special"},
	"6 Ruby Flask": {"base": "Ruby Flask", "type": "unique special"},
	"6 Rustic Sash": {"base": "Rustic Sash", "type": "unique special"},
	"6 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "unique special"},
	"6 Sadist Garb": {"base": "Sadist Garb", "type": "unique special"},
	"6 Sharktooth Arrow Quiver": {"base": "Sharktooth Arrow Quiver", "type": "unique special"},
	"6 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique special"},
	"6 Steelscale Gauntlets": {"base": "Steelscale Gauntlets", "type": "unique special"},
	"6 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique special"},
	"6 Titan Greaves": {"base": "Titan Greaves", "type": "unique special"},
	"6 Topaz Flask": {"base": "Topaz Flask", "type": "unique special"},
	"6 Topaz Ring": {"base": "Topaz Ring", "type": "unique special"},
	"6 Tornado Wand": {"base": "Tornado Wand", "type": "unique special"},
	"6 Two-Point Arrow Quiver": {"base": "Two-Point Arrow Quiver", "type": "unique special"},
	"6 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique special"},
	"6 Unset Ring": {"base": "Unset Ring", "type": "unique special"},
	"6 Vaal Axe": {"base": "Vaal Axe", "type": "unique special"},
	"6 Vaal Blade": {"base": "Vaal Blade", "type": "unique special"},
	"6 Vaal Gauntlets": {"base": "Vaal Gauntlets", "type": "unique special"},
	"6 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique special"},
	"6 Viridian Jewel": {"base": "Viridian Jewel", "type": "unique special"},
	"6 Zealot Gloves": {"base": "Zealot Gloves", "type": "unique special"},
	"7 Abyssal Axe": {"base": "Abyssal Axe", "type": "unique low"},
	"7 Ambusher": {"base": "Ambusher", "type": "unique low"},
	"7 Amethyst Flask": {"base": "Amethyst Flask", "type": "unique low"},
	"7 Ancient Gauntlets": {"base": "Ancient Gauntlets", "type": "unique low"},
	"7 Ancient Greaves": {"base": "Ancient Greaves", "type": "unique low"},
	"7 Ancient Spirit Shield": {"base": "Ancient Spirit Shield", "type": "unique low"},
	"7 Antique Rapier": {"base": "Antique Rapier", "type": "unique low"},
	"7 Assassin Bow": {"base": "Assassin Bow", "type": "unique low"},
	"7 Assassin's Garb": {"base": "Assassin's Garb", "type": "unique low"},
	"7 Assassin's Mitts": {"base": "Assassin's Mitts", "type": "unique low"},
	"7 Astral Plate": {"base": "Astral Plate", "type": "unique low"},
	"7 Auric Mace": {"base": "Auric Mace", "type": "unique low"},
	"7 Aventail Helmet": {"base": "Aventail Helmet", "type": "unique low"},
	"7 Awl": {"base": "Awl", "type": "unique low"},
	"7 Baroque Round Shield": {"base": "Baroque Round Shield", "type": "unique low"},
	"7 Basket Rapier": {"base": "Basket Rapier", "type": "unique low"},
	"7 Bastard Sword": {"base": "Bastard Sword", "type": "unique low"},
	"7 Black Maw Talisman": {"base": "Black Maw Talisman", "type": "unique low"},
	"7 Blinder": {"base": "Blinder", "type": "unique low"},
	"7 Blue Pearl Amulet": {"base": "Blue Pearl Amulet", "type": "unique low"},
	"7 Bone Armour": {"base": "Bone Armour", "type": "unique low"},
	"7 Bone Bow": {"base": "Bone Bow", "type": "unique low"},
	"7 Bone Circlet": {"base": "Bone Circlet", "type": "unique low"},
	"7 Boot Blade": {"base": "Boot Blade", "type": "unique low"},
	"7 Boot Knife": {"base": "Boot Knife", "type": "unique low"},
	"7 Branded Kite Shield": {"base": "Branded Kite Shield", "type": "unique low"},
	"7 Brass Maul": {"base": "Brass Maul", "type": "unique low"},
	"7 Brass Spirit Shield": {"base": "Brass Spirit Shield", "type": "unique low"},
	"7 Broadhead Arrow Quiver": {"base": "Broadhead Arrow Quiver", "type": "unique low"},
	"7 Bronze Gauntlets": {"base": "Bronze Gauntlets", "type": "unique low"},
	"7 Bronze Sceptre": {"base": "Bronze Sceptre", "type": "unique low"},
	"7 Bronzescale Boots": {"base": "Bronzescale Boots", "type": "unique low"},
	"7 Bronzescale Gauntlets": {"base": "Bronzescale Gauntlets", "type": "unique low"},
	"7 Buckskin Tunic": {"base": "Buckskin Tunic", "type": "unique low"},
	"7 Burnished Spiked Shield": {"base": "Burnished Spiked Shield", "type": "unique low"},
	"7 Carnal Mitts": {"base": "Carnal Mitts", "type": "unique low"},
	"7 Cedar Tower Shield": {"base": "Cedar Tower Shield", "type": "unique low"},
	"7 Chain Gloves": {"base": "Chain Gloves", "type": "unique low"},
	"7 Champion Kite Shield": {"base": "Champion Kite Shield", "type": "unique low"},
	"7 Clasped Boots": {"base": "Clasped Boots", "type": "unique low"},
	"7 Cleaver": {"base": "Cleaver", "type": "unique low"},
	"7 Close Helmet": {"base": "Close Helmet", "type": "unique low"},
	"7 Coiled Staff": {"base": "Coiled Staff", "type": "unique low"},
	"7 Colossal Tower Shield": {"base": "Colossal Tower Shield", "type": "unique low"},
	"7 Compound Spiked Shield": {"base": "Compound Spiked Shield", "type": "unique low"},
	"7 Conjurer Boots": {"base": "Conjurer Boots", "type": "unique low"},
	"7 Conjurer Gloves": {"base": "Conjurer Gloves", "type": "unique low"},
	"7 Conquest Chainmail": {"base": "Conquest Chainmail", "type": "unique low"},
	"7 Copper Plate": {"base": "Copper Plate", "type": "unique low"},
	"7 Coral Amulet": {"base": "Coral Amulet", "type": "unique low"},
	"7 Coronal Leather": {"base": "Coronal Leather", "type": "unique low"},
	"7 Corrugated Buckler": {"base": "Corrugated Buckler", "type": "unique low"},
	"7 Corsair Sword": {"base": "Corsair Sword", "type": "unique low"},
	"7 Crude Bow": {"base": "Crude Bow", "type": "unique low"},
	"7 Crusader Chainmail": {"base": "Crusader Chainmail", "type": "unique low"},
	"7 Crusader Gloves": {"base": "Crusader Gloves", "type": "unique low"},
	"7 Crusader Helmet": {"base": "Crusader Helmet", "type": "unique low"},
	"7 Crusader Plate": {"base": "Crusader Plate", "type": "unique low"},
	"7 Crystal Belt": {"base": "Crystal Belt", "type": "unique low"},
	"7 Crystal Sceptre": {"base": "Crystal Sceptre", "type": "unique low"},
	"7 Crystal Wand": {"base": "Crystal Wand", "type": "unique low"},
	"7 Cutthroat's Garb": {"base": "Cutthroat's Garb", "type": "unique low"},
	"7 Death Bow": {"base": "Death Bow", "type": "unique low"},
	"7 Decimation Bow": {"base": "Decimation Bow", "type": "unique low"},
	"7 Decorative Axe": {"base": "Decorative Axe", "type": "unique low"},
	"7 Deerskin Boots": {"base": "Deerskin Boots", "type": "unique low"},
	"7 Deerskin Gloves": {"base": "Deerskin Gloves", "type": "unique low"},
	"7 Demon Dagger": {"base": "Demon Dagger", "type": "unique low"},
	"7 Demon's Horn": {"base": "Demon's Horn", "type": "unique low"},
	"7 Desert Brigandine": {"base": "Desert Brigandine", "type": "unique low"},
	"7 Destroyer Regalia": {"base": "Destroyer Regalia", "type": "unique low"},
	"7 Diamond Flask": {"base": "Diamond Flask", "type": "unique low"},
	"7 Dragonscale Boots": {"base": "Dragonscale Boots", "type": "unique low"},
	"7 Dragonscale Gauntlets": {"base": "Dragonscale Gauntlets", "type": "unique low"},
	"7 Dread Maul": {"base": "Dread Maul", "type": "unique low"},
	"7 Dream Mace": {"base": "Dream Mace", "type": "unique low"},
	"7 Driftwood Wand": {"base": "Driftwood Wand", "type": "unique low"},
	"7 Dusk Blade": {"base": "Dusk Blade", "type": "unique low"},
	"7 Elder Sword": {"base": "Elder Sword", "type": "unique low"},
	"7 Elegant Foil": {"base": "Elegant Foil", "type": "unique low"},
	"7 Elegant Sword": {"base": "Elegant Sword", "type": "unique low"},
	"7 Enameled Buckler": {"base": "Enameled Buckler", "type": "unique low"},
	"7 Engraved Wand": {"base": "Engraved Wand", "type": "unique low"},
	"7 Estoc": {"base": "Estoc", "type": "unique low"},
	"7 Etched Greatsword": {"base": "Etched Greatsword", "type": "unique low"},
	"7 Eternal Sword": {"base": "Eternal Sword", "type": "unique low"},
	"7 Exquisite Leather": {"base": "Exquisite Leather", "type": "unique low"},
	"7 Ezomyte Axe": {"base": "Ezomyte Axe", "type": "unique low"},
	"7 Ezomyte Blade": {"base": "Ezomyte Blade", "type": "unique low"},
	"7 Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "type": "unique low"},
	"7 Ezomyte Staff": {"base": "Ezomyte Staff", "type": "unique low"},
	"7 Festival Mask": {"base": "Festival Mask", "type": "unique low"},
	"7 Fiend Dagger": {"base": "Fiend Dagger", "type": "unique low"},
	"7 Fire Arrow Quiver": {"base": "Fire Arrow Quiver", "type": "unique low"},
	"7 Flaying Knife": {"base": "Flaying Knife", "type": "unique low"},
	"7 Fright Claw": {"base": "Fright Claw", "type": "unique low"},
	"7 Full Dragonscale": {"base": "Full Dragonscale", "type": "unique low"},
	"7 Full Scale Armour": {"base": "Full Scale Armour", "type": "unique low"},
	"7 Gavel": {"base": "Gavel", "type": "unique low"},
	"7 Gilded Sallet": {"base": "Gilded Sallet", "type": "unique low"},
	"7 Gladius": {"base": "Gladius", "type": "unique low"},
	"7 Gnarled Branch": {"base": "Gnarled Branch", "type": "unique low"},
	"7 Goat's Horn": {"base": "Goat's Horn", "type": "unique low"},
	"7 Golden Mask": {"base": "Golden Mask", "type": "unique low"},
	"7 Golden Plate": {"base": "Golden Plate", "type": "unique low"},
	"7 Goliath Gauntlets": {"base": "Goliath Gauntlets", "type": "unique low"},
	"7 Goliath Greaves": {"base": "Goliath Greaves", "type": "unique low"},
	"7 Granite Flask": {"base": "Granite Flask", "type": "unique low"},
	"7 Great Helmet": {"base": "Great Helmet", "type": "unique low"},
	"7 Great Mallet": {"base": "Great Mallet", "type": "unique low"},
	"7 Greater Mana Flask": {"base": "Greater Mana Flask", "type": "unique low"},
	"7 Grinning Fetish": {"base": "Grinning Fetish", "type": "unique low"},
	"7 Gut Ripper": {"base": "Gut Ripper", "type": "unique low"},
	"7 Hallowed Hybrid Flask": {"base": "Hallowed Hybrid Flask", "type": "unique low"},
	"7 Harbinger Bow": {"base": "Harbinger Bow", "type": "unique low"},
	"7 Harmonic Spirit Shield": {"base": "Harmonic Spirit Shield", "type": "unique low"},
	"7 Headsman Axe": {"base": "Headsman Axe", "type": "unique low"},
	"7 Heavy Belt": {"base": "Heavy Belt", "type": "unique low"},
	"7 Hellion's Paw": {"base": "Hellion's Paw", "type": "unique low"},
	"7 Highland Blade": {"base": "Highland Blade", "type": "unique low"},
	"7 Holy Chainmail": {"base": "Holy Chainmail", "type": "unique low"},
	"7 Imbued Wand": {"base": "Imbued Wand", "type": "unique low"},
	"7 Imperial Claw": {"base": "Imperial Claw", "type": "unique low"},
	"7 Imperial Skean": {"base": "Imperial Skean", "type": "unique low"},
	"7 Infernal Axe": {"base": "Infernal Axe", "type": "unique low"},
	"7 Iron Circlet": {"base": "Iron Circlet", "type": "unique low"},
	"7 Iron Gauntlets": {"base": "Iron Gauntlets", "type": "unique low"},
	"7 Iron Hat": {"base": "Iron Hat", "type": "unique low"},
	"7 Iron Sceptre": {"base": "Iron Sceptre", "type": "unique low"},
	"7 Iron Staff": {"base": "Iron Staff", "type": "unique low"},
	"7 Ironscale Boots": {"base": "Ironscale Boots", "type": "unique low"},
	"7 Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "type": "unique low"},
	"7 Ivory Spirit Shield": {"base": "Ivory Spirit Shield", "type": "unique low"},
	"7 Jade Hatchet": {"base": "Jade Hatchet", "type": "unique low"},
	"7 Jagged Foil": {"base": "Jagged Foil", "type": "unique low"},
	"7 Jagged Maul": {"base": "Jagged Maul", "type": "unique low"},
	"7 Judgement Staff": {"base": "Judgement Staff", "type": "unique low"},
	"7 Karui Chopper": {"base": "Karui Chopper", "type": "unique low"},
	"7 Karui Maul": {"base": "Karui Maul", "type": "unique low"},
	"7 Karui Sceptre": {"base": "Karui Sceptre", "type": "unique low"},
	"7 Labrys": {"base": "Labrys", "type": "unique low"},
	"7 Lacquered Garb": {"base": "Lacquered Garb", "type": "unique low"},
	"7 Lacquered Helmet": {"base": "Lacquered Helmet", "type": "unique low"},
	"7 Laminated Kite Shield": {"base": "Laminated Kite Shield", "type": "unique low"},
	"7 Large Hybrid Flask": {"base": "Large Hybrid Flask", "type": "unique low"},
	"7 Lathi": {"base": "Lathi", "type": "unique low"},
	"7 Latticed Ringmail": {"base": "Latticed Ringmail", "type": "unique low"},
	"7 Legion Boots": {"base": "Legion Boots", "type": "unique low"},
	"7 Lion Pelt": {"base": "Lion Pelt", "type": "unique low"},
	"7 Lion Sword": {"base": "Lion Sword", "type": "unique low"},
	"7 Long Staff": {"base": "Long Staff", "type": "unique low"},
	"7 Lunaris Circlet": {"base": "Lunaris Circlet", "type": "unique low"},
	"7 Marble Amulet": {"base": "Marble Amulet", "type": "unique low"},
	"7 Meatgrinder": {"base": "Meatgrinder", "type": "unique low"},
	"7 Mesh Boots": {"base": "Mesh Boots", "type": "unique low"},
	"7 Military Staff": {"base": "Military Staff", "type": "unique low"},
	"7 Mind Cage": {"base": "Mind Cage", "type": "unique low"},
	"7 Mirrored Spiked Shield": {"base": "Mirrored Spiked Shield", "type": "unique low"},
	"7 Mosaic Kite Shield": {"base": "Mosaic Kite Shield", "type": "unique low"},
	"7 Murder Mitts": {"base": "Murder Mitts", "type": "unique low"},
	"7 Nailed Fist": {"base": "Nailed Fist", "type": "unique low"},
	"7 Necromancer Circlet": {"base": "Necromancer Circlet", "type": "unique low"},
	"7 Necromancer Silks": {"base": "Necromancer Silks", "type": "unique low"},
	"7 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique low"},
	"7 Nightmare Mace": {"base": "Nightmare Mace", "type": "unique low"},
	"7 Opal Sceptre": {"base": "Opal Sceptre", "type": "unique low"},
	"7 Opal Wand": {"base": "Opal Wand", "type": "unique low"},
	"7 Ornate Mace": {"base": "Ornate Mace", "type": "unique low"},
	"7 Ornate Ringmail": {"base": "Ornate Ringmail", "type": "unique low"},
	"7 Ornate Sword": {"base": "Ornate Sword", "type": "unique low"},
	"7 Painted Buckler": {"base": "Painted Buckler", "type": "unique low"},
	"7 Painted Tower Shield": {"base": "Painted Tower Shield", "type": "unique low"},
	"7 Pine Buckler": {"base": "Pine Buckler", "type": "unique low"},
	"7 Plank Kite Shield": {"base": "Plank Kite Shield", "type": "unique low"},
	"7 Plate Vest": {"base": "Plate Vest", "type": "unique low"},
	"7 Plated Greaves": {"base": "Plated Greaves", "type": "unique low"},
	"7 Platinum Kris": {"base": "Platinum Kris", "type": "unique low"},
	"7 Platinum Sceptre": {"base": "Platinum Sceptre", "type": "unique low"},
	"7 Poleaxe": {"base": "Poleaxe", "type": "unique low"},
	"7 Polished Spiked Shield": {"base": "Polished Spiked Shield", "type": "unique low"},
	"7 Praetor Crown": {"base": "Praetor Crown", "type": "unique low"},
	"7 Primordial Staff": {"base": "Primordial Staff", "type": "unique low"},
	"7 Prophet Crown": {"base": "Prophet Crown", "type": "unique low"},
	"7 Quartz Wand": {"base": "Quartz Wand", "type": "unique low"},
	"7 Quicksilver Flask": {"base": "Quicksilver Flask", "type": "unique low"},
	"7 Ranger Bow": {"base": "Ranger Bow", "type": "unique low"},
	"7 Reaver Sword": {"base": "Reaver Sword", "type": "unique low"},
	"7 Recurve Bow": {"base": "Recurve Bow", "type": "unique low"},
	"7 Regicide Mask": {"base": "Regicide Mask", "type": "unique low"},
	"7 Reinforced Tower Shield": {"base": "Reinforced Tower Shield", "type": "unique low"},
	"7 Riveted Boots": {"base": "Riveted Boots", "type": "unique low"},
	"7 Rock Breaker": {"base": "Rock Breaker", "type": "unique low"},
	"7 Rotted Round Shield": {"base": "Rotted Round Shield", "type": "unique low"},
	"7 Royal Bow": {"base": "Royal Bow", "type": "unique low"},
	"7 Royal Skean": {"base": "Royal Skean", "type": "unique low"},
	"7 Royal Staff": {"base": "Royal Staff", "type": "unique low"},
	"7 Rusted Sword": {"base": "Rusted Sword", "type": "unique low"},
	"7 Sabre": {"base": "Sabre", "type": "unique low"},
	"7 Sage Wand": {"base": "Sage Wand", "type": "unique low"},
	"7 Sage's Robe": {"base": "Sage's Robe", "type": "unique low"},
	"7 Saintly Chainmail": {"base": "Saintly Chainmail", "type": "unique low"},
	"7 Samite Gloves": {"base": "Samite Gloves", "type": "unique low"},
	"7 Samite Helmet": {"base": "Samite Helmet", "type": "unique low"},
	"7 Scholar Boots": {"base": "Scholar Boots", "type": "unique low"},
	"7 Scholar's Robe": {"base": "Scholar's Robe", "type": "unique low"},
	"7 Secutor Helm": {"base": "Secutor Helm", "type": "unique low"},
	"7 Sentinel Jacket": {"base": "Sentinel Jacket", "type": "unique low"},
	"7 Serpentine Staff": {"base": "Serpentine Staff", "type": "unique low"},
	"7 Serpentscale Boots": {"base": "Serpentscale Boots", "type": "unique low"},
	"7 Serrated Arrow Quiver": {"base": "Serrated Arrow Quiver", "type": "unique low"},
	"7 Shackled Boots": {"base": "Shackled Boots", "type": "unique low"},
	"7 Shadow Axe": {"base": "Shadow Axe", "type": "unique low"},
	"7 Shadow Sceptre": {"base": "Shadow Sceptre", "type": "unique low"},
	"7 Shagreen Boots": {"base": "Shagreen Boots", "type": "unique low"},
	"7 Sharkskin Boots": {"base": "Sharkskin Boots", "type": "unique low"},
	"7 Sharkskin Tunic": {"base": "Sharkskin Tunic", "type": "unique low"},
	"7 Short Bow": {"base": "Short Bow", "type": "unique low"},
	"7 Siege Helmet": {"base": "Siege Helmet", "type": "unique low"},
	"7 Silk Gloves": {"base": "Silk Gloves", "type": "unique low"},
	"7 Silk Slippers": {"base": "Silk Slippers", "type": "unique low"},
	"7 Silver Flask": {"base": "Silver Flask", "type": "unique low"},
	"7 Simple Robe": {"base": "Simple Robe", "type": "unique low"},
	"7 Sinner Tricorne": {"base": "Sinner Tricorne", "type": "unique low"},
	"7 Skinning Knife": {"base": "Skinning Knife", "type": "unique low"},
	"7 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique low"},
	"7 Sledgehammer": {"base": "Sledgehammer", "type": "unique low"},
	"7 Slink Boots": {"base": "Slink Boots", "type": "unique low"},
	"7 Soldier Boots": {"base": "Soldier Boots", "type": "unique low"},
	"7 Soldier Gloves": {"base": "Soldier Gloves", "type": "unique low"},
	"7 Soldier Helmet": {"base": "Soldier Helmet", "type": "unique low"},
	"7 Sorcerer Gloves": {"base": "Sorcerer Gloves", "type": "unique low"},
	"7 Spidersilk Robe": {"base": "Spidersilk Robe", "type": "unique low"},
	"7 Spike-Point Arrow Quiver": {"base": "Spike-Point Arrow Quiver", "type": "unique low"},
	"7 Spiked Club": {"base": "Spiked Club", "type": "unique low"},
	"7 Spine Bow": {"base": "Spine Bow", "type": "unique low"},
	"7 Spiraled Wand": {"base": "Spiraled Wand", "type": "unique low"},
	"7 Stealth Boots": {"base": "Stealth Boots", "type": "unique low"},
	"7 Steel Gauntlets": {"base": "Steel Gauntlets", "type": "unique low"},
	"7 Steelhead": {"base": "Steelhead", "type": "unique low"},
	"7 Stiletto": {"base": "Stiletto", "type": "unique low"},
	"7 Strapped Boots": {"base": "Strapped Boots", "type": "unique low"},
	"7 Strapped Leather": {"base": "Strapped Leather", "type": "unique low"},
	"7 Strapped Mitts": {"base": "Strapped Mitts", "type": "unique low"},
	"7 Studded Belt": {"base": "Studded Belt", "type": "unique low"},
	"7 Studded Round Shield": {"base": "Studded Round Shield", "type": "unique low"},
	"7 Stygian Vise": {"base": "Stygian Vise", "type": "unique low"},
	"7 Sulphur Flask": {"base": "Sulphur Flask", "type": "unique low"},
	"7 Sundering Axe": {"base": "Sundering Axe", "type": "unique low"},
	"7 Supreme Spiked Shield": {"base": "Supreme Spiked Shield", "type": "unique low"},
	"7 Tarnished Spirit Shield": {"base": "Tarnished Spirit Shield", "type": "unique low"},
	"7 Terror Claw": {"base": "Terror Claw", "type": "unique low"},
	"7 Terror Maul": {"base": "Terror Maul", "type": "unique low"},
	"7 Thresher Claw": {"base": "Thresher Claw", "type": "unique low"},
	"7 Throat Stabber": {"base": "Throat Stabber", "type": "unique low"},
	"7 Tiger Sword": {"base": "Tiger Sword", "type": "unique low"},
	"7 Timeworn Claw": {"base": "Timeworn Claw", "type": "unique low"},
	"7 Titan Gauntlets": {"base": "Titan Gauntlets", "type": "unique low"},
	"7 Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "type": "unique low"},
	"7 Tomahawk": {"base": "Tomahawk", "type": "unique low"},
	"7 Trapper Boots": {"base": "Trapper Boots", "type": "unique low"},
	"7 Tribal Circlet": {"base": "Tribal Circlet", "type": "unique low"},
	"7 Tricorne": {"base": "Tricorne", "type": "unique low"},
	"7 Triumphant Lamellar": {"base": "Triumphant Lamellar", "type": "unique low"},
	"7 Turquoise Amulet": {"base": "Turquoise Amulet", "type": "unique low"},
	"7 Twilight Blade": {"base": "Twilight Blade", "type": "unique low"},
	"7 Vaal Buckler": {"base": "Vaal Buckler", "type": "unique low"},
	"7 Vaal Claw": {"base": "Vaal Claw", "type": "unique low"},
	"7 Vaal Hatchet": {"base": "Vaal Hatchet", "type": "unique low"},
	"7 Vaal Regalia": {"base": "Vaal Regalia", "type": "unique low"},
	"7 Vanguard Belt": {"base": "Vanguard Belt", "type": "unique low"},
	"7 Variscite Blade": {"base": "Variscite Blade", "type": "unique low"},
	"7 Varnished Coat": {"base": "Varnished Coat", "type": "unique low"},
	"7 Velvet Gloves": {"base": "Velvet Gloves", "type": "unique low"},
	"7 Velvet Slippers": {"base": "Velvet Slippers", "type": "unique low"},
	"7 Vile Staff": {"base": "Vile Staff", "type": "unique low"},
	"7 Vine Circlet": {"base": "Vine Circlet", "type": "unique low"},
	"7 Visored Sallet": {"base": "Visored Sallet", "type": "unique low"},
	"7 Void Sceptre": {"base": "Void Sceptre", "type": "unique low"},
	"7 War Buckler": {"base": "War Buckler", "type": "unique low"},
	"7 War Hammer": {"base": "War Hammer", "type": "unique low"},
	"7 War Sword": {"base": "War Sword", "type": "unique low"},
	"7 Whalebone Rapier": {"base": "Whalebone Rapier", "type": "unique low"},
	"7 Widowsilk Robe": {"base": "Widowsilk Robe", "type": "unique low"},
	"7 Wild Leather": {"base": "Wild Leather", "type": "unique low"},
	"7 Woodsplitter": {"base": "Woodsplitter", "type": "unique low"},
	"7 Wool Gloves": {"base": "Wool Gloves", "type": "unique low"},
	"7 Wool Shoes": {"base": "Wool Shoes", "type": "unique low"},
	"7 Wrapped Mitts": {"base": "Wrapped Mitts", "type": "unique low"},
	"7 Wyrmscale Gauntlets": {"base": "Wyrmscale Gauntlets", "type": "unique low"},
	"7 Zealot Helmet": {"base": "Zealot Helmet", "type": "unique low"},
	"7 Zodiac Leather": {"base": "Zodiac Leather", "type": "unique low"},
	"9 Other uniques": {"type": "unique normal"}
}
