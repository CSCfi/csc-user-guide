file_type="*.md"
directory="docs/apps"
regex="## License"

APPS_WITHOUT_LICENSE=$(grep -rL --include "$file_type" --exclude index.md -- "$regex" $directory)

if [ -n "$APPS_WITHOUT_LICENSE" ]; then
    echo "Found application(s) with no entry for license:"
    echo "$APPS_WITHOUT_LICENSE"
    exit 1
else
    echo "all applications have an entry for license"
    exit 0
fi

