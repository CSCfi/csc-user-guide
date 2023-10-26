#!/bin/bash
set -e

usage="Usage: $(basename "$0") [-h] [-u]
Print last update timestamp and most recent committer for each Docs page.

Options:
    -h  show this help text
    -u  only show pages no one has touched after you"

while getopts "hu" option; do
  case "$option" in
    u) name="$(git config user.name)";; 
    h) echo "$usage"; exit;;
    *) echo "$usage"; exit;;
  esac
done

declare -A seen

# Loop to get most recent commit
while read -r line ; do
    if [[ "$line" = /* ]] ; then
        date="${line#* }"
        date="${date:0:10}"
        committer="${line#* }"
        committer="${committer:11}"
    elif [[ "$line" && -z "${seen[$line]}" ]] ; then
        seen["$line"]="$date, $committer"
    fi
done < <(git log --format="/%H %as %an" --name-only)

declare -A first

# Loop again to get initial commit
while read -r line ; do
    if [[ "$line" = /* ]] ; then
        committer="${line#* }"
    elif [[ "$line" && -z "${first[$line]}" ]] ; then
        first["$line"]="$committer"
    fi
done < <(git log --reverse --format="/%H %an" --name-only)

git ls-files "*.md" | while read f ; do
    f="${f#./}"
    printf "%-40s %-30s %s\n" "${seen[$f]}" "${first[$f]}" "$f" \
    | iconv -f iso-8859-1 -t utf-8
done | sort -r | grep "$name"

printf "%-40s %-30s %s\n" "--------------------" "---------------" "--------"
printf "%-40s %-30s %s\n" "Page last updated by" "Page created by" "Filename"
