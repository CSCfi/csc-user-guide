#! /usr/bin/bash

set -o errexit \
    -o nounset

declare -gr SOURCE_LANG_CODE=en \
            COMMIT_SHA_FILEPATH=/tmp/commit_sha.txt \
            TRANSLATION_PREFIX=/tmp/docs \
            TRANSLATION_WORKDIR=/tmp/translation \
            MOUNT_PREFIX=/translations

if (( $# != 1 )) || (( ${#1} != 2 )) || [[ $1 == "$SOURCE_LANG_CODE" ]]
then
  exit 0
else
  declare -gr TARGET_LANG_CODE=$1
fi


get_snapshots() {
  restic --json snapshots --path "${TRANSLATION_PREFIX}/${TARGET_LANG_CODE}" \
                          --latest 1 \
  > "./snapshots.json"
}

restore_latest() {
  restic restore --exclude-xattr '*' \
                 --path "${TRANSLATION_PREFIX}/${TARGET_LANG_CODE}" \
                 --target ${TRANSLATION_WORKDIR} \
           latest
}

translate() {
  env LANG_CODE="$TARGET_LANG_CODE" python3 \
                                      refresh.py \
                                        ${TRANSLATION_WORKDIR} \
                                        ${COMMIT_SHA_FILEPATH}
}

new_snapshot() {
  mkdir --parents "${TRANSLATION_PREFIX}" \
  && \
  cp --recursive \
     --no-dereference \
    ${TRANSLATION_WORKDIR}/ \
    "${TRANSLATION_PREFIX}/${TARGET_LANG_CODE}" \
  && \
  cd "${TRANSLATION_PREFIX}/${TARGET_LANG_CODE}" \
  && \
  restic backup --tag "$(cat ${COMMIT_SHA_FILEPATH})" \
                --exclude '.*' \
                --iexclude '* !*.md' \
                --skip-if-unchanged \
           ./
}

copy_translation() {
  cp --recursive \
     --no-dereference \
    ${TRANSLATION_WORKDIR}/ \
    "${MOUNT_PREFIX}/${TARGET_LANG_CODE}"
}

pre_translation() {
  get_snapshots && restore_latest
}

post_translation() {
  new_snapshot && copy_translation
}

main() {
  pre_translation \
  && \
  translate \
  &&
  post_translation
}

main
