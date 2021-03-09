source tests/common_functions.sh
lvsl=$(grep -r "<\s*h[0-9][^>]*>[^<]*</h[0-9]>" --include=*.html $1 -o | grep -v "toc-title" | sed 's/\s*id=\s*"[a-z,0-9, _,-]*"\s*//g' | sed 's/<\/h[0-9]>//g' | sed 's/<h//g' | sed 's/>/:/g')
old_f_name=""
prev_lvl="100"
h1_found=false
unique_h1=true       
ret_code=0
while IFS= read -r head; do
    IFS=':' read -r -a arr <<< "$head"
    f_name=${arr[0]}
    lvl=${arr[1]}
    if [[ ! "$f_name" = "$old_f_name" ]] ; then
        h1_found=false
        unique_h1=true       
        old_f_name=$f_name
        md_file=$(echo "$f_name" | sed 's/site/docs/g' | sed 's/\/index.html/.md/g')
        if [[ ! -f "$md_file" ]] ;then
            md_file=$(echo "$md_file" | sed 's/.md/\/index.md/g')
        fi
        prev_lvl="100"
        h_print=true
    fi
    if [[ "$h1_found" = "true" ]] && [[ "$lvl" -eq 1 ]];then
        unique_h1=false        
    fi
    if [[ "$lvl" -eq 1 ]]; then
        h1_found=true
    fi
    skip=$(( lvl-prev_lvl ))
    h_name=$(join_by : "${arr[@]:2}")
    if [[ "$h_print" = "true" ]] && ( [[ "$skip" -gt 1 ]] || [[ "$unique_h1" = "false"  ]] ); then
        h_print=false 
        ret_code=1
        echo "Incorrect headders in file $md_file"
    fi
    if  [[ "$skip" -gt 1 ]]; then
        echo -e "\t$(eval $(echo printf '"#%0.s"' {1..$lvl})) $h_name"
        echo -e "\t   Jumps from depth $prev_lvl to $lvl" 
    fi
    
    if [[ "$unique_h1" = "false" ]];then
        echo -e "\t # $h_name"
        echo -e "\t   Multiple level 1 headders"
        unique_h1=true
    fi
    prev_lvl=$lvl
done <<< "$lvsl"
if [[ $ret_code -eq 0 ]]; then
    echo "Headders are ok"
fi
exit $ret_code
