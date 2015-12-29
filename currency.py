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

desc = "Currency"

# Text settings for various categories
settings = {
    "very high": ["Class \"Currency\"",
                  "SetBorderColor 0 255 150",
                  "SetBackgroundColor 0 0 0 255",
                  "SetFontSize 45",
                  "PlayAlertSound 3 300"],
    "high": ["Class \"Currency\"",
             "SetBorderColor 170 158 130",
             "SetBackgroundColor 0 0 0 255",
             "SetFontSize 37",
             "PlayAlertSound 5 175"],
    "normal": ["Class \"Currency\"",
               "SetTextColor 170 158 130",
               "SetBorderColor 170 158 130 0",
               "SetBackgroundColor 0 0 0 255",
               "PlayAlertSound 5 75"],
    "low": ["Class \"Currency\"",
            "SetTextColor 170 158 130",
            "SetBorderColor 170 158 130 0",
            "SetBackgroundColor 0 0 0 255",
            "SetFontSize 26"],
    "hide": ["Class \"Currency\""]
}

# Base type : settings pair
items = {
    "01 Mirror of Kalandra": {"base": "Mirror of Kalandra", "type": "very high"},
    "02 Exalted Orb": {"base": "Exalted Orb", "type": "very high"},
    "03 Divine Orb": {"base": "Divine Orb", "type": "very high"},
    "04 Albino Rhoa Feather": {"base": "Albino Rhoa Feather", "type": "very high"},
    "05 Orb of Regret": {"base": "Orb of Regret", "type": "high"},
    "06 Gemcutter's Prism": {"base": "Gemcutter's Prism", "type": "high"},
    "07 Chaos Orb": {"base": "Chaos Orb", "type": "high"},
    "08 Regal Orb": {"base": "Regal Orb", "type": "high"},
    "09 Orb of Fusing": {"base": "Orb of Fusing", "type": "high"},
    "10 Blessed Orb": {"base": "Blessed Orb", "type": "high"},
    "11 Orb of Scouring": {"base": "Orb of Scouring", "type": "high"},
    "12 Orb of Alchemy": {"base": "Orb of Alchemy", "type": "normal"},
    "13 Vaal Orb": {"base": "Vaal Orb", "type": "high"},
    "14 Cartographer's Chisel": {"base": "Cartographer's Chisel", "type": "normal"},
    "15 Glassblower's Bauble": {"base": "Glassblower's Bauble", "type": "normal"},
    "16 Orb of Chance": {"base": "Orb of Chance", "type": "normal"},
    "17 Jeweller's Orb": {"base": "Jeweller's Orb", "type": "normal"},
    "18 Chromatic Orb": {"base": "Chromatic Orb", "type": "normal"},
    "19 Orb of Alteration": {"base": "Orb of Alteration", "type": "normal"},
    "20 Orb of Transmutation": {"base": "Orb of Transmutation", "type": "normal"},
    "21 Blacksmith's Whetstone": {"base": "Blacksmith's Whetstone", "type": "low"},
    "22 Armourer's Scrap": {"base": "Armourer's Scrap", "type": "low"},
    "23 Scroll of Wisdom": {"base": "Scroll of Wisdom", "type": "low"},
    "24 Portal Scroll": {"base": "Portal Scroll", "type": "low"},
    "25 Alteration Shard": {"base": "Alteration Shard", "type": "low"},
    "26 Scroll Fragment": {"base": "Scroll Fragment", "type": "hide"},
    "99 Currency": {"class": "Currency", "type": "normal"}
}