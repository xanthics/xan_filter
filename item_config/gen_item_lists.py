#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher

bases = {
	"Weapon": {
		"Bow|Dex|Ranged|Two|Weapon": [
			{'drop': 1, 'base': 'Bow', 'name': 'Crude Bow'},
			{'drop': 5, 'base': 'Bow', 'name': 'Short Bow'},
			{'drop': 9, 'base': 'Bow', 'name': 'Long Bow'},
			{'drop': 14, 'base': 'Bow', 'name': 'Composite Bow'},
			{'drop': 18, 'base': 'Bow', 'name': 'Recurve Bow'},
			{'drop': 23, 'base': 'Bow', 'name': 'Bone Bow'},
			{'drop': 28, 'base': 'Bow', 'name': 'Royal Bow'},  # Elemental Damage With Attack Skills +(20 to 24)
			{'drop': 32, 'base': 'Bow', 'name': 'Death Bow'},  # Local Critical Strike Chance +(30 to 50)
			{'drop': 35, 'base': 'Bow', 'name': 'Grove Bow'},
			{'drop': 36, 'base': 'Bow', 'name': 'Reflex Bow'},  # Base Movement Velocity +(4)
			{'drop': 38, 'base': 'Bow', 'name': 'Decurve Bow'},
			{'drop': 41, 'base': 'Bow', 'name': 'Compound Bow'},
			{'drop': 44, 'base': 'Bow', 'name': 'Sniper Bow'},
			{'drop': 47, 'base': 'Bow', 'name': 'Ivory Bow'},
			{'drop': 50, 'base': 'Bow', 'name': 'Highborn Bow'},  # Elemental Damage With Attack Skills +(20 to 24)
			{'drop': 53, 'base': 'Bow', 'name': 'Decimation Bow'},  # Local Critical Strike Chance +(30 to 50)
			{'drop': 56, 'base': 'Bow', 'name': 'Thicket Bow'},
			{'drop': 57, 'base': 'Bow', 'name': 'Steelwood Bow'},  # Base Movement Velocity +(4)
			{'drop': 58, 'base': 'Bow', 'name': 'Citadel Bow'},
			{'drop': 60, 'base': 'Bow', 'name': 'Ranger Bow'},
			{'drop': 62, 'base': 'Bow', 'name': 'Assassin Bow'},
			{'drop': 64, 'base': 'Bow', 'name': 'Spine Bow'},
			{'drop': 66, 'base': 'Bow', 'name': 'Imperial Bow'},  # Elemental Damage With Attack Skills +(20 to 24)
			{'drop': 68, 'base': 'Bow', 'name': 'Harbinger Bow'},  # Local Critical Strike Chance +(30 to 50)
			{'drop': 71, 'base': 'Bow', 'name': 'Maraketh Bow'},  # Base Movement Velocity +(6)
		],
		"Claw|Dex|Int|Melee|One|Weapon": [
			{'drop': 3, 'base': 'Claw', 'name': 'Nailed Fist'},  # Local Life Gain Per Target (3)
			{'drop': 7, 'base': 'Claw', 'name': 'Sharktooth Claw'},  # Local Life Gain Per Target (6)
			{'drop': 12, 'base': 'Claw', 'name': 'Awl'},  # Local Life Gain Per Target (7)
			{'drop': 17, 'base': 'Claw', 'name': "Cat's Paw"},  # Local Life Gain Per Target (8)
			{'drop': 22, 'base': 'Claw', 'name': 'Blinder'},  # Local Life Gain Per Target (12)
			{'drop': 26, 'base': 'Claw', 'name': 'Timeworn Claw'},  # Local Life Gain Per Target (19)
			{'drop': 30, 'base': 'Claw', 'name': 'Sparkling Claw'},  # Local Life Gain Per Target (15)
			{'drop': 34, 'base': 'Claw', 'name': 'Fright Claw'},  # Local Life Gain Per Target (20)
			{'drop': 36, 'base': 'Claw', 'name': 'Double Claw'},  # Local Mana Gain Per Target (6), Local Life Gain Per Target (15)
			{'drop': 37, 'base': 'Claw', 'name': 'Thresher Claw'},  # Local Life Gain Per Target (25)
			{'drop': 40, 'base': 'Claw', 'name': 'Gouger'},  # Local Life Gain Per Target (24)
			{'drop': 43, 'base': 'Claw', 'name': "Tiger's Paw"},  # Local Life Leech From Physical Damage (1.6)
			{'drop': 46, 'base': 'Claw', 'name': 'Gut Ripper'},  # Local Life Gain Per Target (44)
			{'drop': 49, 'base': 'Claw', 'name': 'Prehistoric Claw'},  # Local Life Leech From Physical Damage (2.0)
			{'drop': 52, 'base': 'Claw', 'name': 'Noble Claw'},  # Local Life Gain Per Target (40)
			{'drop': 55, 'base': 'Claw', 'name': 'Eagle Claw'},  # Local Life Leech From Physical Damage (2.0)
			{'drop': 57, 'base': 'Claw', 'name': 'Twin Claw'},  # Local Mana Gain Per Target (10), Local Life Gain Per Target (28)
			{'drop': 58, 'base': 'Claw', 'name': 'Great White Claw'},  # Local Life Gain Per Target (46)
			{'drop': 60, 'base': 'Claw', 'name': 'Throat Stabber'},  # Local Life Gain Per Target (40)
			{'drop': 62, 'base': 'Claw', 'name': "Hellion's Paw"},  # Local Life Leech From Physical Damage (1.6)
			{'drop': 64, 'base': 'Claw', 'name': 'Eye Gouger'},  # Local Life Gain Per Target (50)
			{'drop': 66, 'base': 'Claw', 'name': 'Vaal Claw'},  # Local Life Leech From Physical Damage (2.0)
			{'drop': 68, 'base': 'Claw', 'name': 'Imperial Claw'},  # Local Life Gain Per Target (46)
			{'drop': 70, 'base': 'Claw', 'name': 'Terror Claw'},  # Local Life Leech From Physical Damage (2.0)
			{'drop': 72, 'base': 'Claw', 'name': 'Gemini Claw'},  # Local Mana Gain Per Target (14), Local Life Gain Per Target (38)
		],
		"Caster|Dagger|Dex|Int|Melee|One|Weapon": [
			{'drop': 1, 'base': 'Dagger', 'name': 'Glass Shank'},  # Critical Strike Chance +(30)
			{'drop': 5, 'base': 'Dagger', 'name': 'Skinning Knife'},  # Critical Strike Chance +(30)
			{'drop': 10, 'base': 'Dagger', 'name': 'Carving Knife'},  # Critical Strike Chance +(30)
			{'drop': 15, 'base': 'Dagger', 'name': 'Stiletto'},  # Critical Strike Chance +(30)
			{'drop': 20, 'base': 'Dagger', 'name': 'Boot Knife'},  # Critical Strike Chance +(30)
			{'drop': 24, 'base': 'Dagger', 'name': 'Copper Kris'},  # Critical Strike Chance +(50)
			{'drop': 28, 'base': 'Dagger', 'name': 'Skean'},  # Critical Strike Chance +(30)
			{'drop': 32, 'base': 'Dagger', 'name': 'Imp Dagger'},  # Critical Strike Chance +(40)
			{'drop': 35, 'base': 'Dagger', 'name': 'Flaying Knife'},  # Critical Strike Chance +(30)
			{'drop': 36, 'base': 'Dagger', 'name': 'Prong Dagger'},  # Monster Base Block (4)
			{'drop': 38, 'base': 'Dagger', 'name': 'Butcher Knife'},  # Critical Strike Chance +(30)
			{'drop': 41, 'base': 'Dagger', 'name': 'Poignard'},  # Critical Strike Chance +(30)
			{'drop': 44, 'base': 'Dagger', 'name': 'Boot Blade'},  # Critical Strike Chance +(30)
			{'drop': 47, 'base': 'Dagger', 'name': 'Golden Kris'},  # Critical Strike Chance +(50)
			{'drop': 50, 'base': 'Dagger', 'name': 'Royal Skean'},  # Critical Strike Chance +(30)
			{'drop': 53, 'base': 'Dagger', 'name': 'Fiend Dagger'},  # Critical Strike Chance +(40)
			{'drop': 55, 'base': 'Dagger', 'name': 'Trisula'},  # Monster Base Block (4)
			{'drop': 56, 'base': 'Dagger', 'name': 'Gutting Knife'},  # Critical Strike Chance +(30)
			{'drop': 58, 'base': 'Dagger', 'name': 'Slaughter Knife'},  # Critical Strike Chance +(30)
			{'drop': 60, 'base': 'Dagger', 'name': 'Ambusher'},  # Critical Strike Chance +(30)
			{'drop': 62, 'base': 'Dagger', 'name': 'Ezomyte Dagger'},  # Critical Strike Chance +(30)
			{'drop': 64, 'base': 'Dagger', 'name': 'Platinum Kris'},  # Critical Strike Chance +(50)
			{'drop': 66, 'base': 'Dagger', 'name': 'Imperial Skean'},  # Critical Strike Chance +(30)
			{'drop': 68, 'base': 'Dagger', 'name': 'Demon Dagger'},  # Critical Strike Chance +(40)
			{'drop': 70, 'base': 'Dagger', 'name': 'Sai'},  # Monster Base Block (6)
		],
		"Dex|Melee|One|One Hand Axe|Str|Weapon": [
			{'drop': 2, 'base': 'One Hand Axe', 'name': 'Rusted Hatchet'},
			{'drop': 6, 'base': 'One Hand Axe', 'name': 'Jade Hatchet'},
			{'drop': 11, 'base': 'One Hand Axe', 'name': 'Boarding Axe'},
			{'drop': 16, 'base': 'One Hand Axe', 'name': 'Cleaver'},
			{'drop': 21, 'base': 'One Hand Axe', 'name': 'Broad Axe'},
			{'drop': 25, 'base': 'One Hand Axe', 'name': 'Arming Axe'},
			{'drop': 29, 'base': 'One Hand Axe', 'name': 'Decorative Axe'},
			{'drop': 33, 'base': 'One Hand Axe', 'name': 'Spectral Axe'},
			{'drop': 35, 'base': 'One Hand Axe', 'name': 'Etched Hatchet'},  # Physical Damage +(8)
			{'drop': 36, 'base': 'One Hand Axe', 'name': 'Jasper Axe'},
			{'drop': 39, 'base': 'One Hand Axe', 'name': 'Tomahawk'},
			{'drop': 42, 'base': 'One Hand Axe', 'name': 'Wrist Chopper'},
			{'drop': 45, 'base': 'One Hand Axe', 'name': 'War Axe'},
			{'drop': 48, 'base': 'One Hand Axe', 'name': 'Chest Splitter'},
			{'drop': 51, 'base': 'One Hand Axe', 'name': 'Ceremonial Axe'},
			{'drop': 54, 'base': 'One Hand Axe', 'name': 'Wraith Axe'},
			{'drop': 56, 'base': 'One Hand Axe', 'name': 'Engraved Hatchet'},  # Physical Damage +(8)
			{'drop': 57, 'base': 'One Hand Axe', 'name': 'Karui Axe'},
			{'drop': 59, 'base': 'One Hand Axe', 'name': 'Siege Axe'},
			{'drop': 61, 'base': 'One Hand Axe', 'name': 'Reaver Axe'},
			{'drop': 63, 'base': 'One Hand Axe', 'name': 'Butcher Axe'},
			{'drop': 65, 'base': 'One Hand Axe', 'name': 'Vaal Hatchet'},
			{'drop': 67, 'base': 'One Hand Axe', 'name': 'Royal Axe'},
			{'drop': 69, 'base': 'One Hand Axe', 'name': 'Infernal Axe'},
			{'drop': 71, 'base': 'One Hand Axe', 'name': 'Runic Hatchet'},  # Physical Damage +(12)
		],
		"Melee|One|One Hand Mace|Str|Weapon": [
			{'drop': 1, 'base': 'One Hand Mace', 'name': 'Driftwood Club'},  # Base Stun Threshold Reduction +(10)
			{'drop': 5, 'base': 'One Hand Mace', 'name': 'Tribal Club'},  # Base Stun Threshold Reduction +(10)
			{'drop': 10, 'base': 'One Hand Mace', 'name': 'Spiked Club'},  # Base Stun Threshold Reduction +(10)
			{'drop': 15, 'base': 'One Hand Mace', 'name': 'Stone Hammer'},  # Base Stun Threshold Reduction +(15)
			{'drop': 20, 'base': 'One Hand Mace', 'name': 'War Hammer'},  # Base Stun Threshold Reduction +(10)
			{'drop': 24, 'base': 'One Hand Mace', 'name': 'Bladed Mace'},  # Base Stun Threshold Reduction +(10)
			{'drop': 28, 'base': 'One Hand Mace', 'name': 'Ceremonial Mace'},  # Base Stun Threshold Reduction +(15)
			{'drop': 32, 'base': 'One Hand Mace', 'name': 'Dream Mace'},  # Base Stun Threshold Reduction +(10)
			{'drop': 34, 'base': 'One Hand Mace', 'name': 'Wyrm Mace'},  # Local Attack Speed +(4)
			{'drop': 35, 'base': 'One Hand Mace', 'name': 'Petrified Club'},  # Base Stun Threshold Reduction +(10)
			{'drop': 38, 'base': 'One Hand Mace', 'name': 'Barbed Club'},  # Base Stun Threshold Reduction +(10)
			{'drop': 41, 'base': 'One Hand Mace', 'name': 'Rock Breaker'},  # Base Stun Threshold Reduction +(15)
			{'drop': 44, 'base': 'One Hand Mace', 'name': 'Battle Hammer'},  # Base Stun Threshold Reduction +(10)
			{'drop': 47, 'base': 'One Hand Mace', 'name': 'Flanged Mace'},  # Base Stun Threshold Reduction +(10)
			{'drop': 50, 'base': 'One Hand Mace', 'name': 'Ornate Mace'},  # Base Stun Threshold Reduction +(15)
			{'drop': 53, 'base': 'One Hand Mace', 'name': 'Phantom Mace'},  # Base Stun Threshold Reduction +(10)
			{'drop': 55, 'base': 'One Hand Mace', 'name': 'Dragon Mace'},  # Local Attack Speed +(4)
			{'drop': 56, 'base': 'One Hand Mace', 'name': 'Ancestral Club'},  # Base Stun Threshold Reduction +(10)
			{'drop': 58, 'base': 'One Hand Mace', 'name': 'Tenderizer'},  # Base Stun Threshold Reduction +(10)
			{'drop': 60, 'base': 'One Hand Mace', 'name': 'Gavel'},  # Base Stun Threshold Reduction +(15)
			{'drop': 62, 'base': 'One Hand Mace', 'name': 'Legion Hammer'},  # Base Stun Threshold Reduction +(10)
			{'drop': 64, 'base': 'One Hand Mace', 'name': 'Pernarch'},  # Base Stun Threshold Reduction +(10)
			{'drop': 66, 'base': 'One Hand Mace', 'name': 'Auric Mace'},  # Base Stun Threshold Reduction +(15)
			{'drop': 68, 'base': 'One Hand Mace', 'name': 'Nightmare Mace'},  # Base Stun Threshold Reduction +(10)
			{'drop': 70, 'base': 'One Hand Mace', 'name': 'Behemoth Mace'},  # Local Attack Speed +(6)
		],
		"Dex|Melee|One|One Hand Sword|Str|Weapon": [
			{'drop': 1, 'base': 'One Hand Sword', 'name': 'Rusted Sword'},  # Local Accuracy Rating +(40)
			{'drop': 5, 'base': 'One Hand Sword', 'name': 'Copper Sword'},  # Local Accuracy Rating (45)
			{'drop': 10, 'base': 'One Hand Sword', 'name': 'Sabre'},  # Local Accuracy Rating +(40)
			{'drop': 15, 'base': 'One Hand Sword', 'name': 'Broad Sword'},  # Local Accuracy Rating +(40)
			{'drop': 20, 'base': 'One Hand Sword', 'name': 'War Sword'},  # Local Accuracy Rating +(40)
			{'drop': 24, 'base': 'One Hand Sword', 'name': 'Ancient Sword'},  # Local Accuracy Rating (165)
			{'drop': 28, 'base': 'One Hand Sword', 'name': 'Elegant Sword'},  # Local Accuracy Rating (190)
			{'drop': 32, 'base': 'One Hand Sword', 'name': 'Dusk Blade'},  # Local Accuracy Rating +(40)
			{'drop': 34, 'base': 'One Hand Sword', 'name': 'Hook Sword'},  # Base Chance To Dodge (4)
			{'drop': 35, 'base': 'One Hand Sword', 'name': 'Variscite Blade'},  # Local Accuracy Rating (240)
			{'drop': 38, 'base': 'One Hand Sword', 'name': 'Cutlass'},  # Local Accuracy Rating +(40)
			{'drop': 41, 'base': 'One Hand Sword', 'name': 'Baselard'},  # Local Accuracy Rating +(40)
			{'drop': 44, 'base': 'One Hand Sword', 'name': 'Battle Sword'},  # Local Accuracy Rating +(40)
			{'drop': 47, 'base': 'One Hand Sword', 'name': 'Elder Sword'},  # Local Accuracy Rating (330)
			{'drop': 50, 'base': 'One Hand Sword', 'name': 'Graceful Sword'},  # Local Accuracy Rating (350)
			{'drop': 53, 'base': 'One Hand Sword', 'name': 'Twilight Blade'},  # Local Accuracy Rating +(40)
			{'drop': 55, 'base': 'One Hand Sword', 'name': 'Grappler'},  # Base Chance To Dodge (4)
			{'drop': 56, 'base': 'One Hand Sword', 'name': 'Gemstone Sword'},  # Local Accuracy Rating (400)
			{'drop': 58, 'base': 'One Hand Sword', 'name': 'Corsair Sword'},  # Local Accuracy Rating +(40)
			{'drop': 60, 'base': 'One Hand Sword', 'name': 'Gladius'},  # Local Accuracy Rating +(40)
			{'drop': 62, 'base': 'One Hand Sword', 'name': 'Legion Sword'},  # Local Accuracy Rating +(40)
			{'drop': 64, 'base': 'One Hand Sword', 'name': 'Vaal Blade'},  # Local Accuracy Rating (460)
			{'drop': 66, 'base': 'One Hand Sword', 'name': 'Eternal Sword'},  # Local Accuracy Rating (475)
			{'drop': 68, 'base': 'One Hand Sword', 'name': 'Midnight Blade'},  # Local Accuracy Rating +(40)
			{'drop': 70, 'base': 'One Hand Sword', 'name': 'Tiger Hook'},  # Base Chance To Dodge (6)
		],
		"Caster|Int|Melee|One|Sceptre|Str|Weapon": [
			{'drop': 1, 'base': 'Sceptre', 'name': 'Driftwood Sceptre'},  # Elemental Damage +(10)
			{'drop': 5, 'base': 'Sceptre', 'name': 'Darkwood Sceptre'},  # Elemental Damage +(12)
			{'drop': 10, 'base': 'Sceptre', 'name': 'Bronze Sceptre'},  # Elemental Damage +(12)
			{'drop': 15, 'base': 'Sceptre', 'name': 'Quartz Sceptre'},  # Elemental Damage +(20)
			{'drop': 20, 'base': 'Sceptre', 'name': 'Iron Sceptre'},  # Elemental Damage +(14)
			{'drop': 24, 'base': 'Sceptre', 'name': 'Ochre Sceptre'},  # Elemental Damage +(16)
			{'drop': 28, 'base': 'Sceptre', 'name': 'Ritual Sceptre'},  # Elemental Damage +(16)
			{'drop': 32, 'base': 'Sceptre', 'name': 'Shadow Sceptre'},  # Elemental Damage +(22)
			{'drop': 35, 'base': 'Sceptre', 'name': 'Grinning Fetish'},  # Elemental Damage +(18)
			{'drop': 36, 'base': 'Sceptre', 'name': 'Horned Sceptre'},  # Reduce Enemy Elemental Resistance (4)
			{'drop': 38, 'base': 'Sceptre', 'name': 'Sekhem'},  # Elemental Damage +(18)
			{'drop': 41, 'base': 'Sceptre', 'name': 'Crystal Sceptre'},  # Elemental Damage +(30)
			{'drop': 44, 'base': 'Sceptre', 'name': 'Lead Sceptre'},  # Elemental Damage +(22)
			{'drop': 47, 'base': 'Sceptre', 'name': 'Blood Sceptre'},  # Elemental Damage +(24)
			{'drop': 50, 'base': 'Sceptre', 'name': 'Royal Sceptre'},  # Elemental Damage +(24)
			{'drop': 53, 'base': 'Sceptre', 'name': 'Abyssal Sceptre'},  # Elemental Damage +(30)
			{'drop': 55, 'base': 'Sceptre', 'name': 'Stag Sceptre'},  # Reduce Enemy Elemental Resistance (4)
			{'drop': 56, 'base': 'Sceptre', 'name': 'Karui Sceptre'},  # Elemental Damage +(26)
			{'drop': 58, 'base': 'Sceptre', 'name': "Tyrant's Sekhem"},  # Elemental Damage +(26)
			{'drop': 60, 'base': 'Sceptre', 'name': 'Opal Sceptre'},  # Elemental Damage +(40)
			{'drop': 62, 'base': 'Sceptre', 'name': 'Platinum Sceptre'},  # Elemental Damage +(30)
			{'drop': 64, 'base': 'Sceptre', 'name': 'Vaal Sceptre'},  # Elemental Damage +(32)
			{'drop': 66, 'base': 'Sceptre', 'name': 'Carnal Sceptre'},  # Elemental Damage +(32)
			{'drop': 68, 'base': 'Sceptre', 'name': 'Void Sceptre'},  # Elemental Damage +(40)
			{'drop': 70, 'base': 'Sceptre', 'name': 'Sambar Sceptre'},  # Reduce Enemy Elemental Resistance (6)
		],
		"Caster|Int|Melee|Staff|Str|Two|Weapon": [
			{'drop': 4, 'base': 'Stave', 'name': 'Gnarled Branch'},  # Staff Block (18)
			{'drop': 9, 'base': 'Stave', 'name': 'Primitive Staff'},  # Staff Block (18)
			{'drop': 13, 'base': 'Stave', 'name': 'Long Staff'},  # Staff Block (18)
			{'drop': 18, 'base': 'Stave', 'name': 'Iron Staff'},  # Staff Block (18)
			{'drop': 23, 'base': 'Stave', 'name': 'Coiled Staff'},  # Staff Block (20)
			{'drop': 28, 'base': 'Stave', 'name': 'Royal Staff'},  # Staff Block (18)
			{'drop': 33, 'base': 'Stave', 'name': 'Vile Staff'},  # Staff Block (18)
			{'drop': 36, 'base': 'Stave', 'name': 'Crescent Staff'},  # Critical Strike Chance +(80)
			{'drop': 37, 'base': 'Stave', 'name': 'Woodful Staff'},  # Staff Block (18)
			{'drop': 41, 'base': 'Stave', 'name': 'Quarterstaff'},  # Staff Block (18)
			{'drop': 45, 'base': 'Stave', 'name': 'Military Staff'},  # Staff Block (18)
			{'drop': 49, 'base': 'Stave', 'name': 'Serpentine Staff'},  # Staff Block (20)
			{'drop': 52, 'base': 'Stave', 'name': 'Highborn Staff'},  # Staff Block (18)
			{'drop': 55, 'base': 'Stave', 'name': 'Foul Staff'},  # Staff Block (18)
			{'drop': 57, 'base': 'Stave', 'name': 'Moon Staff'},  # Critical Strike Chance +(80)
			{'drop': 58, 'base': 'Stave', 'name': 'Primordial Staff'},  # Staff Block (18)
			{'drop': 60, 'base': 'Stave', 'name': 'Lathi'},  # Staff Block (18)
			{'drop': 62, 'base': 'Stave', 'name': 'Ezomyte Staff'},  # Staff Block (18)
			{'drop': 64, 'base': 'Stave', 'name': 'Maelström Staff'},  # Staff Block (20)
			{'drop': 66, 'base': 'Stave', 'name': 'Imperial Staff'},  # Staff Block (18)
			{'drop': 68, 'base': 'Stave', 'name': 'Judgement Staff'},  # Staff Block (18)
			{'drop': 70, 'base': 'Stave', 'name': 'Eclipse Staff'},  # Critical Strike Chance +(100)
		],
		"Dex|Melee|One|Thrusting One Hand Sword|Weapon": [
			{'drop': 3, 'base': 'Thrusting One Hand Sword', 'name': 'Rusted Spike'},  # Base Critical Strike Multiplier +(25)
			{'drop': 7, 'base': 'Thrusting One Hand Sword', 'name': 'Whalebone Rapier'},  # Base Critical Strike Multiplier +(25)
			{'drop': 12, 'base': 'Thrusting One Hand Sword', 'name': 'Battered Foil'},  # Base Critical Strike Multiplier +(25)
			{'drop': 17, 'base': 'Thrusting One Hand Sword', 'name': 'Basket Rapier'},  # Base Critical Strike Multiplier +(25)
			{'drop': 22, 'base': 'Thrusting One Hand Sword', 'name': 'Jagged Foil'},  # Base Critical Strike Multiplier +(25)
			{'drop': 26, 'base': 'Thrusting One Hand Sword', 'name': 'Antique Rapier'},  # Base Critical Strike Multiplier +(25)
			{'drop': 30, 'base': 'Thrusting One Hand Sword', 'name': 'Elegant Foil'},  # Base Critical Strike Multiplier +(25)
			{'drop': 34, 'base': 'Thrusting One Hand Sword', 'name': 'Thorn Rapier'},  # Base Critical Strike Multiplier +(35)
			{'drop': 36, 'base': 'Thrusting One Hand Sword', 'name': 'Smallsword'},  # Local Chance To Bleed On Hit (15)
			{'drop': 37, 'base': 'Thrusting One Hand Sword', 'name': 'Wyrmbone Rapier'},  # Base Critical Strike Multiplier +(25)
			{'drop': 40, 'base': 'Thrusting One Hand Sword', 'name': 'Burnished Foil'},  # Base Critical Strike Multiplier +(25)
			{'drop': 43, 'base': 'Thrusting One Hand Sword', 'name': 'Estoc'},  # Base Critical Strike Multiplier +(25)
			{'drop': 46, 'base': 'Thrusting One Hand Sword', 'name': 'Serrated Foil'},  # Base Critical Strike Multiplier +(25)
			{'drop': 49, 'base': 'Thrusting One Hand Sword', 'name': 'Primeval Rapier'},  # Base Critical Strike Multiplier +(25)
			{'drop': 52, 'base': 'Thrusting One Hand Sword', 'name': 'Fancy Foil'},  # Base Critical Strike Multiplier +(25)
			{'drop': 55, 'base': 'Thrusting One Hand Sword', 'name': 'Apex Rapier'},  # Base Critical Strike Multiplier +(35)
			{'drop': 57, 'base': 'Thrusting One Hand Sword', 'name': 'Courtesan Sword'},  # Local Chance To Bleed On Hit (15)
			{'drop': 58, 'base': 'Thrusting One Hand Sword', 'name': 'Dragonbone Rapier'},  # Base Critical Strike Multiplier +(25)
			{'drop': 60, 'base': 'Thrusting One Hand Sword', 'name': 'Tempered Foil'},  # Base Critical Strike Multiplier +(25)
			{'drop': 62, 'base': 'Thrusting One Hand Sword', 'name': 'Pecoraro'},  # Base Critical Strike Multiplier +(25)
			{'drop': 64, 'base': 'Thrusting One Hand Sword', 'name': 'Spiraled Foil'},  # Base Critical Strike Multiplier +(25)
			{'drop': 66, 'base': 'Thrusting One Hand Sword', 'name': 'Vaal Rapier'},  # Base Critical Strike Multiplier +(25)
			{'drop': 68, 'base': 'Thrusting One Hand Sword', 'name': 'Jewelled Foil'},  # Base Critical Strike Multiplier +(25)
			{'drop': 70, 'base': 'Thrusting One Hand Sword', 'name': 'Harpy Rapier'},  # Base Critical Strike Multiplier +(35)
			{'drop': 72, 'base': 'Thrusting One Hand Sword', 'name': 'Dragoon Sword'},  # Local Chance To Bleed On Hit (20)
		],
		"Dex|Melee|Str|Two|Two Hand Axe|Weapon": [
			{'drop': 4, 'base': 'Two Hand Axe', 'name': 'Stone Axe'},
			{'drop': 9, 'base': 'Two Hand Axe', 'name': 'Jade Chopper'},
			{'drop': 13, 'base': 'Two Hand Axe', 'name': 'Woodsplitter'},
			{'drop': 18, 'base': 'Two Hand Axe', 'name': 'Poleaxe'},
			{'drop': 23, 'base': 'Two Hand Axe', 'name': 'Double Axe'},
			{'drop': 28, 'base': 'Two Hand Axe', 'name': 'Gilded Axe'},
			{'drop': 33, 'base': 'Two Hand Axe', 'name': 'Shadow Axe'},
			{'drop': 36, 'base': 'Two Hand Axe', 'name': 'Dagger Axe'},  # Local Critical Strike Chance +(50)
			{'drop': 37, 'base': 'Two Hand Axe', 'name': 'Jasper Chopper'},
			{'drop': 41, 'base': 'Two Hand Axe', 'name': 'Timber Axe'},
			{'drop': 45, 'base': 'Two Hand Axe', 'name': 'Headsman Axe'},
			{'drop': 49, 'base': 'Two Hand Axe', 'name': 'Labrys'},
			{'drop': 52, 'base': 'Two Hand Axe', 'name': 'Noble Axe'},
			{'drop': 55, 'base': 'Two Hand Axe', 'name': 'Abyssal Axe'},
			{'drop': 58, 'base': 'Two Hand Axe', 'name': 'Karui Chopper'},
			{'drop': 59, 'base': 'Two Hand Axe', 'name': 'Talon Axe'},  # Local Critical Strike Chance +(50)
			{'drop': 60, 'base': 'Two Hand Axe', 'name': 'Sundering Axe'},
			{'drop': 62, 'base': 'Two Hand Axe', 'name': 'Ezomyte Axe'},
			{'drop': 64, 'base': 'Two Hand Axe', 'name': 'Vaal Axe'},
			{'drop': 66, 'base': 'Two Hand Axe', 'name': 'Despot Axe'},
			{'drop': 68, 'base': 'Two Hand Axe', 'name': 'Void Axe'},
			{'drop': 70, 'base': 'Two Hand Axe', 'name': 'Fleshripper'},  # Local Critical Strike Chance +(50)
		],
		"Melee|Str|Two|Two Hand Mace|Weapon": [
			{'drop': 3, 'base': 'Two Hand Mace', 'name': 'Driftwood Maul'},  # Base Stun Duration +(30)
			{'drop': 8, 'base': 'Two Hand Mace', 'name': 'Tribal Maul'},  # Base Stun Duration +(30)
			{'drop': 12, 'base': 'Two Hand Mace', 'name': 'Mallet'},  # Base Stun Duration +(30)
			{'drop': 17, 'base': 'Two Hand Mace', 'name': 'Sledgehammer'},  # Base Stun Duration +(45)
			{'drop': 22, 'base': 'Two Hand Mace', 'name': 'Jagged Maul'},  # Base Stun Duration +(30)
			{'drop': 27, 'base': 'Two Hand Mace', 'name': 'Brass Maul'},  # Base Stun Duration +(30)
			{'drop': 32, 'base': 'Two Hand Mace', 'name': 'Fright Maul'},  # Base Stun Duration +(30)
			{'drop': 34, 'base': 'Two Hand Mace', 'name': 'Morning Star'},  # Base Skill Area Of Effect +(4)
			{'drop': 36, 'base': 'Two Hand Mace', 'name': 'Totemic Maul'},  # Base Stun Duration +(30)
			{'drop': 40, 'base': 'Two Hand Mace', 'name': 'Great Mallet'},  # Base Stun Duration +(30)
			{'drop': 44, 'base': 'Two Hand Mace', 'name': 'Steelhead'},  # Base Stun Duration +(45)
			{'drop': 48, 'base': 'Two Hand Mace', 'name': 'Spiny Maul'},  # Base Stun Duration +(30)
			{'drop': 51, 'base': 'Two Hand Mace', 'name': 'Plated Maul'},  # Base Stun Duration +(30)
			{'drop': 54, 'base': 'Two Hand Mace', 'name': 'Dread Maul'},  # Base Stun Duration +(30)
			{'drop': 56, 'base': 'Two Hand Mace', 'name': 'Solar Maul'},  # Base Skill Area Of Effect +(4)
			{'drop': 57, 'base': 'Two Hand Mace', 'name': 'Karui Maul'},  # Base Stun Duration +(30)
			{'drop': 59, 'base': 'Two Hand Mace', 'name': 'Colossus Mallet'},  # Base Stun Duration +(30)
			{'drop': 61, 'base': 'Two Hand Mace', 'name': 'Piledriver'},  # Base Stun Duration +(45)
			{'drop': 63, 'base': 'Two Hand Mace', 'name': 'Meatgrinder'},  # Base Stun Duration +(30)
			{'drop': 65, 'base': 'Two Hand Mace', 'name': 'Imperial Maul'},  # Base Stun Duration +(30)
			{'drop': 67, 'base': 'Two Hand Mace', 'name': 'Terror Maul'},  # Base Stun Duration +(30)
			{'drop': 69, 'base': 'Two Hand Mace', 'name': 'Coronal Maul'},  # Base Skill Area Of Effect +(6)
		],
		"Dex|Melee|Str|Two|Two Hand Sword|Weapon": [
			{'drop': 3, 'base': 'Two Hand Sword', 'name': 'Corroded Blade'},  # Local Accuracy Rating +(40)
			{'drop': 8, 'base': 'Two Hand Sword', 'name': 'Longsword'},  # Local Accuracy Rating (60)
			{'drop': 12, 'base': 'Two Hand Sword', 'name': 'Bastard Sword'},  # Local Accuracy Rating +(40)
			{'drop': 17, 'base': 'Two Hand Sword', 'name': 'Two-Handed Sword'},  # Local Accuracy Rating (120)
			{'drop': 22, 'base': 'Two Hand Sword', 'name': 'Etched Greatsword'},  # Local Accuracy Rating +(40)
			{'drop': 27, 'base': 'Two Hand Sword', 'name': 'Ornate Sword'},  # Local Accuracy Rating (185)
			{'drop': 32, 'base': 'Two Hand Sword', 'name': 'Spectral Sword'},  # Local Accuracy Rating +(30)
			{'drop': 35, 'base': 'Two Hand Sword', 'name': 'Curved Blade'},  # Base Critical Strike Multiplier +(40)
			{'drop': 36, 'base': 'Two Hand Sword', 'name': 'Butcher Sword'},  # Local Accuracy Rating (250)
			{'drop': 40, 'base': 'Two Hand Sword', 'name': 'Footman Sword'},  # Local Accuracy Rating +(40)
			{'drop': 44, 'base': 'Two Hand Sword', 'name': 'Highland Blade'},  # Local Accuracy Rating (305)
			{'drop': 48, 'base': 'Two Hand Sword', 'name': 'Engraved Greatsword'},  # Local Accuracy Rating +(40)
			{'drop': 51, 'base': 'Two Hand Sword', 'name': 'Tiger Sword'},  # Local Accuracy Rating (360)
			{'drop': 54, 'base': 'Two Hand Sword', 'name': 'Wraith Sword'},  # Local Accuracy Rating +(30)
			{'drop': 56, 'base': 'Two Hand Sword', 'name': 'Lithe Blade'},  # Base Critical Strike Multiplier +(40)
			{'drop': 57, 'base': 'Two Hand Sword', 'name': "Headman's Sword"},  # Local Accuracy Rating (400)
			{'drop': 59, 'base': 'Two Hand Sword', 'name': 'Reaver Sword'},  # Local Accuracy Rating +(40)
			{'drop': 61, 'base': 'Two Hand Sword', 'name': 'Ezomyte Blade'},  # Local Accuracy Rating (435)
			{'drop': 63, 'base': 'Two Hand Sword', 'name': 'Vaal Greatsword'},  # Local Accuracy Rating +(40)
			{'drop': 65, 'base': 'Two Hand Sword', 'name': 'Lion Sword'},  # Local Accuracy Rating (470)
			{'drop': 67, 'base': 'Two Hand Sword', 'name': 'Infernal Sword'},  # Local Accuracy Rating +(30)
			{'drop': 70, 'base': 'Two Hand Sword', 'name': 'Exquisite Blade'},  # Base Critical Strike Multiplier +(60)
		],
		"Caster|Int|One|Ranged|Wand|Weapon": [
			{'drop': 1, 'base': 'Wand', 'name': 'Driftwood Wand'},  # Spell Damage +(8 to 12)
			{'drop': 6, 'base': 'Wand', 'name': "Goat's Horn"},  # Spell Damage +(10 to 14)
			{'drop': 12, 'base': 'Wand', 'name': 'Carved Wand'},  # Spell Damage +(11 to 15)
			{'drop': 18, 'base': 'Wand', 'name': 'Quartz Wand'},  # Spell Damage +(18 to 22)
			{'drop': 24, 'base': 'Wand', 'name': 'Spiraled Wand'},  # Spell Damage +(15 to 19)
			{'drop': 30, 'base': 'Wand', 'name': 'Sage Wand'},  # Spell Damage +(17 to 21)
			{'drop': 34, 'base': 'Wand', 'name': 'Pagan Wand'},  # Cast Speed +(10)
			{'drop': 35, 'base': 'Wand', 'name': "Faun's Horn"},  # Spell Damage +(20 to 24)
			{'drop': 40, 'base': 'Wand', 'name': 'Engraved Wand'},  # Spell Damage +(22 to 26)
			{'drop': 45, 'base': 'Wand', 'name': 'Crystal Wand'},  # Spell Damage +(29 to 33)
			{'drop': 49, 'base': 'Wand', 'name': 'Serpent Wand'},  # Spell Damage +(26 to 30)
			{'drop': 53, 'base': 'Wand', 'name': 'Omen Wand'},  # Spell Damage +(27 to 31)
			{'drop': 55, 'base': 'Wand', 'name': 'Heathen Wand'},  # Cast Speed +(10)
			{'drop': 56, 'base': 'Wand', 'name': "Demon's Horn"},  # Spell Damage +(31 to 35)
			{'drop': 59, 'base': 'Wand', 'name': 'Imbued Wand'},  # Spell Damage +(33 to 37)
			{'drop': 62, 'base': 'Wand', 'name': 'Opal Wand'},  # Spell Damage +(38 to 42)
			{'drop': 65, 'base': 'Wand', 'name': 'Tornado Wand'},  # Spell Damage +(35 to 39)
			{'drop': 68, 'base': 'Wand', 'name': 'Prophecy Wand'},  # Spell Damage +(36 to 40)
			{'drop': 70, 'base': 'Wand', 'name': 'Profane Wand'},  # Cast Speed +(14)
		],
	},
	"Armour": {
		"Armour|Body Armour|Str": [
			{'drop': 1, 'base': 'Body Armour', 'name': 'Plate Vest'},
			{'drop': 6, 'base': 'Body Armour', 'name': 'Chestplate'},
			{'drop': 17, 'base': 'Body Armour', 'name': 'Copper Plate'},
			{'drop': 21, 'base': 'Body Armour', 'name': 'War Plate'},
			{'drop': 28, 'base': 'Body Armour', 'name': 'Full Plate'},
			{'drop': 32, 'base': 'Body Armour', 'name': 'Arena Plate'},
			{'drop': 35, 'base': 'Body Armour', 'name': 'Lordly Plate'},
			{'drop': 37, 'base': 'Body Armour', 'name': 'Bronze Plate'},
			{'drop': 41, 'base': 'Body Armour', 'name': 'Battle Plate'},
			{'drop': 45, 'base': 'Body Armour', 'name': 'Sun Plate'},
			{'drop': 49, 'base': 'Body Armour', 'name': 'Colosseum Plate'},
			{'drop': 53, 'base': 'Body Armour', 'name': 'Majestic Plate'},
			{'drop': 56, 'base': 'Body Armour', 'name': 'Golden Plate'},
			{'drop': 59, 'base': 'Body Armour', 'name': 'Crusader Plate'},
			{'drop': 62, 'base': 'Body Armour', 'name': 'Astral Plate'},  # Resist all Elements (8 to 12)
			{'drop': 65, 'base': 'Body Armour', 'name': 'Gladiator Plate'},
			{'drop': 68, 'base': 'Body Armour', 'name': 'Glorious Plate'},
		],
		"Armour|Body Armour|Dex": [
			{'drop': 2, 'base': 'Body Armour', 'name': 'Shabby Jerkin'},
			{'drop': 9, 'base': 'Body Armour', 'name': 'Strapped Leather'},
			{'drop': 17, 'base': 'Body Armour', 'name': 'Buckskin Tunic'},
			{'drop': 25, 'base': 'Body Armour', 'name': 'Wild Leather'},
			{'drop': 28, 'base': 'Body Armour', 'name': 'Full Leather'},
			{'drop': 32, 'base': 'Body Armour', 'name': 'Sun Leather'},
			{'drop': 35, 'base': 'Body Armour', 'name': "Thief's Garb"},
			{'drop': 37, 'base': 'Body Armour', 'name': 'Eelskin Tunic'},
			{'drop': 41, 'base': 'Body Armour', 'name': 'Frontier Leather'},
			{'drop': 45, 'base': 'Body Armour', 'name': 'Glorious Leather'},
			{'drop': 49, 'base': 'Body Armour', 'name': 'Coronal Leather'},
			{'drop': 53, 'base': 'Body Armour', 'name': "Cutthroat's Garb"},
			{'drop': 56, 'base': 'Body Armour', 'name': 'Sharkskin Tunic'},
			{'drop': 59, 'base': 'Body Armour', 'name': 'Destiny Leather'},
			{'drop': 62, 'base': 'Body Armour', 'name': 'Exquisite Leather'},
			{'drop': 65, 'base': 'Body Armour', 'name': 'Zodiac Leather'},
			{'drop': 68, 'base': 'Body Armour', 'name': "Assassin's Garb"},  # Base Movement Velocity +(3)
		],
		"Armour|Body Armour|Int": [
			{'drop': 3, 'base': 'Body Armour', 'name': 'Simple Robe'},
			{'drop': 11, 'base': 'Body Armour', 'name': 'Silken Vest'},
			{'drop': 18, 'base': 'Body Armour', 'name': "Scholar's Robe"},
			{'drop': 25, 'base': 'Body Armour', 'name': 'Silken Garb'},
			{'drop': 28, 'base': 'Body Armour', 'name': "Mage's Vestment"},
			{'drop': 32, 'base': 'Body Armour', 'name': 'Silk Robe'},
			{'drop': 35, 'base': 'Body Armour', 'name': 'Cabalist Regalia'},
			{'drop': 37, 'base': 'Body Armour', 'name': "Sage's Robe"},
			{'drop': 41, 'base': 'Body Armour', 'name': 'Silken Wrap'},
			{'drop': 45, 'base': 'Body Armour', 'name': "Conjurer's Vestment"},
			{'drop': 49, 'base': 'Body Armour', 'name': 'Spidersilk Robe'},
			{'drop': 53, 'base': 'Body Armour', 'name': 'Destroyer Regalia'},
			{'drop': 56, 'base': 'Body Armour', 'name': "Savant's Robe"},
			{'drop': 59, 'base': 'Body Armour', 'name': 'Necromancer Silks'},
			{'drop': 62, 'base': 'Body Armour', 'name': "Occultist's Vestment"},  # Spell Damage +(3 to 10)
			{'drop': 65, 'base': 'Body Armour', 'name': 'Widowsilk Robe'},
			{'drop': 68, 'base': 'Body Armour', 'name': 'Vaal Regalia'},
		],
		"Armour|Body Armour|Dex|Int": [
			{'drop': 4, 'base': 'Body Armour', 'name': 'Padded Vest'},
			{'drop': 9, 'base': 'Body Armour', 'name': 'Oiled Vest'},
			{'drop': 18, 'base': 'Body Armour', 'name': 'Padded Jacket'},
			{'drop': 22, 'base': 'Body Armour', 'name': 'Oiled Coat'},
			{'drop': 28, 'base': 'Body Armour', 'name': 'Scarlet Raiment'},
			{'drop': 32, 'base': 'Body Armour', 'name': 'Waxed Garb'},
			{'drop': 35, 'base': 'Body Armour', 'name': 'Bone Armour'},
			{'drop': 40, 'base': 'Body Armour', 'name': 'Quilted Jacket'},
			{'drop': 44, 'base': 'Body Armour', 'name': 'Sleek Coat'},
			{'drop': 48, 'base': 'Body Armour', 'name': 'Crimson Raiment'},
			{'drop': 52, 'base': 'Body Armour', 'name': 'Lacquered Garb'},
			{'drop': 56, 'base': 'Body Armour', 'name': 'Crypt Armour'},
			{'drop': 59, 'base': 'Body Armour', 'name': 'Sentinel Jacket'},
			{'drop': 62, 'base': 'Body Armour', 'name': 'Varnished Coat'},
			{'drop': 65, 'base': 'Body Armour', 'name': 'Blood Raiment'},
			{'drop': 68, 'base': 'Body Armour', 'name': 'Sadist Garb'},
			{'drop': 71, 'base': 'Body Armour', 'name': 'Carnal Armour'},  # Base Maximum Mana (20 to 25)
		],
		"Armour|Body Armour|Int|Str": [
			{'drop': 4, 'base': 'Body Armour', 'name': 'Chainmail Vest'},
			{'drop': 8, 'base': 'Body Armour', 'name': 'Chainmail Tunic'},
			{'drop': 17, 'base': 'Body Armour', 'name': 'Ringmail Coat'},
			{'drop': 21, 'base': 'Body Armour', 'name': 'Chainmail Doublet'},
			{'drop': 28, 'base': 'Body Armour', 'name': 'Full Ringmail'},
			{'drop': 32, 'base': 'Body Armour', 'name': 'Full Chainmail'},
			{'drop': 35, 'base': 'Body Armour', 'name': 'Holy Chainmail'},
			{'drop': 39, 'base': 'Body Armour', 'name': 'Latticed Ringmail'},
			{'drop': 43, 'base': 'Body Armour', 'name': 'Crusader Chainmail'},
			{'drop': 47, 'base': 'Body Armour', 'name': 'Ornate Ringmail'},
			{'drop': 51, 'base': 'Body Armour', 'name': 'Chain Hauberk'},
			{'drop': 55, 'base': 'Body Armour', 'name': 'Devout Chainmail'},
			{'drop': 58, 'base': 'Body Armour', 'name': 'Loricated Ringmail'},
			{'drop': 61, 'base': 'Body Armour', 'name': 'Conquest Chainmail'},
			{'drop': 64, 'base': 'Body Armour', 'name': 'Elegant Ringmail'},
			{'drop': 67, 'base': 'Body Armour', 'name': "Saint's Hauberk"},
			{'drop': 70, 'base': 'Body Armour', 'name': 'Saintly Chainmail'},
		],
		"Armour|Body Armour|Dex|Str": [
			{'drop': 4, 'base': 'Body Armour', 'name': 'Scale Vest'},
			{'drop': 8, 'base': 'Body Armour', 'name': 'Light Brigandine'},
			{'drop': 17, 'base': 'Body Armour', 'name': 'Scale Doublet'},
			{'drop': 21, 'base': 'Body Armour', 'name': 'Infantry Brigandine'},
			{'drop': 28, 'base': 'Body Armour', 'name': 'Full Scale Armour'},
			{'drop': 32, 'base': 'Body Armour', 'name': "Soldier's Brigandine"},
			{'drop': 35, 'base': 'Body Armour', 'name': 'Field Lamellar'},
			{'drop': 38, 'base': 'Body Armour', 'name': 'Wyrmscale Doublet'},
			{'drop': 42, 'base': 'Body Armour', 'name': 'Hussar Brigandine'},
			{'drop': 46, 'base': 'Body Armour', 'name': 'Full Wyrmscale'},
			{'drop': 50, 'base': 'Body Armour', 'name': "Commander's Brigandine"},
			{'drop': 54, 'base': 'Body Armour', 'name': 'Battle Lamellar'},
			{'drop': 57, 'base': 'Body Armour', 'name': 'Dragonscale Doublet'},
			{'drop': 60, 'base': 'Body Armour', 'name': 'Desert Brigandine'},
			{'drop': 63, 'base': 'Body Armour', 'name': 'Full Dragonscale'},
			{'drop': 66, 'base': 'Body Armour', 'name': "General's Brigandine"},
			{'drop': 69, 'base': 'Body Armour', 'name': 'Triumphant Lamellar'},
		],
		"Armour|Body Armour|Dex|Int|Str": [
			{'drop': 72, 'base': 'Body Armour', 'name': 'Sacrificial Garb'},
		],
		"Armour|Boots|Str": [
			{'drop': 1, 'base': 'Boots', 'name': 'Iron Greaves'},
			{'drop': 9, 'base': 'Boots', 'name': 'Steel Greaves'},
			{'drop': 23, 'base': 'Boots', 'name': 'Plated Greaves'},
			{'drop': 33, 'base': 'Boots', 'name': 'Reinforced Greaves'},
			{'drop': 37, 'base': 'Boots', 'name': 'Antique Greaves'},
			{'drop': 46, 'base': 'Boots', 'name': 'Ancient Greaves'},
			{'drop': 54, 'base': 'Boots', 'name': 'Goliath Greaves'},
			{'drop': 62, 'base': 'Boots', 'name': 'Vaal Greaves'},
			{'drop': 68, 'base': 'Boots', 'name': 'Titan Greaves'},
		],
		"Armour|Boots|Int": [
			{'drop': 3, 'base': 'Boots', 'name': 'Wool Shoes'},
			{'drop': 9, 'base': 'Boots', 'name': 'Velvet Slippers'},
			{'drop': 22, 'base': 'Boots', 'name': 'Silk Slippers'},
			{'drop': 32, 'base': 'Boots', 'name': 'Scholar Boots'},
			{'drop': 38, 'base': 'Boots', 'name': 'Satin Slippers'},
			{'drop': 44, 'base': 'Boots', 'name': 'Samite Slippers'},
			{'drop': 53, 'base': 'Boots', 'name': 'Conjurer Boots'},
			{'drop': 61, 'base': 'Boots', 'name': 'Arcanist Slippers'},
			{'drop': 67, 'base': 'Boots', 'name': 'Sorcerer Boots'},
		],
		"Armour|Boots|Dex": [
			{'drop': 3, 'base': 'Boots', 'name': 'Rawhide Boots'},
			{'drop': 12, 'base': 'Boots', 'name': 'Goathide Boots'},
			{'drop': 22, 'base': 'Boots', 'name': 'Deerskin Boots'},
			{'drop': 34, 'base': 'Boots', 'name': 'Nubuck Boots'},
			{'drop': 39, 'base': 'Boots', 'name': 'Eelskin Boots'},
			{'drop': 44, 'base': 'Boots', 'name': 'Sharkskin Boots'},
			{'drop': 55, 'base': 'Boots', 'name': 'Shagreen Boots'},
			{'drop': 62, 'base': 'Boots', 'name': 'Stealth Boots'},
			{'drop': 69, 'base': 'Boots', 'name': 'Slink Boots'},
		],
		"Armour|Boots|Int|Str": [
			{'drop': 5, 'base': 'Boots', 'name': 'Chain Boots'},
			{'drop': 13, 'base': 'Boots', 'name': 'Ringmail Boots'},
			{'drop': 28, 'base': 'Boots', 'name': 'Mesh Boots'},
			{'drop': 36, 'base': 'Boots', 'name': 'Riveted Boots'},
			{'drop': 40, 'base': 'Boots', 'name': 'Zealot Boots'},
			{'drop': 49, 'base': 'Boots', 'name': 'Soldier Boots'},
			{'drop': 58, 'base': 'Boots', 'name': 'Legion Boots'},
			{'drop': 64, 'base': 'Boots', 'name': 'Crusader Boots'},
		],
		"Armour|Boots|Dex|Int": [
			{'drop': 6, 'base': 'Boots', 'name': 'Wrapped Boots'},
			{'drop': 16, 'base': 'Boots', 'name': 'Strapped Boots'},
			{'drop': 27, 'base': 'Boots', 'name': 'Clasped Boots'},
			{'drop': 34, 'base': 'Boots', 'name': 'Shackled Boots'},
			{'drop': 41, 'base': 'Boots', 'name': 'Trapper Boots'},
			{'drop': 47, 'base': 'Boots', 'name': 'Ambush Boots'},
			{'drop': 55, 'base': 'Boots', 'name': 'Carnal Boots'},
			{'drop': 63, 'base': 'Boots', 'name': "Assassin's Boots"},
			{'drop': 69, 'base': 'Boots', 'name': 'Murder Boots'},
		],
		"Armour|Boots|Dex|Str": [
			{'drop': 6, 'base': 'Boots', 'name': 'Leatherscale Boots'},
			{'drop': 18, 'base': 'Boots', 'name': 'Ironscale Boots'},
			{'drop': 30, 'base': 'Boots', 'name': 'Bronzescale Boots'},
			{'drop': 36, 'base': 'Boots', 'name': 'Steelscale Boots'},
			{'drop': 42, 'base': 'Boots', 'name': 'Serpentscale Boots'},
			{'drop': 51, 'base': 'Boots', 'name': 'Wyrmscale Boots'},
			{'drop': 59, 'base': 'Boots', 'name': 'Hydrascale Boots'},
			{'drop': 65, 'base': 'Boots', 'name': 'Dragonscale Boots'},
		],
		"Armour|Boots|Dex|Int|Str": [
			{'drop': 70, 'base': 'Boots', 'name': 'Two-Toned Boots'},  # Fire And Lightning Damage Resistance (15 to 20) or Fire And Cold Damage Resistance (15 to 20) or Cold And Lightning Damage Resistance (15 to 20)
		],
		"Armour|Gloves|Str": [
			{'drop': 1, 'base': 'Gloves', 'name': 'Iron Gauntlets'},
			{'drop': 11, 'base': 'Gloves', 'name': 'Plated Gauntlets'},
			{'drop': 23, 'base': 'Gloves', 'name': 'Bronze Gauntlets'},
			{'drop': 35, 'base': 'Gloves', 'name': 'Steel Gauntlets'},
			{'drop': 39, 'base': 'Gloves', 'name': 'Antique Gauntlets'},
			{'drop': 47, 'base': 'Gloves', 'name': 'Ancient Gauntlets'},
			{'drop': 53, 'base': 'Gloves', 'name': 'Goliath Gauntlets'},
			{'drop': 63, 'base': 'Gloves', 'name': 'Vaal Gauntlets'},
			{'drop': 69, 'base': 'Gloves', 'name': 'Titan Gauntlets'},
			{'drop': 70, 'base': 'Gloves', 'name': 'Spiked Gloves'},  # Melee Damage +(16 to 20)
		],
		"Armour|Dex|Gloves": [
			{'drop': 3, 'base': 'Gloves', 'name': 'Rawhide Gloves'},
			{'drop': 9, 'base': 'Gloves', 'name': 'Goathide Gloves'},
			{'drop': 21, 'base': 'Gloves', 'name': 'Deerskin Gloves'},
			{'drop': 33, 'base': 'Gloves', 'name': 'Nubuck Gloves'},
			{'drop': 38, 'base': 'Gloves', 'name': 'Eelskin Gloves'},
			{'drop': 45, 'base': 'Gloves', 'name': 'Sharkskin Gloves'},
			{'drop': 54, 'base': 'Gloves', 'name': 'Shagreen Gloves'},
			{'drop': 62, 'base': 'Gloves', 'name': 'Stealth Gloves'},
			{'drop': 70, 'base': 'Gloves', 'name': 'Slink Gloves'},
			{'drop': 70, 'base': 'Gloves', 'name': 'Gripped Gloves'},  # Projectile Attack Damage +(14 to 18)
		],
		"Armour|Gloves|Int": [
			{'drop': 3, 'base': 'Gloves', 'name': 'Wool Gloves'},
			{'drop': 12, 'base': 'Gloves', 'name': 'Velvet Gloves'},
			{'drop': 25, 'base': 'Gloves', 'name': 'Silk Gloves'},
			{'drop': 36, 'base': 'Gloves', 'name': 'Embroidered Gloves'},
			{'drop': 41, 'base': 'Gloves', 'name': 'Satin Gloves'},
			{'drop': 47, 'base': 'Gloves', 'name': 'Samite Gloves'},
			{'drop': 55, 'base': 'Gloves', 'name': 'Conjurer Gloves'},
			{'drop': 60, 'base': 'Gloves', 'name': 'Arcanist Gloves'},
			{'drop': 69, 'base': 'Gloves', 'name': 'Sorcerer Gloves'},
			{'drop': 70, 'base': 'Gloves', 'name': 'Fingerless Silk Gloves'},  # Spell Damage +(12 to 16)
		],
		"Armour|Dex|Gloves|Str": [
			{'drop': 4, 'base': 'Gloves', 'name': 'Fishscale Gauntlets'},
			{'drop': 15, 'base': 'Gloves', 'name': 'Ironscale Gauntlets'},
			{'drop': 27, 'base': 'Gloves', 'name': 'Bronzescale Gauntlets'},
			{'drop': 36, 'base': 'Gloves', 'name': 'Steelscale Gauntlets'},
			{'drop': 43, 'base': 'Gloves', 'name': 'Serpentscale Gauntlets'},
			{'drop': 49, 'base': 'Gloves', 'name': 'Wyrmscale Gauntlets'},
			{'drop': 59, 'base': 'Gloves', 'name': 'Hydrascale Gauntlets'},
			{'drop': 67, 'base': 'Gloves', 'name': 'Dragonscale Gauntlets'},
		],
		"Armour|Dex|Gloves|Int": [
			{'drop': 5, 'base': 'Gloves', 'name': 'Wrapped Mitts'},
			{'drop': 16, 'base': 'Gloves', 'name': 'Strapped Mitts'},
			{'drop': 31, 'base': 'Gloves', 'name': 'Clasped Mitts'},
			{'drop': 36, 'base': 'Gloves', 'name': 'Trapper Mitts'},
			{'drop': 45, 'base': 'Gloves', 'name': 'Ambush Mitts'},
			{'drop': 50, 'base': 'Gloves', 'name': 'Carnal Mitts'},
			{'drop': 58, 'base': 'Gloves', 'name': "Assassin's Mitts"},
			{'drop': 67, 'base': 'Gloves', 'name': 'Murder Mitts'},
		],
		"Armour|Gloves|Int|Str": [
			{'drop': 7, 'base': 'Gloves', 'name': 'Chain Gloves'},
			{'drop': 19, 'base': 'Gloves', 'name': 'Ringmail Gloves'},
			{'drop': 32, 'base': 'Gloves', 'name': 'Mesh Gloves'},
			{'drop': 37, 'base': 'Gloves', 'name': 'Riveted Gloves'},
			{'drop': 43, 'base': 'Gloves', 'name': 'Zealot Gloves'},
			{'drop': 51, 'base': 'Gloves', 'name': 'Soldier Gloves'},
			{'drop': 57, 'base': 'Gloves', 'name': 'Legion Gloves'},
			{'drop': 66, 'base': 'Gloves', 'name': 'Crusader Gloves'},
		],
		"Armour|Helmet|Str": [
			{'drop': 1, 'base': 'Helmet', 'name': 'Iron Hat'},
			{'drop': 7, 'base': 'Helmet', 'name': 'Cone Helmet'},
			{'drop': 18, 'base': 'Helmet', 'name': 'Barbute Helmet'},
			{'drop': 26, 'base': 'Helmet', 'name': 'Close Helmet'},
			{'drop': 35, 'base': 'Helmet', 'name': 'Gladiator Helmet'},
			{'drop': 40, 'base': 'Helmet', 'name': 'Reaver Helmet'},
			{'drop': 48, 'base': 'Helmet', 'name': 'Siege Helmet'},
			{'drop': 55, 'base': 'Helmet', 'name': 'Samite Helmet'},
			{'drop': 60, 'base': 'Helmet', 'name': 'Ezomyte Burgonet'},
			{'drop': 65, 'base': 'Helmet', 'name': 'Royal Burgonet'},
			{'drop': 69, 'base': 'Helmet', 'name': 'Eternal Burgonet'},
		],
		"Armour|Dex|Helmet": [
			{'drop': 3, 'base': 'Helmet', 'name': 'Leather Cap'},
			{'drop': 10, 'base': 'Helmet', 'name': 'Tricorne'},
			{'drop': 20, 'base': 'Helmet', 'name': 'Leather Hood'},
			{'drop': 30, 'base': 'Helmet', 'name': 'Wolf Pelt'},
			{'drop': 41, 'base': 'Helmet', 'name': 'Hunter Hood'},
			{'drop': 47, 'base': 'Helmet', 'name': 'Noble Tricorne'},
			{'drop': 55, 'base': 'Helmet', 'name': 'Ursine Pelt'},
			{'drop': 60, 'base': 'Helmet', 'name': 'Silken Hood'},
			{'drop': 64, 'base': 'Helmet', 'name': 'Sinner Tricorne'},
			{'drop': 70, 'base': 'Helmet', 'name': 'Lion Pelt'},
		],
		"Armour|Helmet|Int": [
			{'drop': 3, 'base': 'Helmet', 'name': 'Vine Circlet'},
			{'drop': 8, 'base': 'Helmet', 'name': 'Iron Circlet'},
			{'drop': 17, 'base': 'Helmet', 'name': 'Torture Cage'},
			{'drop': 26, 'base': 'Helmet', 'name': 'Tribal Circlet'},
			{'drop': 34, 'base': 'Helmet', 'name': 'Bone Circlet'},
			{'drop': 39, 'base': 'Helmet', 'name': 'Lunaris Circlet'},
			{'drop': 48, 'base': 'Helmet', 'name': 'Steel Circlet'},
			{'drop': 54, 'base': 'Helmet', 'name': 'Necromancer Circlet'},
			{'drop': 59, 'base': 'Helmet', 'name': 'Solaris Circlet'},
			{'drop': 65, 'base': 'Helmet', 'name': 'Mind Cage'},
			{'drop': 69, 'base': 'Helmet', 'name': 'Hubris Circlet'},
		],
		"Armour|Dex|Helmet|Int": [
			{'drop': 4, 'base': 'Helmet', 'name': 'Scare Mask'},
			{'drop': 10, 'base': 'Helmet', 'name': 'Plague Mask'},
			{'drop': 17, 'base': 'Helmet', 'name': 'Iron Mask'},
			{'drop': 28, 'base': 'Helmet', 'name': 'Festival Mask'},
			{'drop': 35, 'base': 'Helmet', 'name': 'Golden Mask'},
			{'drop': 38, 'base': 'Helmet', 'name': 'Raven Mask'},
			{'drop': 45, 'base': 'Helmet', 'name': 'Callous Mask'},
			{'drop': 52, 'base': 'Helmet', 'name': 'Regicide Mask'},
			{'drop': 57, 'base': 'Helmet', 'name': 'Harlequin Mask'},
			{'drop': 62, 'base': 'Helmet', 'name': 'Vaal Mask'},
			{'drop': 67, 'base': 'Helmet', 'name': 'Deicide Mask'},
		],
		"Armour|Dex|Helmet|Str": [
			{'drop': 4, 'base': 'Helmet', 'name': 'Battered Helm'},
			{'drop': 13, 'base': 'Helmet', 'name': 'Sallet'},
			{'drop': 23, 'base': 'Helmet', 'name': 'Visored Sallet'},
			{'drop': 33, 'base': 'Helmet', 'name': 'Gilded Sallet'},
			{'drop': 36, 'base': 'Helmet', 'name': 'Secutor Helm'},
			{'drop': 43, 'base': 'Helmet', 'name': 'Fencer Helm'},
			{'drop': 51, 'base': 'Helmet', 'name': 'Lacquered Helmet'},
			{'drop': 58, 'base': 'Helmet', 'name': 'Fluted Bascinet'},
			{'drop': 63, 'base': 'Helmet', 'name': 'Pig-Faced Bascinet'},
			{'drop': 67, 'base': 'Helmet', 'name': 'Nightmare Bascinet'},
		],
		"Armour|Helmet|Int|Str": [
			{'drop': 5, 'base': 'Helmet', 'name': 'Rusted Coif'},
			{'drop': 12, 'base': 'Helmet', 'name': 'Soldier Helmet'},
			{'drop': 22, 'base': 'Helmet', 'name': 'Great Helmet'},
			{'drop': 31, 'base': 'Helmet', 'name': 'Crusader Helmet'},
			{'drop': 37, 'base': 'Helmet', 'name': 'Aventail Helmet'},
			{'drop': 44, 'base': 'Helmet', 'name': 'Zealot Helmet'},
			{'drop': 53, 'base': 'Helmet', 'name': 'Great Crown'},
			{'drop': 58, 'base': 'Helmet', 'name': 'Magistrate Crown'},
			{'drop': 63, 'base': 'Helmet', 'name': 'Prophet Crown'},
			{'drop': 68, 'base': 'Helmet', 'name': 'Praetor Crown'},
			{'drop': 73, 'base': 'Helmet', 'name': 'Bone Helmet'},  # Minion Damage increase (30 to 40)
		],
		"Armour|Shield|Str": [
			{'drop': 1, 'base': 'Shield', 'name': 'Splintered Tower Shield'},
			{'drop': 5, 'base': 'Shield', 'name': 'Corroded Tower Shield'},  # Base Maximum Life (10 to 20)
			{'drop': 11, 'base': 'Shield', 'name': 'Rawhide Tower Shield'},  # Base Maximum Life (10 to 20)
			{'drop': 17, 'base': 'Shield', 'name': 'Cedar Tower Shield'},  # Base Maximum Life (20 to 30)
			{'drop': 24, 'base': 'Shield', 'name': 'Copper Tower Shield'},  # Base Maximum Life (30 to 40)
			{'drop': 30, 'base': 'Shield', 'name': 'Reinforced Tower Shield'},  # Base Maximum Life (10 to 20)
			{'drop': 35, 'base': 'Shield', 'name': 'Painted Tower Shield'},  # Base Maximum Life (20 to 30)
			{'drop': 39, 'base': 'Shield', 'name': 'Buckskin Tower Shield'},  # Base Maximum Life (10 to 20)
			{'drop': 43, 'base': 'Shield', 'name': 'Mahogany Tower Shield'},  # Base Maximum Life (20 to 30)
			{'drop': 47, 'base': 'Shield', 'name': 'Bronze Tower Shield'},  # Base Maximum Life (30 to 40)
			{'drop': 51, 'base': 'Shield', 'name': 'Girded Tower Shield'},  # Base Maximum Life (10 to 20)
			{'drop': 55, 'base': 'Shield', 'name': 'Crested Tower Shield'},  # Base Maximum Life (20 to 30)
			{'drop': 58, 'base': 'Shield', 'name': 'Shagreen Tower Shield'},  # Base Maximum Life (10 to 20)
			{'drop': 61, 'base': 'Shield', 'name': 'Ebony Tower Shield'},  # Base Maximum Life (20 to 30)
			{'drop': 64, 'base': 'Shield', 'name': 'Ezomyte Tower Shield'},  # Base Maximum Life (30 to 40)
			{'drop': 67, 'base': 'Shield', 'name': 'Colossal Tower Shield'},  # Base Maximum Life (10 to 20)
			{'drop': 70, 'base': 'Shield', 'name': 'Pinnacle Tower Shield'},  # Base Maximum Life (20 to 30)
		],
		"Armour|Dex|Shield": [
			{'drop': 2, 'base': 'Shield', 'name': 'Goathide Buckler'},  # Base Movement Velocity +(3)
			{'drop': 8, 'base': 'Shield', 'name': 'Pine Buckler'},  # Base Movement Velocity +(3)
			{'drop': 16, 'base': 'Shield', 'name': 'Painted Buckler'},  # Base Movement Velocity +(6)
			{'drop': 23, 'base': 'Shield', 'name': 'Hammered Buckler'},  # Base Movement Velocity +(3)
			{'drop': 29, 'base': 'Shield', 'name': 'War Buckler'},  # Base Movement Velocity +(9)
			{'drop': 34, 'base': 'Shield', 'name': 'Gilded Buckler'},  # Base Movement Velocity +(6)
			{'drop': 38, 'base': 'Shield', 'name': 'Oak Buckler'},  # Base Movement Velocity +(3)
			{'drop': 42, 'base': 'Shield', 'name': 'Enameled Buckler'},  # Base Movement Velocity +(6)
			{'drop': 46, 'base': 'Shield', 'name': 'Corrugated Buckler'},  # Base Movement Velocity +(3)
			{'drop': 50, 'base': 'Shield', 'name': 'Battle Buckler'},  # Base Movement Velocity +(9)
			{'drop': 54, 'base': 'Shield', 'name': 'Golden Buckler'},  # Base Movement Velocity +(6)
			{'drop': 57, 'base': 'Shield', 'name': 'Ironwood Buckler'},  # Base Movement Velocity +(3)
			{'drop': 60, 'base': 'Shield', 'name': 'Lacquered Buckler'},  # Base Movement Velocity +(6)
			{'drop': 63, 'base': 'Shield', 'name': 'Vaal Buckler'},  # Base Movement Velocity +(3)
			{'drop': 66, 'base': 'Shield', 'name': 'Crusader Buckler'},  # Base Movement Velocity +(9)
			{'drop': 69, 'base': 'Shield', 'name': 'Imperial Buckler'},  # Base Movement Velocity +(6)
		],
		"Armour|Int|Shield": [
			{'drop': 3, 'base': 'Shield', 'name': 'Twig Spirit Shield'},  # Spell Damage +(10 to 15)
			{'drop': 9, 'base': 'Shield', 'name': 'Yew Spirit Shield'},  # Spell Damage +(5 to 10)
			{'drop': 15, 'base': 'Shield', 'name': 'Bone Spirit Shield'},  # Spell Damage +(15 to 20)
			{'drop': 23, 'base': 'Shield', 'name': 'Tarnished Spirit Shield'},  # Spell Damage +(5 to 10)
			{'drop': 28, 'base': 'Shield', 'name': 'Jingling Spirit Shield'},  # Spell Damage +(10 to 15)
			{'drop': 33, 'base': 'Shield', 'name': 'Brass Spirit Shield'},
			{'drop': 37, 'base': 'Shield', 'name': 'Walnut Spirit Shield'},  # Spell Damage +(5 to 10)
			{'drop': 41, 'base': 'Shield', 'name': 'Ivory Spirit Shield'},  # Spell Damage +(15 to 20)
			{'drop': 45, 'base': 'Shield', 'name': 'Ancient Spirit Shield'},  # Spell Damage +(5 to 10)
			{'drop': 49, 'base': 'Shield', 'name': 'Chiming Spirit Shield'},  # Spell Damage +(10 to 15)
			{'drop': 53, 'base': 'Shield', 'name': 'Thorium Spirit Shield'},
			{'drop': 56, 'base': 'Shield', 'name': 'Lacewood Spirit Shield'},  # Spell Damage +(5 to 10)
			{'drop': 59, 'base': 'Shield', 'name': 'Fossilised Spirit Shield'},  # Spell Damage +(15 to 20)
			{'drop': 62, 'base': 'Shield', 'name': 'Vaal Spirit Shield'},  # Spell Damage +(5 to 10)
			{'drop': 65, 'base': 'Shield', 'name': 'Harmonic Spirit Shield'},  # Spell Damage +(10 to 15)
			{'drop': 68, 'base': 'Shield', 'name': 'Titanium Spirit Shield'},
		],
		"Armour|Dex|Int|Shield": [
			{'drop': 5, 'base': 'Shield', 'name': 'Spiked Bundle'},  # Base Chance To Dodge (2)
			{'drop': 12, 'base': 'Shield', 'name': 'Driftwood Spiked Shield'},  # Base Chance To Dodge (2)
			{'drop': 20, 'base': 'Shield', 'name': 'Alloyed Spiked Shield'},  # Base Chance To Dodge Spells (2)
			{'drop': 27, 'base': 'Shield', 'name': 'Burnished Spiked Shield'},  # Base Chance To Dodge (4)
			{'drop': 33, 'base': 'Shield', 'name': 'Ornate Spiked Shield'},  # Base Chance To Dodge Spells (4)
			{'drop': 39, 'base': 'Shield', 'name': 'Redwood Spiked Shield'},  # Base Chance To Dodge (2)
			{'drop': 45, 'base': 'Shield', 'name': 'Compound Spiked Shield'},  # Base Chance To Dodge Spells (2)
			{'drop': 49, 'base': 'Shield', 'name': 'Polished Spiked Shield'},  # Base Chance To Dodge (4)
			{'drop': 54, 'base': 'Shield', 'name': 'Sovereign Spiked Shield'},  # Base Chance To Dodge Spells (4)
			{'drop': 58, 'base': 'Shield', 'name': 'Alder Spiked Shield'},  # Base Chance To Dodge (2)
			{'drop': 62, 'base': 'Shield', 'name': 'Ezomyte Spiked Shield'},  # Base Chance To Dodge Spells (2)
			{'drop': 66, 'base': 'Shield', 'name': 'Mirrored Spiked Shield'},  # Base Chance To Dodge (4)
			{'drop': 70, 'base': 'Shield', 'name': 'Supreme Spiked Shield'},  # Base Chance To Dodge Spells (4)
		],
		"Armour|Dex|Shield|Str": [
			{'drop': 5, 'base': 'Shield', 'name': 'Rotted Round Shield'},  # Block Recovery Increase (60)
			{'drop': 12, 'base': 'Shield', 'name': 'Fir Round Shield'},  # Block Recovery Increase (180)
			{'drop': 20, 'base': 'Shield', 'name': 'Studded Round Shield'},  # Block Recovery Increase (60)
			{'drop': 27, 'base': 'Shield', 'name': 'Scarlet Round Shield'},
			{'drop': 33, 'base': 'Shield', 'name': 'Splendid Round Shield'},  # Block Recovery Increase (120)
			{'drop': 39, 'base': 'Shield', 'name': 'Maple Round Shield'},  # Block Recovery Increase (180)
			{'drop': 45, 'base': 'Shield', 'name': 'Spiked Round Shield'},  # Block Recovery Increase (60)
			{'drop': 49, 'base': 'Shield', 'name': 'Crimson Round Shield'},
			{'drop': 54, 'base': 'Shield', 'name': 'Baroque Round Shield'},  # Block Recovery Increase (120)
			{'drop': 58, 'base': 'Shield', 'name': 'Teak Round Shield'},  # Block Recovery Increase (180)
			{'drop': 62, 'base': 'Shield', 'name': 'Spiny Round Shield'},  # Block Recovery Increase (60)
			{'drop': 66, 'base': 'Shield', 'name': 'Cardinal Round Shield'},
			{'drop': 70, 'base': 'Shield', 'name': 'Elegant Round Shield'},  # Block Recovery Increase (120)
		],
		"Armour|Int|Shield|Str": [
			{'drop': 7, 'base': 'Shield', 'name': 'Plank Kite Shield'},  # Resist all Elements (4)
			{'drop': 13, 'base': 'Shield', 'name': 'Linden Kite Shield'},  # Resist all Elements (4)
			{'drop': 20, 'base': 'Shield', 'name': 'Reinforced Kite Shield'},
			{'drop': 27, 'base': 'Shield', 'name': 'Layered Kite Shield'},  # Resist all Elements (8)
			{'drop': 34, 'base': 'Shield', 'name': 'Ceremonial Kite Shield'},  # Resist all Elements (12)
			{'drop': 40, 'base': 'Shield', 'name': 'Etched Kite Shield'},  # Resist all Elements (4)
			{'drop': 46, 'base': 'Shield', 'name': 'Steel Kite Shield'},
			{'drop': 50, 'base': 'Shield', 'name': 'Laminated Kite Shield'},  # Resist all Elements (8)
			{'drop': 55, 'base': 'Shield', 'name': 'Angelic Kite Shield'},  # Resist all Elements (12)
			{'drop': 59, 'base': 'Shield', 'name': 'Branded Kite Shield'},  # Resist all Elements (4)
			{'drop': 62, 'base': 'Shield', 'name': 'Champion Kite Shield'},
			{'drop': 65, 'base': 'Shield', 'name': 'Mosaic Kite Shield'},  # Resist all Elements (8)
			{'drop': 68, 'base': 'Shield', 'name': 'Archon Kite Shield'},  # Resist all Elements (12)
		],
	},
	"Accessory": {
		"Accessory|Amulet": [
			{'drop': 1, 'base': 'Amulet', 'name': 'Mandible Talisman'},  # Attack And Cast Speed +(6 to 10)
			{'drop': 1, 'base': 'Amulet', 'name': 'Hexclaw Talisman'},  # Critical Strike Chance +(40 to 50)
			{'drop': 1, 'base': 'Amulet', 'name': 'Primal Skull Talisman'},  # Life Regeneration Rate Per Minute (120)
			{'drop': 1, 'base': 'Amulet', 'name': 'Wereclaw Talisman'},  # Base Critical Strike Multiplier +(24 to 36)
			{'drop': 1, 'base': 'Amulet', 'name': 'Splitnewt Talisman'},  # Chance To Freeze Shock Ignite (4 to 6)
			{'drop': 1, 'base': 'Amulet', 'name': 'Clutching Talisman'},  # Global Defences +(15 to 25)
			{'drop': 1, 'base': 'Amulet', 'name': 'Avian Twins Talisman'},  # Fire Damage Taken (50) As Cold or Fire Damage Taken (50) As Lightning or Cold Damage Taken (50) As Fire or Cold Damage Taken (50) As Lightning or Lightning Damage Taken (50) As Cold or Lightning Damage Taken (50) As Fire
			{'drop': 1, 'base': 'Amulet', 'name': 'Fangjaw Talisman'},  # Maximum Life +(8 to 12)
			{'drop': 1, 'base': 'Amulet', 'name': 'Horned Talisman'},  # Projectile Base Number Of Targets To Pierce (2)
			{'drop': 1, 'base': 'Amulet', 'name': 'Spinefuse Talisman'},  # Increased Item Quantity (6 to 10)
			{'drop': 1, 'base': 'Amulet', 'name': 'Three Rat Talisman'},  # All Attributes +(12 to 16)
			{'drop': 1, 'base': 'Amulet', 'name': 'Monkey Twins Talisman'},  # Base Skill Area Of Effect +(5 to 8)
			{'drop': 1, 'base': 'Amulet', 'name': 'Longtooth Talisman'},  # Base Additional Physical Damage Reduction (4 to 6)
			{'drop': 1, 'base': 'Amulet', 'name': 'Rotfeather Talisman'},  # All Damage (25 to 35)
			{'drop': 1, 'base': 'Amulet', 'name': 'Monkey Paw Talisman'},  # Add Power Charge On Kill (10) Chance or Add Frenzy Charge On Kill (10) Chance or Endurance Charge On Kill (10)
			{'drop': 1, 'base': 'Amulet', 'name': 'Three Hands Talisman'},  # Physical Damage (6 to 12) To Add As Random Element
			{'drop': 1, 'base': 'Amulet', 'name': 'Jet Amulet'},  # Resist all Elements (8 to 12)
			{'drop': 1, 'base': 'Amulet', 'name': 'Black Maw Talisman'},  # Local Has X Sockets (1)
			{'drop': 1, 'base': 'Amulet', 'name': 'Bonespire Talisman'},  # Maximum Mana +(20 to 30)
			{'drop': 1, 'base': 'Amulet', 'name': 'Ashscale Talisman'},  # Fire Damage +(20 to 30)
			{'drop': 1, 'base': 'Amulet', 'name': 'Lone Antler Talisman'},  # Lightning Damage +(20 to 30)
			{'drop': 1, 'base': 'Amulet', 'name': 'Deep One Talisman'},  # Cold Damage +(20 to 30)
			{'drop': 1, 'base': 'Amulet', 'name': 'Breakrib Talisman'},  # Physical Damage +(20 to 30)
			{'drop': 1, 'base': 'Amulet', 'name': 'Deadhand Talisman'},  # Chaos Damage +(19 to 31)
			{'drop': 1, 'base': 'Amulet', 'name': 'Undying Flesh Talisman'},
			{'drop': 1, 'base': 'Amulet', 'name': 'Rot Head Talisman'},  # Fishing Bite Sensitivity +(30 to 40)
			{'drop': 3, 'base': 'Amulet', 'name': 'Paua Amulet'},  # Mana Regeneration Rate +(20 to 30)
			{'drop': 3, 'base': 'Amulet', 'name': 'Coral Amulet'},  # Life Regeneration Rate per Minute (120 to 240)
			{'drop': 7, 'base': 'Amulet', 'name': 'Jade Amulet'},  # Additional Dexterity (20 to 30)
			{'drop': 7, 'base': 'Amulet', 'name': 'Amber Amulet'},  # Additional Strength (20 to 30)
			{'drop': 7, 'base': 'Amulet', 'name': 'Lapis Amulet'},  # Additional Intelligence (20 to 30)
			{'drop': 15, 'base': 'Amulet', 'name': 'Gold Amulet'},  # Base Item Found Rarity +(12 to 20)
			{'drop': 20, 'base': 'Amulet', 'name': 'Agate Amulet'},  # Additional Strength And Intelligence (16 to 24)
			{'drop': 20, 'base': 'Amulet', 'name': 'Turquoise Amulet'},  # Additional Dexterity And Intelligence (16 to 24)
			{'drop': 20, 'base': 'Amulet', 'name': 'Citrine Amulet'},  # Additional Strength And Dexterity (16 to 24)
			{'drop': 25, 'base': 'Amulet', 'name': 'Onyx Amulet'},  # Additional All Attributes (10 to 16)
			{'drop': 35, 'base': 'Amulet', 'name': 'Writhing Talisman'},  # Attack Damage +(20 to 30)
			{'drop': 35, 'base': 'Amulet', 'name': 'Chrysalis Talisman'},  # Spell Damage +(20 to 30)
			{'drop': 50, 'base': 'Amulet', 'name': 'Ruby Amulet'},  # Base Fire Damage Resistance (20 to 30)
			{'drop': 74, 'base': 'Amulet', 'name': 'Marble Amulet'},  # Life Regeneration Rate Per Minute (72 to 96)
			{'drop': 77, 'base': 'Amulet', 'name': 'Blue Pearl Amulet'},  # Mana Regeneration Rate +(48 to 56)
		],
		"Accessory|Belt": [
			{'drop': 1, 'base': 'Belt', 'name': 'Stygian Vise'},  # Local Has (1) Abyss Sockets
			{'drop': 2, 'base': 'Belt', 'name': 'Rustic Sash'},  # Physical Damage +(12 to 24)
			{'drop': 2, 'base': 'Belt', 'name': 'Chain Belt'},  # Base Maximum Energy Shield (9 to 20)
			{'drop': 10, 'base': 'Belt', 'name': 'Heavy Belt'},  # Additional Strength (25 to 35)
			{'drop': 10, 'base': 'Belt', 'name': 'Leather Belt'},  # Base Maximum Life (25 to 40)
			{'drop': 12, 'base': 'Belt', 'name': 'Golden Obi'},  # Base Item Found Rarity +(20 to 30)
			{'drop': 20, 'base': 'Belt', 'name': 'Cloth Belt'},  # Base Stun Recovery +(15 to 25)
			{'drop': 20, 'base': 'Belt', 'name': 'Studded Belt'},  # Base Stun Duration +(20 to 30)
			{'drop': 73, 'base': 'Belt', 'name': 'Vanguard Belt'},  # Base Physical Damage Reduction and Evasion Rating (260 to 320)
			{'drop': 73, 'base': 'Belt', 'name': 'Crystal Belt'},  # Base Maximum Energy Shield (60 to 80)
		],
		"Accessory|Ring": [
			{'drop': 1, 'base': 'Ring', 'name': 'Breach Ring'},  # Local Item Stats Are Doubled In Breach (1)
			{'drop': 2, 'base': 'Ring', 'name': 'Iron Ring'},  # Minimum Added Physical Damage (1), Maximum Added Physical Damage (4)
			{'drop': 4, 'base': 'Ring', 'name': 'Coral Ring'},  # Base Maximum Life (20 to 30)
			{'drop': 5, 'base': 'Ring', 'name': 'Paua Ring'},  # Base Maximum Mana (20 to 25)
			{'drop': 8, 'base': 'Ring', 'name': 'Sapphire Ring'},  # Base Cold Damage Resistance (20 to 30)
			{'drop': 12, 'base': 'Ring', 'name': 'Golden Hoop'},  # Additional All Attributes (8 to 12)
			{'drop': 12, 'base': 'Ring', 'name': 'Topaz Ring'},  # Base Lightning Damage Resistance (20 to 30)
			{'drop': 15, 'base': 'Ring', 'name': 'Jet Ring'},  # Global Defences +(5 to 10)
			{'drop': 16, 'base': 'Ring', 'name': 'Ruby Ring'},  # Base Fire Damage Resistance (20 to 30)
			{'drop': 20, 'base': 'Ring', 'name': 'Gold Ring'},  # Base Item Found Rarity +(6 to 15)
			{'drop': 20, 'base': 'Ring', 'name': 'Two-Stone Ring'},  # Fire And Lightning Damage Resistance (12 to 16) or Cold And Lightning Damage Resistance (12 to 16) or Fire And Cold Damage Resistance (12 to 16)
			{'drop': 25, 'base': 'Ring', 'name': 'Diamond Ring'},  # Critical Strike Chance +(20 to 30)
			{'drop': 25, 'base': 'Ring', 'name': 'Moonstone Ring'},  # Base Maximum Energy Shield (15 to 25)
			{'drop': 30, 'base': 'Ring', 'name': 'Prismatic Ring'},  # Resist all Elements (8 to 10)
			{'drop': 38, 'base': 'Ring', 'name': 'Amethyst Ring'},  # Base Chaos Damage Resistance (9 to 13)
			{'drop': 45, 'base': 'Ring', 'name': 'Unset Ring'},  # Local Has (1) Sockets
			{'drop': 78, 'base': 'Ring', 'name': 'Opal Ring'},  # Elemental Damage +(15 to 25)
			{'drop': 78, 'base': 'Ring', 'name': 'Steel Ring'},  # Minimum Added Physical Damage (3 to 4), Maximum Added Physical Damage (10 to 14)
		],
		"Other": [
			{'drop': 100, 'base': 'Jewel', 'name': 'Cobalt Jewel'},
			{'drop': 100, 'base': 'Jewel', 'name': 'Crimson Jewel'},
			{'drop': 100, 'base': 'Jewel', 'name': 'Viridian Jewel'},
		]
	},
}


# Helper function to find all item names that are substrings of other items
# That means these items need their bases and drop level defined
def findsubstrings():
	names = []
	for t in bases:
		for j in bases[t]:
			for i in bases[t][j]:
				names.append(i['name'])

	subnames = []
	l = len(names)
	for x in range(l - 1):
		for y in range(x + 1, l):
			if names[x] in names[y]:
				if names[x] not in subnames:
					subnames.append(names[x])
			if names[y] in names[x]:
				if names[y] not in subnames:
					subnames.append(names[y])
	return subnames


# given a list of flags, generate a list of rares to highlight while leveling, will only highlight current best items
# Will match all valid flags
# Valid flags are:
# Bow, Two, Ranged, Dex, Claw, One, Melee, Int, Dagger, Caster, One Hand Axe, Str, One Hand Mace,
# One Hand Sword, Sceptre, Staff, Thrusting One Hand Sword, Two Hand Axe, Two Hand Mace, Two Hand Sword,
# Wand, Body Armour, Armour, Boots, Gloves, Helmet, Shield, Amulet, Accessory, Belt, Ring, Weapon
# All is a special flag that chooses all categories
# overlevel is how many levels to highlight an item after a better base starts dropping
# maxlevel is the maximum item level to highlight levelling rares
# alwayshighlight is a list of bases to always highlight while leveling regardless of drop level (Up to maxlevel)
def genraresleveling(flags='All', overlevel=3, maxlevel=67, alwayshighlight=('Accessory',)):
	ret = {}
	substrings = findsubstrings()

	for category in bases:
		for vals in bases[category]:
			f = vals.split('|')
			l = len(bases[category][vals])
			if set(f).intersection(set(alwayshighlight)):
				for i in range(l):
					cur = bases[category][vals][i]
					if cur['drop'] <= maxlevel:
						ret[cur['name']] = {"base": cur['name'], "other": ["ItemLevel <= {}".format(maxlevel)], "type": "levelling rare normal"}
						if cur['name'] in substrings:
							ret[cur['name']]['class'] = cur['base']
							ret[cur['name']]['other'].append('DropLevel {}'.format(cur['drop']))
			elif flags == 'All' or set(f).intersection(set(flags)) or set(f).intersection(set(alwayshighlight)):
				for i in range(l-1):
					cur = bases[category][vals][i]
					if cur['drop'] <= maxlevel:
						cap = bases[category][vals][i+1]['drop'] + overlevel
						cap = cap if cap < maxlevel else maxlevel
						ret[cur['name']] = {"base": cur['name'], "other": ["ItemLevel <= {}".format(cap)], "type": "levelling rare normal"}
						if cur['name'] in substrings:
							ret[cur['name']]['class'] = cur['base']
							ret[cur['name']]['other'].append('DropLevel {}'.format(cur['drop']))
				cur = bases[category][vals][l-1]
				if cur['drop'] <= maxlevel:
					ret[cur['name']] = {"base": cur['name'], "other": ["ItemLevel <= {}".format(maxlevel)], "type": "levelling rare normal"}
					if cur['name'] in substrings:
						ret[cur['name']]['class'] = cur['base']
						ret[cur['name']]['other'].append('DropLevel {}'.format(cur['drop']))
	return ret


# given a list of flags, generate a list of items to highlight while leveling, will only highlight current best items
# Will match all valid flags
# Valid flags are:
# Bow, Two, Ranged, Dex, Claw, One, Melee, Int, Dagger, Caster, One Hand Axe, Str, One Hand Mace,
# One Hand Sword, Sceptre, Staff, Thrusting One Hand Sword, Two Hand Axe, Two Hand Mace, Two Hand Sword,
# Wand, Body Armour, Armour, Boots, Gloves, Helmet, Shield, Amulet, Accessory, Belt, Ring, Weapon
# All is a special flag that chooses all categories
# overlevel is how many levels to show an item after a better base starts dropping
# maxlevel is the maximum level to highlight levelling normal or magic items
# alwayshighlight is a list of bases to always highlight while leveling regardless of drop level (Up to maxlevel)
def gennonrareleveling(flags='All', overlevel=0, maxlevel=35, alwayshighlight=()):
	ret = {}
	substrings = findsubstrings()

	for category in bases:
		for vals in bases[category]:
			f = vals.split('|')
			l = len(bases[category][vals])
			if set(f).intersection(set(alwayshighlight)):
				for i in range(l):
					cur = bases[category][vals][i]
					if cur['drop'] <= maxlevel:
						ret[cur['name']] = {"base": cur['name'], "other": ["Rarity <= Normal", "ItemLevel <= {}".format(maxlevel)], "type": "leveling low"}
						if cur['name'] in substrings:
							ret[cur['name']]['class'] = cur['base']
							ret[cur['name']]['other'].append('DropLevel {}'.format(cur['drop']))
			elif flags == 'All' or set(f).intersection(set(flags)) or set(f).intersection(set(alwayshighlight)):
				for i in range(l-1):
					cur = bases[category][vals][i]
					if cur['drop'] <= maxlevel:
						cap = bases[category][vals][i+1]['drop'] + overlevel
						cap = cap if cap < maxlevel else maxlevel
						ret[cur['name']] = {"base": cur['name'], "other": ["Rarity <= Normal", "ItemLevel <= {}".format(cap)], "type": "leveling low"}
						if cur['name'] in substrings:
							ret[cur['name']]['class'] = cur['base']
							ret[cur['name']]['other'].append('DropLevel {}'.format(cur['drop']))
				cur = bases[category][vals][l-1]
				if cur['drop'] <= maxlevel:
					ret[cur['name']] = {"base": cur['name'], "other": ["Rarity <= Normal", "ItemLevel <= {}".format(maxlevel)], "type": "leveling low"}
					if cur['name'] in substrings:
						ret[cur['name']]['class'] = cur['base']
						ret[cur['name']]['other'].append('DropLevel {}'.format(cur['drop']))
	return ret


# generate a list of t1, highlighted, and "show anyways" rares
# alwaysshow shows any items that match the flag at the ilvl specificed or higher
# input parameters are a list of (value, number) pairs
#  value is the flag to match
#  number is the min ilvl to start showing
# These overrides take effect after any normal highlighting
def genrareshighlight():
	ret = {}
	substrings = findsubstrings()
	# Bases that are always shown when a certain ilvl threshold is reached
	alwaysshow = {'Helmet': 84, 'Gloves': 84, 'Boots': 84, 'Accessory': 68}

	#  Bases that are always highlighted, supercedes t1 and shown
	highlighted = {'Two-Toned Boots',
	               'Spiked Gloves', 'Gripped Gloves', 'Fingerless Silk Gloves',
	               'Bone Helmet',
	               'Jade Amulet', 'Amber Amulet', 'Lapis Amulet', 'Agate Amulet', 'Turquoise Amulet', 'Citrine Amulet', 'Onyx Amulet', 'Marble Amulet',
	               'Stygian Vise', 'Rustic Sash', 'Heavy Belt', 'Leather Belt',
	               'Coral Ring', 'Sapphire Ring', 'Topaz Ring', 'Ruby Ring', 'Two-Stone Ring', 'Diamond Ring', 'Prismatic Ring', 'Amethyst Ring', 'Unset Ring', 'Opal Ring', 'Steel Ring',
	               'Cobalt Jewel', 'Crimson Jewel', 'Viridian Jewel'}

	#  Best bases, supercedes shown
	t1 = {'Harbinger Bow',
	      'Eye Gouger', 'Imperial Claw', 'Gemini Claw',
	      'Demon Dagger', 'Imperial Skean', 'Platinum Kris',
	      'Void Sceptre', 'Sambar Sceptre',
	      'Harpy Rapier', 'Jewelled Foil',
	      'Astral Plate', 'Glorious Plate', "Assassin's Garb", "Saint's Hauberk", 'Saintly Chainmail', 'Triumphant Lamellar',
	      'Titan Greaves', 'Slink Boots', 'Dragonscale Boots',
	      'Titan Gauntlets', 'Slink Gloves', 'Dragonscale Gauntlets', 'Crusader Gloves',
	      'Eternal Burgonet', 'Lion Pelt', 'Nightmare Bascinet',
	      'Ezomyte Tower Shield', 'Archon Kite Shield', 'Mosaic Kite Shield',
	      'Paua Amulet', 'Coral Amulet', 'Gold Amulet', 'Blue Pearl Amulet',
	      'Chain Belt', 'Cloth Belt', 'Studded Belt', 'Vanguard Belt', 'Crystal Belt',
	      'Breach Ring', 'Iron Ring', 'Paua Ring', 'Moonstone Ring'}

	#  Bases that are always shown
	shown = {'Throat Stabber', 'Great White Claw', 'Twin Claw', 'Noble Claw', 'Gut Ripper',
	         'Golden Kris', 'Copper Kris', 'Fiend Dagger', 'Imp Dagger',
	         'Runic Hatchet',
	         'Behemoth Mace',
	         'Apex Rapier', 'Thorn Rapier',
	         'Fleshripper',
	         'Coronal Maul',
	         'Opal Wand', 'Tornado Wand', 'Prophecy Wand', 'Profane Wand',
	         'Vaal Regalia', 'Carnal Armour', "General's Brigandine",
	         'Sorcerer Boots', 'Crusader Boots', 'Murder Boots',
	         'Sorcerer Gloves', 'Murder Mitts',
	         'Royal Burgonet', 'Sinner Tricorne', 'Hubris Circlet', 'Deicide Mask', 'Pig-Faced Bascinet',
	         'Crusader Buckler', 'Harmonic Spirit Shield', 'Titanium Spirit Shield', 'Fossilised Spirit Shield', 'Angelic Kite Shield', 'Ceremonial Kite Shield', 'Ivory Spirit Shield', 'Bone Spirit Shield',
	         }

	askeys = alwaysshow.keys()
	for category in bases:
		for vals in bases[category]:
			f = vals.split('|')
			l = len(bases[category][vals])
			s = set(f).intersection(set(askeys))
			if s:
				ilvl = min([alwaysshow[x] for x in set(f).intersection(set(askeys))])

			for i in range(l):
				cur = bases[category][vals][i]
				if cur['name'] in highlighted:
					ret['1 {}'.format(cur['name'])] = {"base": cur['name'], "type": "rare highlight"}
					if cur['name'] in substrings:
						ret['1 {}'.format(cur['name'])]['class'] = cur['base']
						ret['1 {}'.format(cur['name'])]['other'] = ['DropLevel {}'.format(cur['drop'])]
				elif cur['name'] in t1:
					ret['2 {}'.format(cur['name'])] = {"base": cur['name'], "type": "rare high"}
					if cur['name'] in substrings:
						ret['2 {}'.format(cur['name'])]['class'] = cur['base']
						ret['2 {}'.format(cur['name'])]['other'] = ['DropLevel {}'.format(cur['drop'])]
				elif cur['name'] in shown:
					ret['3 {}'.format(cur['name'])] = {"base": cur['name'], "type": "rare normal"}
					if cur['name'] in substrings:
						ret['3 {}'.format(cur['name'])]['class'] = cur['base']
						ret['3 {}'.format(cur['name'])]['other'] = ['DropLevel {}'.format(cur['drop'])]
				elif s:
					ret['4 {}'.format(cur['name'])] = {"base": cur['name'], "other": ["ItemLevel >= {}".format(ilvl)], "type": "rare low"}
					if cur['name'] in substrings:
						ret['4 {}'.format(cur['name'])]['class'] = cur['base']
						ret['4 {}'.format(cur['name'])]['other'].append('DropLevel {}'.format(cur['drop']))
	return ret

