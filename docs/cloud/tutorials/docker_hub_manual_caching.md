# How to manually cache images in Rahti 2

It is possible to manually cache images in Rahti 2. This could be useful to remove
an external dependency or improve performance.

The process is simple:

1. [Install](../../rahti2/usage/cli/#how-to-install-the-oc-tool) and [login with OC](../../rahti2/usage/cli/#how-to-login-with-oc).

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
![Image Streams](../img/image_streams_rahti4.png)

## Use the image

Go to your project's deployment or DeploymentConfig, and edit it.

![Edit deployment](../img/edit_deployment.png)

Go to the Images section, make sure the option "Deploy images from an image stream tag" is clicked.
Finally select the new image.

![Use cached image](../img/use_cached_image.png)
