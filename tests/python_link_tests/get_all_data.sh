
get_all_internal_links(){
    grep -o -n -r --include \*.md   -- "\[[^]]*\]([^)(]*)" $1 | sed 's/(\s*/(/g'  | egrep -v "https?://" | grep -v "mailto:"  | sed 's/\[.*\](//g' | sed 's/)$//g' | sed 's/\(.*\)#/\1:/' | sed 's/".*"//g' \
    | awk '{print $1}'
}

get_all_files(){
    find $1 -type f 
}

get_all_headders(){
    grep -r -o -n "<h[0-9] id=.*\">" --include \*.html $1
}

get_all_anchors(){
    grep -E -r -o -n "<a name=.*\">|<a id=.*\">" --include \*.html $1
}



get_all_nav_links(){
    grep "^\s*[^#]*\.md\s*$" "$1" | sed -e 's#^.*\s\(\S*\.md\)\s*$#docs/\1#'
}




link_list=$1
file_list=$2
headder_list=$3
nav_list=$4


get_all_internal_links "docs" > "$link_list"
get_all_files "docs" > "$file_list"
get_all_headders "site" > "$headder_list"
get_all_anchors "site" >> "$headder_list"
get_all_nav_links "mkdocs.yml" > "$nav_list"

