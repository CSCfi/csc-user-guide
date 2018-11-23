#!/bin/sh

set -e
: ${SYSTEM_NAME?"Must set SYSTEM_NAME"}
: ${OSO_WEB_UI_URL?"Must set OSO_WEB_UI_URL"}
: ${OSO_REGISTRY_URL?"Must set OSO_REGISTRY_URL"}

yasha -o mkdocs.yml mkdocs.yml.j2
