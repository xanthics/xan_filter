#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Magic items"


# Mods for rare only
def raremods():
	modtoitem = {'Entombing': ["Dagger", "Sceptre", "Wand"],
				 'Cremating': ["Dagger", "Sceptre", "Wand"],
				 'Electrocuting': ["Dagger", "Sceptre", "Wand"],
				 'Crystalising': ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 'Carbonising': ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 'Heart-Stopping': ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 'Malicious': ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 'Tul\'s': ["Sceptre", "Wand", "Stave"],
				 'Xoph\'s': ["Sceptre", "Wand", "Stave"],
				 'Esh\'s': ["Sceptre", "Wand", "Stave"],
				 'Runic': ["Sceptre", "Wand", "Stave"],
				 'of Unmaking': ["Sceptre", "Wand", "Stave"],

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
	modtoitem = {'Dictator\'s': ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 'Merciless': ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 'Flaring': ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword", "Amulet"],

				 # Veiled mods so they can be eventually disabled when unlocked
				 "Veiled": [
					 "Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword",
					 "Wand",
					 "Bow",
					 "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword",
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

				 "of the Veil": [
					 "Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword",
					 "Wand",
					 "Bow",
					 "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword",
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

	modanyitem = ['Eldritch', "The Shaper's", 'of the Elder', 'of Shaping',
				  "Subterranean", "of the Underground",
				  # "of Weaponcraft", "of Spellcraft",
				  "of Crafting",

				  "Catarina's Veiled",
				  "Elreon's Veiled",
				  "Gravicius' Veiled",
				  "Guff's Veiled",
				  "Haku's Veiled",
				  "It That Fled's Veiled",
				  "Korell's Veiled",
				  "Leo's Veiled",
				  "Rin's Veiled",
				  "Tora's Veiled",
				  "Vagan's Veiled",
				  "Vorici's Veiled",

				  "of Aisling's Veil",
				  "of Cameria's Veil",
				  "of Hillock's Veil",
				  "of Janus' Veil",
				  "of Jorgin's Veil",
				  "of Riker's Veil",

				  "Citaqualotl's", "Guatelitzi's", "Matatl's", "of Puhuarte", "of Tacati", "Tacati's", "Topotante's", "Xopec's",
				  "Brinerot", "Mutewind", "Redblade", "Betrayer\'s", "Deceiver\'s", "Turncoat\'s",
				  "of Farrul", "of Craiceann", "of Fenumus", "of Saqawal",
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


# "Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"
# , "Body Armour", "Boots", "Gloves", "Helmet", "Shield"
# , "Amulet", "Belt", "Ring"
# , "Jewel", "Abyss Jewel"
def itemmods():
	return {**magicmods(), **raremods()}


if __name__ == '__main__':
	rets = itemmods()
	for i in rets:
		print(i, rets[i])
