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

desc = "challenge item"

# Base type : settings pair
items = {
	"0 Splinter of Xoph": {"base": "Splinter of Xoph", "class": "Currency", "type": "chance"},
	"0 Splinter of Tul": {"base": "Splinter of Tul", "class": "Currency", "type": "chance"},
	"0 Splinter of Esh": {"base": "Splinter of Esh", "class": "Currency", "type": "chance"},
	"0 Splinter of Uul-Netol": {"base": "Splinter of Uul-Netol", "class": "Currency", "type": "chance"},
	"0 Splinter of Chayula": {"base": "Splinter of Chayula", "class": "Currency", "type": "chance"},
	"0 Blessing of Xoph": {"base": "Blessing of Xoph", "class": "Currency", "type": "challenge normal"},
	"0 Blessing of Tul": {"base": "Blessing of Tul", "class": "Currency", "type": "challenge normal"},
	"0 Blessing of Esh": {"base": "Blessing of Esh", "class": "Currency", "type": "challenge normal"},
	"0 Blessing of Uul-Netol": {"base": "Blessing of Uul-Netol", "class": "Currency", "type": "challenge normal"},
	"0 Blessing of Chayula": {"base": "Blessing of Chayula", "class": "Currency", "type": "challenge normal"},
	"0 Xoph's Breachstone": {"base": "Xoph's Breachstone", "class": "Map Fragments", "type": "challenge normal"},
	"0 Tul's Breachstone": {"base": "Tul's Breachstone", "class": "Map Fragments", "type": "challenge normal"},
	"0 Esh's Breachstone": {"base": "Esh's Breachstone", "class": "Map Fragments", "type": "challenge normal"},
	"0 Uul-Netol's Breachstone": {"base": "Uul-Netol's Breachstone", "class": "Map Fragments", "type": "challenge normal"},
	"0 Chayula's Breachstone": {"base": "Chayula's Breachstone", "class": "Map Fragments", "type": "challenge normal"},
}