#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 10/03/2016(m/d/y) 21:43:16 UTC from "Hardcore Essence" data
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
	"0 Bowyer's Dream": {"base": "Bowyer's Dream", "class": "Divination Card", "type": "divination very high"},
	"0 Chaotic Disposition": {"base": "Chaotic Disposition", "class": "Divination Card", "type": "divination very high"},
	"0 Emperor of Purity": {"base": "Emperor of Purity", "class": "Divination Card", "type": "divination very high"},
	"0 Heterochromia": {"base": "Heterochromia", "class": "Divination Card", "type": "divination very high"},
	"0 House of Mirrors": {"base": "House of Mirrors", "class": "Divination Card", "type": "divination very high"},
	"0 Hunter's Reward": {"base": "Hunter's Reward", "class": "Divination Card", "type": "divination very high"},
	"0 Last Hope": {"base": "Last Hope", "class": "Divination Card", "type": "divination very high"},
	"0 Mawr Blaidd": {"base": "Mawr Blaidd", "class": "Divination Card", "type": "divination very high"},
	"0 Pride Before the Fall": {"base": "Pride Before the Fall", "class": "Divination Card", "type": "divination very high"},
	"0 The Artist": {"base": "The Artist", "class": "Divination Card", "type": "divination very high"},
	"0 The Brittle Emperor": {"base": "The Brittle Emperor", "class": "Divination Card", "type": "divination very high"},
	"0 The Celestial Justicar": {"base": "The Celestial Justicar", "class": "Divination Card", "type": "divination very high"},
	"0 The Cursed King": {"base": "The Cursed King", "class": "Divination Card", "type": "divination very high"},
	"0 The Dark Mage": {"base": "The Dark Mage", "class": "Divination Card", "type": "divination very high"},
	"0 The Doctor": {"base": "The Doctor", "class": "Divination Card", "type": "divination very high"},
	"0 The Dragon's Heart": {"base": "The Dragon's Heart", "class": "Divination Card", "type": "divination very high"},
	"0 The Enlightened": {"base": "The Enlightened", "class": "Divination Card", "type": "divination very high"},
	"0 The Ethereal": {"base": "The Ethereal", "class": "Divination Card", "type": "divination very high"},
	"0 The Fiend": {"base": "The Fiend", "class": "Divination Card", "type": "divination very high"},
	"0 The Formless Sea": {"base": "The Formless Sea", "class": "Divination Card", "type": "divination very high"},
	"0 The Harvester": {"base": "The Harvester", "class": "Divination Card", "type": "divination very high"},
	"0 The Hunger": {"base": "The Hunger", "class": "Divination Card", "type": "divination very high"},
	"0 The Immortal": {"base": "The Immortal", "class": "Divination Card", "type": "divination very high"},
	"0 The King's Heart": {"base": "The King's Heart", "class": "Divination Card", "type": "divination very high"},
	"0 The Last One Standing": {"base": "The Last One Standing", "class": "Divination Card", "type": "divination very high"},
	"0 The Offering": {"base": "The Offering", "class": "Divination Card", "type": "divination very high"},
	"0 The Queen": {"base": "The Queen", "class": "Divination Card", "type": "divination very high"},
	"0 The Thaumaturgist": {"base": "The Thaumaturgist", "class": "Divination Card", "type": "divination very high"},
	"0 The Vast": {"base": "The Vast", "class": "Divination Card", "type": "divination very high"},
	"0 The Warlord": {"base": "The Warlord", "class": "Divination Card", "type": "divination very high"},
	"0 Time-Lost Relic": {"base": "Time-Lost Relic", "class": "Divination Card", "type": "divination very high"},
	"0 Wealth and Power": {"base": "Wealth and Power", "class": "Divination Card", "type": "divination very high"},
	"1 Dialla's Subjugation": {"base": "Dialla's Subjugation", "class": "Divination Card", "type": "divination high"},
	"1 Earth Drinker": {"base": "Earth Drinker", "class": "Divination Card", "type": "divination high"},
	"1 Glimmer of Hope": {"base": "Glimmer of Hope", "class": "Divination Card", "type": "divination high"},
	"1 Hope": {"base": "Hope", "class": "Divination Card", "type": "divination high"},
	"1 Humility": {"base": "Humility", "class": "Divination Card", "type": "divination high"},
	"1 Jack in the Box": {"base": "Jack in the Box", "class": "Divination Card", "type": "divination high"},
	"1 Lost Worlds": {"base": "Lost Worlds", "class": "Divination Card", "type": "divination high"},
	"1 Lucky Deck": {"base": "Lucky Deck", "class": "Divination Card", "type": "divination high"},
	"1 Lysah's Respite": {"base": "Lysah's Respite", "class": "Divination Card", "type": "divination high"},
	"1 Merciless Armament": {"base": "Merciless Armament", "class": "Divination Card", "type": "divination high"},
	"1 The Aesthete": {"base": "The Aesthete", "class": "Divination Card", "type": "divination high"},
	"1 The Arena Champion": {"base": "The Arena Champion", "class": "Divination Card", "type": "divination high"},
	"1 The Avenger": {"base": "The Avenger", "class": "Divination Card", "type": "divination high"},
	"1 The Body": {"base": "The Body", "class": "Divination Card", "type": "divination high"},
	"1 The Calling": {"base": "The Calling", "class": "Divination Card", "type": "divination high"},
	"1 The Cartographer": {"base": "The Cartographer", "class": "Divination Card", "type": "divination high"},
	"1 The Chains that Bind": {"base": "The Chains that Bind", "class": "Divination Card", "type": "divination high"},
	"1 The Dapper Prodigy": {"base": "The Dapper Prodigy", "class": "Divination Card", "type": "divination high"},
	"1 The Fletcher": {"base": "The Fletcher", "class": "Divination Card", "type": "divination high"},
	"1 The Fox": {"base": "The Fox", "class": "Divination Card", "type": "divination high"},
	"1 The Gladiator": {"base": "The Gladiator", "class": "Divination Card", "type": "divination high"},
	"1 The Hoarder": {"base": "The Hoarder", "class": "Divination Card", "type": "divination high"},
	"1 The Penitent": {"base": "The Penitent", "class": "Divination Card", "type": "divination high"},
	"1 The Risk": {"base": "The Risk", "class": "Divination Card", "type": "divination high"},
	"1 The Road to Power": {"base": "The Road to Power", "class": "Divination Card", "type": "divination high"},
	"1 The Scavenger": {"base": "The Scavenger", "class": "Divination Card", "type": "divination high"},
	"1 The Sephirot": {"base": "The Sephirot", "class": "Divination Card", "type": "divination high"},
	"1 The Soul": {"base": "The Soul", "class": "Divination Card", "type": "divination high"},
	"1 The Stormcaller": {"base": "The Stormcaller", "class": "Divination Card", "type": "divination high"},
	"1 The Surveyor": {"base": "The Surveyor", "class": "Divination Card", "type": "divination high"},
	"1 The Trial": {"base": "The Trial", "class": "Divination Card", "type": "divination high"},
	"1 The Tyrant": {"base": "The Tyrant", "class": "Divination Card", "type": "divination high"},
	"1 The Valkyrie": {"base": "The Valkyrie", "class": "Divination Card", "type": "divination high"},
	"1 The Void": {"base": "The Void", "class": "Divination Card", "type": "divination high"},
	"1 The Wolf": {"base": "The Wolf", "class": "Divination Card", "type": "divination high"},
	"1 Treasure Hunter": {"base": "Treasure Hunter", "class": "Divination Card", "type": "divination high"},
	"1 Vinia's Token": {"base": "Vinia's Token", "class": "Divination Card", "type": "divination high"},
	"2 A Mother's Parting Gift": {"base": "A Mother's Parting Gift", "class": "Divination Card", "type": "divination low"},
	"2 Anarchy's Price": {"base": "Anarchy's Price", "class": "Divination Card", "type": "divination low"},
	"2 Birth of the Three": {"base": "Birth of the Three", "class": "Divination Card", "type": "divination low"},
	"2 Cartographer's Delight": {"base": "Cartographer's Delight", "class": "Divination Card", "type": "divination low"},
	"2 Destined to Crumble": {"base": "Destined to Crumble", "class": "Divination Card", "type": "divination low"},
	"2 Doedre's Madness": {"base": "Doedre's Madness", "class": "Divination Card", "type": "divination low"},
	"2 Dying Anguish": {"base": "Dying Anguish", "class": "Divination Card", "type": "divination low"},
	"2 Her Mask": {"base": "Her Mask", "class": "Divination Card", "type": "divination low"},
	"2 Lantador's Lost Love": {"base": "Lantador's Lost Love", "class": "Divination Card", "type": "divination low"},
	"2 Loyalty": {"base": "Loyalty", "class": "Divination Card", "type": "divination low"},
	"2 Prosperity": {"base": "Prosperity", "class": "Divination Card", "type": "divination low"},
	"2 Rain of Chaos": {"base": "Rain of Chaos", "class": "Divination Card", "type": "divination low"},
	"2 The Betrayal": {"base": "The Betrayal", "class": "Divination Card", "type": "divination low"},
	"2 The Catalyst": {"base": "The Catalyst", "class": "Divination Card", "type": "divination low"},
	"2 The Dragon": {"base": "The Dragon", "class": "Divination Card", "type": "divination low"},
	"2 The Endurance": {"base": "The Endurance", "class": "Divination Card", "type": "divination low"},
	"2 The Feast": {"base": "The Feast", "class": "Divination Card", "type": "divination low"},
	"2 The Flora's Gift": {"base": "The Flora's Gift", "class": "Divination Card", "type": "divination low"},
	"2 The Gambler": {"base": "The Gambler", "class": "Divination Card", "type": "divination low"},
	"2 The Gemcutter": {"base": "The Gemcutter", "class": "Divination Card", "type": "divination low"},
	"2 The Hermit": {"base": "The Hermit", "class": "Divination Card", "type": "divination low"},
	"2 The Lich": {"base": "The Lich", "class": "Divination Card", "type": "divination low"},
	"2 The Lion": {"base": "The Lion", "class": "Divination Card", "type": "divination low"},
	"2 The Lunaris Priestess": {"base": "The Lunaris Priestess", "class": "Divination Card", "type": "divination low"},
	"2 The Metalsmith's Gift": {"base": "The Metalsmith's Gift", "class": "Divination Card", "type": "divination low"},
	"2 The Oath": {"base": "The Oath", "class": "Divination Card", "type": "divination low"},
	"2 The Rabid Rhoa": {"base": "The Rabid Rhoa", "class": "Divination Card", "type": "divination low"},
	"2 The Scarred Meadow": {"base": "The Scarred Meadow", "class": "Divination Card", "type": "divination low"},
	"2 The Scholar": {"base": "The Scholar", "class": "Divination Card", "type": "divination low"},
	"2 The Sun": {"base": "The Sun", "class": "Divination Card", "type": "divination low"},
	"2 The Surgeon": {"base": "The Surgeon", "class": "Divination Card", "type": "divination low"},
	"2 The Twins": {"base": "The Twins", "class": "Divination Card", "type": "divination low"},
	"2 The Warden": {"base": "The Warden", "class": "Divination Card", "type": "divination low"},
	"2 The Web": {"base": "The Web", "class": "Divination Card", "type": "divination low"},
	"2 The Wolf's Shadow": {"base": "The Wolf's Shadow", "class": "Divination Card", "type": "divination low"},
	"2 Three Faces in the Dark": {"base": "Three Faces in the Dark", "class": "Divination Card", "type": "divination low"},
	"2 Thunderous Skies": {"base": "Thunderous Skies", "class": "Divination Card", "type": "divination low"},
	"7 The Carrion Crow": {"base": "The Carrion Crow", "class": "Divination Card", "type": "hide"},
	"7 The Inoculated": {"base": "The Inoculated", "class": "Divination Card", "type": "hide"},
	"7 The King's Blade": {"base": "The King's Blade", "class": "Divination Card", "type": "hide"},
	"7 Turn the Other Cheek": {"base": "Turn the Other Cheek", "class": "Divination Card", "type": "hide"},
	"9 Other uniques": {"class": "Divination Card", "type": "divination normal"}
}
