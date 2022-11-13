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

for url in urls:
	name = os.path.basename(url)

	headers = {}

	if name in timestamps:
		headers['If-Modified-Since'] = timestamps[name]['Last-Modified']
		headers['If-None-Match'] = timestamps[name]['ETag']

	rq = requests.get(url, headers=headers)

	timestamps[name]['Last-Modified'] = rq.headers['Last-Modified']
	timestamps[name]['ETag'] = rq.headers['ETag']

	print(timestamps)

	# {'Connection': 'keep-alive',
	# 'Content-Length': '70296',
	# 'X-GUploader-UploadID': 'ADPycdt8PRc5k3tzKCP_laU4ykTtlqyFoKeW0YQZKDPP-RFc-8HZxKvgYzNBcKUQEBEcT20GYP5re_RIRCUpviDZ9UlkDA',
	# 'Cache-Control': 'max-age=5, stale-if-error=86400, stale-while-revalidate=5, public',
	# 'Expires': 'Sun, 13 Nov 2022 17:50:13 GMT',
	# 'Last-Modified': 'Sun, 13 Nov 2022 17:50:00 GMT',
	# 'ETag': '"f77171f0ef248183db4ee9c65dd3fdcc"',
	# 'x-goog-generation': '1668361800114195',
	# 'x-goog-metageneration': '2',
	# 'x-goog-stored-content-encoding': 'identity',
	# 'x-goog-stored-content-length': '682423',
	# 'Content-Type': 'application/json',
	# 'x-goog-hash': 'crc32c=ZcbcpA==, md5=93Fx8O8kgYPbTunGXdP9zA==',
	# 'x-goog-storage-class': 'STANDARD',
	# 'Server': 'UploadServer',
	# 'Content-Encoding': 'gzip',
	# 'Via': '1.1 varnish, 1.1 varnish',
	# 'Accept-Ranges': 'bytes',
	# 'Date': 'Sun, 13 Nov 2022 17:52:56 GMT',
	# 'Age': '6',
	# 'X-Served-By': 'cache-iad-kjyo7100113-IAD, cache-chi-klot8100171-CHI',
	# 'X-Cache': 'HIT, HIT',
	# 'X-Cache-Hits': '8, 1',
	# 'X-Timer': 'S1668361977.571021,VS0,VE25',
	# 'Vary': 'Accept-Encoding',
	# 'Access-Control-Allow-Origin': '*',
	# 'Timing-Allow-Origin': '*',
	# 'Strict-Transport-Security': 'max-age=63072000; preload; includeSubdomains'}