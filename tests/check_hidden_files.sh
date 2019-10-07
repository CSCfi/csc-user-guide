source tests/link_utils.sh
# Test if there are any hidden files (i.e) file
# which are note linked to in any way
hidden_files=$(get_hidden_files)

whitelist=$(grep -v "^#" tests/hidden_whitelist.txt | sort |uniq)

hidden=$(comm -13 <(echo "$whitelist") <(echo "$hidden_files"))

test_var "$hidden" "No hidden files found" "The following files have no links pointing to them and are not whitelisted:"
