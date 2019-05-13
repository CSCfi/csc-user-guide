#!/bin/bash

# The first word of this script will take the amount of accepted errors that the test willl
# accept. This is to make it easier to start testing without correcting all errors at once.
# One can easy add whitelisted word into aspell.en.pws. Note that the file can't end with a
# empty row. 
ACCEPTED_AMOUNT_OF_TYPOS=$1
DICTIONARY=tests/aspell.en.pws
TEMPLATES=$(find docs -name '*.md')
# the aspell parameters set: english language, utf-8 encoding, home dir and personal dictionary
# to exclude some of our technical terms we also ignore words with 3 or less characters.
# Currently only typos in our e-mail templates were in words with more characters
COMMAND="aspell --lang=en --ignore 3 --encoding=utf-8 --home-dir=. --personal=$DICTIONARY list"
for t in $(echo $TEMPLATES)
do 
    echo $t
    cat $t |$COMMAND | sort | uniq -c | sort --numeric-sort
    SUM=$(($SUM + $(cat $t |$COMMAND |wc -l) ))
done

echo "Number of typos: $SUM"

if [[ $SUM -gt $ACCEPTED_AMOUNT_OF_TYPOS ]]; then
    echo "$SUM is greater than the $ACCEPTED_AMOUNT_OF_TYPOS"
    exit 1
fi
