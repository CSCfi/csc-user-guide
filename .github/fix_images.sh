#!/bin/bash
image_urls=($(grep -r -- "(.*user-image.*)" docs/ | cut -d "(" -f2 | cut -d ")" -f1 ))
mkdir temp_img
cd temp_img
for i in ${image_urls[@]}; do
    wget $i
done
cd ..
cp -r temp_img/* docs/img/
