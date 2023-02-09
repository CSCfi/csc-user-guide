#!/bin/bash

if [[ $(find ./docs -type d '!' -exec test -e "{}/index.md" ';' -print |grep -v 'img\|css\|images\|wn\|tutorials') ]]; then
    echo "There are directories without index.md"
    find ./docs -type d '!' -exec test -e "{}/index.md" ';' -print |grep -v 'img\|css\|images\|wn\|tutorials'
    exit 1
else
    echo "All directories contain index.md"
    exit 0
fi
