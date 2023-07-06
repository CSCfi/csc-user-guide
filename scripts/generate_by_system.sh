#!/bin/bash

app_dir="docs/apps"
ignore_file="scripts/skip_system.txt"
generated_file="docs/apps/by_system.md"
echo -e "# Applications by availability\n" > $generated_file

# If you are adding another system, make sure to add a heading for
# it into the file pointed to by the variable $generated_file above.
# While this script rewrites the whole file, the link tests are
# executed before that when deploying and may thus falsely report
# broken links.

# Case sensitive, the title for the system category
system_name=("Mahti" "Puhti" "LUMI" "Mahti web interface" "Puhti web interface")

# Prefix to indicate a keyword for a web interface
interactive_prefix="www"

# Not case sensitive, the keyword to grep to determine if a software is available on a system
# For exceptions add an entry to skip_system.txt
# Format: SKIP_[system_key] [filename]
system_key=("mahti" "puhti" "lumi" "$interactive_prefix-mahti" "$interactive_prefix-puhti")

system_desc=("CSC supercomputer for massively parallel jobs"\
    "CSC supercomputer for small and medium jobs"\
    "EuroHPC supercomputer for CPU and especially GPU jobs"\
    "Web interface for Mahti"\
    "Web interface for Puhti")

system_prefix () { echo ${system_key[$1]%%-*}; }
system_anchor () { lower_case=${system_name[$1],,}; echo "#${lower_case//\ /-}"; }

num_systems=${#system_name[@]}
num_keys=${#system_key[@]}

if [[ "$num_keys" -ne "$num_systems" ]]
then
    echo "Number of search keys must match the number of systems"
    exit 1;
fi

indexes=$( seq 0 $(($num_systems-1)) )

echo -e "Applications available on\n" >> $generated_file
for i in $indexes
do
    if [[ $(system_prefix $i) != $interactive_prefix ]]
    then
        echo "- [${system_name[$i]}]($( system_anchor $i )), ${system_desc[$i]}" >> $generated_file
    fi
done

echo -e "\nInteractive web applications available on\n" >> $generated_file
for i in $indexes
do
    if [[ $(system_prefix $i) == $interactive_prefix ]]
    then
        echo "- [${system_name[$i]}]($( system_anchor $i ))" >> $generated_file
    fi
done

for i in $indexes
do
    ignores=$(cat <(grep -i SKIP_ALL $ignore_file ) <(grep -i SKIP_${system_key[$i]} $ignore_file ) | awk  '{ print $2 }')
    files=$(grep --exclude-from=<(echo "$ignores") -wirl ${system_key[$i]} $app_dir | sort | uniq | sed s%docs/apps/%%)
    software=$(grep -f <(echo "$files") $app_dir/index.md)
    echo -e "\n## ${system_name[$i]} \n" >> $generated_file
    if [[ "${system_name[$i]}" == "LUMI" ]]
    then
        echo -e "!!! info \"Note\"" >> $generated_file
        echo -e "    This list refers only to applications pre-installed by CSC under \`/appl/local/csc\`." >> $generated_file
        echo -e "    For a comprehensive list of available EasyBuild recipes, see the [LUMI Software" >> $generated_file
        echo -e "    Library](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/).\n" >> $generated_file
    fi
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
