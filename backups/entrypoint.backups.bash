#!/usr/bin/bash

set -o errexit \
    -o nounset \
    -o pipefail

declare repo_dir repo_path repo_url refs_hash refs_tag
repo_dir="${REPO_NAME:?}.git"
repo_path="${HOME:?}/${repo_dir}"
repo_url="https://${REPO_HOST:?}/${REPO_ORG:?}/${repo_dir}"
refs_hash="$(git ls-remote "$repo_url" | sha256sum | cut -c1-16)"
refs_tag="refs:${refs_hash}"
readonly repo_dir repo_path repo_url refs_hash refs_tag

declare -ra snapshot_selectors=(--host "$RESTIC_HOST" --path "$repo_path")

git_in_dir() {
  git -C "$repo_path" "$@"
}
snapshots_json() {
  restic snapshots --json "${snapshot_selectors[@]}" "$@"
}

has_matches() {
  printf '%s' "$1" | jq --exit-status 'length > 0' >/dev/null
}

first_run() {
  ! has_matches "$(snapshots_json)"
}

repo_changed() {
  ! has_matches "$(snapshots_json --tag "$refs_tag" --latest 1)"
}

clone_repo() {
  git clone --mirror "$repo_url" "$repo_path"
}

set_config() {
  git_in_dir config gc.auto 0
  git_in_dir config maintenance.auto 0
}

update_mirror() {
  git_in_dir fetch --prune origin
}

restore_latest() {
  restic restore latest "${snapshot_selectors[@]}" \
                        --exclude-xattr '*' \
                        --target "$HOME"
}

new_snapshot() {
  restic backup --host "$RESTIC_HOST" \
                --tag "$refs_tag" \
           "$repo_dir"
}

main() {
  if first_run
  then
    clone_repo
    set_config
    new_snapshot
  elif repo_changed
  then
    restore_latest
    update_mirror
    set_config
    new_snapshot
  else
    echo 'Repository unchanged, skipping snapshot.'
  fi
}

main
