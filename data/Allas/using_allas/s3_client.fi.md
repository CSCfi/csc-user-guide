# S3-asiakas {#the-s3-client}

Tässä luvussa kuvataan, miten Allas-objektitallennuspalvelua käytetään **s3cmd**-komentorivityökalulla. Tämä asiakasohjelma käyttää _S3_-protokollaa, joka eroaa [Rclone](./rclone.md), [swift](./swift_client.md) ja [a-commands](./a_commands.md) -esimerkeissä käytetystä _Swift_-protokollasta. Tavallisesti S3:lla ladattu data on käytettävissä myös Swift-protokollan kautta. Yli 5 GB:n kokoiset Swiftillä Allakseen ladatut tiedostot eivät kuitenkaan ole ladattavissa S3-protokollalla.

Käyttäjän näkökulmasta yksi tärkeimmistä eroista S3- ja Swift-protokollien välillä on se, että Swift-yhteydet pysyvät voimassa kahdeksan tuntia kerrallaan, mutta S3:lla yhteys pysyy avoimena pysyvästi. Pysyvä yhteys on monessa mielessä kätevä, mutta siihen liittyy myös tietoturvariski: jos CSC-tunnuksesi joutuu vääriin käsiin, myös objektitallennustilasi voidaan vaarantaa.

`s3cmd`-komennon syntaksi:
```text
s3cmd -options command parameters
```

Yleisimmät _s3cmd_-komennot:

| s3cmd-komento | Toiminto |
| :---- | :---- |
| mb | Luo bucket |
| put | Lataa objekti |
| ls | Listaa objektit ja bucketit |
| get | Lataa objektit ja bucketit |
| cp | Siirrä objekti |
| del | Poista objektit tai bucketit |
| md5sum | Tarkista tarkistussumma |
| info | Näytä metatiedot |
| signurl | Luo väliaikainen URL |
| put -P | Julkista objekti |
| setacl --acl-grant | Hallitse käyttöoikeuksia |


Yllä olevassa taulukossa on lueteltu vain keskeisimmät _s3cmd_-komennot. Laajemman listan saat [s3cmd:n manuaalisivulta](https://s3tools.org/usage) tai kirjoittamalla:
```text
s3cmd -h
```

## s3cmd:n käyttöönotto {#getting-started-with-s3cmd}

Jos käytät Allasta Puhtissa tai Mahtissa, kaikki tarvittavat paketit ja ohjelmistot on jo asennettu. Voit tällöin ohittaa tämän luvun ja siirtyä kohtaan [S3-yhteyden määritys supertietokoneilla](#configuring-s3-connection-in-supercomputers).

S3cmd-yhteyden määrittelemiseksi ympäristöösi täytyy olla asennettu _OpenStack_ ja _s3cmd_.

**OpenStack s3cmd -asennus:**

Fedora/RHEL-pohjaiset:
```text
sudo yum update
sudo yum install python3
sudo pip3 install python-openstackclient
sudo yum install s3cmd
```
Debian-pohjaiset:
```text
sudo apt install python3-pip
sudo pip3 install python-openstackclient
sudo apt install restic
curl https://rclone.org/install.sh | sudo bash
sudo pip3 install s3cmd
```
OSX:
```text
python3 virtualenv
pip3 install s3cmd
s3cmd
```

Katso lisäohjeita osoitteista [http://s3tools.org/download](http://s3tools.org/download) ja [http://s3tools.org/usage](http://s3tools.org/usage).

**S3-yhteyden määrittäminen omalla koneella**

Kun _OpenStack_ ja _s3cmd_ on asennettu, voit ladata [allas_conf](https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/allas_conf)
-skriptin S3-yhteyden määrittämiseksi Allas-projektiisi.
```text
wget https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/allas_conf
source allas_conf --mode S3 --user your-csc-username
```
Huomaa, että sinun tulee käyttää `--user`-optiota määrittääksesi oman CSC-tunnuksesi. Konfigurointikomento kysyy ensin CSC-salasanaasi ja sen jälkeen Allas-projektin valintaa. Tämän jälkeen työkalu luo avaintiedoston S3-yhteydelle ja tallentaa sen oletussijaintiin (_.s3cfg_ kotihakemistossa).

## S3-yhteyden määritys supertietokoneilla {#configuring-s3-connection-in-supercomputers}

Jotta voit käyttää _s3cmd_:ia Puhtissa ja Mahtissa, sinun täytyy ensin konfiguroida yhteys:
```text
module load allas
allas-conf --mode S3
```
Konfigurointi kysyy ensin CSC-salasanaasi. Sen jälkeen se listaa Allas-projektisi ja pyytää valitsemaan käytettävän projektin. Konfiguraatiotiedot tallennetaan tiedostoon _$HOME/.s3cfg_. Tämä asetetaan vain kerran. Jatkossa _s3cmd_ käyttää automaattisesti kyseisessä _.s3cfg_-tiedostossa kuvattua objektitallennusyhteyttä. Jos haluat vaihtaa Allas-projektia, jota _s3cmd_ käyttää, suorita konfigurointikomento uudelleen.

Voit käyttää _.s3cfg_-tiedostoon tallennettuja S3-tunnuksia myös muissa palveluissa. Voit tarkistaa käytössä olevan _access keyn_ ja _secret_keyn_ komennolla:
```
grep key $HOME/.s3cfg

```

Jos käytät näitä avaimia muissa palveluissa, varmista, että ne pysyvät aina yksityisinä. Kuka tahansa, jolla on pääsy näihin kahteen avainarvoon, voi käyttää ja muokata kaikkea kyseisen projektin Allas-dataa.

Tarvittaessa voit deaktivoida S3-avaimen komennolla:

```
allas-conf --s3remove
```

## Buckettien luonti ja objektien lataus {#create-buckets-and-upload-objects}

Luo uusi bucket:
```text
s3cmd mb s3://my_bucket
```

Lataa tiedosto bucketiin:
```text
s3cmd put my_file s3://my_bucket
```

## Objektien ja buckettien listaaminen {#list-objects-and-buckets}

Listaa kaikki projektin bucketit:
```text
s3cmd ls
```

Listaa kaikki objektit bucketissa:
```text
s3cmd ls s3://my_bucket
```

Näytä bucketin tiedot:
```text
s3cmd info s3://my_bucket
```

Näytä objektin tiedot:
```text
s3cmd info s3://my_bucket/my_file
```

## Objektien ja buckettien lataus {#download-objects-and-buckets}

Lataa objekti:
```text
s3cmd get s3://my_bucket/my_file new_file_name
```
Parametri *new_file_name* on valinnainen. Se määrittää ladatulle tiedostolle uuden nimen.

Komennolla `md5sum` voit tarkistaa, että tiedosto ei ole muuttunut tai vioittunut:
<pre>
$ <b>md5sum my_file new_file_name</b>
   39bcb6992e461b269b95b3bda303addf  my_file
   39bcb6992e461b269b95b3bda303addf  new_file_name
</pre>
Yllä olevassa esimerkissä tarkistussummat täsmäävät alkuperäisen ja ladatun tiedoston välillä.

Lataa koko bucket:
```text
s3cmd get -r s3://my_bucket/
```

## Objektien siirto {#move-objects}

Kopioi objekti toiseen bucketiin. Huomaa, että näitä komentoja tulee käyttää vain objektien kanssa, jotka on ladattu Allakseen S3-protokollalla:
```text
s3cmd cp s3://sourcebucket/objectname s3://destinationbucket
```

Esimerkiksi:
<pre>
$ <b>s3cmd cp s3://bigbucket/bigfish s3://my-new-bucket</b>
remote copy: 's3://bigbucket/bigfish' -> 's3://my-new-bucket/bigfish'
</pre>

Vaihda tiedoston nimi samalla kun kopioit sen:
<pre>
$ <b>s3cmd cp s3://bigbucket/bigfish s3://my-new-bucket/newname</b>
remote copy: 's3://bigbucket/bigfish' -> 's3://my-new-bucket/newname'
</pre>

## Objektien ja buckettien poisto {#delete-objects-and-buckets}

Poista objekti:
```text
s3cmd del s3://my_bucket/my_file
```

Poista bucket:
```text
s3cmd rb s3://my_bucket
```
**Huom:** Vain tyhjiä bucketteja voi poistaa.

## s3cmd ja julkiset objektit {#s3cmd-and-public-objects}

Tässä esimerkissä tehdään objekti _salmon.jpg_ julkiseksi pseudo-kansiossa _fishes_:
<pre>
$ <b>s3cmd put fishes/salmon.jpg s3://my_fishbucket/fishes/salmon.jpg -P</b>
Public URL of the object is: https://a3s.fi/my_fishbucket/fishes/salmon.jpg
</pre>

## Toisen projektin lukuoikeuden antaminen bucketiin {#giving-another-project-read-access-to-a-bucket}

Voit hallita käyttöoikeuksia komennolla `s3cmd setacl`. Tämä komento vaatii käyttöoikeuden saavan projektin UUID:n (_universally unique identifier_). Projektin jäsenet voivat tarkistaa oman projektinsa ID:n <a href="https://pouta.csc.fi/dashboard/identity/" target="_blank">https://pouta.csc.fi/dashboard/identity/</a> tai komennolla ```openstack project show```. Esimerkiksi Puhtissa ja Mahtissa:

```text
module load allas
allas-conf -k --mode s3cmd
openstack project show $OS_PROJECT_NAME
```

_s3cmd_:n tapauksessa luku- ja kirjoitusoikeuksia voidaan hallita sekä bucketille että yksittäisille objekteille:

Seuraava komento myöntää projektin UUID:lla _3d5b0ae8e724b439a4cd16d1290_ lukuoikeuden _my_fishbucket_:iin, mutta ei objekteihin sen sisällä:
```text
s3cmd setacl --acl-grant=read:3d5b0ae8e724b439a4cd16d1290 s3://my_fishbucket
```
Vastaavasti seuraava komento antaa kirjoitusoikeuden yksittäiselle objektille:
```text
s3cmd setacl --acl-grant=write:3d5b0ae8e724b439a4cd16d1290 s3://my_fishbucket/bigfish
```
Jos haluat muuttaa kaikkien bucketin objektien oikeuksia, lisää `--recursive`-valitsin komentoon:
```text
s3cmd setacl --recursive --acl-grant=read:3d5b0ae8e724b439a4cd16d1290 s3://my_fishbucket
```

Voit tarkistaa käyttöoikeudet _s3cmd info_:lla:
<pre>
$ <b>s3cmd info s3://my_fishbucket|grep -i acl</b>
   ACL:       other_project_uuid: READ
   ACL:       my_project_uuid: FULL_CONTROL
</pre>

Optiota _--acl-revoke_ voidaan käyttää poistaaksesi luku- tai kirjoitusoikeuden:
```text
s3cmd setacl --recursive --acl-revoke=read:$other_project_uuid s3://my_fishbucket
```

Jaetut objektit ja bucketit ovat käytettävissä sekä S3- että Swift-pohjaisilla työkaluilla. Huomaa kuitenkin, että listauskomennot näyttävät vain ne bucketit, joiden omistajana oma projektisi on. Jaettujen buckettien ja objektien tapauksessa tulee tietää bucketin nimi sitä käytettäessä.

Yllä olevassa esimerkissä käyttäjä projektista _3d5b0ae8e724b439a4cd16d1290_ ei näe _my_fishbucket_:ia jaon aikana komennolla:

```text
s3cmd ls
```
Hän voi kuitenkin listata bucketin sisällön komennolla:
```text
s3cmd ls s3://my_fishbucket
```
Pouta-verkkokäyttöliittymässä käyttäjä voi siirtyä jaettuun bucketiin määrittämällä bucketin nimen URL:iin. Siirry oman projektisi bucketiin ja vaihda bucketin nimi URL:n lopusta jaetun bucketin nimeen:
```
https://pouta.csc.fi/dashboard/project/containers/container/my_fishbucket
```

## Käyttöesimerkki {#use-example}

Tässä esimerkissä tallennetaan yksinkertainen aineisto Allakseen s3cmd:llä.

Luo ensin uusi bucket. Komento `s3cmd ls` osoittaa, että objektitallennustila on aluksi tyhjä. Luo sitten uusi bucket nimeltä _fish-bucket_ komennolla `s3cmd mb`.

<pre>
$ <b>s3cmd ls</b>
ls

$ <b>s3cmd mb s3://fish-bucket</b>
mb s3://fish-bucket/
Bucket 's3://fish-bucket/' created

$ <b>s3cmd ls</b>
ls
2018-03-12 13:01  s3://fish-bucket
</pre>
Suositeltavaa on kerätä tallennettava data suurempiin kokonaisuuksiin ja pakata se ennen lataamista järjestelmään.

Tässä esimerkissä tallennetaan Bowtie2-indeksit ja seeprakalan (danio rerio) genomi fish bucketiin. Komennolla `ls -lh` näet, että indeksitiedostot ovat olemassa nykyhakemistossa:

<pre>$ <b>ls -lh</b>
total 3.2G
-rw------- 1 kkayttaj csc 440M Mar 12 13:41 Danio_rerio.1.bt2
-rw------- 1 kkayttaj csc 327M Mar 12 13:41 Danio_rerio.2.bt2
-rw------- 1 kkayttaj csc 217K Mar 12 13:20 Danio_rerio.3.bt2
-rw------- 1 kkayttaj csc 327M Mar 12 13:20 Danio_rerio.4.bt2
-rw------- 1 kkayttaj csc 1.3G Mar 12 13:13 Danio_rerio.GRCz10.dna.toplevel.fa
-rw------- 1 kkayttaj csc 440M Mar 12 14:03 Danio_rerio.rev.1.bt2
-rw------- 1 kkayttaj csc 327M Mar 12 14:03 Danio_rerio.rev.2.bt2
-rw------- 1 kkayttaj csc 599K Mar 12 13:13 log
</pre>

Data kerätään ja pakataan yhteen tiedostoon komennolla `tar`:
```text
tar zcf zebrafish.tgz Danio_rerio*
```

Tuloksena syntyvän tiedoston koko on noin 2 GB. Pakattu tiedosto voidaan ladata fish bucketiin komennolla `s3cmd put`:
<pre>
$ <b>ls -lh zebrafish.tgz</b>
-rw------- 1 kkayttaj csc 9.3G Mar 12 15:23 zebrafish.tgz

$ <b>s3cmd put zebrafish.tgz s3://fish-bucket</b>
put zebrafish.tgz s3://fish-bucket
upload: 'zebrafish.tgz' -> 's3://fish-bucket/zebrafish.tgz'  [1 of 1]
 2081306836 of 2081306836   100% in   39s    50.16 MB/s  done

$ <b>s3cmd ls s3://fish-bucket</b>
ls s3://fish-bucket
2019-10-01 12:11 9982519261   s3://fish-bucket/zebrafish.tgz
</pre>

2 GB datan lähetys kestää hetken. Nouda ladattu tiedosto:
```text
s3cmd get s3://fish-bucket/zebrafish.tgz
```

Oletuksena bucketia voivat käyttää vain projektin jäsenet. Voit kuitenkin tehdä tiedoston julkiseksi komennolla `s3cmd setacl`.

Tee ensin fish bucket julkiseksi:
```text
s3cmd setacl --acl-public s3://fish-bucket
```

Tee sitten zebrafish-genomitiedosto julkiseksi:
```text
s3cmd setacl --acl-public s3://fish-bucket/zebrafish.tgz
```

Tiedoston URL-osoitteen syntaksi:
```text
https://a3s.fi/bucket_name/object_name
```

Tässä tapauksessa tiedosto olisi saatavilla linkillä
_https://a3s.fi/fish-bucket/zebrafish.tgz_

## Objektien tilapäinen julkaisu allekirjoitetuilla URL-osoitteilla {#publishing-objects-temporarily-with-signed-urls}

Komennolla _s3cmd signurl_ objekti voidaan julkaista Allaksessa tilapäisesti, käyttäen URL:ia, joka sisältää turvallisuutta parantavan pääsytunnisteen.

Edellä olevassa esimerkissä objekti _s3://fish-bucket/zebrafish.tgz_ tehtiin pysyvästi julkiseksi yksinkertaisella staattisella URLilla.
_signurl_-komennolla sama objekti voidaan jakaa turvallisemmin ja vain rajatuksi ajaksi. Esimerkiksi komento:

```text
s3cmd signurl s3://fish-bucket/zebrafish.tgz +3600
```
tulostaa URL-osoitteen, joka on voimassa 3600 sekuntia (1 h). Tällöin komennolla saatava URL näyttää esimerkiksi tältä:
```text
https://fish-bucket.a3s.fi/zebrafish.tgz?AWSAccessKeyId=78e6021a086d52f092b3b2b23bfd7a67&Expires=1599835116&Signature=OLyyCY14s%2F0HxKOOd108mldINyE%3D
```

## Objektien elinkaaren määrittäminen {#setting-up-an-object-lifecycle}

Jotta objektit voidaan poistaa/automaattisesti vanhentaa, voidaan Allas-bucketiin määritellä lifecycle policy (elinkaarikäytäntö). Bucketissa olevia objekteja käsitellään policyssä määriteltyjen sääntöjen mukaisesti, mikäli ehdot täyttyvät. Ehtoja voidaan asettaa esimerkiksi objektin etuliitteeseen (prefix) tai tageihin. Elinkaarikäytäntö sopii erityisesti tapauksiin, joissa data tulee poistaa tietyn ajan kuluttua esimerkiksi "ylläpitosyistä".

!!! warning
    Ennen elinkaarikäytännön määrittämistä varmista organisaatioltasi/tiimiltäsi, että se täyttää datan säilytyspolitiikan vaatimukset projektissa. (Juridiset ja säännökselliset rajoitukset).

Alla olevassa elinkaarikäytännön esimerkissä on kaksi sääntöä. Tallennetaan tiedosto nimellä `mypolicy.xml`.

```xml
<?xml version="1.0" ?>
<LifecycleConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <Rule>
      <ID>1-days-expiration</ID>
      <Status>Enabled</Status>
      <Expiration>
         <Days>1</Days>
      </Expiration>
      <Filter>
         <Tag>
            <Key>days</Key>
            <Value>1</Value>
         </Tag>
      </Filter>
   </Rule>
   <Rule>
      <ID>30-days-expiration</ID>
      <Status>Enabled</Status>
      <Expiration>
         <Days>30</Days>
      </Expiration>
      <Filter>
         <Tag>
            <Key>days</Key>
            <Value>30</Value>
         </Tag>
      </Filter>
   </Rule>
</LifecycleConfiguration>
```

Vaihtoehtoisesti policy voidaan asettaa käyttämällä `prefix`-ehtoja, jotka toimivat kuten "kansio". Molempia voidaan myös yhdistää käyttämällä `<And>`-tagia.

```xml
<?xml version="1.0" ?>
<LifecycleConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <Rule>
      <ID>Daily</ID>
      <Status>Enabled</Status>
      <Prefix>daily/</Prefix>
      <Expiration>
         <Days>30</Days>
      </Expiration>
   </Rule>
   <Rule>
      <ID>Weekly</ID>
      <Status>Enabled</Status>
      <Prefix>weekly/</Prefix>
      <Expiration>
         <Days>365</Days>
      </Expiration>
   </Rule>
</LifecycleConfiguration>
```

Asetetaan lifecycle policy buckettiin `setlifecycle`-alikomennolla:

```bash
s3cmd setlifecycle mypolicy.xml s3://MY_BUCKET
```

Policyn voi tarkistaa `getlifecycle`-alikomennolla:

```bash
s3cmd getlifecycle s3://MY_BUCKET
```

Tarkastele buckettia (tai objektia) `info`-alikomennolla:

```bash
s3cmd info s3://MY_BUCKET

s3://MY_BUCKET/ (bucket):
   Location:  cpouta-production
   Payer:     BucketOwner
   Expiration Rule: objects with key prefix 'weekly/' will expire in '365' day(s) after creation
   Policy:    none
   CORS:      none
   ACL:       project_xxxxxxx: FULL_CONTROL
```

Jotta objekti(t) voidaan saattaa elinkaaripolitiikan alaisuuteen, käytä tageja ja/tai prefixejä.

* Taggaaminen onnistuu lisäämällä header, esim. `x-amz-tagging:KEY=VALUE`
* Prefixiä voidaan pitää "kansiona"

Katsotaan seuraavat esimerkit:

```bash
# Poistetaan 24 tunnin kuluttua (rule ID: 1-days-expiration)
s3cmd --add-header=x-amz-tagging:days=1 put MY_FILE_01.tar.gz s3://MY_BUCKET/
s3cmd --add-header=x-amz-tagging:days=1 put MY_FILE_02.tar.gz s3://MY_BUCKET/gone-in-one-day/

# Poistetaan 30 päivän kuluttua (rule ID: 30-days-expiration)
s3cmd --add-header=x-amz-tagging:days=30 put MY_FILE_03.tar.gz s3://MY_BUCKET/

# Poistetaan 30 päivän kuluttua (rule ID: Daily)
s3cmd put MY_FILE_04.tar.gz s3://MY_BUCKET/daily/

# Poistetaan 365 päivän kuluttua (rule ID: Weekly)
s3cmd put MY_FILE_05.tar.gz s3://MY_BUCKET/weekly/
```

Lisätietoa elinkaarikäytännön määrittämisestä:

* [RedHat developer guide for Ceph storage](https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/3/html-single/developer_guide/index#s3-api-bucket-lifecycle).
* [Creating an intelligent object storage system with Ceph’s Object Lifecycle Management](https://shopnpaz.medium.com/creating-an-intelligent-object-storage-system-with-cephs-object-lifecycle-management-112e2e46d490)
* [Multiple lifecycles - s3cmd](https://stackoverflow.com/questions/49615977/multiple-lifecycles-s3cmd)
* Yllättävä löytö yllä olevasta aiheesta [cloud.blog.csc.fi](http://cloud.blog.csc.fi/2019/02/cpouta-cloud-object-storage-service-has.html)

## Bucketin käyttö rajatuista IP-osoitteista {#limit-bucket-access-to-specific-ip-addresses}

Voit rajoittaa bucketin käytön tiettyihin IP-osoitteisiin määrittelemällä policy-tiedoston.

!!! Warning
    Muista olla estämättä omaa pääsyä buckettiin – jos näin käy, et pääse enää buckettiin tai voi korjata policyä.

Seuraavassa IP-politiikan esimerkissä sallitaan pääsy bucketiin POLICY-EXAMPLE-BUCKET IP-verkosta 86.50.164.0/24. Nimeä policy-tiedosto `myippolicy.json`.

```json
{
    "Version": "2012-10-17",
    "Id": "S3PolicyExample",
    "Statement": [
        {
            "Sid": "IPAllow",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::POLICY-EXAMPLE-BUCKET",
                "arn:aws:s3:::POLICY-EXAMPLE-BUCKET/*"
            ],
            "Condition": {
                "NotIpAddress": {
                    "aws:SourceIp": "86.50.164.0/24"
                }
            }
        }
    ]
}
```

Asetetaan IP-policy bucketiin `setpolicy`-alikomennolla:

```bash
s3cmd setpolicy myippolicy.json s3://POLICY-EXAMPLE-BUCKET
```

Voit tarkastella nykyistä policyä `info`-alikomennolla.

Policy voidaan poistaa `delpolicy`-alikomennolla:

```bash
s3cmd delpolicy s3://POLICY-EXAMPLE-BUCKET
s3://POLICY-EXAMPLE-BUCKET/: Policy deleted
```