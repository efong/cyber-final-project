import json
from urllib.request import urlopen

url = 'http://data.phishtank.com/data/online-valid.json'
response = urlopen(url)
print('Reading PhishTank data...')
data = json.loads(response.read())

print('Writing PhishTank data...')
with open('./data/phishtank.json', 'w') as outfile:
	json.dump(data, outfile)

