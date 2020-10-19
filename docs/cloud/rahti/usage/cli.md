# Command line tool usage

Rahti can be used via the command line either with OpenShift's _oc_ tool
or with the _kubectl_ tool from Kubernetes. Certain features specific to OpenShift
are only available when using the oc tool.

## How to install the `oc` tool

The oc tool is a single binary that only needs to be included in your _path_. You may download it from the [latest release](https://github.com/openshift/origin/releases/latest) page in GitHub. The detailed instructions are:

* Go to the aforementioned release page (<https://github.com/openshift/origin/releases/latest>). In the bottom you will see the list of clients. Download the "Openshift origin client" corresponding to your OS (Windows, Mac or Linux).
* Once downloaded, extract the `oc` binary file.
* Copy the file to a folder in your `$PATH` and make it executable. For Mac and Linux the steps are similar to the following:

```
$ echo $PATH
/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:~/bin
$ mkdir -p ~/bin
$ cp oc ~/bin/
$ chmod +x ~/bin/oc
```

In the example above, we are displaying the contents of the `$PATH` variable, choosing the bin folder in the home (~) folder, using `mkdir` just to be sure that the folder exist, copy the oc command (of course, we have to be in the folder `oc` was downloaded), and finally adding executable (`+x`) permissions to the `oc` binary. That is all.

In order to test that it was properly installed, open a new terminal, go to any folder, and run:

```
$ oc --help
```

It should show the list of all available commands.

## The "Command Line Tools" page in the OpenShift web UI

Instructions for downloading the oc tool and logging in via the command line
can be found in the "Command Line Tools" page in the web interface:

![Command line tools](img/cli_help_menu_3.7.png)

The oc tool is a single binary that only needs to be included in your _path_.
The oc login command to login can be found in one of the fields on the page. There is a
button next to it for copying the command to the clipboard:

![OpenShift Command Line Tools page](img/openshift_cli_dialog_3.7.png)

Copy the command and paste it in a terminal to start using OpenShift via the
command line.

!!! note
    If you open multiple terminals, the login session for oc will be active in
    all of them.

## CLI cheat sheet

**Basic usage:**

```bash
oc <command> <--flags>
oc help <command>
```

**Examples:**

Authorize the CLI tool to the cluster:

```bash
oc login https://rahti.csc.fi:8443 --token=<secret access token>
```

This command can be obtained by clicking your usename and "Copy Login Command"
in the web console:

![copy login](../tutorials/img/copy-login.png)

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
* `oc explain` prints out the API documentation. Example: `oc explain dc.spec`
* `oc edit` loads an object from the API to the local editor chosen by the `$EDITOR`
  environment variable. Example: `oc edit DeploymentConfig mydc`

## Abbreviations

Object types have abbreviations that are recognized in the CLI:

|Abbreviation |Meaning|
|-----:|:-------|
|`is`|`ImageStream`|
|`dc`|`DeploymentConfig`|
|`svc`|`Service`|
|`bc`|`BuildConfig`|
|`rc`|`ReplicationController`|
|`pvc`|`PersistentVolumeClaim`|

## Further documentation

See the official documentation for more information about using the command line
interface:

* [OpenShift documentation: CLI reference](https://docs.okd.io/3.11/cli_reference/index.html)
