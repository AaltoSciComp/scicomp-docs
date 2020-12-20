#!/bin/bash

if [ -z "$1" ] ; then
    echo "usage: new.sh <post slug>"
    exit 1
fi

base=$(dirname $0)
slug="$1"
output="$base/$(date +%Y/%m)/$slug.rst"


mkdir -p "$base/$(date +%Y/%m)/"
cp "$base/post.rst.template" "$output"

sed -i s/YYYY-MM-DD/$(date +%Y-%m-%d)/ "$output"

echo "$output"
