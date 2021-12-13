import json

data = {}
with open('movie_providers.json') as f:
    data = dict(json.load(f).items())

print('technical_name, short_name, clear_name, monetization_types')
for item in data['providers']:
	print(item.get('technical_name') + ", " + item.get('short_name') + ", " + item.get('clear_name') + ", " + str(item.get('monetization_types')))

print("Free services: ", end="")
for item in data['providers']:
	if 'free' in item.get('monetization_types') or 'ads' in item.get('monetization_types'):
		print("'"+item.get('short_name')+"', ", end="")
