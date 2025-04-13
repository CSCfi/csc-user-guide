
# Allaksen käyttäminen Pythonin kanssa S3-protokollan yli {#using-allas-with-python-over-the-s3-protocol}

Voit käyttää [AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
(`boto3`) pääsyyn Allakseen [S3-protokollan](../introduction.md#protocols) avulla.
`boto3` on Python-kirjasto, joka on kehitetty työskentelemään
[Amazon S3 -tallennuksen](https://aws.amazon.com/s3/) ja muiden AWS-palveluiden kanssa.

## Yleinen data-analyysityönkulku {#general-data-analysis-workflow}

1. Lataa syöttödata Allakseen käyttämällä `boto3`-ohjelmaa tai [muuta
   asiakasta](../accessing_allas.md).
2. Lataa data Allaksesta paikalliselle laitteelle
(esim. henkilökohtainen työasema tai CSC:n supertietokone) käyttämällä `boto3`-ohjelmaa.
3. Analysoi paikallinen datakopiosi.
4. Kirjoita analyysin tulokset paikalliseen tallennustilaan.
5. Lataa tulokset Allakseen käyttämällä `boto3`-ohjelmaa.

Jotkin Python-kirjastot tukevat suoraa lukemista ja kirjoittamista S3:n kautta,
kuten
[AWS SDK for pandas](https://aws-sdk-pandas.readthedocs.io/en/stable/)
ja
[GDAL-pohjaiset kirjastot](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py)
(paikkatietoaineistojen käsittelyyn).

!!! note ""
    Muista välttää samojen objektien käsittelyä sekä S3:lla että SWIFT:llä, sillä
    [ne toimivat eri tavoin suurten objektien kanssa](../introduction.md#protocols).

## Asennus {#installation}

### Asennus henkilökohtaiselle työasemalle {#installation-on-a-personal-workstation}

`boto3` on saatavilla Python 3.8 ja uudemmille versioille.
Se voidaan
[asentaa henkilökohtaiselle laitteelle](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation)
käyttäen `pip`- tai `conda`-ohjelmaa.

```bash
# pip
pip install boto3

# conda
conda install anaconda::boto3
```

### Asennus CSC:n supertietokoneelle {#installation-on-a-csc-supercomputer}

[`geoconda`](../../../apps/geoconda.md) ja
[`biopythontools`](../../../apps/biopython.md) moduulit sisältävät jo valmiiksi `boto3`-ohjelman.
Jos haluat käyttää kirjastoa jossakin muussa Python-ympäristössä, voit käyttää `pip`-ohjelmaa
[lisätäksesi sen olemassa olevaan moduuliin](../../../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).

## S3-tunnuksien määrittäminen {#configuring-s3-credentials}

### Tunnukset yksittäisen projektin käyttöön {#credentials-for-accessing-a-single-project}

Helpoin tapa määrittää S3-tunnukset `boto3`-ohjelman käyttöä varten on
[säätämällä S3-yhteys CSC:n supertietokoneella](s3_client.md#configuring-s3-connection-in-supercomputers).
Kun `allas-conf --mode s3cmd` suoritetaan, tunnukset tallennetaan
`~/.aws/credentials`, joka on oletussijainti, josta `boto3` etsii niitä.
Voit myös määritellä toisen sijainnin tunnuksien tiedostolle
muokkaamalla `AWS_SHARED_CREDENTIALS_FILE` ympäristömuuttujaa.

Jos haluat käyttää Allasta henkilökohtaiselta työasemalta,
voit yksinkertaisesti kopioida tunnuksien tiedoston laitteellesi
[käyttämällä tiedostonsiirtotyökalua](../../moving/index.md) kuten `scp`.
Jos haluat, että `boto3` löytää tunnukset automaattisesti
ilman `AWS_SHARED_CREDENTIALS_FILE`-muutoksia,
varmista, että kopioit myös yläkansio kuten alla olevassa esimerkissä.

```bash
# Kopioi tunnustiedosto ja sen yläkansio kotihakemistoosi
scp -r <käyttäjänimi>@<isäntänimi>.csc.fi:~/.aws $HOME
```

### Tunnukset useiden projektien käyttöön {#credentials-for-accessing-multiple-projects}

`allas-conf --mode s3cmd` on suoraviivainen tapa,
mutta se ylikirjoittaa olemassa olevan tunnustiedoston jokaisella ajolla,
joka tekee useiden projektien kanssa työskentelystä hieman vaivalloista.
Siksi suositellaan käyttämään
[Pilvitallennuksen määrityssovellusta](../../../computing/webinterface/file-browser.md#accessing-allas-and-lumi-o)
[Puhdin](https://puhti.csc.fi) tai [Mahti](https://mahti.csc.fi)
verkkokäyttöliittymässä S3-yhteyksien määritykseen, koska nämä määritykset tallennetaan
[erillisiin S3-profiileihin](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#shared-credentials-file).

1. Käytä *Pilvitallennuksen määritystä* konfiguroidaksesi S3-yhteydet,
tai _etäyhteydet_, projekteille, joiden Allas-tallennukseen haluat päästä.
Konfiguraatiot tallennetaan `~/.config/rclone/rclone.conf` tiedostoon siinä supertietokoneessa,
jonka verkkokäyttöliittymää käytit niiden luomiseen.

2. S3-konfiguraatiot syöttöavaimen tunnukselle ja salaiselle pääsyavaimelle
tarvitsevat prefiksiksi `aws_` jotta `boto3` tunnistaa ne S3-tunnuksiksi,
mutta emme halua tehdä muutoksia suoraan
`~/.config/rclone/rclone.conf`-tiedostoon, koska sitä käyttävät muutkin ohjelmat.
Sen sijaan käytä `sed`-komentoa lukemaan konfiguraatiotiedoston sisältö,
tekemään tarvittavat muutokset ja kirjoittamaan muokatut sisällöt uuteen tiedostoon,
esimerkiksi `~/.boto3_credentials`. Tämä voidaan tehdä seuraavalla komennolla.

    ```bash
    sed -E 's/^(access|secret)/aws_\1/g' ~/.config/rclone/rclone.conf > ~/.boto3_credentials
    ```

Näiden vaiheiden jälkeen S3-tunnuksesi `boto3`:n käyttöä varten ovat tallennettu
projektiin liittyviin S3-profiileihin tiedostossa, jonka loit vaiheessa 2. Profiilien nimet
ovat muodossa `s3allas-<project>`, esimerkiksi `s3allas-project_2001234`.
Nyt voit käyttää näitä tunnuksia
[luodaksesi `boto3`-resurssin](#create-boto3-resource).

## `boto3` käyttö {#boto3-usage}

### Luo `boto3`-resurssi {#create-boto3-resource}

S3-tunnukset määritetty vain yhdelle projektille:
```python
# Luo resurssi käyttämällä oletuksena olevaa tunnussijaintia
import boto3

s3_resource = boto3.resource('s3', endpoint_url='https://a3s.fi')
```
S3-tunnukset määritetty useille projekteille:
```python
# Luo resurssi käyttämällä profiilin tunnuksia
import boto3
import os

s3_credentials = '<credentials-file>'   # esim. '~/.boto3_credentials'
s3_profile = 's3allas-<project>'        # esim. 's3allas-project_2001234'

os.environ['AWS_SHARED_CREDENTIALS_FILE'] = s3_credentials
s3_session = boto3.Session(profile_name=s3_profile)
s3_resource = s3_session.resource('s3', endpoint_url='https://a3s.fi')
```

!!! note ""
    Jokainen seuraava askel olettaa, että `boto3`-resurssi on luotu.

### Luo ämpäri {#create-a-bucket}

Luo uusi ämpäri seuraavalla skriptillä:

```python
s3_resource.create_bucket(Bucket="examplebucket")
```

### Listaa ämpärit ja tiedostot {#list-buckets-and-objects}

Listaa kaikki projektiin kuuluvat ämpärit:
```python
for bucket in s3_resource.buckets.all():
    print(bucket.name)
```

Listaa kaikki ämpäriin kuuluvat objektit:
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

Lataa pieni tiedosto nimeltä `my_snake.txt` ämpärille `snakebucket`:

```python
s3_resource.Object('examplebucket', 'object_name_in_allas.txt').upload_file('local_file.txt')
```

### Poista ämpärit ja objektit {#remove-buckets-and-objects}

Poista kaikki objektit ämpäristä:

```python
my_bucket = s3_client.Bucket('examplebucket')
my_bucket.objects.all().delete()

```

Poista ämpäri, täytyy olla tyhjä:
```python
s3_resource.Bucket('examplebucket').delete()
```
