#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 01/20/2020(m/d/y) 17:08:44 UTC from "tmpstandard" data

desc = "Helm Enchant Autogen"

# Base type : settings pair
items = {
	"1 +1 to maximum number of Sentinels of Purity": {"enchant": "Enchantment Herald Of Purity Additional Minion 1", "type": "base very high"},
	"1 15% increased Cyclone Attack Speed": {"enchant": "Enchantment Cyclone Attack Speed 2", "type": "base extremely high"},
	"1 15% of Glacial Hammer Physical Damage gained as Extra Cold Damage": {"enchant": "Enchantment Glacial Hammer Physical Damage Percent To Add As Cold Damage 2", "type": "base very high"},
	"1 20% increased Temporal Chains Curse Effect": {"enchant": "Enchantment Temporal Chains Curse Effect 1", "type": "base very high"},
	"1 24% chance to create an additional Animate Weapon copy": {"enchant": "Enchantment Animate Weapon Chance To Create Additional Copy 2", "type": "base very high"},
	"1 25% increased Ice Nova Damage": {"enchant": "Enchantment Ice Nova Damage 1", "type": "base very high"},
	"1 30% chance for Discharge to deal Damage without removing Charges": {"enchant": "Enchantment Discharge Consume Charges 2", "type": "base very high"},
	"1 30% increased Blade Vortex Duration": {"enchant": "Enchantment Blade Vortex Duration 2", "type": "base very high"},
	"1 30% increased Freezing Pulse Projectile Speed": {"enchant": "Enchantment Freezing Pulse Projectile Speed 2", "type": "base very high"},
	"1 30% increased Temporal Chains Curse Effect": {"enchant": "Enchantment Temporal Chains Curse Effect 2", "type": "base extremely high"},
	"1 40% increased Ball Lightning Damage": {"enchant": "Enchantment Ball Lightning Damage 2", "type": "base very high"},
	"1 40% increased Cyclone Damage": {"enchant": "Enchantment Cyclone Damage 2", "type": "base very high"},
	"1 40% increased Essence Drain Damage": {"enchant": "Enchantment Essence Drain Damage 2", "type": "base very high"},
	"1 40% increased Flicker Strike Damage": {"enchant": "Enchantment Flicker Strike Damage 2", "type": "base very high"},
	"1 40% increased Frost Blades Damage": {"enchant": "Enchantment Frost Blades Damage 2", "type": "base very high"},
	"1 40% increased Ice Nova Damage": {"enchant": "Enchantment Ice Nova Damage 2", "type": "base extremely high"},
	"1 40% increased Ice Shot Damage": {"enchant": "Enchantment Ice Shot Damage 2", "type": "base very high"},
	"1 40% increased Lacerate Damage": {"enchant": "Enchantment Lacerate Damage 2", "type": "base very high"},
	"1 9% increased Flicker Strike Damage per Frenzy Charge": {"enchant": "Enchantment Flicker Strike Damage Per Frenzy Charge 2", "type": "base very high"},
	"1 Arc Chains an additional time": {"enchant": "Enchantment Arc Num Of Additional Projectiles In Chain 1", "type": "base very high"},
	"1 Ball Lightning fires an additional Projectile": {"enchant": "Enchantment Ball Lightning Additional Projectiles 1", "type": "base very high"},
	"1 Barrage fires an additional Projectile": {"enchant": "Enchantment Barrage Num Of Additional Projectiles 1", "type": "base very high"},
	"1 Cobra Lash Chains 3 additional times": {"enchant": "Enchantment Cobra Lash Number Of Additional Chains 2", "type": "base very high"},
	"1 Detonate Dead has a 45% chance to detonate an additional corpse": {"enchant": "Enchantment Detonate Dead Percent Chance To Detonate Additional Corpse 2", "type": "base very high"},
	"1 Double Strike has a 15% chance to deal Double Damage to Bleeding Enemies": {"enchant": "Enchantment Double Strike Double Damage Vs Bleeding 2", "type": "base very high"},
	"1 Explosive Arrow has 15% increased Attack Speed": {"enchant": "Enchantment Explosive Arrow Attack Speed 2", "type": "base very high"},
	"1 Explosive Arrow has 40% increased Duration": {"enchant": "Enchantment Explosive Arrow Increased Duration 2", "type": "base very high"},
	"1 Lacerate deals 14 to 25 added Physical Damage against Bleeding Enemies": {"enchant": "Enchantment Double Slash Added Phys To Bleeding 2", "type": "base very high"},
	"1 Molten Strike fires 2 additional Projectiles": {"enchant": "Enchantment Molten Strike Num Of Additional Projectiles 2", "type": "base extremely high"},
	"1 Power Siphon fires 2 additional Projectiles": {"enchant": "Enchantment Power Siphon Additional Projectiles 2", "type": "base very high"},
	"1 Pyroclast Mine fires 2 additional Projectiles": {"enchant": "Enchantment Pyroclast Mine Additional Projectiles 2", "type": "base very high"},
	"1 Scourge Arrow creates an additional spore pod at Maximum Stages": {"enchant": "Enchantment Scourge Arrow Additional Spore 1", "type": "base very high"},
	"1 Shattering Steel fires an additional Projectile": {"enchant": "Enchantment Shattering Steel Additional Projectile 1", "type": "base very high"},
	"1 Split Arrow fires 3 additional Projectiles": {"enchant": "Enchantment Split Arrow Num Of Additional Projectiles 2", "type": "base very high"},
	"1 Storm Brand Damage Penetrates 12% of Branded Enemy's Lightning Resistance": {"enchant": "Storm Brand Attached Target Lightning Penetration 2", "type": "base very high"},
	"1 Storm Burst has a 15% chance to create an additional Orb": {"enchant": "Enchantment Storm Burst Additional Object Chance 2", "type": "base very high"},
	"1 0 Tornado Shot fires an additional secondary Projectile": {"enchant": "Enchantment Tornado Shot Num Of Secondary Projectiles 1", "type": "base very high"},
	"1 1 Tornado Shot fires an additional secondary Projectile": {"enchant": "Enchantment Tornado Shot Num Of Secondary Projectiles 2", "type": "base very high"},
	"1 Toxic Rain fires 1 additional Arrow": {"enchant": "Enchantment Toxic Rain Num Of Additional Projectiles 1", "type": "base very high"},
	"1 0 Volatile Dead Consumes up to 1 additional corpse": {"enchant": "Enchantment Volatile Dead Orbs 1", "type": "base very high"},
	"1 1 Volatile Dead Consumes up to 1 additional corpse": {"enchant": "Enchantment Volatile Dead Orbs 2", "type": "base very high"},
	"1 2 Volatile Dead Consumes up to 1 additional corpse": {"enchant": "Enchantment Volatile Dead Orbs 3", "type": "base very high"},
	"1 Wild Strike's Beam Chains an additional 6 times": {"enchant": "Enchantment Wild Strike Num Of Additional Projectiles In Chain 2", "type": "base very high"},
	"7 enchant default": {"class": "Helmet", "other": ["AnyEnchantment True"], "type": "item mod"}
}
