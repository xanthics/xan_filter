#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.7.x or higher
# Gets current price data from poe.ninja
import json
import requests
from ninja_helm_lookup import helmnames
from validate_ninja_data import validate_data


# get price data from poe.ninja
def scrape_ninja(league='tmpstandard'):
	leaguelookup = {
		"Standard": "Standard",
		"Hardcore": "Hardcore",
		"tmpstandard": "Heist",
		"tmphardcore": "Hardcore Heist",
	}

	keys = [
		'Oil',
		'Vial',
		'SkillGem',
		'Currency',
		'Fragment',
		'Scarab',
		'Fossil',
		'Resonator',
		"Incubator",
		'Essence',
		'DivinationCard',
		'Prophecy',
		'BaseType',
		'HelmetEnchant',
		'UniqueMap',
		'UniqueJewel',
		'UniqueFlask',
		'UniqueWeapon',
		'UniqueArmour',
		'UniqueAccessory',
		'Watchstone',
		'DeliriumOrb',
#		'Seed'
	]

	classtypes = {
		'Currency': 'currency',
		'Vial': 'currency',

		'Fossil': 'currency_strict',
		'Resonator': 'currency_strict',
		'Essence': 'currency_strict',
		'DeliriumOrb': 'currency_strict',

		'SkillGem': 'gems',

		'Fragment': 'fragment',
		'Scarab': 'fragment',

		"Incubator": 'incubator',

		'DivinationCard': 'div',

		'Prophecy': 'prophecy',

		'BaseType': 'base',

		'HelmetEnchant': 'enchant',

		'UniqueMap': 'unique',
		'UniqueJewel': 'unique',
		'UniqueFlask': 'unique',
		'UniqueWeapon': 'unique',
		'UniqueArmour': 'unique',
		'UniqueAccessory': 'unique',
		'Watchstone': 'unique',

		'Oil': 'challenge_stack',
#		'Seed': 'challenge_stack',
	}

	requester = requests.session()
	header = {
		'User-Agent': 'xan.filter)',
		'From': 'xanthics on discord'
	}
	price_val = {}

	for key in keys:
		if key in ['Currency', 'Fragment']:
			request = f'https://poe.ninja/api/data/currencyoverview?league={leaguelookup[league]}&type={key}'
		else:
			request = f'https://poe.ninja/api/data/itemoverview?league={leaguelookup[league]}&type={key}'
		req = requester.get(request, headers=header)
		print(f"{league} {key} Status code: {req.status_code}")
		if req.status_code == 204:
			print("No {} data for {}".format(key, league))
			continue
		data = req.json(encoding='utf-8')

		if classtypes[key] not in price_val:
			price_val[classtypes[key]] = {}

		if key in ['Currency', 'Fragment']:
			for i in data['lines']:
				if 'chaosEquivalent' in i:
					if i['currencyTypeName'] in price_val:
						print(f"Duplicate key for {i['currencyTypeName']} found")
					else:
						pc = i['pay']['count'] if i['pay'] else 0
						rc = i['receive']['count'] if i['receive'] else 0
						if "Splinter" not in i['currencyTypeName']:
							price_val[classtypes[key]][i['currencyTypeName']] = {'baseexact': i['currencyTypeName'], 'value': i['chaosEquivalent'], 'count': pc + rc}
						else:
							price_val['currency'][i['currencyTypeName']] = {'baseexact': i['currencyTypeName'], 'value': i['chaosEquivalent'], 'count': pc + rc}

		elif key in ['Oil', 'DeliriumOrb', 'Resonator', 'Fossil', 'DivinationCard', 'Incubator', 'Essence', 'Scarab', 'Vial']:
			for i in data['lines']:
				if i['name'] in price_val[classtypes[key]]:
					print(f"Duplicate key for {i['name']} found")
				else:
					price_val[classtypes[key]][i['name']] = {'baseexact': i['name'], 'value': i['chaosValue'], 'count': i['count']}

		elif key == 'Prophecy':
			for i in data['lines']:
				tname = i['name']
				if i['name'] in price_val[classtypes[key]]:
					print(f"Duplicate key for {i['name']} found")
					while i['name'] in price_val[classtypes[key]]:
						i['name'] += "*"
				price_val[classtypes[key]][i['name']] = {'prophecy': tname, 'value': i['chaosValue'], 'count': i['count']}

		elif key in ['UniqueJewel', 'UniqueFlask', 'UniqueWeapon', 'UniqueArmour', 'UniqueAccessory']:
			for i in data['lines']:
				if (('links' in i and i['links']) or 'relic' in i['icon']) and i['name'] != 'Tabula Rasa':
					continue
				if key == 'Watchstone':
					i['baseType'] = 'Ivory Watchstone'
				elif 'Synthesised' in i['baseType']:
					i['baseType'] = i['baseType'][12:]
				if i['name'] in price_val[classtypes[key]]:
					while i['name'] in price_val[classtypes[key]]:
						i['name'] += "*"
				price_val[classtypes[key]][i['name']] = {'baseexact': i['baseType'], 'value': i['chaosValue'], 'count': i['count']}

		elif key == 'UniqueMap':
			for i in data['lines']:
				if 'Synthesised' in i['baseType']:
					i['baseType'] = i['baseType'][12:]
				if i['name'] in price_val[classtypes[key]]:
					if i['mapTier'] < price_val[classtypes[key]][i['name']]['tier']:
						t = price_val[classtypes[key]][i['name']]
						name = f"{i['name']} {t['tier']}"
						price_val[classtypes[key]][name] = {'baseexact': t['baseexact'], 'value': t['value'], 'count': t['count'], 'tier': t['tier'], 'other': t['other'][:]}
						price_val[classtypes[key]][i['name']] = {'baseexact': i['baseType'], 'value': i['chaosValue'], 'count': i['count'], 'tier': i['mapTier'], "other": [f"MapTier = {i['mapTier']}"]}
					else:
						name = f"{i['name']} {i['mapTier']}"
						price_val[classtypes[key]][name] = {'baseexact': i['baseType'], 'value': i['chaosValue'], 'count': i['count'], 'tier': i['mapTier'], "other": [f"MapTier = {i['mapTier']}"]}
				else:
					price_val[classtypes[key]][i['name']] = {'baseexact': i['baseType'], 'value': i['chaosValue'], 'count': i['count'], 'tier': i['mapTier'], "other": [f"MapTier = {i['mapTier']}"]}

		elif key == 'Watchstone':
			for i in data['lines']:
				if i['name'] in price_val[classtypes[key]]:
					if i['mapTier'] > price_val[classtypes[key]][i['name']]['charges']:
						t = price_val[classtypes[key]][i['name']]
						name = f"{i['name']} {t['charges']}"
						price_val[classtypes[key]][name] = {'baseexact': 'Ivory Watchstone', 'value': t['value'], 'count': t['count'], 'charges': t['charges']}
						price_val[classtypes[key]][i['name']] = {'baseexact': 'Ivory Watchstone', 'value': i['chaosValue'], 'count': i['count'], 'charges': i['mapTier']}
					else:
						name = f"{i['name']} {i['mapTier']}"
						price_val[classtypes[key]][name] = {'baseexact': 'Ivory Watchstone', 'value': i['chaosValue'], 'count': i['count'], 'charges': i['mapTier']}
				else:
					price_val[classtypes[key]][i['name']] = {'baseexact': 'Ivory Watchstone', 'value': i['chaosValue'], 'count': i['count'], 'charges': i['mapTier']}

		elif key == 'BaseType':
			for i in data['lines']:
				if i['baseType'].startswith('Superior '):
					continue
				# convert numbers to string since we are converting to json later
				if not i['variant']:
					i['variant'] = 'None'
				price_val[classtypes[key]][f"{i['levelRequired']}-{i['variant']}-{i['baseType']}"] = {'baseexact': i['baseType'], 'value': i['chaosValue'], 'count': i['count'], 'influence': i['variant'],
																									  'other': [f'ItemLevel {">= 86" if i["levelRequired"] >= 86 else i["levelRequired"]}']}

		elif key == 'HelmetEnchant':
			for i in data['lines']:
				if i['name'] not in helmnames:
					if not i['name'].startswith('Allocates') and i['name'] not in helmnames:
						print(f"Missing helm enchant mapping for: {repr(i['name'])}")
					continue
				if i['name'] in price_val[classtypes[key]]:
					print(f"Duplicate key for {i['name']} found")
				else:
					for c, ench in enumerate(helmnames[i['name']]):
						price_val[classtypes[key]][f"{c}-{i['name']}"] = {'enchant': ench, 'value': i['chaosValue'], 'count': i['count']}

		elif key == "SkillGem":
			lookup = {
				"Spellslinger Support": "Spellslinger",
				"Rune Blast": "Stormbind",
				"Combust": "Infernal Cry",
				"Arcanist Brand Support": "Arcanist Brand",
				"Signal Prey": "Predator Support",
			}
			for i in data['lines']:
				# convert numbers to string since we are converting to json later
				if i['name'] in ['Enlighten Support', 'Enhance Support', 'Empower Support'] or 'Awakened' in i['name']:
					i['gemQuality'] = 0
				elif i['name'] in lookup:
					i['name'] = lookup[i['name']]
				name = i['name']
				other = ''
				if any(val in i['name'] for val in ['Anomalous', 'Divergent', 'Phantasmal']):
					other, name = i['name'].split(" ", maxsplit=1)
				price_val[classtypes[key]][f"{99-i['gemLevel']}{99-i['gemQuality']}{1 if i['corrupted'] else 0} {i['name']}"] = {'baseexact': name, 'value': i['chaosValue'], 'count': i['count'],
																														   "other": [f"GemLevel >= {i['gemLevel']}", f"Quality >= {i['gemQuality']}", f"Corrupted {i['corrupted']}"]}
				if other:
					price_val[classtypes[key]][f"{99 - i['gemLevel']}{99 - i['gemQuality']}{1 if i['corrupted'] else 0} {i['name']}"]['other'].append(f"GemQualityType {other}")
		elif key == 'Seed':
			for i in data['lines']:
				price_val[classtypes[key]][f"{99-i['levelRequired']} {i['name']}"] = {'baseexact': i['name'], 'value': i['chaosValue'], 'count': i['count'], "other": [f"ItemLevel >= {i['levelRequired']}"]}

		else:
			print('Unhandled key: "{}"'.format(key))

	validate_data(price_val)
	for k in price_val:
		with open(f'autogen/{k}.json', 'w') as f:
			json.dump(price_val[k], f, sort_keys=True)  # , indent=2)


if __name__ == '__main__':
	scrape_ninja()
