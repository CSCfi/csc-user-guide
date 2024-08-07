#!/bin/sh
app_dir="docs/apps"
generated_file="$app_dir/index.md"

echo -e "# Applications\n" > $generated_file

echo -e '!!! default "Cannot find the application you are looking for?"' >> $generated_file
echo -e "    * [See here for ways to install software yourself](../computing/installing.md)." >> $generated_file
echo -e "    * You may also [contact CSC Service Desk](../support/contact.md) with your software" >> $generated_file
echo -e "      installation request. Given enough requests, we may consider pre-installing a particular" >> $generated_file
echo -e "      application, or purchasing a license for it if the software in question is proprietary." >> $generated_file
echo -e "    * Although we cannot promise to pre-install all requested applications, CSC Service Desk" >> $generated_file
echo -e "      is happy to support you in installing software yourself.\n" >> $generated_file

echo -e "- [By discipline](by_discipline.md)" >> $generated_file
echo -e "- [By availability](by_system.md)" >> $generated_file
echo -e "- [By license](by_license.md)" >> $generated_file

echo -e "\n## Applications in alphabetical order\n" >> $generated_file
grep \* $app_dir/by_discipline.md | sort -f | uniq >> $generated_file
