
regex="iframe.* src="

IFRAME_WITH_SRC=$(grep -o -i -n -r --include \*.md -- "$regex" docs)

if [[ ! -z "$IFRAME_WITH_SRC" ]];then
    echo -e "Found iframe with src attribute"
    echo -e "Please change this to srcdoc, so that our cookie blocking works\n"
    files=$(echo "$IFRAME_WITH_SRC" | cut -d ":" -f 1 )
    lines=$(echo "$IFRAME_WITH_SRC" | cut -d ":" -f 2 )
    line_part=$(echo "$lines" | sed 's/$/ in file /g' | sed 's/^/Line /')
    file_part=$(echo "$files" | sed 's/$/ contains iframe with src/g')
    paste <(echo "$line_part") <(echo "$file_part") -d ""  
    exit 1

else
    echo "iframes are correct"
    exit 0
fi
