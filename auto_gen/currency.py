#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 12/21/2016(m/d/y) 23:05:57 UTC from "Standard" data
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

desc = "Currency Autogen"

# Base type : settings pair
items = {
	"0 Orb of Alchemy": {"base": "Orb of Alchemy", "class": "Currency", "type": "currency normal"},
	"0 Orb of Alteration": {"base": "Orb of Alteration", "class": "Currency", "type": "currency low"},
	"0 Apprentice Cartographer's Sextant": {"base": "Apprentice Cartographer's Sextant", "class": "Currency", "type": "currency normal"},
	"0 Orb of Augmentation": {"base": "Orb of Augmentation", "class": "Currency", "type": "currency low"},
	"0 Glassblower's Bauble": {"base": "Glassblower's Bauble", "class": "Currency", "type": "currency low"},
	"0 Blessed Orb": {"base": "Blessed Orb", "class": "Currency", "type": "currency normal"},
	"0 Orb of Chance": {"base": "Orb of Chance", "class": "Currency", "type": "currency low"},
	"0 Chaos Orb": {"base": "Chaos Orb", "class": "Currency", "type": "currency high"},
	"0 Cartographer's Chisel": {"base": "Cartographer's Chisel", "class": "Currency", "type": "currency normal"},
	"0 Chromatic Orb": {"base": "Chromatic Orb", "class": "Currency", "type": "currency low"},
	"0 Divine Orb": {"base": "Divine Orb", "class": "Currency", "type": "currency very high"},
	"0 Orb of Fusing": {"base": "Orb of Fusing", "class": "Currency", "type": "currency normal"},
	"0 Gemcutter's Prism": {"base": "Gemcutter's Prism", "class": "Currency", "type": "currency high"},
	"0 Jeweller's Orb": {"base": "Jeweller's Orb", "class": "Currency", "type": "currency normal"},
	"0 Journeyman Cartographer's Sextant": {"base": "Journeyman Cartographer's Sextant", "class": "Currency", "type": "currency high"},
	"0 Master Cartographer's Sextant": {"base": "Master Cartographer's Sextant", "class": "Currency", "type": "currency very high"},
	"0 Perandus Coin": {"base": "Perandus Coin", "class": "Currency", "type": "currency low"},
	"0 Regal Orb": {"base": "Regal Orb", "class": "Currency", "type": "currency high"},
	"0 Orb of Regret": {"base": "Orb of Regret", "class": "Currency", "type": "currency high"},
	"0 Orb of Scouring": {"base": "Orb of Scouring", "class": "Currency", "type": "currency normal"},
	"0 Silver Coin": {"base": "Silver Coin", "class": "Currency", "type": "currency normal"},
	"0 Orb of Transmutation": {"base": "Orb of Transmutation", "class": "Currency", "type": "currency low"},
	"0 Vaal Orb": {"base": "Vaal Orb", "class": "Currency", "type": "currency high"},
}
