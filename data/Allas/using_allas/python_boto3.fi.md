# Allaksen käyttäminen Pythonilla S3-protokollan yli {#using-allas-with-python-over-the-s3-protocol}

Voit käyttää [AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
(`boto3`) -kirjastoa Allaksen käyttämiseen [S3-protokollan](../introduction.md#protocols) kautta.
`boto3` on Python-kirjasto, joka on kehitetty työskentelyyn
[Amazon S3 -tallennustilan](https://aws.amazon.com/s3/) sekä muiden AWS-palveluiden kanssa.

## Yleinen data-analyysin työnkulku {#general-data-analysis-workflow}

1. Lataa syötedata Allakseen käyttäen `boto3`:a tai [jotakin muuta
   asiakasohjelmaa](../accessing_allas.md).
2. Lataa data Allaksesta paikalliselle laitteelle
(esim. omalle työasemalle tai CSC:n supertietokoneelle) käyttäen `boto3`:a.
3. Analysoi paikallista kopiota datasta.
4. Kirjoita analyysin tulokset paikalliseen tallennukseen.
5. Lataa tulokset Allakseen käyttäen `boto3`:a.

Jotkin Python-kirjastot tukevat suoraa luku- ja kirjoitusyhteyttä S3:n yli,
esimerkiksi
[AWS SDK for pandas](https://aws-sdk-pandas.readthedocs.io/en/stable/)
sekä
[GDAL-pohjaiset kirjastot](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py)
(paineiston käsittelyyn paikkatietoaineistoja varten).

!!! note ""
    Muista välttää samojen objektien käsittelyä sekä S3:lla että SWIFTillä, koska
    [ne toimivat eri tavoin suurten objektien kanssa](../introduction.md#protocols).

## Asennus {#installation}

### Asennus omalle työasemalle {#installation-on-a-personal-workstation}

`boto3` on saatavilla Python 3.8:lle ja uudemmille.
Se voidaan
[asentaa omalle laitteelle](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation)
käyttäen `pip`:iä tai `conda`:a.

```bash
# pip
pip install boto3

# conda
conda install anaconda::boto3
```

### Asennus CSC:n supertietokoneelle {#installation-on-a-csc-supercomputer}

Valmiit [`geoconda`](../../../apps/geoconda.md)- ja
[`biopythontools`](../../../apps/biopython.md)-moduulit sisältävät jo `boto3`-kirjaston.
Jos haluat käyttää kirjastoa jossakin toisessa Python-ympäristössä, voit
käyttää `pip`:iä
[lisätäksesi sen olemassa olevan moduulin päälle](../../../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).

## S3-tunnistetietojen määrittäminen {#configuring-s3-credentials}

### Tunnukset yksittäiseen projektiin {#credentials-for-accessing-a-single-project}

Helpoin tapa määrittää S3-tunnukset `boto3`:n käyttöön on
[määrittää S3-yhteys CSC:n supertietokoneella](s3_client.md#configuring-s3-connection-in-supercomputers).
Kun suoritat komennon `allas-conf --mode s3cmd`, tunnukset tallennetaan
tiedostoon `~/.aws/credentials`, joka on oletussijainti, josta `boto3` etsii niitä.
Voit myös määrittää tiedostolle toisen sijainnin muokkaamalla
ympäristömuuttujaa `AWS_SHARED_CREDENTIALS_FILE`.

Jos haluat käyttää Allasta omalta työasemalta,
voit yksinkertaisesti kopioida tunnistetiedoston laitteellesi
[käyttäen tiedostonsiirto-ohjelmaa](../../moving/index.md) kuten `scp`.
Jos haluat, että `boto3` löytää tunnistetiedot automaattisesti
ilman `AWS_SHARED_CREDENTIALS_FILE`:n muokkaamista,
varmista, että kopioit myös yläkansion seuraavan esimerkin mukaisesti.

```bash
# Kopioi tunnistetiedoston yläkansioineen kotihakemistoosi
scp -r <username>@<hostname>.csc.fi:~/.aws $HOME
```

### Tunnukset useisiin projekteihin {#credentials-for-accessing-multiple-projects}

Komennon `allas-conf --mode s3cmd` käyttäminen on suoraviivaista,
mutta se korvaa olemassa olevan tunnistetiedoston aina, kun se suoritetaan,
mikä tekee monen projektin kanssa työskentelystä hieman hankalaa.
Siksi suositellaan käyttämään
[Pilvitallennuksen konfiguraatio](../../../computing/webinterface/file-browser.md#accessing-allas-and-lumi-o) -sovellusta
[Puhti](https://puhti.csc.fi)- tai [Mahti](https://mahti.csc.fi)-web-liittymässä
S3-yhteyksien määrittämiseen, sillä näiden määritysten tiedot tallennetaan
[erillisiin S3-profiileihin](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#shared-credentials-file).

1. Käytä *Pilvitallennuksen konfiguraatio* ‑sovellusta S3-yhteyksien eli _etäyhteyksien_ määrittämiseen niihin projekteihin, joiden Allas-tallennukseen haluat päästä käsiksi. Määritykset tallennetaan tiedostoon `~/.config/rclone/rclone.conf` sillä supertietokoneella, jonka web-liittymää käytit niiden luomiseen.

2. S3-määrityksissä pääsyavaimen (access key ID) ja salaisen pääsyavaimen (secret access key)
kohta pitää esittää etuliitteellä `aws_`, jotta `boto3` tunnistaa ne S3-tunnuksiksi. Mutta emme halua muokata
suoraan tiedostoa `~/.config/rclone/rclone.conf`, koska sitä käyttävät muutkin
ohjelmat. Käytä sen sijaan `sed`-ohjelmaa konfiguraatiotiedoston sisällön lukemiseen,
teknisten muutosten tekemiseen ja tuloksen tallentamiseen uuteen tiedostoon, esimerkiksi
`~/.boto3_credentials`. Tämän voi tehdä seuraavalla komennolla.

    ```bash
    sed -E 's/^(access|secret)/aws_\1/g' ~/.config/rclone/rclone.conf > ~/.boto3_credentials
    ```

Tämän jälkeen S3-tunnukset `boto3`:n käyttöä varten on tallennettu
projektikohtaisiin S3-profiileihin tähän tiedostoon, jonka loit vaiheessa 2. Profiilien nimet
ovat muodossa `s3allas-<project>`, esim. `s3allas-project_2001234`.
Voit nyt käyttää näitä tunnuksia
[luodaksesi `boto3`-resurssin](#create-boto3-resource).

## `boto3`:n käyttö {#boto3-usage}

### Luo `boto3`-resurssi {#create-boto3-resource}

S3-tunnukset määritetty vain yhtä projektia varten:
```python
# Luo resurssi käyttäen tunnuksia oletussijainnista
import boto3

s3_resource = boto3.resource('s3', endpoint_url='https://a3s.fi')
```
S3-tunnukset määritetty useille projekteille:
```python
# Luo resurssi käyttäen tunnuksia profiilista
import boto3
import os

s3_credentials = '<credentials-file>'   # esim. '~/.boto3_credentials'
s3_profile = 's3allas-<project>'        # esim. 's3allas-project_2001234'

os.environ['AWS_SHARED_CREDENTIALS_FILE'] = s3_credentials
s3_session = boto3.Session(profile_name=s3_profile)
s3_resource = s3_session.resource('s3', endpoint_url='https://a3s.fi')
```

!!! note ""
    Jokainen seuraava vaihe edellyttää, että `boto3`-resurssi on luotu.

### Luo bucket {#create-a-bucket}

Luo uusi bucket seuraavalla skriptillä:

```python
s3_resource.create_bucket(Bucket="examplebucket")
```

### Listaa bucketit ja objektit {#list-buckets-and-objects}

Listaa kaikki projektin bucketit:
```python
for bucket in s3_resource.buckets.all():
    print(bucket.name)
```

Listaa kaikki objektit yhdessä bucketissa:
```python
my_bucket = s3_resource.Bucket('examplebucket')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)

```

### Lataa objekti {#download-an-object}

Lataa objekti:
```python
s3_resource.Object('examplebucket', 'object_name_in_allas.txt').download_file('local_file.txt')
```

### Lataa objekti {#upload-an-object}

Lataa pieni tiedosto nimeltä `my_snake.txt` bucketiin `snakebucket`:

```python
s3_resource.Object('examplebucket', 'object_name_in_allas.txt').upload_file('local_file.txt')
```

### Poista bucketit ja objektit {#remove-buckets-and-objects}

Poista kaikki objektit bucketista:

```python
my_bucket = s3_client.Bucket('examplebucket')
my_bucket.objects.all().delete()

```

Poista bucket (sen täytyy olla tyhjä):
```python
s3_resource.Bucket('examplebucket').delete()
```