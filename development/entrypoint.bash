#! /usr/bin/bash

set -e

declare -gr mkdocs_BIN='/usr/local/bin/mkdocs' \
            mkdocs_BASE_CONFIG='mkdocs.yml' \
            mkdocs_IP='0.0.0.0' \
            mkdocs_PORT='8000'

get_config() {
  cat << EOF
INHERIT: ${mkdocs_BASE_CONFIG}
dev_addr: ${mkdocs_IP}:${mkdocs_PORT}
EOF
}

mkdocs_serve() {
  get_config | $mkdocs_BIN 'serve' --config-file - "$@"
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
