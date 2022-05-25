file_type="*.md"
regex="^#\{2,3\} Licenses\?"
directory="docs/apps"


APPS_WITHOUT_LICENSE=$(grep -r -L \
    --include "$file_type" \
    --exclude index.md \
    --exclude alpha.md \
    --exclude by_system.md \
    -- \
    "$regex" $directory)


if [ -n "$APPS_WITHOUT_LICENSE" ]; then
    echo "Found application(s) with no entry for license:"
    echo "$APPS_WITHOUT_LICENSE"
    exit 1
else
    echo "all applications have an entry for license"
    exit 0
fi

