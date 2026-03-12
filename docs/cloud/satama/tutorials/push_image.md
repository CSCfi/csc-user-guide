# Push Your First Image

This tutorial walks through the process of building a container image and storing it in Satama.

## Step 1: Build a Container Image

First build your container image locally.
```
docker build -t <image_name>:<version>
```
And verify that the image exists locally

```
docker image ls
```
Here you should see your image
## Step 2: Tag the Image

Before pushing the image to Satama, it must be tagged with the registry path.

For a detailed explanation of tagging images, see [Tag image](../cli.md#tagging-an-image)


## Step 3: Authenticate to Satama

Log in to Satama by personal [CLI token](../cli.md#logging-in-to-satama-using-personal-cli-secret) or by [Robot account](../cli.md#logging-in-to-satama-using-robot-account). 

## Step 4: Push the Image
Push the tagged image to the registry.
```
docker push satama.csc.fi/<project>/<image_name>:<version>
```
For more detail about [pushing image](../cli.md#pushing-an-image)
## Step 5: Verify the Image

After pushing the image, open the Satama Web UI and verify that the repository and tag appear in your project.

You can learn more about navigating the [Web interface](../ui.md#project-level-navigation-top-tabs-inside-a-project) 