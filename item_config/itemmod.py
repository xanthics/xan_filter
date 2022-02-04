#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
from collections import defaultdict

desc = "Magic items"


# Mods for rare only
def raremods():
	item_groups = {
		'caster': ["Rune Daggers", "Stave", "Sceptre", "Wand"],
		'attack': ["Claw", "Rune Daggers", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Wand", "Bow", "Warstaves", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
		'stave': ["Stave"],
		'chest': ["Body Armour"],
		'boot_glove_amulet': ["Boots", "Gloves", "Amulet"],
		'boot_glove': ["Boots", "Gloves"],
		'helmet_belt': ["Helmet", "Belt"],
		'helmet': ["Helmet"],
		'shield': ["Shield"],
		'ring': ["Ring"],
		'amulet': ["Amulet"],
		'belt': ["Belt"],
		'def_gear': ["Body Armour", "Boots", "Gloves", "Helmet", "Shield", "Amulet", "Belt", "Ring"],
		'boots': ["Boots"],
		'glove': ["Gloves"],
		'shield_amulet': ["Shield", "Amulet"],
		'amulet_belt': ["Amulet", "Belt"],
	}
	mod_groups = {
		'caster': [
			'Entombing', 'Polar',
			'Cremating', 'Blasting',
			'Electrocuting', 'Discharging',
			"Tul's", "Cryomancer's", 'of Glaciation', 'of Floe',
			"Xoph's", 'Pyroclastic', 'of Ashes', 'of Immolation',
			"Esh's", 'Ionising', 'of Arcing', 'of Discharge',
			'Runic', 'Glyphic',
			'of Unmaking', 'of Ruin',
			"Lich's", "Archmage's",
			'of Finesse', 'of Sortilege',
			'of Destruction', 'of Ferocity',
			'of Conflagrating', 'of Combusting',
			'of Dissolution', 'of Melting',
			'of Disintegrating', 'of Atrophying',
			'of Heartstopping', 'of the Gelid',
			'of the Fanatical', 'of the Zealous',
		],
		'attack': [
			'Crystalising', 'Entombing',
			'Carbonising', 'Cremating',
			'Vapourising', 'Electrocuting',
			'Malicious',
			"Dictator's", "Emperor's",
			'Merciless', 'Tyrannical',
			'Flaring', 'Tempered',
			'Devastating', 'Overpowering',
			'of Acclaim', 'of Renown',
			'of Incision', 'of Penetrating',
			'of Destruction', 'of Ferocity',
			'of Dissolution', 'of Melting',
			'of Disintegrating', 'of Atrophying',
			'of the Fanatical', 'of the Zealous',
			'of Exsanguinating', 'of Hemorrhaging'
		],
		'stave': [
			"Lava Conjurer's",
			"Winter Beckoner's",
			"Tempest Master's",
			"Splintermind's",
			"Tecton's"
		],
		'chest': [
			'Prime', 'Rapturous',
			'Resplendent', 'Incandescent',
			'Unassailable', 'Indomitable',
			'Unfaltering'
		],
		'boot_glove_amulet': [
			"Athlete's", 'Virile',
		],
		'boot_glove': [
			'Seething', 'Pulsing',
			'Unassailable', 'Indomitable',
			"Prior's"
		],
		'helmet_belt': [
			'Fecund', "Athlete's"
		],
		'helmet': [
			"Blazing", 'Seething',
			'Unassailable', 'Indomitable',
			"Necromancer's"
		],
		'shield': [
			'Vigorous', 'Fecund',
			'Incandescent', 'Scintillating',
			'Unfaltering', 'Unassailable', 'Indomitable',
			'of Unmaking', 'of Ruin',
			'Impenetrable', 'Impregnable',
			'Unmoving', 'Abating',
			"Victor's", "Legend's",
			"Adaptable", "Resilient",
			'of Nullification'
		],
		'ring': [
			'Virile', 'Rotund',
			'of Talent',
			'of Skill',
			'Flawless',
			'of the Comet',
			'of the Rainbow', 'of Variegation'
		],
		'amulet': [
			'of Expertise',
			'of the Assassin',
			'of the Multiverse', 'of the Infinite',
			'of Incision', 'of Penetrating',
			'of Destruction', 'of Ferocity',
			'of Dissolution', 'of Melting'
		],
		'belt': [
			'of Overflowing', 'of Brimming',
			'of Sipping',
			'of Reveling', 'of Relishing',
			'of the Godslayer',
			'Magnifying',
			'Dazzling', 'Resplendent',
		],
		'def_gear': [
			'of Bameth', 'of Exile',
			'of Haast', 'of the Ice',
			'of Tzteosh', 'of the Magma',
			'of Ephij', 'of the Lightning',
			'of the Gods', 'of the Titan',
			'of the Wind', 'of the Phantom',
			'of the Genius', 'of the Virtuoso',
			"Exarch's", "Abbot's", "Prior's"
		],
		'boots': [
			"Hellion's", "Cheetah's", "Gazelle's"
		],
		'glove': [
			"Honed",
			'Burning',
			'Frigid',
			'Crackling',
			'of Grandmastery', 'of Mastery'
		],
		'shield_amulet': [
			'of the Span', 'of the Rainbow'
		],
		'amulet_belt': [
			'Devastating', 'Overpowering'
		],
	}

	itemtomods = defaultdict(set)

	for i_set in item_groups:
		for base in item_groups[i_set]:
			for mod in mod_groups[i_set]:
				itemtomods[base].add(mod)
	ret = {}

	for item in itemtomods:
		keyval = "3 {}".format(item)
		ret[keyval] = {"type": "item mod"}
		ret[keyval]['class'] = item
		ret[keyval]['other'] = ['HasExplicitMod >=2 "{}"'.format('" "'.join(itemtomods[item])), 'Rarity Rare']

	return ret


# mods for any rarity
def magicmods():
	modtoitem = {"Magister's": ["Sceptre", "Wand", "Dagger",  "Stave", "Shield"],
				 "Flame Shaper's": ["Sceptre", "Wand", "Dagger", "Shield"],
				 "Frost Singer's": ["Sceptre", "Wand", "Dagger", "Shield"],
				 "Thunderhand's": ["Sceptre", "Wand", "Dagger", "Shield"],
				 "Martinet's": ["Sceptre", "Wand", "Dagger", "Shield"],
				 "Mad Lord's": ["Sceptre", "Wand", "Dagger", "Shield"],
				 "Lithomancer's": ["Sceptre", "Wand", "Dagger","Shield"],
				 # Veiled mods so they can be eventually disabled when unlocked
				 "Veiled": [
					 "Claw", "Rune Daggers", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre",
					 "Wand",
					 "Bow",
					 "Warstaves", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword",
					 "Body Armour",
					 "Gloves",
					 "Boots",
					 "Helmet",
					 "Shield",
					 "Amulet",
					 "Belt",
					 "Ring",
					 "Quiver"
				 ],

				 }

	modtoitem["of the Veil"] = modtoitem["Veiled"].copy()

	modanyitem = [#'Eldritch', "The Shaper's", 'of the Elder', 'of Shaping',
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

#	return {'9 Item Mod': {'other': ['HasExplicitMod "{}"'.format('" "'.join(veiled))], "type": "rare highlight"}, **magicmods(), **raremods()}
	return {**magicmods(), **raremods()}
#	return raremods()


if __name__ == '__main__':
	rets = itemmods()
	for i in rets:
		print(i, rets[i])
