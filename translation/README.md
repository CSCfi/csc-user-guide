# LLM translation

## Build

### Containerfile

```text
Containerfile.alternate
```


### Args

```text
builder_image=<the builder image>
```


## Environment

```text
LANG_CODE=<language code, e.g. fi for Finnish>
OPENAI_API_KEY=<secret>
OS_AUTH_URL=https://pouta.csc.fi:5001/v3
OS_APPLICATION_CREDENTIAL_ID=<secret>
OS_APPLICATION_CREDENTIAL_SECRET=<secret>
RESTIC_REPOSITORY=swift:docs-restic:/translations
RESTIC_HOST=docs.csc.fi
RESTIC_PASSWORD=<secret>
```
