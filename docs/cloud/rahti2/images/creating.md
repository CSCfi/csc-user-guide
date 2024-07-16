There are several reasons to make your own docker image, but mostly there are two. The application you want to run does not have a docker image available, or there is an image available, but it is not working on OpenShift. Due to the fact that OpenShift is designed to be a shared cluster, where users from different teams will run applications in the same hardware, OpenShift has to add limitations and runs things differently than in a standard Kubernetes cluster.

Rahti 2's registry has an image size limit of 5GB. The bigger is an image, the worse the experience is to work with it. It takes more time to pull, and it fills up the image's cache of the node faster. An image more than 1GB is already considered a very big image. See the article about [keeping docker images small](keeping_docker_images_small.md)

## Building images locally

In this example we are going to use the [official nginx image](https://hub.docker.com/_/nginx) built over the [Alpine Linux](https://www.alpinelinux.org/) distribution, and make the necessary changes to make it work in OpenShift.

Three steps are needed to run build an image locally in a computer.

* First a `Dockerfile` must be written, for example this:

```Dockerfile
FROM nginx:alpine

# support running as arbitrary user which belongs to the root group
RUN chmod g+rwx /var/cache/nginx /var/run /var/log/nginx && \
    chown nginx.root /var/cache/nginx /var/run /var/log/nginx && \
    # users are not allowed to listen on privileged ports
    sed -i.bak 's/listen\(.*\)80;/listen 8081;/' /etc/nginx/conf.d/default.conf && \
    # Make /etc/nginx/html/ available to use
    mkdir -p /etc/nginx/html/ && chmod 777 /etc/nginx/html/ && \
    # comment user directive as master process is run as user in OpenShift anyhow
    sed -i.bak 's/^user/#user/' /etc/nginx/nginx.conf

WORKDIR /usr/share/nginx/html/
EXPOSE 8081

USER nginx:root
```

The `Dockerfile` is:

 1. Giving write permissions to the `root` group (not the `root` user) to several folders that nginx needs to write to (/var/cache/nginx, /var/run, /var/log/nginx, and /etc/nginx/html/). Applications are run using a random user and the `root` group.
 2. Changing the port where nginx listens to, as only root is allowed to listen on privileged ports (<1024).
 3. And finally comment out the `user` configuration directive.

 The original `nginx:alpine` image has 5 layers, and we will adding a new one (`RUN`).

A simpler example of `Dockerfile` could be:

```Dockerfile
FROM alpine

RUN apk add git
```

This is just installing git over `alpine`, and add also a new layer.

See the [Dockerfile](https://docs.docker.com/engine/reference/builder/) reference docs.

Then, the following command must be used to build the image `docker.io/user/name:tag`:

```bash
docker build . -t docker.io/user/name:tag
```

And finally, to publish the image:

```bash
docker push docker.io/user/name:tag
```

## Using Rahti 2 to build container images

The methods below use Rahti 2 to build the images.

### Using a local folder for building

This method allows to build an image using a local folder containing a Dockerfile and the other required project files. It is useful when it is not possible or inconvenient to allow Rahti 2 to clone a repository directly.

This assumes that you have authorized a Rahti 2 command line session and created
a project in Rahti 2. Instructions for that are shown in Chapter [Command line
tool usage](../usage/cli.md#cli-cheat-sheet).

**Steps:**

Create Rahti 2 specific definitions with `oc new-build` command. Be sure
not to be in a directory under git version control:

```bash
$ oc new-build --to=my-hello-image:devel --name=my-hello --binary
    * A Docker build using binary input will be created
      * The resulting image will be pushed to image stream tag "my-hello-image:devel"
      * A binary build was created, use 'start-build --from-dir' to trigger a new build

--> Creating resources with label build=my-hello ...
    imagestream.image.openshift.io "my-hello-image" created
    buildconfig.build.openshift.io "my-hello" created
--> Success
```

Then you need a `Dockerfile`, you can use any of the previous `Dockerfile` in the previous example, or any other one you may have around. In order to tell OpenShift to build the image, just `cd` to the folder where the `Dockerfile` is, and start build with the `oc start-build` command, it will take any file in the current directory and output the build process to local terminal:

```bash
oc start-build my-hello --from-dir=./ -F
```

The image will be visible to internet at
`image-registry.apps.2.rahti.csc.fi/<project-name>/my-hello-image:devel` for docker
compatible clients but you will first need to authenticate in order to pull it. 

For command-line usage with docker compatible clients, the docker repository password will be the access token shown when authorizing Rahti 2 command line session and user name can be `unused`.

```sh
docker login -u g -p $(oc whoami -t) image-registry.apps.2.rahti.csc.fi
```

### Using the Source to Image mechanism

OpenShift allows to build and deploy code without writing a `Dockerfile`. This is called Source to Image or `s2i`. It is used by running `oc new-app URL#branch`, the `#branch` is optional. For example, use the official python sample code:

```bash
$ oc new-app https://github.com/CSCfi/nodejs-16-rahti-example.git
--> Found Docker image 9d200cd (7 weeks old) from Docker Hub for "node:16.15.0"

    * An image stream tag will be created as "node:16.15.0" that will track the source image
    * A Docker build using source code from https://github.com/CSCfi/nodejs-16-rahti-example.git will be created
      * The resulting image will be pushed to image stream tag "nodejs-16-rahti-example:latest"
      * Every time "node:16.15.0" changes a new build will be triggered
    * This image will be deployed in deployment config "nodejs-16-rahti-example"
    * Port 8080/tcp will be load balanced by service "nodejs-16-rahti-example"
      * Other containers can access this service through the hostname "nodejs-16-rahti-example"
    * WARNING: Image "node:16.15.0" runs as the 'root' user which may not be permitted by your cluster administrator

--> Creating resources ...
    imagestream.image.openshift.io "node" created
    imagestream.image.openshift.io "nodejs-16-rahti-example" created
    buildconfig.build.openshift.io "nodejs-16-rahti-example" created
    deploymentconfig.apps.openshift.io "nodejs-16-rahti-example" created
    service "nodejs-16-rahti-example" created
--> Success
    Build scheduled, use 'oc logs -f bc/nodejs-16-rahti-example' to track its progress.
    Application is not exposed. You can expose services to the outside world by executing one or more of the commands below:
     'oc expose svc/nodejs-16-rahti-example' 
    Run 'oc status' to view your app.
```

Then do as suggested and expose the new application to the outside world:

```bash
$ oc expose svc/nodejs-16-rahti-example
route.route.openshift.io/nodejs-16-rahti-example exposed
```

In order to get the new route hostname do:

```bash
oc get route nodejs-16-rahti-example
```

If you enter the hostname in a browser, you will see the "Hello World!" message.

A new build can be triggered in the command line:

```bash
oc start-build nodejs-16-rahti-example
```

Or using [webhooks](../../tutorials/webhooks.md)

### Using the inline Dockerfile method

It is possible to create a new build using a Dockerfile provided in the command line. By doing this, the `Dockerfile` itself will be embedded in the Build object, so there is no need for an external Git repository.

```bash
oc new-build -D $'FROM centos:7'
```

In this example, we will build an image that is a copy of `CentOS 7`.

It is also possible to create a build from a given `Dockerfile`:

```bash
cat Dockerfile | oc new-build -D -
```

### Import from Git (Private Repositories) using the Web GUI

Deploying a private Git repository to Rahti involves setting up the necessary authentication to access your private repository. Without proper authentication, you will see the error "URL is valid but cannot be reached" (seen in the pictures below). Here's how to resolve this using two authentication methods:


![oie_1671443U3OLpFT1](https://github.com/user-attachments/assets/a844e224-769e-4d9f-bba2-043ad5c9b258)


#### Option 1: Using a Token for Git Authentication

1. **Generate a Personal Access Token:**

    - **GitHub:**
         - Go to your GitHub account settings.
         - Navigate to "Developer settings" > "Personal access tokens".
         - Click on "Generate new token".
         - Select the scopes you need (typically, you'll need `repo` scope for private repositories).
         - Generate the token and copy it.

    - **GitLab:**
         - Go to your GitLab profile settings.
         - Navigate to "Access Tokens".
         - Give your token a name, select the required scopes (e.g., `api`, `read_repository`), and create the token.
         - Copy the token.

3. **Add the Token to Rahti:**
    - Under "Source Secret" choose "Create new Secret"
    - Name the secret, under "Authentication type" choose "Basic Authentication"
    - Paste the token and create

![oie_1672121lETtYQ6J](https://github.com/user-attachments/assets/4bd9450f-170b-4a9e-ae8c-df4700fb0be4)


#### Option 2: Using a Private SSH Key for Git Authentication

1. **Generate an SSH Key Pair (if you don't have one already):**

    - Open a terminal and run the following command to generate a new SSH key pair:
         ```sh
         ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
         ```
    - This will create two files: a private key (`id_rsa`) and a public key (`id_rsa.pub`).

2. **Add Your Public Key to Your Git Hosting Service:**

    - **GitHub:**
        - Go to your GitHub account settings.
        - Navigate to "SSH and GPG keys".
        - Click "New SSH key" and paste the contents of your `id_rsa.pub` file.

    - **GitLab:**
        - Go to your GitLab profile settings.
        - Navigate to "SSH Keys".
        - Add a new SSH key and paste the contents of your `id_rsa.pub` file.

4. **Add the Private SSH Key to Rahti:**
    - Under "Source Secret" choose "Create new Secret"
    - Name the secret, under "Authentication type" choose "SSH Key"
    - Paste the contents of your private SSH key (`id_rsa`) and create
    - 
![oie_16720584BbbOspb](https://github.com/user-attachments/assets/b1d47511-0ce6-4980-a732-895193895780)


### Import from Git (Private Repositories) using the CLI

This assumes that the users has generated SSH keys and registered their public key with GitHub.

 
**[Log into OpenShift CLI (`oc`)](../usage/cli.md#how-to-login-with-oc)**:

```bash
oc login <cluster-url>
```

**[Create a New Project](../usage/projects_and_quota.md#creating-a-project)**:

```bash
oc new-project <project-name> --display-name=<display-name> --description="csc_project:<project-id>"
```

**Create SSH Key Secret**:

```bash
oc create secret generic <secret-name> --from-file=ssh-privatekey=<path-to-private-key> --type=kubernetes.io/ssh-auth
```

**Link the Secret to the Builder Service Account**:

```bash
oc secrets link builder <secret-name>
```


**Deploy the Application**:

```bash
oc new-app <repository-url> --name=<application-name>
```

**Monitor the Build**:

- monitor logs
  ```bash
  oc logs -f buildconfig.build.openshift.io/<application-name>
  ```
        
- The initial build will probably fail due to authentication issues, set the build secret explicitly:
  ```bash
  oc set build-secret --source bc/<application-name> <secret-name>
  ```
        
- Trigger a new build:
  ```bash
  oc start-build <application-name> --follow
  ```

**Expose the Application**:

```bash
oc expose deployment <application-name> --name=<service-name> --port=<port> --target-port=<target-port>
oc expose svc/<service-name>
```
    
**Access the Application**:

- Use the URL provided by:
    ```bash
    oc get route <application-name>
    ```

## Troubleshooting

If your build fails in Rahti 2, it could mean that your application needs more memory than is provided by default. Unfortunately, it's not possible to set resource limits and requests directly from the CLI when deploying the app. You will need to use a YAML configuration file or the web UI to specify these settings.

You can create a yaml file and then apply it with the command `oc apply -f {your_yaml_file}.yaml` or edit your current `BuildConfig` in the Rahti 2 webUI.  
In the Administrator view, navigate to `Builds > BuildConfigs` and click on your BuildConfig. Select the `YAML` tab.  

Under `spec` you should see `resources: {}`. From here, add `limits.cpu`, `limits.memory`, `requests.cpu` and `requests.memory`:
```yaml
resources:
  limits:
    cpu: 400m
    memory: 8Gi
  requests:
    cpu: 50m
    memory: 1600Mi
```

Note that they cannot be more than 5x apart (default ratio, more information [here](../../usage/projects_and_quota/#default-pod-resource-limits)).

Save and run the build again, and if it succeeds, check the metrics and see how much memory was used. You can adjust the memory limit to 10-20% more than what it was used.
