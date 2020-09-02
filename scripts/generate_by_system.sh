#!/bin/bash
app_dir="docs/apps"
ignores="--exclude-from=scripts/skip_system.txt"
mahti_files=$(grep $ignores -i mahti $app_dir/*.md | awk -F ":" '{print $1}' | sort | uniq | sed s%docs/apps/%%)
puhti_files=$(grep $ignores -i puhti $app_dir/*.md | awk -F ":" '{print $1}' | sort | uniq | sed s%docs/apps/%%)
mahti_software=$(grep -f <(echo "$mahti_files") $app_dir/alpha.md)
puhti_software=$(grep -f <(echo "$puhti_files") $app_dir/alpha.md)

generated_file="docs/apps/by_system.md"
echo -e "# Applications by system\n" > $generated_file

echo -e "## Puhti \n" >> $generated_file
echo "$puhti_software" >> $generated_file
echo -e "\n" >> $generated_file
echo -e "## Mahti\n" >> $generated_file
echo "$mahti_software" >> $generated_file
