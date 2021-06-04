t_dir="docs/support/wn"
main_page_link="../../whats-new.md"
main_page="docs/support/whats-new.md"


cd $t_dir
for filename in ./*; do
    title=$(grep "^# " $filename | sed 's/#//g')
    echo -e "\n## $title\n" >> ../whats-new.md
    topics=$(grep "^## " $filename | sed 's/#//g' | sed 's/ *$//g' | sed 's/^ *//g' )
    while IFS= read -r topic; do
        echo "- [$topic](wn/$(echo $filename | sed 's@^./@@g')#$(python ../../../scripts/convert.py "$topic") )" >> ../whats-new.md 
    done <<< "$topics"     
done
