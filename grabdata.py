import json
from urllib.request import urlopen
from collections import defaultdict


def read_JSON_from_URL(url):
	"""
	Reads json data from a URL.
	Arg(s): url
	Return: json object
	"""
	print('Reading JSON data...')
	response = urlopen(url)
	data = json.loads(response.read())
	return data

def write_JSON_to_File(data):
	print('Writing JSON data...')
	with open('./data/phishtank.json', 'w') as outfile:
		json.dump(data, outfile)

url = 'http://data.phishtank.com/data/online-valid.json'
jsonData = read_JSON_from_URL(url)
# write_JSON_to_File(jsonData)

# dictionary { 'target domain' : [phish_id, url, ...] }
data = defaultdict(list)
for ele in jsonData:
	for x in ele:
		if x == 'phish_id':
			data[ele['target']].append(ele[x])
		elif x == 'url':
			data[ele['target']].append(ele[x])

# print a few dictionary entries
stop = 5
for (key, value) in data.items():
	print(key, "::", value)
	print()
	stop -= 1
	if stop < 0:
		break
