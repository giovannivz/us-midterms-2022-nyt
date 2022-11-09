#!/bin/sh

. ./funcs.sh

cat nyt-urls.txt | xargs -n 2 -P 5 ./download.sh
