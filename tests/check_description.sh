
source tests/common_functions.sh
img_no_desc=$(grep -o -n -r --include \*.md  -- "\!\[[^]]*\]([^)(]*)" $1  | grep  "\[\s*\]\|(.*[^\",^\']\s*)")
link_no_title=$(grep -o -n -r --include \*.md  -- "[^\!]\[[^]]*\]([^)(]*)" $1  | grep  "\[\s*\]")
url_in_title=$(grep -o -n -r --include \*.md  -- "\[[^]]*\]([^)(]*)" $1  | grep "\[\s*http.*\]")


function go_over {
    local err_msg=$1
    local input=$2
    old_f_name=""
    while IFS= read -r res; do
        IFS=':' read -r -a arr <<< "$res"
        f_name=${arr[0]}
        if [[ ! "$f_name" = "$old_f_name" ]]; then
            old_f_name=$f_name
            echo "$err_msg in file $f_name"
        fi
        line=${arr[1]}
        link=$(join_by : "${arr[@]:2}")
        echo -e "\t $link on line $line"
    done <<< "$input"
}

ret_code=0

if [[ ! -z "$img_no_desc" ]];then
    go_over "Missing title or alt-txt" "$img_no_desc"
    ret_code=1
fi

if [[ ! -z "$link_no_title" ]];then
    go_over "Missing title in" "$link_no_title"
    ret_code=1
fi

if [[ ! -z "$url_in_title" ]];then
    go_over "Url in title " "$url_in_title"
    ret_code=1
fi
if [[ $ret_code -eq 0 ]]; then
    echo "No missing descriptions or urls in titles found"
fi
exit $ret_code
