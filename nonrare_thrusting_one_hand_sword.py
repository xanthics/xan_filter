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

desc = "Nonrare item for leveling or crafting"

# Text settings for various categories
# This is where you would define general settings for a category, such as PlayAlertSound.
# Each config should be its own array element.  Parsing will handle tabs/etc.
# ignore and hide have special meaning(see comment) everything else is local to file
settings = {
	"very high": ["SetFontSize 28",
				  "Sockets > 2",
				  "SetBackgroundColor 0 0 0 100",
				  "SetBorderColor 255 40 0"],
	"high": ["SetFontSize 24",
			 "Sockets > 2",
			 "SetBackgroundColor 0 0 0 100",
			 "SetBorderColor 0 100 150"],
	"normal": ["SetFontSize 18",
			   "Sockets > 2",
			   "SetBackgroundColor 0 0 0 100",
			   "SetBorderColor 100 100 100"],
	"low": [""],
	"ignore": [""],  # will have no styling applied and will use the default set at the end
	"hide": [""]  # Will be explicitly hidden with applied styling
}

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Rusted Spike": {"base": "Rusted Spike", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "normal"},
	"Whalebone Rapier": {"base": "Whalebone Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 12"], "type": "normal"},
	"Battered Foil": {"base": "Battered Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "normal"},
	"Basket Rapier": {"base": "Basket Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "normal"},
	"Jagged Foil": {"base": "Jagged Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 27"], "type": "normal"},
	"Antique Rapier": {"base": "Antique Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 31"], "type": "normal"},
	"Elegant Foil": {"base": "Elegant Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 35"], "type": "normal"},
	"Thorn Rapier": {"base": "Thorn Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "normal"},
	"Smallsword": {"base": "Smallsword", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "normal"},
	"Wyrmbone Rapier": {"base": "Wyrmbone Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "normal"},
	"Burnished Foil": {"base": "Burnished Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 45"], "type": "normal"},
	"Estoc": {"base": "Estoc", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 48"], "type": "normal"},
	"Serrated Foil": {"base": "Serrated Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 51"], "type": "normal"},
	"Primeval Rapier": {"base": "Primeval Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "normal"},
	"Fancy Foil": {"base": "Fancy Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 57"], "type": "normal"},
	"Apex Rapier": {"base": "Apex Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "normal"},
	"Courtesan Sword": {"base": "Courtesan Sword", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "normal"},
	"Dragonbone Rapier": {"base": "Dragonbone Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "normal"},
	"Tempered Foil": {"base": "Tempered Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "normal"},
	"Pecoraro": {"base": "Pecoraro", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "normal"},
	"Spiraled Foil": {"base": "Spiraled Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "normal"},
	"Vaal Rapier": {"base": "Vaal Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "normal"},
	"Jewelled Foil": {"base": "Jewelled Foil", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "normal"},
	"Harpy Rapier": {"base": "Harpy Rapier", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "normal"},
	"Dragoon Sword": {"base": "Dragoon Sword", "class": "Thrusting One Hand Sword", "other": ["Rarity <= Magic", "ItemLevel <= 77"], "type": "normal"}}
