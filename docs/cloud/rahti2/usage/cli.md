# Command line tool usage

Rahti 2 can be used via the command line either with OpenShift's _oc_ tool
or with the _kubectl_ tool from Kubernetes. Certain features specific to OpenShift
are only available when using the oc tool.

## How to install the `oc` tool

The oc tool is a single binary that only needs to be included in your _path_. You may download it from the [Getting started with the OpenShift CLI](https://docs.openshift.com/container-platform/4.15/cli_reference/openshift_cli/getting-started-cli.html) page in OpenShift's documentation. Follow the detailed instructions in the link.

In order to test that it was properly installed, open a new terminal, go to any folder, and run:

```
$ oc --help
```

It should show the list of all available commands.

## The "Command Line Tools" page in the OpenShift web UI

Instructions for downloading the oc tool including the download link for several platforms and operating systems can be found in the "Command Line Tools" page in the web interface:

![Command line tools](../../img/cli_help_menu_4.png)

after clicking you will be welcomed with:

![OpenShift Command Line Tools page](../../img/openshift_cli_dialog_4.png)

## How to login with `oc`?

The oc login command to login can be found in the dropdown menu next to your name. There is a
button next to it for copying the command to the clipboard. Copy the command and paste it in a terminal to start using OpenShift via the
command line. The command looks like:

```bash
oc login https://api.2.rahti.csc.fi:6443 --token=<secret access token>
```

This command can be obtained by clicking your username and "Copy Login Command"
in the web console:

![copy login](../../img/CopyLoginCommand.png)

!!! info "sudo"

    If you open multiple terminals, the login session for oc will be active in
    all of them.

!!! info "Helm login"
    If you are using Helm and you are not logged in, you might get an error like:
    ```sh
    $ helm ls       
    Error: Kubernetes cluster unreachable: Get "http://localhost:8080/version": dial tcp 127.0.0.1:8080: connect: connection refused
    ```

## How to login in the registry?

In order to use Rahti 2 internal container registry, it is necessary to login separately. Once you login, it is possible to use the client docker to `pull` and `push` from Rahti 2's registry.

### Using personal account

After login with `oc`, it is possible to use the command to generate a token (`oc whoami -t`):

`docker login -p $(oc whoami -t ) -u unused image-registry.apps.2.rahti.csc.fi`

!!! info "sudo use"
    Some docker client setups require to run the `docker` client as root using `sudo`. In this case the `oc login` command needs to also be run using `sudo`. This is because the login information is stored in the user's home directory, only the user that runs `oc login` is logged in to Rahti.

    As a general recommendation, it is better to use other "rootless" runtimes like podman, when possible. It is also possible to configure Docker as non-root user. In order to do so, in most Linux distributions, you just need to type this command:  
    
    ```sh
    sudo usermod -aG docker $USER
    ```

    And then log out and log back to have the group membership re-evaluated.

### Using a service account token

Rahti 2 also offers the opportunity of using an internal service account to interact with the registry. This is recommended for automated procedures like a CI pipeline. Even though by default 3 internal service accounts are created in every Rahti 2 namespace: builder, default and deployer, it is recommended to create a dedicated internal service account and assign to it the `system:image-pusher` role.

```sh
oc create serviceaccount pusher
oc policy add-role-to-user system:image-pusher pusher
docker login -p $(oc sa get-token pusher) -u unused image-registry.apps.2.rahti.csc.fi
```

This service account token, the one you get with `oc sa get-token pusher` does not expire.

## CLI cheat sheet

**Basic usage:**

```bash
oc <command> <--flags>
oc help <command>
```

**Examples:**

Show projects:

```bash
oc projects
```

Switch to project `my-project`:

```bash
oc project my-project
```

Show all pods in the current namespace:

```bash
oc get pods
```

Show all pods in the namespace `<my-other-name-space>`:

```bash
oc get pods -n <my-other-namespace>
```

Show all pods that have the key-value pair `app: myapp` in `metadata.labels`:

```bash
oc get pods --selector app=myapp
```

Print the specifications of the pod `mypod`

```bash
oc get pod mypod -o yaml
```

### Other useful commands

* `oc create` creates an object. Example: `oc create -f file.yaml`
* `oc replace` replaces an object. Example: `oc replace -f file.yaml`
* `oc delete` deletes an object in OpenShift. Example: `oc delete rc
  myreplicationcontroller`
* `oc apply` modifies an object according to the input. Example `oc apply -f
  file.yaml`
* `oc explain` prints out the API documentation. Example: `oc explain deploy.spec`
* `oc edit` loads an object from the API to the local editor chosen by the `$EDITOR`
  environment variable. Example: `oc edit Deployment mydeploy`

## Abbreviations

Object types have abbreviations that are recognized in the CLI:

|Abbreviation |Meaning|
|-----:|:-------|
|`is`|`ImageStream`|
|`dc`|`DeploymentConfig`\*|
|`svc`|`Service`|
|`bc`|`BuildConfig`|
|`rc`|`ReplicationController`|
|`pvc`|`PersistentVolumeClaim`|

\* Deployment Config is deprecated

## Further documentation

See the official documentation for more information about using the command line
interface:

* [OpenShift documentation: CLI reference](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.10/html-single/cli_tools/index)
