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

desc = "challenge item"

# Base type : settings pair
items = {
	"0 The Fox": {"base": "The Fox", "class": "Divination Card", "type": "challenge high"},
	"0 Lucky Deck": {"base": "Lucky Deck", "class": "Divination Card", "type": "challenge high"},
	"0 Treasure Hunter": {"base": "Treasure Hunter", "class": "Divination Card", "type": "challenge high"},
	"0 Vinia's Token": {"base": "Vinia's Token", "class": "Divination Card", "type": "challenge high"},
	"0 The Stormcaller": {"base": "The Stormcaller", "class": "Divination Card", "type": "challenge high"},
	"0 The Penitent": {"base": "The Penitent", "class": "Divination Card", "type": "challenge high"},
	"0 The Trial": {"base": "The Trial", "class": "Divination Card", "type": "challenge high"},
	"0 Earth Drinker": {"base": "Earth Drinker", "class": "Divination Card", "type": "challenge high"},
	"0 The Surveyor": {"base": "The Surveyor", "class": "Divination Card", "type": "challenge high"},
	"0 Death": {"base": "Death", "class": "Divination Card", "type": "challenge high"},
	"0 Dialla's Subjugation": {"base": "Dialla's Subjugation", "class": "Divination Card", "type": "challenge high"},
	"0 The Enlightened": {"base": "The Enlightened", "class": "Divination Card", "type": "challenge high"},

	"0 Bone Helmet": {"base": "Bone Helmet", "other": ["Rarity Rare"], "type": "challenge normal"},
	"0 Two-Toned Boots": {"base": "Two-Toned Boots", "other": ["Rarity Rare"], "type": "challenge normal"},
	"0 Spiked Gloves": {"base": "Spiked Gloves", "other": ["Rarity Rare"], "type": "challenge normal"},
	"0 Gripped Gloves": {"base": "Gripped Gloves", "other": ["Rarity Rare"], "type": "challenge normal"},
	"0 Fingerless Silk Gloves": {"base": "Fingerless Silk Gloves", "other": ["Rarity Rare"], "type": "challenge normal"},
	"0 Steel Ring": {"base": "Steel Ring", "other": ["Rarity Rare"], "type": "challenge normal"},
	"0 Opal Ring": {"base": "Opal Ring", "other": ["Rarity Rare"], "type": "challenge normal"},
	"0 Blue Pearl Amulet": {"base": "Blue Pearl Amulet", "other": ["Rarity Rare"], "type": "challenge normal"},
	"0 Marble Amulet": {"base": "Marble Amulet", "other": ["Rarity Rare"], "type": "challenge normal"},
	"0 Vanguard Belt": {"base": "Vanguard Belt", "other": ["Rarity Rare"], "type": "challenge normal"},
	"0 Crystal Belt": {"base": "Crystal Belt", "other": ["Rarity Rare"], "type": "challenge normal"},

}