# Rahti command line usage

Rahti can be used via the command line either with OpenShift's oc tool
or with the kubectl tool from Kubernetes. Certain features specific to OpenShift
are only available when using the oc tool.

## The "Command Line Tools" page in the OpenShift web UI

The information for downloading the oc tool and logging in from the command line
can be found in the "Command Line Tools" page in the web interface. After
logging in to the web interface, you can find the page here:

![Command line tools](../images/rahti-command-line-usage-fig1.png)

The oc tool is a single binary that just needs to be placed in your path. You
can find the oc command to login in one the fields on the page. There is a
button next to it to copy the command to the clipboard:

![OpenShift Command Line Tools page](../images/rahti-command-line-usage-fig2.png)

Copy the command and paste it into a terminal to start using OpenShift via the
command line.

!!! note
    If you open multiple terminals, the login session for oc will be active in
    all of them.

## Basic commands

Get information:

```bash
# List existing API objects
oc get pods|deployments|services|...
# Get more detailed information about an API object
oc describe pod|deployment|service|... myapiobject
# Get the YAML representation of an API object
oc get pod|deployment|service|... myapiobject -o yaml
```

Create or update:

```bash
# Create an API object from a file
oc create -f somefile.yaml
# Edit an existing API object
oc edit deployment|service|... myapiobject
# Replace API object with an updated one
oc replace -f somefile.yaml
```

## More documentation

See the official documentation for more information on using the command line
interface:

   * [OpenShift documentation: CLI reference](https://docs.okd.io/latest/cli_reference/index.html)
