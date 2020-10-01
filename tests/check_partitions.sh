part_flags=$(grep -E -n -r --include \*.md "^\s*#SBATCH\s*--partition=" docs)
res=$(echo "$part_flags" | grep -Ev "#SBATCH\s*--partition=(All|small|large|medium|gc|test|longrun|fmi|hugemem|hugemem_longrun|gputest|gpu|interactive)")

if [[ -z $res ]]; then
    echo "All partition names seem to be valid"
    exit 0

else
    echo "Found possibly invalid partitions."
    echo $res
    exit 1
fi

