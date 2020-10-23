

# .md files can not have the same name as directory
# on the same level in the hierarchy as they will be
# Masked and not visible



index_files=$(find docs/ -mindepth 2 -name "index.md")
RET=0

while read -r file; do
    masked_md=$(echo $file | sed  's@/index@@g')
    if [[ -f $masked_md ]];then
        RET=1
        echo "File docs/$masked_md is masked by docs/$file"
    fi
done<<<"$index_files"
if [[ $RET -eq 0 ]];then
    echo "No masked files found"
    exit 0 
else
    exit 1
fi
