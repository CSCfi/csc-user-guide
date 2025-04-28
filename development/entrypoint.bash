#! /usr/bin/env bash

set -e

declare -gr mkdocs_BIN='/usr/local/bin/mkdocs' \
            mkdocs_IP='0.0.0.0' \
            mkdocs_PORT='8000'

mkdocs_serve() {
  $mkdocs_BIN 'serve' --dev-addr=${mkdocs_IP}:${mkdocs_PORT} "$@"
}

case $1 in
  '')
    $mkdocs_BIN
  ;;
  serve)
    shift 1
    mkdocs_serve "$@"
  ;;
  *)
    $mkdocs_BIN "$@"
  ;;
esac
