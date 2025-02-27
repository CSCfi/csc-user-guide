#!/usr/local/env bash

internal_urls=$(grep -o -n -r --include \*.md -- "\[[^]]*\](http[^)]*docs.csc.fi[^)]*" docs)

if [ -n "$internal_urls" ];
then
    echo -e "Found web urls pointing to docs.csc.fi"
    echo -e "Please change these to internal markdown links"

    echo "$internal_urls" | sed 's#\([^:]*\):\([^:]*\):.*(\(.*\)#Url \3 on line \2 in file \1 points to docs.csc.fi#g'

    exit 1

else
    echo "No web urls pointing to docs.csc.fi found"
    exit 0
fi

