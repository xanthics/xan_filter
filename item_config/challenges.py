#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher

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

good = set()  # {"Echoist", "Gargantuan", "Opulent", "Assassin", "Rejuvenating", "Treant Horde", "Mirror Image", "Effigy", "Solaris-touched", "Arakaali-touched", "Innocence-touched", "Kitava-touched"}

highlight = {"Opulent", "Kitava-touched",  # , "Treant Horde"
             "Arakaali-touched", "Innocence-touched", "Lunaris-touched", "Effigy", "Empowering Minions", "Shakari-touched", "Solaris-touched"}

have = {"Toxic", "", "Sentinel", "", "", "", "", "",
        "Juggernaut", "Flame Strider", "Malediction", "Bonebreaker", "Frostweaver", "Sentinel", "Gargantuan", "",
        "Soul Eater", "Corpse Detonator", "Magma Barrier", "Hexer", '', 'Vampiric' "Overcharged", "Frenzied"}

base_set = set()
set_len = (good | highlight) - have

while set_len:
	base_set.update(set_len)
	t_set = set()
	for base in set_len:
		if archnem_parts[base] and have.issuperset(archnem_parts[base]) and base not in have:
			print(f"Craft {base} with {archnem_parts[base]}")
		if base not in have:
			t_set.update(archnem_parts[base])
	set_len = t_set

base_set -= have
for base in base_set:
	items[f"1 Archnemesis {base}"] = {'archnem': base, "class": "Archnemesis Mod", "type": "challenge normal"}

base_set = set()
set_len = highlight - have
while set_len:
	base_set.update(set_len)
	t_set = set()
	for base in set_len:
		if base not in have:
			t_set.update(archnem_parts[base])
	set_len = t_set

base_set -= have
base_set -= highlight

for base in base_set:
	items[f"1 Archnemesis {base}"]['other'] = ['PlayEffect Pink']

for base in highlight:
	items[f"1 Archnemesis {base}"]['other'] = ['PlayEffect White']
