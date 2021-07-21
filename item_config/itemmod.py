#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Magic items"


# Mods for rare only
def raremods():
	modtoitem = {'Entombing': ["Rune Daggers", "Dagger", "Sceptre", "Wand"],
				 'Cremating': ["Rune Daggers", "Dagger", "Sceptre", "Wand"],
				 'Electrocuting': ["Rune Daggers", "Dagger", "Sceptre", "Wand"],
				 'Crystalising': ["Claw", "Rune Daggers", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Wand", "Bow", "Warstaves", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 'Carbonising': ["Claw", "Rune Daggers", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Wand", "Bow", "Warstaves", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 'Vapourising': ["Claw", "Rune Daggers", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Wand", "Bow", "Warstaves", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 'Malicious': ["Claw", "Rune Daggers", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Wand", "Bow", "Warstaves", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 "Tul's": ["Sceptre", "Wand", "Dagger", "Stave"],
				 "Xoph's": ["Sceptre", "Wand", "Dagger", "Stave"],
				 "Esh's": ["Sceptre", "Wand", "Dagger", "Stave"],
				 'Runic': ["Sceptre", "Wand", "Dagger", "Stave"],
				 "Flame Shaper's": ["Sceptre", "Wand", "Dagger", "Stave", "Shield"],
				 "Frost Singer's": ["Sceptre", "Wand", "Dagger", "Stave", "Shield"],
				 "Thunderhand's": ["Sceptre", "Wand", "Dagger", "Stave", "Shield"],
				 "Martinet's": ["Sceptre", "Wand", "Dagger", "Stave", "Shield"],
				 "Mad Lord's": ["Sceptre", "Wand", "Dagger", "Stave", "Shield"],
				 "Lithomancer's": ["Sceptre", "Wand", "Dagger", "Stave", "Shield"],
				 'of Unmaking': ["Sceptre", "Wand", "Dagger", "Stave"],

				 'Prime': ["Body Armour"],
				 'Athlete\'s': ["Boots", "Gloves", "Amulet"],
				 'Fecund': ["Helmet", "Belt"],
				 'Vigorous': ["Shield"],
				 'Virile': ["Ring"],
				 'of Bameth': ["Body Armour", "Boots", "Gloves", "Helmet", "Shield", "Amulet", "Belt", "Ring"],
				 'of Haast': ["Body Armour", "Boots", "Gloves", "Helmet", "Shield", "Amulet", "Belt", "Ring"],
				 'of Tzteosh': ["Body Armour", "Boots", "Gloves", "Helmet", "Shield", "Amulet", "Belt", "Ring"],
				 'of Ephij': ["Body Armour", "Boots", "Gloves", "Helmet", "Shield", "Amulet", "Belt", "Ring"],
				 'Hellion\'s': ["Boots"],
				 'Cheetah\'s': ["Boots"],
				 #'Dragon\'s': ["Helmet"],
				 #'of Excavation': ["Helmet", "Amulet", "Ring"],
				 'of the Span': ["Shield", "Amulet"],
				 'of the Rainbow': ["Shield", "Amulet"],
				 'Devastating': ["Amulet", "Belt"],
				 #'Perandus\'': ["Amulet", "Ring"],
				 'of Expertise': ["Amulet"],
				 'of the Assassin': ["Amulet"],
				 'of the Infinite': ["Amulet"],
				 'of the Multiverse': ["Amulet"],
				 'of Overflowing': ["Belt"],
				 'of Sipping': ["Belt"],
				 'of Savouring': ["Belt"],
				 'of the Godslayer': ['Belt'],
				 'of Talent': ["Ring"],
				 'of Skill': ["Ring"],
				 'Flawless': ["Ring"],
				 }

	ret = {}

	for mod in modtoitem:
		for item in modtoitem[mod]:
			keyval = "3 {}".format(item)
			if keyval in ret:
				ret[keyval]['other'][0] += ' "{}"'.format(mod)
			else:
				ret[keyval] = {"type": "item mod"}
				ret[keyval]['class'] = item
				ret[keyval]['other'] = ['HasExplicitMod "{}"'.format(mod), 'Rarity Rare']

	return ret


# mods for any rarity
def magicmods():
	modtoitem = {'Dictator\'s': ["Claw", "Rune Daggers", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Wand", "Bow", "Warstaves", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 'Merciless': ["Claw", "Rune Daggers", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Wand", "Bow", "Warstaves", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 'Flaring': ["Claw", "Rune Daggers", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Wand", "Bow", "Warstaves", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword", "Amulet"],

				 # Veiled mods so they can be eventually disabled when unlocked
				 "Veiled": [
					 "Claw", "Rune Daggers", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre",
					 "Wand",
					 "Bow",
					 "Warstaves", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword",
					 "Body Armour",
					 "Boots",
					 "Gloves",
					 "Helmet",
					 "Shield",
					 "Amulet",
					 "Belt",
					 "Ring",
					 "Quiver"
				 ],

				 }

	modtoitem["of the Veil"] = modtoitem["Veiled"].copy()

	modanyitem = ['Eldritch', "The Shaper's", 'of the Elder', 'of Shaping',
				  "Subterranean", "of the Underground",
				  # "of Weaponcraft", "of Spellcraft",
				  "of Crafting",

				  "Catarina's Veiled",  # weapons, shields
				  "Elreon's Veiled",  # rings, amulets
				  "Gravicius' Veiled",  # Body Armour
				  "Guff's Veiled",  # gloves
				  "Haku's Veiled",  # weapon, shield
				  "It That Fled's Veiled",  # weapon, shield
				  "Korell's Veiled",  # helmet
				  "Leo's Veiled",  # ring, belt
				  "Rin's Veiled",  # boots
				  "Tora's Veiled",  # weapons
				  "Vagan's Veiled",  # melee weapon
				  "Vorici's Veiled",  # gloves, amulets

				  "of Aisling's Veil",  # ring
				  "of Cameria's Veil",  # ring
				  "of Hillock's Veil",  # body armour
				  "of Janus' Veil",  # helmet
				  "of Jorgin's Veil",  # amulet
				  "of Riker's Veil",  # ring

				  "Citaqualotl's", "Guatelitzi's", "Matatl's", "of Puhuarte", "of Tacati", "Tacati's", "Topotante's", "Xopec's",
				  "Brinerot", "Mutewind", "Redblade", "Betrayer\'s", "Deceiver\'s", "Turncoat\'s",
				  # Bestiary mods by themselves are not that useful
				  # "of Farrul", "of Craiceann", "of Fenumus", "of Saqawal",
				 ]

	ret = {'0 Item Mod': {'other': ['HasExplicitMod "{}"'.format('" "'.join(modanyitem))], "type": "item mod"}}

	for mod in modtoitem:
		for item in modtoitem[mod]:
			keyval = "1 {}".format(item)
			if keyval in ret:
				ret[keyval]['other'][0] += ' "{}"'.format(mod)
			else:
				ret[keyval] = {"type": "item mod"}
				ret[keyval]['class'] = item
				ret[keyval]['other'] = ['HasExplicitMod "{}"'.format(mod)]

	return ret


# "Claw", "Rune Daggers", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Wand", "Bow", "Warstaves", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"
# , "Body Armour", "Boots", "Gloves", "Helmet", "Shield"
# , "Amulet", "Belt", "Ring"
# , "Jewel", "Abyss Jewel"
def itemmods():
	veiled = ["Leo's Veiled", "Vagan's Veiled", "Catarina's Veiled", "Elreon's Veiled"]

	return {'9 Item Mod': {'other': ['HasExplicitMod "{}"'.format('" "'.join(veiled))], "type": "rare highlight"}, **magicmods(), **raremods()}


if __name__ == '__main__':
	rets = itemmods()
	for i in rets:
		print(i, rets[i])
