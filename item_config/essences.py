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

desc = "Essences"

# Base type : settings pair
items = {
	"0 Remnant of Corruption": {"base": "Remnant of Corruption", "class": "Currency", "type": "currency normal"},
	"0 Whispering Essence": {"base": "Whispering Essence", "class": "Currency", "type": "currency low"},
	"0 Muttering Essence": {"base": "Muttering Essence", "class": "Currency", "type": "currency low"},
	"0 Weeping Essence": {"base": "Weeping Essence", "class": "Currency", "type": "currency low"},
	"0 Wailing Essence": {"base": "Wailing Essence", "class": "Currency", "type": "currency low"},
	"0 Screaming Essence": {"base": "Screaming Essence", "class": "Currency", "type": "currency normal"},
	"0 Shrieking Essence": {"base": "Shrieking Essence", "class": "Currency", "type": "currency normal"},
	"0 Deafening Essence": {"base": "Deafening Essence", "class": "Currency", "type": "currency normal"},
	"0 Essence of Delirium": {"base": "Essence of Delirium", "class": "Currency", "type": "currency normal"},
	"0 Essence of Horror": {"base": "Essence of Horror", "class": "Currency", "type": "currency normal"},
	"0 Essence of Hysteria": {"base": "Essence of Hysteria", "class": "Currency", "type": "currency normal"},
	"0 Essence of Insanity": {"base": "Essence of Insanity", "class": "Currency", "type": "currency normal"},
	"0 Prophecy": {"base": "Prophecy", "class": "Currency", "type": "currency high"},
}