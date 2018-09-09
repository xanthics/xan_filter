#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 09/09/2018(m/d/y) 00:44:56 UTC from "Hardcore" data

desc = "Currency Autogen"

# Base type : settings pair
items = {
	"1 Aberrant Fossil": {"base": "Aberrant Fossil", "class": "Currency", "type": "currency normal"},
	"1 Aetheric Fossil": {"base": "Aetheric Fossil", "class": "Currency", "type": "currency high"},
	"1 Alchemy Shard": {"base": "Alchemy Shard", "class": "Currency", "type": "hide"},
	"09 Alchemy Shard": {"base": "Alchemy Shard", 'other': ['StackSize >= 3'], "class": "Currency", "type": "currency very low"},
	"08 Alchemy Shard": {"base": "Alchemy Shard", 'other': ['StackSize >= 5'], "class": "Currency", "type": "currency low"},
	"07 Alchemy Shard": {"base": "Alchemy Shard", 'other': ['StackSize >= 16'], "class": "Currency", "type": "currency normal"},
	"1 Alteration Shard": {"base": "Alteration Shard", "class": "Currency", "type": "hide"},
	"09 Alteration Shard": {"base": "Alteration Shard", 'other': ['StackSize >= 9'], "class": "Currency", "type": "currency very low"},
	"08 Alteration Shard": {"base": "Alteration Shard", 'other': ['StackSize >= 17'], "class": "Currency", "type": "currency low"},
	"1 Ancient Orb": {"base": "Ancient Orb", "class": "Currency", "type": "currency very high"},
	"09 Ancient Orb": {"base": "Ancient Orb", 'other': ['StackSize >= 11'], "class": "Currency", "type": "currency extremely high"},
	"1 Ancient Shard": {"base": "Ancient Shard", "class": "Currency", "type": "currency normal"},
	"09 Ancient Shard": {"base": "Ancient Shard", 'other': ['StackSize >= 3'], "class": "Currency", "type": "currency high"},
	"08 Ancient Shard": {"base": "Ancient Shard", 'other': ['StackSize >= 20'], "class": "Currency", "type": "currency very high"},
	"1 Annulment Shard": {"base": "Annulment Shard", "class": "Currency", "type": "currency normal"},
	"09 Annulment Shard": {"base": "Annulment Shard", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency high"},
	"08 Annulment Shard": {"base": "Annulment Shard", 'other': ['StackSize >= 14'], "class": "Currency", "type": "currency very high"},
	"1 Apprentice Cartographer's Sextant": {"base": "Apprentice Cartographer's Sextant", "class": "Currency", "type": "currency normal"},
	"09 Apprentice Cartographer's Sextant": {"base": "Apprentice Cartographer's Sextant", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency high"},
	"08 Apprentice Cartographer's Sextant": {"base": "Apprentice Cartographer's Sextant", 'other': ['StackSize >= 14'], "class": "Currency", "type": "currency very high"},
	"1 Armourer's Scrap": {"base": "Armourer's Scrap", "class": "Currency", "type": "hide"},
	"09 Armourer's Scrap": {"base": "Armourer's Scrap", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency very low"},
	"08 Armourer's Scrap": {"base": "Armourer's Scrap", 'other': ['StackSize >= 4'], "class": "Currency", "type": "currency low"},
	"07 Armourer's Scrap": {"base": "Armourer's Scrap", 'other': ['StackSize >= 13'], "class": "Currency", "type": "currency normal"},
	"1 Binding Shard": {"base": "Binding Shard", "class": "Currency", "type": "hide"},
	"09 Binding Shard": {"base": "Binding Shard", 'other': ['StackSize >= 3'], "class": "Currency", "type": "currency very low"},
	"08 Binding Shard": {"base": "Binding Shard", 'other': ['StackSize >= 6'], "class": "Currency", "type": "currency low"},
	"07 Binding Shard": {"base": "Binding Shard", 'other': ['StackSize >= 20'], "class": "Currency", "type": "currency normal"},
	"1 Blacksmith's Whetstone": {"base": "Blacksmith's Whetstone", "class": "Currency", "type": "currency very low"},
	"09 Blacksmith's Whetstone": {"base": "Blacksmith's Whetstone", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency low"},
	"08 Blacksmith's Whetstone": {"base": "Blacksmith's Whetstone", 'other': ['StackSize >= 8'], "class": "Currency", "type": "currency normal"},
	"1 Blessed Orb": {"base": "Blessed Orb", "class": "Currency", "type": "currency high"},
	"09 Blessed Orb": {"base": "Blessed Orb", 'other': ['StackSize >= 4'], "class": "Currency", "type": "currency very high"},
	"1 Blessing of Chayula": {"base": "Blessing of Chayula", "class": "Currency", "type": "currency extremely high"},
	"1 Blessing of Esh": {"base": "Blessing of Esh", "class": "Currency", "type": "currency very high"},
	"1 Blessing of Tul": {"base": "Blessing of Tul", "class": "Currency", "type": "currency high"},
	"1 Blessing of Uul-Netol": {"base": "Blessing of Uul-Netol", "class": "Currency", "type": "currency very high"},
	"1 Blessing of Xoph": {"base": "Blessing of Xoph", "class": "Currency", "type": "currency high"},
	"1 Bloodstained Fossil": {"base": "Bloodstained Fossil", "class": "Currency", "type": "currency very high"},
	"1 Bound Fossil": {"base": "Bound Fossil", "class": "Currency", "type": "currency high"},
	"1 Cartographer's Chisel": {"base": "Cartographer's Chisel", "class": "Currency", "type": "currency normal"},
	"09 Cartographer's Chisel": {"base": "Cartographer's Chisel", 'other': ['StackSize >= 3'], "class": "Currency", "type": "currency high"},
	"08 Cartographer's Chisel": {"base": "Cartographer's Chisel", 'other': ['StackSize >= 20'], "class": "Currency", "type": "currency very high"},
	"1 Chaos Orb": {"base": "Chaos Orb", "class": "Currency", "type": "currency high"},
	"09 Chaos Orb": {"base": "Chaos Orb", 'other': ['StackSize >= 7'], "class": "Currency", "type": "currency very high"},
	"1 Chaos Shard": {"base": "Chaos Shard", "class": "Currency", "type": "currency very low"},
	"09 Chaos Shard": {"base": "Chaos Shard", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency low"},
	"08 Chaos Shard": {"base": "Chaos Shard", 'other': ['StackSize >= 5'], "class": "Currency", "type": "currency normal"},
	"07 Chaos Shard": {"base": "Chaos Shard", 'other': ['StackSize >= 20'], "class": "Currency", "type": "currency high"},
	"1 Chromatic Orb": {"base": "Chromatic Orb", "class": "Currency", "type": "currency show"},
	"09 Chromatic Orb": {"base": "Chromatic Orb", 'other': ['StackSize >= 4'], "class": "Currency", "type": "currency normal"},
	"08 Chromatic Orb": {"base": "Chromatic Orb", 'other': ['StackSize >= 15'], "class": "Currency", "type": "currency high"},
	"1 Corroded Fossil": {"base": "Corroded Fossil", "class": "Currency", "type": "currency high"},
	"1 Dense Fossil": {"base": "Dense Fossil", "class": "Currency", "type": "currency normal"},
	"1 Divine Orb": {"base": "Divine Orb", "class": "Currency", "type": "currency very high"},
	"09 Divine Orb": {"base": "Divine Orb", 'other': ['StackSize >= 4'], "class": "Currency", "type": "currency extremely high"},
	"1 Enchanted Fossil": {"base": "Enchanted Fossil", "class": "Currency", "type": "currency high"},
	"1 Encrusted Fossil": {"base": "Encrusted Fossil", "class": "Currency", "type": "currency high"},
	"1 Engineer's Orb": {"base": "Engineer's Orb", "class": "Currency", "type": "currency normal"},
	"09 Engineer's Orb": {"base": "Engineer's Orb", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency high"},
	"08 Engineer's Orb": {"base": "Engineer's Orb", 'other': ['StackSize >= 14'], "class": "Currency", "type": "currency very high"},
	"1 Engineer's Shard": {"base": "Engineer's Shard", "class": "Currency", "type": "hide"},
	"09 Engineer's Shard": {"base": "Engineer's Shard", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency very low"},
	"08 Engineer's Shard": {"base": "Engineer's Shard", 'other': ['StackSize >= 3'], "class": "Currency", "type": "currency low"},
	"07 Engineer's Shard": {"base": "Engineer's Shard", 'other': ['StackSize >= 10'], "class": "Currency", "type": "currency normal"},
	"1 Eternal Orb": {"base": "Eternal Orb", "class": "Currency", "type": "currency extremely high"},
	"1 Exalted Orb": {"base": "Exalted Orb", "class": "Currency", "type": "currency very high"},
	"09 Exalted Orb": {"base": "Exalted Orb", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency extremely high"},
	"1 Exalted Shard": {"base": "Exalted Shard", "class": "Currency", "type": "currency high"},
	"09 Exalted Shard": {"base": "Exalted Shard", 'other': ['StackSize >= 3'], "class": "Currency", "type": "currency very high"},
	"1 Faceted Fossil": {"base": "Faceted Fossil", "class": "Currency", "type": "currency very high"},
	"1 Fractured Fossil ": {"base": "Fractured Fossil ", "class": "Currency", "type": "currency extremely high"},
	"1 Frigid Fossil": {"base": "Frigid Fossil", "class": "Currency", "type": "currency normal"},
	"1 Gemcutter's Prism": {"base": "Gemcutter's Prism", "class": "Currency", "type": "currency high"},
	"1 Gilded Fossil": {"base": "Gilded Fossil", "class": "Currency", "type": "currency very high"},
	"1 Glassblower's Bauble": {"base": "Glassblower's Bauble", "class": "Currency", "type": "currency normal"},
	"09 Glassblower's Bauble": {"base": "Glassblower's Bauble", 'other': ['StackSize >= 4'], "class": "Currency", "type": "currency high"},
	"1 Glyphic Fossil": {"base": "Glyphic Fossil", "class": "Currency", "type": "currency very high"},
	"1 Harbinger's Orb": {"base": "Harbinger's Orb", "class": "Currency", "type": "currency high"},
	"09 Harbinger's Orb": {"base": "Harbinger's Orb", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency very high"},
	"08 Harbinger's Orb": {"base": "Harbinger's Orb", 'other': ['StackSize >= 20'], "class": "Currency", "type": "currency extremely high"},
	"1 Harbinger's Shard": {"base": "Harbinger's Shard", "class": "Currency", "type": "currency low"},
	"09 Harbinger's Shard": {"base": "Harbinger's Shard", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency normal"},
	"08 Harbinger's Shard": {"base": "Harbinger's Shard", 'other': ['StackSize >= 5'], "class": "Currency", "type": "currency high"},
	"1 Hollow Fossil": {"base": "Hollow Fossil", "class": "Currency", "type": "currency very high"},
	"1 Horizon Shard": {"base": "Horizon Shard", "class": "Currency", "type": "currency very low"},
	"09 Horizon Shard": {"base": "Horizon Shard", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency low"},
	"08 Horizon Shard": {"base": "Horizon Shard", 'other': ['StackSize >= 8'], "class": "Currency", "type": "currency normal"},
	"1 Jagged Fossil": {"base": "Jagged Fossil", "class": "Currency", "type": "currency high"},
	"1 Jeweller's Orb": {"base": "Jeweller's Orb", "class": "Currency", "type": "currency show"},
	"09 Jeweller's Orb": {"base": "Jeweller's Orb", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency normal"},
	"08 Jeweller's Orb": {"base": "Jeweller's Orb", 'other': ['StackSize >= 8'], "class": "Currency", "type": "currency high"},
	"1 Journeyman Cartographer's Sextant": {"base": "Journeyman Cartographer's Sextant", "class": "Currency", "type": "currency very high"},
	"09 Journeyman Cartographer's Sextant": {"base": "Journeyman Cartographer's Sextant", 'other': ['StackSize >= 10'], "class": "Currency", "type": "currency extremely high"},
	"1 Lucent Fossil": {"base": "Lucent Fossil", "class": "Currency", "type": "currency high"},
	"1 Master Cartographer's Sextant": {"base": "Master Cartographer's Sextant", "class": "Currency", "type": "currency very high"},
	"09 Master Cartographer's Sextant": {"base": "Master Cartographer's Sextant", 'other': ['StackSize >= 8'], "class": "Currency", "type": "currency extremely high"},
	"1 Metallic Fossil": {"base": "Metallic Fossil", "class": "Currency", "type": "currency normal"},
	"1 Mirror Shard": {"base": "Mirror Shard", "class": "Currency", "type": "currency very high"},
	"09 Mirror Shard": {"base": "Mirror Shard", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency extremely high"},
	"1 Mirror of Kalandra": {"base": "Mirror of Kalandra", "class": "Currency", "type": "currency extremely high"},
	"1 Orb of Alchemy": {"base": "Orb of Alchemy", "class": "Currency", "type": "currency normal"},
	"09 Orb of Alchemy": {"base": "Orb of Alchemy", 'other': ['StackSize >= 4'], "class": "Currency", "type": "currency high"},
	"1 Orb of Alteration": {"base": "Orb of Alteration", "class": "Currency", "type": "currency show"},
	"09 Orb of Alteration": {"base": "Orb of Alteration", 'other': ['StackSize >= 4'], "class": "Currency", "type": "currency normal"},
	"08 Orb of Alteration": {"base": "Orb of Alteration", 'other': ['StackSize >= 13'], "class": "Currency", "type": "currency high"},
	"1 Orb of Annulment": {"base": "Orb of Annulment", "class": "Currency", "type": "currency high"},
	"09 Orb of Annulment": {"base": "Orb of Annulment", 'other': ['StackSize >= 3'], "class": "Currency", "type": "currency very high"},
	"1 Orb of Augmentation": {"base": "Orb of Augmentation", "class": "Currency", "type": "currency very low"},
	"09 Orb of Augmentation": {"base": "Orb of Augmentation", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency low"},
	"08 Orb of Augmentation": {"base": "Orb of Augmentation", 'other': ['StackSize >= 7'], "class": "Currency", "type": "currency normal"},
	"1 Orb of Binding": {"base": "Orb of Binding", "class": "Currency", "type": "currency normal"},
	"09 Orb of Binding": {"base": "Orb of Binding", 'other': ['StackSize >= 4'], "class": "Currency", "type": "currency high"},
	"1 Orb of Chance": {"base": "Orb of Chance", "class": "Currency", "type": "currency show"},
	"09 Orb of Chance": {"base": "Orb of Chance", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency normal"},
	"08 Orb of Chance": {"base": "Orb of Chance", 'other': ['StackSize >= 8'], "class": "Currency", "type": "currency high"},
	"1 Orb of Fusing": {"base": "Orb of Fusing", "class": "Currency", "type": "currency normal"},
	"09 Orb of Fusing": {"base": "Orb of Fusing", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency high"},
	"08 Orb of Fusing": {"base": "Orb of Fusing", 'other': ['StackSize >= 13'], "class": "Currency", "type": "currency very high"},
	"1 Orb of Horizons": {"base": "Orb of Horizons", "class": "Currency", "type": "currency normal"},
	"09 Orb of Horizons": {"base": "Orb of Horizons", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency high"},
	"08 Orb of Horizons": {"base": "Orb of Horizons", 'other': ['StackSize >= 11'], "class": "Currency", "type": "currency very high"},
	"1 Orb of Regret": {"base": "Orb of Regret", "class": "Currency", "type": "currency normal"},
	"09 Orb of Regret": {"base": "Orb of Regret", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency high"},
	"08 Orb of Regret": {"base": "Orb of Regret", 'other': ['StackSize >= 10'], "class": "Currency", "type": "currency very high"},
	"1 Orb of Scouring": {"base": "Orb of Scouring", "class": "Currency", "type": "currency normal"},
	"09 Orb of Scouring": {"base": "Orb of Scouring", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency high"},
	"08 Orb of Scouring": {"base": "Orb of Scouring", 'other': ['StackSize >= 9'], "class": "Currency", "type": "currency very high"},
	"1 Orb of Transmutation": {"base": "Orb of Transmutation", "class": "Currency", "type": "hide"},
	"09 Orb of Transmutation": {"base": "Orb of Transmutation", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency very low"},
	"08 Orb of Transmutation": {"base": "Orb of Transmutation", 'other': ['StackSize >= 3'], "class": "Currency", "type": "currency low"},
	"07 Orb of Transmutation": {"base": "Orb of Transmutation", 'other': ['StackSize >= 9'], "class": "Currency", "type": "currency normal"},
	"1 Perandus Coin": {"base": "Perandus Coin", "class": "Currency", "type": "currency show"},
	"09 Perandus Coin": {"base": "Perandus Coin", 'other': ['StackSize >= 12'], "class": "Currency", "type": "currency normal"},
	"1 Perfect Fossil": {"base": "Perfect Fossil", "class": "Currency", "type": "currency high"},
	"1 Portal Scroll": {"base": "Portal Scroll", "class": "Currency", "type": "hide"},
	"09 Portal Scroll": {"base": "Portal Scroll", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency very low"},
	"08 Portal Scroll": {"base": "Portal Scroll", 'other': ['StackSize >= 4'], "class": "Currency", "type": "currency low"},
	"07 Portal Scroll": {"base": "Portal Scroll", 'other': ['StackSize >= 13'], "class": "Currency", "type": "currency normal"},
	"1 Potent Alchemical Resonator": {"base": "Potent Alchemical Resonator", "class": "Currency", "type": "currency normal"},
	"1 Potent Chaotic Resonator": {"base": "Potent Chaotic Resonator", "class": "Currency", "type": "currency normal"},
	"1 Powerful Alchemical Resonator": {"base": "Powerful Alchemical Resonator", "class": "Currency", "type": "currency high"},
	"1 Powerful Chaotic Resonator": {"base": "Powerful Chaotic Resonator", "class": "Currency", "type": "currency high"},
	"1 Prime Alchemical Resonator": {"base": "Prime Alchemical Resonator", "class": "Currency", "type": "currency very high"},
	"1 Prime Chaotic Resonator": {"base": "Prime Chaotic Resonator", "class": "Currency", "type": "currency very high"},
	"1 Primitive Alchemical Resonator": {"base": "Primitive Alchemical Resonator", "class": "Currency", "type": "currency normal"},
	"1 Primitive Chaotic Resonator": {"base": "Primitive Chaotic Resonator", "class": "Currency", "type": "currency normal"},
	"1 Prismatic Fossil": {"base": "Prismatic Fossil", "class": "Currency", "type": "currency high"},
	"1 Pristine Fossil": {"base": "Pristine Fossil", "class": "Currency", "type": "currency high"},
	"1 Regal Orb": {"base": "Regal Orb", "class": "Currency", "type": "currency high"},
	"09 Regal Orb": {"base": "Regal Orb", 'other': ['StackSize >= 7'], "class": "Currency", "type": "currency very high"},
	"1 Regal Shard": {"base": "Regal Shard", "class": "Currency", "type": "currency very low"},
	"09 Regal Shard": {"base": "Regal Shard", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency low"},
	"08 Regal Shard": {"base": "Regal Shard", 'other': ['StackSize >= 5'], "class": "Currency", "type": "currency normal"},
	"07 Regal Shard": {"base": "Regal Shard", 'other': ['StackSize >= 20'], "class": "Currency", "type": "currency high"},
	"1 Sanctified Fossil": {"base": "Sanctified Fossil", "class": "Currency", "type": "currency very high"},
	"1 Scorched Fossil": {"base": "Scorched Fossil", "class": "Currency", "type": "currency high"},
	"1 Scroll Fragment": {"base": "Scroll Fragment", "class": "Currency", "type": "hide"},
	"1 Scroll of Wisdom": {"base": "Scroll of Wisdom", "class": "Currency", "type": "hide"},
	"09 Scroll of Wisdom": {"base": "Scroll of Wisdom", 'other': ['StackSize >= 4'], "class": "Currency", "type": "currency very low"},
	"08 Scroll of Wisdom": {"base": "Scroll of Wisdom", 'other': ['StackSize >= 7'], "class": "Currency", "type": "currency low"},
	"1 Serrated Fossil": {"base": "Serrated Fossil", "class": "Currency", "type": "currency high"},
	"1 Shuddering Fossil": {"base": "Shuddering Fossil", "class": "Currency", "type": "currency very high"},
	"1 Silver Coin": {"base": "Silver Coin", "class": "Currency", "type": "currency show"},
	"09 Silver Coin": {"base": "Silver Coin", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency normal"},
	"08 Silver Coin": {"base": "Silver Coin", 'other': ['StackSize >= 5'], "class": "Currency", "type": "currency high"},
	"1 Splinter of Chayula": {"base": "Splinter of Chayula", "class": "Currency", "type": "currency high"},
	"09 Splinter of Chayula": {"base": "Splinter of Chayula", 'other': ['StackSize >= 3'], "class": "Currency", "type": "currency very high"},
	"1 Splinter of Esh": {"base": "Splinter of Esh", "class": "Currency", "type": "currency normal"},
	"09 Splinter of Esh": {"base": "Splinter of Esh", 'other': ['StackSize >= 4'], "class": "Currency", "type": "currency high"},
	"1 Splinter of Tul": {"base": "Splinter of Tul", "class": "Currency", "type": "currency show"},
	"09 Splinter of Tul": {"base": "Splinter of Tul", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency normal"},
	"08 Splinter of Tul": {"base": "Splinter of Tul", 'other': ['StackSize >= 5'], "class": "Currency", "type": "currency high"},
	"1 Splinter of Uul-Netol": {"base": "Splinter of Uul-Netol", "class": "Currency", "type": "currency normal"},
	"09 Splinter of Uul-Netol": {"base": "Splinter of Uul-Netol", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency high"},
	"08 Splinter of Uul-Netol": {"base": "Splinter of Uul-Netol", 'other': ['StackSize >= 14'], "class": "Currency", "type": "currency very high"},
	"1 Splinter of Xoph": {"base": "Splinter of Xoph", "class": "Currency", "type": "currency normal"},
	"09 Splinter of Xoph": {"base": "Splinter of Xoph", 'other': ['StackSize >= 4'], "class": "Currency", "type": "currency high"},
	"1 Tangled Fossil": {"base": "Tangled Fossil", "class": "Currency", "type": "currency very high"},
	"1 Transmutation Shard": {"base": "Transmutation Shard", "class": "Currency", "type": "hide"},
	"1 Vaal Orb": {"base": "Vaal Orb", "class": "Currency", "type": "currency normal"},
	"09 Vaal Orb": {"base": "Vaal Orb", 'other': ['StackSize >= 2'], "class": "Currency", "type": "currency high"},
	"08 Vaal Orb": {"base": "Vaal Orb", 'other': ['StackSize >= 11'], "class": "Currency", "type": "currency very high"},
}
