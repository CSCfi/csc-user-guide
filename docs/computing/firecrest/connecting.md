# Connecting to Roihu FirecREST HPC API

!!! warning "Access tokens are secrets"
    Access tokens issued for FirecREST HPC API allow the token holder to interact with Slurm jobs, and read, manipulate and transfer data with your privileges. Don't share your access token with anyone.

Roihu FirecREST HPC API endpoints can be found under the URL [https://api.roihu.csc.fi](https://api.roihu.csc.fi). The service uses versioned URL scheme, where the first element of the URL path represents the API generation. The current, latest API generation is `v1`. It is based on the latest release of FirecREST v2.

Possible major or breaking changes to the API will be released as new API generation. By default, a new release will not replace any existing APIs. Earlier generations will be maintained and kept available.

## Subsystems

FirecREST HPC API supports multiple subsystems with different configuration options, identified by subsystem identifier in API endpoint URLs (e.g. `/v1/compute/<subsystem>/jobs`).

API and subsystem configuration on `api.roihu.csc.fi`:

| API generation | API subsystem | Partitions | Data transfer |
|----------------|---------------|-----------|---------------|
| `v1` | `cpu` | All *CPU* partitions | S3 via Allas, pre-signed URLs |
| `v1` | `gpu` | All *GPU* partitions | S3 via Allas, pre-signed URLs |

## API documentation

Up-to-date API specification for `v1` is available in OpenAPI format at [https://api.roihu.csc.fi/v1/openapi.json](https://api.roihu.csc.fi/v1/openapi.json) and it can be viewed through FirecREST's Swagger UI at [https://api.roihu.csc.fi/v1/docs/](https://api.roihu.csc.fi/v1/docs).

## Connecting to the API

FirecREST HPC API uses JWT bearer tokens as authorization method. Accepted tokens are issued by CSC authentication and authorization infrastructure (AAI) identity provider (IdP). Only those tokens that have been specifically issued to be used with FirecREST HPC API (indicated by `aud` member in the JWT) are accepted by the API.

In order to connect to an API endpoint, tokens are sent to FirecREST using standard `Authorization` header, example:

```
access_token="<JWT>"
curl -X GET https://api.roihu.csc.fi/v1/compute/cpu/jobs \
  -H "Authorization: Bearer ${access_token}"
```

Authorization header must be present in every API request sent to FirecREST. Token validity is verified on server-side for each request. An attempt to use invalid access token will result in a `HTTP 401 Unauthorized` return code, with a specific error message recorded in a JSON document in the response body.

All requests sent to the API are executed on Roihu using the same user account that was used to retrieve the access token. For example, with a personal access token, all commands run via FirecREST are executed as you on the target system.

## Connecting with a personal access token

FirecREST HPC API can be used with personal access tokens, which allow access to same computing resources and projects as your direct terminal access. Personal access tokens are useful for running desktop applications or automation utilities in interactive terminals, that integrate with HPC resources using [PyFirecREST](pyfirecrest.md) Python SDK, for example.

As the name suggests, personal access tokens are intended for personal use. A [project-specific robot account](../../accounts/how-to-create-new-user-account.md#getting-a-machine-to-machine-robot-account) should be used for implementing machine-to-machine HPC API integration for headless non-interactive systems.

A personal access token can be retrieved from the [MyCSC portal](https://my.csc.fi/firecrest-token). Note that there's no direct link from the portal itself yet. Personal access tokens are valid for 24 hours at a time.

You can view and revoke your active tokens at [CSC IdP federated personal profile page](https://user-auth.csc.fi/idp/profile/userprofile), under *Connected organizations* -> *Firecrest-access-tokens*.

## Connecting with a robot account

!!! Note 
    Robot accounts are not yet supported, support coming in Q3 2026.

[Machine-to-machine robot accounts](../../accounts/how-to-create-new-user-account.md#getting-a-machine-to-machine-robot-account) can access computing resources on Roihu using FirecREST HPC API.

Similarly to personal access tokens, connecting to the API using a robot account also requires supplying a JWT bearer token as authorization credential. Robot accounts can request a suitable JWT from the token endpoint on CSC IdP using standard [OAuth 2.0 Client Credentials Grant](https://oauth.net/2/grant-types/client-credentials/).

Settings typically required for client credentials configuration:

| Setting | Value |
|---------|-------|
| Client ID | Username of your robot account |
| Client Secret | Password of your robot account |
| Token URL | `https://user-auth.csc.fi/idp/profile/oidc/token` |
| Scope | `openid` |

You can, for example, retrieve an access token for a robot account with a simple `curl` call:

```
curl -X POST https://user-auth.csc.fi/idp/profile/oidc/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Accept: application/json" \
  -d "client_id=${my_robot_username}&client_secret=${my_robot_password}&scope=openid&grant_type=client_credentials"
```

A successful call returns a JSON document with the access token and associated metadata (token type, scope and lifetime).
