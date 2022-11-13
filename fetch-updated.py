import json
import os.path
import requests

urls = open('nyt-urls.txt').read().strip()
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

	if name in timestamps:
		headers['If-Modified-Since'] = timestamps[name]['Last-Modified']
		headers['If-None-Match'] = timestamps[name]['ETag']

	rq = requests.get(url, headers=headers)

	if rq.status_code == 200:
		print(name)
		open(f'{path}/{name}', 'w').write(rq.content).close()

	if not name in timestamps:
		timestamps[name] = {}

	timestamps[name]['Last-Modified'] = rq.headers['Last-Modified']
	timestamps[name]['ETag'] = rq.headers['ETag']

open('timestamps.json', 'w').write(json.dumps(timestamps)).close()