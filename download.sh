#!/bin/sh

prefix=$1
url=$2

mkdir -p "./$prefix"

filename=$(basename "$url")

echo "$url"
curl -k --compressed --connect-timeout 10 -m 10 -s -o "./$prefix/$filename" "$url"
