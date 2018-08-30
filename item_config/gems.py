#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "gems"

# Base type : settings pair
items = {
	"01 Quality Gem 20": {"class": "Gems", "other": ["Quality 20"], "type": "currency high"},
	"02 Quality Gem High": {"class": "Gems", "other": ["Quality >= 10"], "type": "gem very high"},
	"03 Quality Gem": {"class": "Gems", "other": ["Quality >= 1"], "type": "gem high"},
	"1 Portal": {"base": "Portal", "class": "Gems", "type": "gem normal"},
	"1 Detonate Mines": {"base": "Detonate Mines", "class": "Gems", "type": "gem low"},
	"1 Empower": {"base": "Empower Support", "class": "Gems", "type": "gem normal"},
	"1 Enhance": {"base": "Enhance Support", "class": "Gems", "type": "ignore"},
	"1 Enlighten": {"base": "Enlighten Support", "class": "Gems", "type": "gem normal"},
	"1 Added Chaos Damage": {"base": "Added Chaos Damage Support", "class": "Gems", "type": "gem low"},
	"8 Vaal Gems": {"base": "Vaal", "class": "Gems", "type": "gem low"},
	"9 Other Gems": {"class": "Gems", "type": "ignore"},
	
	# Autogenerated list
	"1 Abyssal Cry": {"base": "Abyssal Cry", "class": "Gems", "type": "ignore"},
	"1 Added Cold Damage Support": {"base": "Added Cold Damage Support", "class": "Gems", "type": "ignore"},
	"1 Added Fire Damage Support": {"base": "Added Fire Damage Support", "class": "Gems", "type": "ignore"},
	"1 Added Lightning Damage Support": {"base": "Added Lightning Damage Support", "class": "Gems", "type": "ignore"},
	"1 Additional Accuracy Support": {"base": "Additional Accuracy Support", "class": "Gems", "type": "ignore"},
	"1 Advanced Traps Support": {"base": "Advanced Traps Support", "class": "Gems", "type": "ignore"},
	"1 Ancestral Call Support": {"base": "Ancestral Call Support", "class": "Gems", "type": "ignore"},
	"1 Ancestral Protector": {"base": "Ancestral Protector", "class": "Gems", "type": "ignore"},
	"1 Ancestral Warchief": {"base": "Ancestral Warchief", "class": "Gems", "type": "ignore"},
	"1 Anger": {"base": "Anger", "class": "Gems", "type": "ignore"},
	"1 Animate Guardian": {"base": "Animate Guardian", "class": "Gems", "type": "ignore"},
	"1 Animate Weapon": {"base": "Animate Weapon", "class": "Gems", "type": "ignore"},
	"1 Arc": {"base": "Arc", "class": "Gems", "type": "ignore"},
	"1 Arcane Surge Support": {"base": "Arcane Surge Support", "class": "Gems", "type": "ignore"},
	"1 Arctic Armour": {"base": "Arctic Armour", "class": "Gems", "type": "ignore"},
	"1 Arctic Breath": {"base": "Arctic Breath", "class": "Gems", "type": "ignore"},
	"1 Assassin's Mark": {"base": "Assassin's Mark", "class": "Gems", "type": "ignore"},
	"1 Ball Lightning": {"base": "Ball Lightning", "class": "Gems", "type": "ignore"},
	"1 Barrage": {"base": "Barrage", "class": "Gems", "type": "ignore"},
	"1 Bear Trap": {"base": "Bear Trap", "class": "Gems", "type": "ignore"},
	"1 Blade Flurry": {"base": "Blade Flurry", "class": "Gems", "type": "ignore"},
	"1 Blade Vortex": {"base": "Blade Vortex", "class": "Gems", "type": "ignore"},
	"1 Bladefall": {"base": "Bladefall", "class": "Gems", "type": "ignore"},
	"1 Blasphemy Support": {"base": "Blasphemy Support", "class": "Gems", "type": "ignore"},
	"1 Blast Rain": {"base": "Blast Rain", "class": "Gems", "type": "ignore"},
	"1 Blight": {"base": "Blight", "class": "Gems", "type": "ignore"},
	"1 Blind Support": {"base": "Blind Support", "class": "Gems", "type": "ignore"},
	"1 Blink Arrow": {"base": "Blink Arrow", "class": "Gems", "type": "ignore"},
	"1 Block Chance Reduction Support": {"base": "Block Chance Reduction Support", "class": "Gems", "type": "ignore"},
	"1 Blood Magic Support": {"base": "Blood Magic Support", "class": "Gems", "type": "ignore"},
	"1 Blood Rage": {"base": "Blood Rage", "class": "Gems", "type": "ignore"},
	"1 Bloodlust Support": {"base": "Bloodlust Support", "class": "Gems", "type": "ignore"},
	"1 Bodyswap": {"base": "Bodyswap", "class": "Gems", "type": "ignore"},
	"1 Bone Offering": {"base": "Bone Offering", "class": "Gems", "type": "ignore"},
	"1 Brutality Support": {"base": "Brutality Support", "class": "Gems", "type": "ignore"},
	"1 Burning Arrow": {"base": "Burning Arrow", "class": "Gems", "type": "ignore"},
	"1 Burning Damage Support": {"base": "Burning Damage Support", "class": "Gems", "type": "ignore"},
	"1 Cast On Critical Strike Support": {"base": "Cast On Critical Strike Support", "class": "Gems", "type": "ignore"},
	"1 Cast on Death Support": {"base": "Cast on Death Support", "class": "Gems", "type": "ignore"},
	"1 Cast on Melee Kill Support": {"base": "Cast on Melee Kill Support", "class": "Gems", "type": "ignore"},
	"1 Cast when Damage Taken Support": {"base": "Cast when Damage Taken Support", "class": "Gems", "type": "ignore"},
	"1 Cast when Stunned Support": {"base": "Cast when Stunned Support", "class": "Gems", "type": "ignore"},
	"1 Cast while Channelling Support": {"base": "Cast while Channelling Support", "class": "Gems", "type": "ignore"},
	"1 Caustic Arrow": {"base": "Caustic Arrow", "class": "Gems", "type": "ignore"},
	"1 Chain Support": {"base": "Chain Support", "class": "Gems", "type": "ignore"},
	"1 Chance to Bleed Support": {"base": "Chance to Bleed Support", "class": "Gems", "type": "ignore"},
	"1 Chance to Flee Support": {"base": "Chance to Flee Support", "class": "Gems", "type": "ignore"},
	"1 Charged Dash": {"base": "Charged Dash", "class": "Gems", "type": "ignore"},
	"1 Charged Traps Support": {"base": "Charged Traps Support", "class": "Gems", "type": "ignore"},
	"1 Clarity": {"base": "Clarity", "class": "Gems", "type": "ignore"},
	"1 Cleave": {"base": "Cleave", "class": "Gems", "type": "ignore"},
	"1 Cluster Traps Support": {"base": "Cluster Traps Support", "class": "Gems", "type": "ignore"},
	"1 Cold Penetration Support": {"base": "Cold Penetration Support", "class": "Gems", "type": "ignore"},
	"1 Cold Snap": {"base": "Cold Snap", "class": "Gems", "type": "ignore"},
	"1 Cold to Fire Support": {"base": "Cold to Fire Support", "class": "Gems", "type": "ignore"},
	"1 Combustion Support": {"base": "Combustion Support", "class": "Gems", "type": "ignore"},
	"1 Concentrated Effect Support": {"base": "Concentrated Effect Support", "class": "Gems", "type": "ignore"},
	"1 Conductivity": {"base": "Conductivity", "class": "Gems", "type": "ignore"},
	"1 Consecrated Path": {"base": "Consecrated Path", "class": "Gems", "type": "ignore"},
	"1 Contagion": {"base": "Contagion", "class": "Gems", "type": "ignore"},
	"1 Controlled Destruction Support": {"base": "Controlled Destruction Support", "class": "Gems", "type": "ignore"},
	"1 Conversion Trap": {"base": "Conversion Trap", "class": "Gems", "type": "ignore"},
	"1 Convocation": {"base": "Convocation", "class": "Gems", "type": "ignore"},
	"1 Cremation": {"base": "Cremation", "class": "Gems", "type": "ignore"},
	"1 Culling Strike Support": {"base": "Culling Strike Support", "class": "Gems", "type": "ignore"},
	"1 Curse On Hit Support": {"base": "Curse On Hit Support", "class": "Gems", "type": "ignore"},
	"1 Cyclone": {"base": "Cyclone", "class": "Gems", "type": "ignore"},
	"1 Damage on Full Life Support": {"base": "Damage on Full Life Support", "class": "Gems", "type": "ignore"},
	"1 Dark Pact": {"base": "Dark Pact", "class": "Gems", "type": "ignore"},
	"1 Deadly Ailments Support": {"base": "Deadly Ailments Support", "class": "Gems", "type": "ignore"},
	"1 Decay Support": {"base": "Decay Support", "class": "Gems", "type": "ignore"},
	"1 Decoy Totem": {"base": "Decoy Totem", "class": "Gems", "type": "ignore"},
	"1 Desecrate": {"base": "Desecrate", "class": "Gems", "type": "ignore"},
	"1 Despair": {"base": "Despair", "class": "Gems", "type": "ignore"},
	"1 Determination": {"base": "Determination", "class": "Gems", "type": "ignore"},
	"1 Detonate Dead": {"base": "Detonate Dead", "class": "Gems", "type": "ignore"},
	"1 Devouring Totem": {"base": "Devouring Totem", "class": "Gems", "type": "ignore"},
	"1 Discharge": {"base": "Discharge", "class": "Gems", "type": "ignore"},
	"1 Discipline": {"base": "Discipline", "class": "Gems", "type": "ignore"},
	"1 Dominating Blow": {"base": "Dominating Blow", "class": "Gems", "type": "ignore"},
	"1 Double Strike": {"base": "Double Strike", "class": "Gems", "type": "ignore"},
	"1 Dual Strike": {"base": "Dual Strike", "class": "Gems", "type": "ignore"},
	"1 Earthquake": {"base": "Earthquake", "class": "Gems", "type": "ignore"},
	"1 Efficacy Support": {"base": "Efficacy Support", "class": "Gems", "type": "ignore"},
	"1 Elemental Damage with Attacks Support": {"base": "Elemental Damage with Attacks Support", "class": "Gems", "type": "ignore"},
	"1 Elemental Focus Support": {"base": "Elemental Focus Support", "class": "Gems", "type": "ignore"},
	"1 Elemental Hit": {"base": "Elemental Hit", "class": "Gems", "type": "ignore"},
	"1 Elemental Proliferation Support": {"base": "Elemental Proliferation Support", "class": "Gems", "type": "ignore"},
	"1 Elemental Weakness": {"base": "Elemental Weakness", "class": "Gems", "type": "ignore"},
	"1 Endurance Charge on Melee Stun Support": {"base": "Endurance Charge on Melee Stun Support", "class": "Gems", "type": "ignore"},
	"1 Enduring Cry": {"base": "Enduring Cry", "class": "Gems", "type": "ignore"},
	"1 Enfeeble": {"base": "Enfeeble", "class": "Gems", "type": "ignore"},
	"1 Essence Drain": {"base": "Essence Drain", "class": "Gems", "type": "ignore"},
	"1 Ethereal Knives": {"base": "Ethereal Knives", "class": "Gems", "type": "ignore"},
	"1 Explosive Arrow": {"base": "Explosive Arrow", "class": "Gems", "type": "ignore"},
	"1 Explosive Trap": {"base": "Explosive Trap", "class": "Gems", "type": "ignore"},
	"1 Faster Attacks Support": {"base": "Faster Attacks Support", "class": "Gems", "type": "ignore"},
	"1 Faster Casting Support": {"base": "Faster Casting Support", "class": "Gems", "type": "ignore"},
	"1 Faster Projectiles Support": {"base": "Faster Projectiles Support", "class": "Gems", "type": "ignore"},
	"1 Fire Nova Mine": {"base": "Fire Nova Mine", "class": "Gems", "type": "ignore"},
	"1 Fire Penetration Support": {"base": "Fire Penetration Support", "class": "Gems", "type": "ignore"},
	"1 Fire Trap": {"base": "Fire Trap", "class": "Gems", "type": "ignore"},
	"1 Fireball": {"base": "Fireball", "class": "Gems", "type": "ignore"},
	"1 Firestorm": {"base": "Firestorm", "class": "Gems", "type": "ignore"},
	"1 Flame Dash": {"base": "Flame Dash", "class": "Gems", "type": "ignore"},
	"1 Flame Surge": {"base": "Flame Surge", "class": "Gems", "type": "ignore"},
	"1 Flame Totem": {"base": "Flame Totem", "class": "Gems", "type": "ignore"},
	"1 Flameblast": {"base": "Flameblast", "class": "Gems", "type": "ignore"},
	"1 Flamethrower Trap": {"base": "Flamethrower Trap", "class": "Gems", "type": "ignore"},
	"1 Flammability": {"base": "Flammability", "class": "Gems", "type": "ignore"},
	"1 Flesh Offering": {"base": "Flesh Offering", "class": "Gems", "type": "ignore"},
	"1 Flicker Strike": {"base": "Flicker Strike", "class": "Gems", "type": "ignore"},
	"1 Fork Support": {"base": "Fork Support", "class": "Gems", "type": "ignore"},
	"1 Fortify Support": {"base": "Fortify Support", "class": "Gems", "type": "ignore"},
	"1 Freeze Mine": {"base": "Freeze Mine", "class": "Gems", "type": "ignore"},
	"1 Freezing Pulse": {"base": "Freezing Pulse", "class": "Gems", "type": "ignore"},
	"1 Frenzy": {"base": "Frenzy", "class": "Gems", "type": "ignore"},
	"1 Frost Blades": {"base": "Frost Blades", "class": "Gems", "type": "ignore"},
	"1 Frost Bomb": {"base": "Frost Bomb", "class": "Gems", "type": "ignore"},
	"1 Frost Wall": {"base": "Frost Wall", "class": "Gems", "type": "ignore"},
	"1 Frostbite": {"base": "Frostbite", "class": "Gems", "type": "ignore"},
	"1 Frostbolt": {"base": "Frostbolt", "class": "Gems", "type": "ignore"},
	"1 Generosity Support": {"base": "Generosity Support", "class": "Gems", "type": "ignore"},
	"1 Glacial Cascade": {"base": "Glacial Cascade", "class": "Gems", "type": "ignore"},
	"1 Glacial Hammer": {"base": "Glacial Hammer", "class": "Gems", "type": "ignore"},
	"1 Grace": {"base": "Grace", "class": "Gems", "type": "ignore"},
	"1 Greater Multiple Projectiles Support": {"base": "Greater Multiple Projectiles Support", "class": "Gems", "type": "ignore"},
	"1 Ground Slam": {"base": "Ground Slam", "class": "Gems", "type": "ignore"},
	"1 Haste": {"base": "Haste", "class": "Gems", "type": "ignore"},
	"1 Hatred": {"base": "Hatred", "class": "Gems", "type": "ignore"},
	"1 Heavy Strike": {"base": "Heavy Strike", "class": "Gems", "type": "ignore"},
	"1 Herald of Agony": {"base": "Herald of Agony", "class": "Gems", "type": "ignore"},
	"1 Herald of Ash": {"base": "Herald of Ash", "class": "Gems", "type": "ignore"},
	"1 Herald of Ice": {"base": "Herald of Ice", "class": "Gems", "type": "ignore"},
	"1 Herald of Purity": {"base": "Herald of Purity", "class": "Gems", "type": "ignore"},
	"1 Herald of Thunder": {"base": "Herald of Thunder", "class": "Gems", "type": "ignore"},
	"1 Hypothermia Support": {"base": "Hypothermia Support", "class": "Gems", "type": "ignore"},
	"1 Ice Bite Support": {"base": "Ice Bite Support", "class": "Gems", "type": "ignore"},
	"1 Ice Crash": {"base": "Ice Crash", "class": "Gems", "type": "ignore"},
	"1 Ice Nova": {"base": "Ice Nova", "class": "Gems", "type": "ignore"},
	"1 Ice Shot": {"base": "Ice Shot", "class": "Gems", "type": "ignore"},
	"1 Ice Spear": {"base": "Ice Spear", "class": "Gems", "type": "ignore"},
	"1 Ice Trap": {"base": "Ice Trap", "class": "Gems", "type": "ignore"},
	"1 Ignite Proliferation Support": {"base": "Ignite Proliferation Support", "class": "Gems", "type": "ignore"},
	"1 Immolate Support": {"base": "Immolate Support", "class": "Gems", "type": "ignore"},
	"1 Immortal Call": {"base": "Immortal Call", "class": "Gems", "type": "ignore"},
	"1 Incinerate": {"base": "Incinerate", "class": "Gems", "type": "ignore"},
	"1 Increased Area of Effect Support": {"base": "Increased Area of Effect Support", "class": "Gems", "type": "ignore"},
	"1 Increased Critical Damage Support": {"base": "Increased Critical Damage Support", "class": "Gems", "type": "ignore"},
	"1 Increased Critical Strikes Support": {"base": "Increased Critical Strikes Support", "class": "Gems", "type": "ignore"},
	"1 Increased Duration Support": {"base": "Increased Duration Support", "class": "Gems", "type": "ignore"},
	"1 Infernal Blow": {"base": "Infernal Blow", "class": "Gems", "type": "ignore"},
	"1 Innervate Support": {"base": "Innervate Support", "class": "Gems", "type": "ignore"},
	"1 Iron Grip Support": {"base": "Iron Grip Support", "class": "Gems", "type": "ignore"},
	"1 Iron Will Support": {"base": "Iron Will Support", "class": "Gems", "type": "ignore"},
	"1 Item Quantity Support": {"base": "Item Quantity Support", "class": "Gems", "type": "ignore"},
	"1 Item Rarity Support": {"base": "Item Rarity Support", "class": "Gems", "type": "ignore"},
	"1 Kinetic Blast": {"base": "Kinetic Blast", "class": "Gems", "type": "ignore"},
	"1 Knockback Support": {"base": "Knockback Support", "class": "Gems", "type": "ignore"},
	"1 Lacerate": {"base": "Lacerate", "class": "Gems", "type": "ignore"},
	"1 Leap Slam": {"base": "Leap Slam", "class": "Gems", "type": "ignore"},
	"1 Less Duration Support": {"base": "Less Duration Support", "class": "Gems", "type": "ignore"},
	"1 Lesser Multiple Projectiles Support": {"base": "Lesser Multiple Projectiles Support", "class": "Gems", "type": "ignore"},
	"1 Lesser Poison Support": {"base": "Lesser Poison Support", "class": "Gems", "type": "ignore"},
	"1 Life Gain on Hit Support": {"base": "Life Gain on Hit Support", "class": "Gems", "type": "ignore"},
	"1 Life Leech Support": {"base": "Life Leech Support", "class": "Gems", "type": "ignore"},
	"1 Lightning Arrow": {"base": "Lightning Arrow", "class": "Gems", "type": "ignore"},
	"1 Lightning Penetration Support": {"base": "Lightning Penetration Support", "class": "Gems", "type": "ignore"},
	"1 Lightning Spire Trap": {"base": "Lightning Spire Trap", "class": "Gems", "type": "ignore"},
	"1 Lightning Strike": {"base": "Lightning Strike", "class": "Gems", "type": "ignore"},
	"1 Lightning Tendrils": {"base": "Lightning Tendrils", "class": "Gems", "type": "ignore"},
	"1 Lightning Trap": {"base": "Lightning Trap", "class": "Gems", "type": "ignore"},
	"1 Lightning Warp": {"base": "Lightning Warp", "class": "Gems", "type": "ignore"},
	"1 Magma Orb": {"base": "Magma Orb", "class": "Gems", "type": "ignore"},
	"1 Maim Support": {"base": "Maim Support", "class": "Gems", "type": "ignore"},
	"1 Mana Leech Support": {"base": "Mana Leech Support", "class": "Gems", "type": "ignore"},
	"1 Melee Physical Damage Support": {"base": "Melee Physical Damage Support", "class": "Gems", "type": "ignore"},
	"1 Melee Splash Support": {"base": "Melee Splash Support", "class": "Gems", "type": "ignore"},
	"1 Minefield Support": {"base": "Minefield Support", "class": "Gems", "type": "ignore"},
	"1 Minion Damage Support": {"base": "Minion Damage Support", "class": "Gems", "type": "ignore"},
	"1 Minion Life Support": {"base": "Minion Life Support", "class": "Gems", "type": "ignore"},
	"1 Minion Speed Support": {"base": "Minion Speed Support", "class": "Gems", "type": "ignore"},
	"1 Minion and Totem Elemental Resistance Support": {"base": "Minion and Totem Elemental Resistance Support", "class": "Gems", "type": "ignore"},
	"1 Mirage Archer Support": {"base": "Mirage Archer Support", "class": "Gems", "type": "ignore"},
	"1 Mirror Arrow": {"base": "Mirror Arrow", "class": "Gems", "type": "ignore"},
	"1 Molten Shell": {"base": "Molten Shell", "class": "Gems", "type": "ignore"},
	"1 Molten Strike": {"base": "Molten Strike", "class": "Gems", "type": "ignore"},
	"1 Multiple Traps Support": {"base": "Multiple Traps Support", "class": "Gems", "type": "ignore"},
	"1 Multistrike Support": {"base": "Multistrike Support", "class": "Gems", "type": "ignore"},
	"1 Onslaught Support": {"base": "Onslaught Support", "class": "Gems", "type": "ignore"},
	"1 Orb of Storms": {"base": "Orb of Storms", "class": "Gems", "type": "ignore"},
	"1 Phase Run": {"base": "Phase Run", "class": "Gems", "type": "ignore"},
	"1 Physical Projectile Attack Damage Support": {"base": "Physical Projectile Attack Damage Support", "class": "Gems", "type": "ignore"},
	"1 Physical to Lightning Support": {"base": "Physical to Lightning Support", "class": "Gems", "type": "ignore"},
	"1 Pierce Support": {"base": "Pierce Support", "class": "Gems", "type": "ignore"},
	"1 Poacher's Mark": {"base": "Poacher's Mark", "class": "Gems", "type": "ignore"},
	"1 Point Blank Support": {"base": "Point Blank Support", "class": "Gems", "type": "ignore"},
	"1 Poison Support": {"base": "Poison Support", "class": "Gems", "type": "ignore"},
	"1 Power Charge On Critical Support": {"base": "Power Charge On Critical Support", "class": "Gems", "type": "ignore"},
	"1 Power Siphon": {"base": "Power Siphon", "class": "Gems", "type": "ignore"},
	"1 Projectile Weakness": {"base": "Projectile Weakness", "class": "Gems", "type": "ignore"},
	"1 Puncture": {"base": "Puncture", "class": "Gems", "type": "ignore"},
	"1 Punishment": {"base": "Punishment", "class": "Gems", "type": "ignore"},
	"1 Purity of Elements": {"base": "Purity of Elements", "class": "Gems", "type": "ignore"},
	"1 Purity of Fire": {"base": "Purity of Fire", "class": "Gems", "type": "ignore"},
	"1 Purity of Ice": {"base": "Purity of Ice", "class": "Gems", "type": "ignore"},
	"1 Purity of Lightning": {"base": "Purity of Lightning", "class": "Gems", "type": "ignore"},
	"1 Rain of Arrows": {"base": "Rain of Arrows", "class": "Gems", "type": "ignore"},
	"1 Raise Spectre": {"base": "Raise Spectre", "class": "Gems", "type": "ignore"},
	"1 Raise Zombie": {"base": "Raise Zombie", "class": "Gems", "type": "ignore"},
	"1 Rallying Cry": {"base": "Rallying Cry", "class": "Gems", "type": "ignore"},
	"1 Ranged Attack Totem Support": {"base": "Ranged Attack Totem Support", "class": "Gems", "type": "ignore"},
	"1 Reave": {"base": "Reave", "class": "Gems", "type": "ignore"},
	"1 Reckoning": {"base": "Reckoning", "class": "Gems", "type": "ignore"},
	"1 Reduced Mana Support": {"base": "Reduced Mana Support", "class": "Gems", "type": "ignore"},
	"1 Rejuvenation Totem": {"base": "Rejuvenation Totem", "class": "Gems", "type": "ignore"},
	"1 Remote Mine Support": {"base": "Remote Mine Support", "class": "Gems", "type": "ignore"},
	"1 Righteous Fire": {"base": "Righteous Fire", "class": "Gems", "type": "ignore"},
	"1 Riposte": {"base": "Riposte", "class": "Gems", "type": "ignore"},
	"1 Ruthless Support": {"base": "Ruthless Support", "class": "Gems", "type": "ignore"},
	"1 Scorching Ray": {"base": "Scorching Ray", "class": "Gems", "type": "ignore"},
	"1 Scourge Arrow": {"base": "Scourge Arrow", "class": "Gems", "type": "ignore"},
	"1 Searing Bond": {"base": "Searing Bond", "class": "Gems", "type": "ignore"},
	"1 Seismic Trap": {"base": "Seismic Trap", "class": "Gems", "type": "ignore"},
	"1 Shield Charge": {"base": "Shield Charge", "class": "Gems", "type": "ignore"},
	"1 Shock Nova": {"base": "Shock Nova", "class": "Gems", "type": "ignore"},
	"1 Shockwave Totem": {"base": "Shockwave Totem", "class": "Gems", "type": "ignore"},
	"1 Shrapnel Shot": {"base": "Shrapnel Shot", "class": "Gems", "type": "ignore"},
	"1 Siege Ballista": {"base": "Siege Ballista", "class": "Gems", "type": "ignore"},
	"1 Siphoning Trap": {"base": "Siphoning Trap", "class": "Gems", "type": "ignore"},
	"1 Slower Projectiles Support": {"base": "Slower Projectiles Support", "class": "Gems", "type": "ignore"},
	"1 Smite": {"base": "Smite", "class": "Gems", "type": "ignore"},
	"1 Smoke Mine": {"base": "Smoke Mine", "class": "Gems", "type": "ignore"},
	"1 Spark": {"base": "Spark", "class": "Gems", "type": "ignore"},
	"1 Spectral Shield Throw": {"base": "Spectral Shield Throw", "class": "Gems", "type": "ignore"},
	"1 Spectral Throw": {"base": "Spectral Throw", "class": "Gems", "type": "ignore"},
	"1 Spell Cascade Support": {"base": "Spell Cascade Support", "class": "Gems", "type": "ignore"},
	"1 Spell Echo Support": {"base": "Spell Echo Support", "class": "Gems", "type": "ignore"},
	"1 Spell Totem Support": {"base": "Spell Totem Support", "class": "Gems", "type": "ignore"},
	"1 Spirit Offering": {"base": "Spirit Offering", "class": "Gems", "type": "ignore"},
	"1 Split Arrow": {"base": "Split Arrow", "class": "Gems", "type": "ignore"},
	"1 Static Strike": {"base": "Static Strike", "class": "Gems", "type": "ignore"},
	"1 Storm Barrier Support": {"base": "Storm Barrier Support", "class": "Gems", "type": "ignore"},
	"1 Storm Burst": {"base": "Storm Burst", "class": "Gems", "type": "ignore"},
	"1 Storm Call": {"base": "Storm Call", "class": "Gems", "type": "ignore"},
	"1 Stun Support": {"base": "Stun Support", "class": "Gems", "type": "ignore"},
	"1 Summon Chaos Golem": {"base": "Summon Chaos Golem", "class": "Gems", "type": "ignore"},
	"1 Summon Flame Golem": {"base": "Summon Flame Golem", "class": "Gems", "type": "ignore"},
	"1 Summon Holy Relic": {"base": "Summon Holy Relic", "class": "Gems", "type": "ignore"},
	"1 Summon Ice Golem": {"base": "Summon Ice Golem", "class": "Gems", "type": "ignore"},
	"1 Summon Lightning Golem": {"base": "Summon Lightning Golem", "class": "Gems", "type": "ignore"},
	"1 Summon Phantasm on Kill Support": {"base": "Summon Phantasm on Kill Support", "class": "Gems", "type": "ignore"},
	"1 Summon Raging Spirit": {"base": "Summon Raging Spirit", "class": "Gems", "type": "ignore"},
	"1 Summon Skeleton": {"base": "Summon Skeleton", "class": "Gems", "type": "ignore"},
	"1 Summon Stone Golem": {"base": "Summon Stone Golem", "class": "Gems", "type": "ignore"},
	"1 Sunder": {"base": "Sunder", "class": "Gems", "type": "ignore"},
	"1 Sweep": {"base": "Sweep", "class": "Gems", "type": "ignore"},
	"1 Swift Affliction Support": {"base": "Swift Affliction Support", "class": "Gems", "type": "ignore"},
	"1 Tectonic Slam": {"base": "Tectonic Slam", "class": "Gems", "type": "ignore"},
	"1 Tempest Shield": {"base": "Tempest Shield", "class": "Gems", "type": "ignore"},
	"1 Temporal Chains": {"base": "Temporal Chains", "class": "Gems", "type": "ignore"},
	"1 Tornado Shot": {"base": "Tornado Shot", "class": "Gems", "type": "ignore"},
	"1 Toxic Rain": {"base": "Toxic Rain", "class": "Gems", "type": "ignore"},
	"1 Trap Support": {"base": "Trap Support", "class": "Gems", "type": "ignore"},
	"1 Trap and Mine Damage Support": {"base": "Trap and Mine Damage Support", "class": "Gems", "type": "ignore"},
	"1 Unbound Ailments Support": {"base": "Unbound Ailments Support", "class": "Gems", "type": "ignore"},
	"1 Unearth": {"base": "Unearth", "class": "Gems", "type": "ignore"},
	"1 Vaal Ancestral Warchief": {"base": "Vaal Ancestral Warchief", "class": "Gems", "type": "ignore"},
	"1 Vaal Arc": {"base": "Vaal Arc", "class": "Gems", "type": "ignore"},
	"1 Vaal Blade Vortex": {"base": "Vaal Blade Vortex", "class": "Gems", "type": "ignore"},
	"1 Vaal Blight": {"base": "Vaal Blight", "class": "Gems", "type": "ignore"},
	"1 Vaal Breach": {"base": "Vaal Breach", "class": "Gems", "type": "ignore"},
	"1 Vaal Burning Arrow": {"base": "Vaal Burning Arrow", "class": "Gems", "type": "ignore"},
	"1 Vaal Clarity": {"base": "Vaal Clarity", "class": "Gems", "type": "ignore"},
	"1 Vaal Cold Snap": {"base": "Vaal Cold Snap", "class": "Gems", "type": "ignore"},
	"1 Vaal Cyclone": {"base": "Vaal Cyclone", "class": "Gems", "type": "ignore"},
	"1 Vaal Detonate Dead": {"base": "Vaal Detonate Dead", "class": "Gems", "type": "ignore"},
	"1 Vaal Discipline": {"base": "Vaal Discipline", "class": "Gems", "type": "ignore"},
	"1 Vaal Double Strike": {"base": "Vaal Double Strike", "class": "Gems", "type": "ignore"},
	"1 Vaal Earthquake": {"base": "Vaal Earthquake", "class": "Gems", "type": "ignore"},
	"1 Vaal Fireball": {"base": "Vaal Fireball", "class": "Gems", "type": "ignore"},
	"1 Vaal Flameblast": {"base": "Vaal Flameblast", "class": "Gems", "type": "ignore"},
	"1 Vaal Glacial Hammer": {"base": "Vaal Glacial Hammer", "class": "Gems", "type": "ignore"},
	"1 Vaal Grace": {"base": "Vaal Grace", "class": "Gems", "type": "ignore"},
	"1 Vaal Ground Slam": {"base": "Vaal Ground Slam", "class": "Gems", "type": "ignore"},
	"1 Vaal Haste": {"base": "Vaal Haste", "class": "Gems", "type": "ignore"},
	"1 Vaal Ice Nova": {"base": "Vaal Ice Nova", "class": "Gems", "type": "ignore"},
	"1 Vaal Immortal Call": {"base": "Vaal Immortal Call", "class": "Gems", "type": "ignore"},
	"1 Vaal Impurity of Fire": {"base": "Vaal Impurity of Fire", "class": "Gems", "type": "ignore"},
	"1 Vaal Impurity of Ice": {"base": "Vaal Impurity of Ice", "class": "Gems", "type": "ignore"},
	"1 Vaal Impurity of Lightning": {"base": "Vaal Impurity of Lightning", "class": "Gems", "type": "ignore"},
	"1 Vaal Lightning Strike": {"base": "Vaal Lightning Strike", "class": "Gems", "type": "ignore"},
	"1 Vaal Lightning Trap": {"base": "Vaal Lightning Trap", "class": "Gems", "type": "ignore"},
	"1 Vaal Lightning Warp": {"base": "Vaal Lightning Warp", "class": "Gems", "type": "ignore"},
	"1 Vaal Molten Shell": {"base": "Vaal Molten Shell", "class": "Gems", "type": "ignore"},
	"1 Vaal Power Siphon": {"base": "Vaal Power Siphon", "class": "Gems", "type": "ignore"},
	"1 Vaal Rain of Arrows": {"base": "Vaal Rain of Arrows", "class": "Gems", "type": "ignore"},
	"1 Vaal Reave": {"base": "Vaal Reave", "class": "Gems", "type": "ignore"},
	"1 Vaal Righteous Fire": {"base": "Vaal Righteous Fire", "class": "Gems", "type": "ignore"},
	"1 Vaal Spark": {"base": "Vaal Spark", "class": "Gems", "type": "ignore"},
	"1 Vaal Spectral Throw": {"base": "Vaal Spectral Throw", "class": "Gems", "type": "ignore"},
	"1 Vaal Storm Call": {"base": "Vaal Storm Call", "class": "Gems", "type": "ignore"},
	"1 Vaal Summon Skeletons": {"base": "Vaal Summon Skeletons", "class": "Gems", "type": "ignore"},
	"1 Vengeance": {"base": "Vengeance", "class": "Gems", "type": "ignore"},
	"1 Vigilant Strike": {"base": "Vigilant Strike", "class": "Gems", "type": "ignore"},
	"1 Vile Toxins Support": {"base": "Vile Toxins Support", "class": "Gems", "type": "ignore"},
	"1 Viper Strike": {"base": "Viper Strike", "class": "Gems", "type": "ignore"},
	"1 Vitality": {"base": "Vitality", "class": "Gems", "type": "ignore"},
	"1 Void Manipulation Support": {"base": "Void Manipulation Support", "class": "Gems", "type": "ignore"},
	"1 Volatile Dead": {"base": "Volatile Dead", "class": "Gems", "type": "ignore"},
	"1 Volley Support": {"base": "Volley Support", "class": "Gems", "type": "ignore"},
	"1 Vortex": {"base": "Vortex", "class": "Gems", "type": "ignore"},
	"1 Vulnerability": {"base": "Vulnerability", "class": "Gems", "type": "ignore"},
	"1 Warlord's Mark": {"base": "Warlord's Mark", "class": "Gems", "type": "ignore"},
	"1 Whirling Blades": {"base": "Whirling Blades", "class": "Gems", "type": "ignore"},
	"1 Wild Strike": {"base": "Wild Strike", "class": "Gems", "type": "ignore"},
	"1 Wither": {"base": "Wither", "class": "Gems", "type": "ignore"},
	"1 Withering Touch Support": {"base": "Withering Touch Support", "class": "Gems", "type": "ignore"},
	"1 Wrath": {"base": "Wrath", "class": "Gems", "type": "ignore"},
}