#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
import importlib
from datetime import datetime
import os
from io import open

import pricetool_ninja
from item_config import animate_weapon, show_catchall
from item_config import challenges
from item_config import chance
from item_config import chroma
from item_config import flask
from item_config import gems
from item_config import general_levelling
from item_config import hide
from item_config import labyrinth
from item_config import maps
from item_config import recipe_item
from item_config import show
from item_config.gen_item_lists import genraresleveling, gennonrareleveling, genrareshighlighttiered
from item_config.itemmod import itemmods

from theme_config import formatting
from theme_config.min_w_highlight import volume
from wav_mixer import convert_wav
from gen_always_highlight_currency import create_always_highlight



def gen_list_compact(items, desc):
	#	print("Starting {}".format(obj))

	# gen our string
	l = {}
	from pprint import pprint
	for item in items:
		sitem = items[item]
		if sitem['type'] != "ignore":
			if not item.split()[0].isdigit():
				firstval = '1'
			else:
				firstval = item.split()[0]
			if firstval not in l:
				l[firstval] = {}
			# Prophecy and BaseType will not appear in the same rule (personal choice)
			# have a flag that is 0(neither), 1(Base), 2(prophecy), 3(enchant)
			class_ = ''
			type_ = ''
			other = ''
			base = ''
			flag = 0
			influence = None
			t = 'Show'
			if sitem['type'] == "hide":
				t = "Hide"
			if 'base' in sitem:
				base = sitem['base']
				flag = 1
			elif 'prophecy' in sitem:
				base = sitem['prophecy']
				flag = 2
			elif 'enchant' in sitem:
				base = sitem['enchant']
				flag = 3
			elif 'baseexact' in sitem:
				base = sitem['baseexact']
				flag = 4
			if 'class' in sitem:
				class_ = sitem['class']
			if 'other' in sitem:
				getcustomsound(sitem['other'], soundlist)
				other = ",".join(sitem['other'])
			if 'influence' in sitem:
				influence = sitem['influence']

			if formatting.settings[sitem['type']]:
				type_ = sitem['type']
			else:
				print("Missing type field {} ** {}".format(items[item], item))

			k = '{}|{}|{}|{}|{}'.format(t, class_, type_, flag, other)
			if k not in l[firstval]:
				l[firstval][k] = {}
			if influence in l[firstval][k]:
				l[firstval][k][influence].append(base)
			else:
				l[firstval][k][influence] = [base]
	base = ""
	for item in sorted(l.keys()):
		for ii in sorted(l[item].keys()):
			# build item->influence lists
			itemlist = {}
			influencelist = {}
			for influence in l[item][ii]:
				if influence:
					for ba in l[item][ii][influence]:
						if ba not in itemlist:
							itemlist[ba] = []
						itemlist[ba].append(influence)
				else:
					influencelist[None] = l[item][ii][None][:]
			# convert previous list to influences->bases
			for itl in itemlist:
				key = " ".join(sorted(itemlist[itl]))
				if key in influencelist:
					influencelist[key].append(itl)
				else:
					influencelist[key] = [itl]

			t, class_, type_, flag, other = ii.split('|')

			for influence in influencelist:
				base += "#{}\n".format(desc)
				base += t
				if flag == '1':
					base += "\n\tBaseType \"{}\"".format('" "'.join(influencelist[influence]))
				elif flag == '2':
					base += "\n\tProphecy == \"{}\"".format('" "'.join(influencelist[influence]))
				elif flag == '3':
					base += "\n\tHasEnchantment == \"{}\"".format('" "'.join(influencelist[influence]))
				elif flag == '4':
					base += "\n\tBaseType == \"{}\"".format('" "'.join(influencelist[influence]))
				elif flag == '5':  # merge on class
					base += "\n\tClass \"{}\"".format('" "'.join(influencelist[influence]))
				if class_:
					base += "\n\tClass \"{}\"".format(class_)
				if influence:
					base += "\n\tHasInfluence {}".format(influence)
				if other:
					base += "\n\t{}".format("\n\t".join(sorted(other.split(','))))
				if formatting.settings[type_]:
					if formatting.settings[type_][0]:
						getcustomsound(formatting.settings[type_], soundlist)
						base += "\n\t{}".format("\n\t".join(sorted(formatting.settings[type_])))
				else:
					print("Missing type field {} ** {}".format(items[item], item))
				base += "\n\tDisableDropSound True"
				base += "\n\n"

	return base


def get_poe_path():
	try:
		from win32com.shell import shell, shellcon
		userDir = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0)
	except ImportError:
		import ctypes.wintypes
		CSIDL_PERSONAL = 5  # My Documents
		SHGFP_TYPE_CURRENT = 0  # Get current, not default value
		buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
		ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
		userDir = buf.value
		#userDir = os.path.expanduser('~')

	poeDir = os.path.join(userDir, "My Games", "Path of Exile")
	return poeDir


# Helper function to convert a league name to a file prefix
def convertname(league):
	if league == 'Standard':
		return ""
	elif league == 'Hardcore':
		return "hc"
	elif 'tmphardcore' in league:
		return "thc"
	else:
		return "t"

# main function for creating a filter
def main(league='tmpstandard'):
	gen_list = gen_list_compact

	leveling = False  # toggle to show leveling items

	buffer = """#**************************************************************
# Welcome to xan.filter, a Python generated loot filter for PoE
# This filter was generated for {} on {} UTC
# The most current version of code can always be found at https://github.com/xanthics/poe_filter
#**************************************************************

""".format(league, datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'))
	buffer += gen_list(show.items, show.desc)  # Always show these items
	buffer += gen_list(hide.items, hide.desc)  # Always hide these items
	buffer += gen_list(challenges.items, challenges.desc)
	buffer += gen_list(custom_challenge.items, custom_challenge.desc)
	buffer += gen_list(convert_json_to_filter(), "Autogen filter rules")
	buffer += gen_list(labyrinth.items, labyrinth.desc)
	buffer += gen_list(gems.items, gems.desc)  # Gems
	buffer += gen_list(recipe_item.items, recipe_item.desc)  # Items for vendor recipe
	buffer += gen_list(maps.items, maps.desc)  # maps
	buffer += gen_list(flask.items, flask.desc)  # Flasks
	buffer += gen_list(chance.items, chance.desc)  # Chance bases
	buffer += gen_list(itemmods(), "Items Mods")  # mod based highlighting

	league = convertname(league)
	if leveling:
		desc = "Rare item for leveling"
		flags = 'All'  # see item_config/rare_gen - genraresleveling for valid values
		buffer += gen_list(genraresleveling(flags, overlevel=3, maxlevel=64), desc)

	buffer += gen_list(genrareshighlighttiered(), 'Rare item highlighting for endgame')

	buffer += gen_list(chroma.items, chroma.desc)  # chrome vendor items
	if leveling:
		buffer += gen_list(general_levelling.items, general_levelling.desc)
	# buffer += gen_list(animate_weapon.items, animate_weapon.desc)  # Animate Weapon bases

	if leveling:
		desc = 'item for leveling'
		flags = ['All']  # 'All'  # see item_config/rare_gen - genraresleveling for valid values
		buffer += gen_list(gennonrareleveling(flags, overlevel=2, maxlevel=25), desc)

	buffer += gen_list(show_catchall.items, show_catchall.desc)  # Always show these items

	poeDir = get_poe_path()
	print("Writing files to: {}".format(poeDir))

	with open("xan.{}.show.filter".format(league), "w", encoding='utf-8') as f:
		f.write(buffer)
		# Default for all other items
		f.write("Show\n\tDisableDropSound True\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")
	with open(os.path.join(poeDir, "xan.{}.show.filter".format(league)), "w", encoding='utf-8') as f:
		f.write(buffer)
		# Default for all other items
		f.write("Show\n\tDisableDropSound True\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")

	with open("xan.{}.hide.filter".format(league), "w", encoding='utf-8') as f:
		f.write(buffer)
		# Default for all other items
		f.write("Hide\n\tDisableDropSound True\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")
	with open(os.path.join(poeDir, "xan.{}.hide.filter".format(league)), "w", encoding='utf-8') as f:
		f.write(buffer)
		# Default for all other items
		f.write("Hide\n\tDisableDropSound True\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")


if __name__ == "__main__":
	create_always_highlight()
	league = 'tmpstandard'
	pricetool_ninja.scrape_ninja(league)
	# reload updated modules
	importlib.reload(custom_challenge)
	main(league)
