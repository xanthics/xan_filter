"""
* Copyright (c) 2016 Jeremy Parks. All rights reserved.
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

desc = "Currency catchall and special currency"

# Base type : settings pair
items = {
	"0 Mirror of Kalandra": {"base": "Mirror of Kalandra", "class": "Currency", "type": "currency extremely high"},
	"0 Exalted Orb": {"base": "Exalted Orb", "class": "Currency", "type": "currency extremely high"},
	"0 Albino Rhoa Feather": {"base": "Albino Rhoa Feather", "class": "Currency", "type": "currency extremely high"},
	"0 Stacked Deck": {"base": "Stacked Deck", "class": "Currency", "type": "currency normal"},
	"0 Blessing of Xoph": {"base": "Blessing of Xoph", "class": "Currency", "type": "currency normal"},
	"0 Blessing of Tul": {"base": "Blessing of Tul", "class": "Currency", "type": "currency normal"},
	"0 Blessing of Esh": {"base": "Blessing of Esh", "class": "Currency", "type": "currency normal"},
	"0 Blessing of Uul-Netol": {"base": "Blessing of Uul-Netol", "class": "Currency", "type": "currency normal"},
	"0 Blessing of Chayula": {"base": "Blessing of Chayula", "class": "Currency", "type": "currency normal"},
	"0 Blacksmith's Whetstone": {"base": "Blacksmith's Whetstone", "class": "Currency", "type": "currency very low"},
	"0 Armourer's Scrap": {"base": "Armourer's Scrap", "class": "Currency", "type": "currency very low"},
	"0 Scroll of Wisdom": {"base": "Scroll of Wisdom", "class": "Currency", "type": "currency very low"},
	"0 Portal Scroll": {"base": "Portal Scroll", "class": "Currency", "type": "currency very low"},
	"0 Alteration Shard": {"base": "Alteration Shard", "class": "Currency", "type": "currency very low"},
	"0 Apprentice Cartographer's Seal": {"base": "Apprentice Cartographer's Seal", "class": "Currency", "type": "currency normal"},
	"0 Journeyman Cartographer's Seal": {"base": "Journeyman Cartographer's Seal", "class": "Currency", "type": "currency normal"},
	"0 Master Cartographer's Seal": {"base": "Master Cartographer's Seal", "class": "Currency", "type": "currency normal"},
	"0 Unshaping Orb": {"base": "Unshaping Orb", "class": "Currency", "type": "currency normal"},
	"0 Prophecy": {"base": "Prophecy", "class": "Currency", "type": "currency high"},
	"7 Scroll Fragment": {"base": "Scroll Fragment", "class": "Currency", "type": "hide"},
	"9 Currency": {"class": "Currency", "type": "currency normal"}
}