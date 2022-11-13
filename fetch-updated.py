import json
import multiprocessing
import os
import os.path
import requests
import sys

MAX_PROCS=5

def fetch_url(line):
	path, url = line.split(" ")
	name = os.path.basename(url)
	filename = f'{path}/{name}'
	timestampdir = f'{path}/timestamps'

	if not os.path.exists(timestampdir):
		os.mkdir(f'{path}/timestamps')

	timestamp = {}

	try:
		timestamp = json.load(open(f'{timestampdir}/{name}'))
	except:
		pass

	headers = {}

	if timestamp.get('Last-Modified', None):
		headers['If-Modified-Since'] = timestamp['Last-Modified']

	if timestamp.get('ETag', None):
		headers['If-None-Match'] = timestamp['ETag']

	rq = requests.get(url, headers=headers)

	print(rq.status_code, name, headers)

	if rq.status_code == 200:
		with open(f'{path}/{name}', 'wb') as f:
			f.write(rq.content)

		timestamp['Last-Modified'] = rq.headers.get('Last-Modified', None)
		timestamp['ETag'] = rq.headers.get('ETag', None)

	with open(f'{timestampdir}/{name}', 'w') as f:
		f.write(json.dumps(timestamp))

urls = open(sys.argv[1]).read().strip()
urls = urls.split("\n")

with multiprocessing.Pool(processes=MAX_PROCS) as pool:
	pool.map(fetch_url, urls)
