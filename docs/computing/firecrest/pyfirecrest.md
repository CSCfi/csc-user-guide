# PyFirecREST

PyFirecREST is a Python SDK library for interacting with FirecREST API, and the HPC resources available via the API.

The package is available in [PyPI](https://pypi.org/project/pyfirecrest/). It can be installed with a simple `pip` call:

```
python3 -m pip install pyfirecrest
```

Please see the [PyFirecREST documentation from CSCS](https://pyfirecrest.readthedocs.io/en/stable/index.html) for tutorials and API reference. FirecREST HPC API on Roihu only supports [PyFirecREST API v2](https://pyfirecrest.readthedocs.io/en/stable/reference_v2_index.html).


## Using with personal access tokens

The PyFirecREST library ships with one built-in authorization class, `ClientCredentialsAuth`, which is suitable for use with robot accounts. 

In order to use the library with personal access token, a separate Authorization object needs to be created for the `firecrest.v2.Firecrest` client. In this example, we create a "pass-through" authorization class which reads the token from environment variable `FIRECREST_TOKEN`, makes sure it has not expired, and then hands it over to the `firecrest.v2.Firecrest` client as-is:

```python
import os
import time
import jwt

class TokenAuth:
  def __init__(self):
    pass

  # Use PyJWT to decode the token and verify expiration time.
  # Return False if decoding fails (input is not valid JWT) or if the token has expired
  def _is_token_valid(self, token: str) -> bool:
    try:
      payload = jwt.decode(token, options={"verify_signature": False, "verify_exp": False, "verify_aud": False})
      return time.time() <= payload["exp"]
    except Exception:
      return False

  # A PyFirecREST Authorization object is required to have method get_access_token(),
  # which, when called, will return a valid JWT access token.
  def get_access_token(self):
    token = os.getenv('FIRECREST_TOKEN', None)
    if not token:
      raise RuntimeError("Environment variable FIRECREST_TOKEN is not defined.")
    if not self._is_token_valid(token):
      raise RuntimeError("Token is invalid or has expired.")
    return token

import firecrest as fc
firecrest = fc.v2.Firecrest(firecrest_url="https://api.roihu.csc.fi/v1", authorization=TokenAuth())

# Example: Call the userinfo endpoint on Roihu CPU subsystem to verify FirecREST API connection
try:
    userinfo = firecrest.userinfo(system_name="cpu")
    print(f"Userinfo endpoint returned:\n{userinfo}")
except fc.FirecrestException as e:
    print(f"FirecREST error: {e}")
except Exception as e:
    print(f"System error: {e}")

```

## Using with Robot accounts

You can use the built-in `ClientCredentialsAuth` class with a robot account, with configuration as described on [connecting to Roihu FirecREST API](connecting.md#connecting-with-a-robot-account), for example:

```
import firecrest as fc
authorization = fc.ClientCredentialsAuth(
  client_id="my_robot_username",
  client_secret="my_robot_password",
  token_uri="https://user-auth.csc.fi/idp/profile/oidc/token"
)
firecrest = fc.v2.Firecrest(firecrest_url="https://api.roihu.csc.fi/v1", authorization=authorization)
```

Please refer to the [PyFirecREST Authorization reference](https://pyfirecrest.readthedocs.io/en/stable/reference_auth.html) for all configuration options for the built-in `ClientCredentialsAuth` class.


## FirecREST CLI

PyFirecREST also ships with a handy command line utility `firecrest` for interacting with FirecREST APIs. It implements support for OIDC client credentials based authentication, which can be used with robot accounts, as well as support for getting or setting an access token with an arbitrary shell command starting from version `v3.8.0`.

### Using CLI with personal acces token

We can use the `--token-command` (env `FIRECREST_TOKEN_COMMAND`) option of `firecrest` CLI to supply the personal access token to the utility:

```
# Copied and pasted access token from MyCSC
access_token="<JWT>"

# Set up URL and token command using environment variables.
export FIRECREST_URL=https://api.roihu.csc.fi/v1
export FIRECREST_TOKEN_COMMAND="echo ${access_token}"

# Example: query the userinfo endpoint on Roihu-CPU
firecrest id -s cpu
```
