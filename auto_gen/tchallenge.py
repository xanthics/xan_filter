#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 07/15/2019(m/d/y) 23:54:31 UTC from "tmpstandard" data

desc = "Challenge Autogen"

# Base type : settings pair
items = {
	"1 Abyssal Incubator": {"base": "Abyssal Incubator", 'other': ['CustomAlertSound "45_challenge10.wav"'], "class": "Incubator", "type": "challenge normal"},
	"1 Cartographer's Incubator": {"base": "Cartographer's Incubator", 'other': ['CustomAlertSound "75_challenge12.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Celestial Armoursmith's Incubator": {"base": "Celestial Armoursmith's Incubator", 'other': ['CustomAlertSound "75_challenge14.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Celestial Blacksmith's Incubator": {"base": "Celestial Blacksmith's Incubator", 'other': ['CustomAlertSound "75_challenge14.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Celestial Jeweller's Incubator": {"base": "Celestial Jeweller's Incubator", 'other': ['CustomAlertSound "75_challenge12.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Decadent Incubator": {"base": "Decadent Incubator", 'other': ['CustomAlertSound "75_challenge12.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Diviner's Incubator": {"base": "Diviner's Incubator", 'other': ['CustomAlertSound "75_challenge12.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Eldritch Incubator": {"base": "Eldritch Incubator", 'other': ['CustomAlertSound "75_challenge11.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Enchanted Incubator": {"base": "Enchanted Incubator", 'other': ['CustomAlertSound "75_challenge15.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Fine Incubator": {"base": "Fine Incubator", 'other': ['CustomAlertSound "75_challenge15.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Foreboding Incubator": {"base": "Foreboding Incubator", 'other': ['CustomAlertSound "75_challenge11.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Fossilised Incubator": {"base": "Fossilised Incubator", 'other': ['CustomAlertSound "75_challenge12.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Fragmented Incubator": {"base": "Fragmented Incubator", 'other': ['CustomAlertSound "75_challenge12.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Gemcutter's Incubator": {"base": "Gemcutter's Incubator", 'other': ['CustomAlertSound "45_challenge9.wav"'], "class": "Incubator", "type": "challenge normal"},
	"1 Geomancer's Incubator": {"base": "Geomancer's Incubator", 'other': ['CustomAlertSound "100_challenge13.wav"'], "class": "Incubator", "type": "challenge very high"},
	"1 Infused Incubator": {"base": "Infused Incubator", 'other': ['CustomAlertSound "75_challenge15.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Mysterious Incubator": {"base": "Mysterious Incubator", 'other': ['CustomAlertSound "75_challenge14.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Obscured Incubator": {"base": "Obscured Incubator", 'other': ['CustomAlertSound "75_challenge11.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Ornate Incubator": {"base": "Ornate Incubator", 'other': ['CustomAlertSound "75_challenge12.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Otherworldly Incubator": {"base": "Otherworldly Incubator", 'other': ['CustomAlertSound "75_challenge11.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Primal Incubator": {"base": "Primal Incubator", 'other': ['CustomAlertSound "45_challenge6.wav"'], "class": "Incubator", "type": "challenge normal"},
	"1 Singular Incubator": {"base": "Singular Incubator", 'other': ['CustomAlertSound "75_challenge14.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Skittering Incubator": {"base": "Skittering Incubator", 'other': ['CustomAlertSound "75_challenge15.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Thaumaturge's Incubator": {"base": "Thaumaturge's Incubator", 'other': ['CustomAlertSound "75_challenge11.wav"'], "class": "Incubator", "type": "challenge high"},
	"1 Time-Lost Incubator": {"base": "Time-Lost Incubator", 'other': ['CustomAlertSound "100_challenge11.wav"'], "class": "Incubator", "type": "challenge very high"},
	"1 Timeless Eternal Emblem": {"base": "Timeless Eternal Emblem", 'other': ['CustomAlertSound "75_challenge14.wav"'], "class": "Map Fragments", "type": "challenge high"},
	"1 Timeless Eternal Empire Splinter": {"base": "Timeless Eternal Empire Splinter", 'other': ['CustomAlertSound "20_challenge3.wav"'], "class": "Currency", "type": "challenge show"},
	"09 Timeless Eternal Empire Splinter": {"base": "Timeless Eternal Empire Splinter", 'other': ['StackSize >= 3', 'CustomAlertSound "45_challenge9.wav"'], "class": "Currency", "type": "challenge normal"},
	"08 Timeless Eternal Empire Splinter": {"base": "Timeless Eternal Empire Splinter", 'other': ['StackSize >= 9', 'CustomAlertSound "75_challenge14.wav"'], "class": "Currency", "type": "challenge high"},
	"1 Timeless Karui Emblem": {"base": "Timeless Karui Emblem", 'other': ['CustomAlertSound "75_challenge11.wav"'], "class": "Map Fragments", "type": "challenge high"},
	"1 Timeless Karui Splinter": {"base": "Timeless Karui Splinter", 'other': ['CustomAlertSound "20_challenge1.wav"'], "class": "Currency", "type": "challenge show"},
	"09 Timeless Karui Splinter": {"base": "Timeless Karui Splinter", 'other': ['StackSize >= 4', 'CustomAlertSound "45_challenge9.wav"'], "class": "Currency", "type": "challenge normal"},
	"08 Timeless Karui Splinter": {"base": "Timeless Karui Splinter", 'other': ['StackSize >= 15', 'CustomAlertSound "75_challenge11.wav"'], "class": "Currency", "type": "challenge high"},
	"1 Timeless Maraketh Emblem": {"base": "Timeless Maraketh Emblem", 'other': ['CustomAlertSound "175_challenge11.wav"'], "class": "Map Fragments", "type": "challenge extremely high"},
	"1 Timeless Maraketh Splinter": {"base": "Timeless Maraketh Splinter", 'other': ['CustomAlertSound "75_challenge15.wav"'], "class": "Currency", "type": "challenge high"},
	"09 Timeless Maraketh Splinter": {"base": "Timeless Maraketh Splinter", 'other': ['StackSize >= 9', 'CustomAlertSound "100_challenge15.wav"'], "class": "Currency", "type": "challenge very high"},
	"08 Timeless Maraketh Splinter": {"base": "Timeless Maraketh Splinter", 'other': ['StackSize >= 95', 'CustomAlertSound "175_challenge15.wav"'], "class": "Currency", "type": "challenge extremely high"},
	"1 Timeless Templar Emblem": {"base": "Timeless Templar Emblem", 'other': ['CustomAlertSound "100_challenge11.wav"'], "class": "Map Fragments", "type": "challenge very high"},
	"1 Timeless Templar Splinter": {"base": "Timeless Templar Splinter", 'other': ['CustomAlertSound "45_challenge5.wav"'], "class": "Currency", "type": "challenge normal"},
	"09 Timeless Templar Splinter": {"base": "Timeless Templar Splinter", 'other': ['StackSize >= 2', 'CustomAlertSound "75_challenge12.wav"'], "class": "Currency", "type": "challenge high"},
	"08 Timeless Templar Splinter": {"base": "Timeless Templar Splinter", 'other': ['StackSize >= 27', 'CustomAlertSound "100_challenge14.wav"'], "class": "Currency", "type": "challenge very high"},
	"1 Timeless Vaal Emblem": {"base": "Timeless Vaal Emblem", 'other': ['CustomAlertSound "100_challenge12.wav"'], "class": "Map Fragments", "type": "challenge very high"},
	"1 Timeless Vaal Splinter": {"base": "Timeless Vaal Splinter", 'other': ['CustomAlertSound "20_challenge1.wav"'], "class": "Currency", "type": "challenge show"},
	"09 Timeless Vaal Splinter": {"base": "Timeless Vaal Splinter", 'other': ['StackSize >= 2', 'CustomAlertSound "45_challenge7.wav"'], "class": "Currency", "type": "challenge normal"},
	"08 Timeless Vaal Splinter": {"base": "Timeless Vaal Splinter", 'other': ['StackSize >= 7', 'CustomAlertSound "75_challenge13.wav"'], "class": "Currency", "type": "challenge high"},
	"1 Whispering Incubator": {"base": "Whispering Incubator", 'other': ['CustomAlertSound "45_challenge7.wav"'], "class": "Incubator", "type": "challenge normal"},
}
