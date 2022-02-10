#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
from collections import defaultdict


desc = "challenge item"


# Base type : settings pair
items = {
	"1 Exotic Coinage": {"baseexact": "Exotic Coinage", "class": "Currency", "type": "challenge normal"},
	"1 Scrap Metal": {"baseexact": "Scrap Metal", "class": "Currency", "type": "challenge normal"},
	"1 Astragali": {"baseexact": "Astragali", "class": "Currency", "type": "challenge normal"},
	"1 Burial Medallion": {"baseexact": "Burial Medallion", "class": "Currency", "type": "challenge normal"},

#	"1 Archnemesis Items Maps": {"class": "Archnemesis Mod", "other": ["ItemLevel >= 68"], "type": "challenge normal"},
	"9 Archnemesis Items Catchall": {"class": "Archnemesis Mod", "type": "challenge low"},
	# initial Heist highlighting
	"2 Heist Any": {"class": "Heist", "type": "challenge low"},
	"1 Trinket": {"class": "Trinket", "type": "challenge high"},
	"1 Blueprint": {"class": "Blueprint", "type": "challenge high"},

	"1 Expedition Logbook": {"class": "Expedition Logbook", "type": "challenge high"},

	"0 Contract": {"other": ["ItemLevel >= 83"], "class": "Contract", "type": "challenge high"},
#	"1 Contract": {"other": ["ItemLevel >= 75"], "class": "Contract", "type": "challenge normal"},
	"2 Contract": {"class": "Contract", "type": "challenge low"},
}

for base in [
	'Sharpening Stone', 'Arrowhead', 'Focal Stone', 'Conduit Line', 'Aggregator Charm', 'Burst Band',
	'Lockpick',  # Karst
	'Bracers',  # Tibbs
	'Drill',  # Isla
	'Sole',  # Tullina
	'Ward',  # Niles
	'Sensing Charm',  # Nenet
	'Flashpowder',  # Vinderi
	'Keyring',  # Vinderi
	'Disguise Kit',  # Gianna
	'Cloak',
	'Brooch'
]:
	items[f"1 Heist {base} 83+"] = {'base': base, "class": "Heist", "other": ["ItemLevel >= 83"], "type": "challenge normal"}

archnem_parts = {
	# Basic Drops
	'Arcane Buffer': {},  # Essences
	'Berserker': {},  # Uniques
	'Bloodletter': {},  # Weapon, Trinkets - Items dropped from the Monster and its Minions are Corrupted
	'Bombardier': {},  # Weapon, Armour
	'Bonebreaker': {},  # Generic, Weapon
	'Chaosweaver': {},  # Gems
	'Consecrator': {},  # Fragments
	'Deadeye': {},  # Armour, Trinkets
	'Dynamo': {},  # Generic, Trinkets
	'Echoist': {},  # Generic, Currency
	'Flameweaver': {},  # Weapon
	'Frenzied': {},  # Generic, Uniques
	'Frostweaver': {},  # Armour
	'Gargantuan': {},  # Currency
	'Hasted': {},  # Generic
	'Incendiary': {},  # Generic, Weapon
	'Juggernaut': {},  # Harbinger
	'Malediction': {},  # Divination Cards
	'Opulent': {},  # Monster is fabulously wealthy
	'Overcharged': {},  # Trinkets, Trinkets
	'Permafrost': {},  # Generic, Armour
	'Sentinel': {},  # Armour Armour
	'Soul Conduit': {},  # Maps
	'Steel-infused': {},  # Weapon
	'Stormweaver': {},  # Trinkets
	'Toxic': {},  # Generic Gems
	'Vampiric': {},  # Fossils
	# Basic Recipes
	'Executioner': {'Frenzied', 'Berserker'},  # Legion Breach
	'Necromancer': {'Overcharged', 'Bombardier'},  # Generic - Rewards are rolled 2 additional times, choosing the rarest result
	# Intermediate Recipes
	'Empowering Minions': {'Executioner', 'Gargantuan', 'Necromancer'},  # Blight, Ritual
	'Flame Strider': {'Hasted', 'Flameweaver'},  # Weapon, Weapon, Weapon
	'Frost Strider': {'Hasted', 'Frostweaver'},  # Armour, Armour, Armour
	'Invulnerable': {'Sentinel', 'Consecrator', 'Juggernaut'},  # Delirium, Metamorphosis
	'Magma Barrier': {'Bonebreaker', 'Incendiary'},  # Weapon, Weapon - Rewards are rolled 1 additional time, choosing the rarest result
	'Rejuvenating': {'Vampiric', 'Gargantuan'},  # Currency - Rewards are rolled 1 additional time, choosing the rarest result
	# Complex Recipes
	'Abberath-touched': {'Frenzied', 'Flame Strider', 'Rejuvenating'},  # Trinkets, Trinkets, Maps - Rewards are rolled 4 additional times, choosing the rarest result
	'Assassin': {'Deadeye', 'Vampiric'},  # Currency, Currency
	'Corpse Detonator': {'Necromancer', 'Incendiary'},  # Divination Cards, Divination Cards
	'Corrupter': {'Chaosweaver', 'Bloodletter'},  # Abyss, Abyss - Items dropped from the Monster and its Minions are Corrupted
	'Drought Bringer': {'Malediction', 'Deadeye'},  # Labyrinth Labyrinth
	'Entangler': {'Bloodletter', 'Toxic'},  # Fossils, Fossils
	'Evocationist': {'Stormweaver', 'Flameweaver', 'Frostweaver'},  # Generic, Weapon, Armour, Trinkets
	'Heralding Minions': {'Dynamo', 'Arcane Buffer'},  # Fragments, Fragments
	'Hexer': {'Chaosweaver', 'Echoist'},  # Essences, Essences
	'Ice Prison': {'Permafrost', 'Sentinel'},  # Armour Armour - Rewards are rolled 1 additional time, choosing the rarest result
	'Lunaris-touched': {'Frost Strider', 'Invulnerable', 'Empowering Minions'},  # Uniques - All Reward Types have an additional reward
	'Mana Siphoner': {'Consecrator', 'Dynamo'},  # Trinkets, Trinkets - Rewards are rolled 1 additional time, choosing the rarest result
	'Mirror Image': {'Soul Conduit', 'Echoist'},  # Scarabs - Rewards are rolled 2 additional times, choosing the rarest result
	'Solaris-touched': {'Magma Barrier', 'Invulnerable', 'Empowering Minions'},  # Scarabs - All Reward Types have an additional reward
	'Soul Eater': {'Soul Conduit', 'Gargantuan', 'Necromancer'},  # Maps, Maps
	'Storm Strider': {'Hasted', 'Stormweaver'},  # Trinkets, Trinkets, Trinkets
	'Tukohama-touched': {'Executioner', 'Magma Barrier', 'Bonebreaker'},  # Weapon, Weapon, Fragments - Rewards are rolled 4 additional times, choosing the rarest result
	# Terminal Recipes
	'Arakaali-touched': {'Entangler', 'Corpse Detonator', 'Assassin'},  # Divination Cards - All Reward Types are Divination Cards
	'Brine King-touched': {'Storm Strider', 'Ice Prison', 'Heralding Minions'},  # Armour, Armour, Armour - Rewards are rolled 6 additional times, choosing the rarest result
	'Crystal-skinned': {'Permafrost', 'Rejuvenating', 'Berserker'},  # Harbinger, Harbinger
	'Effigy': {'Malediction', 'Hexer', 'Corrupter'},  # Divination Cards, Divination Cards - Rewards are rolled 1 additional time, choosing the rarest result
	'Empowered Elements': {'Chaosweaver', 'Evocationist', 'Steel-infused'},  # Uniques, Uniques - Rewards are rolled 1 additional time, choosing the rarest result
	'Innocence-touched': {'Solaris-touched', 'Lunaris-touched', 'Mana Siphoner', 'Mirror Image'},  # Currency, Currency, Currency - All Reward Types are Currency
	'Kitava-touched': {'Abberath-touched', 'Tukohama-touched', 'Corrupter', 'Corpse Detonator'},  # Generic - Rewards are doubled
	'Shakari-touched': {'Drought Bringer', 'Entangler', 'Soul Eater'},  # Uniques - All Reward Types are Uniques
	'Temporal Bubble': {'Juggernaut', 'Hexer', 'Arcane Buffer'},  # Heist, Expedition
	'Treant Horde': {'Sentinel', 'Toxic', 'Steel-infused'},  # Generic - Monster's Minions drop a randomly-chosen Reward Type
	'Trickster': {'Overcharged', 'Echoist', 'Assassin'},  # Currency, Uniques, Divination Cards
}

good_highlight = {"Opulent"}  # {"Echoist", "Gargantuan", "Opulent", "Assassin", "Rejuvenating", "Treant Horde", "Mirror Image", "Effigy", "Solaris-touched", "Arakaali-touched", "Innocence-touched", "Kitava-touched"}

need_highlight = {"Arakaali-touched", "Innocence-touched", "Lunaris-touched", "Effigy", "Solaris-touched"}

have_list = [
	"", "", "", "", "", "", "", "",
	"", "Magma Barrier", "", "", "", "", "", "",
	"Invulnerable", "Malediction", "Gargantuan", "Toxic", "Berserker", "Frost Strider", "Sentinel", "Necromancer",
	"Mirror Image", "", "Overcharged", "Hexer", 'Mana Siphoner', 'Assassin', "Frostweaver", "Sentinel"
]

# Initialise our item counts
need = defaultdict(int)
need_t = defaultdict(int)
for i in need_highlight:
	need_t[i] += 1
have = defaultdict(int)
for i in have_list:
	if i:
		have[i] += 1
# calculate how many we need of each part
while need_t:
	for i in need_t:
		need[i] += need_t[i]
	t_set = defaultdict(int)
	for i in need_t:
		if archnem_parts[i] and all(j in have and have[j] for j in archnem_parts[i]):
			print(f"Craft {i} with: {archnem_parts[i]}")
		for j in archnem_parts[i]:
			if j in have and have[j]:
				have[j] -= 1
				continue
			t_set[j] += 1
	need_t = t_set
# calculate what parts are good, always seen
want = set()
good = good_highlight
while good:
	want.update(good)
	t_set = set()
	for i in good:
		t_set.update(archnem_parts[i])
	good = t_set

# create filter rules
for base in set(need.keys()) | want:
	if need[base] or base in want:
		if not archnem_parts[base] and base in need and need[base]:
			print(f"Need: {base} ({need[base]})")
		items[f"1 Archnemesis {base}"] = {'archnem': base, "class": "Archnemesis Mod", "type": "challenge normal"}
		if base in good_highlight | need_highlight:
			items[f"1 Archnemesis {base}"]['other'] = ['PlayEffect White']
		else:
			items[f"1 Archnemesis {base}"]['other'] = ['PlayEffect Green']

