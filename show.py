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

desc = "Always show"

# Text settings for various categories
settings = {
    "very high": ["SetBorderColor 0 255 150",
                  "SetFontSize 45",
                  "PlayAlertSound 1 175"],
    "high": ["SetBorderColor 0 255 75",
             "SetFontSize 37"],
    "normal": ["SetBorderColor 0 255 0",
               "SetFontSize 28"],
    "low": ["SetFontSize 20"],
    "ignore": [""],
    "hide": [""]
}

# Base type : settings pair
items = {
    "01 Tabula Exception": {"base": "Simple Robe", "other": ["Rarity Unique", "SocketGroup WWWWWW"], "type": "high"},
    "02 6L": {"other": ["LinkedSockets 6"], "type": "very high"},
    "03 5L": {"other": ["LinkedSockets 5", "PlayAlertSound 2 75"], "type": "high"},
    "04 6S": {"other": ["Sockets 6", "PlayAlertSound 2 50"], "type": "high"},
    "10 Talisman": {'other': ["Rarity >= Rare", "ItemLevel >= 70"], "base": "Talisman", "type": "high"},
    "11 Talisman": {'other': ["ItemLevel >= 70"], "base": "Talisman", "type": "high"},
    "12 Talisman": {"base": "Talisman", "type": "low"},
    "0 Fishing Rod": {"base": "Fishing Rod", "type": "very high"},
    "0 Hideout Doodads": {"class": "Hideout Doodads","type": "low"},
    "0 Microtransactions": {"class": "Microtransactions","type": "low"},
    "0 Quest": {"class": "Quest", "type": "normal"},
    "0 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "high"},
    "0 Jewel": {"class": "Jewel", "other": ["Rarity <= Magic"], "type": "normal"},
}