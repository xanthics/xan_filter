#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 12/28/2016(m/d/y) 05:35:44 UTC from "Breach" data
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
	"0 alch: {"base": "alch", "class": "Currency", "type": "currency normal"},
	"0 alt: {"base": "alt", "class": "Currency", "type": "currency low"},
	"0 apprenticecartosextant: {"base": "apprenticecartosextant", "class": "Currency", "type": "currency high"},
	"0 aug: {"base": "aug", "class": "Currency", "type": "currency low"},
	"0 bauble: {"base": "bauble", "class": "Currency", "type": "currency normal"},
	"0 blessed: {"base": "blessed", "class": "Currency", "type": "currency normal"},
	"0 chance: {"base": "chance", "class": "Currency", "type": "currency normal"},
	"0 chaos: {"base": "chaos", "class": "Currency", "type": "currency high"},
	"0 chisel: {"base": "chisel", "class": "Currency", "type": "currency normal"},
	"0 chrom: {"base": "chrom", "class": "Currency", "type": "currency low"},
	"0 divine: {"base": "divine", "class": "Currency", "type": "currency very high"},
	"0 fuse: {"base": "fuse", "class": "Currency", "type": "currency normal"},
	"0 gcp: {"base": "gcp", "class": "Currency", "type": "currency high"},
	"0 jew: {"base": "jew", "class": "Currency", "type": "currency low"},
	"0 journeycartosextant: {"base": "journeycartosextant", "class": "Currency", "type": "currency high"},
	"0 mastercartosextant: {"base": "mastercartosextant", "class": "Currency", "type": "currency very high"},
	"0 perandus: {"base": "perandus", "class": "Currency", "type": "currency low"},
	"0 regal: {"base": "regal", "class": "Currency", "type": "currency high"},
	"0 regret: {"base": "regret", "class": "Currency", "type": "currency high"},
	"0 scour: {"base": "scour", "class": "Currency", "type": "currency normal"},
	"0 silver: {"base": "silver", "class": "Currency", "type": "currency normal"},
	"0 transmute: {"base": "transmute", "class": "Currency", "type": "currency low"},
	"0 vaal: {"base": "vaal", "class": "Currency", "type": "currency high"},
}
