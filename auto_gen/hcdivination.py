#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 11/24/2018(m/d/y) 01:08:08 UTC from "Hardcore" data

desc = "Divination Card"

# Base type : settings pair
items = {
	"000 The Wolf's Shadow": {"base": "The Wolf's Shadow", "class": "Divination Card", "type": "divination low"},
	"001 The Dragon's Heart": {"base": "The Dragon's Heart", "class": "Divination Card", "type": "divination very high"},
	"002 Last Hope": {"base": "Last Hope", "class": "Divination Card", "type": "divination very high"},
	"003 Glimmer of Hope": {"base": "Glimmer of Hope", "class": "Divination Card", "type": "divination high"},
	"004 Beauty Through Death": {"base": "Beauty Through Death", "class": "Divination Card", "type": "divination extremely high"},
	"1 House of Mirrors": {"base": "House of Mirrors", "class": "Divination Card", "type": "divination extremely high"},
	"1 Hunter's Reward": {"base": "Hunter's Reward", "class": "Divination Card", "type": "divination extremely high"},
	"1 Immortal Resolve": {"base": "Immortal Resolve", "class": "Divination Card", "type": "divination extremely high"},
	"1 Mawr Blaidd": {"base": "Mawr Blaidd", "class": "Divination Card", "type": "divination extremely high"},
	"1 The Doctor": {"base": "The Doctor", "class": "Divination Card", "type": "divination extremely high"},
	"1 The Fiend": {"base": "The Fiend", "class": "Divination Card", "type": "divination extremely high"},
	"1 The Immortal": {"base": "The Immortal", "class": "Divination Card", "type": "divination extremely high"},
	"1 The Samurai's Eye": {"base": "The Samurai's Eye", "class": "Divination Card", "type": "divination extremely high"},
	"1 The Spark and the Flame": {"base": "The Spark and the Flame", "class": "Divination Card", "type": "divination extremely high"},
	"1 The Wolven King's Bite": {"base": "The Wolven King's Bite", "class": "Divination Card", "type": "divination extremely high"},
	"2 Abandoned Wealth": {"base": "Abandoned Wealth", "class": "Divination Card", "type": "divination very high"},
	"2 Boon of the First Ones": {"base": "Boon of the First Ones", "class": "Divination Card", "type": "divination very high"},
	"2 Chaotic Disposition": {"base": "Chaotic Disposition", "class": "Divination Card", "type": "divination very high"},
	"2 Heterochromia": {"base": "Heterochromia", "class": "Divination Card", "type": "divination very high"},
	"2 Perfection": {"base": "Perfection", "class": "Divination Card", "type": "divination very high"},
	"2 Pride Before the Fall": {"base": "Pride Before the Fall", "class": "Divination Card", "type": "divination very high"},
	"2 The Artist": {"base": "The Artist", "class": "Divination Card", "type": "divination very high"},
	"2 The Brittle Emperor": {"base": "The Brittle Emperor", "class": "Divination Card", "type": "divination very high"},
	"2 The Celestial Justicar": {"base": "The Celestial Justicar", "class": "Divination Card", "type": "divination very high"},
	"2 The Celestial Stone": {"base": "The Celestial Stone", "class": "Divination Card", "type": "divination very high"},
	"2 The Endless Darkness": {"base": "The Endless Darkness", "class": "Divination Card", "type": "divination very high"},
	"2 The Hale Heart": {"base": "The Hale Heart", "class": "Divination Card", "type": "divination very high"},
	"2 The Hoarder": {"base": "The Hoarder", "class": "Divination Card", "type": "divination very high"},
	"2 The Iron Bard": {"base": "The Iron Bard", "class": "Divination Card", "type": "divination very high"},
	"2 The King's Heart": {"base": "The King's Heart", "class": "Divination Card", "type": "divination very high"},
	"2 The Last One Standing": {"base": "The Last One Standing", "class": "Divination Card", "type": "divination very high"},
	"2 The Master": {"base": "The Master", "class": "Divination Card", "type": "divination very high"},
	"2 The Mayor": {"base": "The Mayor", "class": "Divination Card", "type": "divination very high"},
	"2 The Polymath": {"base": "The Polymath", "class": "Divination Card", "type": "divination very high"},
	"2 The Professor": {"base": "The Professor", "class": "Divination Card", "type": "divination very high"},
	"2 The Queen": {"base": "The Queen", "class": "Divination Card", "type": "divination very high"},
	"2 The Saint's Treasure": {"base": "The Saint's Treasure", "class": "Divination Card", "type": "divination very high"},
	"2 The Sephirot": {"base": "The Sephirot", "class": "Divination Card", "type": "divination very high"},
	"2 The Thaumaturgist": {"base": "The Thaumaturgist", "class": "Divination Card", "type": "divination very high"},
	"2 The Undaunted": {"base": "The Undaunted", "class": "Divination Card", "type": "divination very high"},
	"2 The Valkyrie": {"base": "The Valkyrie", "class": "Divination Card", "type": "divination very high"},
	"2 The Vast": {"base": "The Vast", "class": "Divination Card", "type": "divination very high"},
	"2 The Wind": {"base": "The Wind", "class": "Divination Card", "type": "divination very high"},
	"2 The Wolf": {"base": "The Wolf", "class": "Divination Card", "type": "divination very high"},
	"2 The World Eater": {"base": "The World Eater", "class": "Divination Card", "type": "divination very high"},
	"2 Time-Lost Relic": {"base": "Time-Lost Relic", "class": "Divination Card", "type": "divination very high"},
	"2 Wealth and Power": {"base": "Wealth and Power", "class": "Divination Card", "type": "divination very high"},
	"3 Atziri's Arsenal": {"base": "Atziri's Arsenal", "class": "Divination Card", "type": "divination high"},
	"3 Birth of the Three": {"base": "Birth of the Three", "class": "Divination Card", "type": "divination high"},
	"3 Bowyer's Dream": {"base": "Bowyer's Dream", "class": "Divination Card", "type": "divination high"},
	"3 Emperor of Purity": {"base": "Emperor of Purity", "class": "Divination Card", "type": "divination high"},
	"3 Gemcutter's Promise": {"base": "Gemcutter's Promise", "class": "Divination Card", "type": "divination high"},
	"3 Harmony of Souls": {"base": "Harmony of Souls", "class": "Divination Card", "type": "divination high"},
	"3 Humility": {"base": "Humility", "class": "Divination Card", "type": "divination high"},
	"3 Jack in the Box": {"base": "Jack in the Box", "class": "Divination Card", "type": "divination high"},
	"3 Left to Fate": {"base": "Left to Fate", "class": "Divination Card", "type": "divination high"},
	"3 Lingering Remnants": {"base": "Lingering Remnants", "class": "Divination Card", "type": "divination high"},
	"3 Lucky Deck": {"base": "Lucky Deck", "class": "Divination Card", "type": "divination high"},
	"3 Lysah's Respite": {"base": "Lysah's Respite", "class": "Divination Card", "type": "divination high"},
	"3 No Traces": {"base": "No Traces", "class": "Divination Card", "type": "divination high"},
	"3 Rebirth": {"base": "Rebirth", "class": "Divination Card", "type": "divination high"},
	"3 Scholar of the Seas": {"base": "Scholar of the Seas", "class": "Divination Card", "type": "divination high"},
	"3 The Admirer": {"base": "The Admirer", "class": "Divination Card", "type": "divination high"},
	"3 The Avenger": {"base": "The Avenger", "class": "Divination Card", "type": "divination high"},
	"3 The Body": {"base": "The Body", "class": "Divination Card", "type": "divination high"},
	"3 The Breach": {"base": "The Breach", "class": "Divination Card", "type": "divination high"},
	"3 The Cartographer": {"base": "The Cartographer", "class": "Divination Card", "type": "divination high"},
	"3 The Chains that Bind": {"base": "The Chains that Bind", "class": "Divination Card", "type": "divination high"},
	"3 The Conduit": {"base": "The Conduit", "class": "Divination Card", "type": "divination high"},
	"3 The Cursed King": {"base": "The Cursed King", "class": "Divination Card", "type": "divination high"},
	"3 The Dapper Prodigy": {"base": "The Dapper Prodigy", "class": "Divination Card", "type": "divination high"},
	"3 The Dark Mage": {"base": "The Dark Mage", "class": "Divination Card", "type": "divination high"},
	"3 The Dreamer": {"base": "The Dreamer", "class": "Divination Card", "type": "divination high"},
	"3 The Dreamland": {"base": "The Dreamland", "class": "Divination Card", "type": "divination high"},
	"3 The Enlightened": {"base": "The Enlightened", "class": "Divination Card", "type": "divination high"},
	"3 The Ethereal": {"base": "The Ethereal", "class": "Divination Card", "type": "divination high"},
	"3 The Fletcher": {"base": "The Fletcher", "class": "Divination Card", "type": "divination high"},
	"3 The Formless Sea": {"base": "The Formless Sea", "class": "Divination Card", "type": "divination high"},
	"3 The Hunger": {"base": "The Hunger", "class": "Divination Card", "type": "divination high"},
	"3 The Innocent": {"base": "The Innocent", "class": "Divination Card", "type": "divination high"},
	"3 The Inventor": {"base": "The Inventor", "class": "Divination Card", "type": "divination high"},
	"3 The Jeweller's Boon": {"base": "The Jeweller's Boon", "class": "Divination Card", "type": "divination high"},
	"3 The Obscured": {"base": "The Obscured", "class": "Divination Card", "type": "divination high"},
	"3 The Offering": {"base": "The Offering", "class": "Divination Card", "type": "divination high"},
	"3 The Penitent": {"base": "The Penitent", "class": "Divination Card", "type": "divination high"},
	"3 The Porcupine": {"base": "The Porcupine", "class": "Divination Card", "type": "divination high"},
	"3 The Price of Protection": {"base": "The Price of Protection", "class": "Divination Card", "type": "divination high"},
	"3 The Risk": {"base": "The Risk", "class": "Divination Card", "type": "divination high"},
	"3 The Rite of Elements": {"base": "The Rite of Elements", "class": "Divination Card", "type": "divination high"},
	"3 The Soul": {"base": "The Soul", "class": "Divination Card", "type": "divination high"},
	"3 The Standoff": {"base": "The Standoff", "class": "Divination Card", "type": "divination high"},
	"3 The Surveyor": {"base": "The Surveyor", "class": "Divination Card", "type": "divination high"},
	"3 The Sword King's Salute": {"base": "The Sword King's Salute", "class": "Divination Card", "type": "divination high"},
	"3 The Throne": {"base": "The Throne", "class": "Divination Card", "type": "divination high"},
	"3 The Traitor": {"base": "The Traitor", "class": "Divination Card", "type": "divination high"},
	"3 The Twilight Moon": {"base": "The Twilight Moon", "class": "Divination Card", "type": "divination high"},
	"3 The Union": {"base": "The Union", "class": "Divination Card", "type": "divination high"},
	"3 The Valley of Steel Boxes": {"base": "The Valley of Steel Boxes", "class": "Divination Card", "type": "divination high"},
	"3 The Void": {"base": "The Void", "class": "Divination Card", "type": "divination high"},
	"3 The Wilted Rose": {"base": "The Wilted Rose", "class": "Divination Card", "type": "divination high"},
	"3 The Wrath": {"base": "The Wrath", "class": "Divination Card", "type": "divination high"},
	"3 The Wretched": {"base": "The Wretched", "class": "Divination Card", "type": "divination high"},
	"3 Treasure Hunter": {"base": "Treasure Hunter", "class": "Divination Card", "type": "divination high"},
	"3 Vinia's Token": {"base": "Vinia's Token", "class": "Divination Card", "type": "divination high"},
	"4 A Mother's Parting Gift": {"base": "A Mother's Parting Gift", "class": "Divination Card", "type": "divination low"},
	"4 Anarchy's Price": {"base": "Anarchy's Price", "class": "Divination Card", "type": "divination low"},
	"4 Cartographer's Delight": {"base": "Cartographer's Delight", "class": "Divination Card", "type": "divination low"},
	"4 Death": {"base": "Death", "class": "Divination Card", "type": "divination low"},
	"4 Her Mask": {"base": "Her Mask", "class": "Divination Card", "type": "divination low"},
	"4 Lantador's Lost Love": {"base": "Lantador's Lost Love", "class": "Divination Card", "type": "divination low"},
	"4 Loyalty": {"base": "Loyalty", "class": "Divination Card", "type": "divination low"},
	"4 Rain of Chaos": {"base": "Rain of Chaos", "class": "Divination Card", "type": "divination low"},
	"4 Shard of Fate": {"base": "Shard of Fate", "class": "Divination Card", "type": "divination low"},
	"4 The Betrayal": {"base": "The Betrayal", "class": "Divination Card", "type": "divination low"},
	"4 The Doppelganger": {"base": "The Doppelganger", "class": "Divination Card", "type": "divination low"},
	"4 The Endurance": {"base": "The Endurance", "class": "Divination Card", "type": "divination low"},
	"4 The Flora's Gift": {"base": "The Flora's Gift", "class": "Divination Card", "type": "divination low"},
	"4 The Hermit": {"base": "The Hermit", "class": "Divination Card", "type": "divination low"},
	"4 The Incantation": {"base": "The Incantation", "class": "Divination Card", "type": "divination low"},
	"4 The Lich": {"base": "The Lich", "class": "Divination Card", "type": "divination low"},
	"4 The Lover": {"base": "The Lover", "class": "Divination Card", "type": "divination low"},
	"4 The Lunaris Priestess": {"base": "The Lunaris Priestess", "class": "Divination Card", "type": "divination low"},
	"4 The Opulent": {"base": "The Opulent", "class": "Divination Card", "type": "divination low"},
	"4 The Ruthless Ceinture": {"base": "The Ruthless Ceinture", "class": "Divination Card", "type": "divination low"},
	"4 The Scholar": {"base": "The Scholar", "class": "Divination Card", "type": "divination low"},
	"4 The Summoner": {"base": "The Summoner", "class": "Divination Card", "type": "divination low"},
	"4 The Warden": {"base": "The Warden", "class": "Divination Card", "type": "divination low"},
	"4 Turn the Other Cheek": {"base": "Turn the Other Cheek", "class": "Divination Card", "type": "divination low"},
	"4 Volatile Power": {"base": "Volatile Power", "class": "Divination Card", "type": "divination low"},
	"7 Blessing of God": {"base": "Blessing of God", "class": "Divination Card", "type": "hide"},
	"7 Destined to Crumble": {"base": "Destined to Crumble", "class": "Divination Card", "type": "hide"},
	"7 Merciless Armament": {"base": "Merciless Armament", "class": "Divination Card", "type": "hide"},
	"7 Prosperity": {"base": "Prosperity", "class": "Divination Card", "type": "hide"},
	"7 Rain Tempter": {"base": "Rain Tempter", "class": "Divination Card", "type": "hide"},
	"7 Struck by Lightning": {"base": "Struck by Lightning", "class": "Divination Card", "type": "hide"},
	"7 The Carrion Crow": {"base": "The Carrion Crow", "class": "Divination Card", "type": "hide"},
	"7 The Inoculated": {"base": "The Inoculated", "class": "Divination Card", "type": "hide"},
	"7 The Jester": {"base": "The Jester", "class": "Divination Card", "type": "hide"},
	"7 The King's Blade": {"base": "The King's Blade", "class": "Divination Card", "type": "hide"},
	"7 The Lord in Black": {"base": "The Lord in Black", "class": "Divination Card", "type": "hide"},
	"7 The Metalsmith's Gift": {"base": "The Metalsmith's Gift", "class": "Divination Card", "type": "hide"},
	"7 The Rabid Rhoa": {"base": "The Rabid Rhoa", "class": "Divination Card", "type": "hide"},
	"7 The Road to Power": {"base": "The Road to Power", "class": "Divination Card", "type": "hide"},
	"7 The Scarred Meadow": {"base": "The Scarred Meadow", "class": "Divination Card", "type": "hide"},
	"7 The Sigil": {"base": "The Sigil", "class": "Divination Card", "type": "hide"},
	"7 The Spoiled Prince": {"base": "The Spoiled Prince", "class": "Divination Card", "type": "hide"},
	"7 The Surgeon": {"base": "The Surgeon", "class": "Divination Card", "type": "hide"},
	"7 The Twins": {"base": "The Twins", "class": "Divination Card", "type": "hide"},
	"7 The Tyrant": {"base": "The Tyrant", "class": "Divination Card", "type": "hide"},
	"7 The Undisputed": {"base": "The Undisputed", "class": "Divination Card", "type": "hide"},
	"7 The Web": {"base": "The Web", "class": "Divination Card", "type": "hide"},
	"7 Thunderous Skies": {"base": "Thunderous Skies", "class": "Divination Card", "type": "hide"},
	"9 Other Divination Cards": {"class": "Divination Card", "type": "divination normal"}
}
