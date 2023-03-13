#!/bin/sh
app_dir="docs/apps"
generated_file="$app_dir/index.md"

echo -e "# Applications\n" > $generated_file

echo -e "- [By discipline](by_discipline.md)" >> $generated_file
echo -e "- [By availability](by_system.md)" >> $generated_file
echo -e "- [By license](by_license.md)" >> $generated_file

echo -e "\n## Applications in alphabetical order\n" >> $generated_file
grep \* $app_dir/by_discipline.md | sort -f | uniq >> $generated_file
