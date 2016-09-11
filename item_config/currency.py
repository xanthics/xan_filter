"""
* Copyright (c) 2015 Jeremy Parks. All rights reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a
* copy of this software and associated documentation files (the "Software"),
* to deal in the Software without restriction, including without limitation
* the rights to use, copy, modify, merge, publish, distribute, sublicense,
* and/or sell copies of the Software, and to permit persons to whom the
* Software is furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
* DEALINGS IN THE SOFTWARE.

Author: Jeremy Parks
Purpose: Create an item filter based on config files
Note: Requires Python 3.4.x
"""

desc = "Currency"

# Base type : settings pair
items = {
	"0 Mirror of Kalandra": {"base": "Mirror of Kalandra", "class": "Currency", "type": "currency very high"},
	"0 Exalted Orb": {"base": "Exalted Orb", "class": "Currency", "type": "currency very high"},
	"0 Divine Orb": {"base": "Divine Orb", "class": "Currency", "type": "currency very high"},
	"0 Albino Rhoa Feather": {"base": "Albino Rhoa Feather", "class": "Currency", "type": "currency very high"},
	"0 Orb of Regret": {"base": "Orb of Regret", "class": "Currency", "type": "currency high"},
	"0 Gemcutter's Prism": {"base": "Gemcutter's Prism", "class": "Currency", "type": "currency high"},
	"0 Chaos Orb": {"base": "Chaos Orb", "class": "Currency", "type": "currency high"},
	"0 Regal Orb": {"base": "Regal Orb", "class": "Currency", "type": "currency high"},
	"0 Stacked Deck": {"base": "Stacked Deck", "class": "Currency", "type": "currency high"},
	"0 Orb of Fusing": {"base": "Orb of Fusing", "class": "Currency", "type": "currency normal"},
	"0 Blessed Orb": {"base": "Blessed Orb", "class": "Currency", "type": "currency high"},
	"0 Orb of Scouring": {"base": "Orb of Scouring", "class": "Currency", "type": "currency normal"},
	"0 Orb of Alchemy": {"base": "Orb of Alchemy", "class": "Currency", "type": "currency normal"},
	"0 Vaal Orb": {"base": "Vaal Orb", "class": "Currency", "type": "currency high"},
	"0 Cartographer's Chisel": {"base": "Cartographer's Chisel", "class": "Currency", "type": "currency normal"},
	"0 Glassblower's Bauble": {"base": "Glassblower's Bauble", "class": "Currency", "type": "currency low"},
	"0 Orb of Chance": {"base": "Orb of Chance", "class": "Currency", "type": "currency normal"},
	"0 Jeweller's Orb": {"base": "Jeweller's Orb", "class": "Currency", "type": "currency normal"},
	"0 Chromatic Orb": {"base": "Chromatic Orb", "class": "Currency", "type": "currency low"},
	"0 Orb of Alteration": {"base": "Orb of Alteration", "class": "Currency", "type": "currency low"},
	"0 Orb of Augmentation": {"base": "Orb of Augmentation", "class": "Currency", "type": "currency low"},
	"0 Orb of Transmutation": {"base": "Orb of Transmutation", "class": "Currency", "type": "currency low"},
	"0 Blacksmith's Whetstone": {"base": "Blacksmith's Whetstone", "class": "Currency", "type": "currency low"},
	"0 Armourer's Scrap": {"base": "Armourer's Scrap", "class": "Currency", "type": "currency low"},
	"0 Scroll of Wisdom": {"base": "Scroll of Wisdom", "class": "Currency", "type": "currency low"},
	"0 Portal Scroll": {"base": "Portal Scroll", "class": "Currency", "type": "currency low"},
	"0 Alteration Shard": {"base": "Alteration Shard", "class": "Currency", "type": "currency low"},
	"0 Perandus Coin": {"base": "Perandus Coin", "class": "Currency", "type": "currency low"},
	"0 Silver Coin": {"base": "Silver Coin", "class": "Currency", "type": "currency normal"},
	"0 Apprentice Cartographer's Sextant": {"base": "Apprentice Cartographer's Sextant", "class": "Currency", "type": "currency normal"},
	"0 Journeyman Cartographer's Sextant": {"base": "Journeyman Cartographer's Sextant", "class": "Currency", "type": "currency normal"},
	"0 Master Cartographer's Sextant": {"base": "Master Cartographer's Sextant", "class": "Currency", "type": "currency normal"},
	"0 Apprentice Cartographer's Seal": {"base": "Apprentice Cartographer's Seal", "class": "Currency", "type": "currency normal"},
	"0 Journeyman Cartographer's Seal": {"base": "Journeyman Cartographer's Seal", "class": "Currency", "type": "currency normal"},
	"0 Master Cartographer's Seal": {"base": "Master Cartographer's Seal", "class": "Currency", "type": "currency normal"},
	"0 Unshaping Orb": {"base": "Unshaping Orb", "class": "Currency", "type": "currency normal"},
	"0 Remnant of Corruption": {"base": "Remnant of Corruption", "class": "Currency", "type": "challenge normal"},
	"0 Whispering Essence": {"base": "Whispering Essence", "class": "Currency", "type": "challenge low"},
	"0 Muttering Essence": {"base": "Muttering Essence", "class": "Currency", "type": "challenge low"},
	"0 Weeping Essence": {"base": "Weeping Essence", "class": "Currency", "type": "challenge low"},
	"0 Wailing Essence": {"base": "Wailing Essence", "class": "Currency", "type": "challenge low"},
	"0 Screaming Essence": {"base": "Screaming Essence", "class": "Currency", "type": "challenge normal"},
	"0 Shrieking Essence": {"base": "Shrieking Essence", "class": "Currency", "type": "challenge normal"},
	"0 Deafening Essence": {"base": "Deafening Essence", "class": "Currency", "type": "challenge normal"},
	"0 Essence of Delirium": {"base": "Essence of Delirium", "class": "Currency", "type": "challenge normal"},
	"0 Essence of Horror": {"base": "Essence of Horror", "class": "Currency", "type": "challenge normal"},
	"0 Essence of Hysteria": {"base": "Essence of Hysteria", "class": "Currency", "type": "challenge normal"},
	"0 Essence of Insanity": {"base of Insanity": "Essence", "class": "Currency", "type": "challenge normal"},
	"0 Prophecy": {"base": "Prophecy", "class": "Currency", "type": "currency high"},
	"7 Scroll Fragment": {"base": "Scroll Fragment", "class": "Currency", "type": "hide"},
	"9 Currency": {"class": "Currency", "type": "currency normal"}
}