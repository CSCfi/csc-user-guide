
time_stamps=$(git ls-files -z docs/ | xargs -0 -n1 -I{} -- git log -1 --format="%ad {}" {} | grep "\.md" | cut -d " " -f 1,2,3,5,7 | grep -v -f scripts/skip_stamp.txt )

while read -r line; do
    date=$(echo $line | cut -d " " -f 1-4 )
    file_name=$(echo $line | cut -d " " -f 5)
    echo -e "\n\n_Last edited ${date}_" >> "$file_name"
done <<< "$time_stamps"
