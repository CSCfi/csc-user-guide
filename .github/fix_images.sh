#!/bin/bash
image_urls=($(grep -r -- "(.*user-image.*)" docs/ | cut -d "(" -f2 | cut -d ")" -f1 ))
mkdir temp_img
cd temp_img
for i in ${image_urls[@]}; do
    wget $i
done
cd ..
cp -r temp_img/* docs/img/
find docs -name "*.md" -exec sed -i --follow-symlinks  's@https://user-images\.githubusercontent\.com/[0-9]*/@/img/@g' {} \;
