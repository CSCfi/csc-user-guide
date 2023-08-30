#!/bin/bash
set -e

usage="Usage: $(basename "${0}") [-h] [-n \"NAME\"]
Print last update timestamp and most recent committer for each page.

Options:
    -h  show this help text
    -n  filter based on user"

while getopts "hn:" option; do
  case "${option}" in
    n) NAME="${OPTARG}";; 
    h) echo "${usage}"; exit;;
    *) echo "${usage}"; exit;;
  esac
done

declare -A seen

while read -r line ; do
    if [[ $line = /* ]] ; then
        date=${line#* }
        date=${date:0:25}
        committer=${line#* }
        committer=${committer:26}
    elif [[ $line && -z ${seen[$line]} ]] ; then
        seen[$line]="$date, $committer"
    fi
done < <(git log --format='/%H %ai %an' --name-only)

git ls-files '*.md' | while read f ; do
    f=${f#./}
    printf '%s %s\n' "${seen[$f]}" "$f"
done | sort -r | grep "$NAME"
