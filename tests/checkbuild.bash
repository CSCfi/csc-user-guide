




build_out=$(mkdocs build 2>&1)
res_val=$?

if [ $res_val = 0 ]; then
	
    NUMBERS_OF_WARNINGS=$(echo "$build_out" |grep -i  WARNING |wc -l)
    if [ $NUMBERS_OF_WARNINGS -ne 0 ]; then 
        echo "BUILD COMPLETED WITH WARNINGS:"
        echo "$build_out" |grep -i  WARNING
    exit 1
     else
	echo "BUILD SUCCESSFUL"
    exit 0
    fi


else
	echo "BUILD FAILED"
	echo "$build_out"
	exit 1
fi
