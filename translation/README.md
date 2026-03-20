# LLM translation

## Build

### Containerfile

```text
Containerfile.alternate
```


### Args

```text
restic_image=ghcr.io/restic/restic
translator_image=<the translator image>
builder_image=<the builder image>
nginx_image=ubi8/nginx-124
repo_org=CSCfi
repo_name=csc-user-guide
repo_branch=master
```


## Environment

```text
LANG_CODE=<language code, e.g. fi for Finnish>
RESTIC_REPOSITORY=swift:docs-restic:/translations
RESTIC_HOST=docs.csc.fi
RESTIC_PASSWORD=<secret>
OS_AUTH_URL=https://pouta.csc.fi:5001/v3
OS_APPLICATION_CREDENTIAL_ID=<secret>
OS_APPLICATION_CREDENTIAL_SECRET=<secret>
OPENAI_API_KEY=<secret>
CACHE_CONTAINER=<such that no collision with RESTIC_REPOSITORY occurs>
CACHE_PREFIX=<such that no collision with RESTIC_REPOSITORY occurs>
SITE_URL=<e.g. https://docs.csc.fi/fi for Finnish>
MKDOCS_ENV=<production, defaults to preview>
```
