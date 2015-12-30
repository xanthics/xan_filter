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
    "very high": ["Class \"Divination Card\""],
    "high": ["Class \"Divination Card\"",
             "SetBorderColor 175 96 37",
             "SetFontSize 40",
             "PlayAlertSound 6 175"],
    "normal": ["Class \"Divination Card\"",
               "SetBorderColor 0 186 254",
               "PlayAlertSound 6 75"],
    "low": ["Class \"Divination Card\""],
    "ignore": [""],
    "hide": ["Class \"Divination Card\""]
}

# Base type : settings pair
items = {
    "0 The Brittle Emperor": {"base": "The Brittle Emperor", "type": "high"},
    "0 The Doctor": {"base": "The Doctor", "type": "high"},
    "0 The Hunger": {"base": "The Hunger", "type": "high"},
    "0 The Wind": {"base": "The Wind", "type": "high"},
    "0 The Avenger": {"base": "The Avenger", "type": "high"},
    "0 The Celestial Justicar": {"base": "The Celestial Justicar", "type": "high"},
    "0 The Fiend": {"base": "The Fiend", "type": "high"},
    "0 The King's Heart": {"base": "The King's Heart", "type": "high"},
    "0 The Pact": {"base": "The Pact", "type": "high"},
    "0 The Watcher": {"base": "The Watcher", "type": "high"},
    "0 The Queen": {"base": "The Queen", "type": "high"},
    "0 The Last One Standing": {"base": "The Last One Standing", "type": "high"},
    "0 The Artist": {"base": "The Artist", "type": "high"},
    "0 Wealth and Power": {"base": "Wealth and Power", "type": "high"},
    "0 House of Mirrors": {"base": "House of Mirrors", "type": "high"},
    "0 The Dragon's Heart": {"base": "The Dragon's Heart", "type": "high"},
    "0 Pride Before the Fall": {"base": "Pride Before the Fall", "type": "high"},
    "0 The Vast": {"base": "The Vast", "type": "high"},
    "0 Bowyer's Dream": {"base": "Bowyer's Dream", "type": "high"},
    "0 Hunter's Reward": {"base": "Hunter's Reward", "type": "high"},
    "0 The Hoarder": {"base": "The Hoarder", "type": "high"},
    "0 The Drunken Aristocrat": {"base": "The Drunken Aristocrat", "type": "high"},
    "0 The Pack Leader": {"base": "The Pack Leader", "type": "high"},
    "0 The Sun": {"base": "The Sun", "type": "high"},
    "0 The Gladiator": {"base": "The Gladiator", "type": "high"},
    "0 Abandoned Wealth": {"base": "Abandoned Wealth", "type": "high"},
    "0 The Incantation": {"base": "The Incantation", "type": "high"},
    "0 Time-Lost Relic": {"base": "Time-Lost Relic", "type": "high"},
    "0 The Dark Mage": {"base": "The Dark Mage", "type": "high"},
    "0 The Road to Power": {"base": "The Road to Power", "type": "high"},
    "0 The Chains that Bind": {"base": "The Chains that Bind", "type": "high"},
    "0 The Betrayal": {"base": "The Betrayal", "type": "high"},
    "0 The Trial": {"base": "The Trial", "type": "high"},
    "0 Last Hope": {"base": "Last Hope", "type": "high"},
    "0 Anarchy's Price": {"base": "Anarchy's Price", "type": "high"},
    "0 Chaotic Disposition": {"base": "Chaotic Disposition", "type": "high"},
    "0 Coveted Possession": {"base": "Coveted Possession", "type": "high"},
    "0 The Enlightened": {"base": "The Enlightened", "type": "high"},
    "0 The Ethereal": {"base": "The Ethereal", "type": "high"},
    "0 The Fletcher": {"base": "The Fletcher", "type": "high"},
    "0 The Offering": {"base": "The Offering", "type": "high"},
    "0 The Poet": {"base": "The Poet", "type": "high"},
    "0 The Thaumaturgist": {"base": "The Thaumaturgist", "type": "high"},
    "0 The Warlord": {"base": "The Warlord", "type": "high"},
    "7 A Mother's Parting Gift": {"base": "A Mother's Parting Gift", "type": "hide"},
    "7 The Carrion Crow": {"base": "The Carrion Crow", "type": "hide"},
    "7 The King's Blade": {"base": "The King's Blade", "type": "hide"},
    "7 The Inoculated": {"base": "The Inoculated", "type": "hide"},
    "7 Turn the Other Cheek": {"base": "Turn the Other Cheek", "type": "hide"},
    "9 Other Divination Cards": {"type": "normal"}
}
