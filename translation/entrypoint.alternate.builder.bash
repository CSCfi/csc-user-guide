#! /usr/bin/bash

set -o errexit \
    -o nounset
shopt -s dotglob

export CLONE_PATH=/tmp/${REPO_NAME:?}
declare -gr TRANSLATION_MOUNT_PREFIX=/translations \
            BUILD_WORKDIR=/tmp/site \
            BUILD_MOUNT_PREFIX=/site
declare -gr SOURCE_DIR=${TRANSLATION_MOUNT_PREFIX}/${LANG_CODE:?} \
            TARGET_DIR=${BUILD_MOUNT_PREFIX}/${LANG_CODE:?}
declare -gra CONFIG_FILES=(
  mkdocs.yml
  "mkdocs_${LANG_CODE:?}.yml"
  .git-revision-date-ignore-revs
)
declare -gra SPARSE_PATTERNS=(
  "/${DOCS_DIR:?}/"
  /csc-overrides/
  /hooks/
  /scripts/convert.py
  /scripts/generate_glossary.sh
  /scripts/generate_new.sh
  "${CONFIG_FILES[@]/#//}"
)


get_clone() {
  cp --recursive \
     --no-dereference \
    "${CLONE_PATH}/"* \
    ./
}

get_config() {
  # Save values before modifying
  local -r clone_path_orig=$CLONE_PATH \
           repo_branch_orig=$REPO_BRANCH

  export CLONE_PATH=${clone_path_orig}-config \
         REPO_BRANCH=${CONFIG_BRANCH:?}
  /sparse-clone.bash "${CONFIG_FILES[@]/#//}"

  cp --no-dereference \
    "${CONFIG_FILES[@]/#/${CLONE_PATH}/}" \
    ./

  # Restore values
  [[ -n ${clone_path_orig:-} ]] && export CLONE_PATH=$clone_path_orig
  [[ -n ${repo_branch_orig:-} ]] && export REPO_BRANCH=$repo_branch_orig
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
    echo "No new translation for '${LANG_CODE:?}', exiting..."
    exit 0
  fi
}

build() {
  mkdocs build --site-dir="${BUILD_WORKDIR}/" \
               --config-file="mkdocs_${LANG_CODE:?}.yml"
}

run_scripts() {
  for feat in new glossary
  do
    bash scripts/generate_${feat}.sh
  done
}

cleanup_site() {
  rm --recursive \
     --force \
    "${TARGET_DIR:?}"*
}

copy_site() {
  mkdir  --parents "$TARGET_DIR"

  cp --recursive \
     --no-dereference \
    ${BUILD_WORKDIR}/* \
    "$TARGET_DIR"
}

pre_build() {
  /sparse-clone.bash "${SPARSE_PATTERNS[@]}" \
  && \
  get_clone \
  && {
    if [[ -n ${CONFIG_BRANCH:-} ]]
    then
      get_config
    fi
  } && \
  get_translation \
  && \
  run_scripts
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
