#!/bin/bash

declare -A seen

while read -r line ; do
    if [[ $line = /* ]] ; then
        hash=${line%% *}
        date=${line#* }
        date=${date:0:25}
        committer=${line#* }
        committer=${committer:26}
    elif [[ $line && -z ${seen[$line]} ]] ; then
        seen[$line]="$date, $committer"
    fi
done < <(git log --format='/%H %ai %an' --name-only)

find -name .git -prune -or -print | while read f ; do
    f=${f#./}
    printf '%s %s\n' "${seen[$f]}" "$f"
done | sort | grep "$(git config user.name)"
