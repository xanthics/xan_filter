#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher

desc = "challenge item"


# Base type : settings pair
items = {
	"1 Cluster Jewel": {"base": "Cluster Jewel", "class": "Jewel", "type": "show high"},

	"75 Harvest Wild Ursaling Seed": {"baseexact": "Wild Ursaling Seed", "type": "challenge show"},  # Tier 1
	"75 Harvest Wild Hellion Seed": {"baseexact": "Wild Hellion Seed", "type": "challenge show"},  # Tier 1
	"75 Harvest Wild Thornwolf Seed": {"baseexact": "Wild Thornwolf Seed", "type": "challenge show"},  # Tier 1
	"75 Harvest Wild Ape Seed": {"baseexact": "Wild Ape Seed", "type": "challenge show"},  # Tier 1
	"75 Harvest Wild Hatchling Seed": {"baseexact": "Wild Hatchling Seed", "type": "challenge show"},  # Tier 1

	"75 Harvest Vivid Arachnid Seed": {"baseexact": "Vivid Arachnid Seed", "type": "challenge show"},  # Tier 1
	"75 Harvest Vivid Weta Seed": {"baseexact": "Vivid Weta Seed", "type": "challenge show"},  # Tier 1
	"75 Harvest Vivid Leech Seed": {"baseexact": "Vivid Leech Seed", "type": "challenge show"},  # Tier 1
	"75 Harvest Vivid Scorpion Seed": {"baseexact": "Vivid Scorpion Seed", "type": "challenge show"},  # Tier 1
	"75 Harvest Vivid Thornweaver Seed": {"baseexact": "Vivid Thornweaver Seed", "type": "challenge show"},  # Tier 1

	"75 Harvest Primal Rhoa Seed": {"baseexact": "Primal Rhoa Seed", "type": "challenge show"},  # Tier 1
	"75 Harvest Primal Dustspitter Seed": {"baseexact": "Primal Dustspitter Seed", "type": "challenge show"},  # Tier 1
	"75 Harvest Primal Feasting Horror Seed": {"baseexact": "Primal Feasting Horror Seed", "type": "challenge show"},  # Tier 1
	"75 Harvest Primal Maw Seed": {"baseexact": "Primal Maw Seed", "type": "challenge show"},  # Tier 1
	"75 Harvest Primal Cleaveling Seed": {"baseexact": "Primal Cleaveling Seed", "type": "challenge show"},  # Tier 1

	"75 Harvest Wild Bristlebeast Grain": {"baseexact": "Wild Bristlebeast Grain", "type": "challenge normal"},  # Tier 2
	"75 Harvest Wild Snap Hound Grain": {"baseexact": "Wild Snap Hound Grain", "type": "challenge normal"},  # Tier 2
	"75 Harvest Wild Homunculus Grain": {"baseexact": "Wild Homunculus Grain", "type": "challenge normal"},  # Tier 2
	"75 Harvest Wild Chieftain Grain": {"baseexact": "Wild Chieftain Grain", "type": "challenge high"},  # Tier 2
	"75 Harvest Wild Spikeback Grain": {"baseexact": "Wild Spikeback Grain", "type": "challenge high"},  # Tier 2

	"75 Harvest Vivid Razorleg Grain": {"baseexact": "Vivid Razorleg Grain", "type": "challenge normal"},  # Tier 2
	"75 Harvest Vivid Sapsucker Grain": {"baseexact": "Vivid Sapsucker Grain", "type": "challenge normal"},  # Tier 2
	"75 Harvest Vivid Parasite Grain": {"baseexact": "Vivid Parasite Grain", "type": "challenge normal"},  # Tier 2
	"75 Harvest Vivid Striketail Grain": {"baseexact": "Vivid Striketail Grain", "type": "challenge normal"},  # Tier 2
	"75 Harvest Vivid Nestback Grain": {"baseexact": "Vivid Nestback Grain", "type": "challenge high"},  # Tier 2

	"75 Harvest Primal Rhex Grain": {"baseexact": "Primal Rhex Grain", "type": "challenge normal"},  # Tier 2
	"75 Harvest Primal Dustcrab Grain": {"baseexact": "Primal Dustcrab Grain", "type": "challenge normal"},  # Tier 2
	"75 Harvest Primal Viper Grain": {"baseexact": "Primal Viper Grain", "type": "challenge normal"},  # Tier 2
	"75 Harvest Primal Chimeral Grain": {"baseexact": "Primal Chimeral Grain", "type": "challenge normal"},  # Tier 2
	"75 Harvest Primal Scrabbler Grain": {"baseexact": "Primal Scrabbler Grain", "type": "challenge normal"},  # Tier 2

	"75 Harvest Wild Bristle Matron Bulb": {"baseexact": "Wild Bristle Matron Bulb", "type": "challenge high"},  # Tier 3
	"75 Harvest Wild Hellion Alpha Bulb": {"baseexact": "Wild Hellion Alpha Bulb", "type": "challenge high"},  # Tier 3
	"75 Harvest Wild Thornmaw Bulb": {"baseexact": "Wild Thornmaw Bulb", "type": "challenge high"},  # Tier 3
	"75 Harvest Wild Brambleback Bulb": {"baseexact": "Wild Brambleback Bulb", "type": "challenge high"},  # Tier 3
	"75 Harvest Wild Infestation Queen Bulb": {"baseexact": "Wild Infestation Queen Bulb", "type": "challenge very high"},  # Tier 3

	"75 Harvest Vivid Whipleg Bulb": {"baseexact": "Vivid Whipleg Bulb", "type": "challenge high"},  # Tier 3
	"75 Harvest Vivid Watcher Bulb": {"baseexact": "Vivid Watcher Bulb", "type": "challenge high"},  # Tier 3
	"75 Harvest Vivid Vulture Bulb": {"baseexact": "Vivid Vulture Bulb", "type": "challenge high"},  # Tier 3
	"75 Harvest Vivid Abberarach Bulb": {"baseexact": "Vivid Abberarach Bulb", "type": "challenge very high"},  # Tier 3
	"75 Harvest Vivid Devourer Bulb": {"baseexact": "Vivid Devourer Bulb", "type": "challenge high"},  # Tier 3

	"75 Harvest Primal Rhex Matriarch Bulb": {"baseexact": "Primal Rhex Matriarch Bulb", "type": "challenge high"},  # Tier 3
	"75 Harvest Primal Crushclaw Bulb": {"baseexact": "Primal Crushclaw Bulb", "type": "challenge high"},  # Tier 3
	"75 Harvest Primal Blisterlord Bulb": {"baseexact": "Primal Blisterlord Bulb", "type": "challenge very high"},  # Tier 3
	"75 Harvest Primal Cystcaller Bulb": {"baseexact": "Primal Cystcaller Bulb", "type": "challenge high"},  # Tier 3
	"75 Harvest Primal Reborn Bulb": {"baseexact": "Primal Reborn Bulb", "type": "challenge very high"},  # Tier 3

	"75 Harvest Wild Thornfruit": {"baseexact": "Wild Thornfruit", "type": "challenge very high"},  # Tier 4
	"75 Harvest Vivid Scalefruit": {"baseexact": "Vivid Scalefruit", "type": "challenge very high"},  # Tier 4
	"75 Harvest Primal Blisterfruit": {"baseexact": "Primal Blisterfruit", "type": "challenge very high"},  # Tier 4

	"75 Harvest Fortune Bud": {"baseexact": "Fortune Bud", "type": "challenge normal"},
	"75 Harvest Fortune Flower": {"baseexact": "Fortune Flower", "type": "challenge normal"},
	"75 Harvest Fortune Blossom": {"baseexact": "Fortune Blossom", "type": "challenge normal"},
	"75 Harvest Lifeforce Bud": {"baseexact": "Lifeforce Bud", "type": "challenge normal"},
	"75 Harvest Lifeforce Flower": {"baseexact": "Lifeforce Flower", "type": "challenge normal"},
	"75 Harvest Lifeforce Blossom": {"baseexact": "Lifeforce Blossom", "type": "challenge normal"},
	"75 Harvest Horticrafting Bud": {"baseexact": "Horticrafting Bud", "type": "challenge normal"},
	"75 Harvest Horticrafting Flower": {"baseexact": "Horticrafting Flower", "type": "challenge normal"},
	"75 Harvest Horticrafting Blossom": {"baseexact": "Horticrafting Blossom", "type": "challenge normal"},

	"76 Harvest Seed": {"class": "Harvest Seed", "type": "challenge normal"},
	"76 Harvest Seed Enhancer": {"class": "Seed Enhancer", "type": "challenge normal"},
}
