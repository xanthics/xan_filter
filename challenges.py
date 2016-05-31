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
	"0 Desert Map": {"base": "Desert Map", "class": "Maps", "other": ["Rarity Rare"], "type": "challenge"},
	"0 Dunes Map": {"base": "Dunes Map", "class": "Maps", "other": ["Rarity Rare"], "type": "challenge"},
	"0 Cemetary Map": {"base": "Cemetary Map", "class": "Maps", "other": ["Rarity Rare"], "type": "challenge"},
	"0 Thicket Map": {"base": "Thicket Map", "class": "Maps", "other": ["Rarity Rare"], "type": "challenge"},
	"0 Mud Geyser Map": {"base": "Mud Geyser Map", "class": "Maps", "other": ["Rarity Rare"], "type": "challenge"},
	"0 Quarry Map": {"base": "Quarry Map", "class": "Maps", "other": ["Rarity Rare"], "type": "challenge"},
	"0 Phantasmagoria Map": {"base": "Phantasmagoria Map", "class": "Maps", "other": ["Rarity Rare"], "type": "challenge"},
	"0 Shore Map": {"base": "Shore Map", "class": "Maps", "other": ["Rarity Rare"], "type": "challenge"},
	"0 Graveyard Map": {"base": "Graveyard Map", "class": "Maps", "other": ["Rarity Rare"], "type": "challenge"},
	"0 Villa Map": {"base": "Villa Map", "class": "Maps", "other": ["Rarity Rare"], "type": "challenge"},

	"0 Assassin's Favour": {"base": "Assassin's Favour", "class": "Divination Card", "type": "challenge"},
	"0 Cartographer's Delight": {"base": "Cartographer's Delight", "class": "Divination Card", "type": "challenge"},
	"0 Humility": {"base": "Humility", "class": "Divination Card", "type": "challenge"},
	"0 Hunter's Resolve": {"base": "Hunter's Resolve", "class": "Divination Card", "type": "challenge"},
	"0 Lysah's Respite": {"base": "Lysah's Respite", "class": "Divination Card", "type": "challenge"},
	"0 The Battle Born": {"base": "The Battle Born", "class": "Divination Card", "type": "challenge"},
	"0 The Body": {"base": "The Body", "class": "Divination Card", "type": "challenge"},
	"0 The Brittle Emperor": {"base": "The Brittle Emperor", "class": "Divination Card", "type": "challenge"},
	"0 The Gentleman": {"base": "The Gentleman", "class": "Divination Card", "type": "challenge"},
	"0 The Mercenary": {"base": "The Mercenary", "class": "Divination Card", "type": "challenge"},
	"0 The Trial": {"base": "The Trial", "class": "Divination Card", "type": "challenge"},
	"0 Volatile Power": {"base": "Volatile Power", "class": "Divination Card", "type": "challenge"},

}