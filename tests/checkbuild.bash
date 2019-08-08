
build_out=$(mkdocs build 2>&1)
res_val=$?

if [ $res_val = 0 ]; then
	echo "BUILD SUCCESSFUL"
	exit 0
else
	echo "BUILD FAILED"
	echo "$build_out"
	exit 1
fi
