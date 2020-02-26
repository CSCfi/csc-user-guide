FOUND_FIXME=$(grep -o -i -n -r --include \*.md -- FIXME docs ) 


if [[ ! -z "$FOUND_FIXME" ]];then
    echo -e "Documentation contains FIXME"
    echo -e "Please correct the documentation and remove the FIXME\n"
    files=$(echo "$FOUND_FIXME" | cut -d ":" -f 1 )
    lines=$(echo "$FOUND_FIXME" | cut -d ":" -f 2 )
    line_part=$(echo "$lines" | sed 's/$/ in file /g' | sed 's/^/Line /')
    file_part=$(echo "$files" | sed 's/$/ contains FIXME/g')
    paste <(echo "$line_part") <(echo "$file_part") -d ""  
    exit 1

else
    echo "No FIXME found in the documentation"
    exit 0
fi
