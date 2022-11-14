#!/bin/bash

. ./funcs.sh

while [ 1 ]; do
    #./fetch-nyt.sh
    python3 fetch-updated.py nyt-urls.txt
    gitcommit .

    if (( $RANDOM % 30 == 0 )); then
        gitupload
    fi

    sleep 60
done
