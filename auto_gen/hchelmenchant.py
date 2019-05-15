#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 05/15/2019(m/d/y) 09:07:59 UTC from "Hardcore" data

desc = "Helm Enchant Autogen"

# Base type : settings pair
items = {
	"000 40% increased Flame Surge Damage against Burning Enemies": {"enchant": "40% increased Flame Surge Damage against Burning Enemies", "type": "ignore"},
	"1 10% increased Incinerate Damage for each stage": {"enchant": "10% increased Incinerate Damage for each stage", "type": "currency very high"},
	"1 12% increased Contagion Area of Effect": {"enchant": "12% increased Contagion Area of Effect", "type": "currency very high"},
	"1 12% increased Reave Radius": {"enchant": "12% increased Reave Radius", "type": "currency very high"},
	"1 12% increased Scorching Ray Cast Speed": {"enchant": "12% increased Scorching Ray Cast Speed", "type": "currency very high"},
	"1 12% increased Tectonic Slam Area of Effect": {"enchant": "12% increased Tectonic Slam Area of Effect", "type": "currency very high"},
	"1 15% increased Double Strike Attack Speed": {"enchant": "15% increased Double Strike Attack Speed", "type": "currency very high"},
	"1 15% increased Elemental Hit Attack Speed": {"enchant": "15% increased Elemental Hit Attack Speed", "type": "currency very high"},
	"1 150% increased Effect of the Buff granted by your Stone Golems": {"enchant": "150% increased Effect of the Buff granted by your Stone Golems", "type": "currency very high"},
	"1 20% reduced Storm Call Duration": {"enchant": "20% reduced Storm Call Duration", "type": "currency very high"},
	"1 30% chance for Discharge to deal Damage without removing Charges": {"enchant": "30% chance for Discharge to deal Damage without removing Charges", "type": "currency very high"},
	"1 30% increased Blade Vortex Duration": {"enchant": "30% increased Blade Vortex Duration", "type": "currency very high"},
	"1 30% increased Despair Curse Effect": {"enchant": "30% increased Despair Curse Effect", "type": "currency very high"},
	"1 30% increased Ethereal Knives Projectile Speed": {"enchant": "30% increased Ethereal Knives Projectile Speed", "type": "currency very high"},
	"1 30% increased Freezing Pulse Projectile Speed": {"enchant": "30% increased Freezing Pulse Projectile Speed", "type": "currency very high"},
	"1 30% increased Spark Projectile Speed": {"enchant": "30% increased Spark Projectile Speed", "type": "currency very high"},
	"1 30% increased Temporal Chains Curse Effect": {"enchant": "30% increased Temporal Chains Curse Effect", "type": "currency very high"},
	"1 30% increased Vortex Duration": {"enchant": "30% increased Vortex Duration", "type": "currency very high"},
	"1 30% reduced Earthquake Duration": {"enchant": "30% reduced Earthquake Duration", "type": "currency very high"},
	"1 30% reduced Lightning Warp Duration": {"enchant": "30% reduced Lightning Warp Duration", "type": "currency very high"},
	"1 30% reduced Spectral Throw Projectile Deceleration": {"enchant": "30% reduced Spectral Throw Projectile Deceleration", "type": "currency very high"},
	"1 30% reduced Storm Call Duration": {"enchant": "30% reduced Storm Call Duration", "type": "currency extremely high"},
	"1 40% increased Arctic Breath Damage": {"enchant": "40% increased Arctic Breath Damage", "type": "currency very high"},
	"1 40% increased Blade Flurry Damage": {"enchant": "40% increased Blade Flurry Damage", "type": "currency very high"},
	"1 40% increased Caustic Arrow Damage": {"enchant": "40% increased Caustic Arrow Damage", "type": "currency very high"},
	"1 40% increased Cyclone Damage": {"enchant": "40% increased Cyclone Damage", "type": "currency very high"},
	"1 40% increased Essence Drain Damage": {"enchant": "40% increased Essence Drain Damage", "type": "currency very high"},
	"1 40% increased Fireball Damage": {"enchant": "40% increased Fireball Damage", "type": "currency very high"},
	"1 40% increased Flicker Strike Damage": {"enchant": "40% increased Flicker Strike Damage", "type": "currency very high"},
	"1 40% increased Freezing Pulse Damage": {"enchant": "40% increased Freezing Pulse Damage", "type": "currency very high"},
	"1 40% increased Frost Blades Damage": {"enchant": "40% increased Frost Blades Damage", "type": "currency very high"},
	"1 40% increased Glacial Cascade Damage": {"enchant": "40% increased Glacial Cascade Damage", "type": "currency very high"},
	"1 40% increased Ice Nova Damage": {"enchant": "40% increased Ice Nova Damage", "type": "currency very high"},
	"1 40% increased Ice Shot Damage": {"enchant": "40% increased Ice Shot Damage", "type": "currency very high"},
	"1 40% increased Lacerate Damage": {"enchant": "40% increased Lacerate Damage", "type": "currency very high"},
	"1 40% increased Orb of Storms Damage": {"enchant": "40% increased Orb of Storms Damage", "type": "currency very high"},
	"1 40% increased Righteous Fire Damage": {"enchant": "40% increased Righteous Fire Damage", "type": "currency very high"},
	"1 40% increased Spark Damage": {"enchant": "40% increased Spark Damage", "type": "currency very high"},
	"1 40% increased Tectonic Slam Damage": {"enchant": "40% increased Tectonic Slam Damage", "type": "currency very high"},
	"1 40% of Glacial Cascade Physical Damage Converted to Cold Damage": {"enchant": "40% of Glacial Cascade Physical Damage Converted to Cold Damage", "type": "currency very high"},
	"1 8% increased Glacial Cascade Area of Effect": {"enchant": "8% increased Glacial Cascade Area of Effect", "type": "currency very high"},
	"1 9% increased Flicker Strike Damage per Frenzy Charge": {"enchant": "9% increased Flicker Strike Damage per Frenzy Charge", "type": "currency very high"},
	"1 Arc Chains an additional time": {"enchant": "Arc Chains an additional time", "type": "currency very high"},
	"1 Bane deals 40% increased Damage": {"enchant": "Bane deals 40% increased Damage", "type": "currency very high"},
	"1 Barrage fires an additional Projectile": {"enchant": "Barrage fires an additional Projectile", "type": "currency very high"},
	"1 Blood Rage grants additional 12% increased Attack Speed": {"enchant": "Blood Rage grants additional 12% increased Attack Speed", "type": "currency very high"},
	"1 Consecrated Ground from Purifying Flame applies 9% increased Damage taken to Enemies": {"enchant": "Consecrated Ground from Purifying Flame applies 9% increased Damage taken to Enemies", "type": "currency very high"},
	"1 Consecrated Path deals 40% increased Damage": {"enchant": "Consecrated Path deals 40% increased Damage", "type": "currency very high"},
	"1 Discipline has 20% reduced Mana Reservation": {"enchant": "Discipline has 20% reduced Mana Reservation", "type": "currency very high"},
	"1 Divine Ire Damages 2 additional nearby Enemies when gaining Stages": {"enchant": "Divine Ire Damages 2 additional nearby Enemies when gaining Stages", "type": "currency very high"},
	"1 Divine Ire deals 40% increased Damage": {"enchant": "Divine Ire deals 40% increased Damage", "type": "currency very high"},
	"1 Double Strike has a 15% chance to deal Double Damage to Bleeding Enemies": {"enchant": "Double Strike has a 15% chance to deal Double Damage to Bleeding Enemies", "type": "currency very high"},
	"1 Dread Banner has 40% increased Aura Effect": {"enchant": "Dread Banner has 40% increased Aura Effect", "type": "currency very high"},
	"1 Elemental Hit deals 40% increased Damage": {"enchant": "Elemental Hit deals 40% increased Damage", "type": "currency very high"},
	"1 Hatred has 15% reduced Mana Reservation": {"enchant": "Hatred has 15% reduced Mana Reservation", "type": "currency very high"},
	"1 Heavy Strike has a 12% chance to deal Double Damage": {"enchant": "Heavy Strike has a 12% chance to deal Double Damage", "type": "currency very high"},
	"1 Herald of Agony has 20% reduced Mana Reservation": {"enchant": "Herald of Agony has 20% reduced Mana Reservation", "type": "currency very high"},
	"1 Herald of Agony has 30% reduced Mana Reservation": {"enchant": "Herald of Agony has 30% reduced Mana Reservation", "type": "currency extremely high"},
	"1 Holy Flame Totem deals 40% increased Damage": {"enchant": "Holy Flame Totem deals 40% increased Damage", "type": "currency very high"},
	"1 Holy Flame Totem fires 2 additional Projectiles": {"enchant": "Holy Flame Totem fires 2 additional Projectiles", "type": "currency very high"},
	"1 Holy Flame Totem has 30% increased Projectile Speed": {"enchant": "Holy Flame Totem has 30% increased Projectile Speed", "type": "currency very high"},
	"1 Ice Golems deal 40% increased Damage": {"enchant": "Ice Golems deal 40% increased Damage", "type": "currency very high"},
	"1 Ice Spear fires an additional Projectile": {"enchant": "Ice Spear fires an additional Projectile", "type": "currency extremely high"},
	"1 Incinerate has +2 to maximum stages": {"enchant": "Incinerate has +2 to maximum stages", "type": "currency very high"},
	"1 Lightning Trap Damage Penetrates 10% Lightning Resistance": {"enchant": "Lightning Trap Damage Penetrates 10% Lightning Resistance", "type": "currency very high"},
	"1 Lightning Trap pierces 3 additional Targets": {"enchant": "Lightning Trap pierces 3 additional Targets", "type": "currency very high"},
	"1 Magma Orb Chains an additional 2 times": {"enchant": "Magma Orb Chains an additional 2 times", "type": "currency very high"},
	"1 Molten Strike fires 2 additional Projectiles": {"enchant": "Molten Strike fires 2 additional Projectiles", "type": "currency extremely high"},
	"1 Molten Strike fires an additional Projectile": {"enchant": "Molten Strike fires an additional Projectile", "type": "currency very high"},
	"1 Purifying Flame deals 40% increased Damage": {"enchant": "Purifying Flame deals 40% increased Damage", "type": "currency very high"},
	"1 Purity of Fire has 20% reduced Mana Reservation": {"enchant": "Purity of Fire has 20% reduced Mana Reservation", "type": "currency very high"},
	"1 Scourge Arrow creates an additional spore pod at Maximum Stages": {"enchant": "Scourge Arrow creates an additional spore pod at Maximum Stages", "type": "currency very high"},
	"1 Soulrend deals 40% increased Damage": {"enchant": "Soulrend deals 40% increased Damage", "type": "currency very high"},
	"1 Soulrend fires an additional Projectile": {"enchant": "Soulrend fires an additional Projectile", "type": "currency very high"},
	"1 Spark fires 3 additional Projectiles": {"enchant": "Spark fires 3 additional Projectiles", "type": "currency very high"},
	"1 Storm Brand Damage Penetrates 12% of Branded Enemy's Lightning Resistance": {"enchant": "Storm Brand Damage Penetrates 12% of Branded Enemy's Lightning Resistance", "type": "currency very high"},
	"1 Storm Brand deals 40% increased Damage": {"enchant": "Storm Brand deals 40% increased Damage", "type": "currency very high"},
	"1 Storm Burst has a 15% chance to create an additional Orb": {"enchant": "Storm Burst has a 15% chance to create an additional Orb", "type": "currency very high"},
	"1 Summoned Agony Crawler fires 2 additional Projectiles": {"enchant": "Summoned Agony Crawler fires 2 additional Projectiles", "type": "currency very high"},
	"1 Tectonic Slam has 20% chance to create a Charged Slam": {"enchant": "Tectonic Slam has 20% chance to create a Charged Slam", "type": "currency very high"},
	"1 Tornado Shot fires 2 additional secondary Projectiles": {"enchant": "Tornado Shot fires 2 additional secondary Projectiles", "type": "currency extremely high"},
	"1 Tornado Shot fires an additional secondary Projectile": {"enchant": "Tornado Shot fires an additional secondary Projectile", "type": "currency very high"},
	"1 Toxic Rain deals 40% increased Damage": {"enchant": "Toxic Rain deals 40% increased Damage", "type": "currency very high"},
	"1 Toxic Rain fires 1 additional Arrow": {"enchant": "Toxic Rain fires 1 additional Arrow", "type": "currency very high"},
	"1 Wild Strike Chains an additional 6 times": {"enchant": "Wild Strike Chains an additional 6 times", "type": "currency very high"},
	"1 Winter Orb deals 25% increased Damage": {"enchant": "Winter Orb deals 25% increased Damage", "type": "currency very high"},
	"1 Winter Orb deals 40% increased Damage": {"enchant": "Winter Orb deals 40% increased Damage", "type": "currency extremely high"},
	"1 Winter Orb has +2 Maximum Stages": {"enchant": "Winter Orb has +2 Maximum Stages", "type": "currency extremely high"},
	"1 Zealotry has 15% reduced Mana Reservation": {"enchant": "Zealotry has 15% reduced Mana Reservation", "type": "currency very high"},
}
