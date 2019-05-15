#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 05/15/2019(m/d/y) 09:17:17 UTC from "Hardcore" data

desc = "Prophecy Autogen"

# Base type : settings pair
items = {
	"000 Thaumaturgical History III": {"prophecy": "Thaumaturgical History III", "class": "Currency", "type": "currency low"},
	"001 Thaumaturgical History II": {"prophecy": "Thaumaturgical History II", "class": "Currency", "type": "currency low"},
	"002 Thaumaturgical History IV": {"prophecy": "Thaumaturgical History IV", "class": "Currency", "type": "currency high"},
	"003 The Unbreathing Queen III": {"prophecy": "The Unbreathing Queen III", "class": "Currency", "type": "currency low"},
	"004 The Unbreathing Queen IV": {"prophecy": "The Unbreathing Queen IV", "class": "Currency", "type": "currency high"},
	"005 The Ambitious Bandit III": {"prophecy": "The Ambitious Bandit III", "class": "Currency", "type": "currency high"},
	"006 The Unbreathing Queen II": {"prophecy": "The Unbreathing Queen II", "class": "Currency", "type": "currency low"},
	"007 Unbearable Whispers III": {"prophecy": "Unbearable Whispers III", "class": "Currency", "type": "currency low"},
	"008 The Ambitious Bandit II": {"prophecy": "The Ambitious Bandit II", "class": "Currency", "type": "currency low"},
	"009 Unbearable Whispers II": {"prophecy": "Unbearable Whispers II", "class": "Currency", "type": "currency low"},
	"010 Unbearable Whispers IV": {"prophecy": "Unbearable Whispers IV", "class": "Currency", "type": "currency low"},
	"011 Day of Sacrifice III": {"prophecy": "Day of Sacrifice III", "class": "Currency", "type": "currency low"},
	"012 Day of Sacrifice II": {"prophecy": "Day of Sacrifice II", "class": "Currency", "type": "currency low"},
	"013 Deadly Rivalry III": {"prophecy": "Deadly Rivalry III", "class": "Currency", "type": "currency low"},
	"014 The Warmongers III": {"prophecy": "The Warmongers III", "class": "Currency", "type": "currency low"},
	"015 The Feral Lord III": {"prophecy": "The Feral Lord III", "class": "Currency", "type": "currency low"},
	"016 The Warmongers IV": {"prophecy": "The Warmongers IV", "class": "Currency", "type": "currency low"},
	"017 The Warmongers II": {"prophecy": "The Warmongers II", "class": "Currency", "type": "currency low"},
	"018 Deadly Rivalry IV": {"prophecy": "Deadly Rivalry IV", "class": "Currency", "type": "currency low"},
	"019 The Feral Lord IV": {"prophecy": "The Feral Lord IV", "class": "Currency", "type": "currency low"},
	"020 The Plaguemaw III": {"prophecy": "The Plaguemaw III", "class": "Currency", "type": "currency low"},
	"021 The Feral Lord II": {"prophecy": "The Feral Lord II", "class": "Currency", "type": "currency low"},
	"022 Anarchy's End III": {"prophecy": "Anarchy's End III", "class": "Currency", "type": "currency low"},
	"023 Deadly Rivalry II": {"prophecy": "Deadly Rivalry II", "class": "Currency", "type": "currency low"},
	"024 Anarchy's End IV": {"prophecy": "Anarchy's End IV", "class": "Currency", "type": "currency high"},
	"025 The Plaguemaw IV": {"prophecy": "The Plaguemaw IV", "class": "Currency", "type": "currency high"},
	"026 The Plaguemaw II": {"prophecy": "The Plaguemaw II", "class": "Currency", "type": "currency low"},
	"027 Beyond Sight III": {"prophecy": "Beyond Sight III", "class": "Currency", "type": "currency low"},
	"028 Anarchy's End II": {"prophecy": "Anarchy's End II", "class": "Currency", "type": "currency low"},
	"029 Beyond Sight II": {"prophecy": "Beyond Sight II", "class": "Currency", "type": "currency low"},
	"030 Beyond Sight IV": {"prophecy": "Beyond Sight IV", "class": "Currency", "type": "currency high"},
	"1 A Master Seeks Help": {"prophecy": "A Master Seeks Help", "class": "Currency", "type": "currency high"},
	"1 A Vision of Ice and Fire": {"prophecy": "A Vision of Ice and Fire", "class": "Currency", "type": "currency high"},
	"1 Bountiful Traps": {"prophecy": "Bountiful Traps", "class": "Currency", "type": "currency high"},
	"1 Cleanser of Sins": {"prophecy": "Cleanser of Sins", "class": "Currency", "type": "currency very high"},
	"1 Darktongue's Shriek": {"prophecy": "Darktongue's Shriek", "class": "Currency", "type": "currency high"},
	"1 Fated Connections": {"prophecy": "Fated Connections", "class": "Currency", "type": "currency extremely high"},
	"1 Fire from the Sky": {"prophecy": "Fire from the Sky", "class": "Currency", "type": "currency high"},
	"1 Heavy Blows": {"prophecy": "Heavy Blows", "class": "Currency", "type": "currency very low"},
	"1 Ice from Above": {"prophecy": "Ice from Above", "class": "Currency", "type": "currency high"},
	"1 Kalandra's Craft": {"prophecy": "Kalandra's Craft", "class": "Currency", "type": "currency high"},
	"1 Lost in the Pages": {"prophecy": "Lost in the Pages", "class": "Currency", "type": "currency high"},
	"1 Monstrous Treasure": {"prophecy": "Monstrous Treasure", "class": "Currency", "type": "currency very high"},
	"1 Plague of Rats": {"prophecy": "Plague of Rats", "class": "Currency", "type": "currency high"},
	"1 Song of the Sekhema": {"prophecy": "Song of the Sekhema", "class": "Currency", "type": "currency high"},
	"1 The Bowstring's Music": {"prophecy": "The Bowstring's Music", "class": "Currency", "type": "currency very high"},
	"1 The Fall of an Empire": {"prophecy": "The Fall of an Empire", "class": "Currency", "type": "currency very low"},
	"1 The Feral Lord V": {"prophecy": "The Feral Lord V", "class": "Currency", "type": "currency high"},
	"1 The Flayed Man": {"prophecy": "The Flayed Man", "class": "Currency", "type": "currency very low"},
	"1 The Jeweller's Touch": {"prophecy": "The Jeweller's Touch", "class": "Currency", "type": "currency very high"},
	"1 The King's Path": {"prophecy": "The King's Path", "class": "Currency", "type": "currency high"},
	"1 The Plaguemaw V": {"prophecy": "The Plaguemaw V", "class": "Currency", "type": "currency high"},
	"1 The Queen's Sacrifice": {"prophecy": "The Queen's Sacrifice", "class": "Currency", "type": "currency extremely high"},
	"1 The Servant's Heart": {"prophecy": "The Servant's Heart", "class": "Currency", "type": "currency high"},
	"1 The Sinner's Stone": {"prophecy": "The Sinner's Stone", "class": "Currency", "type": "currency very low"},
	"1 The Unbreathing Queen V": {"prophecy": "The Unbreathing Queen V", "class": "Currency", "type": "currency very high"},
	"1 The Undead Storm": {"prophecy": "The Undead Storm", "class": "Currency", "type": "currency high"},
	"1 Twice Enchanted": {"prophecy": "Twice Enchanted", "class": "Currency", "type": "currency high"},
	"1 Unbearable Whispers V": {"prophecy": "Unbearable Whispers V", "class": "Currency", "type": "currency high"},
	"1 Vaal Winds": {"prophecy": "Vaal Winds", "class": "Currency", "type": "currency high"},
	"1 Wind and Thunder": {"prophecy": "Wind and Thunder", "class": "Currency", "type": "currency high"},
	"7 Prophecy default": {"Prophecy": "", "class": "Currency", "type": "currency low"}
}
