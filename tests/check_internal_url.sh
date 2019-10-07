internal_urls=$(grep -o -n -r --include \*.md   -- "\[[^]]*\]([^)(]*)" docs  | grep "http" | grep "docs.csc.fi")

if [[ ! -z "$internal_urls" ]];then
    echo -e "Found web urls pointing to docs.csc.fi"
    echo -e "Please change these to internal markdown links"
    urls=$(echo "$internal_urls" | sed 's/.*](//g' | sed 's/)$//g')
    files=$(echo "$internal_urls" | cut -d ":" -f 1 )
    lines=$(echo "$internal_urls" | cut -d ":" -f 2 )



    url_part=$(echo "$urls" | sed 's/^/Url /' | sed 's/$/ on line /g' )
    line_part=$(echo "$lines" | sed 's/$/ in file /g')
    file_part=$(echo "$files" | sed 's/$/ points to docs.csc.fi/g')

    paste <(echo "$url_part") <(echo "$line_part") <(echo "$file_part") -d ""  
    exit 1

else
    echo "No web urls pointing to docs.csc.fi found"
    exit 0
fi

