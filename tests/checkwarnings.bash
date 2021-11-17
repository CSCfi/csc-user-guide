#!/bin/bash

NUMBERS_OF_WARNINGS=$(mkdocs build 2>&1 |grep -i  WARNING |wc -l)

if [ $NUMBERS_OF_WARNINGS -ne 0 ]; then 
    mkdocs build 2>&1 |grep -i  WARNING
    echo "There are $NUMBERS_OF_WARNINGS WARNINGS"
    exit 1
else
    echo "There were no warnings"
fi
