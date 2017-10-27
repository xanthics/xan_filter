#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 10/27/2017(m/d/y) 08:12:17 UTC from "Standard" data

desc = "Divination Card"

# Base type : settings pair
items = {
	"000 The Wolf's Shadow": {"base": "The Wolf's Shadow", "class": "Divination Card", "type": "divination normal"},
	"001 The Dragon's Heart": {"base": "The Dragon's Heart", "class": "Divination Card", "type": "divination very high"},
	"002 Last Hope": {"base": "Last Hope", "class": "Divination Card", "type": "divination very high"},
	"003 Glimmer of Hope": {"base": "Glimmer of Hope", "class": "Divination Card", "type": "divination high"},
	"1 Abandoned Wealth": {"base": "Abandoned Wealth", "class": "Divination Card", "type": "divination very high"},
	"1 Bowyer's Dream": {"base": "Bowyer's Dream", "class": "Divination Card", "type": "divination very high"},
	"1 House of Mirrors": {"base": "House of Mirrors", "class": "Divination Card", "type": "divination very high"},
	"1 Hunter's Reward": {"base": "Hunter's Reward", "class": "Divination Card", "type": "divination very high"},
	"1 Mawr Blaidd": {"base": "Mawr Blaidd", "class": "Divination Card", "type": "divination very high"},
	"1 Pride Before the Fall": {"base": "Pride Before the Fall", "class": "Divination Card", "type": "divination very high"},
	"1 The Cartographer": {"base": "The Cartographer", "class": "Divination Card", "type": "divination very high"},
	"1 The Doctor": {"base": "The Doctor", "class": "Divination Card", "type": "divination very high"},
	"1 The Fiend": {"base": "The Fiend", "class": "Divination Card", "type": "divination very high"},
	"1 The Immortal": {"base": "The Immortal", "class": "Divination Card", "type": "divination very high"},
	"1 The King's Heart": {"base": "The King's Heart", "class": "Divination Card", "type": "divination very high"},
	"1 The Last One Standing": {"base": "The Last One Standing", "class": "Divination Card", "type": "divination very high"},
	"1 The Queen": {"base": "The Queen", "class": "Divination Card", "type": "divination very high"},
	"1 The Spark and the Flame": {"base": "The Spark and the Flame", "class": "Divination Card", "type": "divination very high"},
	"1 The Standoff": {"base": "The Standoff", "class": "Divination Card", "type": "divination very high"},
	"1 The Vast": {"base": "The Vast", "class": "Divination Card", "type": "divination very high"},
	"1 Wealth and Power": {"base": "Wealth and Power", "class": "Divination Card", "type": "divination very high"},
	"2 Atziri's Arsenal": {"base": "Atziri's Arsenal", "class": "Divination Card", "type": "divination high"},
	"2 Birth of the Three": {"base": "Birth of the Three", "class": "Divination Card", "type": "divination high"},
	"2 Boundless Realms": {"base": "Boundless Realms", "class": "Divination Card", "type": "divination high"},
	"2 Chaotic Disposition": {"base": "Chaotic Disposition", "class": "Divination Card", "type": "divination high"},
	"2 Emperor of Purity": {"base": "Emperor of Purity", "class": "Divination Card", "type": "divination high"},
	"2 Heterochromia": {"base": "Heterochromia", "class": "Divination Card", "type": "divination high"},
	"2 Hope": {"base": "Hope", "class": "Divination Card", "type": "divination high"},
	"2 Lingering Remnants": {"base": "Lingering Remnants", "class": "Divination Card", "type": "divination high"},
	"2 Lucky Connections": {"base": "Lucky Connections", "class": "Divination Card", "type": "divination high"},
	"2 Lucky Deck": {"base": "Lucky Deck", "class": "Divination Card", "type": "divination high"},
	"2 Merciless Armament": {"base": "Merciless Armament", "class": "Divination Card", "type": "divination high"},
	"2 Rain Tempter": {"base": "Rain Tempter", "class": "Divination Card", "type": "divination high"},
	"2 The Arena Champion": {"base": "The Arena Champion", "class": "Divination Card", "type": "divination high"},
	"2 The Artist": {"base": "The Artist", "class": "Divination Card", "type": "divination high"},
	"2 The Body": {"base": "The Body", "class": "Divination Card", "type": "divination high"},
	"2 The Brittle Emperor": {"base": "The Brittle Emperor", "class": "Divination Card", "type": "divination high"},
	"2 The Celestial Justicar": {"base": "The Celestial Justicar", "class": "Divination Card", "type": "divination high"},
	"2 The Coming Storm": {"base": "The Coming Storm", "class": "Divination Card", "type": "divination high"},
	"2 The Cursed King": {"base": "The Cursed King", "class": "Divination Card", "type": "divination high"},
	"2 The Dapper Prodigy": {"base": "The Dapper Prodigy", "class": "Divination Card", "type": "divination high"},
	"2 The Dark Mage": {"base": "The Dark Mage", "class": "Divination Card", "type": "divination high"},
	"2 The Dragon": {"base": "The Dragon", "class": "Divination Card", "type": "divination high"},
	"2 The Drunken Aristocrat": {"base": "The Drunken Aristocrat", "class": "Divination Card", "type": "divination high"},
	"2 The Enlightened": {"base": "The Enlightened", "class": "Divination Card", "type": "divination high"},
	"2 The Ethereal": {"base": "The Ethereal", "class": "Divination Card", "type": "divination high"},
	"2 The Explorer": {"base": "The Explorer", "class": "Divination Card", "type": "divination high"},
	"2 The Fletcher": {"base": "The Fletcher", "class": "Divination Card", "type": "divination high"},
	"2 The Formless Sea": {"base": "The Formless Sea", "class": "Divination Card", "type": "divination high"},
	"2 The Forsaken": {"base": "The Forsaken", "class": "Divination Card", "type": "divination high"},
	"2 The Harvester": {"base": "The Harvester", "class": "Divination Card", "type": "divination high"},
	"2 The Hoarder": {"base": "The Hoarder", "class": "Divination Card", "type": "divination high"},
	"2 The Hunger": {"base": "The Hunger", "class": "Divination Card", "type": "divination high"},
	"2 The Jester": {"base": "The Jester", "class": "Divination Card", "type": "divination high"},
	"2 The Lich": {"base": "The Lich", "class": "Divination Card", "type": "divination high"},
	"2 The Offering": {"base": "The Offering", "class": "Divination Card", "type": "divination high"},
	"2 The One With All": {"base": "The One With All", "class": "Divination Card", "type": "divination high"},
	"2 The Polymath": {"base": "The Polymath", "class": "Divination Card", "type": "divination high"},
	"2 The Porcupine": {"base": "The Porcupine", "class": "Divination Card", "type": "divination high"},
	"2 The Risk": {"base": "The Risk", "class": "Divination Card", "type": "divination high"},
	"2 The Saint's Treasure": {"base": "The Saint's Treasure", "class": "Divination Card", "type": "divination high"},
	"2 The Sephirot": {"base": "The Sephirot", "class": "Divination Card", "type": "divination high"},
	"2 The Soul": {"base": "The Soul", "class": "Divination Card", "type": "divination high"},
	"2 The Thaumaturgist": {"base": "The Thaumaturgist", "class": "Divination Card", "type": "divination high"},
	"2 The Traitor": {"base": "The Traitor", "class": "Divination Card", "type": "divination high"},
	"2 The Tyrant": {"base": "The Tyrant", "class": "Divination Card", "type": "divination high"},
	"2 The Valkyrie": {"base": "The Valkyrie", "class": "Divination Card", "type": "divination high"},
	"2 The Valley of Steel Boxes": {"base": "The Valley of Steel Boxes", "class": "Divination Card", "type": "divination high"},
	"2 The Void": {"base": "The Void", "class": "Divination Card", "type": "divination high"},
	"2 The Warlord": {"base": "The Warlord", "class": "Divination Card", "type": "divination high"},
	"2 The Wind": {"base": "The Wind", "class": "Divination Card", "type": "divination high"},
	"2 The Wolf": {"base": "The Wolf", "class": "Divination Card", "type": "divination high"},
	"2 The Wolven King's Bite": {"base": "The Wolven King's Bite", "class": "Divination Card", "type": "divination high"},
	"2 The Wretched": {"base": "The Wretched", "class": "Divination Card", "type": "divination high"},
	"2 Time-Lost Relic": {"base": "Time-Lost Relic", "class": "Divination Card", "type": "divination high"},
	"3 Death": {"base": "Death", "class": "Divination Card", "type": "divination low"},
	"3 Destined to Crumble": {"base": "Destined to Crumble", "class": "Divination Card", "type": "divination low"},
	"3 Rain of Chaos": {"base": "Rain of Chaos", "class": "Divination Card", "type": "divination low"},
	"3 The Flora's Gift": {"base": "The Flora's Gift", "class": "Divination Card", "type": "divination low"},
	"3 The Hermit": {"base": "The Hermit", "class": "Divination Card", "type": "divination low"},
	"3 The Incantation": {"base": "The Incantation", "class": "Divination Card", "type": "divination low"},
	"3 The Rabid Rhoa": {"base": "The Rabid Rhoa", "class": "Divination Card", "type": "divination low"},
	"3 The Scholar": {"base": "The Scholar", "class": "Divination Card", "type": "divination low"},
	"3 The Surgeon": {"base": "The Surgeon", "class": "Divination Card", "type": "divination low"},
	"3 The Twins": {"base": "The Twins", "class": "Divination Card", "type": "divination low"},
	"3 Thunderous Skies": {"base": "Thunderous Skies", "class": "Divination Card", "type": "divination low"},
	"7 The Carrion Crow": {"base": "The Carrion Crow", "class": "Divination Card", "type": "hide"},
	"7 The Inoculated": {"base": "The Inoculated", "class": "Divination Card", "type": "hide"},
	"7 The King's Blade": {"base": "The King's Blade", "class": "Divination Card", "type": "hide"},
	"7 Turn the Other Cheek": {"base": "Turn the Other Cheek", "class": "Divination Card", "type": "hide"},
	"9 Other uniques": {"class": "Divination Card", "type": "divination normal"}
}
