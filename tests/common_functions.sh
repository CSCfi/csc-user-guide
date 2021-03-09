
# Test passes if the regex does not match anything
# Otherwise fails
run_regex_test(){
    REGEX_STRING="$1"
    SUCCESS_MESSAGE="$2"
    FAIL_MESSAGE="$3"
    res=$(grep -r -n --include \*.md -- "$REGEX_STRING" docs)

    if [[ -z $res ]]; then
        echo "$SUCCESS_MESSAGE"
        return 0
    else
        echo -e "$FAIL_MESSAGE\n"
        echo "$res"
        return 1
    fi

}

function join_by { local IFS="$1"; shift; echo "$*"; }
