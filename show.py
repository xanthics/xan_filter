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

# Base type : settings pair
items = {
    "01 Tabula Exception": {"base": "Simple Robe", "other": ["Rarity Unique", "SocketGroup WWWWWW", "PlayAlertSound 3 50"], "type": "show high"},
    "02 6L": {"other": ["LinkedSockets 6"], "type": "show very high"},
    "03 5L": {"other": ["LinkedSockets 5", "PlayAlertSound 2 75"], "type": "show high"},
    "04 6S": {"other": ["Sockets 6", "PlayAlertSound 2 50"], "type": "show high"},
    "10 Talisman": {'other': ["Rarity >= Rare", "ItemLevel >= 70"], "base": "Talisman", "type": "show high"},
    "11 Talisman": {'other': ["ItemLevel >= 70"], "base": "Talisman", "type": "show high"},
    "12 Talisman": {"base": "Talisman", "type": "show low"},
    "0 Fishing Rod": {"base": "Fishing Rod", "type": "show very high"},
    "0 Hideout Doodads": {"class": "Hideout Doodads", "type": "show low"},
    "0 Microtransactions": {"class": "Microtransactions", "type": "show low"},
    "0 Quest": {"class": "Quest", "type": "show normal"},
    "0 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "show high"},
    "0 Jewel": {"class": "Jewel", "other": ["Rarity <= Magic"], "type": "show normal"},
    "0 Silver Key": {"base": "Silver Key", "type": "show high"},
    "0 Golden Key": {"base": "Golden Key", "type": "show high"},
    "0 Treasure Key": {"base": "Treasure Key", "type": "show high"},
    "0 Bane of the Loyal": {"base": "Bane of the Loyal", "type": "show high"},
    "0 Cogs of Disruption": {"base": "Cogs of Disruption", "type": "show high"},
    "0 Cube of Absorption": {"base": "Cube Of Absorption", "type": "show high"},
    "0 Heart of the Gargoyle": {"base": "Heart of the Gargoyle", "type": "show high"},
    "0 Orb of Elemental Essence": {"base": "Orb of Elemental Essence", "type": "show high"},
    "0 Portal Shredder": {"base": "Portal Shredder", "type": "show high"},
    "0 Rod of Detonation": {"base": "Rod of Detonation", "type": "show high"},
    "0 Sand of Eternity": {"base": "Sand of Eternity", "type": "show high"},
    "9 Starter weapon": {"other": ["Class Dagger Wand \"One Hand\" Bow Stave \"Two Hand\" Sceptre Claws", "ItemLevel < 2"], "type": "low"},

    "0 Brinerot magic item": {"class": "Gloves", "other": ["Rarity Magic"], "type": "ignore"},
    "0 Mutewind magic item": {"class": "Boots", "other": ["Rarity Magic"], "type": "ignore"},
    "0 Redblade magic item": {"class": "Helms", "other": ["Rarity Magic"], "type": "ignore"},
    "0 Renegade magic item": {"other": ["Class Dagger Wand \"One Hand\" Bow Stave \"Two Hand\" Sceptre Claws", "Rarity Magic"], "type": "ignore"},

}