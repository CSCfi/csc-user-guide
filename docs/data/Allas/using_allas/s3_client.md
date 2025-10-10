# S3-asiakasohjelma { #the-s3-client }

Tässä luvussa kuvataan, miten Allas-objektitallennuspalvelua käytetään komentorivityökalulla **s3cmd**. Tämä asiakasohjelma käyttää _S3_-protokollaa, joka poikkeaa _Swift_-protokollasta, jota käytetään esimerkeissä [Rclone](./rclone.md), [swift](./swift_client.md) ja [a-commands](./a_commands.md). Tavallisesti S3:lla lähetettyä dataa voi käyttää myös Swift-protokollan kautta. Huomaa kuitenkin, että yli 5 Gt:n kokoisia tiedostoja, jotka on lähetetty Allakseen Swiftillä, ei voi ladata S3-protokollalla.

Käyttäjän näkökulmasta yksi merkittävimmistä eroista S3:n ja Swiftin välillä on, että Swift-pohjaiset yhteydet ovat kerrallaan voimassa kahdeksan tuntia, kun taas S3-yhteys pysyy pysyvästi auki. Pysyvä yhteys on monin tavoin kätevä, mutta siinä on tietoturvanäkökulma: jos CSC-tunnuksesi vaarantuu, myös objektitallennustilasi vaarantuu.

Käytä versiota 2.0.2 tai uudempaa.

Komennon `s3cmd` syntaksi:
```text
s3cmd -options command parameters
```

Yleisimmät _s3cmd_-komennot:

| s3cmd command | Toiminto |
| :---- | :---- |
| mb | Luo bucket |
| put | Lähetä objekti |
| ls | Listaa objektit ja bucketit |
| get | Lataa objekteja ja bucketteja |
| cp | Siirrä objekti |
| del | Poista objekteja tai bucketteja |
| md5sum | Hae tarkistussumma |
| info | Näytä metadata |
| signurl | Luo tilapäinen URL |
| put -P | Tee objektista julkinen |
| setacl --acl-grant | Hallitse käyttöoikeuksia |


Yllä oleva taulukko listaa vain keskeisimmät _s3cmd_-komennot. Kattavamman listan löydät [s3cmd-käyttöohjeesta](https://s3tools.org/usage) tai kirjoittamalla:
```text
s3cmd -h
```
## s3cmd:n käytön aloittaminen { #getting-started-with-s3cmd }

Jos käytät Allasta Puhtissa tai Mahtissa, kaikki vaadittavat paketit ja ohjelmistot on jo asennettu. Tässä tapauksessa voit ohittaa tämän luvun ja siirtyä kohtaan [Configuring S3 connection in supercomputers](#configuring-s3-connection).

Jotta voit määrittää s3cmd-yhteyden, ympäristöösi on oltava asennettuna _OpenStack_ ja _s3cmd_.

**OpenStack s3cmd -asennus:**

Fedora/RHEL-johdannaiset:
```text
sudo yum update
sudo yum install python3
sudo pip3 install python-openstackclient
sudo yum install s3cmd
```
Debian-johdannaiset:
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

Katso myös ylävirran dokumentaatio: [http://s3tools.org/download](http://s3tools.org/download) ja [http://s3tools.org/usage](http://s3tools.org/usage).

Asenna lisäksi [`allas-conf`](allas-conf.md#allas-conf-installation).

## S3-yhteyden määrittäminen { #configuring-s3-connection }

Jotta voit käyttää _s3cmd_-ohjelmaa Puhtissa ja Mahtissa, sinun on ensin määritettävä yhteys:
```text
module load allas
allas-conf --mode S3
```

Paikallisella tietokoneella:
```text
source allas_conf --mode S3 --user your-csc-username
```

Lisätietoja ja muita valintoja: [`allas-conf`](allas-conf.md).


## Luo bucketteja ja lähetä objekteja { #create-buckets-and-upload-objects }

Luo uusi bucket:
```text
s3cmd mb s3://my_bucket
```

Lähetä tiedosto bucketiin:
```text
s3cmd put my_file s3://my_bucket
```

## Listaa objektit ja bucketit { #list-objects-and-buckets }

Listaa kaikki projektin bucketit:
```text
s3cmd ls
```

List all objects in a bucket:du
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

Tarkista projektisi objektitallennuksen käyttö:
```text
s3cmd du -H
```

## Lataa objekteja ja bucketteja { #download-objects-and-buckets }

Lataa objekti:
```text
s3cmd get s3://my_bucket/my_file new_file_name
```
Parametri *new_file_name* on valinnainen. Se määrittää ladattavan tiedoston uuden nimen.

Komennolla `md5sum` voit varmistaa, ettei tiedosto ole muuttunut tai vioittunut:
<pre>
$ <b>md5sum my_file new_file_name</b>
   39bcb6992e461b269b95b3bda303addf  my_file
   39bcb6992e461b269b95b3bda303addf  new_file_name
</pre>
Yllä olevassa esimerkissä tarkistussummat täsmäävät alkuperäisen ja ladatun tiedoston välillä.

Lataa kokonainen bucket:
```text
s3cmd get -r s3://my_bucket/
```

## Siirrä objekteja { #move-objects }

Kopioi objekti toiseen bucketiin. Huomaa, että näitä komentoja tulisi käyttää vain objekteille, jotka on lähetetty Allakseen S3-protokollalla:
```text
s3cmd cp s3://sourcebucket/objectname s3://destinationbucket
```

Esimerkiksi:
<pre>
$ <b>s3cmd cp s3://bigbucket/bigfish s3://my-new-bucket</b>
remote copy: 's3://bigbucket/bigfish' -> 's3://my-new-bucket/bigfish'
</pre>

Nimeä tiedosto uudelleen kopioinnin yhteydessä:
<pre>
$ <b>s3cmd cp s3://bigbucket/bigfish s3://my-new-bucket/newname</b>
remote copy: 's3://bigbucket/bigfish' -> 's3://my-new-bucket/newname'
</pre>

## Poista objekteja ja bucketteja { #delete-objects-and-buckets }

Poista objekti:
```text
s3cmd del s3://my_bucket/my_file
```

Poista bucket:
```text
s3cmd rb s3://my_bucket
```
**Huom:** Voit poistaa vain tyhjiä bucketteja.

## s3cmd ja julkiset objektit { #s3cmd-and-public-objects }

Tässä esimerkissä pseudo-kansiossa _fishes_ oleva objekti _salmon.jpg_ tehdään julkiseksi:
<pre>
$ <b>s3cmd put fishes/salmon.jpg s3://my_fishbucket/fishes/salmon.jpg -P</b>
Public URL of the object is: https://a3s.fi/my_fishbucket/fishes/salmon.jpg
</pre>


## Lukuoikeuden antaminen toiseen projektiin bucketille { #giving-another-project-read-access-to-a-bucket }

Voit hallita käyttöoikeuksia komennolla `s3cmd setacl`. Tämä komento vaatii sen projektin UUID:n (_universally unique identifier_), jolle haluat myöntää pääsyn. Projektin jäsenet voivat tarkistaa projektinsa ID:n <a href="https://pouta.csc.fi/dashboard/identity/" target="_blank">https://pouta.csc.fi/dashboard/identity/</a> -sivulta tai komennolla ```openstack project show```. Esimerkiksi Puhtissa ja Mahtissa:

```text
module load allas
allas-conf -k --mode s3cmd
openstack project show $OS_PROJECT_NAME
```

_s3cmd_-työkalulla luku- ja kirjoitusoikeuksia voidaan hallita sekä bucketeille että objekteille:

Seuraava komento antaa UUID:lla _3d5b0ae8e724b439a4cd16d1290_ olevalle projektille lukuoikeuden _my_fishbucket_-bucketiin, mutta ei sen sisällä oleviin objekteihin:
```text
s3cmd setacl --acl-grant=read:3d5b0ae8e724b439a4cd16d1290 s3://my_fishbucket
```
Vastaavasti seuraava komento antaa kirjoitusoikeuden vain yhteen objektiin:
```text
s3cmd setacl --acl-grant=write:3d5b0ae8e724b439a4cd16d1290 s3://my_fishbucket/bigfish
```
Jos haluat muokata bucketin kaikkien objektien käyttöoikeuksia, voit lisätä komentoihin valinnan `--recursive`:
```text
s3cmd setacl --recursive --acl-grant=read:3d5b0ae8e724b439a4cd16d1290 s3://my_fishbucket
```

Voit tarkistaa käyttöoikeudet komennolla _s3cmd info_:
<pre>
$ <b>s3cmd info s3://my_fishbucket|grep -i acl</b>
   ACL:       other_project_uuid: READ
   ACL:       my_project_uuid: FULL_CONTROL
</pre>

Valinnalla _--acl-revoke_ voidaan poistaa luku- tai kirjoitusoikeus:
```text
s3cmd setacl --recursive --acl-revoke=read:$other_project_uuid s3://my_fishbucket
```

Jaettuja objekteja ja bucketteja voi käyttää sekä S3- että Swift-pohjaisilla työkaluilla. Huomaa kuitenkin, että listauskomennot näyttävät vain oman projektisi omistamat bucketit. Jaettujen buckettien ja objektien kohdalla sinun on tiedettävä buckettien nimet voidaksesi käyttää niitä.

Yllä olevan esimerkin tapauksessa projektiin _3d5b0ae8e724b439a4cd16d1290_ kuuluva käyttäjä ei näe _my_fishbucket_-buckettia, kun se on jaettu, komennolla:

```text
s3cmd ls
```
Kuitenkin hän voi listata bucketin sisällön komennolla:
```text
s3cmd ls s3://my_fishbucket
```
Poutan web-käyttöliittymässä käyttäjä voi siirtyä jaettuun bucketiin määrittämällä bucketin nimen URL-osoitteessa. Siirry johonkin projektisi bucketiin ja korvaa URL-osoitteen lopussa oleva bucketin nimi jaetun bucketin nimellä:
```
https://pouta.csc.fi/dashboard/project/containers/container/my_fishbucket
```

## Käyttöesimerkki { #use-example }

Tässä esimerkissä tallennamme yksinkertaisen aineiston Allakseen s3cmd:llä.

Luo ensin uusi bucket. Komento `s3cmd ls` paljastaa, että objektitallennus on aluksi tyhjä. Käytä sitten komentoa `s3cmd mb` luodaksesi _fish-bucket_-nimisen bucketin.

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
On suositeltavaa koota talletettava data suuremmiksi kokonaisuuksiksi ja pakata se ennen järjestelmään lataamista.

Tässä esimerkissä tallennamme Bowtie2-indeksit ja seeprakalojen (danio rerio) genomin fish-bucketiin. Komento `ls -lh` näyttää, että indeksitiedostot ovat saatavilla nykyisessä hakemistossa:

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

Data kootaan ja pakataan yhdeksi tiedostoksi `tar`-komennolla:
```text
tar zcf zebrafish.tgz Danio_rerio*
```

Tuloksena olevan tiedoston koko on noin 2 Gt. Pakattu tiedosto voidaan lähettää fish-bucketiin komennolla `s3cmd put`:
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

2 Gt:n datan lataaminen kestää jonkin aikaa. Nouda ladattu tiedosto:
```text
s3cmd get s3://fish-bucket/zebrafish.tgz
```

Oletuksena tähän bucketiin pääsevät vain projektin jäsenet. Komennolla `s3cmd setacl` voit kuitenkin tehdä tiedoston julkisesti saataville.

Tee ensin fish-bucket julkiseksi:
```text
s3cmd setacl --acl-public s3://fish-bucket
```

Tee sitten seeprakalojen genomitiedosto julkiseksi:
```text
s3cmd setacl --acl-public s3://fish-bucket/zebrafish.tgz
```

Tiedoston URL-osoitteen syntaksi:
```text
https://a3s.fi/bucket_name/object_name
```

Tässä tapauksessa tiedosto olisi saatavilla linkistä
_https://a3s.fi/fish-bucket/zebrafish.tgz_


## Objektien tilapäinen julkaisu allekirjoitetuilla URL-osoitteilla { #publishing-objects-temporarily-with-signed-urls }

Komennolla _s3cmd signurl_ Allaksessa oleva objekti voidaan julkaista tilapäisesti URL-osoitteella, joka sisältää käyttöä rajaavan turvatunnisteen.

Edellisessä esimerkissä objekti _s3://fish-bucket/zebrafish.tgz_ tehtiin pysyvästi saataville yksinkertaisella staattisella URL-osoitteella. Komennolla _signurl_ sama objekti voidaan jakaa turvallisemmin ja vain rajatuksi ajaksi. Esimerkiksi komento:

```text
s3cmd signurl s3://fish-bucket/zebrafish.tgz +3600
```
tulostaa URL-osoitteen, joka on voimassa 3600 s (1 h). Tässä tapauksessa komennon tuottama URL-osoite näyttäisi jotakuinkin tältä:
```text
https://fish-bucket.a3s.fi/zebrafish.tgz?AWSAccessKeyId=78e6021a086d52f092b3b2b23bfd7a67&Expires=1599835116&Signature=OLyyCY14s%2F0HxKOOd108mldINyE%3D
```

## Objektien elinkaaren käyttöönotto { #setting-up-an-object-lifecycle }

Objektien automaattista poistamista/vanhentamista varten bucketiin voidaan määrittää elinkaarikäytäntö (lifecycle policy). Bucketin objektit käsitellään elinkaarikäytännön mukaisesti, jos ne täyttävät asetetut ehdot. Ehdot voidaan kohdistaa avaimen etuliitteeseen (prefix) ja/tai objektin tageihin. Elinkaarikäytäntö sopii erityisen hyvin tilanteisiin, joissa data halutaan poistaa “ylläpidollisena” toimenpiteenä tietyn ajan kuluttua.

!!! warning
    Ennen elinkaarikäytännön määrittämistä tarkista organisaatioltasi/tiimiltäsi, että se vastaa projektin datan säilytyskäytäntöjä. (Oikeudelliset tai sääntelyyn liittyvät rajoitteet).

Seuraavassa elinkaarikäytännössä on kaksi sääntöä. Nimetään tiedosto `mypolicy.xml`.

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

Vaihtoehtoisesti käytännöt voidaan määrittää käyttämällä `prefix`-arvoa, joka vastaa “kansiota”. Molempia menetelmiä voidaan myös yhdistää käyttämällä `<And>`-tagia.

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

Asetetaan elinkaarikäytäntö bucketiimme komennolla `setlifecycle`:

```bash
s3cmd setlifecycle mypolicy.xml s3://MY_BUCKET
```

Voimme varmistaa nykyisen käytännön komennolla `getlifecycle`:

```bash
s3cmd getlifecycle s3://MY_BUCKET
```

Bucketin (tai objektin) tietoja voi tarkastella `info`-komennolla:

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

Jotta saat objektisi elinkaarikäytännön piiriin, voit käyttää tageja ja/tai prefixejä.

* Tagaus tehdään lisäämällä otsake muodossa `x-amz-tagging:KEY=VALUE`.
* Prefixiä voi ajatella “kansiona”.

Tarkastellaan seuraavia tapauksia:

```bash
# Should be removed in 24 hours per rule ID: 1-days-expiration
s3cmd --add-header=x-amz-tagging:days=1 put MY_FILE_01.tar.gz s3://MY_BUCKET/
s3cmd --add-header=x-amz-tagging:days=1 put MY_FILE_02.tar.gz s3://MY_BUCKET/gone-in-one-day/

# Should be removed in 30 days per rule ID: 30-days-expiration
s3cmd --add-header=x-amz-tagging:days=30 put MY_FILE_03.tar.gz s3://MY_BUCKET/

# Should be removed in 30 days per rule ID: Daily
s3cmd put MY_FILE_04.tar.gz s3://MY_BUCKET/daily/

# Should be removed in 365 days per rule ID: Weekly
s3cmd put MY_FILE_05.tar.gz s3://MY_BUCKET/weekly/
```

Lisälukemista elinkaaren määrittämisestä:

* [RedHat Developer -opas Ceph-tallennukselle](https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/3/html-single/developer_guide/index#s3-api-bucket-lifecycle).
* [Creating an intelligent object storage system with Ceph’s Object Lifecycle Management](https://shopnpaz.medium.com/creating-an-intelligent-object-storage-system-with-cephs-object-lifecycle-management-112e2e46d490)
* [Multiple lifecycles - s3cmd](https://stackoverflow.com/questions/49615977/multiple-lifecycles-s3cmd)
* Yllä mainittuun liittyvä kirjoitus: [cloud.blog.csc.fi](http://cloud.blog.csc.fi/2019/02/cpouta-cloud-object-storage-service-has.html)

## Rajoita bucketin pääsyä tiettyihin IP-osoitteisiin { #limit-bucket-access-to-specific-ip-addresses }

Voit rajoittaa pääsyn bucketiin tiettyihin IP-osoitteisiin määrittämällä käytännön (policy).

!!! Warning
    Muista olla estämättä omaa pääsyäsi bucketiin. Jos teet niin, et voi käyttää buckettia tai korjata käytäntöä.

Seuraavassa IP-käytännön esimerkissä sallitaan pääsy bucketiin POLICY-EXAMPLE-BUCKET IP-aliverkosta 86.50.164.0/24. Nimetään käytäntötiedosto `myippolicy.json`.

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

Asetetaan tämä IP-käytäntö bucketiimme komennolla `setpolicy`:

```bash
s3cmd setpolicy myippolicy.json s3://POLICY-EXAMPLE-BUCKET
```

Nykyisen käytännön voi katsoa `info`-komennolla.

Nykyisen käytännön voi poistaa `delpolicy`-komennolla:

```bash
s3cmd delpolicy s3://POLICY-EXAMPLE-BUCKET
s3://POLICY-EXAMPLE-BUCKET/: Policy deleted
```