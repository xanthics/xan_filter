#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 12/14/2016(m/d/y) 10:36:54 UTC from "Hardcore" data
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
	"000 The Wolf's Shadow": {"base": "The Wolf's Shadow", "class": "Divination Card", "type": "divination very high"},
	"001 The Dragon's Heart": {"base": "The Dragon's Heart", "class": "Divination Card", "type": "divination very high"},
	"002 Last Hope": {"base": "Last Hope", "class": "Divination Card", "type": "divination high"},
	"003 Glimmer of Hope": {"base": "Glimmer of Hope", "class": "Divination Card", "type": "divination high"},
	"1 Abandoned Wealth": {"base": "Abandoned Wealth", "class": "Divination Card", "type": "divination very high"},
	"1 Bowyer's Dream": {"base": "Bowyer's Dream", "class": "Divination Card", "type": "divination very high"},
	"1 Heterochromia": {"base": "Heterochromia", "class": "Divination Card", "type": "divination very high"},
	"1 House of Mirrors": {"base": "House of Mirrors", "class": "Divination Card", "type": "divination very high"},
	"1 Hunter's Reward": {"base": "Hunter's Reward", "class": "Divination Card", "type": "divination very high"},
	"1 Lucky Deck": {"base": "Lucky Deck", "class": "Divination Card", "type": "divination very high"},
	"1 Lysah's Respite": {"base": "Lysah's Respite", "class": "Divination Card", "type": "divination very high"},
	"1 Mawr Blaidd": {"base": "Mawr Blaidd", "class": "Divination Card", "type": "divination very high"},
	"1 Pride Before the Fall": {"base": "Pride Before the Fall", "class": "Divination Card", "type": "divination very high"},
	"1 The Aesthete": {"base": "The Aesthete", "class": "Divination Card", "type": "divination very high"},
	"1 The Artist": {"base": "The Artist", "class": "Divination Card", "type": "divination very high"},
	"1 The Brittle Emperor": {"base": "The Brittle Emperor", "class": "Divination Card", "type": "divination very high"},
	"1 The Celestial Justicar": {"base": "The Celestial Justicar", "class": "Divination Card", "type": "divination very high"},
	"1 The Cursed King": {"base": "The Cursed King", "class": "Divination Card", "type": "divination very high"},
	"1 The Dapper Prodigy": {"base": "The Dapper Prodigy", "class": "Divination Card", "type": "divination very high"},
	"1 The Dark Mage": {"base": "The Dark Mage", "class": "Divination Card", "type": "divination very high"},
	"1 The Doctor": {"base": "The Doctor", "class": "Divination Card", "type": "divination very high"},
	"1 The Enlightened": {"base": "The Enlightened", "class": "Divination Card", "type": "divination very high"},
	"1 The Ethereal": {"base": "The Ethereal", "class": "Divination Card", "type": "divination very high"},
	"1 The Fiend": {"base": "The Fiend", "class": "Divination Card", "type": "divination very high"},
	"1 The Formless Sea": {"base": "The Formless Sea", "class": "Divination Card", "type": "divination very high"},
	"1 The Fox": {"base": "The Fox", "class": "Divination Card", "type": "divination very high"},
	"1 The Harvester": {"base": "The Harvester", "class": "Divination Card", "type": "divination very high"},
	"1 The Hunger": {"base": "The Hunger", "class": "Divination Card", "type": "divination very high"},
	"1 The Immortal": {"base": "The Immortal", "class": "Divination Card", "type": "divination very high"},
	"1 The King's Heart": {"base": "The King's Heart", "class": "Divination Card", "type": "divination very high"},
	"1 The Last One Standing": {"base": "The Last One Standing", "class": "Divination Card", "type": "divination very high"},
	"1 The Offering": {"base": "The Offering", "class": "Divination Card", "type": "divination very high"},
	"1 The One With All": {"base": "The One With All", "class": "Divination Card", "type": "divination very high"},
	"1 The Queen": {"base": "The Queen", "class": "Divination Card", "type": "divination very high"},
	"1 The Scavenger": {"base": "The Scavenger", "class": "Divination Card", "type": "divination very high"},
	"1 The Sephirot": {"base": "The Sephirot", "class": "Divination Card", "type": "divination very high"},
	"1 The Stormcaller": {"base": "The Stormcaller", "class": "Divination Card", "type": "divination very high"},
	"1 The Surveyor": {"base": "The Surveyor", "class": "Divination Card", "type": "divination very high"},
	"1 The Thaumaturgist": {"base": "The Thaumaturgist", "class": "Divination Card", "type": "divination very high"},
	"1 The Valkyrie": {"base": "The Valkyrie", "class": "Divination Card", "type": "divination very high"},
	"1 The Vast": {"base": "The Vast", "class": "Divination Card", "type": "divination very high"},
	"1 The Void": {"base": "The Void", "class": "Divination Card", "type": "divination very high"},
	"1 The Warlord": {"base": "The Warlord", "class": "Divination Card", "type": "divination very high"},
	"1 The Wolf": {"base": "The Wolf", "class": "Divination Card", "type": "divination very high"},
	"1 Time-Lost Relic": {"base": "Time-Lost Relic", "class": "Divination Card", "type": "divination very high"},
	"1 Wealth and Power": {"base": "Wealth and Power", "class": "Divination Card", "type": "divination very high"},
	"2 Assassin's Favour": {"base": "Assassin's Favour", "class": "Divination Card", "type": "divination high"},
	"2 Blind Venture": {"base": "Blind Venture", "class": "Divination Card", "type": "divination high"},
	"2 Chaotic Disposition": {"base": "Chaotic Disposition", "class": "Divination Card", "type": "divination high"},
	"2 Dialla's Subjugation": {"base": "Dialla's Subjugation", "class": "Divination Card", "type": "divination high"},
	"2 Dying Anguish": {"base": "Dying Anguish", "class": "Divination Card", "type": "divination high"},
	"2 Earth Drinker": {"base": "Earth Drinker", "class": "Divination Card", "type": "divination high"},
	"2 Emperor of Purity": {"base": "Emperor of Purity", "class": "Divination Card", "type": "divination high"},
	"2 Hope": {"base": "Hope", "class": "Divination Card", "type": "divination high"},
	"2 Humility": {"base": "Humility", "class": "Divination Card", "type": "divination high"},
	"2 Jack in the Box": {"base": "Jack in the Box", "class": "Divination Card", "type": "divination high"},
	"2 Lost Worlds": {"base": "Lost Worlds", "class": "Divination Card", "type": "divination high"},
	"2 Lucky Connections": {"base": "Lucky Connections", "class": "Divination Card", "type": "divination high"},
	"2 Merciless Armament": {"base": "Merciless Armament", "class": "Divination Card", "type": "divination high"},
	"2 The Arena Champion": {"base": "The Arena Champion", "class": "Divination Card", "type": "divination high"},
	"2 The Avenger": {"base": "The Avenger", "class": "Divination Card", "type": "divination high"},
	"2 The Body": {"base": "The Body", "class": "Divination Card", "type": "divination high"},
	"2 The Calling": {"base": "The Calling", "class": "Divination Card", "type": "divination high"},
	"2 The Cartographer": {"base": "The Cartographer", "class": "Divination Card", "type": "divination high"},
	"2 The Chains that Bind": {"base": "The Chains that Bind", "class": "Divination Card", "type": "divination high"},
	"2 The Demoness": {"base": "The Demoness", "class": "Divination Card", "type": "divination high"},
	"2 The Dragon": {"base": "The Dragon", "class": "Divination Card", "type": "divination high"},
	"2 The Gladiator": {"base": "The Gladiator", "class": "Divination Card", "type": "divination high"},
	"2 The Hoarder": {"base": "The Hoarder", "class": "Divination Card", "type": "divination high"},
	"2 The Incantation": {"base": "The Incantation", "class": "Divination Card", "type": "divination high"},
	"2 The Inventor": {"base": "The Inventor", "class": "Divination Card", "type": "divination high"},
	"2 The Jester": {"base": "The Jester", "class": "Divination Card", "type": "divination high"},
	"2 The Penitent": {"base": "The Penitent", "class": "Divination Card", "type": "divination high"},
	"2 The Risk": {"base": "The Risk", "class": "Divination Card", "type": "divination high"},
	"2 The Road to Power": {"base": "The Road to Power", "class": "Divination Card", "type": "divination high"},
	"2 The Soul": {"base": "The Soul", "class": "Divination Card", "type": "divination high"},
	"2 The Spoiled Prince": {"base": "The Spoiled Prince", "class": "Divination Card", "type": "divination high"},
	"2 The Summoner": {"base": "The Summoner", "class": "Divination Card", "type": "divination high"},
	"2 The Tower": {"base": "The Tower", "class": "Divination Card", "type": "divination high"},
	"2 The Trial": {"base": "The Trial", "class": "Divination Card", "type": "divination high"},
	"2 The Tyrant": {"base": "The Tyrant", "class": "Divination Card", "type": "divination high"},
	"2 The Union": {"base": "The Union", "class": "Divination Card", "type": "divination high"},
	"2 The Wind": {"base": "The Wind", "class": "Divination Card", "type": "divination high"},
	"3 Cartographer's Delight": {"base": "Cartographer's Delight", "class": "Divination Card", "type": "divination low"},
	"3 Destined to Crumble": {"base": "Destined to Crumble", "class": "Divination Card", "type": "divination low"},
	"3 Rain of Chaos": {"base": "Rain of Chaos", "class": "Divination Card", "type": "divination low"},
	"3 Shard of Fate": {"base": "Shard of Fate", "class": "Divination Card", "type": "divination low"},
	"3 The Catalyst": {"base": "The Catalyst", "class": "Divination Card", "type": "divination low"},
	"3 The Fletcher": {"base": "The Fletcher", "class": "Divination Card", "type": "divination low"},
	"3 The Hermit": {"base": "The Hermit", "class": "Divination Card", "type": "divination low"},
	"3 The Lunaris Priestess": {"base": "The Lunaris Priestess", "class": "Divination Card", "type": "divination low"},
	"3 The Oath": {"base": "The Oath", "class": "Divination Card", "type": "divination low"},
	"3 The Rabid Rhoa": {"base": "The Rabid Rhoa", "class": "Divination Card", "type": "divination low"},
	"3 The Scholar": {"base": "The Scholar", "class": "Divination Card", "type": "divination low"},
	"3 The Siren": {"base": "The Siren", "class": "Divination Card", "type": "divination low"},
	"3 The Surgeon": {"base": "The Surgeon", "class": "Divination Card", "type": "divination low"},
	"3 The Twins": {"base": "The Twins", "class": "Divination Card", "type": "divination low"},
	"3 Thunderous Skies": {"base": "Thunderous Skies", "class": "Divination Card", "type": "divination low"},
	"7 The Carrion Crow": {"base": "The Carrion Crow", "class": "Divination Card", "type": "hide"},
	"7 The Inoculated": {"base": "The Inoculated", "class": "Divination Card", "type": "hide"},
	"7 The King's Blade": {"base": "The King's Blade", "class": "Divination Card", "type": "hide"},
	"7 Turn the Other Cheek": {"base": "Turn the Other Cheek", "class": "Divination Card", "type": "hide"},
	"9 Other uniques": {"class": "Divination Card", "type": "divination normal"}
}
