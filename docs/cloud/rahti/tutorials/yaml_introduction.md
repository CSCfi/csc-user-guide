<style>
.admonition-title { background-color: rgba(255, 145, 0, 0.1) !important; }
.admonition { background-color: white !important; }
</style>
!!! Attention "⚠️ Rahti 3 is deprecated"

    This page is about a deprecated version of Rahti, please consult the [updated documentation article](../../../rahti4/tutorials/yaml_introduction/)

# Short introduction to YAML

YAML is used to describe key-value maps and arrays. YAML files are recognized
by the `.yml` or `.yaml` file suffix.

A YAML dataset can be

* a value

```yaml
value
```

* an array

```yaml
- value 1
- value 2
- value 3
```

or

```yaml
[value 1, value 2, value 3]
```

* a dictionary

```yaml
key: value
another_key: another value
```

  or

```yaml
key:
  value
another_key:
  another value
```

* YAML dataset

```yaml
key:
  - value 1
  - another key:
      yet another key: value 2
    another key 2:
      - more values
    this keys value is also an array:
    - but indentation is not necessary here
```

Values can be input across multiple lines using `>`:

```yaml
key: >
  Here's a value that is written over multiple lines
  but is actually still considered a single line until now.

  Placing double newline here will result in newline in the actual data.
```

Verbatim style is supported with the `|` character:

```yaml
key: |
  Now each
  newline is
  treated as such
```

## YAML vs JSON

YAML is a superset of JSON (JavaScript Object Notation). Thus,

```json
{
  "key": [
    {
      "value 1": {
        "another key": {
          "yet another key": "value 2"
        },
        "another key 2": [
          "more values"
        ],
        "this keys value is also an array": ["but indentation is not necessary here"]
      }
    }
  ]
}
```

is also valid YAML. In general YAML is more compact than JSON:

```yaml
key:
  - value 1:
      another key:
        yet another key: value 2
      another key 2:
        - more values
      this keys value is also an array:
        - but indentation is not necessary here
```

## yq command line tool

`yq` is a useful tool to work with `yaml`. It can be installed using `pip`:

```bash
$ pip show yq  
Name: yq
Version: 2.10.0
Summary: Command-line YAML/XML processor - jq wrapper for YAML/XML documents
Home-page: https://github.com/kislyuk/yq
Author: Andrey Kislyuk
Author-email: kislyuk@gmail.com
License: Apache Software License
Location: /usr/local/lib/python3.6/site-packages
Requires: PyYAML, setuptools, xmltodict, argcomplete
Required-by: 
```

`yq` is a `jq` wrapper, this means that it converts the yaml input to json and then handles the processing to `jq`, for this reason it has the same syntax as `jq`. In the example below, the value of `.data.WebHookSecretKey` is retrieved in raw mode (without quotes):

```bash
$ echo 'apiVersion: v1
kind: Secret
data:
  WebHookSecretKey: dGhpc19pc19hX2JhZF90b2tlbgo=
metadata:
  name: webhooksecret
  namespace: mynamespace     # set this to your project namespace
' | yq ' .data.WebHookSecretKey ' -r
dGhpc19pc19hX2JhZF90b2tlbgo=
```

For more information, see [yaml.org](https://yaml.org/) or [json.org](https://json.org).
