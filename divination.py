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

desc = "Divination Card"

# Text settings for various categories
settings = {
	"low": [""],
	"ignore": [""],
	"hide": [""]
}

# Base type : settings pair
items = {
	"0 The Brittle Emperor": {"base": "The Brittle Emperor", "class": "Divination Card", "type": "divination high"},
	"0 The Doctor": {"base": "The Doctor", "class": "Divination Card", "type": "divination high"},
	"0 The Hunger": {"base": "The Hunger", "class": "Divination Card", "type": "divination high"},
	"0 The Wind": {"base": "The Wind", "class": "Divination Card", "type": "divination high"},
	"0 The Avenger": {"base": "The Avenger", "class": "Divination Card", "type": "divination high"},
	"0 The Celestial Justicar": {"base": "The Celestial Justicar", "class": "Divination Card", "type": "divination high"},
	"0 The Fiend": {"base": "The Fiend", "class": "Divination Card", "type": "divination high"},
	"0 The King's Heart": {"base": "The King's Heart", "class": "Divination Card", "type": "divination high"},
	"0 The Pact": {"base": "The Pact", "class": "Divination Card", "type": "divination high"},
	"0 The Watcher": {"base": "The Watcher", "class": "Divination Card", "type": "divination high"},
	"0 The Queen": {"base": "The Queen", "class": "Divination Card", "type": "divination high"},
	"0 The Last One Standing": {"base": "The Last One Standing", "class": "Divination Card", "type": "divination high"},
	"0 The Artist": {"base": "The Artist", "class": "Divination Card", "type": "divination high"},
	"0 Wealth and Power": {"base": "Wealth and Power", "class": "Divination Card", "type": "divination high"},
	"0 House of Mirrors": {"base": "House of Mirrors", "class": "Divination Card", "type": "divination high"},
	"0 The Dragon's Heart": {"base": "The Dragon's Heart", "class": "Divination Card", "type": "divination high"},
	"0 Pride Before the Fall": {"base": "Pride Before the Fall", "class": "Divination Card", "type": "divination high"},
	"0 The Vast": {"base": "The Vast", "class": "Divination Card", "type": "divination high"},
	"0 Bowyer's Dream": {"base": "Bowyer's Dream", "class": "Divination Card", "type": "divination high"},
	"0 Hunter's Reward": {"base": "Hunter's Reward", "class": "Divination Card", "type": "divination high"},
	"0 The Hoarder": {"base": "The Hoarder", "class": "Divination Card", "type": "divination high"},
	"0 The Drunken Aristocrat": {"base": "The Drunken Aristocrat", "class": "Divination Card", "type": "divination high"},
	"0 The Pack Leader": {"base": "The Pack Leader", "class": "Divination Card", "type": "divination high"},
	"0 The Sun": {"base": "The Sun", "class": "Divination Card", "type": "divination high"},
	"0 The Gladiator": {"base": "The Gladiator", "class": "Divination Card", "type": "divination high"},
	"0 Abandoned Wealth": {"base": "Abandoned Wealth", "class": "Divination Card", "type": "divination high"},
	"0 The Incantation": {"base": "The Incantation", "class": "Divination Card", "type": "divination high"},
	"0 Time-Lost Relic": {"base": "Time-Lost Relic", "class": "Divination Card", "type": "divination high"},
	"0 The Dark Mage": {"base": "The Dark Mage", "class": "Divination Card", "type": "divination high"},
	"0 The Road to Power": {"base": "The Road to Power", "class": "Divination Card", "type": "divination high"},
	"0 The Chains that Bind": {"base": "The Chains that Bind", "class": "Divination Card", "type": "divination high"},
	"0 The Betrayal": {"base": "The Betrayal", "class": "Divination Card", "type": "divination high"},
	"0 The Trial": {"base": "The Trial", "class": "Divination Card", "type": "divination high"},
	"0 Last Hope": {"base": "Last Hope", "class": "Divination Card", "type": "divination high"},
	"0 Anarchy's Price": {"base": "Anarchy's Price", "class": "Divination Card", "type": "divination high"},
	"0 Chaotic Disposition": {"base": "Chaotic Disposition", "class": "Divination Card", "type": "divination high"},
	"0 Coveted Possession": {"base": "Coveted Possession", "class": "Divination Card", "type": "divination high"},
	"0 The Enlightened": {"base": "The Enlightened", "class": "Divination Card", "type": "divination high"},
	"0 The Ethereal": {"base": "The Ethereal", "class": "Divination Card", "type": "divination high"},
	"0 The Fletcher": {"base": "The Fletcher", "class": "Divination Card", "type": "divination high"},
	"0 The Offering": {"base": "The Offering", "class": "Divination Card", "type": "divination high"},
	"0 The Poet": {"base": "The Poet", "class": "Divination Card", "type": "divination high"},
	"0 The Thaumaturgist": {"base": "The Thaumaturgist", "class": "Divination Card", "type": "divination high"},
	"0 The Dapper Prodigy": {"base": "The Dapper Prodigy", "class": "Divination Card", "type": "divination high"},
	"0 The Warlord": {"base": "The Warlord", "class": "Divination Card", "type": "divination high"},
	"0 Rats": {"base": "Rats", "class": "Divination Card", "type": "divination high"},
	"0 Tranquillity": {"base": "Tranquillity", "class": "Divination Card", "type": "divination high"},
	"0 The Risk": {"base": "The Risk", "class": "Divination Card", "type": "divination high"},
	"0 The Devastator": {"base": "The Devastator", "class": "Divination Card", "type": "divination high"},
	"0 The Immortal": {"base": "The Immortal", "class": "Divination Card", "type": "divination high"},
	"0 Heterochromia": {"base": "Heterochromia", "class": "Divination Card", "type": "divination high"},

	"1 Thunderous Skies": {"base": "Thunderous Skies", "class": "Divination Card", "type": "divination low"},
	"1 The Scholar": {"base": "The Scholar", "class": "Divination Card", "type": "divination low"},

	"7 A Mother's Parting Gift": {"base": "A Mother's Parting Gift", "class": "Divination Card", "type": "hide"},
	"7 The Carrion Crow": {"base": "The Carrion Crow", "class": "Divination Card", "type": "hide"},
	"7 The Rabid Rhoa": {"base": "The Rabid Rhoa", "class": "Divination Card", "type": "hide"},
	"7 The King's Blade": {"base": "The King's Blade", "class": "Divination Card", "type": "hide"},
	"7 The Inoculated": {"base": "The Inoculated", "class": "Divination Card", "type": "hide"},
	"7 Turn the Other Cheek": {"base": "Turn the Other Cheek", "class": "Divination Card", "type": "hide"},
	"9 Other Divination Cards": {"class": "Divination Card", "type": "divination normal"}
}
