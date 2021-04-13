source tests/common_functions.sh

regex="^\s*#SBATCH\s*--mail-type"
pass_message="The --mail-type flag is commented out in all batch job scripts"
fail_message="The --mail-type flag should not be active in examples."

ret_code=0

run_regex_test "$regex" "$pass_message" "$fail_message"
if [[ ! $? -eq 0 ]];then
    ret_code=1
    echo -e ""
fi

regex="^\s*[#]*SBATCH\s*--mail-user"
pass_message="The --mail-user is not present in any example script"
fail_message="The --mail-user should not be present in any example script"

run_regex_test "$regex" "$pass_message" "$fail_message"
if [[ ! $? -eq 0 ]];then
    ret_code=1
fi

exit $ret_code
