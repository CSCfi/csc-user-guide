no_desc=$(grep -o -n -r --include \*.md  -- "\!\[[^]]*\]([^)(]*)" $1  | grep  "\[\s*\]\|(.*[^\",^\']\s*)")
old_f_name=""
while IFS= read -r res; do
    IFS=':' read -r -a arr <<< "$res"
    f_name=${arr[0]}
    if [[ ! "$f_name" = "$old_f_name" ]]; then
        old_f_name=$f_name
        echo "Missing alt-txt in file $f_name"
    fi
    line=${arr[1]}
    link=("${arr[@]:2}")
    echo -e "\t $link on line $line"
done <<< "$no_desc"

