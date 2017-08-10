#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
from datetime import datetime
from os import path
from io import open

from auto_gen import divination
from auto_gen import hcdivination
from auto_gen import pdivination
from auto_gen import phcdivination
from auto_gen import uniques
from auto_gen import hcuniques
from auto_gen import puniques
from auto_gen import phcuniques
from auto_gen import currency as stcurrency
from auto_gen import hccurrency
from auto_gen import pcurrency
from auto_gen import phccurrency
from auto_gen import essence as stessence
from auto_gen import hcessence
from auto_gen import pessence
from auto_gen import phcessence


from item_config import animate_weapon
from item_config import challenges
from item_config import chance
from item_config import chroma
from item_config import crafting_bases
from item_config import currency
from item_config import essences
from item_config import flask
from item_config import gems
from item_config import general_levelling
from item_config import hide
from item_config import labyrinth
from item_config import maps
from item_config import nonrare_armor_dex
from item_config import nonrare_armor_dex_int
from item_config import nonrare_armor_int
from item_config import nonrare_armor_str
from item_config import nonrare_armor_str_dex
from item_config import nonrare_armor_str_int
from item_config import nonrare_bow
from item_config import nonrare_claw
from item_config import nonrare_dagger
from item_config import nonrare_jewelry
from item_config import nonrare_one_hand_axe
from item_config import nonrare_one_hand_mace
from item_config import nonrare_one_hand_sword
from item_config import nonrare_sceptre
from item_config import nonrare_staff
from item_config import nonrare_thrusting_one_hand_sword
from item_config import nonrare_two_hand_axe
from item_config import nonrare_two_hand_mace
from item_config import nonrare_two_hand_sword
from item_config import nonrare_wand
from item_config import rare_armor_dex
from item_config import rare_armor_dex_int
from item_config import rare_armor_int
from item_config import rare_armor_str
from item_config import rare_armor_str_dex
from item_config import rare_armor_str_int
from item_config import rare_bow
from item_config import rare_claw
from item_config import rare_dagger
from item_config import rare_highlight
from item_config import rare_one_hand_axe
from item_config import rare_one_hand_mace
from item_config import rare_one_hand_sword
from item_config import rare_sceptre
from item_config import rare_staff
from item_config import rare_thrusting_one_hand_sword
from item_config import rare_two_hand_axe
from item_config import rare_two_hand_mace
from item_config import rare_two_hand_sword
from item_config import rare_wand
from item_config import rares
from item_config import recipe_item
from item_config import show
from item_config import t1_rares
from item_config import warbands

from theme_config import formatting


def gen_list_full(items, desc):
#	print("Starting {}".format(obj))
	b = ""

	# gen our string
	for i in sorted(items):
		s = items[i]
		if s['type'] != "ignore":
			b += "#{} - {}\n".format(i, desc)
			if s['type'] == "hide":
				b += "Hide"
			else:
				b += "Show"
			if 'base' in s:
				b += "\n\tBaseType \"{}\"".format(s['base'])
			if 'class' in s:
				b += "\n\tClass \"{}\"".format(s['class'])
			if 'other' in s:
				b += "\n\t{}".format("\n\t".join(s['other']))
			if formatting.settings[s['type']]:
				b += "\n\t{}".format("\n\t".join(formatting.settings[s['type']]))
			else:
				print("Missing type field {} ** {}".format(items[i], i))
			b += "\n\n"

	return b


def gen_list_compact(items, desc):
#	print("Starting {}".format(obj))

	# gen our string
	l = {}
	for i in items:
		s = items[i]
		if s['type'] != "ignore":
			if not i.split()[0].isdigit():
				v = '0'
			else:
				v = i.split()[0]
			if v not in l:
				l[v] = {}

			c = ''
			f = ''
			o = ''
			b = ''
			t = 'Show'
			if s['type'] == "hide":
				t = "Hide"
			if 'base' in s:
				b = s['base']
			if 'class' in s:
				c = s['class']
			if 'other' in s:
				o = ",".join(s['other'])

			if formatting.settings[s['type']]:
				f = s['type']
			else:
				print("Missing type field {} ** {}".format(items[i], i))

			k = '{},{},{},{}'.format(t, c, f, o)
			if k in l[v]:
				l[v][k].append(b)
			else:
				l[v][k] = [b]
	b = ""
	for i in sorted(l.keys()):
		for ii in sorted(l[i].keys()):
			t, c, f, o = ii.split(',', maxsplit=3)
			b += "#{}\n".format(desc)
			b += t
			if l[i][ii][0]:
				b += "\n\tBaseType \"{}\"".format('" "'.join(sorted(l[i][ii])))
			if c:
				b += "\n\tClass \"{}\"".format(c)
			if o:
				b += "\n\t{}".format("\n\t".join(sorted(o.split(','))))
			if formatting.settings[f]:
				b += "\n\t{}".format("\n\t".join(sorted(formatting.settings[f])))
			else:
				print("Missing type field {} ** {}".format(items[i], i))
			b += "\n\n"
	return b


# main function for creating a filter
def main():
	# gen_list = gen_list_full
	gen_list = gen_list_compact
	leagues = [("st", "Standard", uniques, divination, stcurrency, stessence),
			   ("hc", "Hardcore", hcuniques, hcdivination, hccurrency, hcessence),
			   ("t", "Temp Standard", puniques, pdivination, pcurrency, pessence),
			   ("thc", "Temp Hardcore", phcuniques, phcdivination, phccurrency, phcessence)]

	leveling = True  # toggle to show leveling items

	for i in leagues:

		buffer = """#**************************************************************
# Welcome to xan.filter, a Python generated loot filter for PoE
# This filter was generated for {} on {} UTC
# The most current version of code can always be found at https://github.com/xanthics/poe_filter
#**************************************************************

""".format(i[1], datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'))

		buffer += gen_list(show.items, show.desc)  # Always show these items
		buffer += gen_list(hide.items, hide.desc)  # Always hide these items
		if i[0] not in ['st', 'hc']:
			buffer += gen_list(challenges.items, challenges.desc)
		buffer += gen_list(labyrinth.items, labyrinth.desc)
		buffer += gen_list(i[4].items, i[4].desc)  # Autogen currency values
		# buffer += gen_list(essences.items, essences.desc)  # Essences
		buffer += gen_list(i[5].items, i[5].desc)  # Autogen Essences
		buffer += gen_list(currency.items, currency.desc)  # Currency
		buffer += gen_list(gems.items, gems.desc)  # Gems
		buffer += gen_list(i[2].items, i[2].desc)  # uniques
		buffer += gen_list(recipe_item.items, recipe_item.desc)  # Items for vendor recipe
		buffer += gen_list(maps.items, maps.desc)  # maps
		buffer += gen_list(i[3].items, i[3].desc)  # divination cards
		buffer += gen_list(flask.items, flask.desc)  # Flasks
		buffer += gen_list(t1_rares.items, t1_rares.desc)
		if leveling:
			buf = {}
			desc = rare_armor_dex.desc
			for rareitemleveling in [rare_armor_dex, rare_armor_dex_int, rare_armor_str_dex, rare_armor_str, rare_armor_int, rare_armor_str_int, rare_bow, rare_claw, rare_dagger, rare_one_hand_sword,
									 rare_one_hand_mace, rare_one_hand_axe, rare_sceptre, rare_staff, rare_thrusting_one_hand_sword, rare_two_hand_sword, rare_two_hand_mace, rare_two_hand_axe, rare_wand]:
				buf.update(rareitemleveling.items)
			buffer += gen_list(buf, desc)

		buffer += gen_list(rare_highlight.items, rare_highlight.desc)  # rares highlighting + jewelry
		buffer += gen_list(rares.items, rares.desc)  # rares catchall
		buffer += gen_list(chroma.items, chroma.desc)  # chrome vendor items
		if leveling:
			buffer += gen_list(general_levelling.items, general_levelling.desc)
		buffer += gen_list(chance.items, chance.desc)  # Chance bases
		buffer += gen_list(crafting_bases.items, crafting_bases.desc)  # Crafting bases
		# buffer += gen_list(animate_weapon.items, animate_weapon.desc)  # Animate Weapon bases

		if leveling:
			buf = {}
			desc = rare_armor_dex.desc
			for nonrareitemleveling in [nonrare_armor_dex, nonrare_armor_dex_int, nonrare_armor_str_dex, nonrare_armor_str, nonrare_armor_int, nonrare_armor_str_int, nonrare_bow, nonrare_claw, nonrare_dagger,
										nonrare_jewelry, nonrare_one_hand_sword, nonrare_one_hand_mace, nonrare_one_hand_axe, nonrare_sceptre, nonrare_staff,
										nonrare_thrusting_one_hand_sword, nonrare_two_hand_sword, nonrare_two_hand_mace, nonrare_two_hand_axe, nonrare_wand]:
				buf.update(nonrareitemleveling.items)
			buffer += gen_list(buf, desc)

		buffer += gen_list(warbands.items, warbands.desc)  # Warband base type highlighting

		print("Writing files to {}".format(path.expanduser("~\\my game\\Path of Exile\\")))

		with open("xan.{}.show.filter".format(i[0]), "w", encoding='utf-8') as f:
			f.write(buffer)
			# Default for all other items
			f.write("Show\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")
		with open(path.expanduser(r"~\Documents\my games\Path of Exile\xan.{}.show.filter".format(i[0])), "w", encoding='utf-8') as f:
			f.write(buffer)
			# Default for all other items
			f.write("Show\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")

		with open("xan.{}.hide.filter".format(i[0]), "w", encoding='utf-8') as f:
			f.write(buffer)
			# Default for all other items
			f.write("Hide\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")
		with open(path.expanduser(r"~\Documents\my games\Path of Exile\xan.{}.hide.filter".format(i[0])), "w", encoding='utf-8') as f:
			f.write(buffer)
			# Default for all other items
			f.write("Hide\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")


if __name__ == "__main__":
	main()
