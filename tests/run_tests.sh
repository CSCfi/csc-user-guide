#!/urs/bin/env bash
#run from top level


# Semi standard way of cheking
# if the output is going to a terminal => enable colors

# Or if it is being piped => no colors

if [[ -t 1 ]];then
    UNDERLINE='\033[0;4m'
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    NC='\033[0m' # No Color
else
    UNDERLINE=""
    RED=""
    GREEN=""
    NC=""
fi

ERROR=false

TRAVIS=$(dirname "$0")/../.travis.yml

tests=$(grep script -A 200 "$TRAVIS" | grep "^\s*-" | cut -d "-" -f2 )

which misspell &> /dev/null

if [[ $? -eq 1 ]];then
    echo -e "\nWARN: misspell not found, skipping spelling test"
    tests=$(echo "$tests" | grep -v misspell )
fi

TEST_LOG="$(dirname "$0")/test.log"

if [[ -f $TEST_LOG ]]; then rm "$TEST_LOG"; fi
touch "$TEST_LOG"
echo -e "\nRUNNING TESTS, output in $TEST_LOG"
echo    "--------------------------------------------"
while IFS= read -r cmd; do
    t_name=$(echo "$cmd" | rev |cut -d "/" -f 1 | rev | cut -d "." -f 1 )
    STAT="${GREEN}OK${NC}"
    LN=""
    out=$(eval "$cmd")

    if ! out=$(eval "$cmd");
    then
      STAT="${RED}FAILED${NC}"
      LN=", see $TEST_LOG line $(wc -l "$TEST_LOG" | awk '{print $1+2}')"
      ERROR=true
    fi
    echo -e "\n--------------- $t_name" >> "$TEST_LOG"
    echo "$out" >> "$TEST_LOG"
    echo -e "$t_name  $STAT $LN"
done <<< "$tests"

if $ERROR
then
  echo -e "\n${UNDERLINE}${TEST_LOG}:${NC}"
  cat --number "$TEST_LOG"
fi
