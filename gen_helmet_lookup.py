import json


def validate(state, conditions):
	for i in range(len(conditions)):
		if 'max' not in conditions[i]:
			conditions[i]['max'] = 999999999
		if 'min' not in conditions[i]:
			conditions[i]['min'] = -999999999
	return all([conditions[state[x][0]]['min'] <= state[x][1] <= conditions[state[x][0]]['max'] for x in state])


def main():
	with open(r'C:\git\RePoE\RePoE\data\mods.json', 'r') as f:
		mods = json.load(f)
	with open(r'C:\git\RePoE\RePoE\data\stat_translations.json', 'r') as f:
		translation = json.load(f)

	transmod = {}

	value_transforms = {
		"per_minute_to_per_second_2dp_if_required": 1/60,
		"per_minute_to_per_second_2dp": 1/60,
		"per_minute_to_per_second": 1/60,
		"milliseconds_to_seconds": 1/1000,
		"divide_by_one_hundred": 1/100,
		"negate": -1,
		"canonical_stat": 1,
		"divide_by_two_0dp": 1/2
	}

	for val in translation:
		for key in val['ids']:
			if key in transmod:
				print(f"Error: {key}")
			transmod[key] = val

	for f in ['EnchantmentDoubleSlashAddedPhysToBleeding1', 'EnchantmentDoubleSlashAddedPhysToBleeding2']:
		mods[f]['stats'][0]['max'] = mods[f]['stats'][0]['min']
		mods[f]['stats'][1]['min'] = mods[f]['stats'][1]['max']

	q = {}
	for val in mods:
		if mods[val]['generation_type'] == 'enchantment' and 'helmet' in [x['tag'] for x in mods[val]['spawn_weights']] and not mods[val]['type'].endswith("Old"):
	#		if not mods[val]['name']:
	#			print(val)
			if len(mods[val]['stats']) > 0:
				lu = {}
				for _id in mods[val]['stats']:
					if _id['min'] != _id['max']:
						print(val)
					lu[_id['id']] = [transmod[mods[val]['stats'][0]['id']]['ids'].index(_id['id']), _id['min']]

				cond = ''
				if len(transmod[mods[val]['stats'][0]['id']]['English']) == 1:
					cond = transmod[mods[val]['stats'][0]['id']]['English'][0]
				else:
					for condition in transmod[mods[val]['stats'][0]['id']]['English']:
						if validate(lu, condition['condition']):
							cond = condition
							break

	#			print("***")
	#			print(cond)
	#			print(lu)
	#			print(mods[val]['name'], mods[val]['stats'])
	#			print(transmod[mods[val]['stats'][0]['id']])
				mq = []
				while lu:
					for x in lu:
						if lu[x][0] == len(mq):
							mq.append(lu[x][1])
							break
					del lu[x]

				for idx in range(len(cond['index_handlers'])):
					v = cond['index_handlers'][idx]
					if v:
						if "2dp" in v[0]:
							mq[idx] = round(mq[idx] * value_transforms[v[0]], 2)
						else:
							mq[idx] = int(mq[idx] * value_transforms[v[0]])
					if cond['format'][idx] not in ['#', 'ignore']:
						if mq[idx] < 0 and '+' in cond['format'][idx]:
							cond['format'][idx] = cond['format'][idx].replace('+', '')
						mq[idx] = cond['format'][idx].replace('#', str(mq[idx]))
				if cond['string'].format(*mq) and mods[val]['name']:
					if cond['string'].format(*mq) not in q:
						q[cond['string'].format(*mq)] = []
					if mods[val]["name"] not in q[cond['string'].format(*mq)]:
						q[cond['string'].format(*mq)].append(mods[val]["name"])

	buf = 'helmnames = {\n'
	for i in sorted(q):
		buf += f'\t"{i}": {q[i]},\n'
	buf += '}'

	with open('ninja_helm_lookup.py', 'w') as f:
		f.write(buf)


if __name__ == "__main__":
	main()