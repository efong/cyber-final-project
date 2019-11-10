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

def read_JSON_from_File():
	"""
	Reads json object from file.
	Arg(s): none
	Return: json object
	"""
	with open('./data/phishtank.json', 'r') as infile:
		data = json.loads(infile.read())
		return data

def write_JSON_to_File(jsonData):
	"""
	Writes json object to file.
	Arg(s): json object
	Return: none
	"""
	print('Writing JSON data...')
	with open('./data/phishtank.json', 'w') as outfile:
		json.dump(jsonData, outfile)

def find_targets(jsonData):
	"""
	Collects names of targets of phishing domains as dictionary keys
	and lists phishing id and phishing url as values.
	{ 'target domain' : [phish_id, url, ...] }
	Arg(s): json object
	Return: default dictionary
	"""
	data = defaultdict(list)
	for ele in jsonData:
		for x in ele:
			if x == 'phish_id':
				data[ele['target']].append(ele[x])
			elif x == 'url':
				data[ele['target']].append(ele[x])
	return data

def print_targets(sorted, stop):
	"""
	Prints dictionary entries to a given range.
	Arg(s): dictionary, int
	Return: none
	"""
	for (key, value) in sorted.items():
		print(key, "::", value)
		print()
		stop -= 1
		if stop <= 0:
			break

# ---- Only used for initial data grab ----
# url = 'http://data.phishtank.com/data/online-valid.json'
# jsonData = read_JSON_from_URL(url)
# write_JSON_to_File(jsonData)
jsonData = read_JSON_from_File()
cluster = find_targets(jsonData)

# ---- print a few dictionary entries ----
print_targets(cluster, 5)
