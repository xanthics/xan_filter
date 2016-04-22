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

desc = "Rare item for leveling or crafting"

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Simple Robe": {"base": "Simple Robe", "other": ["ItemLevel <= 8"], "type": "levelling rare normal"},
	"Silken Vest": {"base": "Silken Vest", "other": ["ItemLevel <= 16"], "type": "levelling rare normal"},
	"Scholar's Robe": {"base": "Scholar's Robe", "other": ["ItemLevel <= 23"], "type": "levelling rare normal"},
	"Silken Garb": {"base": "Silken Garb", "other": ["ItemLevel <= 30"], "type": "levelling rare normal"},
	"Mage's Vestment": {"base": "Mage's Vestment", "other": ["ItemLevel <= 33"], "type": "levelling rare normal"},
	"Silk Robe": {"base": "Silk Robe", "other": ["ItemLevel <= 37"], "type": "levelling rare normal"},
	"Cabalist Regalia": {"base": "Cabalist Regalia", "other": ["ItemLevel <= 40"], "type": "levelling rare normal"},
	"Sage's Robe": {"base": "Sage's Robe", "other": ["ItemLevel <= 42"], "type": "levelling rare normal"},
	"Silken Wrap": {"base": "Silken Wrap", "other": ["ItemLevel <= 46"], "type": "levelling rare normal"},
	"Conjurer's Vestment": {"base": "Conjurer's Vestment", "other": ["ItemLevel <= 50"], "type": "levelling rare normal"},
	"Spidersilk Robe": {"base": "Spidersilk Robe", "other": ["ItemLevel <= 54"], "type": "levelling rare normal"},
	"Destroyer Regalia": {"base": "Destroyer Regalia", "other": ["ItemLevel <= 58"], "type": "levelling rare normal"},
	"Savant's Robe": {"base": "Savant's Robe", "other": ["ItemLevel <= 61"], "type": "levelling rare normal"},
	"Necromancer Silks": {"base": "Necromancer Silks", "other": ["ItemLevel <= 64"], "type": "levelling rare normal"},
	"Occultist's Vestment": {"base": "Occultist's Vestment", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Widowsilk Robe": {"base": "Widowsilk Robe", "other": ["ItemLevel <= 70"], "type": "ignore"},
	"Vaal Regalia": {"base": "Vaal Regalia", "other": ["ItemLevel <= 73"], "type": "ignore"},
	"Wool Shoes": {"base": "Wool Shoes", "other": ["ItemLevel <= 8"], "type": "levelling rare normal"},
	"Velvet Slippers": {"base": "Velvet Slippers", "other": ["ItemLevel <= 14"], "type": "levelling rare normal"},
	"Silk Slippers": {"base": "Silk Slippers", "other": ["ItemLevel <= 27"], "type": "levelling rare normal"},
	"Scholar Boots": {"base": "Scholar Boots", "other": ["ItemLevel <= 37"], "type": "levelling rare normal"},
	"Satin Slippers": {"base": "Satin Slippers", "other": ["ItemLevel <= 43"], "type": "levelling rare normal"},
	"Samite Slippers": {"base": "Samite Slippers", "other": ["ItemLevel <= 49"], "type": "levelling rare normal"},
	"Conjurer Boots": {"base": "Conjurer Boots", "other": ["ItemLevel <= 58"], "type": "levelling rare normal"},
	"Arcanist Slippers": {"base": "Arcanist Slippers", "other": ["ItemLevel <= 66"], "type": "levelling rare normal"},
	"Sorcerer Boots": {"base": "Sorcerer Boots", "other": ["ItemLevel <= 72"], "type": "ignore"},
	"Wool Gloves": {"base": "Wool Gloves", "other": ["ItemLevel <= 8"], "type": "levelling rare normal"},
	"Velvet Gloves": {"base": "Velvet Gloves", "other": ["ItemLevel <= 17"], "type": "levelling rare normal"},
	"Silk Gloves": {"base": "Silk Gloves", "other": ["ItemLevel <= 30"], "type": "levelling rare normal"},
	"Embroidered Gloves": {"base": "Embroidered Gloves", "other": ["ItemLevel <= 41"], "type": "levelling rare normal"},
	"Satin Gloves": {"base": "Satin Gloves", "other": ["ItemLevel <= 46"], "type": "levelling rare normal"},
	"Samite Gloves": {"base": "Samite Gloves", "other": ["ItemLevel <= 52"], "type": "levelling rare normal"},
	"Conjurer Gloves": {"base": "Conjurer Gloves", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Arcanist Gloves": {"base": "Arcanist Gloves", "other": ["ItemLevel <= 65"], "type": "levelling rare normal"},
	"Sorcerer Gloves": {"base": "Sorcerer Gloves", "other": ["ItemLevel <= 74"], "type": "ignore"},
	"Vine Circlet": {"base": "Vine Circlet", "other": ["ItemLevel <= 8"], "type": "levelling rare normal"},
	"Iron Circlet": {"base": "Iron Circlet", "other": ["ItemLevel <= 13"], "type": "levelling rare normal"},
	"Torture Cage": {"base": "Torture Cage", "other": ["ItemLevel <= 22"], "type": "levelling rare normal"},
	"Tribal Circlet": {"base": "Tribal Circlet", "other": ["ItemLevel <= 31"], "type": "levelling rare normal"},
	"Bone Circlet": {"base": "Bone Circlet", "other": ["ItemLevel <= 39"], "type": "levelling rare normal"},
	"Lunaris Circlet": {"base": "Lunaris Circlet", "other": ["ItemLevel <= 44"], "type": "levelling rare normal"},
	"Steel Circlet": {"base": "Steel Circlet", "other": ["ItemLevel <= 53"], "type": "levelling rare normal"},
	"Necromancer Circlet": {"base": "Necromancer Circlet", "other": ["ItemLevel <= 59"], "type": "levelling rare normal"},
	"Solaris Circlet": {"base": "Solaris Circlet", "other": ["ItemLevel <= 64"], "type": "levelling rare normal"},
	"Mind Cage": {"base": "Mind Cage", "other": ["ItemLevel <= 70"], "type": "ignore"},
	"Hubris Circlet": {"base": "Hubris Circlet", "other": ["ItemLevel <= 74"], "type": "ignore"},
	"Twig Spirit Shield": {"base": "Twig Spirit Shield", "other": ["ItemLevel <= 8"], "type": "levelling rare normal"},
	"Yew Spirit Shield": {"base": "Yew Spirit Shield", "other": ["ItemLevel <= 14"], "type": "levelling rare normal"},
	"Bone Spirit Shield": {"base": "Bone Spirit Shield", "other": ["ItemLevel <= 20"], "type": "levelling rare normal"},
	"Tarnished Spirit Shield": {"base": "Tarnished Spirit Shield", "other": ["ItemLevel <= 28"], "type": "levelling rare normal"},
	"Jingling Spirit Shield": {"base": "Jingling Spirit Shield", "other": ["ItemLevel <= 33"], "type": "levelling rare normal"},
	"Brass Spirit Shield": {"base": "Brass Spirit Shield", "other": ["ItemLevel <= 38"], "type": "levelling rare normal"},
	"Walnut Spirit Shield": {"base": "Walnut Spirit Shield", "other": ["ItemLevel <= 42"], "type": "levelling rare normal"},
	"Ivory Spirit Shield": {"base": "Ivory Spirit Shield", "other": ["ItemLevel <= 46"], "type": "levelling rare normal"},
	"Ancient Spirit Shield": {"base": "Ancient Spirit Shield", "other": ["ItemLevel <= 50"], "type": "levelling rare normal"},
	"Chiming Spirit Shield": {"base": "Chiming Spirit Shield", "other": ["ItemLevel <= 54"], "type": "levelling rare normal"},
	"Thorium Spirit Shield": {"base": "Thorium Spirit Shield", "other": ["ItemLevel <= 58"], "type": "levelling rare normal"},
	"Lacewood Spirit Shield": {"base": "Lacewood Spirit Shield", "other": ["ItemLevel <= 61"], "type": "levelling rare normal"},
	"Fossilised Spirit Shield": {"base": "Fossilised Spirit Shield", "other": ["ItemLevel <= 64"], "type": "levelling rare normal"},
	"Vaal Spirit Shield": {"base": "Vaal Spirit Shield", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Harmonic Spirit Shield": {"base": "Harmonic Spirit Shield", "other": ["ItemLevel <= 70"], "type": "ignore"},
	"Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "other": ["ItemLevel <= 73"], "type": "ignore"}
}
