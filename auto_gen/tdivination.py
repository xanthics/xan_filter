#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 12/21/2017(m/d/y) 08:00:49 UTC from "tmpstandard" data

desc = "Divination Card"

# Base type : settings pair
items = {
	"000 The Wolf's Shadow": {"base": "The Wolf's Shadow", "class": "Divination Card", "type": "divination low"},
	"001 The Dragon's Heart": {"base": "The Dragon's Heart", "class": "Divination Card", "type": "divination very high"},
	"002 Last Hope": {"base": "Last Hope", "class": "Divination Card", "type": "divination high"},
	"003 Glimmer of Hope": {"base": "Glimmer of Hope", "class": "Divination Card", "type": "divination normal"},
	"1 Abandoned Wealth": {"base": "Abandoned Wealth", "class": "Divination Card", "type": "divination very high"},
	"1 House of Mirrors": {"base": "House of Mirrors", "class": "Divination Card", "type": "divination very high"},
	"1 Hunter's Reward": {"base": "Hunter's Reward", "class": "Divination Card", "type": "divination very high"},
	"1 Mawr Blaidd": {"base": "Mawr Blaidd", "class": "Divination Card", "type": "divination very high"},
	"1 Pride Before the Fall": {"base": "Pride Before the Fall", "class": "Divination Card", "type": "divination very high"},
	"1 Rebirth": {"base": "Rebirth", "class": "Divination Card", "type": "divination very high"},
	"1 The Brittle Emperor": {"base": "The Brittle Emperor", "class": "Divination Card", "type": "divination very high"},
	"1 The Celestial Justicar": {"base": "The Celestial Justicar", "class": "Divination Card", "type": "divination very high"},
	"1 The Doctor": {"base": "The Doctor", "class": "Divination Card", "type": "divination very high"},
	"1 The Fiend": {"base": "The Fiend", "class": "Divination Card", "type": "divination very high"},
	"1 The Formless Sea": {"base": "The Formless Sea", "class": "Divination Card", "type": "divination very high"},
	"1 The Hunger": {"base": "The Hunger", "class": "Divination Card", "type": "divination very high"},
	"1 The Immortal": {"base": "The Immortal", "class": "Divination Card", "type": "divination very high"},
	"1 The King's Heart": {"base": "The King's Heart", "class": "Divination Card", "type": "divination very high"},
	"1 The Last One Standing": {"base": "The Last One Standing", "class": "Divination Card", "type": "divination very high"},
	"1 The Queen": {"base": "The Queen", "class": "Divination Card", "type": "divination very high"},
	"1 The Wolven King's Bite": {"base": "The Wolven King's Bite", "class": "Divination Card", "type": "divination very high"},
	"1 Wealth and Power": {"base": "Wealth and Power", "class": "Divination Card", "type": "divination very high"},
	"2 Bowyer's Dream": {"base": "Bowyer's Dream", "class": "Divination Card", "type": "divination high"},
	"2 Chaotic Disposition": {"base": "Chaotic Disposition", "class": "Divination Card", "type": "divination high"},
	"2 Emperor of Purity": {"base": "Emperor of Purity", "class": "Divination Card", "type": "divination high"},
	"2 Heterochromia": {"base": "Heterochromia", "class": "Divination Card", "type": "divination high"},
	"2 Left to Fate": {"base": "Left to Fate", "class": "Divination Card", "type": "divination high"},
	"2 The Artist": {"base": "The Artist", "class": "Divination Card", "type": "divination high"},
	"2 The Cursed King": {"base": "The Cursed King", "class": "Divination Card", "type": "divination high"},
	"2 The Dapper Prodigy": {"base": "The Dapper Prodigy", "class": "Divination Card", "type": "divination high"},
	"2 The Enlightened": {"base": "The Enlightened", "class": "Divination Card", "type": "divination high"},
	"2 The Ethereal": {"base": "The Ethereal", "class": "Divination Card", "type": "divination high"},
	"2 The Fletcher": {"base": "The Fletcher", "class": "Divination Card", "type": "divination high"},
	"2 The Hoarder": {"base": "The Hoarder", "class": "Divination Card", "type": "divination high"},
	"2 The Offering": {"base": "The Offering", "class": "Divination Card", "type": "divination high"},
	"2 The Polymath": {"base": "The Polymath", "class": "Divination Card", "type": "divination high"},
	"2 The Risk": {"base": "The Risk", "class": "Divination Card", "type": "divination high"},
	"2 The Saint's Treasure": {"base": "The Saint's Treasure", "class": "Divination Card", "type": "divination high"},
	"2 The Sephirot": {"base": "The Sephirot", "class": "Divination Card", "type": "divination high"},
	"2 The Soul": {"base": "The Soul", "class": "Divination Card", "type": "divination high"},
	"2 The Spark and the Flame": {"base": "The Spark and the Flame", "class": "Divination Card", "type": "divination high"},
	"2 The Standoff": {"base": "The Standoff", "class": "Divination Card", "type": "divination high"},
	"2 The Thaumaturgist": {"base": "The Thaumaturgist", "class": "Divination Card", "type": "divination high"},
	"2 The Throne": {"base": "The Throne", "class": "Divination Card", "type": "divination high"},
	"2 The Valkyrie": {"base": "The Valkyrie", "class": "Divination Card", "type": "divination high"},
	"2 The Vast": {"base": "The Vast", "class": "Divination Card", "type": "divination high"},
	"2 The Void": {"base": "The Void", "class": "Divination Card", "type": "divination high"},
	"2 The Wind": {"base": "The Wind", "class": "Divination Card", "type": "divination high"},
	"2 The Wolf": {"base": "The Wolf", "class": "Divination Card", "type": "divination high"},
	"2 Time-Lost Relic": {"base": "Time-Lost Relic", "class": "Divination Card", "type": "divination high"},
	"3 A Mother's Parting Gift": {"base": "A Mother's Parting Gift", "class": "Divination Card", "type": "divination low"},
	"3 Anarchy's Price": {"base": "Anarchy's Price", "class": "Divination Card", "type": "divination low"},
	"3 Assassin's Favour": {"base": "Assassin's Favour", "class": "Divination Card", "type": "divination low"},
	"3 Birth of the Three": {"base": "Birth of the Three", "class": "Divination Card", "type": "divination low"},
	"3 Blind Venture": {"base": "Blind Venture", "class": "Divination Card", "type": "divination low"},
	"3 Call to the First Ones": {"base": "Call to the First Ones", "class": "Divination Card", "type": "divination low"},
	"3 Cartographer's Delight": {"base": "Cartographer's Delight", "class": "Divination Card", "type": "divination low"},
	"3 Death": {"base": "Death", "class": "Divination Card", "type": "divination low"},
	"3 Destined to Crumble": {"base": "Destined to Crumble", "class": "Divination Card", "type": "divination low"},
	"3 Doedre's Madness": {"base": "Doedre's Madness", "class": "Divination Card", "type": "divination low"},
	"3 Dying Anguish": {"base": "Dying Anguish", "class": "Divination Card", "type": "divination low"},
	"3 Grave Knowledge": {"base": "Grave Knowledge", "class": "Divination Card", "type": "divination low"},
	"3 Her Mask": {"base": "Her Mask", "class": "Divination Card", "type": "divination low"},
	"3 Hubris": {"base": "Hubris", "class": "Divination Card", "type": "divination low"},
	"3 Hunter's Resolve": {"base": "Hunter's Resolve", "class": "Divination Card", "type": "divination low"},
	"3 Lantador's Lost Love": {"base": "Lantador's Lost Love", "class": "Divination Card", "type": "divination low"},
	"3 Light and Truth": {"base": "Light and Truth", "class": "Divination Card", "type": "divination low"},
	"3 Loyalty": {"base": "Loyalty", "class": "Divination Card", "type": "divination low"},
	"3 Might is Right": {"base": "Might is Right", "class": "Divination Card", "type": "divination low"},
	"3 Mitts": {"base": "Mitts", "class": "Divination Card", "type": "divination low"},
	"3 Prosperity": {"base": "Prosperity", "class": "Divination Card", "type": "divination low"},
	"3 Rain Tempter": {"base": "Rain Tempter", "class": "Divination Card", "type": "divination low"},
	"3 Rain of Chaos": {"base": "Rain of Chaos", "class": "Divination Card", "type": "divination low"},
	"3 Shard of Fate": {"base": "Shard of Fate", "class": "Divination Card", "type": "divination low"},
	"3 The Aesthete": {"base": "The Aesthete", "class": "Divination Card", "type": "divination low"},
	"3 The Betrayal": {"base": "The Betrayal", "class": "Divination Card", "type": "divination low"},
	"3 The Blazing Fire": {"base": "The Blazing Fire", "class": "Divination Card", "type": "divination low"},
	"3 The Calling": {"base": "The Calling", "class": "Divination Card", "type": "divination low"},
	"3 The Catalyst": {"base": "The Catalyst", "class": "Divination Card", "type": "divination low"},
	"3 The Coming Storm": {"base": "The Coming Storm", "class": "Divination Card", "type": "divination low"},
	"3 The Conduit": {"base": "The Conduit", "class": "Divination Card", "type": "divination low"},
	"3 The Doppelganger": {"base": "The Doppelganger", "class": "Divination Card", "type": "divination low"},
	"3 The Drunken Aristocrat": {"base": "The Drunken Aristocrat", "class": "Divination Card", "type": "divination low"},
	"3 The Endurance": {"base": "The Endurance", "class": "Divination Card", "type": "divination low"},
	"3 The Eye of the Dragon": {"base": "The Eye of the Dragon", "class": "Divination Card", "type": "divination low"},
	"3 The Feast": {"base": "The Feast", "class": "Divination Card", "type": "divination low"},
	"3 The Flora's Gift": {"base": "The Flora's Gift", "class": "Divination Card", "type": "divination low"},
	"3 The Gambler": {"base": "The Gambler", "class": "Divination Card", "type": "divination low"},
	"3 The Garish Power": {"base": "The Garish Power", "class": "Divination Card", "type": "divination low"},
	"3 The Gemcutter": {"base": "The Gemcutter", "class": "Divination Card", "type": "divination low"},
	"3 The Hermit": {"base": "The Hermit", "class": "Divination Card", "type": "divination low"},
	"3 The Incantation": {"base": "The Incantation", "class": "Divination Card", "type": "divination low"},
	"3 The Lich": {"base": "The Lich", "class": "Divination Card", "type": "divination low"},
	"3 The Lover": {"base": "The Lover", "class": "Divination Card", "type": "divination low"},
	"3 The Lunaris Priestess": {"base": "The Lunaris Priestess", "class": "Divination Card", "type": "divination low"},
	"3 The Metalsmith's Gift": {"base": "The Metalsmith's Gift", "class": "Divination Card", "type": "divination low"},
	"3 The Oath": {"base": "The Oath", "class": "Divination Card", "type": "divination low"},
	"3 The Opulent": {"base": "The Opulent", "class": "Divination Card", "type": "divination low"},
	"3 The Pack Leader": {"base": "The Pack Leader", "class": "Divination Card", "type": "divination low"},
	"3 The Rabid Rhoa": {"base": "The Rabid Rhoa", "class": "Divination Card", "type": "divination low"},
	"3 The Ruthless Ceinture": {"base": "The Ruthless Ceinture", "class": "Divination Card", "type": "divination low"},
	"3 The Scarred Meadow": {"base": "The Scarred Meadow", "class": "Divination Card", "type": "divination low"},
	"3 The Scholar": {"base": "The Scholar", "class": "Divination Card", "type": "divination low"},
	"3 The Sigil": {"base": "The Sigil", "class": "Divination Card", "type": "divination low"},
	"3 The Summoner": {"base": "The Summoner", "class": "Divination Card", "type": "divination low"},
	"3 The Sun": {"base": "The Sun", "class": "Divination Card", "type": "divination low"},
	"3 The Surgeon": {"base": "The Surgeon", "class": "Divination Card", "type": "divination low"},
	"3 The Twins": {"base": "The Twins", "class": "Divination Card", "type": "divination low"},
	"3 The Visionary": {"base": "The Visionary", "class": "Divination Card", "type": "divination low"},
	"3 The Warden": {"base": "The Warden", "class": "Divination Card", "type": "divination low"},
	"3 The Watcher": {"base": "The Watcher", "class": "Divination Card", "type": "divination low"},
	"3 The Web": {"base": "The Web", "class": "Divination Card", "type": "divination low"},
	"3 The Wolverine": {"base": "The Wolverine", "class": "Divination Card", "type": "divination low"},
	"3 Thunderous Skies": {"base": "Thunderous Skies", "class": "Divination Card", "type": "divination low"},
	"3 Tranquillity": {"base": "Tranquillity", "class": "Divination Card", "type": "divination low"},
	"3 Volatile Power": {"base": "Volatile Power", "class": "Divination Card", "type": "divination low"},
	"7 Struck by Lightning": {"base": "Struck by Lightning", "class": "Divination Card", "type": "hide"},
	"7 The Carrion Crow": {"base": "The Carrion Crow", "class": "Divination Card", "type": "hide"},
	"7 The Inoculated": {"base": "The Inoculated", "class": "Divination Card", "type": "hide"},
	"7 The King's Blade": {"base": "The King's Blade", "class": "Divination Card", "type": "hide"},
	"7 Turn the Other Cheek": {"base": "Turn the Other Cheek", "class": "Divination Card", "type": "hide"},
	"9 Other uniques": {"class": "Divination Card", "type": "divination normal"}
}
