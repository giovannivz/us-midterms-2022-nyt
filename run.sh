#!/bin/sh

. ./funcs.sh

while [ 1 ]; do
    ./fetch-nyt.sh
    gitupload .
    sleep 60
done
