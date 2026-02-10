#! /usr/bin/bash

set -o errexit \
    -o nounset
shopt -s dotglob

declare -gr CLONE_PATH=/tmp/${REPO_NAME:?} \
            DOCS_DIR=docs \
            TRANSLATION_MOUNT_PREFIX=/translations \
            BUILD_WORKDIR=/tmp/site \
            BUILD_MOUNT_PREFIX=/site

if (( $# != 1 )) || (( ${#1} != 2 ))
then
  exit 0
else
  declare -gr TARGET_LANG_CODE=$1
  export SITE_URL=${SITE_BASE_URL:?}/${TARGET_LANG_CODE}
fi

clone() {
  git clone --filter=blob:none \
            --no-checkout \
        "https://github.com/${REPO_ORG:?}/${REPO_NAME:?}.git" \
        "$CLONE_PATH"
}

sparse_checkout() {
  git -C "$CLONE_PATH" sparse-checkout init --no-cone
  git -C "$CLONE_PATH" sparse-checkout set \
                                         "/${DOCS_DIR}" \
                                         /csc-overrides \
                                         /hooks \
                                         /scripts \
                                         mkdocs.yml \
                                         "mkdocs_${TARGET_LANG_CODE}.yml" \
                                         .git-revision-date-ignore-revs
  git -C "$CLONE_PATH" checkout "${REPO_BRANCH:?}"
}

get_clone() {
  cp --recursive \
     --no-dereference \
    "${CLONE_PATH}/"* \
    ./
}

get_translation() {
  local -r source_dir="${TRANSLATION_MOUNT_PREFIX}/${TARGET_LANG_CODE}"

  if [[ -d $source_dir ]] && \
     ! [[ -z $(find "$source_dir" -mindepth 1 -maxdepth 1) ]]
  then
    cp --recursive \
       --no-dereference \
       --force \
      "${source_dir}/"* \
      "./${DOCS_DIR}/"
  else
    echo "No new translation for '${TARGET_LANG_CODE}', exiting..."
    exit 0
  fi
}

build() {
  mkdocs build --site-dir="${BUILD_WORKDIR}/" \
               --config-file="mkdocs_${TARGET_LANG_CODE}.yml"
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
    "${BUILD_MOUNT_PREFIX:?}/${TARGET_LANG_CODE:?}"*
}

copy_site() {
  local -r target_dir="${BUILD_MOUNT_PREFIX:?}/${TARGET_LANG_CODE:?}"

  if ! [[ -d $target_dir ]]
  then
    mkdir "$target_dir"
  fi

  cp --recursive \
     --no-dereference \
    ${BUILD_WORKDIR}/* \
    "$target_dir"
}

pre_build() {
  clone \
  && \
  sparse_checkout \
  && \
  get_clone \
  && \
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
