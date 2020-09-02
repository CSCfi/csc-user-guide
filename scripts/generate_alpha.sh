app_dir="docs/apps"
ignores="--exclude-from=scripts/skip_alpha.txt"
echo -e "<h1> Applications in alphabetical order</h1>\n" > $app_dir/alpha.md
grep \* $app_dir/index.md | sort -f | uniq >> $app_dir/alpha.md
