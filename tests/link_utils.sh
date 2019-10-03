## Utility scripts to check markdown links
## This whole thing could probably be done much cleaner using
## bash + python or some other combo
## I currently don't have the time to do this,
## but I might do it at a later time
## -Henrik 9/2019

## If you have question or something is not working
## Open an issue on github.




# This function parses all the links of the form [text](link) from all .md files under .docs
# It then discards all links containing http and mailto (this are not checked)
# We we then remove all the parenthesis + remove the # from the section link and produce a : separated list
# What file is the link in: line number :link in file : section link
# The function will not parse files/paths containing the symbols []()# but I don't think
# mkdocs even handles these correctly so it is ok to throw an errror
# File paths containing : will also cause problems down the line

get_all_local_links(){
    grep -o -n -r --include \*.md   -- "\[[^]]*\]([^)(]*)" docs  | grep -v "http" | grep -v "mailto:.*@csc\.fi" \
    | sed 's/\[.*\](//g'  | tr -d ")" \
    | sed 's/#/:/g' | sed 's/^/\.\//g'
}


# This function parses the incoming list into a more verbose
# format and check if the file links are valid
# This is the function that needs the most "cleaning" to look nicer

parser(){
    links="$1"
    mode="$2"

    if [[ -z "$links" ]];then
        return 0
    fi

        
    files=$(echo "$links" | cut -d ':' -f1)
    file_folders="$(echo "$files" | rev |cut -d"/" -f1 --complement | rev  | sed 's/$/\//g')"
    file_names=$(echo "$files" | rev | cut -d"/" -f1 | rev)
    line_numbers=$(echo "$links" | cut -d ':' -f2)
    file_links_relative=$(echo "$links" | cut -d ':' -f3 | sed 's/ //g')
    
    section_links=$(echo "$links" | cut -d ':' -f4)
    
    if [[ "$mode" == "relative" ]];then
        # Relative path > correct path in the project is given by joining the folder for the file where the link is and the link itself 
        # A .md ending is required for markdown files
        merged_path="$(paste <(echo "$file_folders") <(echo "$file_links_relative" ) -d ""  )"
    
    elif [[ "$mode" == "relative_no_ending"  ]];then

        merged_path="$(paste <(echo "$file_folders") <(echo "$file_links_relative" | sed 's/^...//g' | sed 's/\/*$/\.md/' ) -d ""  )"
        echo "$merged_path" > temp.temp
    else
        # Absolute path + .md ending => not a valid path so we put a ERR to cause an error
        # Absolute paths start from ./docs/
        # In order to check if the absolute path is valid we need to append .md to it 
        # Absolute paths ending in / are also valid therefore the last sed
        # We only do one pass over file -> links of the form ![image](img/picture) (no ending and not a markdown file)
        # will give a false positive of being broken. The only fix for this is to check files without an ending twice.
        merged_path="$(echo "$file_links_relative" | sed 's/\.md\s*$/ERR/g'  | sed 's/^/\.\/docs/g' |  sed 's/\/[^.][A-Z,a-z,0-9,-,_]*$/&\.md/g' | sed 's/\/$/\.md/g'  )"
    fi
    # Using readlink to check if a file exist + resolve relative paths (../../ etc.)
    # readlink give the full path so we remove everything above ./docs
    # If the path is invalid we set the string #INVALID LINK in its place
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


# Absolute and relative links need to be handled separately
# as they have different rules for valid paths
# Absolute paths begin with /
get_full_link_info(){

        all_links="$(get_all_local_links)"
        relative_links="$(echo "$all_links" | grep -v "^.*:.*:\s*/")"
        relative_links_ending="$(echo "$relative_links" | grep -E   "^[^:]*:[^:]*:.*\.[^./]|^[^:]*:[^:]*::")"
        relative_links_no_ending="$(echo "$relative_links" | grep -v -E "^[^:]*:[^:]*:.*\.[^./]|^[^:]*:[^:]*::")"
        absolute_links="$(echo "$all_links" | grep    "^.*:.*:\s*/" )"

        echo -e "$(parser "$relative_links_ending" "relative")\n$(parser "$relative_links_no_ending" "relative_no_ending")\n$(parser "$absolute_links" "absolute")" 

}
# Get all links where the file path is invalid
get_invalid_file_path(){
    get_full_link_info | grep "#INVALID LINK"
}

# Get all links where the file path is valid
get_valid_path(){
    get_full_link_info | grep -v "#INVALID LINK"
}


# Get all markdown files in docs
get_markdown_files(){
    find docs -name "*.md" | sort | sed 's/^/\.\//g'
}

# Get all links to .md files present in the navbar
get_nav_links(){
    cat mkdocs.yml  | grep "^\s*[^#]*\.md" | cut -d":" -f 2 | sed 's/^\s/.\/docs\//g'
}

# Don't count links containing section references in the navbar
# mkdocs gives a warning and does not link to the section, so it goes right to the page
# so we consider section references in the navbar to be errors
get_nav_page_links(){
    get_nav_links | grep -v "#"
}

# Get all links to .md files which are found in the files
get_md_page_links(){
    get_valid_path | cut -d ":" -f 5 | tr -d ":"  

}

# join, sort , and remove duplicate .md links for comparison 
get_page_links(){
    echo -e "$(get_nav_page_links)\n$(get_md_page_links)" | sort | uniq
}


# Get a list of files which are present in the directory but no
# link exist to them
get_hidden_files(){
    comm -13 <(get_page_links) <(get_markdown_files)
}


## For all non empty sections check if the section is found
## as header id in the generated html file for the link target file
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

# Parse a generated html file for a .md file found in ./docs
# get all the id tags for the headers 
# This is the best way of checking if section links are valid
# as they need to match these exactly 
get_section_anchors_in_file(){
    site_page=$(echo "$1" |  sed 's/^\.\/docs/\.\/site/g' | sed 's/\.md$/\/index\.html/g' ) 
    cat "$site_page" | grep -o "<h[0-9] id.*\">"  | sed 's/^.*id=\"//g' | sed 's/\">$//g'
}

# Function used to display the test results
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

# Helper function to extract fields from our list
get_field(){
echo "$1" | cut -d ":" -f "$2"    
}

# Function used to display the test results
# Very ugly
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
