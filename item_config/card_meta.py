# Implemented tags
# '5l', '6l', 'amulet', 'awakened', 'belt', 'body armour', 'boot', 'bow', 'corrupt', 'crusader', 'currency', 'dagger', 'div', 'double-influenced',
# 'elder', 'enchanted', 'essence', 'fishing', 'flask', 'fragment', 'gem', 'glove', 'helmet', 'hunter', 'ilvl100', 'influenced', 'jewel', 'jewellery',
# 'jewellry', 'magic', 'map', 'prophecy', 'quiver', 'rare', 'ring', 'scarab', 'sceptre', 'shaper', 'shield', 'staff', 'thrusting sword', 'two-implicit',
# 'unique', 'wand', 'white'

card_meta = {
	"A Dab of Ink": {'unique', 'wand'},  # The Poet's Pen
	"A Familiar Call": {'magic', 'shaper', 'influenced', 'hunter', 'ilvl100'},  # Jewellery of Farrul|Item Level: 100|Shaper + Hunter Item
	"A Mother's Parting Gift": {'unique', 'jewel'},  # Fertile Mind
	"A Note in the Wind": {'prophecy'},  # Song of the Sekhema
	"Abandoned Wealth": {'currency'},  # 3x Exalted Orb
	"Akil's Prophecy": {'prophecy'},  # Fated Unique Item
	"Alluring Bounty": {'currency'},  # 10x Exalted Orb
	"Alone in the Darkness": {'unique'},  # Delve Item
	"Anarchy's Price": {'unique', 'corrupt', 'bow'},  # Voltaxic Rift|Corrupted
	"Arrogance of the Vaal": {'unique', 'corrupt', 'two-implicit'},  # Item| Two-Implicit| Corrupted
	"Assassin's Favour": {'unique', 'dagger'},  # Dagger
	"Atziri's Arsenal": {'unique', 'corrupt'},  # Weapon|Corrupted
	"Audacity": {'unique', 'corrupt', 'glove'},  # Doryani's Fist|Corrupted
	"Azyran's Reward": {'unique', 'corrupt', 'jewel'},  # Prismatic Jewel|Corrupted
	"Baited Expectations": {'unique', 'fishing'},  # Fishing Item
	"Beauty Through Death": {'prophecy'},  # Queen's Sacrifice
	"Blessing of God": {'magic', 'jewellry'},  # Elreon's Jewellery|Item Level: 85
	"Blind Venture": {'unique', 'corrupt', 'ring'},  # Ring|Corrupted
	"Boon of Justice": {'white', 'fragment'},  # Offering to the Goddess
	"Boon of the First Ones": {'unique'},  # Bestiary Item
	"Boundless Realms": {'white', 'map'},  # Map
	"Bowyer's Dream": {'white', '6l', 'bow'},  # Six-Link Harbinger Bow|Item Level: 91
	"Buried Treasure": {'white', 'scarab', 'fragment'},  # Sulphite Scarab
	"Burning Blood": {'unique', 'corrupt', 'amulet'},  # Xoph's Blood|Corrupted
	"Call to the First Ones": {'rare', 'corrupt', 'amulet'},  # Tier 1 Talisman|Corrupted
	"Cameria's Cut": {'white', 'scarab', 'fragment'},  # Scarab
	"Cartographer's Delight": {'map'},  # Map|Map Tier: 5
	"Chaotic Disposition": {'currency'},  # 5x Chaos Orb
	"Council of Cats": {'unique'},  # Farrul Item
	"Coveted Possession": {'currency'},  # 5x Regal Orb
	"Dark Dreams": {'rare', 'elder', 'influenced', 'helmet'},  # Bone Helmet|Elder Item
	"Dark Temptation": {'unique', 'wand'},  # Obliteration
	"Death": {'unique', 'sceptre'},  # Mon'tregul's Grasp
	"Deathly Designs": {'corrupt', 'gem'},  # Level 21 Trap Gem|Quality: +23%|Corrupted
	"Demigod's Wager": {'currency'},  # Orb of Annulment
	"Destined to Crumble": {'rare', 'ilvl100'},  # Body Armour|Item Level: 100
	"Dialla's Subjugation": {'corrupt', 'gem'},  # Superior Support Gem|Quality: +23%|Corrupted
	"Divine Justice": {'unique', 'enchanted', 'helmet'},  # Helmet|Eternal Labyrinth Enchantment
	"Doedre's Madness": {'unique'},  # Doedre Item
	"Earth Drinker": {'unique', 'flask'},  # Granite Flask
	"Echoes of Love": {'unique', 'corrupt', 'two-implicit', 'thrusting sword'},  # Fidelitas' Spike| Two-Implicit| Corrupted
	"Emperor of Purity": {'white', '6l', 'body armour'},  # Six-Link Holy Chainmail|Item Level: 60
	"Emperor's Luck": {'currency'},  # 5x Currency
	"Etched in Blood": {'unique', 'corrupt', 'two-implicit', 'quiver'},  # Rigwald's Quills|Two-Implicit|Corrupted
	"Forbidden Power": {'unique', 'corrupt', 'sceptre'},  # Balefire|Corrupted
	"Friendship": {'prophecy'},  # A Master Seeks Help (Niko)
	"Gemcutter's Promise": {'gem'},  # Superior Gem|Quality: +20%
	"Gift of Asenath": {'unique', 'corrupt', 'two-implicit', 'glove'},  # Asenath's Gentle Touch|Two-Implicit|Corrupted
	"Gift of the Gemling Queen": {'gem'},  # Level 20 Support Gem
	"Glimmer of Hope": {'unique', 'ring'},  # Gold Ring
	"Grave Knowledge": {'gem'},  # Summon Raging Spirit|Quality: +20%
	"Harmony of Souls": {'currency', 'essence'},  # 9x Shrieking Essence
	"Her Mask": {'white', 'fragment'},  # Sacrifice Fragment
	"Heterochromia": {'unique', 'ring'},  # Two-Stone Ring
	"Hope": {'unique', 'corrupt', 'ring'},  # Prismatic Ring|Corrupted
	"House of Mirrors": {'currency'},  # Mirror of Kalandra
	"Hubris": {'unique', 'ring'},  # Ring
	"Humility": {'unique', '6l'},  # Tabula Rasa
	"Hunter's Resolve": {'unique', 'bow'},  # Bow
	"Hunter's Reward": {'unique', 'ring'},  # The Taming
	"Immortal Resolve": {'prophecy'},  # Fated Connections
	"Imperial Legacy": {'white', '6l', 'ilvl100', 'bow'},  # Six-Link Imperial Bow|Item Level: 100
	"Jack in the Box": {'unique'},  # Item
	"Lantador's Lost Love": {'rare', 'ring'},  # Two-Stone Ring
	"Last Hope": {'white'},  # Mortal Hope
	"Left to Fate": {'rare', 'corrupt', 'map'},  # Map|Map Tier: 16|Unidentified Corrupted
	"Light and Truth": {'unique', 'sceptre'},  # Crystal Sceptre
	"Lingering Remnants": {'rare', 'corrupt', 'map'},  # Vaal Temple Map|Item Level: 83|Corrupted
	"Lost Worlds": {'white', 'map'},  # Map|Map Tier: 15
	"Loyalty": {'currency'},  # 3x Orb of Fusing
	"Lucky Connections": {'currency'},  # 20x Orb of Fusing
	"Lucky Deck": {'currency'},  # 10x Stacked Deck
	"Lysah's Respite": {'unique', 'corrupt', 'amulet'},  # Agate Amulet|Corrupted
	"Mawr Blaidd": {'unique', 'amulet'},  # Eyes of the Greatwolf
	"Merciless Armament": {'magic', 'ilvl100'},  # Merciless Two-Hand Weapon|Item Level: 100
	"Might is Right": {'unique'},  # Trypanon
	"Mitts": {'unique', 'glove'},  # Gloves
	"Monochrome": {'currency'},  # 10x Sextant
	"More is Never Enough": {'white', 'scarab', 'fragment'},  # Gilded Scarab
	"No Traces": {'currency'},  # 30x Orb of Scouring
	"Nook's Crown": {'rare', 'elder', 'influenced', 'ilvl100'},  # Bone Helmet|Item Level: 100|Elder Item
	"Peaceful Moments": {'unique', 'jewel'},  # Timeless Jewel
	"Perfection": {'rare', 'shaper', 'influenced', 'ilvl100', 'jewellery'},  # Jewellery|Item Level: 100|Shaper Item
	"Pride Before the Fall": {'unique', 'corrupt', 'body armour'},  # Kaom's Heart|Corrupted
	"Pride of the First Ones": {'unique', 'body armour'},  # Farrul's Fur
	"Prometheus' Armoury": {'rare', 'double-influenced', 'influenced', 'ilvl100'},  # One-Hand Weapon|Item Level: 100|Double-Influenced Item
	"Prosperity": {'magic', 'ring'},  # Perandus' Gold Ring
	"Rain Tempter": {'white', 'map'},  # Strand Map|Item Level: 73
	"Rain of Chaos": {'currency'},  # Chaos Orb
	"Rats": {'unique', 'helmet'},  # Rat's Nest
	"Rebirth": {'unique', '6l'},  # Charan's Sword
	"Remembrance": {'unique', 'corrupt', 'ring'},  # Precursor's Emblem|Corrupted
	"Sambodhi's Vow": {'white', 'fragment'},  # Mortal Fragment
	"Scholar of the Seas": {'unique', 'map'},  # Mao Kun
	"Seven Years Bad Luck": {'currency'},  # Mirror Shard
	"Shard of Fate": {'magic', 'jewel'},  # Vivid Jewel
	"Squandered Prosperity": {'unique', 'corrupt', 'map'},  # Perandus Manor|Watchstone Count: 4|Corrupted
	"Struck by Lightning": {'magic', 'jewellery'},  # Electrocuting Jewellery|Item Level: 76
	"Succor of the Sinless": {'unique', 'flask'},  # Bottled Faith
	"The Admirer": {'unique'},  # Atziri Item
	"The Aesthete": {'unique'},  # Shavronne Item
	"The Archmage's Right Hand": {'magic', 'ilvl100', 'wand'},  # Glyphic Prophecy Wand|Item Level: 100
	"The Arena Champion": {'white', 'map'},  # Colosseum Map
	"The Army of Blood": {'unique', 'body armour'},  # Bloodbond
	"The Artist": {'corrupt', 'gem'},  # Level 4 Enhance|Corrupted
	"The Avenger": {'unique', 'corrupt'},  # Mjölner|Corrupted
	"The Awakened": {'rare', 'double-influenced', 'influenced', 'jewellery'},  # Jewellery|Item Level: 86|Double-Influenced Item
	"The Bargain": {'fragment'},  # Pure Breachstone
	"The Battle Born": {'unique'},  # Axe
	"The Beast": {'unique', 'body armour'},  # Belly of the Beast
	"The Betrayal": {'unique', 'glove'},  # Maligaro's Virtuosity
	"The Blazing Fire": {'unique', 'bow'},  # Chin Sol
	"The Body": {'unique', 'body armour'},  # Body Armour
	"The Bones": {'corrupt', 'gem'},  # Level 21 Vaal Summon Skeletons|Corrupted
	"The Breach": {'unique'},  # Breach Item
	"The Brittle Emperor": {'unique', 'corrupt', 'amulet'},  # Voll's Devotion|Corrupted
	"The Cacophony": {'currency', 'essence'},  # 3x Deafening Essence
	"The Calling": {'unique'},  # Beyond Item
	"The Carrion Crow": {'magic'},  # Life Armour
	"The Cartographer": {'currency'},  # 10x Cartographer's Chisel
	"The Cataclysm": {'corrupt', 'gem'},  # Level 21 Spell Gem|Corrupted
	"The Catalyst": {'currency'},  # Vaal Orb
	"The Celestial Justicar": {'white', '6l'},  # Six-Link Astral Plate
	"The Celestial Stone": {'white', 'shaper', 'influenced', 'ring', 'ilvl100'},  # Opal Ring|Item Level: 100|Shaper Item
	"The Chains that Bind": {'white', '6l'},  # Six-Link Body Armour
	"The Cheater": {'corrupt', 'gem', 'awakened'},  # Level 6 Awakened Support Gem|Quality: +20%|Corrupted
	"The Chosen": {'unique', 'corrupt', '6l'},  # Skin of the Lords|Corrupted
	"The Coming Storm": {'unique', 'body armour'},  # Lightning Coil
	"The Conduit": {'unique', 'glove'},  # Doryani's Fist
	"The Craving": {'unique', 'jewel'},  # Unending Hunger
	"The Cursed King": {'unique', 'amulet'},  # Rigwald's Curse
	"The Damned": {'unique'},  # Soul Ripper
	"The Dapper Prodigy": {'white', '6l', 'ilvl100'},  # Six-Link Body Armour|Item Level: 100
	"The Dark Mage": {'white', '6l'},  # Six-Link Staff|Item Level: 55
	"The Darkest Dream": {'unique', 'corrupt'},  # Severed in Sleep|Corrupted
	"The Deal": {'white', 'scarab', 'fragment'},  # Cartography Scarab
	"The Deceiver": {'unique', 'corrupt', 'belt'},  # Belt of the Deceiver|Corrupted
	"The Deep Ones": {'unique'},  # Tidebreaker
	"The Demon": {'unique', 'corrupt', 'two-implicit', 'belt'},  # Headhunter|Two-Implicit|Corrupted
	"The Demoness": {'unique', 'sceptre'},  # Death's Hand
	"The Doctor": {'unique', 'belt'},  # Headhunter
	"The Doppelganger": {'gem'},  # Superior Mirror Arrow|Quality: +20%
	"The Dragon": {'unique', 'flask'},  # Coruscating Elixir
	"The Dragon's Heart": {'corrupt', 'gem'},  # Level 4 Empower|Corrupted
	"The Dreamer": {'unique'},  # Chayula Item
	"The Dreamland": {'unique', 'map'},  # Poorjoy's Asylum
	"The Drunken Aristocrat": {'unique', 'flask'},  # Divination Distillate
	"The Easy Stroll": {'rare', 'corrupt', 'map'},  # Terrace Map|Modifiers: 8|Corrupted
	"The Eldritch Decay": {'white', 'fragment'},  # Uber Elder Fragment
	"The Encroaching Darkness": {'unique', 'corrupt', 'map'},  # Map|Corrupted
	"The Endless Darkness": {'unique'},  # Voidforge
	"The Endurance": {'magic', 'jewel'},  # Vivid Crimson Jewel
	"The Enlightened": {'gem'},  # Level 3 Enlighten
	"The Escape": {'unique', 'boot'},  # Seven-League Step
	"The Ethereal": {'white', '6l', 'body armour'},  # Six-Link Vaal Regalia
	"The Explorer": {'rare', 'corrupt', 'map'},  # Map|Corrupted
	"The Eye of Terror": {'fragment'},  # Pure Chayula Breachstone
	"The Eye of the Dragon": {'unique', 'corrupt', 'jewel'},  # Jewel|Corrupted
	"The Fathomless Depths": {'unique', 'helmet'},  # Lightpoacher
	"The Feast": {'unique', 'corrupt', 'ring'},  # Romira's Banquet|Corrupted
	"The Fiend": {'unique', 'corrupt', 'belt'},  # Headhunter|Corrupted
	"The Fishmonger": {'white', 'currency'},  # Albino Rhoa Feather
	"The Fletcher": {'unique', 'corrupt', 'quiver'},  # Drillneck|Corrupted
	"The Flora's Gift": {'white', '5l', 'staff'},  # Five-Link Staff|Item Level: 66
	"The Fool": {'currency'},  # 20x Orb of Chance
	"The Formless Sea": {'unique'},  # Varunastra
	"The Forsaken": {'unique', 'belt'},  # Umbilicus Immortalis
	"The Fox": {'gem'},  # Level 20 Gem
	"The Gambler": {'div'},  # Divination Card
	"The Garish Power": {'unique', 'jewel'},  # Jewel
	"The Gemcutter": {'currency'},  # Gemcutter's Prism
	"The Gentleman": {'unique', 'corrupt'},  # Sword|Corrupted
	"The Gladiator": {'unique', 'helmet'},  # Nightmare Bascinet
	"The Golden Era": {'magic', 'ilvl100', 'staff'},  # Flaring Eclipse Staff|Item Level: 100
	"The Greatest Intentions": {'unique', 'corrupt', 'two-implicit'},  # The Saviour|Two-Implicit|Corrupted
	"The Hale Heart": {'rare', 'elder', 'influenced', 'ilvl100'},  # Item|Item Level: 100|Elder Item
	"The Harvester": {'unique'},  # The Harvest
	"The Hermit": {'unique', 'wand'},  # Lifesprig
	"The Heroic Shot": {'currency'},  # 17x Chromatic Orb
	"The Hive of Knowledge": {'unique', 'corrupt', 'two-implicit'},  # Machina Mitts|Two-Implicit|Corrupted
	"The Hoarder": {'currency'},  # Exalted Orb
	"The Hunger": {'unique', 'flask'},  # Taste of Hate
	"The Immortal": {'div'},  # House of Mirrors
	"The Incantation": {'unique', 'staff'},  # The Whispering Ice
	"The Innocent": {'currency'},  # 40x Orb of Regret
	"The Inoculated": {'magic', 'body armour'},  # Seraphim's Armour
	"The Insatiable": {'unique', 'corrupt'},  # The Harvest|Corrupted
	"The Inventor": {'currency'},  # 10x Vaal Orb
	"The Iron Bard": {'prophecy'},  # Trash to Treasure
	"The Jester": {'magic', 'ilvl100'},  # Merciless One-Hand Weapon|Item Level: 100
	"The Jeweller's Boon": {'prophecy'},  # The Jeweller's Touch
	"The Journey": {'currency'},  # Harbinger's Orb
	"The King's Blade": {'magic'},  # Bloodthirsty Eternal Sword|Item Level: 66
	"The King's Heart": {'unique', 'body armour'},  # Kaom's Heart
	"The Landing": {'unique', 'corrupt', 'map'},  # The Beachhead|Map Tier: 15|Corrupted
	"The Last One Standing": {'unique'},  # Atziri's Disfavour
	"The Lich": {'unique', 'corrupt', 'wand'},  # Midnight Bargain|Corrupted
	"The Life Thief": {'unique', 'amulet'},  # Zerphi's Heart
	"The Lion": {'unique', 'bow'},  # Lioneye Item
	"The Long Con": {'currency'},  # Elderslayer's Exalted Orb
	"The Lord in Black": {'magic', 'ring'},  # Ring of Bameth|Item Level: 83
	"The Lord of Celebration": {'magic', 'shaper', 'influenced', 'sceptre'},  # Sceptre of Celebration|Shaper Item
	"The Lover": {'rare', 'jewellery'},  # Jewellery|Item Level: 79
	"The Lunaris Priestess": {'unique', 'staff'},  # Sire of Shards
	"The Mad King": {'prophecy'},  # The King's Path
	"The Master Artisan": {'currency'},  # 20x Quality Currency
	"The Master": {'unique', 'amulet'},  # Bisco's Collar
	"The Mayor": {'unique', 'map'},  # The Perandus Manor|Watchstone Count: 4
	"The Mercenary": {'unique', 'corrupt', 'shield'},  # Shield|Corrupted
	"The Messenger": {'unique'},  # Harbinger Fragment
	"The Metalsmith's Gift": {'white', 'ring'},  # Prismatic Ring
	"The Mountain": {'magic', 'jewel'},  # Jewel of Potency
	"The Nurse": {'div'},  # The Doctor
	"The Oath": {'unique'},  # Death's Oath
	"The Obscured": {'fragment'},  # Breachstone
	"The Offering": {'unique', 'body armour'},  # Shavronne's Wrappings
	"The Old Man": {'rare', 'corrupt', 'two-implicit', 'fishing'},  # Fishing Rod|Two-Implicit|Corrupted
	"The One With All": {'unique', 'corrupt', 'ring'},  # Le Heup of All|Corrupted
	"The Opulent": {'rare', 'ring', 'ilvl100'},  # Ring|Item Level: 100
	"The Pack Leader": {'unique', 'helmet'},  # Alpha's Howl
	"The Pact": {'unique', 'staff'},  # Pledge of Hands
	"The Penitent": {'unique', 'ring'},  # Unset Ring
	"The Poet": {'unique', 'corrupt', 'amulet'},  # Blood of Corruption|Corrupted
	"The Polymath": {'unique', 'amulet'},  # Astramentis
	"The Porcupine": {'white', '6l', 'bow'},  # Six-Link Short Bow|Item Level: 50
	"The Price of Loyalty": {'unique', 'corrupt', 'two-implicit', 'body armour'},  # Skin of the Loyal|Item Level: 25|Two-Implicit|Corrupted
	"The Price of Protection": {'map'},  # Chateau Map|Watchstone Count: 4
	"The Primordial": {'unique', 'jewel'},  # Jewel|Primordial
	"The Professor": {'unique', 'map'},  # The Putrid Cloister
	"The Progeny of Lunaris": {'unique', 'flask'},  # Dying Sun
	"The Puzzle": {'currency'},  # 5x Breachstone Splinter
	"The Queen": {'unique', 'glove'},  # Atziri's Acuity
	"The Rabid Rhoa": {'magic'},  # Malicious Gemini Claw|Item Level: 83
	"The Realm": {'gem'},  # Superior Portal
	"The Risk": {'unique', 'ring'},  # Ventor's Gamble
	"The Rite of Elements": {'corrupt', 'gem'},  # Level 21 Golem Gem|Corrupted
	"The Road to Power": {'magic', 'ilvl100'},  # Runic One-Hand Weapon|Item Level: 100
	"The Ruthless Ceinture": {'unique', 'corrupt', 'belt'},  # Meginord's Girdle|Corrupted
	"The Sacrifice": {'white', '6l', 'ilvl100', 'body armour'},  # Six-Link Sacrificial Garb|Item Level: 100
	"The Saint's Treasure": {'currency'},  # 2x Exalted Orb
	"The Samurai's Eye": {'unique', 'jewel'},  # Watcher's Eye
	"The Scarred Meadow": {'unique', 'boot'},  # Wake of Destruction
	"The Scavenger": {'unique', 'body armour'},  # Carcass Jack
	"The Scholar": {'currency'},  # 40x Scroll of Wisdom
	"The Seeker": {'currency'},  # 3x Orb of Annulment
	"The Sephirot": {'currency'},  # 10x Divine Orb
	"The Side Quest": {'prophecy'},  # A Master Seeks Help
	"The Sigil": {'magic', 'amulet'},  # Unassailable Amulet
	"The Siren": {'unique', 'corrupt', 'staff'},  # The Whispering Ice|Corrupted
	"The Skeleton": {'corrupt', 'gem'},  # Level 1 Summon Skeletons|Quality: +23%|Corrupted
	"The Soul": {'unique'},  # Soul Taker
	"The Spark and the Flame": {'unique', 'ring'},  # Berek's Respite
	"The Spoiled Prince": {'magic', 'ilvl100', 'wand'},  # Dictator's Prophecy Wand|Item Level: 100
	"The Standoff": {'unique', 'belt'},  # Rustic Sash
	"The Stormcaller": {'unique', 'staff'},  # Agnerod Staff
	"The Strategist": {'unique', 'corrupt', 'jewel'},  # Inspired Learning|Corrupted
	"The Summoner": {'gem'},  # Superior Minion Gem|Quality: +20%
	"The Sun": {'unique', 'shield'},  # Rise of the Phoenix
	"The Surgeon": {'magic', 'flask'},  # Surgeon's Flask
	"The Surveyor": {'white', 'map'},  # Map|Map Tier: 14
	"The Survivalist": {'currency'},  # 7x Orb of Alchemy
	"The Sustenance": {'unique', 'corrupt', 'two-implicit', 'jewel'},  # Energy From Within|Two-Implicit|Corrupted
	"The Sword King's Salute": {'unique', 'amulet'},  # Daresso's Salute
	"The Thaumaturgist": {'unique', 'corrupt', 'ring'},  # Shavronne's Revelation|Corrupted
	"The Throne": {'unique', 'corrupt', 'boot'},  # Kaom's Roots|Corrupted
	"The Tinkerer's Table": {'currency'},  # 5x Fossil
	"The Tower": {'unique', 'staff'},  # Staff
	"The Traitor": {'unique', 'corrupt', 'wand'},  # Wand|Corrupted
	"The Trial": {'rare', 'corrupt', 'map'},  # Map|Map Tier: 15|Corrupted
	"The Tumbleweed": {'white', 'map'},  # Wasteland Map
	"The Twilight Moon": {'unique', 'map'},  # The Twilight Temple
	"The Twins": {'magic'},  # Gemini Claw of Celebration|Item Level: 83
	"The Tyrant": {'magic', 'ilvl100'},  # Merciless Weapon|Item Level: 100
	"The Undaunted": {'unique', 'corrupt'},  # Nemesis Item|Corrupted
	"The Undisputed": {'magic', 'elder', 'influenced', 'ilvl100'},  # Merciless Vaal Axe|Item Level: 100|Elder Item
	"The Union": {'currency'},  # 10x Gemcutter's Prism
	"The Valkyrie": {'unique'},  # Nemesis Item
	"The Valley of Steel Boxes": {'prophecy'},  # Monstrous Treasure
	"The Vast": {'unique', 'fishing'},  # Song of the Sirens
	"The Visionary": {'unique', 'body armour'},  # Lioneye's Vision
	"The Void": {},  # Random card turn in
	"The Warden": {'rare', 'corrupt', 'amulet'},  # Amulet|Corrupted
	"The Warlord": {'white', '6l'},  # Six-Link Coronal Maul|Item Level: 83
	"The Watcher": {'unique', 'helmet'},  # Crown of Eyes
	"The Web": {'magic'},  # Weapon of Crafting
	"The White Knight": {'white', 'crusader', 'influenced', '6l', 'ilvl100'},  # Six-Link Astral Plate|Item Level: 100|Crusader Item
	"The Wilted Rose": {'corrupt', 'gem'},  # Level 21 Aura Gem|Corrupted
	"The Wind": {'unique', 'bow'},  # Windripper
	"The Witch": {'unique', 'flask'},  # Kiara's Determination
	"The Wolf": {'unique'},  # Rigwald Item
	"The Wolf's Legacy": {'unique', 'map'},  # Vaults of Atziri
	"The Wolf's Shadow": {'unique'},  # Hyaon's Fury
	"The Wolven King's Bite": {'unique', 'quiver'},  # Rigwald's Quills
	"The Wolverine": {'unique', 'corrupt'},  # Claw|Corrupted
	"The World Eater": {'unique'},  # Starforge
	"The Wrath": {'currency'},  # 10x Chaos Orb
	"The Wretched": {'unique', 'belt'},  # Belt
	"Thirst for Knowledge": {'unique', 'amulet'},  # Gluttony
	"Three Faces in the Dark": {'currency'},  # 3x Chaos Orb
	"Three Voices": {'currency', 'essence'},  # 3x Essence
	"Thunderous Skies": {'unique', 'bow'},  # Storm Cloud
	"Time-Lost Relic": {'unique'},  # League-Specific Item
	"Tranquillity": {'unique', 'bow'},  # Voltaxic Rift
	"Treasure Hunter": {'unique', 'corrupt', 'map'},  # Vaults of Atziri|Corrupted
	"Turn the Other Cheek": {'unique', 'corrupt', 'jewel'},  # Pacifism|Corrupted
	"Underground Forest": {'currency'},  # 10x Awakened Sextant
	"Vanity": {'unique', 'corrupt', '6l', 'body armour'},  # Tabula Rasa|Corrupted
	"Vile Power": {'prophecy'},  # Ancient Doom
	"Vinia's Token": {'currency'},  # 10x Orb of Regret
	"Void of the Elements": {'magic', 'elder', 'influenced', 'ring', 'ilvl100'},  # Overpowering Opal Ring|Item Level: 100|Elder Item
	"Volatile Power": {'corrupt', 'gem'},  # Superior Vaal Gem|Quality: +20%|Corrupted
	"Wealth and Power": {'corrupt', 'gem'},  # Level 4 Enlighten|Corrupted
}