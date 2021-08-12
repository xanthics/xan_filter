#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
import importlib
from datetime import datetime
import os
from io import open
import time

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
from item_config import uniform_color
from item_config.gen_item_lists import genraresleveling, gennonrareleveling, genrareshighlighttiered
from item_config.itemmod import itemmods

from autogen import custom_challenge, custom_ex_shard_recipe
from gen_always_highlight_currency import create_always_highlight
from theme_config.min_w_highlight import settings
from process_ninja_json import convert_json_to_filter
import wav_mixer


def gen_list_compact(items, desc):
	#	print("Starting {}".format(obj))
	# gen our string
	item_dict = {}
	# A list of actions so we can always make sure they are after conditions
	actions = ['CustomAlertSound', 'DisableDropSound', 'EnableDropSound', 'MinimapIcon', 'PlayAlertSound', 'PlayAlertSoundPositional', 'PlayEffect', 'SetBackgroundColor', 'SetBorderColor', 'SetFontSize', 'SetTextColor']
	for item in items:
		item_info = items[item]
		if item_info['type'] != "ignore":
			if not item.split()[0].isdigit():
				firstval = '1'
			else:
				firstval = item.split()[0]
			if firstval not in item_dict:
				item_dict[firstval] = {}
			# Prophecy and BaseType will not appear in the same rule (personal choice)
			# have a flag that is 0(neither), 1(Base), 2(prophecy), 3(enchant)
			class_ = ''
			formatting = []
			base = ''
			flag = 0
			influence = None
			t = 'Show'
			if item_info['type'] == "hide":
				t = "Hide"
			if 'base' in item_info:
				base = item_info['base']
				flag = 1
			elif 'prophecy' in item_info:
				base = item_info['prophecy']
				flag = 2
			elif 'enchant' in item_info:
				base = item_info['enchant']
				flag = 3
			elif 'baseexact' in item_info:
				base = item_info['baseexact']
				flag = 4
			elif 'class' in item_info:  # merge on class
				base = item_info['class']
				del item_info['class']
				flag = 5
			if 'class' in item_info:
				class_ = item_info['class']
			if 'other' in item_info:
				formatting.extend(item_info['other'])
			if 'influence' in item_info:
				influence = item_info['influence']
			if settings[item_info['type']]:
				formatting.extend(settings[item_info['type']])
			else:
				print("Missing type field {} ** {}".format(items[item], item))
				exit(-1)

			# sort - rules should be before styles
			t_actions = []
			for i in list(formatting):
				if any(i.startswith(x) for x in actions):
					t_actions.append(i)
					formatting.remove(i)
			formatting.sort()
			t_actions.sort()
			formatting.extend(t_actions)

			c = wav_mixer.convert_sound_reference(formatting)
			if c[0] > -1:
				formatting[c[0]] = f"{formatting[c[0]].replace(c[1], c[2])} {c[3]}"
			other = ",".join(formatting)

			# converted to string to it is easier to see if different objects have the same formatting
			k = f'{t}|{class_}|{flag}|{other}'
			if k not in item_dict[firstval]:
				item_dict[firstval][k] = {}
			if influence in item_dict[firstval][k]:
				item_dict[firstval][k][influence].append(base)
			else:
				item_dict[firstval][k][influence] = [base]
	base = ""
	for item in sorted(item_dict.keys()):
		for ii in sorted(item_dict[item].keys()):
			# build item->influence lists
			itemlist = {}
			influencelist = {}
			for influence in item_dict[item][ii]:
				if influence:
					for ba in item_dict[item][ii][influence]:
						if ba not in itemlist:
							itemlist[ba] = []
						itemlist[ba].append(influence)
				else:
					influencelist[None] = item_dict[item][ii][None][:]
			# convert previous list to influences->bases
			for itl in itemlist:
				key = " ".join(sorted(itemlist[itl]))
				if key in influencelist:
					influencelist[key].append(itl)
				else:
					influencelist[key] = [itl]

			t, class_, flag, other = ii.split('|')

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
					base += "\n\t{}".format("\n\t".join(other.split(',')))
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

	leveling = True  # toggle to show leveling items

	buffer = """#**************************************************************
# Welcome to xan.filter, a Python generated loot filter for PoE
# This filter was generated for {} on {} UTC
# The most current version of code can always be found at https://github.com/xanthics/poe_filter
#**************************************************************

# Disable drop sounds
Show
	DisableDropSound True
	Continue

""".format(league, datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'))
	league = convertname(league)

	buffer += gen_list_compact(uniform_color.items, uniform_color.desc)  # Text color rules first since they use Continue
	buffer += gen_list_compact(show.items, show.desc)  # Always show these items
	buffer += gen_list_compact(hide.items, hide.desc)  # Always hide these items
	buffer += gen_list_compact(challenges.items, challenges.desc)
	buffer += gen_list_compact(custom_challenge.items, custom_challenge.desc)
	buffer += gen_list_compact(convert_json_to_filter(), "Autogen filter rules")
	buffer += gen_list_compact(labyrinth.items, labyrinth.desc)
	buffer += gen_list_compact(gems.items, gems.desc)  # Gems
	buffer += gen_list_compact(maps.items, maps.desc)  # maps
	buffer += gen_list_compact(flask.items, flask.desc)  # Flasks
	buffer += gen_list_compact(chance.items, chance.desc)  # Chance bases
	buffer += gen_list_compact(itemmods(), "Items Mods")  # mod based highlighting

	if leveling:
		desc = "Rare item for leveling"
		flags = 'All'  # see item_config/rare_gen - genraresleveling for valid values
		buffer += gen_list_compact(genraresleveling(flags, overlevel=3, maxlevel=64), desc)

	buffer += gen_list_compact(genrareshighlighttiered(), 'Rare item highlighting for endgame')

	buffer += gen_list_compact(chroma.items, chroma.desc)  # chrome vendor items
	if leveling:
		buffer += gen_list_compact(general_levelling.items, general_levelling.desc)
	# buffer += gen_list(animate_weapon.items, animate_weapon.desc)  # Animate Weapon bases

	if leveling:
		desc = 'item for leveling'
		flags = ['Accessory', 'Axe', 'Sword']  # 'All'  # see item_config/rare_gen - genraresleveling for valid values
		buffer += gen_list_compact(gennonrareleveling(flags, overlevel=25, maxlevel=25), desc)
		flags = ['All']  # see item_config/rare_gen - genraresleveling for valid values
		buffer += gen_list_compact(gennonrareleveling(flags, overlevel=2, maxlevel=25), desc)

	buffer += gen_list_compact(recipe_item.items, recipe_item.desc)  # Items for vendor recipe
	buffer += gen_list_compact(custom_ex_shard_recipe.items, custom_ex_shard_recipe.desc)  # autogen rules for ex shard recipe items
	buffer += gen_list_compact(show_catchall.items, show_catchall.desc)  # Always show these items

	poeDir = get_poe_path()
	print("Writing files to: {}".format(poeDir))

	with open("xan.{}.show.filter".format(league), "w", encoding='utf-8') as f:
		f.write(buffer)
		# Default for all other items
		f.write("Show\n\tSetFontSize 18\n\tSetBorderColor 100 100 100")
	with open(os.path.join(poeDir, "xan.{}.show.filter".format(league)), "w", encoding='utf-8') as f:
		f.write(buffer)
		# Default for all other items
		f.write("Show\n\tSetFontSize 18\n\tSetBorderColor 100 100 100")

	with open("xan.{}.hide.filter".format(league), "w", encoding='utf-8') as f:
		f.write(buffer)
		# Default for all other items
		f.write("Hide\n\tSetFontSize 18\n\tSetBorderColor 100 100 100")
	with open(os.path.join(poeDir, "xan.{}.hide.filter".format(league)), "w", encoding='utf-8') as f:
		f.write(buffer)
		# Default for all other items
		f.write("Hide\n\tSetFontSize 18\n\tSetBorderColor 100 100 100")


# check that poe.ninja hasn't been checked 'recently'
def last_ninja():
	n_val = int(time.time())
	if os.path.isfile('last_ninja_check'):
		last = int(open('last_ninja_check').readline())
		if n_val - last < 3600:
			return False
	open('last_ninja_check', 'w').write(str(n_val))
	return True


if __name__ == "__main__":
	create_always_highlight()
	g_league = 'tmpstandard'
	if last_ninja():
		pricetool_ninja.scrape_ninja(g_league)
	# reload updated modules
	importlib.reload(custom_challenge)
	importlib.reload(custom_ex_shard_recipe)
	main(g_league)
