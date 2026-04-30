# Connecting to Roihu FirecREST API

!!! warning "Access tokens are secrets"
    Access tokens issued for FirecREST API allow the token holder to interact with Slurm jobs, and read, manipulate and transfer data with your privileges. Don't share your access token with anyone.

Roihu FirecREST HPC API endpoints can be found under the URL [https://api.roihu.csc.fi](https://api.roihu.csc.fi). The service uses versioned URL scheme, where the first element of the URL path identifies the API revision. The current, latest API revision is `v1`, which is based on the latest release of FirecREST v2. Possible major or breaking changes to the API in the future will be published as new revisions.

## Subsystems

FirecREST HPC API supports multiple subsystems with different configuration options, identified by subsystem identifier in API endpoint URLs (e.g. `/v1/compute/<subsystem>/jobs`).

API and subsystem configuration on `api.roihu.csc.fi`:

| API revision | API subsystem | Partitions | Data transfer |
|----------------|---------------|-----------|---------------|
| `v1` | `cpu` | All *CPU* partitions | S3 via Allas, pre-signed URLs |
| `v1` | `gpu` | All *GPU* partitions | S3 via Allas, pre-signed URLs |

## API documentation

Up-to-date API specification for `v1` is available in OpenAPI format at [https://api.roihu.csc.fi/v1/openapi.json](https://api.roihu.csc.fi/v1/openapi.json) and it can be viewed through FirecREST's Swagger UI at [https://api.roihu.csc.fi/v1/docs/](https://api.roihu.csc.fi/v1/docs).

## Connecting with a personal access token

FirecREST HPC API can be used with personal access tokens, which are useful for running desktop applications or automation in interactive terminals, that integrate with HPC resources, using [PyFirecREST](pyfirecrest.md) Python SDK, for example. 

As the name suggests, personal access tokens are intended for personal use. A [project-specific robot account](../../accounts/how-to-create-new-user-account.md#getting-a-machine-to-machine-robot-account) should be used for implementing non-interactive machine-to-machine API integrations, such as CI pipelines.

A personal access token can be retrieved from `TODO: MyCSC token interface link`. These tokens are valid for 24 hours at a time.

You can view and revoke your active tokens at [CSC IdP federated personal profile page](https://user-auth.csc.fi/idp/profile/userprofile), under *Connected organizations* -> *Firecrest-access-tokens*.

Personal access tokens are sent to FirecREST API endpoints using standard `Authorization: Bearer` header:

```
my_token="<PAT JWT>"
curl -X GET https://api.roihu.csc.fi/v1/compute/cpu/jobs \
  -H "Authorization: Bearer ${my_token}"
```

All requests made via FirecREST API are executed under your personal account and privileges on Roihu.

## Connecting with a robot account

[Machine-to-machine robot accounts](../../accounts/how-to-create-new-user-account.md#getting-a-machine-to-machine-robot-account) can access computing resources on Roihu using FirecREST HPC API.

Similarly to personal access tokens, connecting to the API using a robot account also requires supplying a JWT bearer token as authorization credential. Robot accounts can request a suitable JWT from the token endpoint on CSC IdP using standard [OAuth 2.0 Client Credentials Grant](https://oauth.net/2/grant-types/client-credentials/).

Settings typically required for client credentials configuration:

| Setting | Value |
|---------|-------|
| Client ID | Username of your robot account |
| Client Secret | Password of your robot account |
| Token URL | https://user-auth.csc.fi/idp/profile/oidc/token |

You can, for example, retrieve an access token for a robot account with a simple `curl` call:

```
curl -X POST https://user-auth.csc.fi/idp/profile/oidc/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=${my_robot_username},client_secret=${my_robot_password},grant_type=client_credentials"
```

The [IdP token endpoint](https://user-auth.csc.fi/idp/profile/oidc/token) also supports `client_secret_basic` and `client_secret_jwt` methods, which can be used instead of the `client_secret_post` method demonstrated above.
