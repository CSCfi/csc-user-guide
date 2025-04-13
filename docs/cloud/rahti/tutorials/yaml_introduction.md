
# Lyhyt johdatus YAML-kieleen {#short-introduction-to-yaml}

YAML:ia käytetään kuvaamaan avain-arvo -karttoja ja taulukoita. YAML-tiedostot tunnistetaan käyttämällä `.yml` tai `.yaml` tiedostopäätettä.

YAML-datasetti voi olla

* arvo

```yaml
value
```

* taulukko

```yaml
- value 1
- value 2
- value 3
```

tai

```yaml
[value 1, value 2, value 3]
```

* sanakirja

```yaml
key: value
another_key: another value
```

tai

```yaml
key:
  value
another_key:
  another value
```

* YAML-datasetti

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

Arvot voidaan syöttää monille riveille käyttäen `>`:

```yaml
key: >
  Here's a value that is written over multiple lines
  but is actually still considered a single line until now.

  Placing double newline here will result in newline in the actual data.
```

Verbatim-tyyliä tuetaan `|` merkillä:

```yaml
key: |
  Now each
  newline is
  treated as such
```

## YAML vs JSON {#yaml-vs-json}

YAML on JSON:in (JavaScript Object Notation) yläjoukko. Tällöin,

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

on myös kelvollinen YAML. Yleisesti ottaen YAML on kompaktimpaa kuin JSON:

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

## yq komentorivityökalu {#yq-command-line-tool}

`yq` on hyödyllinen työkalu `yaml`-tiedostojen kanssa työskentelyyn. Sen voi asentaa käyttämällä [`pip`](https://pypi.org/project/yq/):

```bash
$ pip show yq  
Name: yq
Version: 3.0.2
Summary: Command-line YAML/XML processor - jq wrapper for YAML/XML documents
Home-page: https://github.com/kislyuk/yq
Author: Andrey Kislyuk
Author-email: kislyuk@gmail.com
License: Apache Software License
Location: /home/jtahir/Documents/csc-stuff/osclient/lib/python3.6/site-packages
Requires: argcomplete, PyYAML, toml, xmltodict
Required-by: 
```

`yq` on `jq`-kääre. Tämä tarkoittaa, että se muuntaa yaml-syötteen jsoniksi ja käsittelee sen sen jälkeen `jq`:lle, ja siksi sillä on sama syntaksi kuin `jq`:lla. Seuraavassa esimerkissä `.data.WebHookSecretKey`:n arvo haetaan raakatilassa (ilman lainausmerkkejä):

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

Lisätietoja löytyy osoitteista [yaml.org](https://yaml.org/) tai [json.org](https://json.org).

