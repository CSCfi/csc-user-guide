#run from top level 

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

tests=$(cat .travis.yml | grep script -A 200 | grep "^\s*-" | cut -d "-" -f2 )

which misspell &> /dev/null

if [[ $? -eq 1 ]];then
    echo -e "\nWARN: misspell not found, skipping spelling test"
    tests=$(echo "$tests" | grep -v misspell )
fi

TEST_LOG=tests/test.log

rm $TEST_LOG 
touch $TEST_LOG
echo -e "\nRUNNING TESTS, output in $TEST_LOG"
echo    "--------------------------------------------"
while IFS= read -r cmd; do
    t_name=$(echo $cmd | rev |cut -d "/" -f 1 | rev | cut -d "." -f 1 )
    STAT="${GREEN}OK${NC}"
    LN=""
    out=$(eval "$cmd")
    if [[ ! $? -eq 0 ]];then
    STAT="${RED}FAILED${NC}" 
    LN=", see $TEST_LOG line $(($(cat $TEST_LOG | wc -l ) +2 ))"
    fi
    echo -e "\n--------------- $t_name" >> $TEST_LOG
    echo "$out" >> $TEST_LOG
    echo -e "$t_name  $STAT $LN"
done <<< "$tests"


