# Pushing an image to an External repository

It is possible to build an image in Rahti and push it to a private external repository. The steps to make it so are:

1. Login into Rahti and, if needed, create a [new Rahti project](../usage/projects_and_quota.md#creating-a-project).

2. Create a secret of type `docker-registry`. And link with the Service account that will run the build:

    ```sh
    oc create secret --docker-server=<url> docker-registry <url> \
                     --docker-username=<user> --docker-password=<token>
    oc secrets link builder <url>
    ```

    - **url** is the url of the registry. In case of docker hub the value should be `docker.io`, and for GitHub Packages it will be `ghcr.io`.
    - **user** is the username needed to login in the registry.
    - **password** is the password or token. It is recommended to avoid using a password and better use very narrow purpose TOKEN that ideally only allow to push images and nothing else.  

3. Create the build:

    ```sh
    oc new-build --binary --to-docker=true \
                 --to=<image-url>:<tag> \
                 --name tutorial
    ```

    * **image-url:tag** is the url of the image that you are building. It is the same URL that you will later use to pull the image using `docker pull`.
    * The **name** can be anything that helps you remember what is this build for.

4. Set the build secret for `push`:

    ```sh
    oc set build-secret --push bc/tutorial <url>
    ```

    * <url> is the same as in step 2.

    !!! Info "Pull private image"
        If you are building from a private image you can run the same command again replacing `--push` by `--pull`

5. Test it. You can test the build by running the `oc start-build` command. The directory (`.` in the example below), must have a `Dockerfile`. You can also use the other methods described in the [Creating images](./creating.md#using-the-inline-dockerfile-method) article.

    ```sh
    oc start-build tutorial --from-dir=.
    ```
