#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 03/13/2020(m/d/y) 20:39:54 UTC from "tmpstandard" data

desc = "Helm Enchant Autogen"

# Base type : settings pair
items = {
	"1 15% increased Cyclone Attack Speed": {"enchant": "Enchantment Cyclone Attack Speed 2", "type": "base very high"},
	"1 24% increased Ball Lightning Area of Effect": {"enchant": "Enchantment Ball Lightning Area Of Effect 2", "type": "base very high"},
	"1 30% increased Freezing Pulse Projectile Speed": {"enchant": "Enchantment Freezing Pulse Projectile Speed 2", "type": "base very high"},
	"1 30% increased Temporal Chains Curse Effect": {"enchant": "Enchantment Temporal Chains Curse Effect 2", "type": "base very high"},
	"1 30% reduced Lightning Warp Duration": {"enchant": "Enchantment Lightning Warp Duration 2", "type": "base very high"},
	"1 40% increased Arc Damage": {"enchant": "Enchantment Arc Damage 2", "type": "base very high"},
	"1 40% increased Ball Lightning Damage": {"enchant": "Enchantment Ball Lightning Damage 2", "type": "base very high"},
	"1 40% increased Caustic Arrow Damage": {"enchant": "Enchantment Caustic Arrow Damage 2", "type": "base very high"},
	"1 40% increased Cyclone Damage": {"enchant": "Enchantment Cyclone Damage 2", "type": "base very high"},
	"1 40% increased Essence Drain Damage": {"enchant": "Enchantment Essence Drain Damage 2", "type": "base very high"},
	"1 40% increased Freezing Pulse Damage": {"enchant": "Enchantment Freezing Pulse Damage 2", "type": "base very high"},
	"1 40% increased Frostbolt Damage": {"enchant": "Enchantment Frost Bolt Damage 2", "type": "base very high"},
	"1 40% increased Ice Nova Damage": {"enchant": "Enchantment Ice Nova Damage 2", "type": "base extremely high"},
	"1 40% increased Ice Shot Damage": {"enchant": "Enchantment Ice Shot Damage 2", "type": "base very high"},
	"1 40% increased Lacerate Damage": {"enchant": "Enchantment Lacerate Damage 2", "type": "base very high"},
	"1 40% increased Puncture Damage": {"enchant": "Enchantment Puncture Damage 2", "type": "base very high"},
	"1 Arc Chains an additional time": {"enchant": "Enchantment Arc Num Of Additional Projectiles In Chain 1", "type": "base extremely high"},
	"1 Ball Lightning fires an additional Projectile": {"enchant": "Enchantment Ball Lightning Additional Projectiles 1", "type": "base extremely high"},
	"1 Barrage fires an additional Projectile": {"enchant": "Enchantment Barrage Num Of Additional Projectiles 1", "type": "base very high"},
	"1 Burning Arrow has 24% increased Debuff Effect": {"enchant": "Enchantment Burning Arrow Debuff Effect 2", "type": "base very high"},
	"1 Cobra Lash Chains 3 additional times": {"enchant": "Enchantment Cobra Lash Number Of Additional Chains 2", "type": "base very high"},
	"1 Consecrated Ground from Purifying Flame applies 9% increased Damage taken to Enemies": {"enchant": "Enchantment Purifying Flame Consecrated Ground Enemy Damage Taken 2", "type": "base very high"},
	"1 Detonate Dead has a 45% chance to detonate an additional corpse": {"enchant": "Enchantment Detonate Dead Percent Chance To Detonate Additional Corpse 2", "type": "base very high"},
	"1 Explosive Arrow has 15% increased Attack Speed": {"enchant": "Enchantment Explosive Arrow Attack Speed 2", "type": "base very high"},
	"1 Explosive Arrow has 40% increased Duration": {"enchant": "Enchantment Explosive Arrow Increased Duration 2", "type": "base very high"},
	"1 Herald of Agony has 30% reduced Mana Reservation": {"enchant": "Enchantment Herald Of Agony Mana Reservation 2", "type": "base very high"},
	"1 Icicle Mine has +30% to Critical Strike Multiplier": {"enchant": "Enchantment Icicle Mine Critical Multiplier 2", "type": "base very high"},
	"1 Molten Strike fires 2 additional Projectiles": {"enchant": "Enchantment Molten Strike Num Of Additional Projectiles 2", "type": "base very high"},
	"1 Power Siphon fires 2 additional Projectiles": {"enchant": "Enchantment Power Siphon Additional Projectiles 2", "type": "base very high"},
	"1 Pyroclast Mine fires 2 additional Projectiles": {"enchant": "Enchantment Pyroclast Mine Additional Projectiles 2", "type": "base extremely high"},
	"1 Scourge Arrow creates an additional spore pod at Maximum Stages": {"enchant": "Enchantment Scourge Arrow Additional Spore 1", "type": "base extremely high"},
	"1 Split Arrow fires 3 additional Projectiles": {"enchant": "Enchantment Split Arrow Num Of Additional Projectiles 2", "type": "base very high"},
	"1 Storm Brand Damage Penetrates 12% of Branded Enemy's Lightning Resistance": {"enchant": "Storm Brand Attached Target Lightning Penetration 2", "type": "base very high"},
	"1 Storm Brand deals 40% increased Damage": {"enchant": "Enchantment Storm Brand Damage 2", "type": "base very high"},
	"1 Storm Burst has a 15% chance to create an additional Orb": {"enchant": "Enchantment Storm Burst Additional Object Chance 2", "type": "base very high"},
	"1 0 Tornado Shot fires an additional secondary Projectile": {"enchant": "Enchantment Tornado Shot Num Of Secondary Projectiles 1", "type": "base very high"},
	"1 1 Tornado Shot fires an additional secondary Projectile": {"enchant": "Enchantment Tornado Shot Num Of Secondary Projectiles 2", "type": "base very high"},
	"1 Toxic Rain deals 40% increased Damage": {"enchant": "Enchantment Toxic Rain Damage 2", "type": "base very high"},
	"1 Toxic Rain fires 1 additional Arrow": {"enchant": "Enchantment Toxic Rain Num Of Additional Projectiles 1", "type": "base extremely high"},
	"1 0 Volatile Dead Consumes up to 1 additional corpse": {"enchant": "Enchantment Volatile Dead Orbs 1", "type": "base very high"},
	"1 1 Volatile Dead Consumes up to 1 additional corpse": {"enchant": "Enchantment Volatile Dead Orbs 2", "type": "base very high"},
	"1 2 Volatile Dead Consumes up to 1 additional corpse": {"enchant": "Enchantment Volatile Dead Orbs 3", "type": "base very high"},
	"1 Wild Strike's Beam Chains an additional 6 times": {"enchant": "Enchantment Wild Strike Num Of Additional Projectiles In Chain 2", "type": "base very high"},
	"1 Winter Orb has +2 Maximum Stages": {"enchant": "Enchantment Frost Fury Additional Max Number Of Stages 1", "type": "base very high"},
	"7 enchant default": {"class": "Helmet", "other": ["AnyEnchantment True"], "type": "item mod"}
}
