#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
* Copyright (c) 2016 Jeremy Parks. All rights reserved.
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

# Base type : settings pair
items = {
	"0 The Doctor": {"base": "The Doctor", "class": "Divination Card", "type": "divination very high"},
	"0 Heterochromia": {"base": "Heterochromia", "class": "Divination Card", "type": "divination very high"},
	"0 The Queen": {"base": "The Queen", "class": "Divination Card", "type": "divination very high"},
	"0 The Dragon's Heart": {"base": "The Dragon's Heart", "class": "Divination Card", "type": "divination very high"},
	"0 The Ethereal": {"base": "The Ethereal", "class": "Divination Card", "type": "divination very high"},
	"0 The Brittle Emperor": {"base": "The Brittle Emperor", "class": "Divination Card", "type": "divination very high"},
	"0 The Cursed King": {"base": "The Cursed King", "class": "Divination Card", "type": "divination very high"},
	"0 The Last One Standing": {"base": "The Last One Standing", "class": "Divination Card", "type": "divination very high"},
	"0 The Warlord": {"base": "The Warlord", "class": "Divination Card", "type": "divination very high"},
	"0 Bowyer's Dream": {"base": "Bowyer's Dream", "class": "Divination Card", "type": "divination very high"},
	"0 Last Hope": {"base": "Last Hope", "class": "Divination Card", "type": "divination very high"},
	"0 The Offering": {"base": "The Offering", "class": "Divination Card", "type": "divination very high"},
	"0 The King's Heart": {"base": "The King's Heart", "class": "Divination Card", "type": "divination very high"},
	"0 Abandoned Wealth": {"base": "Abandoned Wealth", "class": "Divination Card", "type": "divination very high"},
	"0 Pride Before the Fall": {"base": "Pride Before the Fall", "class": "Divination Card", "type": "divination very high"},
	"0 The Artist": {"base": "The Artist", "class": "Divination Card", "type": "divination very high"},
	"0 The Celestial Justicar": {"base": "The Celestial Justicar", "class": "Divination Card", "type": "divination very high"},
	"0 The Dark Mage": {"base": "The Dark Mage", "class": "Divination Card", "type": "divination very high"},
	"0 The Enlightened": {"base": "The Enlightened", "class": "Divination Card", "type": "divination very high"},
	"0 The Harvester": {"base": "The Harvester", "class": "Divination Card", "type": "divination very high"},
	"0 The Hunger": {"base": "The Hunger", "class": "Divination Card", "type": "divination very high"},
	"0 The Dapper Prodigy": {"base": "The Dapper Prodigy", "class": "Divination Card", "type": "divination very high"},
	"0 Hope": {"base": "Hope", "class": "Divination Card", "type": "divination very high"},
	"0 The Avenger": {"base": "The Avenger", "class": "Divination Card", "type": "divination very high"},
	"0 The Road to Power": {"base": "The Road to Power", "class": "Divination Card", "type": "divination very high"},
	"0 The Spoiled Prince": {"base": "The Spoiled Prince", "class": "Divination Card", "type": "divination very high"},
	"0 The Surveyor": {"base": "The Surveyor", "class": "Divination Card", "type": "divination very high"},
	"0 The Trial": {"base": "The Trial", "class": "Divination Card", "type": "divination very high"},
	"1 Cartographer's Delight": {"base": "Cartographer's Delight", "class": "Divination Card", "type": "divination high"},
	"1 Emperor of Purity": {"base": "Emperor of Purity", "class": "Divination Card", "type": "divination high"},
	"1 Glimmer of Hope": {"base": "Glimmer of Hope", "class": "Divination Card", "type": "divination high"},
	"1 The Chains that Bind": {"base": "The Chains that Bind", "class": "Divination Card", "type": "divination high"},
	"1 Gift of the Gemling Queen": {"base": "Gift of the Gemling Queen", "class": "Divination Card", "type": "divination high"},
	"1 The Demoness": {"base": "The Demoness", "class": "Divination Card", "type": "divination high"},
	"1 Assassin's Favour": {"base": "Assassin's Favour", "class": "Divination Card", "type": "divination high"},
	"1 Earth Drinker": {"base": "Earth Drinker", "class": "Divination Card", "type": "divination high"},
	"1 Lost Worlds": {"base": "Lost Worlds", "class": "Divination Card", "type": "divination high"},
	"1 The Arena Champion": {"base": "The Arena Champion", "class": "Divination Card", "type": "divination high"},
	"1 The Body": {"base": "The Body", "class": "Divination Card", "type": "divination high"},
	"1 The Risk": {"base": "The Risk", "class": "Divination Card", "type": "divination high"},
	"1 The Cartographer": {"base": "The Cartographer", "class": "Divination Card", "type": "divination high"},
	"1 Lysah's Respite": {"base": "Lysah's Respite", "class": "Divination Card", "type": "divination high"},
	"1 The Union": {"base": "The Union", "class": "Divination Card", "type": "divination high"},
	"1 Merciless Armament": {"base": "Merciless Armament", "class": "Divination Card", "type": "divination high"},
	"1 Rain Tempter": {"base": "Rain Tempter", "class": "Divination Card", "type": "divination high"},
	"1 The Gentleman": {"base": "The Gentleman", "class": "Divination Card", "type": "divination high"},
	"1 The Gladiator": {"base": "The Gladiator", "class": "Divination Card", "type": "divination high"},
	"1 The Mercenary": {"base": "The Mercenary", "class": "Divination Card", "type": "divination high"},
	"1 The Pack Leader": {"base": "The Pack Leader", "class": "Divination Card", "type": "divination high"},
	"1 The Watcher": {"base": "The Watcher", "class": "Divination Card", "type": "divination high"},
	"1 The Hoarder": {"base": "The Hoarder", "class": "Divination Card", "type": "divination high"},
	"1 The Incantation": {"base": "The Incantation", "class": "Divination Card", "type": "divination high"},
	"1 Grave Knowledge": {"base": "Grave Knowledge", "class": "Divination Card", "type": "divination high"},
	"1 Humility": {"base": "Humility", "class": "Divination Card", "type": "divination high"},
	"1 Hunter's Resolve": {"base": "Hunter's Resolve", "class": "Divination Card", "type": "divination high"},
	"1 Rats": {"base": "Rats", "class": "Divination Card", "type": "divination high"},
	"1 The Cataclysm": {"base": "The Cataclysm", "class": "Divination Card", "type": "divination high"},
	"1 The Dragon": {"base": "The Dragon", "class": "Divination Card", "type": "divination high"},
	"1 The Drunken Aristocrat": {"base": "The Drunken Aristocrat", "class": "Divination Card", "type": "divination high"},
	"1 The Pact": {"base": "The Pact", "class": "Divination Card", "type": "divination high"},
	"1 The Sigil": {"base": "The Sigil", "class": "Divination Card", "type": "divination high"},
	"1 The Wind": {"base": "The Wind", "class": "Divination Card", "type": "divination high"},
	"1 Tranquillity": {"base": "Tranquillity", "class": "Divination Card", "type": "divination high"},
	"1 Vinia's Token": {"base": "Vinia's Token", "class": "Divination Card", "type": "divination high"},
	"1 Volatile Power": {"base": "Volatile Power", "class": "Divination Card", "type": "divination high"},
	"1 Lucky Connections": {"base": "Lucky Connections", "class": "Divination Card", "type": "divination high"},
	"1 The Lion": {"base": "The Lion", "class": "Divination Card", "type": "divination high"},
	"1 The Sun": {"base": "The Sun", "class": "Divination Card", "type": "divination high"},
	"1 The One With All": {"base": "The One With All", "class": "Divination Card", "type": "divination high"},
	"1 Anarchy's Price": {"base": "Anarchy's Price", "class": "Divination Card", "type": "divination high"},
	"1 Birth of the Three": {"base": "Birth of the Three", "class": "Divination Card", "type": "divination high"},
	"1 Coveted Possession": {"base": "Coveted Possession", "class": "Divination Card", "type": "divination high"},
	"1 Death": {"base": "Death", "class": "Divination Card", "type": "divination high"},
	"1 Destined to Crumble": {"base": "Destined to Crumble", "class": "Divination Card", "type": "divination high"},
	"1 Doedre's Madness": {"base": "Doedre's Madness", "class": "Divination Card", "type": "divination high"},
	"1 Dying Anguish": {"base": "Dying Anguish", "class": "Divination Card", "type": "divination high"},
	"1 Emperor's Luck": {"base": "Emperor's Luck", "class": "Divination Card", "type": "divination high"},
	"1 Gemcutter's Promise": {"base": "Gemcutter's Promise", "class": "Divination Card", "type": "divination high"},
	"1 Her Mask": {"base": "Her Mask", "class": "Divination Card", "type": "divination high"},
	"1 Hubris": {"base": "Hubris", "class": "Divination Card", "type": "divination high"},
	"1 Jack in the Box": {"base": "Jack in the Box", "class": "Divination Card", "type": "divination high"},
	"1 Rain of Chaos": {"base": "Rain of Chaos", "class": "Divination Card", "type": "divination high"},
	"1 Scholar of the Seas": {"base": "Scholar of the Seas", "class": "Divination Card", "type": "divination high"},
	"1 Shard of Fate": {"base": "Shard of Fate", "class": "Divination Card", "type": "divination high"},
	"1 The Battle Born": {"base": "The Battle Born", "class": "Divination Card", "type": "divination high"},
	"1 The Betrayal": {"base": "The Betrayal", "class": "Divination Card", "type": "divination high"},
	"1 The Catalyst": {"base": "The Catalyst", "class": "Divination Card", "type": "divination high"},
	"1 The Doppelganger": {"base": "The Doppelganger", "class": "Divination Card", "type": "divination high"},
	"1 The Encroaching Darkness": {"base": "The Encroaching Darkness", "class": "Divination Card", "type": "divination high"},
	"1 The Feast": {"base": "The Feast", "class": "Divination Card", "type": "divination high"},
	"1 The Fletcher": {"base": "The Fletcher", "class": "Divination Card", "type": "divination high"},
	"1 The Flora's Gift": {"base": "The Flora's Gift", "class": "Divination Card", "type": "divination high"},
	"1 The Fox": {"base": "The Fox", "class": "Divination Card", "type": "divination high"},
	"1 The Gambler": {"base": "The Gambler", "class": "Divination Card", "type": "divination high"},
	"1 The Gemcutter": {"base": "The Gemcutter", "class": "Divination Card", "type": "divination high"},
	"1 The Inventor": {"base": "The Inventor", "class": "Divination Card", "type": "divination high"},
	"1 The Lich": {"base": "The Lich", "class": "Divination Card", "type": "divination high"},
	"1 The Lover": {"base": "The Lover", "class": "Divination Card", "type": "divination high"},
	"1 The Lunaris Priestess": {"base": "The Lunaris Priestess", "class": "Divination Card", "type": "divination high"},
	"1 The Poet": {"base": "The Poet", "class": "Divination Card", "type": "divination high"},
	"1 The Summoner": {"base": "The Summoner", "class": "Divination Card", "type": "divination high"},
	"1 The Survivalist": {"base": "The Survivalist", "class": "Divination Card", "type": "divination high"},
	"1 The Throne": {"base": "The Throne", "class": "Divination Card", "type": "divination high"},
	"1 The Tower": {"base": "The Tower", "class": "Divination Card", "type": "divination high"},
	"1 The Traitor": {"base": "The Traitor", "class": "Divination Card", "type": "divination high"},
	"1 The Warden": {"base": "The Warden", "class": "Divination Card", "type": "divination high"},
	"1 The Web": {"base": "The Web", "class": "Divination Card", "type": "divination high"},
	"1 The Wolf's Shadow": {"base": "The Wolf's Shadow", "class": "Divination Card", "type": "divination high"},
	"1 The Wrath": {"base": "The Wrath", "class": "Divination Card", "type": "divination high"},
	"2 Thunderous Skies": {"base": "Thunderous Skies", "class": "Divination Card", "type": "divination low"},
	"2 The Scholar": {"base": "The Scholar", "class": "Divination Card", "type": "divination low"},
	"7 A Mother's Parting Gift": {"base": "A Mother's Parting Gift", "class": "Divination Card", "type": "hide"},
	"7 The Carrion Crow": {"base": "The Carrion Crow", "class": "Divination Card", "type": "hide"},
	"7 The Rabid Rhoa": {"base": "The Rabid Rhoa", "class": "Divination Card", "type": "hide"},
	"7 The King's Blade": {"base": "The King's Blade", "class": "Divination Card", "type": "hide"},
	"7 The Inoculated": {"base": "The Inoculated", "class": "Divination Card", "type": "hide"},
	"7 Turn the Other Cheek": {"base": "Turn the Other Cheek", "class": "Divination Card", "type": "hide"},
	"9 Other uniques": {"class": "Divination Card", "type": "divination normal"}
}
