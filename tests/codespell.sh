#!/bin/bash
# https://github.com/codespell-project/codespell
# Check for commonly misspelled English words in source files
#
# -L: comma-separated list of words to ignore
if find . -type f \( -name '*.yml' -o -name '*.md' \) -print0 | xargs -0 codespell -L "bu,namd,DAA";
then
  echo "No commonly misspelled English words found"
  exit 0
else
  exit 1
fi
