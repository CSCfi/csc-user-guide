is_valid_slurm_option(){
   
    res=$(grep -- "$1" tests/slurm_options.txt)
    if [[ -z $res ]];then
        return 1
    else
        return 0
    fi

}

# also contains the file name and line number for the match
found_arguments="$(grep -r -n --include=\*.md "^\s*#SBATCH"  docs)"
return_val=0
wrong_list=""


while read -r option; do
    parsed_option=$(echo "$option" | grep -o "\-\-[A-Z,a-z,0-9,-]*")
    is_valid_slurm_option "$parsed_option"  
    res=$?
    if [[  "$res" -eq 1 ]];then
        wrong_list="${wrong_list}\n${option}"
        return_val=1
    fi
        
done <<< "$found_arguments"

if [[ ${return_val} -eq 0 ]];then
    echo "All option flags seem to be valid"
    exit 0
else
    echo "Found possibly invalid slurm options:"
    echo -e "$wrong_list"
    exit 1
fi

