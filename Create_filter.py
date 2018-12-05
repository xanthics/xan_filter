#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
import importlib
from datetime import datetime
import os
from io import open
from zipfile import ZipFile

from auto_gen import divination
from auto_gen import hcdivination
from auto_gen import tdivination
from auto_gen import thcdivination
from auto_gen import uniques
from auto_gen import hcuniques
from auto_gen import tuniques
from auto_gen import thcuniques
from auto_gen import currency as stcurrency
from auto_gen import hccurrency
from auto_gen import tcurrency
from auto_gen import thccurrency
from auto_gen import essence as stessence
from auto_gen import hcessence
from auto_gen import tessence
from auto_gen import thcessence
from auto_gen import bases
from auto_gen import hcbases
from auto_gen import tbases
from auto_gen import thcbases


from item_config import animate_weapon, show_catchall
from item_config import challenges
from item_config import chance
from item_config import chroma
from item_config import currency
from item_config import essences
from item_config import flask
from item_config import gems
from item_config import general_levelling
from item_config import hide
from item_config import labyrinth
from item_config import maps
from item_config import recipe_item
from item_config import show
from item_config.gen_item_lists import genrareshighlight, genraresleveling, gennonrareleveling
from item_config.itemmod import itemmods

from theme_config import formatting
from wav_mixer import convert_wav


# Input is a list
def getcustomsound(flags, soundlist):
	if "Custom" in str(flags):
		for val in flags:
			if val.startswith('CustomAlertSound'):
				sound = val.split('"')[1][:-4]
				if sound not in soundlist:
					soundlist.append(sound)


def gen_list_compact(items, desc, soundlist):
#	print("Starting {}".format(obj))

	# gen our string
	l = {}
	for i in items:
		s = items[i]
		if s['type'] != "ignore":
			if not i.split()[0].isdigit():
				v = '1'
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
				getcustomsound(s['other'], soundlist)
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
				getcustomsound(formatting.settings[f], soundlist)
				b += "\n\t{}".format("\n\t".join(sorted(formatting.settings[f])))
			else:
				print("Missing type field {} ** {}".format(items[i], i))
			b += "\n\tDisableDropSound True"
			b += "\n\n"
	return b


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


# main function for creating a filter
def main(leagues=('Standard', 'Hardcore', 'tmpstandard', 'tmphardcore')):
	gen_list = gen_list_compact
	lookup_leagues = {'Standard': ("st", "Standard", uniques, divination, stcurrency, stessence, bases),
					  'Hardcore': ("hc", "Hardcore", hcuniques, hcdivination, hccurrency, hcessence, hcbases),
					  'tmpstandard': ("t", "Temp Sofcore", tuniques, tdivination, tcurrency, tessence, tbases),
					  'tmphardcore': ("thc", "Temp Hardcore", thcuniques, thcdivination, thccurrency, thcessence, thcbases)}

	leveling = True  # toggle to show leveling items
	soundlist = []
	for i in leagues:

		buffer = """#**************************************************************
# Welcome to xan.filter, a Python generated loot filter for PoE
# This filter was generated for {} on {} UTC
# The most current version of code can always be found at https://github.com/xanthics/poe_filter
#**************************************************************

""".format(lookup_leagues[i][1], datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'))

		buffer += gen_list(show.items, show.desc, soundlist)  # Always show these items
		buffer += gen_list(hide.items, hide.desc, soundlist)  # Always hide these items
		if lookup_leagues[i][0] not in ['st', 'hc']:
			buffer += gen_list(challenges.items, challenges.desc, soundlist)
		buffer += gen_list(labyrinth.items, labyrinth.desc, soundlist)
		buffer += gen_list(lookup_leagues[i][4].items, lookup_leagues[i][4].desc, soundlist)  # Autogen currency values
		buffer += gen_list(lookup_leagues[i][5].items, lookup_leagues[i][5].desc, soundlist)  # Autogen Essences
		buffer += gen_list(currency.items, currency.desc, soundlist)  # Currency
		buffer += gen_list(gems.items, gems.desc, soundlist)  # Gems
		buffer += gen_list(lookup_leagues[i][2].items, lookup_leagues[i][2].desc, soundlist)  # uniques
		# buffer += gen_list(recipe_item.items, recipe_item.desc, soundlist)  # Items for vendor recipe
		buffer += gen_list(maps.items, maps.desc, soundlist)  # maps
		buffer += gen_list(lookup_leagues[i][3].items, lookup_leagues[i][3].desc, soundlist)  # divination cards
		buffer += gen_list(flask.items, flask.desc, soundlist)  # Flasks
		buffer += gen_list(lookup_leagues[i][6].items, lookup_leagues[i][6].desc, soundlist)  # Autogen Bases

		buffer += gen_list(itemmods(), "Items Mods", soundlist)  # mod based highlighting

		if leveling:
			desc = "Rare item for leveling"
			flags = 'All'  # see item_config/rare_gen - genraresleveling for valid values
			buffer += gen_list(genraresleveling(flags, overlevel=3, maxlevel=67), desc, soundlist)

		buffer += gen_list(genrareshighlight(), 'Rare item highlighting for endgame', soundlist)
		# buffer += gen_list(chroma.items, chroma.desc, soundlist)  # chrome vendor items
		if leveling:
			buffer += gen_list(general_levelling.items, general_levelling.desc, soundlist)
		buffer += gen_list(chance.items, chance.desc, soundlist)  # Chance bases
		# buffer += gen_list(animate_weapon.items, animate_weapon.desc, soundlist)  # Animate Weapon bases

		if leveling:
			desc = 'item for leveling'
			flags = ['Weapon']  # 'All'  # see item_config/rare_gen - genraresleveling for valid values
			buffer += gen_list(gennonrareleveling(flags, overlevel=2, maxlevel=25), desc, soundlist)

		buffer += gen_list(show_catchall.items, show_catchall.desc, soundlist)  # Always show these items

		poeDir = get_poe_path()
		print("Writing files to: {}".format(poeDir))

		with open("xan.{}.show.filter".format(lookup_leagues[i][0]), "w", encoding='utf-8') as f:
			f.write(buffer)
			# Default for all other items
			f.write("Show\n\tDisableDropSound True\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")
		with open(os.path.join(poeDir, "xan.{}.show.filter".format(lookup_leagues[i][0])), "w", encoding='utf-8') as f:
			f.write(buffer)
			# Default for all other items
			f.write("Show\n\tDisableDropSound True\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")

		with open("xan.{}.hide.filter".format(lookup_leagues[i][0]), "w", encoding='utf-8') as f:
			f.write(buffer)
			# Default for all other items
			f.write("Hide\n\tDisableDropSound True\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")
		with open(os.path.join(poeDir, "xan.{}.hide.filter".format(lookup_leagues[i][0])), "w", encoding='utf-8') as f:
			f.write(buffer)
			# Default for all other items
			f.write("Hide\n\tDisableDropSound True\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")

	# Delete existing wav files before creating new ones
	for file in os.listdir('filter_sounds'):
		os.remove(os.path.join('filter_sounds', file))
	if os.path.isfile('soundpack.zip'):
		os.remove('soundpack.zip')
	for file in os.listdir(poeDir):
		if file.endswith('.wav'):
			os.remove(os.path.join(poeDir, file))
	# Create requested sound files
	for track in soundlist:
		i, sound = track.split('_', maxsplit=1)
		convert_wav(int(i), sound, poeDir)
	# Create sound pack
	with ZipFile('soundpack.zip', 'w') as zipper:
		for track in soundlist:
			zipper.write('filter_sounds/{}.wav'.format(track), arcname='{}.wav'.format(track))


if __name__ == "__main__":
	import pricetool_ninja
#	league = ['Standard', 'Hardcore', 'tmpstandard', 'tmphardcore']
	league = ['Standard']
	pricetool_ninja.scrape_ninja(league)
	# reload updated modules
	for module in [divination, hcdivination, tdivination, thcdivination,
				   uniques, hcuniques, tuniques, thcuniques,
				   stcurrency, hccurrency, tcurrency, thccurrency,
				   stessence, hcessence, tessence, thcessence,
				   bases, hcbases, tbases, thcbases]:
		importlib.reload(module)
	main(league)
