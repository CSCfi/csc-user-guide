# Known Issues

The most common issues encountered while using Satama are related to authentication and user permissions. The following examples describe typical errors and how to resolve them.

### Authentication Required

If you encounter the error:
```
unauthorized: authentication required
```
This usually means that the Docker or CLI client is not authenticated with the Satama registry. 

Possible solutions:

* Ensure you are logged in using the correct credentials.
* Run the login command again:

```
docker login satam.csc.fi
```
* Verify that your CLI secret or authentication token has not expired.

### Insufficient Permissions

If the following error appears while pushing an image:
```
denied: requested access to the resource is denied
```
This means your account does not have permission to push images to the specified project.

Possible causes include:

* You are not a member of the project.
* Your role does not allow pushing images.

Contact the project administrator to request the necessary permissions.

### Expired Session Token

During image push or pull operations, you may see errors such as:
```
unauthorized
```
This may occur when your session token has expired. To resolve this issue:

1. Log out from the Satama Web UI.
2. Log in again to refresh your session.
3. Generate or copy the updated CLI credentials.
4. Authenticate again using the Docker/Podman CLI.

### Image Push Fails Due to Tag Immutability

If tag immutability is enabled, attempting to overwrite an existing tag may result in an error. This happens when a repository policy prevents tags from being modified after creation.

Possible solution is to use a new tag for the image.

### Docker Login Fails

If the login command fails:
```
docker login satama.csc.fi
```
Possible causes include:

* Incorrect username or password
* Expired credentials
* Incorrect registry URL
* Network connectivity issues

Verify the registry URL and ensure that your account has valid credentials.

### Repository Not Found

When pulling an image, you may encounter:
```
repository does not exist
```
This usually means:

* The repository name is incorrect.
* The project name is incorrect.
* The image tag does not exist.

Verify the image reference in the Satama Web UI before pulling the image.