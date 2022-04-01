#!/bin/bash
t_dir="docs/support/wn"


cd $t_dir
for filename in ./*; do
    title=$(grep "^# " $filename | sed 's/#//g')
    echo -e "\n## $title\n" >> ../../index.md
    echo -e "\n## $title\n" >> ../whats-new.md
    topics=$(grep "^## " $filename | sed 's/#//g' | sed 's/ *$//g' | sed 's/^ *//g' )
    i=0
    while IFS= read -r topic; do
        echo "- [$topic](wn/$(echo $filename | sed 's@^./@@g')#$(python ../../../scripts/convert.py "$topic") )" >> ../whats-new.md
        if [[ "$i" -lt 5 ]]; then
            echo "- [$topic](support/wn/$(echo $filename | sed 's@^./@@g')#$(python ../../../scripts/convert.py "$topic") )" >> ../../index.md
            let i++
        fi
    done <<< "$topics"     
done
