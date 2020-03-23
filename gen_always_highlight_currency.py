import json
from copy import deepcopy

import requests
from datetime import datetime
from bs4 import BeautifulSoup
from item_config.challenges import gen_moo


def create_always_highlight():
	currencytab = "0"  # Update to the tabid(s) where you keep your currency
	league = "Delirium"
	accountname = ""
	cookies = {'POESESSID': ''}  # update to your session id, blank session id will use default(on) highlighting rules

	if cookies['POESESSID']:
		requester = requests.session()
	else:
		requester = None
	create_highlight_currency(currencytab, league, accountname, cookies, requester)
	create_highlight_challenge(accountname, league, cookies, requester)


# Uses your session id (if provided) to change always highlight settings for currency
def create_highlight_currency(currencytab, league, accountname, cookies, requester):
	currencyvals = {  # update to currencies that you want to have shown and thresholds for them. -1 to always highlight
		"Simple Sextant": -1,
		"Cartographer's Chisel": -1,
		'Exalted Orb': -1,
		'Divine Orb': -1,
		"Prime Sextant": -1,
		"Awakened Sextant": -1,
		'Orb of Annulment': -1,
		'Orb of Binding': 5,
		"Ancient Orb": -1,
		"Armourer's Scrap": 160,
		"Blacksmith's Whetstone": 80,
		"Blessed Orb": 100,
		"Chaos Orb": -1,
		"Chromatic Orb": 1000,
		"Engineer's Orb": 20,
		"Gemcutter's Prism": 100,
		"Glassblower's Bauble": 100,
		"Jeweller's Orb": 350,
		"Orb of Alchemy": 100,
		"Orb of Alteration": -1,
		"Orb of Augmentation": 500,
		"Orb of Chance": 500,
		"Orb of Fusing": -1,
		"Orb of Horizons": 50,
		"Orb of Regret": 100,
		"Orb of Scouring": 100,
		"Orb of Transmutation": 500,
		"Perandus Coin": -1,
		"Portal Scroll": 40,
		"Regal Orb": 100,
		"Scroll of Wisdom": 100,
		"Silver Coin": 200,
		"Vaal Orb": -1,
	}

	shards = {
		"Orb of Alchemy": ["Alchemy Shard", "Orb of Binding", "Binding Shard"],
		"Orb of Alteration": ["Alteration Shard"],
		"Orb of Horizons": ["Horizon Shard"],
		"Engineer's Orb": ["Engineer's Shard"],
		"Regal Orb": ["Regal Shard"],
		"Orb of Regret": ['Orb of Scouring'],
		"Orb of Scouring": ["Orb of Chance"],
		"Scroll of Wisdom": ["Armourer's Scrap", "Blacksmith's Whetstone", "Orb of Transmutation"],
		"Chaos Orb": ["Chaos Shard"]
	}

	currency = list(currencyvals.keys())
	if cookies['POESESSID']:
		request = f'https://www.pathofexile.com/character-window/get-stash-items?league={league}&realm=pc&accountName={accountname}&tabs=0&tabIndex={currencytab}'

		req = requester.post(request, cookies=cookies)

		data = json.loads(req.content)
		skipped = set()
		for item in data['items']:
			if item['typeLine'] in currencyvals and currencyvals[item['typeLine']] < item['stackSize'] and currencyvals[item['typeLine']] != -1:
				currency.pop(currency.index(item['typeLine']))
			elif item['typeLine'] not in currencyvals and 'Oil' not in item['typeLine'] and 'Shard' not in item['typeLine'] and 'Fragment' not in item['typeLine']:
				skipped.add(item['typeLine'])
		print(f"Skipped determining always show for: {sorted(skipped)}")

	for shard in shards:
		if shard in currency:
			currency.extend(shards[shard])

	currency = list(set(currency))
	currency.sort()
	currency_text = '",\n\t"'.join(currency)
	with open("auto_gen/always_highlight.py", "w") as f:
		f.write(f'#!/usr/bin/python\n# -*- coding: utf-8 -*-\n# Created: {datetime.utcnow().strftime("%m/%d/%Y(m/d/y) %H:%M:%S")} UTC from "{league}" data\n\nauto_ah = [\n\t"{currency_text}"\n]\n')


def create_highlight_challenge(accountname, league, cookies, requester):
	# These highlight rules are selected to bring more attention to cards/items that may be overlooked.  If something is already valuable then it is not included.
	highlights = {
		'Complete Unique Maps': {
			'base': {"other": ["Rarity Unique"], "type": "challenge high"},
			'vals': {
				"Acton's Nightmare": [{"baseexact": "Overgrown Shrine Map"}],
				"Caer Blaidd, Wolfpack's Den": [{"baseexact": "Underground River Map"}],
				'Death and Taxes': [{"baseexact": "Necropolis Map"}],
				"Doryani's Machinarium": [{"baseexact": "Maze Map"}],
				'Hall of Grandmasters': [{"baseexact": "Promenade Map"}],
				'Hallowed Ground': [{"baseexact": "Cemetery Map"}],
				'Maelström of Chaos': [{"baseexact": "Atoll Map"}],
				'Mao Kun': [{"baseexact": "Shore Map"}],
				"Oba's Cursed Trove": [{"baseexact": "Underground Sea Map"}],
				"Olmec's Sanctum": [{"baseexact": "Bone Crypt Map"}],
				'Perandus Manor': [{"baseexact": "Chateau Map"}],
				'Pillars of Arun': [{"baseexact": "Dunes Map"}],
				"Poorjoy's Asylum": [{"baseexact": "Temple Map"}],
				"The Coward's Trial": [{"baseexact": "Cursed Crypt Map"}],
				'The Putrid Cloister': [{"baseexact": "Museum Map"}],
				'The Twilight Temple': [{"baseexact": "Moon Temple Map"}],
				'The Vinktar Square': [{"baseexact": "Courtyard Map"}],
				'Vaults of Atziri': [{"baseexact": "Vaal Pyramid Map"}],
				'Whakawairua Tuahu': [{"baseexact": "Strand Map"}]
			},
		},
		'Complete Unidentified Maps': {
			'base': {"class": "Maps", "other": ["Rarity Rare", "Identified False"], "type": "challenge high"},
			'vals': {
				"Tier 1": [{"other": ["MapTier = 1"]}],
				"Tier 2": [{"other": ["MapTier = 2"]}],
				"Tier 3": [{"other": ["MapTier = 3"]}],
				"Tier 4": [{"other": ["MapTier = 4"]}],
				"Tier 5": [{"other": ["MapTier = 5"]}],
				"Tier 6": [{"other": ["MapTier = 6"]}],
				"Tier 7": [{"other": ["MapTier = 7"]}],
				"Tier 8": [{"other": ["MapTier = 8"]}],
				"Tier 9": [{"other": ["MapTier = 9"]}],
				"Tier 10": [{"other": ["MapTier = 10"]}],
				"Tier 11": [{"other": ["MapTier = 11"]}],
				"Tier 12": [{"other": ["MapTier = 12"]}],
				"Tier 13": [{"other": ["MapTier = 13"]}],
				"Tier 14": [{"other": ["MapTier = 14"]}],
				"Tier 15": [{"other": ["MapTier = 15"]}],
				"Tier 16": [{"other": ["MapTier = 16"]}]
			}
		},
		'Complete Twinned Maps': {
			'base': {"class": "Maps", "other": ["HasExplicitMod Twinned"], "type": "challenge high"},
			'vals': {
				"Tier 1": [{"other": ["MapTier = 1"]}],
				"Tier 2": [{"other": ["MapTier = 2"]}],
				"Tier 3": [{"other": ["MapTier = 3"]}],
				"Tier 4": [{"other": ["MapTier = 4"]}],
				"Tier 5": [{"other": ["MapTier = 5"]}],
				"Tier 6": [{"other": ["MapTier = 6"]}],
				"Tier 7": [{"other": ["MapTier = 7"]}],
				"Tier 8": [{"other": ["MapTier = 8"]}],
				"Tier 9": [{"other": ["MapTier = 9"]}],
				"Tier 10": [{"other": ["MapTier = 10"]}],
				"Tier 11": [{"other": ["MapTier = 11"]}],
				"Tier 12": [{"other": ["MapTier = 12"]}],
				"Tier 13": [{"other": ["MapTier = 13"]}],
				"Tier 14": [{"other": ["MapTier = 14"]}],
				"Tier 15": [{"other": ["MapTier = 15"]}],
				"Tier 16": [{"other": ["MapTier = 16"]}]
			}
		},
		'Turn in Divination Cards': {
			'base': {"class": "Divination Card", "other": [], "type": "challenge high"},
			'vals': {
				"Bow": [{"baseexact": "Imperial Legacy"}, {"baseexact": "The Porcupine"}, {"baseexact": "The Blazing Fire"}, {"baseexact": "Thunderous Skies"}, {"baseexact": "Tranquillity"}, {"baseexact": "Anarchy's Price"}, {"baseexact": "Hunter's Resolve"}],
				"Divination Card": [{"baseexact": "The Gambler"}],
				"Essence": [{"baseexact": "Harmony of Souls"}, {"baseexact": "The Cacophony"}, {"baseexact": "Three Voices"}],
				"Gem": [{"baseexact": "Volatile Power"}, {"baseexact": "Dialla's Subjugation"}, {"baseexact": "Gemcutter's Promise"}, {"baseexact": "The Summoner"}, {"baseexact": "The Cataclysm"}, {"baseexact": "Gift of the Gemling Queen"}, {"baseexact": "The Fox"}, {"baseexact": "The Skeleton"}, {"baseexact": "Grave Knowledge"}, {"baseexact": "The Realm"}, {"baseexact": "The Doppelganger"}],
				"Map": [{"baseexact": "Rain Tempter"}, {"baseexact": "Boundless Realms"}, {"baseexact": "The Surveyor"}, {"baseexact": "Cartographer's Delight"}, {"baseexact": "Scholar of the Seas"}, {"baseexact": "The Dreamland"}, {"baseexact": "The Twilight Moon"}, {"baseexact": "The Wolf's Legacy"}, {"baseexact": "Treasure Hunter"}, {"baseexact": "The Encroaching Darkness"}],
				"Ring": [{"baseexact": "The Metalsmith's Gift"}, {"baseexact": "Lantador's Lost Love"}, {"baseexact": "The Opulent"}, {"baseexact": "Glimmer of Hope"}, {"baseexact": "The Penitent"}, {"baseexact": "Hubris"}, {"baseexact": "Blind Venture"}, {"baseexact": "Prosperity"}],
				"Corrupted Gem": [{"baseexact": "The Dragon's Heart"}, {"baseexact": "The Artist"}, {"baseexact": "Wealth and Power"}, {"baseexact": "The Skeleton"}, {"baseexact": "The Wilted Rose"}, {"baseexact": "The Rite of Elements"}, {"baseexact": "The Cataclysm"}, {"baseexact": "The Bones"}, {"baseexact": "Deathly Designs"}, {"baseexact": "Dialla's Subjugation"}, {"baseexact": "Volatile Power"}],
				"Itemlevel 100 Item": [{"baseexact": "Imperial Legacy"}, {"baseexact": "The Celestial Stone"}, {"baseexact": "The Sacrifice"}, {"baseexact": "The Dapper Prodigy"}, {"baseexact": "Nook's Crown"}, {"baseexact": "Destined to Crumble"}, {"baseexact": "The Hale Heart"}, {"baseexact": "Perfection"}, {"baseexact": "The Opulent"}, {"baseexact": "The Golden Era"}, {"baseexact": "The Undisputed"}, {"baseexact": "The Jester"}, {"baseexact": "Merciless Armament"}, {"baseexact": "The Tyrant"}, {"baseexact": "The Spoiled Prince"}, {"baseexact": "The Archmage's Right Hand"}, {"baseexact": "The Road to Power"}, {"baseexact": "Void of the Elements"}],
				"Jewel": [{"baseexact": "The Mountain"}, {"baseexact": "Azyran's Reward"}, {"baseexact": "The Garish Power"}, {"baseexact": "The Eye of the Dragon"}, {"baseexact": "The Primordial"}, {"baseexact": "The Endurance"}, {"baseexact": "Shard of Fate"}],
				"Prophecy": [{"baseexact": "Akil's Prophecy"}, {"baseexact": "Friendship"}, {"baseexact": "The Side Quest"}, {"baseexact": "Vile Power"}, {"baseexact": "Immortal Resolve"}, {"baseexact": "The Valley of Steel Boxes"}, {"baseexact": "The Jeweller's Boon"}, {"baseexact": "The Mad King"}, {"baseexact": "The Iron Bard"}, {"baseexact": "Beauty Through Death"}],
				"Rare Item": [{"baseexact": "Nook's Crown"}, {"baseexact": "Destined to Crumble"}, {"baseexact": "The Hale Heart"}, {"baseexact": "Perfection"}, {"baseexact": "The Opulent"}, {"baseexact": "Dark Dreams"}, {"baseexact": "Lingering Remnants"}, {"baseexact": "Lantador's Lost Love"}, {"baseexact": "The Warden"}, {"baseexact": "The Lover"}, {"baseexact": "The Explorer"}, {"baseexact": "The Trial"}, {"baseexact": "Left to Fate"}, {"baseexact": "Call to the First Ones"}]
			}
		}
	}

	if cookies['POESESSID']:
		request = f'https://www.pathofexile.com/account/view-profile/{accountname}/challenges?season={league}'
		req = requester.post(request, cookies=cookies)
		text = req.content.decode("utf-8")
		soup = BeautifulSoup(text, 'html.parser')
		challenges = {}
		for challenge in soup.find_all("div", class_="incomplete"):
			title = challenge.h2.text
			challenges[title] = []
			for val in challenge.find_all("li", class_=""):
				challenges[title].append(val.get_text().strip())

		results = {}
		for chal in challenges:
			if chal in highlights:
				for val in challenges[chal]:
					if val in highlights[chal]['vals']:
						for c, item in enumerate(highlights[chal]['vals'][val]):
							key = f'0 {chal} - {val} - {c}'
							results[key] = deepcopy(highlights[chal]['base'])
							if 'other' in item:
								results[key]['other'].extend(item['other'])
								del item['other']
							results[key] = {**results[key], **item}
							results[key]['other'].append(gen_moo('high'))
					else:
						print(f"Not handling {chal} - {val}")
			else:
				print(f"Not handling custom alerts for: {chal}")
	else:
		results = {}
		for chal in highlights:
			for val in highlights[chal]['vals']:
				for c, item in enumerate(highlights[chal]['vals'][val]):
					key = f'0 {chal} - {val} - {c}'
					results[key] = deepcopy(highlights[chal]['base'])
					if 'other' in item:
						results[key]['other'].extend(item['other'])
						del item['other']
					results[key] = {**results[key], **item}
					results[key]['other'].append(gen_moo('high'))

	header = '''#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: {} UTC from "{}" data
'''
	buf = '''{}\ndesc = "Challenge Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))
	for item in sorted(results):
		buf += f'\t"{item}": {results[item]},\n'
	buf += u'}\n'

	with open('auto_gen\\custom_challenge.py', 'w', encoding='utf-8') as f:
		f.write(buf)
