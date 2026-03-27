#! /usr/bin/bash

set -o errexit \
    -o nounset

declare -ga patterns
patterns=("$@")
readonly patterns


clone_repo() {
  git clone --filter=blob:none \
            --no-checkout \
        "https://github.com/${REPO_ORG:?}/${REPO_NAME:?}.git" \
        "${CLONE_PATH:?}"
}

sparse_checkout() {
  git -C "$CLONE_PATH" sparse-checkout init --no-cone
  git -C "$CLONE_PATH" sparse-checkout set "${patterns[@]}"
  git -C "$CLONE_PATH" checkout "${REPO_BRANCH:?}"
}

main() {
  clone_repo \
  && \
  sparse_checkout
}

main
