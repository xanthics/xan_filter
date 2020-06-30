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
		"tmpstandard": "Harvest",
		"tmphardcore": "Hardcore Harvest",
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
		'DeliriumOrb'
	]

	classtypes = {
		'Oil': 'currency',
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
	}

	requester = requests.session()

	price_val = {}

	for key in keys:
		if key in ['Currency', 'Fragment']:
			request = f'https://poe.ninja/api/data/currencyoverview?league={leaguelookup[league]}&type={key}'
		else:
			request = f'https://poe.ninja/api/data/itemoverview?league={leaguelookup[league]}&type={key}'
		req = requester.get(request)
		print(f"{league} {key} Status code: {req.status_code}")
		if req.status_code == 204:
			print("No {} data for {}".format(key, league))
			continue
		data = req.json(encoding='utf-8')

			if key == 'Currency':
				for ii in data['lines']:
					if 'chaosEquivalent' in ii:
						pc = ii['pay']['count'] if ii['pay'] else 0
						rc = ii['receive']['count'] if ii['receive'] else 0
						if pc + rc < mincount:
							continue
						currency[ii['currencyTypeName']] = ii['chaosEquivalent']

			elif key == 'Fragment':
				for ii in data['lines']:
					if 'chaosEquivalent' in ii:
						pc = ii['pay']['count'] if ii['pay'] else 0
						rc = ii['receive']['count'] if ii['receive'] else 0
						if pc + rc < mincount:
							continue
						if "Splinter" in ii['currencyTypeName']:
							currency[ii['currencyTypeName']] = ii['chaosEquivalent']
						else:
							fragments[ii['currencyTypeName']] = ii['chaosEquivalent']

			elif key == 'SkillGem':
				lookup = {
					"Spellslinger Support": "Spellslinger",
					"Rune Blast": "Stormbind",
					"Combust": "Infernal Cry",
					"Arcanist Brand Support": "Arcanist Brand"
				}
				for i in data['lines']:
					if i['count'] < mincount:
						continue
					if i['name'] in ['Enlighten Support', 'Enhance Support', 'Empower Support'] or 'Awakened' in i['name']:
						i['gemQuality'] = 0
#					if i['name'] in ['Deathmark', 'Shockwave'] and 'Support' not in i['name']:
#						i['name'] += ' Support'
					elif i['name'] in lookup:
						i['name'] = lookup[i['name']]
					if i['gemLevel'] not in skillgem:
						skillgem[i['gemLevel']] = {}
					if i['gemQuality'] not in skillgem[i['gemLevel']]:
						skillgem[i['gemLevel']][i['gemQuality']] = {}
					if i['corrupted'] not in skillgem[i['gemLevel']][i['gemQuality']]:
						skillgem[i['gemLevel']][i['gemQuality']][i['corrupted']] = {}
					skillgem[i['gemLevel']][i['gemQuality']][i['corrupted']][i['name']] = i['chaosValue']

			elif key == 'BaseType':
				for ii in data['lines']:
					if ii['baseType'].startswith('Superior ') or \
							(ii['count'] < mincount and ii['variant'] and ii['baseType'] not in goodbases[ii['variant']]) or \
							(not ii['variant'] and (ii['baseType'] not in goodbases[ii['variant']] or ii['count'] < mincount)):
						continue
					if ii['levelRequired'] not in bases:
						bases[ii['levelRequired']] = {}
					if ii['variant'] not in bases[ii['levelRequired']]:
						bases[ii['levelRequired']][ii['variant']] = {}
					bases[ii['levelRequired']][ii['variant']][ii['baseType']] = ii['chaosValue']

		else:
			print('Unhandled key: "{}"'.format(key))

	validate_data(price_val)
	for k in price_val:
		with open(f'autogen/{k}.json', 'w') as f:
			json.dump(price_val[k], f, sort_keys=True)  # , indent=2)


if __name__ == '__main__':
	scrape_ninja()
