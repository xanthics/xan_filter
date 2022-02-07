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
	"Toxic": {},  # Generic Gems
	"Chaosweaver": {},  # Gems
	"Frostweaver": {},  # Armour
	"Permafrost": {},  # Generic, Armour
	"Hasted": {},  # Generic
	"Deadeye": {},  # Armour, Trinkets
	"Bombardier": {},  # Weapon, Armour
	"Flameweaver": {},  # Weapon
	"Incendiary": {},  # Generic, Weapon
	"Arcane Buffer": {},  # Essences
	"Echoist": {},  # Generic, Currency
	"Stormweaver": {},  # Trinkets
	"Dynamo": {},  # Generic, Trinkets
	"Bonebreaker": {},  # Generic, Weapon
	"Bloodletter": {},  # Weapon, Trinkets - Items dropped from the Monster and its Minions are Corrupted
	"Steel-infused": {},  # Weapon
	"Gargantuan": {},  # Currency
	"Berserker": {},  # Uniques
	"Sentinel": {},  # Armour Armour
	"Juggernaut": {},  # Harbinger
	"Vampiric": {},  # Fossils
	"Overcharged": {},  # Trinkets, Trinkets
	"Soul Conduit": {},  # Maps
	"Opulent": {},  # Monster is fabulously wealthy
	"Malediction": {},  # Divination Cards
	"Consecrator": {},  # Fragments
	"Frenzied": {},  # Generic, Uniques
	"Heralding Minions": {"Dynamo", "Arcane Buffer"},  # Fragments, Fragments
	"Empowering Minions": {"Necromancer", "Executioner", "Gargantuan"},  # Blight, Ritual
	"Assassin": {"Deadeye", "Vampiric"},  # Currency, Currency
	"Trickster": {"Overcharged", "Assassin", "Echoist"},  # Currency, Uniques, Divination Cards
	"Necromancer": {"Bombardier", "Overcharged"},  # Generic - Rewards are rolled 2 additional times, choosing the rarest result
	"Rejuvenating": {"Gargantuan", "Vampiric"},  # Currency - Rewards are rolled 1 additional time, choosing the rarest result
	"Executioner": {"Frenzied", "Berserker"},  # Legion Breach
	"Hexer": {"Chaosweaver", "Echoist"},  # Essences, Essences
	"Drought Bringer": {"Malediction", "Deadeye"},  # Labyrinth Labyrinth
	"Entangler": {"Toxic", "Bloodletter"},  # Fossils, Fossils
	"Temporal Bubble": {"Juggernaut", "Hexer", "Arcane Buffer"},  # Heist, Expedition
	"Treant Horde": {"Toxic", "Sentinel", "Steel-infused"},  # Generic - Monster's Minions drop a randomly-chosen Reward Type
	"Frost Strider": {"Frostweaver", "Hasted"},  # Armour, Armour, Armour
	"Ice Prison": {"Permafrost", "Sentinel"},  # Armour Armour - Rewards are rolled 1 additional time, choosing the rarest result
	"Soul Eater": {"Soul Conduit", "Necromancer", "Gargantuan"},  # Maps, Maps
	"Flame Strider": {"Flameweaver", "Hasted"},  # Weapon, Weapon, Weapon
	"Corpse Detonator": {"Necromancer", "Incendiary"},  # Divination Cards, Divination Cards
	"Evocationist": {"lameweaver", "Frostweaver", "Stormweaver"},  # Generic, Weapon, Armour, Trinkets
	"Magma Barrier": {"Incendiary", "Bonebreaker"},  # Weapon, Weapon - Rewards are rolled 1 additional time, choosing the rarest result
	"Mirror Image": {"Echoist", "Soul Conduit"},  # Scarabs - Rewards are rolled 2 additional times, choosing the rarest result
	"Storm Strider": {"Stormweaver", "Hasted"},  # Trinkets, Trinkets, Trinkets
	"Mana Siphoner": {"Consecrator", "Dynamo"},  # Trinkets, Trinkets - Rewards are rolled 1 additional time, choosing the rarest result
	"Corrupter": {"Bloodletter", "Chaosweaver"},  # Abyss, Abyss - Items dropped from the Monster and its Minions are Corrupted
	"Invulnerable": {"Sentinel", "Juggernaut", "Consecrator"},  # Delirium, Metamorphosis
	"Crystal-skinned": {"Permafrost", "Rejuvenating", "Berserker"},  # Harbinger, Harbinger
	"Empowered Elements": {"Evocationist", "Steel-infused", "Chaosweaver"},  # Uniques, Uniques - Rewards are rolled 1 additional time, choosing the rarest result
	"Effigy": {"Hexer", "Malediction", "Corrupter"},  # Divination Cards, Divination Cards - Rewards are rolled 1 additional time, choosing the rarest result
	"Lunaris-touched": {"Invulnerable", "Frost Strider", "Empowering Minions"},  # Uniques - All Reward Types have an additional reward
	"Solaris-touched": {"Invulnerable", "Magma Barrier", "Empowering Minions"},  # Scarabs - All Reward Types have an additional reward
	"Arakaali-touched": {"Corpse Detonator", "Entangler", "Assassin"},  # Divination Cards - All Reward Types are Divination Cards
	"Brine King-touched": {"Ice Prison", "Storm Strider", "Heralding Minions"},  # Armour, Armour, Armour - Rewards are rolled 6 additional times, choosing the rarest result
	"Tukohama-touched": {"Bonebreaker", "Executioner", "Magma Barrier"},  # Weapon, Weapon, Fragments - Rewards are rolled 4 additional times, choosing the rarest result
	"Abberath-touched": {"Flame Strider", "Frenzied", "Rejuvenating"},  # Trinkets, Trinkets, Maps - Rewards are rolled 4 additional times, choosing the rarest result
	"Shakari-touched": {"Entangler", "Soul Eater", "Drought Bringer"},  # Uniques - All Reward Types are Uniques
	"Innocence-touched": {"Lunaris-touched", "Solaris-touched", "Mirror Image", "Mana Siphoner"},  # Currency, Currency, Currency - All Reward Types are Currency
	"Kitava-touched": {"Tukohama-touched", "Abberath-touched", "Corrupter", "Corpse Detonator"},  # Generic - Rewards are doubled
}

good = {"Echoist", "Gargantuan", "Opulent", "Assassin", "Rejuvenating", "Treant Horde", "Mirror Image", "Effigy", "Solaris-touched", "Arakaali-touched", "Innocence-touched", "Kitava-touched"}
highlight = {"Opulent", "Treant Horde", "Kitava-touched"}

base_set = set()
set_len = good | highlight
while set_len:
	base_set.update(set_len)
	t_set = set()
	for base in set_len:
		t_set.update(archnem_parts[base])
	set_len = t_set

for base in base_set:
	items[f"1 Archnemesis {base} 68+"] = {'archnem': base, "class": "Archnemesis Mod", "other": ["ItemLevel >= 68"], "type": "challenge normal"}

base_set = set()
set_len = highlight
while set_len:
	base_set.update(set_len)
	t_set = set()
	for base in set_len:
		t_set.update(archnem_parts[base])
	set_len = t_set

for base in base_set:
	items[f"1 Archnemesis {base} 68+"]['other'].append('PlayEffect Green')
