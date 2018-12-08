#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 12/08/2018(m/d/y) 01:57:26 UTC from "tmphardcore" data

desc = "Prophecy Autogen"

# Base type : settings pair
items = {
	"000 Thaumaturgical History III": {"prophecy": "Thaumaturgical History III", "class": "Currency", "type": "currency low"},
	"001 Thaumaturgical History II": {"prophecy": "Thaumaturgical History II", "class": "Currency", "type": "currency low"},
	"002 Thaumaturgical History IV": {"prophecy": "Thaumaturgical History IV", "class": "Currency", "type": "currency low"},
	"003 The Unbreathing Queen III": {"prophecy": "The Unbreathing Queen III", "class": "Currency", "type": "currency low"},
	"004 The Unbreathing Queen IV": {"prophecy": "The Unbreathing Queen IV", "class": "Currency", "type": "currency low"},
	"005 The Unbreathing Queen II": {"prophecy": "The Unbreathing Queen II", "class": "Currency", "type": "currency low"},
	"006 The Ambitious Bandit III": {"prophecy": "The Ambitious Bandit III", "class": "Currency", "type": "currency high"},
	"007 Unbearable Whispers III": {"prophecy": "Unbearable Whispers III", "class": "Currency", "type": "currency low"},
	"008 The Ambitious Bandit II": {"prophecy": "The Ambitious Bandit II", "class": "Currency", "type": "currency low"},
	"009 Unbearable Whispers IV": {"prophecy": "Unbearable Whispers IV", "class": "Currency", "type": "currency high"},
	"010 Unbearable Whispers II": {"prophecy": "Unbearable Whispers II", "class": "Currency", "type": "currency low"},
	"011 Ancient Rivalries III": {"prophecy": "Ancient Rivalries III", "class": "Currency", "type": "currency very high"},
	"012 Ancient Rivalries II": {"prophecy": "Ancient Rivalries II", "class": "Currency", "type": "currency very high"},
	"013 Day of Sacrifice III": {"prophecy": "Day of Sacrifice III", "class": "Currency", "type": "currency high"},
	"014 Day of Sacrifice IV": {"prophecy": "Day of Sacrifice IV", "class": "Currency", "type": "currency high"},
	"015 Day of Sacrifice II": {"prophecy": "Day of Sacrifice II", "class": "Currency", "type": "currency low"},
	"016 The Feral Lord III": {"prophecy": "The Feral Lord III", "class": "Currency", "type": "currency low"},
	"017 Deadly Rivalry III": {"prophecy": "Deadly Rivalry III", "class": "Currency", "type": "currency low"},
	"018 The Warmongers III": {"prophecy": "The Warmongers III", "class": "Currency", "type": "currency low"},
	"019 The Warmongers IV": {"prophecy": "The Warmongers IV", "class": "Currency", "type": "currency low"},
	"020 The Warmongers II": {"prophecy": "The Warmongers II", "class": "Currency", "type": "currency low"},
	"021 Deadly Rivalry II": {"prophecy": "Deadly Rivalry II", "class": "Currency", "type": "currency low"},
	"022 The Feral Lord II": {"prophecy": "The Feral Lord II", "class": "Currency", "type": "currency low"},
	"023 Anarchy's End III": {"prophecy": "Anarchy's End III", "class": "Currency", "type": "currency low"},
	"024 The Feral Lord IV": {"prophecy": "The Feral Lord IV", "class": "Currency", "type": "currency low"},
	"025 The Plaguemaw III": {"prophecy": "The Plaguemaw III", "class": "Currency", "type": "currency low"},
	"026 Deadly Rivalry IV": {"prophecy": "Deadly Rivalry IV", "class": "Currency", "type": "currency low"},
	"027 Anarchy's End IV": {"prophecy": "Anarchy's End IV", "class": "Currency", "type": "currency high"},
	"028 The Plaguemaw IV": {"prophecy": "The Plaguemaw IV", "class": "Currency", "type": "currency low"},
	"029 The Plaguemaw II": {"prophecy": "The Plaguemaw II", "class": "Currency", "type": "currency low"},
	"030 Anarchy's End II": {"prophecy": "Anarchy's End II", "class": "Currency", "type": "currency low"},
	"031 Beyond Sight III": {"prophecy": "Beyond Sight III", "class": "Currency", "type": "currency high"},
	"032 Beyond Sight II": {"prophecy": "Beyond Sight II", "class": "Currency", "type": "currency low"},
	"033 Beyond Sight IV": {"prophecy": "Beyond Sight IV", "class": "Currency", "type": "currency high"},
	"1 A Dishonourable Death": {"prophecy": "A Dishonourable Death", "class": "Currency", "type": "currency high"},
	"1 A Vision of Ice and Fire": {"prophecy": "A Vision of Ice and Fire", "class": "Currency", "type": "currency very high"},
	"1 Ancient Doom": {"prophecy": "Ancient Doom", "class": "Currency", "type": "currency high"},
	"1 Battle Hardened": {"prophecy": "Battle Hardened", "class": "Currency", "type": "currency high"},
	"1 Blind Faith": {"prophecy": "Blind Faith", "class": "Currency", "type": "currency high"},
	"1 Bountiful Traps": {"prophecy": "Bountiful Traps", "class": "Currency", "type": "currency high"},
	"1 Cleanser of Sins": {"prophecy": "Cleanser of Sins", "class": "Currency", "type": "currency very high"},
	"1 Dance of Steel": {"prophecy": "Dance of Steel", "class": "Currency", "type": "currency high"},
	"1 Darktongue's Shriek": {"prophecy": "Darktongue's Shriek", "class": "Currency", "type": "currency very high"},
	"1 Echoes of Witchcraft": {"prophecy": "Echoes of Witchcraft", "class": "Currency", "type": "currency high"},
	"1 Fallow At Last": {"prophecy": "Fallow At Last", "class": "Currency", "type": "currency very high"},
	"1 Fated Connections": {"prophecy": "Fated Connections", "class": "Currency", "type": "currency extremely high"},
	"1 Fire and Brimstone": {"prophecy": "Fire and Brimstone", "class": "Currency", "type": "currency high"},
	"1 Fire and Ice": {"prophecy": "Fire and Ice", "class": "Currency", "type": "currency high"},
	"1 Fire, Wood and Stone": {"prophecy": "Fire, Wood and Stone", "class": "Currency", "type": "currency high"},
	"1 Flesh of the Beast": {"prophecy": "Flesh of the Beast", "class": "Currency", "type": "currency high"},
	"1 Holding the Bridge": {"prophecy": "Holding the Bridge", "class": "Currency", "type": "currency high"},
	"1 Ice from Above": {"prophecy": "Ice from Above", "class": "Currency", "type": "currency high"},
	"1 In the Grasp of Corruption": {"prophecy": "In the Grasp of Corruption", "class": "Currency", "type": "currency extremely high"},
	"1 Living Fires": {"prophecy": "Living Fires", "class": "Currency", "type": "currency extremely high"},
	"1 Lost in the Pages": {"prophecy": "Lost in the Pages", "class": "Currency", "type": "currency high"},
	"1 Monstrous Treasure": {"prophecy": "Monstrous Treasure", "class": "Currency", "type": "currency very high"},
	"1 Pools of Wealth": {"prophecy": "Pools of Wealth", "class": "Currency", "type": "currency high"},
	"1 Song of the Sekhema": {"prophecy": "Song of the Sekhema", "class": "Currency", "type": "currency very high"},
	"1 The Apex Predator": {"prophecy": "The Apex Predator", "class": "Currency", "type": "currency high"},
	"1 The Beautiful Guide": {"prophecy": "The Beautiful Guide", "class": "Currency", "type": "currency high"},
	"1 The Bowstring's Music": {"prophecy": "The Bowstring's Music", "class": "Currency", "type": "currency high"},
	"1 The Child of Lunaris": {"prophecy": "The Child of Lunaris", "class": "Currency", "type": "currency very high"},
	"1 The Feral Lord V": {"prophecy": "The Feral Lord V", "class": "Currency", "type": "currency high"},
	"1 The Fortune Teller's Collection": {"prophecy": "The Fortune Teller's Collection", "class": "Currency", "type": "currency high"},
	"1 The Great Leader of the North": {"prophecy": "The Great Leader of the North", "class": "Currency", "type": "currency high"},
	"1 The Great Mind of the North": {"prophecy": "The Great Mind of the North", "class": "Currency", "type": "currency high"},
	"1 The Jeweller's Touch": {"prophecy": "The Jeweller's Touch", "class": "Currency", "type": "currency very high"},
	"1 The King's Path": {"prophecy": "The King's Path", "class": "Currency", "type": "currency very high"},
	"1 The Misunderstood Queen": {"prophecy": "The Misunderstood Queen", "class": "Currency", "type": "currency high"},
	"1 The Mysterious Gift": {"prophecy": "The Mysterious Gift", "class": "Currency", "type": "currency high"},
	"1 The Plaguemaw V": {"prophecy": "The Plaguemaw V", "class": "Currency", "type": "currency high"},
	"1 The Queen's Sacrifice": {"prophecy": "The Queen's Sacrifice", "class": "Currency", "type": "currency extremely high"},
	"1 The Queen's Vaults": {"prophecy": "The Queen's Vaults", "class": "Currency", "type": "currency high"},
	"1 The Servant's Heart": {"prophecy": "The Servant's Heart", "class": "Currency", "type": "currency high"},
	"1 The Unbreathing Queen V": {"prophecy": "The Unbreathing Queen V", "class": "Currency", "type": "currency very high"},
	"1 Trash to Treasure": {"prophecy": "Trash to Treasure", "class": "Currency", "type": "currency extremely high"},
	"1 Twice Enchanted": {"prophecy": "Twice Enchanted", "class": "Currency", "type": "currency very high"},
	"1 Unbearable Whispers V": {"prophecy": "Unbearable Whispers V", "class": "Currency", "type": "currency high"},
	"1 Undead Uprising": {"prophecy": "Undead Uprising", "class": "Currency", "type": "currency very high"},
	"1 Vaal Invasion": {"prophecy": "Vaal Invasion", "class": "Currency", "type": "currency high"},
	"1 Vaal Winds": {"prophecy": "Vaal Winds", "class": "Currency", "type": "currency very high"},
	"1 Visions of the Drowned": {"prophecy": "Visions of the Drowned", "class": "Currency", "type": "currency very low"},
	"1 Wind and Thunder": {"prophecy": "Wind and Thunder", "class": "Currency", "type": "currency very high"},
	"7 Prophecy default": {"Prophecy": "", "class": "Currency", "type": "currency low"}
}
