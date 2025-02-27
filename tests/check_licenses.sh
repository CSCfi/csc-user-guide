#!/usr/bin/env sh

file_type="*.md"
regex="^#\{2,3\} Licenses\?"
directory="docs/apps"


APPS_WITHOUT_LICENSE=$(grep -r -L \
    --include "$file_type" \
    --exclude index.md \
    --exclude by_discipline.md \
    --exclude by_system.md \
    --exclude by_license.md \
    --exclude bioconda.md \
    --exclude discovery-studio.md \
    --exclude materialsstudio.md \
    --exclude nomachine.md \
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

