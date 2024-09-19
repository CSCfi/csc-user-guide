# Using Rahti 2 integrated registry

## Manual Image Caching 

It is possible to manually cache images in Rahti 2. This could be useful to remove
an external dependency or improve performance.

The process is simple:

1. [Install](../../usage/cli/#how-to-install-the-oc-tool) and [login with OC](../../usage/cli/#how-to-login-with-oc).

1. With a terminal, connect to the Rahti 2 registry:
    ```sh
    docker login -p $(oc whoami -t ) -u unused image-registry.apps.2.rahti.csc.fi
    ```

    !!! info
        If you get any error, make sure you are logged in. If you run `oc whoami`, the command should return your username.

2. Tag the image you want to push:
   ```sh
   docker tag centos:7 image-registry.apps.2.rahti.csc.fi/{YOUR_PROJECT_NAME}/centos:<tag>
   ```
   _Replace {YOUR_PROJECT_NAME} by the name of your project._

3. Push your image:
   ```sh
   docker push image-registry.apps.2.rahti.csc.fi/{YOUR_PROJECT_NAME}/centos:<tag>
   ```

You should be able to see your images in your project:
![Image Streams](../../img/image_streams_rahti4.png)

## Using Manually Cached Images 

Go to your project's deployment, and edit it.

![Edit deployment](../../img/edit_deployment.png)

Go to the Images section, make sure the option "Deploy images from an image stream tag" is clicked.
Finally select the new image.

![Use cached image](../../img/use_cached_image.png)

## Access Control for the Rahti 2 Integrated Registry

Rahti 2 allows fine-grained control over access to the integrated image registry, enabling management of access based on [user authentication](https://docs.openshift.com/container-platform/4.15/authentication/understanding-authentication.html).

### 1. **Anonymous Access** (`system:anonymous`)

This refers to users who access the registry without providing any authentication credentials. In this scenario, they have no identity attached to their requests.

- **How to enable**: Use the following command to allow anonymous users to pull images from your project's registry:
  ```bash
  oc policy add-role-to-user registry-viewer system:anonymous -n <project>
  ```
- **Use case**: Suitable for cases where you want to make images publicly accessible, allowing anyone to view or pull images without logging in.

### 2. **Unauthenticated Access** (`system:unauthenticated`)

This group includes all users who are accessing the system without valid authentication credentials, including anonymous users but potentially also used automated systems, scripts or external services  that do not need to be authenticate.

- **How to enable**: Grant unauthenticated users access with the command:
  ```bash
  oc policy add-role-to-user registry-viewer system:unauthenticated -n <project>
  ```
- **Use case**: This is broader than `system:anonymous` and is useful for systems or services to access your registry without authentication.

### 3. **Authenticated Access** (`system:authenticated`)

Authenticated users are those who have successfully logged in using valid credentials (e.g., OAuth tokens).

- **How to enable**: To allow all authenticated users to access the registry:
  ```bash
  oc policy add-role-to-user registry-viewer system:authenticated -n <project>
  ```
- **Use case**: This allows any user with valid credentials to view or pull images, useful for restricting access.

## Guide on Pulling Images from Rahti 1 Registry

To securely pull images from Rahti 1 registry to Rahti 2, follow this [guide](../../../support/faq/pull-from-rahtiv1-registry.md). It also explains how to convert images using `Skopeo` for compatibility with future releases.