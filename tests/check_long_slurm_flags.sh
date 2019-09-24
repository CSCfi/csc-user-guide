
source tests/common_functions.sh
regex="^\s*#SBATCH\s*-[A-Z,a-z]"
pass_message="No short slurm flags found"
fail_message="Short slurm flags found, change these to the long version:"


run_regex_test "$regex" "$pass_message" "$fail_message"

