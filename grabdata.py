import json
from urllib.request import urlopen
from collections import defaultdict
import pandas as pd     # for csv

def read_json_from_url(url):
	"""Reads JSON data from a URL.
	Args:
		url (string): URL to a JSON object
	Returns:
		data (JSON object): imported JSON object
	"""
	print('Reading JSON data...')
	response = urlopen(url)
	data = json.loads(response.read())
	return data

def read_json_from_file():
	"""Reads JSON object from file.
	Args:
		none
	Returns:
		data (JSON object): imported JSON object
	"""
	print('Reading JSON data...')
	with open('./data/phishtank.json', 'r') as infile:
		data = json.loads(infile.read())
	return data

def write_json_to_File(jsonData):
	"""Writes JSON object to file.
	Args:
		jsonData (JSON object): JSON to write to file
	Returns:
		none
	"""
	print('Writing JSON data...')
	with open('./data/phishtank.json', 'w') as outfile:
		json.dump(jsonData, outfile)

def find_json_targets(jsonData):
	"""Collects names of targets of phishing domains as dictionary keys and lists phishing id and phishing url as values.
	Args:
		jsonData (JSON object): JSON object to parse
	Returns:
		data (defaultdict): dictionary of elements by target { 'target domain' : [phish_id, url, ...] }
	"""
	data = defaultdict(list)
	for ele in jsonData:
		for x in ele:
			# PhishTank phishing id
			# if x == 'phish_id':
			# 	data[ele['target']].append(ele[x])
			if x == 'url':
				data[ele['target']].append(ele[x])
	return data

def print_json_targets(sorted, n=1000):
	"""Prints dictionary entries to a given range or 1000.
	Args:
		sorted (defaultdict): dictionary to print
		n (int): stop after printing this amount
	Returns:
		none
	"""
	count = 0
	for (key, values) in sorted.items():
		# Print trusted name
		print(key, "::")
		# Print phishing urls
		for val in values:
			print("\t", val)
		print()
		count += 1
		if count >= n:
			break
	print("Targets: ", count)

# ---- Only used for initial download of json data ----
# url = 'http://data.phishtank.com/data/online-valid.json'
# jsonData = read_JSON_from_URL(url)
# write_JSON_to_File(jsonData)

#jsonData = read_json_from_file()
#filter = find_json_targets(jsonData)

# ---- print a few dictionary entries ----
#print_json_targets(filter)

# ---- Download and save csv data ----
url = 'http://data.phishtank.com/data/online-valid.csv'
csv_data = pd.read_csv(url)
csv_data.head()
csv_data.to_csv('./data/online-valid.csv')
