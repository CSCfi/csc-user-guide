# Allaksen käyttäminen Pythonilla S3-protokollan yli { #using-allas-with-python-over-the-s3-protocol }

Voit käyttää [AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
(`boto3`)-kirjastoa Allaksen käyttämiseen [S3-protokollan](../introduction.md#protocols) yli.
`boto3` on Python-kirjasto, joka on kehitetty työskentelyyn
[Amazon S3 -tallennuksen](https://aws.amazon.com/s3/) ja muiden AWS-palveluiden kanssa.

## Yleinen data-analyysin työnkulku { #general-data-analysis-workflow }

1. Lataa syötedata Allakseen `boto3`:lla tai [toisella
   asiakkaalla](../accessing_allas.md).
2. Lataa data Allaksesta paikalliselle laitteelle
(esim. omalle työasemalle tai CSC:n supertietokoneelle) käyttäen `boto3`:a.
3. Analysoi datan paikallinen kopio.
4. Kirjoita analyysin tulokset paikalliseen tallennustilaan.
5. Lataa tulokset Allakseen `boto3`:lla.

Jotkin Python-kirjastot tukevat suoraa lukemista ja kirjoittamista S3:n yli,
kuten
[AWS SDK for pandas](https://aws-sdk-pandas.readthedocs.io/en/stable/)
ja
[GDAL-pohjaiset kirjastot](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py)
(paikkatietojen käsittelyyn).

!!! note ""
    Muista välttää samojen objektien käsittelyä sekä S3:lla että SWIFTillä, sillä
    [ne toimivat eri tavoin suurten objektien kanssa](../introduction.md#protocols).

## Asennus { #installation }

### Asennus omalle työasemalle { #installation-on-a-personal-workstation }

`boto3` on saatavilla Python 3.8:lle ja uudemmille.
Sen voi
[asentaa omalle laitteelle](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation)
käyttäen `pip`:iä tai `conda`:a.

```bash
# pip
pip install boto3

# conda
conda install anaconda::boto3
```

### Asennus CSC:n supertietokoneelle { #installation-on-a-csc-supercomputer }

Ennalta olemassa olevissa [`geoconda`](../../../apps/geoconda.md)- ja
[`biopythontools`](../../../apps/biopython.md) -moduleissa `boto3`
on jo asennettuna. Jos haluat käyttää kirjastoa toisessa Python-ympäristössä, voit
käyttää `pip`:iä
[lisätäksesi sen olemassa olevan moduulin päälle](../../../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).

### Tunnistetiedot yhden CSC-projektin käyttöön { #credentials-for-accessing-one-csc-project }

```text
module load allas
allas-conf -m S3
```

`boto3` käyttää sisäisesti `aws`-kirjastoa, joten jos haluat [kopioida tunnistetietosi](allas-conf.md#s3-connection-details) supertietokoneen ulkopuolelle, seuraa `aws`:n ohjeita.

### Tunnistetiedot useiden CSC-projektien käyttöön { #credentials-for-accessing-multiple-csc-projects }

`allas-conf -m S3` on suoraviivainen,
mutta se ylikirjoittaa olemassa olevan tunnistetietotiedoston ajon yhteydessä,
mikä tekee useiden projektien kanssa työskentelystä hieman työlästä.
Siksi suositellaan käyttämään 
[Cloud storage configuration](../../../computing/webinterface/file-browser.md#accessing-allas-and-lumi-o)
-sovellusta [Puhti](https://puhti.csc.fi)- tai [Mahti](https://mahti.csc.fi)-
verkkokäyttöliittymässä S3-yhteyksien määrittämiseen, koska nämä määritykset
tallennetaan
[erillisiin S3-profiileihin](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#shared-credentials-file).

1. Käytä sovellusta *Cloud storage configuration* määrittääksesi S3-yhteydet,
tai _remotet_, niille projekteille, joiden Allas-tallennukseen haluat
pääsyn. Määritykset tallennetaan tiedostoon `~/.config/rclone/rclone.conf` sillä
supertietokoneella, jonka verkkokäyttöliittymää käytit niiden luomiseen.

2. S3-määritysten access key ID- ja secret access key -kenttien
alkuun pitää lisätä etuliite `aws_`, jotta `boto3` tunnistaa ne S3-
tunnistetiedoiksi, mutta emme halua muokata suoraan
tiedostoa `~/.config/rclone/rclone.conf`, koska sitä käyttävät muutkin ohjelmat.
Käytä sen sijaan `sed`-työkalua lukemaan määritystiedoston sisältö,
tekemään tarvittavat muutokset ja kirjoittamaan muokattu sisältö uuteen tiedostoon,
esimerkiksi `~/.boto3_credentials`. Tämä kaikki onnistuu seuraavalla komennolla.

    ```bash
    sed -E 's/^(access|secret)/aws_\1/g' ~/.config/rclone/rclone.conf > ~/.boto3_credentials
    ```

Kun olet tehnyt nämä vaiheet, `boto3`:n käyttöä varten S3-tunnistetietosi ovat
tallessa projektikohtaisissa S3-profiileissa tiedostossa, jonka loit kohdassa 2. Profiilien nimet
ovat muotoa `s3allas-<project>`, esim. `s3allas-project_2001234`.
Voit nyt käyttää näitä tunnistetietoja
[luodaksesi `boto3`-resurssin](#create-boto3-resource).

## `boto3`:n käyttö { #boto3-usage }

### Luo `boto3`-resurssi { #create-boto3-resource }

S3-tunnistetiedot konfiguroitu vain yhdelle projektille:
```python
# Create resource using credentials from the default location
# With newer versions of aws-library:
#   - defining endpoint here is not any more mandatory, if it is given in the config file.
#   - two checksum settings must be added that moving objects to/from Allas would work

import boto3
os.environ["AWS_REQUEST_CHECKSUM_CALCULATION"] = "when_required"
os.environ["AWS_RESPONSE_CHECKSUM_VALIDATION"] = "when_required"

s3_resource = boto3.resource('s3', endpoint_url='https://a3s.fi')
```
S3-tunnistetiedot konfiguroitu usealle projektille:
```python
# Create resource using credentials from a profile
import boto3
import os

s3_credentials = '<credentials-file>'   # e.g. '~/.boto3_credentials'
s3_profile = 's3allas-<project>'        # e.g. 's3allas-project_2001234'

os.environ['AWS_SHARED_CREDENTIALS_FILE'] = s3_credentials
os.environ["AWS_REQUEST_CHECKSUM_CALCULATION"] = "when_required"
os.environ["AWS_RESPONSE_CHECKSUM_VALIDATION"] = "when_required"

s3_session = boto3.Session(profile_name=s3_profile)
s3_resource = s3_session.resource('s3', endpoint_url='https://a3s.fi')
```

!!! note ""
    Kaikki seuraavat vaiheet olettavat, että `boto3`-resurssi on luotu.

### Luo bucket { #create-a-bucket }

Luo uusi bucket seuraavalla skriptillä:

```python
s3_resource.create_bucket(Bucket="examplebucket")
```

### Listaa bucketit ja objektit { #list-buckets-and-objects }

Listaa kaikki projektiin kuuluvat bucketit:
```python
for bucket in s3_resource.buckets.all():
    print(bucket.name)
```

Listaa kaikki bucketiin kuuluvat objektit:
```python
my_bucket = s3_resource.Bucket('examplebucket')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)

```

### Lataa objekti { #download-an-object }

Lataa objekti:
```python
s3_resource.Object('examplebucket', 'object_name_in_allas.txt').download_file('local_file.txt')
```

### Lähetä objekti { #upload-an-object }

Lähetä pieni tiedosto nimeltä `my_snake.txt` bucketiin `snakebucket`:

```python
s3_resource.Object('examplebucket', 'object_name_in_allas.txt').upload_file('local_file.txt')
```

### Poista bucketit ja objektit { #remove-buckets-and-objects }

Poista kaikki objektit bucketista:

```python
my_bucket = s3_client.Bucket('examplebucket')
my_bucket.objects.all().delete()

```

Poista bucket, sen on oltava tyhjä:
```python
s3_resource.Bucket('examplebucket').delete()
```