#! /usr/bin/bash

set -o errexit \
    -o nounset
shopt -s dotglob

# shellcheck source=SCRIPTDIR/../scripts/sparse-clone.bash
source /sparse-clone.bash

declare -r CLONE_PATH=${APP_ROOT}/${REPO_NAME:?} \
           TRANSLATION_MOUNT_PREFIX=/translations \
           BUILD_WORKDIR=${APP_ROOT}/site \
           BUILD_MOUNT_PREFIX=/site
declare -r SOURCE_DIR=${TRANSLATION_MOUNT_PREFIX}/${LANG_CODE:?} \
           TARGET_DIR=${BUILD_MOUNT_PREFIX}/${LANG_CODE:?}
declare -ra CONFIG_FILES=(
  properdocs.yml
  "properdocs_${LANG_CODE:?}.yml"
)
# shellcheck disable=SC2034
declare -ra SPARSE_PATTERNS=(
  "/${DOCS_DIR:?}/"
  /hooks/
  /includes/
  /overrides/
  "${CONFIG_FILES[@]/#//}"
)


get_clone() {
  cp --recursive \
     --no-dereference \
    "${CLONE_PATH}/"* \
    ./
}

get_translation() {
  if [[ -d $SOURCE_DIR ]] && \
     [[ -n $(find "$SOURCE_DIR" -mindepth 1 -maxdepth 1) ]]
  then
    cp --recursive \
       --no-dereference \
       --force \
      "${SOURCE_DIR}/"* \
      "./${DOCS_DIR}/"
  else
    echo "No translation for '${LANG_CODE:?}'." >&2
    exit 1
  fi
}

build() {
  properdocs build --site-dir="${BUILD_WORKDIR}/" \
               --config-file="properdocs_${LANG_CODE:?}.yml"
}

cleanup_site() {
  rm --recursive \
     --force \
    "${TARGET_DIR:?}/"*
}

copy_site() {
  cp --recursive \
     --no-dereference \
    "${BUILD_WORKDIR}/"* \
    "$TARGET_DIR"
}

pre_build() {
  clone_repo "${REPO_HOST:?}" "${REPO_ORG:?}" "${REPO_NAME:?}" "${CLONE_PATH:?}" \
  && \
  sparse_checkout "${REPO_BRANCH:?}" "${CLONE_PATH:?}" SPARSE_PATTERNS \
  && \
  get_clone \
  && {
    if [[ -n ${CONFIG_BRANCH:-} ]]
    then
      get_config
    fi
  } && \
  get_translation
}

post_build() {
  cleanup_site && copy_site
}

main() {
  pre_build \
  && \
  build \
  && \
  post_build
}

main
