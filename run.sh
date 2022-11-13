#!/bin/bash

. ./funcs.sh

while [ 1 ]; do
    #./fetch-nyt.sh
    python3 fetch-updated.py nyt-urls.txt
    gitcommit .

    if (( $RANDOM % 10 == 0 )); then
        gitupload
    fi

    sleep 30
done