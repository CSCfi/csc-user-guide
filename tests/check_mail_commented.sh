source tests/common_functions.sh

regex="^\s*#SBATCH\s*--mail-user"
pass_message="The --mail-user flag is commented out in all batch job scripts"
fail_message="The --mail-user flag should not be active in examples."


run_regex_test "$regex" "$pass_message" "$fail_message"

