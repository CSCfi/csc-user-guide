#!/bin/bash

app_dir="docs/apps"
ignore_file="scripts/skip_system.txt"
generated_file="docs/apps/by_system.md"
echo -e "# Applications by availability\n" > $generated_file

# Case sensitive, the title for the system category
system_name=("Mahti" "Puhti")
# Not case sensitive, the keyword to grep to determine if a software is available on a system
# For exceptions add an entry to skip_system.txt
# Format: SKIP_[system_key] [filename]
system_key=("mahti" "puhti")

system_desc=("CSC supercomputer for massively parallel jobs"\ 
    "CSC supercomputer for small and medium jobs") 


num_systems=${#system_name[@]}
num_keys=${#system_key[@]}

if [[ "$num_keys" -ne "$num_systems" ]]; then
    echo "Number of search keys must match the number of systems"
    exit 1;
fi

echo -e "\n" >> $generated_file
for i in $( seq 0 $(($num_systems-1)) )
do
    echo "- [ Available on ${system_name[$i]}](by_system.md#${system_name[$i],,}), ${system_desc[$i]}" >> $generated_file
done
echo -e "\n" >> $generated_file

for i in $( seq 0 $(($num_systems-1)) )
do
    ignores=$(cat <(grep -i SKIP_ALL $ignore_file ) <(grep -i SKIP_${system_key[$i]} $ignore_file ) | awk  '{ print $2 }')
    files=$(grep --exclude-from=<(echo "$ignores") -i ${system_key[$i]} $app_dir/*.md | awk -F ":" '{print $1}' | sort | uniq | sed s%docs/apps/%%)
    software=$(grep -f <(echo "$files") $app_dir/alpha.md)
    echo -e "\n## ${system_name[$i]} \n" >> $generated_file
    echo "$software" >> $generated_file
done


#mahti_files=$(grep $ignores -i mahti $app_dir/*.md | awk -F ":" '{print $1}' | sort | uniq | sed s%docs/apps/%%)
#puhti_files=$(grep $ignores -i puhti $app_dir/*.md | awk -F ":" '{print $1}' | sort | uniq | sed s%docs/apps/%%)
#mahti_software=$(grep -f <(echo "$mahti_files") $app_dir/alpha.md)
#puhti_software=$(grep -f <(echo "$puhti_files") $app_dir/alpha.md)


#echo -e "## Puhti \n" >> $generated_file
#echo "$puhti_software" >> $generated_file
#echo -e "\n" >> $generated_file
#echo -e "## Mahti\n" >> $generated_file
#echo "$mahti_software" >> $generated_file
