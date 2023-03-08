#!/bin/sh
source_dir="csc-overrides/assets/glossaries"
glossary_dir="docs/support"
generated_file="$glossary_dir/glossary.md"

echo -e "# Glossary\n" > $generated_file

first_letter="A"
echo -e "## $first_letter\n" >> $generated_file

cat $source_dir/*.md |
uniq |
sort -f |
awk -F ": " '{ gsub(/\*\[|\]/, "`"); print $1 " &mdash; " "_" $2 "_" }' |
while read line; do
  new_first_letter="${line:1:1}"
  if [ "$new_first_letter" != "$first_letter" ]; then
    first_letter="$new_first_letter"
    echo -e "\n## $first_letter\n" >> $generated_file
  fi
  echo -e "* $line" >> $generated_file
done
