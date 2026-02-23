#! /usr/bin/bash

set -o errexit \
    -o nounset

# Don't translate to source language
if [[ ${LANG_CODE:?} == 'en' ]]
then
  echo "Target language '${LANG_CODE}' is source language, exiting..."
  exit 0
fi

export CLONE_PATH=/tmp/${REPO_NAME:?}
declare -gr COMMIT_SHA_FILEPATH=/tmp/commit_sha.txt \
            CACHED_OBJS_FILEPATH=/tmp/cached_objects.json \
            TRANSLATION_WORKDIR=/tmp/translation \
            MOUNT_PREFIX=/translations \
            SNAPSHOT_PREFIX=/tmp/${DOCS_DIR:?}
declare -gr SNAPSHOT_PATH=${SNAPSHOT_PREFIX}/${LANG_CODE:?}
declare -gra CONFIG_FILES=(
  translation/exclude.txt
  translation/force.yml
  translation/dictionary.yml
)
declare -gra SPARSE_PATTERNS=(
  "/${DOCS_DIR:?}/**/*.md"
  "${CONFIG_FILES[@]/#//}"
)


get_snapshots() {
  restic --json snapshots --path "${SNAPSHOT_PATH}" \
  > ./snapshots.json
}

restore_latest() {
  restic restore --exclude-xattr '*' \
                 --path "${SNAPSHOT_PATH}" \
                 --target ${TRANSLATION_WORKDIR} \
           latest
}

get_config() {
  if [[ -n ${CONFIG_BRANCH:-} ]]
  then
    # Save values before modifying
    local -r clone_path_orig=$CLONE_PATH \
             repo_branch_orig=$REPO_BRANCH

    export CLONE_PATH=${clone_path_orig}-config \
           REPO_BRANCH=$CONFIG_BRANCH
    /sparse-clone.bash "${CONFIG_FILES[@]/#//}"
  fi

  cp --no-dereference \
    "${CONFIG_FILES[@]/#/${CLONE_PATH}/}" \
    ./

  # Restore values
  [[ -n ${clone_path_orig:-} ]] && export CLONE_PATH=$clone_path_orig
  [[ -n ${repo_branch_orig:-} ]] && export REPO_BRANCH=$repo_branch_orig
}

translate() {
  python3 refresh_translation.py \
            $TRANSLATION_WORKDIR \
            $COMMIT_SHA_FILEPATH \
            $CACHED_OBJS_FILEPATH
}

new_snapshot() {
  mkdir --parents "${SNAPSHOT_PREFIX}"

  cp --recursive \
     --no-dereference \
    ${TRANSLATION_WORKDIR}/ \
    "$SNAPSHOT_PATH"

  if [[ -d $SNAPSHOT_PATH ]] && \
     [[ -f $COMMIT_SHA_FILEPATH ]]
  then
    cd "$SNAPSHOT_PATH" \
    && \
    restic backup --tag "$(cat ${COMMIT_SHA_FILEPATH})" \
                  --exclude '.*' \
                  --iexclude '* !*.md' \
                  --skip-if-unchanged \
            ./
  fi
}

copy_translation() {
  cp --recursive \
     --no-dereference \
    ${TRANSLATION_WORKDIR}/ \
    "${MOUNT_PREFIX}/${LANG_CODE:?}"
}

pre_translation() {
  get_snapshots \
  && \
  restore_latest \
  && \
  /sparse-clone.bash "${SPARSE_PATTERNS[@]}" \
  && \
  get_config
}

post_translation() {
  new_snapshot \
  && \
  copy_translation \
  && \
  python3 clear_cache.py $CACHED_OBJS_FILEPATH
}

main() {
  pre_translation \
  && \
  translate \
  && \
  post_translation
}

main
