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

desc = "formatting template for all files"

# Text settings for various categories
# This is where you would define general settings for a category, such as PlayAlertSound.
# Each config should be its own array element.  Parsing will handle tabs/etc.
# ignore and hide have special meaning(see comment)
settings = {
	"chance": ["Rarity Normal", "SetFontSize 28", "SetBackgroundColor 0 0 0 200", "SetBorderColor 191 91 0 150"],

	"chromatic": ["SocketGroup RGB", "SetBorderColor 0 191 0", "SetFontSize 28"],

	"t1 ilvl83/84 crafting": ["Rarity <= Magic"],

	"currency very high": ["SetBorderColor 170 158 130", "SetFontSize 45", "PlayAlertSound 3 300"],
	"currency high": ["SetBorderColor 170 158 130", "SetFontSize 37", "PlayAlertSound 5 75"],
	"currency normal": ["SetBorderColor 170 158 130", "PlayAlertSound 5 25"],
	"currency low": ["SetBorderColor 170 158 130 200", "SetFontSize 30"],

	"divination high": ["SetBorderColor 30 144 255", "SetFontSize 40", "PlayAlertSound 6 175"],
	"divination normal": ["SetBorderColor 30 144 255", "PlayAlertSound 6 50"],

	"flask high": ["SetBorderColor 0 255 0", "SetFontSize 35"],

	"gem very high": ["SetBorderColor 27 162 155", "SetFontSize 35"],
	"gem high": ["SetBorderColor 27 162 155", "SetFontSize 30"],
	"gem normal": ["SetBorderColor 27 162 155"],
	"gem low": ["SetFontSize 24", "SetBackgroundColor 0 0 0 200"],

	"leveling high": ["SetFontSize 28", "SetBackgroundColor 0 0 0 100", "SetBorderColor 255 40 0"],
	"leveling normal": ["SetFontSize 24", "SetBackgroundColor 0 0 0 100", "SetBorderColor 0 100 150"],
	"leveling low": ["SetFontSize 18", "Sockets > 2", "SetBackgroundColor 0 0 0 100", "SetBorderColor 100 100 100"],

	"map very high": ["SetBorderColor 150 0 0", "SetFontSize 42", "PlayAlertSound 6 125"],
	"map high": ["PlayAlertSound 2 100", "SetFontSize 37"],
	"map normal": [""],

	"levelling rare high": ["Rarity Rare", "SetBorderColor 255 255 119 150", "SetFontSize 34"],
	"rare high": ["Rarity Rare", "SetBorderColor 255 255 119", "SetFontSize 34"],
	"levelling rare normal": ["Rarity Rare", "SetBorderColor 255 255 119 150"],
	"rare normal": ["Rarity Rare", "SetBorderColor 255 255 119"],
	"rare low": ["Rarity Rare", "SetFontSize 28"],

	"recipe item normal": ["SetBorderColor 204 0 154", "SetFontSize 28"],

	"show very high": ["SetBorderColor 0 255 150", "SetFontSize 45", "PlayAlertSound 1 175"],
	"show high": ["SetBorderColor 0 255 75", "SetFontSize 37"],
	"show normal": ["SetBorderColor 0 255 0", "SetFontSize 28"],
	"show low": ["SetFontSize 20"],

	"t1 83/84 rare high": ["Rarity Rare", "SetBorderColor 255 40 0", "SetFontSize 34"],

	"unique very high": ["Rarity Unique", "SetBorderColor 175 96 37", "SetFontSize 45", "PlayAlertSound 3 300"],
	"unique high": ["Rarity Unique", "SetFontSize 37", "SetBorderColor 175 96 37", "PlayAlertSound 3 75"],
	"unique normal": ["Rarity Unique", "PlayAlertSound 3 50"],

	"normal": ["SetFontSize 28"],
	"low": ["SetFontSize 18", "SetBackgroundColor 0 0 0 100", "SetBorderColor 100 100 100"],
	"ignore": [""],  # will have no styling applied and will use the default set at the end
	"hide": [""]  # Will be explicitly hidden with applied styling

}
