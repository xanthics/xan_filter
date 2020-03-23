#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 03/23/2020(m/d/y) 20:12:55 UTC from "tmpstandard" data

desc = "Prophecy Autogen"

# Base type : settings pair
items = {
	"1 A Call into the Void": {"prophecy": "A Call into the Void", "class": "Currency", "type": "currency low"},
	"1 A Dishonourable Death": {"prophecy": "A Dishonourable Death", "class": "Currency", "type": "currency very high"},
	"1 A Firm Foothold": {"prophecy": "A Firm Foothold", "class": "Currency", "type": "currency low"},
	"1 A Forest of False Idols": {"prophecy": "A Forest of False Idols", "class": "Currency", "type": "currency low"},
	"1 A Master Seeks Help": {"prophecy": "A Master Seeks Help", "class": "Currency", "type": "currency show"},
	"1 A Prodigious Hand": {"prophecy": "A Prodigious Hand", "class": "Currency", "type": "currency high"},
	"1 A Regal Death": {"prophecy": "A Regal Death", "class": "Currency", "type": "currency show"},
	"1 A Rift in Time": {"prophecy": "A Rift in Time", "class": "Currency", "type": "currency low"},
	"1 A Valuable Combination": {"prophecy": "A Valuable Combination", "class": "Currency", "type": "currency low"},
	"1 A Vision of Ice and Fire": {"prophecy": "A Vision of Ice and Fire", "class": "Currency", "type": "currency high"},
	"1 A Whispered Prayer": {"prophecy": "A Whispered Prayer", "class": "Currency", "type": "currency low"},
	"1 Abnormal Effulgence": {"prophecy": "Abnormal Effulgence", "class": "Currency", "type": "currency low"},
	"1 Against the Tide": {"prophecy": "Against the Tide", "class": "Currency", "type": "currency low"},
	"1 Agony at Dusk": {"prophecy": "Agony at Dusk", "class": "Currency", "type": "currency low"},
	"1 An Unseen Peril": {"prophecy": "An Unseen Peril", "class": "Currency", "type": "currency show"},
	"1 Anarchy's End I": {"prophecy": "Anarchy's End I", "class": "Currency", "type": "currency low"},
	"1 Anarchy's End II": {"prophecy": "Anarchy's End II", "class": "Currency", "type": "currency low"},
	"1 Anarchy's End III": {"prophecy": "Anarchy's End III", "class": "Currency", "type": "currency low"},
	"1 Anarchy's End IV": {"prophecy": "Anarchy's End IV", "class": "Currency", "type": "currency low"},
	"1 Ancient Doom": {"prophecy": "Ancient Doom", "class": "Currency", "type": "currency low"},
	"1 Baptism by Death": {"prophecy": "Baptism by Death", "class": "Currency", "type": "currency low"},
	"1 Battle Hardened": {"prophecy": "Battle Hardened", "class": "Currency", "type": "currency low"},
	"1 Beyond Sight I": {"prophecy": "Beyond Sight I", "class": "Currency", "type": "currency low"},
	"1 Beyond Sight II": {"prophecy": "Beyond Sight II", "class": "Currency", "type": "currency low"},
	"1 Beyond Sight III": {"prophecy": "Beyond Sight III", "class": "Currency", "type": "currency low"},
	"1 Beyond Sight IV": {"prophecy": "Beyond Sight IV", "class": "Currency", "type": "currency low"},
	"1 Black Devotion": {"prophecy": "Black Devotion", "class": "Currency", "type": "currency low"},
	"1 Blind Faith": {"prophecy": "Blind Faith", "class": "Currency", "type": "currency low"},
	"1 Blinding Light": {"prophecy": "Blinding Light", "class": "Currency", "type": "currency low"},
	"1 Blood in the Eyes": {"prophecy": "Blood in the Eyes", "class": "Currency", "type": "currency low"},
	"1 Blood of the Betrayed": {"prophecy": "Blood of the Betrayed", "class": "Currency", "type": "currency low"},
	"1 Bountiful Traps": {"prophecy": "Bountiful Traps", "class": "Currency", "type": "currency show"},
	"1 Burning Dread": {"prophecy": "Burning Dread", "class": "Currency", "type": "currency low"},
	"1 Cleanser of Sins": {"prophecy": "Cleanser of Sins", "class": "Currency", "type": "currency high"},
	"1 Cold Blooded Fury": {"prophecy": "Cold Blooded Fury", "class": "Currency", "type": "currency low"},
	"1 Cold Greed": {"prophecy": "Cold Greed", "class": "Currency", "type": "currency low"},
	"1 Crimson Hues": {"prophecy": "Crimson Hues", "class": "Currency", "type": "currency low"},
	"1 Crushing Squall": {"prophecy": "Crushing Squall", "class": "Currency", "type": "currency low"},
	"1 Custodians of Silence": {"prophecy": "Custodians of Silence", "class": "Currency", "type": "currency low"},
	"1 Dance of Steel": {"prophecy": "Dance of Steel", "class": "Currency", "type": "currency low"},
	"1 Dark Instincts": {"prophecy": "Dark Instincts", "class": "Currency", "type": "currency low"},
	"1 Darktongue's Shriek": {"prophecy": "Darktongue's Shriek", "class": "Currency", "type": "currency very high"},
	"1 Day of Sacrifice I": {"prophecy": "Day of Sacrifice I", "class": "Currency", "type": "currency low"},
	"1 Day of Sacrifice II": {"prophecy": "Day of Sacrifice II", "class": "Currency", "type": "currency low"},
	"1 Day of Sacrifice III": {"prophecy": "Day of Sacrifice III", "class": "Currency", "type": "currency low"},
	"1 Day of Sacrifice IV": {"prophecy": "Day of Sacrifice IV", "class": "Currency", "type": "currency low"},
	"1 Deadly Rivalry I": {"prophecy": "Deadly Rivalry I", "class": "Currency", "type": "currency low"},
	"1 Deadly Rivalry II": {"prophecy": "Deadly Rivalry II", "class": "Currency", "type": "currency low"},
	"1 Deadly Rivalry III": {"prophecy": "Deadly Rivalry III", "class": "Currency", "type": "currency low"},
	"1 Deadly Rivalry IV": {"prophecy": "Deadly Rivalry IV", "class": "Currency", "type": "currency low"},
	"1 Deadly Rivalry V": {"prophecy": "Deadly Rivalry V", "class": "Currency", "type": "currency low"},
	"1 Deadly Twins": {"prophecy": "Deadly Twins", "class": "Currency", "type": "currency show"},
	"1 Defiled in the Sceptre": {"prophecy": "Defiled in the Sceptre", "class": "Currency", "type": "currency low"},
	"1 Dying Cry": {"prophecy": "Dying Cry", "class": "Currency", "type": "currency low"},
	"1 Echoes of Witchcraft": {"prophecy": "Echoes of Witchcraft", "class": "Currency", "type": "currency low"},
	"1 End of the Light": {"prophecy": "End of the Light", "class": "Currency", "type": "currency low"},
	"1 Ending the Torment": {"prophecy": "Ending the Torment", "class": "Currency", "type": "currency low"},
	"1 Erased from Memory": {"prophecy": "Erased from Memory", "class": "Currency", "type": "currency show"},
	"1 Erasmus' Gift": {"prophecy": "Erasmus' Gift", "class": "Currency", "type": "currency show"},
	"1 Faith Exhumed": {"prophecy": "Faith Exhumed", "class": "Currency", "type": "currency low"},
	"1 Fallow At Last": {"prophecy": "Fallow At Last", "class": "Currency", "type": "currency low"},
	"1 Fated Connections": {"prophecy": "Fated Connections", "class": "Currency", "type": "currency extremely high"},
	"1 Fear's Wide Reach": {"prophecy": "Fear's Wide Reach", "class": "Currency", "type": "currency low"},
	"1 Fire and Brimstone": {"prophecy": "Fire and Brimstone", "class": "Currency", "type": "currency low"},
	"1 Fire and Ice": {"prophecy": "Fire and Ice", "class": "Currency", "type": "currency low"},
	"1 Fire from the Sky": {"prophecy": "Fire from the Sky", "class": "Currency", "type": "currency low"},
	"1 Fire, Wood and Stone": {"prophecy": "Fire, Wood and Stone", "class": "Currency", "type": "currency low"},
	"1 Flesh of the Beast": {"prophecy": "Flesh of the Beast", "class": "Currency", "type": "currency low"},
	"1 Forceful Exorcism": {"prophecy": "Forceful Exorcism", "class": "Currency", "type": "currency low"},
	"1 From Death Springs Life": {"prophecy": "From Death Springs Life", "class": "Currency", "type": "currency low"},
	"1 From The Void": {"prophecy": "From The Void", "class": "Currency", "type": "currency low"},
	"1 Gilded Within": {"prophecy": "Gilded Within", "class": "Currency", "type": "currency low"},
	"1 Golden Touch": {"prophecy": "Golden Touch", "class": "Currency", "type": "currency low"},
	"1 Graceful Flames": {"prophecy": "Graceful Flames", "class": "Currency", "type": "currency low"},
	"1 Greed's Folly": {"prophecy": "Greed's Folly", "class": "Currency", "type": "currency low"},
	"1 Heart of the Fire": {"prophecy": "Heart of the Fire", "class": "Currency", "type": "currency low"},
	"1 Heavy Blows": {"prophecy": "Heavy Blows", "class": "Currency", "type": "currency low"},
	"1 Hidden Reinforcements": {"prophecy": "Hidden Reinforcements", "class": "Currency", "type": "currency low"},
	"1 Hidden Vaal Pathways": {"prophecy": "Hidden Vaal Pathways", "class": "Currency", "type": "currency low"},
	"1 Holding the Bridge": {"prophecy": "Holding the Bridge", "class": "Currency", "type": "currency low"},
	"1 Hunter's Lesson": {"prophecy": "Hunter's Lesson", "class": "Currency", "type": "currency show"},
	"1 Ice from Above": {"prophecy": "Ice from Above", "class": "Currency", "type": "currency low"},
	"1 In the Grasp of Corruption": {"prophecy": "In the Grasp of Corruption", "class": "Currency", "type": "currency low"},
	"1 Kalandra's Craft": {"prophecy": "Kalandra's Craft", "class": "Currency", "type": "currency low"},
	"1 Last of the Wildmen": {"prophecy": "Last of the Wildmen", "class": "Currency", "type": "currency high"},
	"1 Lasting Impressions": {"prophecy": "Lasting Impressions", "class": "Currency", "type": "currency low"},
	"1 Lightning Falls": {"prophecy": "Lightning Falls", "class": "Currency", "type": "currency low"},
	"1 Living Fires": {"prophecy": "Living Fires", "class": "Currency", "type": "currency low"},
	"1 Lost in the Pages": {"prophecy": "Lost in the Pages", "class": "Currency", "type": "currency very high"},
	"1 Monstrous Treasure": {"prophecy": "Monstrous Treasure", "class": "Currency", "type": "currency high"},
	"1 Mouth of Horrors": {"prophecy": "Mouth of Horrors", "class": "Currency", "type": "currency low"},
	"1 Mysterious Invaders": {"prophecy": "Mysterious Invaders", "class": "Currency", "type": "currency show"},
	"1 Nature's Resilience": {"prophecy": "Nature's Resilience", "class": "Currency", "type": "currency low"},
	"1 Nemesis of Greed": {"prophecy": "Nemesis of Greed", "class": "Currency", "type": "currency low"},
	"1 Notched Flesh": {"prophecy": "Notched Flesh", "class": "Currency", "type": "currency low"},
	"1 Overflowing Riches": {"prophecy": "Overflowing Riches", "class": "Currency", "type": "currency show"},
	"1 Path of Betrayal": {"prophecy": "Path of Betrayal", "class": "Currency", "type": "currency low"},
	"1 Plague of Frogs": {"prophecy": "Plague of Frogs", "class": "Currency", "type": "currency show"},
	"1 Plague of Rats": {"prophecy": "Plague of Rats", "class": "Currency", "type": "currency show"},
	"1 Pleasure and Pain": {"prophecy": "Pleasure and Pain", "class": "Currency", "type": "currency low"},
	"1 Pools of Wealth": {"prophecy": "Pools of Wealth", "class": "Currency", "type": "currency low"},
	"1 Possessed Foe": {"prophecy": "Possessed Foe", "class": "Currency", "type": "currency low"},
	"1 Power Magnified": {"prophecy": "Power Magnified", "class": "Currency", "type": "currency low"},
	"1 Rebirth": {"prophecy": "Rebirth", "class": "Currency", "type": "currency show"},
	"1 Reforged Bonds": {"prophecy": "Reforged Bonds", "class": "Currency", "type": "currency show"},
	"1 Resistant to Change": {"prophecy": "Resistant to Change", "class": "Currency", "type": "currency low"},
	"1 Risen Blood": {"prophecy": "Risen Blood", "class": "Currency", "type": "currency low"},
	"1 Roth's Legacy": {"prophecy": "Roth's Legacy", "class": "Currency", "type": "currency low"},
	"1 Severed Limbs": {"prophecy": "Severed Limbs", "class": "Currency", "type": "currency low"},
	"1 Smothering Tendrils": {"prophecy": "Smothering Tendrils", "class": "Currency", "type": "currency low"},
	"1 Soil, Worms and Blood": {"prophecy": "Soil, Worms and Blood", "class": "Currency", "type": "currency low"},
	"1 Song of the Sekhema": {"prophecy": "Song of the Sekhema", "class": "Currency", "type": "currency very high"},
	"1 Storm on the Horizon": {"prophecy": "Storm on the Horizon", "class": "Currency", "type": "currency low"},
	"1 Storm on the Reef": {"prophecy": "Storm on the Reef", "class": "Currency", "type": "currency low"},
	"1 Strong as a Bull": {"prophecy": "Strong as a Bull", "class": "Currency", "type": "currency low"},
	"1 Sun's Punishment": {"prophecy": "Sun's Punishment", "class": "Currency", "type": "currency low"},
	"1 Thaumaturgical History I": {"prophecy": "Thaumaturgical History I", "class": "Currency", "type": "currency low"},
	"1 Thaumaturgical History II": {"prophecy": "Thaumaturgical History II", "class": "Currency", "type": "currency low"},
	"1 Thaumaturgical History III": {"prophecy": "Thaumaturgical History III", "class": "Currency", "type": "currency low"},
	"1 Thaumaturgical History IV": {"prophecy": "Thaumaturgical History IV", "class": "Currency", "type": "currency low"},
	"1 The Alchemist": {"prophecy": "The Alchemist", "class": "Currency", "type": "currency low"},
	"1 The Ambitious Bandit I": {"prophecy": "The Ambitious Bandit I", "class": "Currency", "type": "currency low"},
	"1 The Ambitious Bandit II": {"prophecy": "The Ambitious Bandit II", "class": "Currency", "type": "currency low"},
	"1 The Ambitious Bandit III": {"prophecy": "The Ambitious Bandit III", "class": "Currency", "type": "currency low"},
	"1 The Apex Predator": {"prophecy": "The Apex Predator", "class": "Currency", "type": "currency low"},
	"1 The Beautiful Guide": {"prophecy": "The Beautiful Guide", "class": "Currency", "type": "currency show"},
	"1 The Beginning and the End": {"prophecy": "The Beginning and the End", "class": "Currency", "type": "currency low"},
	"1 The Bishop's Legacy": {"prophecy": "The Bishop's Legacy", "class": "Currency", "type": "currency low"},
	"1 The Bloody Flowers Redux": {"prophecy": "The Bloody Flowers Redux", "class": "Currency", "type": "currency low"},
	"1 The Bowstring's Music": {"prophecy": "The Bowstring's Music", "class": "Currency", "type": "currency very high"},
	"1 The Brothers of Necromancy": {"prophecy": "The Brothers of Necromancy", "class": "Currency", "type": "currency show"},
	"1 The Brutal Enforcer": {"prophecy": "The Brutal Enforcer", "class": "Currency", "type": "currency low"},
	"1 The Child of Lunaris": {"prophecy": "The Child of Lunaris", "class": "Currency", "type": "currency low"},
	"1 The Corrupt": {"prophecy": "The Corrupt", "class": "Currency", "type": "currency low"},
	"1 The Cursed Choir": {"prophecy": "The Cursed Choir", "class": "Currency", "type": "currency show"},
	"1 The Dreaded Rhoa": {"prophecy": "The Dreaded Rhoa", "class": "Currency", "type": "currency low"},
	"1 The Dream Trial": {"prophecy": "The Dream Trial", "class": "Currency", "type": "currency low"},
	"1 The Dreamer's Dream": {"prophecy": "The Dreamer's Dream", "class": "Currency", "type": "currency low"},
	"1 The Eagle's Cry": {"prophecy": "The Eagle's Cry", "class": "Currency", "type": "currency low"},
	"1 The Fall of an Empire": {"prophecy": "The Fall of an Empire", "class": "Currency", "type": "currency low"},
	"1 The Feral Lord I": {"prophecy": "The Feral Lord I", "class": "Currency", "type": "currency low"},
	"1 The Feral Lord II": {"prophecy": "The Feral Lord II", "class": "Currency", "type": "currency low"},
	"1 The Feral Lord III": {"prophecy": "The Feral Lord III", "class": "Currency", "type": "currency low"},
	"1 The Feral Lord IV": {"prophecy": "The Feral Lord IV", "class": "Currency", "type": "currency low"},
	"1 The Feral Lord V": {"prophecy": "The Feral Lord V", "class": "Currency", "type": "currency low"},
	"1 The Flayed Man": {"prophecy": "The Flayed Man", "class": "Currency", "type": "currency low"},
	"1 The Flow of Energy": {"prophecy": "The Flow of Energy", "class": "Currency", "type": "currency low"},
	"1 The Forgotten Garrison": {"prophecy": "The Forgotten Garrison", "class": "Currency", "type": "currency low"},
	"1 The Fortune Teller's Collection": {"prophecy": "The Fortune Teller's Collection", "class": "Currency", "type": "currency low"},
	"1 The Four Feral Exiles": {"prophecy": "The Four Feral Exiles", "class": "Currency", "type": "currency show"},
	"1 The God of Misfortune": {"prophecy": "The God of Misfortune", "class": "Currency", "type": "currency show"},
	"1 The Great Leader of the North": {"prophecy": "The Great Leader of the North", "class": "Currency", "type": "currency very high"},
	"1 The Great Mind of the North": {"prophecy": "The Great Mind of the North", "class": "Currency", "type": "currency low"},
	"1 The Hardened Armour": {"prophecy": "The Hardened Armour", "class": "Currency", "type": "currency show"},
	"1 The Hollow Pledge": {"prophecy": "The Hollow Pledge", "class": "Currency", "type": "currency very high"},
	"1 The Hungering Swarm": {"prophecy": "The Hungering Swarm", "class": "Currency", "type": "currency show"},
	"1 The Invader": {"prophecy": "The Invader", "class": "Currency", "type": "currency show"},
	"1 The Jeweller's Touch": {"prophecy": "The Jeweller's Touch", "class": "Currency", "type": "currency high"},
	"1 The Karui Rebellion": {"prophecy": "The Karui Rebellion", "class": "Currency", "type": "currency low"},
	"1 The King and the Brambles": {"prophecy": "The King and the Brambles", "class": "Currency", "type": "currency low"},
	"1 The King's Path": {"prophecy": "The King's Path", "class": "Currency", "type": "currency high"},
	"1 The Lady in Black": {"prophecy": "The Lady in Black", "class": "Currency", "type": "currency low"},
	"1 The Last Watch": {"prophecy": "The Last Watch", "class": "Currency", "type": "currency low"},
	"1 The Lost Maps": {"prophecy": "The Lost Maps", "class": "Currency", "type": "currency low"},
	"1 The Lost Undying": {"prophecy": "The Lost Undying", "class": "Currency", "type": "currency low"},
	"1 The Malevolent Witch": {"prophecy": "The Malevolent Witch", "class": "Currency", "type": "currency low"},
	"1 The Misunderstood Queen": {"prophecy": "The Misunderstood Queen", "class": "Currency", "type": "currency low"},
	"1 The Mysterious Gift": {"prophecy": "The Mysterious Gift", "class": "Currency", "type": "currency low"},
	"1 The Nest": {"prophecy": "The Nest", "class": "Currency", "type": "currency low"},
	"1 The Nightmare Awakens": {"prophecy": "The Nightmare Awakens", "class": "Currency", "type": "currency low"},
	"1 The Petrified": {"prophecy": "The Petrified", "class": "Currency", "type": "currency low"},
	"1 The Plaguemaw I": {"prophecy": "The Plaguemaw I", "class": "Currency", "type": "currency low"},
	"1 The Plaguemaw II": {"prophecy": "The Plaguemaw II", "class": "Currency", "type": "currency low"},
	"1 The Plaguemaw III": {"prophecy": "The Plaguemaw III", "class": "Currency", "type": "currency low"},
	"1 The Plaguemaw IV": {"prophecy": "The Plaguemaw IV", "class": "Currency", "type": "currency show"},
	"1 The Plaguemaw V": {"prophecy": "The Plaguemaw V", "class": "Currency", "type": "currency low"},
	"1 The Prison Guard": {"prophecy": "The Prison Guard", "class": "Currency", "type": "currency low"},
	"1 The Prison Key": {"prophecy": "The Prison Key", "class": "Currency", "type": "currency low"},
	"1 The Queen's Sacrifice": {"prophecy": "The Queen's Sacrifice", "class": "Currency", "type": "currency extremely high"},
	"1 The Queen's Vaults": {"prophecy": "The Queen's Vaults", "class": "Currency", "type": "currency show"},
	"1 The Scout": {"prophecy": "The Scout", "class": "Currency", "type": "currency show"},
	"1 The Servant's Heart": {"prophecy": "The Servant's Heart", "class": "Currency", "type": "currency low"},
	"1 The Sharpened Blade": {"prophecy": "The Sharpened Blade", "class": "Currency", "type": "currency show"},
	"1 The Silverwood": {"prophecy": "The Silverwood", "class": "Currency", "type": "currency low"},
	"1 The Singular Spirit": {"prophecy": "The Singular Spirit", "class": "Currency", "type": "currency low"},
	"1 The Sinner's Stone": {"prophecy": "The Sinner's Stone", "class": "Currency", "type": "currency low"},
	"1 The Snuffed Flame": {"prophecy": "The Snuffed Flame", "class": "Currency", "type": "currency low"},
	"1 The Soulless Beast": {"prophecy": "The Soulless Beast", "class": "Currency", "type": "currency low"},
	"1 The Stockkeeper": {"prophecy": "The Stockkeeper", "class": "Currency", "type": "currency low"},
	"1 The Storm Spire": {"prophecy": "The Storm Spire", "class": "Currency", "type": "currency low"},
	"1 The Sword King's Passion": {"prophecy": "The Sword King's Passion", "class": "Currency", "type": "currency low"},
	"1 The Trembling Earth": {"prophecy": "The Trembling Earth", "class": "Currency", "type": "currency show"},
	"1 The Twins": {"prophecy": "The Twins", "class": "Currency", "type": "currency show"},
	"1 The Unbreathing Queen I": {"prophecy": "The Unbreathing Queen I", "class": "Currency", "type": "currency low"},
	"1 The Unbreathing Queen II": {"prophecy": "The Unbreathing Queen II", "class": "Currency", "type": "currency low"},
	"1 The Unbreathing Queen III": {"prophecy": "The Unbreathing Queen III", "class": "Currency", "type": "currency low"},
	"1 The Unbreathing Queen IV": {"prophecy": "The Unbreathing Queen IV", "class": "Currency", "type": "currency low"},
	"1 The Unbreathing Queen V": {"prophecy": "The Unbreathing Queen V", "class": "Currency", "type": "currency low"},
	"1 The Undead Brutes": {"prophecy": "The Undead Brutes", "class": "Currency", "type": "currency show"},
	"1 The Undead Storm": {"prophecy": "The Undead Storm", "class": "Currency", "type": "currency low"},
	"1 The Vanguard": {"prophecy": "The Vanguard", "class": "Currency", "type": "currency low"},
	"1 The Walking Mountain": {"prophecy": "The Walking Mountain", "class": "Currency", "type": "currency low"},
	"1 The Ward's Ward": {"prophecy": "The Ward's Ward", "class": "Currency", "type": "currency low"},
	"1 The Warmongers I": {"prophecy": "The Warmongers I", "class": "Currency", "type": "currency low"},
	"1 The Warmongers II": {"prophecy": "The Warmongers II", "class": "Currency", "type": "currency low"},
	"1 The Warmongers III": {"prophecy": "The Warmongers III", "class": "Currency", "type": "currency low"},
	"1 The Warmongers IV": {"prophecy": "The Warmongers IV", "class": "Currency", "type": "currency low"},
	"1 The Watcher's Watcher": {"prophecy": "The Watcher's Watcher", "class": "Currency", "type": "currency low"},
	"1 The Wealthy Exile": {"prophecy": "The Wealthy Exile", "class": "Currency", "type": "currency low"},
	"1 Touched by the Wind": {"prophecy": "Touched by the Wind", "class": "Currency", "type": "currency low"},
	"1 Trapped in the Tower": {"prophecy": "Trapped in the Tower", "class": "Currency", "type": "currency low"},
	"1 Trash to Treasure": {"prophecy": "Trash to Treasure", "class": "Currency", "type": "currency extremely high"},
	"1 Twice Enchanted": {"prophecy": "Twice Enchanted", "class": "Currency", "type": "currency show"},
	"1 Unbearable Whispers I": {"prophecy": "Unbearable Whispers I", "class": "Currency", "type": "currency low"},
	"1 Unbearable Whispers II": {"prophecy": "Unbearable Whispers II", "class": "Currency", "type": "currency low"},
	"1 Unbearable Whispers III": {"prophecy": "Unbearable Whispers III", "class": "Currency", "type": "currency low"},
	"1 Unbearable Whispers IV": {"prophecy": "Unbearable Whispers IV", "class": "Currency", "type": "currency low"},
	"1 Unbearable Whispers V": {"prophecy": "Unbearable Whispers V", "class": "Currency", "type": "currency low"},
	"1 Undead Uprising": {"prophecy": "Undead Uprising", "class": "Currency", "type": "currency low"},
	"1 Unnatural Energy": {"prophecy": "Unnatural Energy", "class": "Currency", "type": "currency low"},
	"1 Vaal Invasion": {"prophecy": "Vaal Invasion", "class": "Currency", "type": "currency low"},
	"1 Vaal Winds": {"prophecy": "Vaal Winds", "class": "Currency", "type": "currency show"},
	"1 Visions of the Drowned": {"prophecy": "Visions of the Drowned", "class": "Currency", "type": "currency low"},
	"1 Vital Transformation": {"prophecy": "Vital Transformation", "class": "Currency", "type": "currency low"},
	"1 Waiting in Ambush": {"prophecy": "Waiting in Ambush", "class": "Currency", "type": "currency show"},
	"1 Weeping Death": {"prophecy": "Weeping Death", "class": "Currency", "type": "currency low"},
	"1 Wind and Thunder": {"prophecy": "Wind and Thunder", "class": "Currency", "type": "currency show"},
	"1 Winter's Mournful Melodies": {"prophecy": "Winter's Mournful Melodies", "class": "Currency", "type": "currency low"},
}
