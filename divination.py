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
             "SetTextColor 0 186 254",
             "SetBorderColor 175 96 37",
             "SetFontSize 40",
             "PlayAlertSound 6 175"],
    "normal": ["Class \"Divination Card\"",
               "SetTextColor 0 186 254",
               "SetBorderColor 0 186 254",
               "PlayAlertSound 6 75"],
    "low": ["Class \"Divination Card\""],
    "hide": ["Class \"Divination Card\""]
}

# Base type : settings pair
items = {
    "01 The Brittle Emperor": {"base": "The Brittle Emperor", "type": "high"},
    "02 The Doctor": {"base": "The Doctor", "type": "high"},
    "03 The Hunger": {"base": "The Hunger", "type": "high"},
    "04 The Wind": {"base": "The Wind", "type": "high"},
    "05 The Avenger": {"base": "The Avenger", "type": "high"},
    "06 The Celestial Justicar": {"base": "The Celestial Justicar", "type": "high"},
    "07 The Fiend": {"base": "The Fiend", "type": "high"},
    "08 The King's Heart": {"base": "The King's Heart", "type": "high"},
    "09 The Pact": {"base": "The Pact", "type": "high"},
    "10 The Watcher": {"base": "The Watcher", "type": "high"},
    "11 The Queen": {"base": "The Queen", "type": "high"},
    "12 The Last One Standing": {"base": "The Last One Standing", "type": "high"},
    "13 The Artist": {"base": "The Artist", "type": "high"},
    "14 Wealth and Power": {"base": "Wealth and Power", "type": "high"},
    "15 House of Mirrors": {"base": "House of Mirrors", "type": "high"},
    "16 The Dragon's Heart": {"base": "The Dragon's Heart", "type": "high"},
    "17 Pride Before the Fall": {"base": "Pride Before the Fall", "type": "high"},
    "18 The Vast": {"base": "The Vast", "type": "high"},
    "19 Bowyer's Dream": {"base": "Bowyer's Dream", "type": "high"},
    "20 Hunter's Reward": {"base": "Hunter's Reward", "type": "high"},
    "21 The Hoarder": {"base": "The Hoarder", "type": "high"},
    "22 The Drunken Aristocrat": {"base": "The Drunken Aristocrat", "type": "high"},
    "23 The Pack Leader": {"base": "The Pack Leader", "type": "high"},
    "24 The Sun": {"base": "The Sun", "type": "high"},
    "25 The Gladiator": {"base": "The Gladiator", "type": "high"},
    "26 Abandoned Wealth": {"base": "Abandoned Wealth", "type": "high"},
    "27 The Incantation": {"base": "The Incantation", "type": "high"},
    "28 Time-Lost Relic": {"base": "Time-Lost Relic", "type": "high"},
    "29 The Dark Mage": {"base": "The Dark Mage", "type": "high"},
    "30 The Road to Power": {"base": "The Road to Power", "type": "high"},
    "31 The Chains that Bind": {"base": "The Chains that Bind", "type": "high"},
    "32 The Betrayal": {"base": "The Betrayal", "type": "high"},
    "33 The Trial": {"base": "The Trial", "type": "high"},
    "34 Last Hope": {"base": "Last Hope", "type": "high"},
    "35 A Mother's Parting Gift": {"base": "A Mother's Parting Gift", "type": "hide"},
    "36 The Carrion Crow": {"base": "The Carrion Crow", "type": "hide"},
    "37 The King's Blade": {"base": "The King's Blade", "type": "hide"},
    "38 The Inoculated": {"base": "The Inoculated", "type": "hide"},
    "39 Turn the Other Cheek": {"base": "Turn the Other Cheek", "type": "hide"},
    "99 Other Divination Cards": {"type": "normal"}
}
