#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 10/02/2019(m/d/y) 02:19:38 UTC from "tmpstandard" data

desc = "Helm Enchant Autogen"

# Base type : settings pair
items = {
	"1 15% increased Cyclone Attack Speed": {"enchant": "Enchantment Cyclone Attack Speed 2", "type": "base very high"},
	"1 15% of Infernal Blow Physical Damage gained as Extra Fire Damage": {"enchant": "Enchantment Infernal Blow Physical Damage Percent To Add As Fire Damage 2", "type": "base very high"},
	"1 25% increased Ice Nova Damage": {"enchant": "Enchantment Ice Nova Damage 1", "type": "base very high"},
	"1 30% increased Blade Vortex Duration": {"enchant": "Enchantment Blade Vortex Duration 2", "type": "base very high"},
	"1 30% increased Freezing Pulse Projectile Speed": {"enchant": "Enchantment Freezing Pulse Projectile Speed 2", "type": "base very high"},
	"1 30% increased Temporal Chains Curse Effect": {"enchant": "Enchantment Temporal Chains Curse Effect 2", "type": "base extremely high"},
	"1 30% reduced Earthquake Duration": {"enchant": "Enchantment Earthquake Duration 2", "type": "base very high"},
	"1 30% reduced Storm Call Duration": {"enchant": "Enchantment Storm Call Duration 2", "type": "base very high"},
	"1 40% increased Cyclone Damage": {"enchant": "Enchantment Cyclone Damage 2", "type": "base very high"},
	"1 40% increased Freezing Pulse Damage": {"enchant": "Enchantment Freezing Pulse Damage 2", "type": "base very high"},
	"1 40% increased Frost Blades Damage": {"enchant": "Enchantment Frost Blades Damage 2", "type": "base very high"},
	"1 40% increased Ice Nova Damage": {"enchant": "Enchantment Ice Nova Damage 2", "type": "base extremely high"},
	"1 40% increased Ice Shot Damage": {"enchant": "Enchantment Ice Shot Damage 2", "type": "base very high"},
	"1 40% increased Volatile Dead Damage": {"enchant": "Enchantment Volatile Dead Damage 2", "type": "base very high"},
	"1 45% increased Static Strike Duration": {"enchant": "Enchantment Static Strike Duration 2", "type": "base extremely high"},
	"1 9% increased Flicker Strike Damage per Frenzy Charge": {"enchant": "Enchantment Flicker Strike Damage Per Frenzy Charge 2", "type": "base very high"},
	"1 Arc Chains an additional time": {"enchant": "Enchantment Arc Num Of Additional Projectiles In Chain 1", "type": "base very high"},
	"1 Ball Lightning fires an additional Projectile": {"enchant": "Enchantment Ball Lightning Additional Projectiles 1", "type": "base very high"},
	"1 Barrage fires an additional Projectile": {"enchant": "Enchantment Barrage Num Of Additional Projectiles 1", "type": "base very high"},
	"1 Blood Rage grants additional 12% increased Attack Speed": {"enchant": "Enchantment Blood Rage Attack Speed 2", "type": "base very high"},
	"1 Divine Ire deals 40% increased Damage": {"enchant": "Enchantment Divine Ire Damage 2", "type": "base very high"},
	"1 Herald of Agony has 30% reduced Mana Reservation": {"enchant": "Enchantment Herald Of Agony Mana Reservation 2", "type": "base very high"},
	"1 Ice Spear fires an additional Projectile": {"enchant": "Enchantment Ice Spear Additional Projectile 1", "type": "base very high"},
	"1 Incinerate has +2 to maximum stages": {"enchant": "Enchantment Incinerate Maximum Stages 2", "type": "base very high"},
	"1 Lightning Trap Damage Penetrates 10% Lightning Resistance": {"enchant": "Enchantment Lightning Trap Penetration 2", "type": "base very high"},
	"1 Magma Orb Chains an additional 2 times": {"enchant": "Enchantment Magma Orb Num Of Additional Projectiles In Chain 2", "type": "base very high"},
	"1 Molten Strike fires 2 additional Projectiles": {"enchant": "Enchantment Molten Strike Num Of Additional Projectiles 2", "type": "base very high"},
	"1 Orb of Storms has 30% increased Cast Speed": {"enchant": "Enchantment Orb Of Storms Cast Speed 2", "type": "base very high"},
	"1 Scourge Arrow creates an additional spore pod at Maximum Stages": {"enchant": "Enchantment Scourge Arrow Additional Spore 1", "type": "base extremely high"},
	"1 Storm Brand Damage Penetrates 12% of Branded Enemy's Lightning Resistance": {"enchant": "Storm Brand Attached Target Lightning Penetration 2", "type": "base very high"},
	"1 Storm Burst has a 15% chance to create an additional Orb": {"enchant": "Enchantment Storm Burst Additional Object Chance 2", "type": "base very high"},
	"1 Summoned Agony Crawler fires 2 additional Projectiles": {"enchant": "Enchantment Herald Of Agony Num Of Secondary Projectiles 1", "type": "base very high"},
	"1 Tornado Shot fires 2 additional secondary Projectiles": {"enchant": "Enchantment Tornado Shot Num Of Secondary Projectiles 2", "type": "base extremely high"},
	"1 Tornado Shot fires an additional secondary Projectile": {"enchant": "Enchantment Tornado Shot Num Of Secondary Projectiles 1", "type": "base extremely high"},
	"1 Toxic Rain fires 1 additional Arrow": {"enchant": "Enchantment Toxic Rain Num Of Additional Projectiles 1", "type": "base very high"},
	"1 0 Volatile Dead destroys up to 1 additional Corpse": {"enchant": "Enchantment Volatile Dead Orbs 1", "type": "base very high"},
	"1 1 Volatile Dead destroys up to 1 additional Corpse": {"enchant": "Enchantment Volatile Dead Orbs 2", "type": "base very high"},
	"1 2 Volatile Dead destroys up to 1 additional Corpse": {"enchant": "Enchantment Volatile Dead Orbs 3", "type": "base very high"},
	"1 Wild Strike Chains an additional 6 times": {"enchant": "Enchantment Wild Strike Num Of Additional Projectiles In Chain 2", "type": "base extremely high"},
	"1 Winter Orb has +2 Maximum Stages": {"enchant": "Enchantment Frost Fury Additional Max Number Of Stages 1", "type": "base very high"},
	"7 enchant default": {"class": "Helmet", "other": ["AnyEnchantment True"], "type": "item mod"}
}
