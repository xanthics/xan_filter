import json
from copy import deepcopy
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from item_config.card_meta import card_meta
from item_config.gen_item_lists import bases


def create_always_highlight():
	currencytab = "0"  # Update to the tabid(s) where you keep your currency
	ex_shard_tab = "5"
	league = "Expedition"
	accountname = "xanqos"
	cookies = {'POESESSID': ''}  # update to your session id, blank session id will use default(on) highlighting rules
	header = {
		'User-Agent': 'xan.filter)',
		'From': 'xanthics on discord'
	}
	if cookies['POESESSID']:
		requester = requests.session()
	else:
		requester = None
#	create_highlight_currency(currencytab, league, accountname, cookies, header, requester)
#	create_highlight_challenge(accountname, league, cookies, header, requester)
	create_highlight_ex_recipe(ex_shard_tab, league, accountname, cookies, header, requester)


# Given a tab, determine what items it is missing for a full ex shard recipe and create highlighting rules
def create_highlight_ex_recipe(ex_shard_tab, league, accountname, cookies, header, requester):
	# Prime our lookups so we can see what is missing
	needed = {k: ["Crusader", "Elder", "Hunter", "Redeemer", "Shaper", "Warlord"] for k in ["Two Hand\" \"Staves\" \"Bow", 'Helmet', 'Body Armour', 'Gloves', 'Boots', 'Amulet', 'Ring', 'Belt']}
	base_lookup = {}
	for typ in bases:
		for modset in bases[typ]:
			group = ''
			if any(x in modset.lower() for x in ["two hand", "stave", "bow"]):
				group = "Two Hand\" \"Staves\" \"Bow"
			elif any(x in modset for x in ['Helmet', 'Body Armour', 'Gloves', 'Boots', 'Amulet', 'Ring', 'Belt']):
				group = bases[typ][modset][0]['base']
			if group:
				for item in bases[typ][modset]:
					base_lookup[item['name']] = group

	if cookies['POESESSID']:
		request = f'https://www.pathofexile.com/character-window/get-stash-items?league={league}&realm=pc&accountName={accountname}&tabs=0&tabIndex={ex_shard_tab}'

		req = requester.post(request, cookies=cookies, headers=header)
		if req.status_code == 200:
			data = json.loads(req.content)
			if 'items' in data:
				for item in data['items']:
					if 'influences' in item:
						typ = base_lookup[item['baseType']]
						if typ in ['Amulet', 'Ring', 'Belt']:
							continue
						inf = [k.capitalize() for k in item['influences']]
						for infl in inf:
							if infl in needed[typ]:
								needed[typ].remove(infl)
							else:
								print(f"Found influenced item that is not needed: {inf}, {typ}")
			else:
				print(f"Error: {req.reason} - {repr(data)}")
		else:
			print(f"Error code {req.status_code}: {req.reason}")

	header = '''#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: {} UTC from "{}" data
'''
	buf = '''{}\ndesc = "Ex Shard Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))
	for item in sorted(needed):
		infl = ' '.join(needed[item])
		buf += f"\t'0 {item}': {{'class': '{item}', 'other': ['HasInfluence {infl}', 'Rarity Rare', 'Identified False'], 'type': 'recipe item rare'}},\n"
	buf += u'}\n'

	with open('autogen\\custom_ex_shard_recipe.py', 'w', encoding='utf-8') as f:
		f.write(buf)


# Uses your session id (if provided) to change always highlight settings for currency
def create_highlight_currency(currencytab, league, accountname, cookies, header, requester):
	currencyvals = {  # update to currencies that you want to have shown and thresholds for them. -1 to always highlight but doesn't highlight shards
		"Simple Sextant": -1,
		"Cartographer's Chisel": -1,
		'Exalted Orb': 9999,
		'Divine Orb': -1,
		"Prime Sextant": -1,
		"Awakened Sextant": -1,
		'Orb of Annulment': 9999,
		'Orb of Binding': 150,
		"Ancient Orb": 50,
		"Armourer's Scrap": 160,
		"Blacksmith's Whetstone": 80,
		"Blessed Orb": 100,
		"Chaos Orb": 500,
		"Chromatic Orb": 500,
		"Engineer's Orb": 20,
		"Gemcutter's Prism": 100,
		"Glassblower's Bauble": 60,
		"Harbinger's Orb": 9999,
		"Jeweller's Orb": 350,
		"Orb of Alchemy": 150,
		"Orb of Alteration": 1000,
		"Orb of Augmentation": 500,
		"Orb of Chance": 250,
		"Orb of Fusing": 1500,
		"Orb of Horizons": 50,
		"Orb of Regret": 100,
		"Orb of Scouring": -1,
		"Orb of Transmutation": 500,
		"Perandus Coin": -1,
		"Portal Scroll": 40,
		"Regal Orb": 100,
		"Scroll of Wisdom": 100,
		"Silver Coin": 200,
		"Vaal Orb": 200,
		"Stacked Deck": -1,
		"Rogue's Marker": 1,
		'Enkindling Orb': 40,
		'Instilling Orb': 40
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
		"Chaos Orb": ["Chaos Shard"],
		"Harbinger's Orb": ["Harbinger's Shard"],
		"Orb of Annulment": ['Annulment Shard'],
		"Ancient Orb": ['Ancient Shard']
	}

	currency = list(currencyvals.keys())
	if cookies['POESESSID']:
		request = f'https://www.pathofexile.com/character-window/get-stash-items?league={league}&realm=pc&accountName={accountname}&tabs=0&tabIndex={currencytab}'

		req = requester.post(request, cookies=cookies, headers=header)
		if req.status_code == 200:
			data = json.loads(req.content)
			skipped = set()
			if 'items' in data:
				for item in data['items']:
					if item['typeLine'] in currencyvals and currencyvals[item['typeLine']] < item['stackSize'] and currencyvals[item['typeLine']] != -1:
						currency.pop(currency.index(item['typeLine']))
					elif item['typeLine'] not in currencyvals and 'Oil' not in item['typeLine'] and 'Shard' not in item['typeLine'] and 'Fragment' not in item['typeLine']:
						skipped.add(item['typeLine'])
					if item['typeLine'] in shards and item['stackSize'] > currencyvals[item['typeLine']] * 0.5:
						del shards[item['typeLine']]
				print(f"Skipped determining always show for: {sorted(skipped)}")
			else:
				print(f"Error: {req.reason} - {repr(data)}")
		else:
			print(f"Error code {req.status_code}: {req.reason}")

	for shard in shards:
		if shard in currency:
			currency.extend(shards[shard])
	currency = list(set(currency))
	# add div cards that give currency
	currency.extend([card for card in card_meta if 'currency' in card_meta[card]])
	currency.sort()
	with open("autogen/always_highlight.json", "w") as f:
		json.dump(currency, f)


def create_highlight_challenge(accountname, league, cookies, header, requester):
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
		'Complete Rare Unidentified Maps': {
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
			'base': {"class": "Divination Card", "type": "challenge high"},
			'vals': {
				"Bow": [{'bow'}],
				"Divination Card": [{'div'}],
				"Essence": [{'essence'}],
				"Gem": [{'gem'}],
				"Map": [{'map'}],
				"Ring": [{'ring'}],
				"Corrupted Gem": [{'gem', 'corrupt'}],
				"Item Level 100 Item": [{'ilvl100'}],
				"Jewel": [{'jewel'}],
				"Influenced Item": [{'influenced'}],
				"Prophecy": [{'prophecy'}],
				"Rare Item": [{'rare'}],
				"Six-Linked Item": [{'6l'}],
				"Scarab": [{'scarab'}],
				"Shaper or Elder Item": [{'shaper'}, {'elder'}],
				"Two-Implicit Unique Item": [{'two-implicit'}],
				"Two-Implicit Corrupted Unique Item": [{'two-implicit', 'corrupt', 'unique'}],
				"Unique Map": [{'unique', 'map'}],
				'Unique Item': [{'unique'}],
				'Stack of Currency': [{'currency'}],
				"Itemised Prophecy": [{"NYI"}],
				'Vaal Gem': [{"vaalgem"}],
				'23% Quality Gem': [{"23%"}],
				'Level 21 Gem': [{"21gem"}],
				'Unique Jewel': [{'unique', 'jewel'}]
			}
		},
	}

	results = {}
	if cookies['POESESSID']:
		request = f'https://www.pathofexile.com/account/view-profile/{accountname}/challenges?season={league}'
		req = requester.post(request, cookies=cookies, headers=header)
		text = req.content.decode("utf-8")
		soup = BeautifulSoup(text, 'html.parser')
		challenges = {}
		for challenge in soup.find_all("div", class_="incomplete"):
			title = challenge.h2.text
			challenges[title] = []
			for val in challenge.find_all("li", class_=""):
				challenges[title].append(val.get_text().strip())

		for chal in challenges:
			if chal in highlights:
				if chal == "Turn in Divination Cards":
					cards = set()
					for cat in challenges[chal]:
						for li in highlights[chal]['vals'][cat]:
							for card in card_meta:
								if li.issubset(card_meta[card]):
									cards.add(card)
					for card in cards:
						key = f'0 {chal} - {card}'
						results[key] = deepcopy(highlights[chal]['base'])
						results[key]['baseexact'] = card
				else:
					for val in challenges[chal]:
						if val in highlights[chal]['vals']:
							for item in highlights[chal]['vals'][val]:
								key = f'0 {chal} - {val}'
								results[key] = deepcopy(highlights[chal]['base'])
								if 'other' in item:
									results[key]['other'].extend(item['other'])
									del item['other']
								results[key] = {**results[key], **item}
						else:
							print(f"Not handling {chal} - {val}")
			else:
				print(f"Not handling custom alerts for: {chal}")

	header = '''#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: {} UTC from "{}" data
'''
	buf = '''{}\ndesc = "Challenge Autogen"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'), league))
	for item in sorted(results):
		buf += f'\t"{item}": {results[item]},\n'
	buf += u'}\n'

	with open('autogen\\custom_challenge.py', 'w', encoding='utf-8') as f:
		f.write(buf)


if __name__ == '__main__':
	create_always_highlight()
