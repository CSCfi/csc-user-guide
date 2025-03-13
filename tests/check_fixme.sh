#!/usr/local/env bash

FOUND_FIXME=$(grep -o -i -n -r --include \*.md -- FIXME docs )

if [ -n "$FOUND_FIXME" ];then
    echo -e "Documentation contains FIXME"
    echo -e "Please correct the documentation and remove the FIXME\n"

    echo "$FOUND_FIXME" | sed 's#^\([^:]*\):\([^:]*\):.*#Line \2 in file \1 contains FIXME#'

    exit 1

else
    echo "No FIXME found in the documentation"
    exit 0
fi
