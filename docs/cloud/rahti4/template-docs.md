
# Rahti Templates

Rahti supports templating service deployment code allowing its re-use. The
templates documented here are available to be launched on the Rahti Service
Catalog.

The Service Catalog also lists default templates bundled with OKD which are not
documented here.

## How to launch a template using the CLI

First, list the templates available:

```bash
oc get -n openshift templates
```

Then, describe the template, so we know the list of parameters:

```bash
oc describe -n openshift template httpd-example
```

Finally launch the template, for each required parameter a value must be set:

```bash
oc new-app --template=httpd-example \
  -p SOURCE_REPOSITORY_URL=https://github.com/sclorg/httpd-ex.git
```

## Templates

<style>
.admonition-title { background-color: rgba(255, 0, 0, 0.15) !important; }
.admonition { background-color: white !important; }
</style>
!!! Attention "⚠️ Not all Rahti3 templates have been ported to Rahti4"

    The process of adapting and testing the templates to Rahti4 is labor intensive and not in the top of our task list. If you have any special interest on the functionality provided by a Rahti3 template that is missing in Rahti4, please let us know (servicedesk@csc.fi).
