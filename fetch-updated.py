import json
import os.path
import requests
import sys

urls = open(sys.argv[1]).read().strip()
urls = urls.split("\n")

timestamps = {}

try:
	timestamps = json.load(open('timestamps.json'))
except:
	pass

for line in urls:
	path, url = line.split(" ")
	name = os.path.basename(url)

	headers = {}

	if name in timestamps and timestamps[name].get('Last-Modified', None):
		headers['If-Modified-Since'] = timestamps[name]['Last-Modified']

	if name in timestamps and timestamps[name].get('ETag', None):
		headers['If-None-Match'] = timestamps[name]['ETag']

	rq = requests.get(url, headers=headers)

	print(rq.status_code, name, headers)

	if rq.status_code == 200:
		with open(f'{path}/{name}', 'wb') as f:
			f.write(rq.content)

		timestamps[name] = timestamps.get(name, {})
		timestamps[name]['Last-Modified'] = rq.headers.get('Last-Modified', None)
		timestamps[name]['ETag'] = rq.headers.get('ETag', None)

with open('timestamps.json', 'w') as f:
	f.write(json.dumps(timestamps))