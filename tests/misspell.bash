#!/bin/bash
# https://github.com/client9/misspell
#  Correct commonly misspelled English words in source files
##
# parameters:
# -error makes it exit code 2 on errors - travis build failure
# * is better than . because . includes the ".git" directory 
#   and stops this from spellchecking git commit messages..
# -locale - the default is a neutral English (so not UK or US)
##
# -w there's also a -w argument to misspell, it fixes the errors instead of just 
#   outputting them
find . -type f -name '*.yml' -o -name '*.md'|xargs misspell -error
if [ "$?" == 0 ]; then
  echo "No commonly misspelled English words found"
  exit 0
else
  exit 1
fi
