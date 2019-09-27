

get_all_local_links(){
    grep -o -n -r --include \*.md   -- "\[[^]]*\]([^)(]*)" docs  | grep -v "http" | grep -v "mailto:.*@csc\.fi" \
    | sed 's/\[.*\](//g'  | tr -d ")" \
    | sed 's/#/:/g' | sed 's/^/\.\//g'
}


parser(){
    links="$1"
    mode="$2"
    md_ending="$3"
        
    files=$(echo "$links" | cut -d ':' -f1)
    file_folders="$(echo "$files" | rev |cut -d"/" -f1 --complement | rev  | sed 's/$/\//g')"
    file_names=$(echo "$files" | rev | cut -d"/" -f1 | rev)
    line_numbers=$(echo "$links" | cut -d ':' -f2)
    file_links_relative=$(echo "$links" | cut -d ':' -f3 | sed 's/ //g')
    
    section_links=$(echo "$links" | cut -d ':' -f4)
    
    if [[ "$mode" == "relative" ]];then
        merged_path="$(paste <(echo "$file_folders") <(echo "$file_links_relative" ) -d ""  )"
    else
        if [[ ! -z "$file_links_relative" ]];then
        # Absolute path + .md ending => not a valid path
        merged_path="$(echo "$file_links_relative" | sed 's/\.md\s*$/ERR/g'  | sed 's/^/\.\/docs/g' |  sed 's/\/[^.][A-Z,a-z,0-9,-,_]*$/&\.md/g' | sed 's/\/$/\.md/g'  )"
        fi
    fi
    file_links_absolute=$(readlink -ev -- $(echo "$merged_path") 2>&1 | sed 's/^readlink.*/#INVALID LINK/g')
    file_links_absolute=$(echo "$file_links_absolute"  | sed 's@'$PWD'@\.@g')
    final_line=$(paste <(echo "$file_folders") \
                           <(echo "$file_names") \
                           <(echo "$line_numbers") \
                           <(echo "$file_links_relative") \
                           <(echo "$file_links_absolute") \
                           <(echo "$section_links") \
                           -d ":" )
    echo "$final_line"


}


get_full_link_info(){

        all_links="$(get_all_local_links)"
        relative_links="$(echo "$all_links" | grep -v "^.*:.*:\s*/")"
        absolute_links="$(echo "$all_links" | grep    "^.*:.*:\s*/" )"


        echo -e "$(parser "$relative_links" "relative")\n$(parser "$absolute_links" "absolute")" 

}
get_invalid_file_path(){
    get_full_link_info | grep "#INVALID LINK"
}

get_valid_path(){
    get_full_link_info | grep -v "#INVALID LINK"
}


get_markdown_files(){
    find docs -name "*.md" | sort | sed 's/^/\.\//g'
}

get_nav_links(){
    cat mkdocs.yml  | grep "^\s*[^#]*\.md" | cut -d":" -f 2 | sed 's/^\s/.\/docs\//g'
}
get_nav_page_links(){
    get_nav_links | grep -v "#"
}

get_md_page_links(){
    get_valid_path | cut -d ":" -f 5 | tr -d ":"  

}

get_page_links(){
    echo -e "$(get_nav_page_links)\n$(get_md_page_links)" | sort | uniq
}

get_hidden_files(){
    comm -13 <(get_page_links) <(get_markdown_files)
}


get_broken_section_links(){
    while read -r line;do
        section=$(echo "$line" | cut -d ":" -f 6)
        if [[ ! -z "$section" ]];then
            filename=$(echo "$line" | cut -d ":" -f 5)
            # The relative file link is empty if the section is in the same file
            if [[  -z "$(echo "$line" | cut -d ":" -f 4)" ]];then
                filename="$(echo "$line" | cut -d ":" -f 1-2 | tr -d ":")"
            fi

            res=$(get_section_anchors_in_file "$filename" | grep "$section")

            if [[ -z "$res" ]];then
                echo "$line"
            fi
        fi

    done <<< "$(get_valid_path)"
}

get_section_anchors_in_file(){
    site_page=$(echo "$1" |  sed 's/^\.\/docs/\.\/site/g' | sed 's/\.md$/\/index\.html/g' ) 
    cat "$site_page" | grep -o "<h[0-9] id.*\">"  | sed 's/^.*id=\"//g' | sed 's/\">$//g'
}


test_var(){
if [[ ! -z "$1" ]];then
    echo $3
    echo "$1"
    return 1
else
    echo $2
    return 0
fi
}

get_field(){
echo "$1" | cut -d ":" -f "$2"    
}
report_test_links(){

    test_res=$1
    link_type=$2


    if [[ ! -z "$test_res" ]];then
        echo "Found broken $link_type"
        folders=$(get_field "$test_res" 1 )
        files=$(get_field "$test_res" 2 | sed 's/$/ on line /g')
        line_numbers=$(get_field "$test_res" 3)
        relative_paths=$(get_field "$test_res" 4)
        sections=$(get_field "$test_res" 6 | sed 's/$/ in file /g')

        file_names=$(paste <(echo "$folders") <(echo "$files") -d "")
        refs=$(paste <(echo "$relative_paths") <(echo "$sections") -d"#")
        refs=$(echo "$refs" | sed 's/# / /g')
        first_part="$(paste <(echo "$refs") <(echo "$file_names") -d "" )"
        second_part="$(paste <(echo "$first_part") <(echo "$line_numbers") -d "" )"

        echo "$(echo "$second_part" | sed 's/^/Link /g'  | sed 's/$/ is broken/g')"

        return 1
    else
        echo "No broken $link_type found."
        return 0
    fi
}
