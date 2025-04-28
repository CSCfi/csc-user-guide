#!/bin/bash
set -e

usage="Usage: $(basename "$0") [-h] [-u]
Print last update timestamp and most recent committer for each Docs page.

Options:
    -h  show this help text
    -u  only show pages no one has touched after you
    -p  path to restrict the report
    -s  Since when to report changes

    Example: $(basename "$0") -p docs/cloud -s 2025-01-02
    "
while getopts "hp:s:u" option; do
  case "$option" in
    u) name="$(git config user.name)";;
    p) path=${OPTARG};;
    s) since=${OPTARG};;
    h) echo "$usage"; exit;;
    *) echo "$usage"; exit;;
  esac
done

if [ -n "$since" ];
then
  GIT_LOG_OPTS="$GIT_LOG_OPTS --since=$since"
fi

if [ -n "$path" ];
then
    GIT_LOG_OPTS="$GIT_LOG_OPTS $path"
fi

declare -A seen

# Loop to get most recent commit
while read -r line ; do
    if [[ "$line" = /* ]] ; then
        date="${line#* }"
        date="${date:0:10}"
        committer="${line#* }"
        committer="${committer:11}"
    elif [[ "$line" && -z "${seen[$line]}" ]] ; then
        seen["$line"]="$date"
    fi
done < <(git log --format="/%H %as %an" --name-only "$GIT_LOG_OPTS")

echo "|Updated|Filename|Head line|"
echo "|:-:|:-:|:-:|"

git ls-files "$path*.md" | while read -r f ; do
    f="${f#./}"
    if [ -n "${seen[$f]}" ];
    then
      head_line=$(grep -oP '^\#\s\K.*$' "$f" | head -1)

      if [ -z "$head_line" ];
      then
        echo "##### $f"
      fi

      echo "|${seen[$f]}|$f|$head_line|"\
      | iconv -f iso-8859-1 -t utf-8
    fi
done | sort -r | grep "$name"

