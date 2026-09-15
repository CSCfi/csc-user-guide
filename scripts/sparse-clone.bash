#! /usr/bin/bash

clone_repo() {
  local -r repo_host=${1:?} \
           repo_org=${2:?} \
           repo_name=${3:?} \
           clone_path=${4:?}

  git clone --filter=blob:none \
            --no-checkout \
        "https://${repo_host}/${repo_org}/${repo_name}.git" \
        "$clone_path"
}

sparse_checkout() {
  local -r repo_branch=${1:?} \
           clone_path=${2:?}
  local -rn _sparse_patterns=${3:?}

  git -C "$clone_path" sparse-checkout init --no-cone
  git -C "$clone_path" sparse-checkout set "${_sparse_patterns[@]}"
  git -C "$clone_path" checkout "$repo_branch"
}

get_config() {
  local -ra config_files=("${@:?}")

  shopt -s extglob
  local -r clone_path="${CLONE_PATH:?}"
  local -r effective_path="${clone_path%%+(/)}${CONFIG_BRANCH:+-config}"
  shopt -u extglob

  if [[ -n ${CONFIG_BRANCH:-} ]]
  then
    clone_repo "${REPO_HOST:?}" \
               "${REPO_ORG:?}" \
               "${REPO_NAME:?}" \
               "$effective_path"

    # shellcheck disable=SC2034
    local -ra config_patterns=("${config_files[@]/#//}")
    local -r repo_branch="${REPO_BRANCH:?}"

    sparse_checkout "${CONFIG_BRANCH:-$repo_branch}" \
                    "$effective_path" \
                    config_patterns
  fi

  cp --verbose \
     --no-dereference \
    "${config_files[@]/#/${effective_path}/}" \
    ./
}

if ! (return 0 2>/dev/null)
then
    set -eo pipefail

    # shellcheck disable=SC2034
    declare -a patterns=("$@")

    clone_repo "${REPO_HOST:?}" "${REPO_ORG:?}" "${REPO_NAME:?}" "${CLONE_PATH:?}" \
    && \
    sparse_checkout "${REPO_BRANCH:?}" "${CLONE_PATH:?}" patterns
fi
