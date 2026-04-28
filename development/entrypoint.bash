#! /usr/bin/env bash

set -e

declare -gr properdocs_BIN='/usr/local/bin/properdocs' \
            properdocs_IP='0.0.0.0' \
            properdocs_PORT='8000'

properdocs_serve() {
  $properdocs_BIN 'serve' --dev-addr=${properdocs_IP}:${properdocs_PORT} "$@"
}

case $1 in
  '')
    $properdocs_BIN
  ;;
  serve)
    shift 1
    properdocs_serve "$@"
  ;;
  *)
    $properdocs_BIN "$@"
  ;;
esac
