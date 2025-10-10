!!! success "Perustaso"
    Tarvitset vain perustiedot tietotekniikasta. On hyödyllistä tietää, miten XML tai JSON toimii.

# Lyhyt johdanto YAML:iin { #short-introduction-to-yaml }

YAML:ia käytetään avain–arvokarttojen ja listojen kuvaamiseen. YAML-tiedostot tunnistaa
`.yml`- tai `.yaml`-tiedostopäätteestä.

YAML-tietojoukko voi olla

* arvo

```yaml
value
```

* lista

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

* YAML-tietojoukko

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

Arvoja voi syöttää useille riveille käyttäen merkkiä `>`:

```yaml
key: >
  Here's a value that is written over multiple lines
  but is actually still considered a single line until now.

  Placing double newline here will result in newline in the actual data.
```

Literaalityyli (verbatim) on tuettu merkillä `|`:

```yaml
key: |
  Now each
  newline is
  treated as such
```

## YAML vs JSON { #yaml-vs-json }

YAML on JSONin ylijoukko (JavaScript Object Notation). Näin ollen,

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

on myös kelvollista YAML:ia. Yleisesti ottaen YAML on kompaktimpaa kuin JSON:

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

## yq-komentorivityökalu { #yq-command-line-tool }

`yq` on hyödyllinen työkalu `yaml`:n kanssa työskentelyyn. Sen voi asentaa [`pip`](https://pypi.org/project/yq/)-komennolla:

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

`yq` on `jq`-kääre, mikä tarkoittaa, että se muuntaa yaml-syötteen jsoniksi ja välittää käsittelyn `jq`:lle; tästä syystä sen syntaksi on sama kuin `jq`:n. Alla olevassa esimerkissä haetaan `.data.WebHookSecretKey`-arvo raakamuodossa (ilman lainausmerkkejä):

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

Lisätietoja: [yaml.org](https://yaml.org/) tai [json.org](https://json.org).