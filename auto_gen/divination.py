#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 09/05/2016(m/d/y) 00:16:15 UTC from "Standard" data
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
	"0 Abandoned Wealth": {"base": "Abandoned Wealth", "class": "Divination Card", "type": "divination very high"},
	"0 Anarchy's Price": {"base": "Anarchy's Price", "class": "Divination Card", "type": "divination very high"},
	"0 Audacity": {"base": "Audacity", "class": "Divination Card", "type": "divination very high"},
	"0 Bowyer's Dream": {"base": "Bowyer's Dream", "class": "Divination Card", "type": "divination very high"},
	"0 Chaotic Disposition": {"base": "Chaotic Disposition", "class": "Divination Card", "type": "divination very high"},
	"0 Dialla's Subjugation": {"base": "Dialla's Subjugation", "class": "Divination Card", "type": "divination very high"},
	"0 Emperor of Purity": {"base": "Emperor of Purity", "class": "Divination Card", "type": "divination very high"},
	"0 Gemcutter's Promise": {"base": "Gemcutter's Promise", "class": "Divination Card", "type": "divination very high"},
	"0 Glimmer of Hope": {"base": "Glimmer of Hope", "class": "Divination Card", "type": "divination very high"},
	"0 Heterochromia": {"base": "Heterochromia", "class": "Divination Card", "type": "divination very high"},
	"0 Hope": {"base": "Hope", "class": "Divination Card", "type": "divination very high"},
	"0 House of Mirrors": {"base": "House of Mirrors", "class": "Divination Card", "type": "divination very high"},
	"0 Hunter's Reward": {"base": "Hunter's Reward", "class": "Divination Card", "type": "divination very high"},
	"0 Jack in the Box": {"base": "Jack in the Box", "class": "Divination Card", "type": "divination very high"},
	"0 Last Hope": {"base": "Last Hope", "class": "Divination Card", "type": "divination very high"},
	"0 Lost Worlds": {"base": "Lost Worlds", "class": "Divination Card", "type": "divination very high"},
	"0 Lucky Deck": {"base": "Lucky Deck", "class": "Divination Card", "type": "divination very high"},
	"0 Lysah's Respite": {"base": "Lysah's Respite", "class": "Divination Card", "type": "divination very high"},
	"0 Merciless Armament": {"base": "Merciless Armament", "class": "Divination Card", "type": "divination very high"},
	"0 Pride Before the Fall": {"base": "Pride Before the Fall", "class": "Divination Card", "type": "divination very high"},
	"0 The Aesthete": {"base": "The Aesthete", "class": "Divination Card", "type": "divination very high"},
	"0 The Arena Champion": {"base": "The Arena Champion", "class": "Divination Card", "type": "divination very high"},
	"0 The Artist": {"base": "The Artist", "class": "Divination Card", "type": "divination very high"},
	"0 The Avenger": {"base": "The Avenger", "class": "Divination Card", "type": "divination very high"},
	"0 The Body": {"base": "The Body", "class": "Divination Card", "type": "divination very high"},
	"0 The Brittle Emperor": {"base": "The Brittle Emperor", "class": "Divination Card", "type": "divination very high"},
	"0 The Calling": {"base": "The Calling", "class": "Divination Card", "type": "divination very high"},
	"0 The Cataclysm": {"base": "The Cataclysm", "class": "Divination Card", "type": "divination very high"},
	"0 The Celestial Justicar": {"base": "The Celestial Justicar", "class": "Divination Card", "type": "divination very high"},
	"0 The Chains that Bind": {"base": "The Chains that Bind", "class": "Divination Card", "type": "divination very high"},
	"0 The Cursed King": {"base": "The Cursed King", "class": "Divination Card", "type": "divination very high"},
	"0 The Dapper Prodigy": {"base": "The Dapper Prodigy", "class": "Divination Card", "type": "divination very high"},
	"0 The Dark Mage": {"base": "The Dark Mage", "class": "Divination Card", "type": "divination very high"},
	"0 The Doctor": {"base": "The Doctor", "class": "Divination Card", "type": "divination very high"},
	"0 The Dragon's Heart": {"base": "The Dragon's Heart", "class": "Divination Card", "type": "divination very high"},
	"0 The Enlightened": {"base": "The Enlightened", "class": "Divination Card", "type": "divination very high"},
	"0 The Ethereal": {"base": "The Ethereal", "class": "Divination Card", "type": "divination very high"},
	"0 The Fiend": {"base": "The Fiend", "class": "Divination Card", "type": "divination very high"},
	"0 The Fletcher": {"base": "The Fletcher", "class": "Divination Card", "type": "divination very high"},
	"0 The Formless Sea": {"base": "The Formless Sea", "class": "Divination Card", "type": "divination very high"},
	"0 The Harvester": {"base": "The Harvester", "class": "Divination Card", "type": "divination very high"},
	"0 The Hunger": {"base": "The Hunger", "class": "Divination Card", "type": "divination very high"},
	"0 The Immortal": {"base": "The Immortal", "class": "Divination Card", "type": "divination very high"},
	"0 The Incantation": {"base": "The Incantation", "class": "Divination Card", "type": "divination very high"},
	"0 The Inventor": {"base": "The Inventor", "class": "Divination Card", "type": "divination very high"},
	"0 The King's Heart": {"base": "The King's Heart", "class": "Divination Card", "type": "divination very high"},
	"0 The Last One Standing": {"base": "The Last One Standing", "class": "Divination Card", "type": "divination very high"},
	"0 The Lord in Black": {"base": "The Lord in Black", "class": "Divination Card", "type": "divination very high"},
	"0 The Offering": {"base": "The Offering", "class": "Divination Card", "type": "divination very high"},
	"0 The Queen": {"base": "The Queen", "class": "Divination Card", "type": "divination very high"},
	"0 The Risk": {"base": "The Risk", "class": "Divination Card", "type": "divination very high"},
	"0 The Road to Power": {"base": "The Road to Power", "class": "Divination Card", "type": "divination very high"},
	"0 The Scavenger": {"base": "The Scavenger", "class": "Divination Card", "type": "divination very high"},
	"0 The Sephirot": {"base": "The Sephirot", "class": "Divination Card", "type": "divination very high"},
	"0 The Spoiled Prince": {"base": "The Spoiled Prince", "class": "Divination Card", "type": "divination very high"},
	"0 The Surveyor": {"base": "The Surveyor", "class": "Divination Card", "type": "divination very high"},
	"0 The Survivalist": {"base": "The Survivalist", "class": "Divination Card", "type": "divination very high"},
	"0 The Thaumaturgist": {"base": "The Thaumaturgist", "class": "Divination Card", "type": "divination very high"},
	"0 The Trial": {"base": "The Trial", "class": "Divination Card", "type": "divination very high"},
	"0 The Tyrant": {"base": "The Tyrant", "class": "Divination Card", "type": "divination very high"},
	"0 The Valkyrie": {"base": "The Valkyrie", "class": "Divination Card", "type": "divination very high"},
	"0 The Vast": {"base": "The Vast", "class": "Divination Card", "type": "divination very high"},
	"0 The Visionary": {"base": "The Visionary", "class": "Divination Card", "type": "divination very high"},
	"0 The Void": {"base": "The Void", "class": "Divination Card", "type": "divination very high"},
	"0 The Warlord": {"base": "The Warlord", "class": "Divination Card", "type": "divination very high"},
	"0 The Wolf": {"base": "The Wolf", "class": "Divination Card", "type": "divination very high"},
	"0 Time-Lost Relic": {"base": "Time-Lost Relic", "class": "Divination Card", "type": "divination very high"},
	"0 Wealth and Power": {"base": "Wealth and Power", "class": "Divination Card", "type": "divination very high"},
	"1 Assassin's Favour": {"base": "Assassin's Favour", "class": "Divination Card", "type": "divination high"},
	"1 Birth of the Three": {"base": "Birth of the Three", "class": "Divination Card", "type": "divination high"},
	"1 Blind Venture": {"base": "Blind Venture", "class": "Divination Card", "type": "divination high"},
	"1 Boundless Realms": {"base": "Boundless Realms", "class": "Divination Card", "type": "divination high"},
	"1 Earth Drinker": {"base": "Earth Drinker", "class": "Divination Card", "type": "divination high"},
	"1 Emperor's Luck": {"base": "Emperor's Luck", "class": "Divination Card", "type": "divination high"},
	"1 Grave Knowledge": {"base": "Grave Knowledge", "class": "Divination Card", "type": "divination high"},
	"1 Hubris": {"base": "Hubris", "class": "Divination Card", "type": "divination high"},
	"1 Humility": {"base": "Humility", "class": "Divination Card", "type": "divination high"},
	"1 Hunter's Resolve": {"base": "Hunter's Resolve", "class": "Divination Card", "type": "divination high"},
	"1 Light and Truth": {"base": "Light and Truth", "class": "Divination Card", "type": "divination high"},
	"1 Lucky Connections": {"base": "Lucky Connections", "class": "Divination Card", "type": "divination high"},
	"1 Rain Tempter": {"base": "Rain Tempter", "class": "Divination Card", "type": "divination high"},
	"1 Rats": {"base": "Rats", "class": "Divination Card", "type": "divination high"},
	"1 Scholar of the Seas": {"base": "Scholar of the Seas", "class": "Divination Card", "type": "divination high"},
	"1 Shard of Fate": {"base": "Shard of Fate", "class": "Divination Card", "type": "divination high"},
	"1 The Battle Born": {"base": "The Battle Born", "class": "Divination Card", "type": "divination high"},
	"1 The Betrayal": {"base": "The Betrayal", "class": "Divination Card", "type": "divination high"},
	"1 The Cartographer": {"base": "The Cartographer", "class": "Divination Card", "type": "divination high"},
	"1 The Conduit": {"base": "The Conduit", "class": "Divination Card", "type": "divination high"},
	"1 The Demoness": {"base": "The Demoness", "class": "Divination Card", "type": "divination high"},
	"1 The Doppelganger": {"base": "The Doppelganger", "class": "Divination Card", "type": "divination high"},
	"1 The Drunken Aristocrat": {"base": "The Drunken Aristocrat", "class": "Divination Card", "type": "divination high"},
	"1 The Encroaching Darkness": {"base": "The Encroaching Darkness", "class": "Divination Card", "type": "divination high"},
	"1 The Explorer": {"base": "The Explorer", "class": "Divination Card", "type": "divination high"},
	"1 The Fox": {"base": "The Fox", "class": "Divination Card", "type": "divination high"},
	"1 The Gladiator": {"base": "The Gladiator", "class": "Divination Card", "type": "divination high"},
	"1 The Hoarder": {"base": "The Hoarder", "class": "Divination Card", "type": "divination high"},
	"1 The Jester": {"base": "The Jester", "class": "Divination Card", "type": "divination high"},
	"1 The Mercenary": {"base": "The Mercenary", "class": "Divination Card", "type": "divination high"},
	"1 The One With All": {"base": "The One With All", "class": "Divination Card", "type": "divination high"},
	"1 The Pact": {"base": "The Pact", "class": "Divination Card", "type": "divination high"},
	"1 The Penitent": {"base": "The Penitent", "class": "Divination Card", "type": "divination high"},
	"1 The Poet": {"base": "The Poet", "class": "Divination Card", "type": "divination high"},
	"1 The Sigil": {"base": "The Sigil", "class": "Divination Card", "type": "divination high"},
	"1 The Siren": {"base": "The Siren", "class": "Divination Card", "type": "divination high"},
	"1 The Soul": {"base": "The Soul", "class": "Divination Card", "type": "divination high"},
	"1 The Stormcaller": {"base": "The Stormcaller", "class": "Divination Card", "type": "divination high"},
	"1 The Tower": {"base": "The Tower", "class": "Divination Card", "type": "divination high"},
	"1 The Traitor": {"base": "The Traitor", "class": "Divination Card", "type": "divination high"},
	"1 The Union": {"base": "The Union", "class": "Divination Card", "type": "divination high"},
	"1 The Watcher": {"base": "The Watcher", "class": "Divination Card", "type": "divination high"},
	"1 The Web": {"base": "The Web", "class": "Divination Card", "type": "divination high"},
	"1 The Wind": {"base": "The Wind", "class": "Divination Card", "type": "divination high"},
	"1 The Wrath": {"base": "The Wrath", "class": "Divination Card", "type": "divination high"},
	"1 Three Faces in the Dark": {"base": "Three Faces in the Dark", "class": "Divination Card", "type": "divination high"},
	"1 Tranquillity": {"base": "Tranquillity", "class": "Divination Card", "type": "divination high"},
	"1 Treasure Hunter": {"base": "Treasure Hunter", "class": "Divination Card", "type": "divination high"},
	"1 Vinia's Token": {"base": "Vinia's Token", "class": "Divination Card", "type": "divination high"},
	"1 Volatile Power": {"base": "Volatile Power", "class": "Divination Card", "type": "divination high"},
	"2 Destined to Crumble": {"base": "Destined to Crumble", "class": "Divination Card", "type": "divination low"},
	"2 The Rabid Rhoa": {"base": "The Rabid Rhoa", "class": "Divination Card", "type": "divination low"},
	"2 The Scholar": {"base": "The Scholar", "class": "Divination Card", "type": "divination low"},
	"2 The Surgeon": {"base": "The Surgeon", "class": "Divination Card", "type": "divination low"},
	"2 The Twins": {"base": "The Twins", "class": "Divination Card", "type": "divination low"},
	"2 Thunderous Skies": {"base": "Thunderous Skies", "class": "Divination Card", "type": "divination low"},
	"7 The Carrion Crow": {"base": "The Carrion Crow", "class": "Divination Card", "type": "hide"},
	"7 The Inoculated": {"base": "The Inoculated", "class": "Divination Card", "type": "hide"},
	"7 The King's Blade": {"base": "The King's Blade", "class": "Divination Card", "type": "hide"},
	"7 Turn the Other Cheek": {"base": "Turn the Other Cheek", "class": "Divination Card", "type": "hide"},
	"9 Other uniques": {"class": "Divination Card", "type": "divination normal"}
}
