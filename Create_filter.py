#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
* Copyright (c) 2015 Jeremy Parks. All rights reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a
* copy of this software and associated documentation files (the "Software"),
* to deal in the Software without restriction, including without limitation
* the rights to use, copy, modify, merge, publish, distribute, sublicense,
* and/or sell copies of the Software, and to permit persons to whom the
* Software is furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
* DEALINGS IN THE SOFTWARE.

Author: Jeremy Parks
Purpose: Create an item filter based on config files
Note: Requires Python 3.4.x
"""

import chance
import general_levelling
import hide
import nonrare_armor_dex
import nonrare_armor_dex_int
import nonrare_armor_int
import nonrare_armor_str
import nonrare_armor_str_dex
import nonrare_armor_str_int
import nonrare_bow
import nonrare_claw
import nonrare_dagger
import nonrare_jewelry
import nonrare_one_hand_axe
import nonrare_one_hand_mace
import nonrare_one_hand_sword
import nonrare_sceptre
import nonrare_thrusting_one_hand_sword
import nonrare_two_hand_axe
import nonrare_two_hand_mace
import nonrare_two_hand_sword
import nonrare_wand
import nonrare_staff
import rare_armor_dex
import rare_armor_dex_int
import rare_armor_int
import rare_armor_str
import rare_armor_str_dex
import rare_armor_str_int
import rare_bow
import rare_claw
import rare_dagger
import rare_one_hand_axe
import rare_one_hand_mace
import rare_one_hand_sword
import rare_sceptre
import rare_thrusting_one_hand_sword
import rare_two_hand_axe
import rare_two_hand_mace
import rare_two_hand_sword
import rare_wand
import rare_staff
import show
import currency
import gems
import uniques
import maps
import divination
import chroma
import flask
import rares
import rare_highlight
import crafting_bases
import recipe_item
import t1_rares
import formatting
from os import path


def gen_list(obj):
	print("Starting {}".format(obj))
	b = ""

	# gen our string
	for i in sorted(obj.items):
		s = obj.items[i]
		if s['type'] != "ignore":
			b += "#{} - {}\n".format(i, obj.desc)
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
				print("Missing type field {} ** {}".format(obj, i))
			b += "\n\n"

	return b


# main function for creating a filter
def main():

	leveling = False  # toggle to show leveling items

	buffer = ""

	buffer += gen_list(show)  # Always show these items
	buffer += gen_list(hide)  # Always hide these items
	buffer += gen_list(currency)  # Currency
	buffer += gen_list(gems)  # Gems
	buffer += gen_list(uniques)  # uniques
	buffer += gen_list(recipe_item)  # Items for vendor recipe
	buffer += gen_list(maps)  # maps
	buffer += gen_list(divination)  # divination cards
	buffer += gen_list(flask)  # Flasks
	buffer += gen_list(t1_rares)
	if leveling:
		for rareitemleveling in [rare_armor_dex, rare_armor_dex_int, rare_armor_str_dex, rare_armor_str, rare_armor_int,
						 rare_armor_str_int, rare_bow, rare_claw, rare_dagger, rare_one_hand_sword, rare_one_hand_mace,
						 rare_one_hand_axe, rare_sceptre, rare_staff, rare_thrusting_one_hand_sword,
						 rare_two_hand_sword, rare_two_hand_mace, rare_two_hand_axe, rare_wand]:
			buffer += gen_list(rareitemleveling)

	buffer += gen_list(rare_highlight)  # rares highlighting + jewelry
	buffer += gen_list(rares)  # rares catchall
	buffer += gen_list(chroma)  # chrome vendor items
	if leveling:
		buffer += gen_list(general_levelling)
	buffer += gen_list(chance)  # Chance bases
	buffer += gen_list(crafting_bases)  # Crafting bases

	if leveling:
		for nonrareitemleveling in [nonrare_armor_dex, nonrare_armor_dex_int, nonrare_armor_str_dex, nonrare_armor_str,
									nonrare_armor_int, nonrare_armor_str_int, nonrare_bow, nonrare_claw, nonrare_dagger,
									nonrare_jewelry, nonrare_one_hand_sword, nonrare_one_hand_mace,
									nonrare_one_hand_axe, nonrare_sceptre, nonrare_staff,
									nonrare_thrusting_one_hand_sword, nonrare_two_hand_sword, nonrare_two_hand_mace,
									nonrare_two_hand_axe, nonrare_wand]:
			buffer += gen_list(nonrareitemleveling)

	print("Writing files to {}".format(path.expanduser("~/my game/Path of Exile/")))

	with open("xan.show.filter", "w") as f:
		f.write(buffer)
		# Default for all other items
		f.write("Show\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")
	with open(path.expanduser(r"~\Documents\my games\Path of Exile\xan.show.filter"), "w") as f:
		f.write(buffer)
		# Default for all other items
		f.write("Show\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")

	with open("xan.hide.filter", "w") as f:
		f.write(buffer)
		# Default for all other items
		f.write("Hide\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")
	with open(path.expanduser(r"~\Documents\my games\Path of Exile\xan.hide.filter"), "w") as f:
		f.write(buffer)
		# Default for all other items
		f.write("Hide\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")


if __name__ == "__main__":
	main()
