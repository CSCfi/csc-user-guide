#!/bin/bash

# find ./docs -type d '!' -exec test -e "{}/index.md" ';' -print |grep -v 'img\|css'

# find ./docs -type d '!' -exec test -e "{}/index.md" ';' -print |grep -v 'img\|css' | tee >(wc -l)

if [[ $(find ./docs -type d '!' -exec test -e "{}/index.md" ';' -print |grep -v 'img\|css\|images') ]]; then
    echo "There are directories without index.md"
    find ./docs -type d '!' -exec test -e "{}/index.md" ';' -print |grep -v 'img\|css\|images'
    exit 0
else
    echo "All directories contain index.md"
    exit 1
fi
