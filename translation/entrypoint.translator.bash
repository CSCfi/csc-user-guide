#! /usr/bin/bash

set -o errexit

# shellcheck source=SCRIPTDIR/../scripts/sparse-clone.bash
source /sparse-clone.bash

# Don't translate to source language
if [[ ${LANG_CODE:?} == 'en' ]]
then
  echo "Target language '${LANG_CODE}' is source language, exiting..."
  exit 0
fi

declare -r CLONE_PATH=${APP_ROOT}/${REPO_NAME:?} \
           COMMIT_SHA_FILEPATH=${APP_ROOT}/commit_sha.txt \
           CACHED_OBJS_FILEPATH=${APP_ROOT}/cached_objects.json \
           TRANSLATION_WORKDIR=${APP_ROOT}/translation \
           MOUNT_PREFIX=/translations \
           SNAPSHOT_PREFIX=${APP_ROOT}/${DOCS_DIR:?}
declare -r SNAPSHOT_PATH=${SNAPSHOT_PREFIX}/${LANG_CODE:?}
declare -ra CONFIG_FILES=(
  translation/exclude.txt
  translation/force.yml
  translation/dictionary.yml
)
# shellcheck disable=SC2034
declare -ra SPARSE_PATTERNS=(
  "/${DOCS_DIR:?}/**/*.md"
  "${CONFIG_FILES[@]/#//}"
)

dryrun_disabled() {
  [[ -z ${RESTORE_ONLY:-} \
    || ${RESTORE_ONLY,,} =~ ^false$ \
    || ($RESTORE_ONLY =~ ^[0-9]+$ && $RESTORE_ONLY -eq 0) ]]
}

get_snapshots() {
  restic --json snapshots --path "${SNAPSHOT_PATH}" \
  > ./snapshots.json
}

restore_latest() {
  restic restore --exclude-xattr '*' \
                 --path "${SNAPSHOT_PATH}" \
                 --target "${TRANSLATION_WORKDIR}" \
           latest
}

translate() {
  python refresh_translation.py \
           "$TRANSLATION_WORKDIR" \
           "$COMMIT_SHA_FILEPATH" \
           "$CACHED_OBJS_FILEPATH"
}

new_snapshot() {
  mkdir --parents "${SNAPSHOT_PREFIX}"

  cp --recursive \
     --no-dereference \
    "${TRANSLATION_WORKDIR}/" \
    "$SNAPSHOT_PATH"

  if [[ -d $SNAPSHOT_PATH ]] && \
     [[ -f $COMMIT_SHA_FILEPATH ]]
  then
    cd "$SNAPSHOT_PATH" \
    && \
    restic backup --tag "$(cat "${COMMIT_SHA_FILEPATH}")" \
                  --exclude '.*' \
                  --iexclude '* !*.md' \
                  --skip-if-unchanged \
            ./ \
    && \
    cd -
  fi
}

copy_translation() {
  cp --recursive \
     --no-dereference \
    "${TRANSLATION_WORKDIR}/" \
    "${MOUNT_PREFIX}/${LANG_CODE:?}"
}

pre_translation() {
  get_snapshots \
  && \
  restore_latest \
  && \
  clone_repo "${REPO_HOST:?}" "${REPO_ORG:?}" "${REPO_NAME:?}" "${CLONE_PATH:?}" \
  && \
  sparse_checkout "${REPO_BRANCH:?}" "${CLONE_PATH:?}" SPARSE_PATTERNS \
  && \
  get_config "${CONFIG_FILES[@]}"
}

post_translation() {
  new_snapshot \
  && \
  copy_translation \
  && \
  if dryrun_disabled
  then
    python clear_cache.py "$CACHED_OBJS_FILEPATH"
  fi
}

main() {
  pre_translation \
  && \
  if dryrun_disabled
  then
    translate
  fi \
  && \
  post_translation
}

main
