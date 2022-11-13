#!/bin/sh

getversion() {
    prefix=$1
    url=$2
    version=$(curl -s $url)
    mkdir -p "./$prefix"
    echo "$version" > $prefix/versions
    echo "$version"
}

download() {
    prefix=$1
    url=$2
    mkdir -p "./$prefix"
    filename=$(basename "$url")
    echo "$url"
    curl -k --compressed --connect-timeout 10 -m 10 -s -o "./$prefix/$filename" "$url"
}

gitcommit() {
    prefix=$1

    # Use git to find differences and push to github
    git add -A $prefix
    git diff --cached --name-only | cat
    git add log.txt

    updated=$(git diff --name-only --cached $prefix | xargs)

    echo "updated: $updated"

    git commit --author "Automated Script <run@localhost>" -m "$updated" | cat
    git log --name-status HEAD^..HEAD | cat
}

gitupload() {
    git push origin master
}
