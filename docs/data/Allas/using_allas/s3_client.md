# S3-asiakas {#the-s3-client}

Tässä luvussa kuvataan, kuinka käyttää Allas-objektien tallennuspalvelua **s3cmd** komentorivikomentojen avulla. Tämä asiakasohjelma käyttää _S3_-protokollaa, joka eroaa _Swift_-protokollasta, jota käytetään [Rclone](./rclone.md), [swift](./swift_client.md) ja [a-commands](./a_commands.md) esimerkeissä. Yleensä S3:lla ladatut tiedot ovat käytettävissä myös swift-protokollan kanssa. Kuitenkin, yli 5 GB tiedostot, jotka on ladattu swiftillä Allakseen, eivät ole ladattavissa S3-protokollan avulla.

Käyttäjän näkökulmasta yksi suurimmista eroista S3- ja Swift-protokollien välillä on se, että Swift-pohjaiset yhteydet pysyvät voimassa kahdeksan tuntia kerrallaan, kun taas S3:ssa yhteys pysyy pysyvästi avoimena. Pysyvä yhteys on käytännöllinen monin tavoin, mutta sillä on myös turvallisuusnäkökulma: jos CSC-tilisi vaarantuu, vaarantuu myös objektien tallennustila.

`s3cmd`-komennon syntaksi:
```text
s3cmd -options command parameters
```

Yleisimmät _s3cmd_ komennot:

| s3cmd komento | Toiminto |
| :---- | :---- |
| mb | Luo ämpäri (bucket) |
| put | Lataa objekti |
| ls | Listaa objektit ja ämpärit |
| get | Lataa objektit ja ämpärit |
| cp | Siirrä objekti |
| del | Poista objektit tai ämpärit |
| md5sum | Hanki tarkistussumma |
| info | Näytä metadata |
| signurl | Luo väliaikainen URL |
| put -P | Aseta objekti julkiseksi |
| setacl --acl-grant | Hallitse käyttöoikeuksia |

Yllä oleva taulukko listaa vain olennaisimmat _s3cmd_ komennot. Täydentävämmän listan saamiseksi, vieraile [s3cmd käyttöohje](https://s3tools.org/usage) tai kirjoita:
```text
s3cmd -h
```

## S3cmd:n aloittaminen {#getting-started-with-s3cmd}

Jos käytät Allasta Puhtissa tai Mahtissa, kaikki tarvittavat paketit ja ohjelmistot on jo asennettu. Tässä tapauksessa voit ohittaa tämän luvun ja siirtyä osioon [S3-yhteyden konfigurointi supertietokoneissa](#configuring-s3-connection-in-supercomputers).

Jotta voit konfiguroida s3cmd-yhteyden, sinulla tulee olla _OpenStack_ ja _s3cmd_ asennettuna ympäristöösi.

**OpenStack s3cmd asennus:**

Fedora/RHEL johdannaiset:
```text
sudo yum update
sudo yum install python3
sudo pip3 install python-openstackclient
sudo yum install s3cmd
```
Debian johdannaiset:
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

Viittaa [http://s3tools.org/download](http://s3tools.org/download) ja [http://s3tools.org/usage](http://s3tools.org/usage) saadaksesi lisätietoa.

**S3-yhteyden konfigurointi paikallisessa tietokoneessa**

Kun olet asentanut _OpenStack_ ja _s3cmd_ ympäristöösi, voit ladata [allas_conf](https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/allas_conf) skriptin konfiguroidaksesi S3-yhteyden Allaksen projektiisi.
```text
wget https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/allas_conf
source allas_conf --mode S3 --user your-csc-username
```
Huomaa, että sinun tulisi käyttää `--user` -asetusta määritelläksesi CSC-käyttäjänimesi. Konfigurointikomento kysyy ensin CSC-salasanasi ja sitten valitsemaan Allas-projektin. Sen jälkeen työkalu luo avain-tiedoston S3-yhteyttä varten ja tallentaa sen oletussijaintiin (_.s3cfg_ kotikansiossa).

## S3-yhteyden konfigurointi supertietokoneissa {#configuring-s3-connection-in-supercomputers}

Jotta voit käyttää _s3cmd_ Puhtissa ja Mahtissa, sinun on ensin konfiguroitava yhteys:
```text
module load allas
allas-conf --mode S3
```
Konfigurointiprosessi kysyy ensin CSC-salasanasi. Sitten se listaa Allas-projektisi ja pyytää valitsemaan käytettävän projektin. Konfigurointitiedot tallennetaan tiedostoon _$HOME/.s3cfg_. Tämä konfiguraatio tarvitsee määritellä vain kerran. Tulevaisuudessa _s3cmd_ käyttää automaattisesti objektien tallennusyhteyttä, joka on kuvailtu _.s3cfg_ tiedostossa. Jos haluat vaihtaa Allas-projektia, jota _s3cmd_ käyttää, sinun täytyy suorittaa konfigurointikomento uudelleen.

Voit käyttää _.s3cfg_ -tiedostoon tallennettuja S3-todennustietoja myös muissa palveluissa. Voit tarkistaa parhaillaan käytössä olevat _access key_ ja _secret_key_ komennolla:
```
grep key $HOME/.s3cfg
```
Kun käytät näitä avaimia muissa palveluissa, sinun tulisi varmistaa, että avaimet pysyvät aina yksityisinä. Kuka tahansa, joka pääsee käsiksi näihin kahteen avaimeen, voi käyttää ja muokata kaikkea projektin dataa Allaksessa.

Tarvittaessa voit deaktivoida S3-avainparin komennolla:
```
allas-conf --s3remove
```

## Luo ämpärit ja lataa objekteja {#create-buckets-and-upload-objects}

Luo uusi ämpäri:
```text
s3cmd mb s3://my_bucket
```

Lataa tiedosto ämpäriin:
```text
s3cmd put my_file s3://my_bucket
```

## Listaa objektit ja ämpärit {#list-objects-and-buckets}

Listaa kaikki ämpärit projektissa:
```text
s3cmd ls
```

Listaa kaikki objektit ämpärissä:
```text
s3cmd ls s3://my_bucket
```

Näytä tietoja ämpäristä:
```text
s3cmd info s3://my_bucket
```

Näytä tietoja objekteista:
```text
s3cmd info s3://my_bucket/my_file
```

## Lataa objektit ja ämpärit {#download-objects-and-buckets}

Lataa objekti:
```text
s3cmd get s3://my_bucket/my_file new_file_name
```
Paramentteri *new_file_name* on vapaaehtoinen. Se määrittää ladatulle tiedostolle uuden nimen.

Komennolla `md5sum` voit tarkistaa, ettei tiedosto ole muuttunut tai vioittunut:
<pre>
$ <b>md5sum my_file new_file_name</b>
   39bcb6992e461b269b95b3bda303addf  my_file
   39bcb6992e461b269b95b3bda303addf  new_file_name
</pre>
Yllä olevassa esimerkissä tarkistussummat täsmäävät alkuperäisen ja ladatun tiedoston välillä.

Lataa koko ämpäri:
```text
s3cmd get -r s3://my_bucket/
```

## Siirrä objekteja {#move-objects}

Kopioi objekti toiseen ämpäriin. Huomaa, että näitä komentoja tulisi käyttää vain objekteihin, jotka on ladattu Allakseen S3-protokollalla:
```text
s3cmd cp s3://sourcebucket/objectname s3://destinationbucket
```

Esimerkiksi:
<pre>
$ <b>s3cmd cp s3://bigbucket/bigfish s3://my-new-bucket</b>
kaukokopio: 's3://bigbucket/bigfish' -> 's3://my-new-bucket/bigfish'
</pre>

Nimeä tiedosto uudelleen kopioidessasi sitä:
<pre>
$ <b>s3cmd cp s3://bigbucket/bigfish s3://my-new-bucket/newname</b>
kaukokopio: 's3://bigbucket/bigfish' -> 's3://my-new-bucket/newname'
</pre>

## Poista objektit ja ämpärit {#delete-objects-and-buckets}

Poista objekti:
```text
s3cmd del s3://my_bucket/my_file
```

Poista ämpäri:
```text
s3cmd rb s3://my_bucket
```
**Huom:** Voit poistaa vain tyhjät ämpärit.

## s3cmd ja julkiset objektit {#s3cmd-and-public-objects}

Tässä esimerkissä objekti _salmon.jpg_ pseudo-kansiossa _kalat_ tehdään julkiseksi:
<pre>
$ <b>s3cmd put fishes/salmon.jpg s3://my_fishbucket/fishes/salmon.jpg -P</b>
Objektin julkinen URL on: https://a3s.fi/my_fishbucket/fishes/salmon.jpg
</pre>

## Toisen projektin lukuoikeuden antaminen ämpäriin {#giving-another-project-read-access-to-a-bucket}

Voit hallita käyttöoikeuksia komennolla `s3cmd setacl`. Tämä komento vaatii projektin _UUID_ (universaali yksilöivä tunniste), jolle haluat myöntää käyttöoikeuden. Projektin jäsenet voivat tarkistaa projektinsa tunnuksen osoitteessa <a href="https://pouta.csc.fi/dashboard/identity/" target="_blank">https://pouta.csc.fi/dashboard/identity/</a> tai käyttämällä komentoa ```openstack project show```. Esimerkiksi Puhtilla ja Mahtilla:

```text
module load allas
allas-conf -k --mode s3cmd
openstack project show $OS_PROJECT_NAME
```

S3cmd:n tapauksessa luku- ja kirjoitusoikeuksia voidaan hallita sekä kauhoille että objekteille:

Seuraava komento antaa projektin UUID:llä _3d5b0ae8e724b439a4cd16d1290_ lukuoikeuden _my_fishbucket_ ämpäriin, mutta ei sen sisällä oleviin objekteihin:
```text
s3cmd setacl --acl-grant=read:3d5b0ae8e724b439a4cd16d1290 s3://my_fishbucket
```
Samalla tavalla seuraava komento antaa kirjoitusoikeuden vain yhdelle objektille:
```text
s3cmd setacl --acl-grant=write:3d5b0ae8e724b439a4cd16d1290 s3://my_fishbucket/bigfish
```
Jos haluat muuttaa kaikkien ämpärin objektien käyttöoikeuksia, voit lisätä komennolle `--recursive`-asetuksen:
```text
s3cmd setacl --recursive --acl-grant=read:3d5b0ae8e724b439a4cd16d1290 s3://my_fishbucket
```

Voit tarkistaa käyttöoikeudet _s3cmd info_ -komennolla:
<pre>
$ <b>s3cmd info s3://my_fishbucket|grep -i acl</b>
   ACL:       other_project_uuid: READ
   ACL:       my_project_uuid: FULL_CONTROL
</pre>

Vaihtoehto _--acl-revoke_ voidaan käyttää lukemis- tai kirjoitusoikeuden poistamiseen:
```text
s3cmd setacl --recursive --acl-revoke=read:$other_project_uuid s3://my_fishbucket
```

Jaetut objektit ja ämpärit voidaan käyttää sekä S3- että Swift-pohjaisilla työkaluilla. Huomaa kuitenkin, että listauskomennot näyttävät vain projektisi omistamat ämpärit. Jaettujen ämpärien ja objektien tapauksessa sinun on tiedettävä ämpärien nimet voidaksesi käyttää niitä.

Yllä olevassa esimerkissä käyttäjä projektista _3d5b0ae8e724b439a4cd16d1290_ ei näe _my_fishbucket_, kun se on jaettu, komennolla:
```text
s3cmd ls
```
Hän voi kuitenkin listata ämpärin sisällön komennolla:
```text
s3cmd ls s3://my_fishbucket
```
Poutan verkkokäyttöliittymässä käyttäjä voi siirtyä jaettuun ämpäriin määrittämällä ämpärin nimen URL-osoitteessa. Siirry projektiin kuuluvan ämpärin ja korvaa URL-osoitteen lopussa oleva ämpärin nimi jaetun ämpärin nimellä:
```
https://pouta.csc.fi/dashboard/project/containers/container/my_fishbucket
```

## Käyttöesimerkki {#use-example}

Tässä esimerkissä tallennamme yksinkertaisen tietoaineiston Allakseen käyttäen s3cmd.

Ensiksi luo uusi ämpäri. Komento `s3cmd ls` paljastaa, että objektien tallennustila on alussa tyhjä. Käytä sitten komentoa `s3cmd mb` luodaksesi uusi ämpäri nimeltään _fish-bucket_.

<pre>
$ <b>s3cmd ls</b>
ls

$ <b>s3cmd mb s3://fish-bucket</b>
mb s3://fish-bucket/
Ämpäri 's3://fish-bucket/' luotu

$ <b>s3cmd ls</b>
ls
2018-03-12 13:01  s3://fish-bucket
</pre>
On suositeltavaa kerätä tallennettava aineisto suuremmiksi yksiköiksi ja pakata se ennen järjestelmään lataamista.

Tässä esimerkissä tallennamme Bowtie2-indeksit ja seeprakalagenomin (danio rerio) kalojen ämpäriin. `ls -lh`-komennon suorittaminen näyttää, että indeksitiedostot ovat saatavilla nykyisessä hakemistossa:

<pre>$ <b>ls -lh</b>
yhteensä 3.2G
-rw------- 1 kkayttaj csc 440M Mar 12 13:41 Danio_rerio.1.bt2
-rw------- 1 kkayttaj csc 327M Mar 12 13:41 Danio_rerio.2.bt2
-rw------- 1 kkayttaj csc 217K Mar 12 13:20 Danio_rerio.3.bt2
-rw------- 1 kkayttaj csc 327M Mar 12 13:20 Danio_rerio.4.bt2
-rw------- 1 kkayttaj csc 1.3G Mar 12 13:13 Danio_rerio.GRCz10.dna.toplevel.fa
-rw------- 1 kkayttaj csc 440M Mar 12 14:03 Danio_rerio.rev.1.bt2
-rw------- 1 kkayttaj csc 327M Mar 12 14:03 Danio_rerio.rev.2.bt2
-rw------- 1 kkayttaj csc 599K Mar 12 13:13 log
</pre>

Kerää ja pakkaa aineisto yhdeksi tiedostoksi `tar`-komentoa käyttäen:
```text
tar zcf zebrafish.tgz Danio_rerio*
```

Lopputiedoston koko on noin 2 GB. Pakattu tiedosto voidaan ladata kalojen ämpäriin käyttämällä komentoa `s3cmd put`:
<pre>
$ <b>ls -lh zebrafish.tgz</b>
-rw------- 1 kkayttaj csc 9.3G Mar 12 15:23 zebrafish.tgz

$ <b>s3cmd put zebrafish.tgz s3://fish-bucket</b>
put zebrafish.tgz s3://fish-bucket
lataus: 'zebrafish.tgz' -> 's3://fish-bucket/zebrafish.tgz'  [1 of 1]
 2081306836 of 2081306836   100% in   39s    50.16 MB/s  valmis

$ <b>s3cmd ls s3://fish-bucket</b>
ls s3://fish-bucket
2019-10-01 12:11 9982519261   s3://fish-bucket/zebrafish.tgz
</pre>

2 GB datan lataaminen vie aikaa. Nouda ladattu tiedosto:
```text
s3cmd get s3://fish-bucket/zebrafish.tgz
```

Oletusarvoisesti tähän ämpäriin pääsevät vain projektin jäsenet. Kuitenkin käyttämällä komentoa `s3cmd setacl`, voit tehdä tiedoston julkisesti saatavilla.

Ensiksi tee kalojen ämpäristä julkinen:
```text
s3cmd setacl --acl-public s3://fish-bucket
```

Sitten tee seeprakalagenomi tiedosto julkiseksi:
```text
s3cmd setacl --acl-public s3://fish-bucket/zebrafish.tgz
```

Tiedoston URL-osoitteen syntaksi:
```text
https://a3s.fi/bucket_name/object_name
```

Tässä tapauksessa tiedosto olisi saatavilla linkin avulla
_https://a3s.fi/fish-bucket/zebrafish.tgz_

## Objekteiden julkaiseminen tilapäisesti allekirjoitetuilla URL-osoitteilla {#publishing-objects-temporarily-with-signed-urls}

Komennolla _s3cmd signurl_ voidaan Allaksessa oleva objekti julkaista tilapäisesti URL-osoitteella, joka sisältää turvallisuutta lisäävän pääsytunnuksen.

Edellisessä esimerkissä objekti _s3://fish-bucket/zebrafish.tgz_ tehtiin pysyvästi saataville yksinkertaisen staattisen URL-osoitteen kautta. Komennolla _signurl_ voidaan sama objekti jakaa turvallisemmin ja vain rajalliseksi ajaksi. Esimerkiksi komento:
```text
s3cmd signurl s3://fish-bucket/zebrafish.tgz +3600
```
tulostaisi URL-osoitteen, joka säilyy voimassa 3600 s (1 h). Tässä tapauksessa yllä olevan komennon tuottama URL-osoite näyttäisi suunnilleen tältä:
```text
https://fish-bucket.a3s.fi/zebrafish.tgz?AWSAccessKeyId=78e6021a086d52f092b3b2b23bfd7a67&Expires=1599835116&Signature=OLyyCY14s%2F0HxKOOd108mldINyE%3D
```

## Objektien elinkaaren määrittäminen {#setting-up-an-object-lifecycle}

Jotta sinulla olisi mahdollisuus poistaa/vanhentaa objekteja automaattisesti, voit määrittää elinkaarikäytännön Allas-ämpärille. Ämpärissä olevia objekteja käsitellään elinkaarikäytännön mukaisesti, jos vastaavuusehdot täyttyvät. Vastaavuusehdot voidaan asettaa objektin etuliitteelle ja/tai tunnisteille. Elinkaarikäytäntö soveltuu erityisesti tapauksiin, joissa tiedot on poistettava "ylläpitoa" varten tietyin aikavälein.

!!! varoitus
    Ennen kuin määrität elinkaarikäytännön, varmista osastoltasi/tiimiltäsi, että se vastaa projektissa olevan datan säilytyskäytäntöä. (Lailliset tai säädökselliset rajoitukset).

Seuraavassa elinkaarikäytännössä meillä on kaksi sääntöä. Nimetään se `mypolicy.xml`.

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

Vaihtoehtoisesti politiikat voidaan asettaa `prefix`-asetuksella, jota voidaan pitää vastaavana kuin `kansio`. Molempia menetelmiä voidaan myös yhdistää käyttäen `<And>`-tunnistetta.

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

Asettaaksemme tämän elinkaarikäytännön ämpäriimme käytämme `setlifecycle`-alakomento:
```bash
s3cmd setlifecycle mypolicy.xml s3://MY_BUCKET
```

Voimme tarkistaa nykyisen käytännön `getlifecycle`-alakomennolla:
```bash
s3cmd getlifecycle s3://MY_BUCKET
```

Tarkista ämpäri (tai objekti) `info`-alakomennolla:
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

Jotta objectit voidaan laittaa elinkaarikäytännön alaisiksi, voit hyödyntää tunnisteita ja/tai etuliitteitä.

* Tunnisteiden lisääminen tapahtuu antamalla otsikko muodossa `x-amz-tagging:KEY=VALUE`.
* Etuliitettä voidaan ajatella "kansiona".

Katsotaanpa seuraavia tapauksia:

```bash
# Pitäisi poistaa 24 tunnin sisällä sääntömäärityksen ID: 1-days-expiration mukaisesti
s3cmd --add-header=x-amz-tagging:days=1 put MY_FILE_01.tar.gz s3://MY_BUCKET/
s3cmd --add-header=x-amz-tagging:days=1 put MY_FILE_02.tar.gz s3://MY_BUCKET/gone-in-one-day/

# Pitäisi poistaa 30 päivän sisällä sääntömäärityksen ID: 30-days-expiration mukaisesti
s3cmd --add-header=x-amz-tagging:days=30 put MY_FILE_03.tar.gz s3://MY_BUCKET/

# Pitäisi poistaa 30 päivän sisällä sääntömäärityksen ID: Daily mukaisesti
s3cmd put MY_FILE_04.tar.gz s3://MY_BUCKET/daily/

# Pitäisi poistaa 365 päivän sisällä sääntömäärityksen ID: Weekly mukaisesti
s3cmd put MY_FILE_05.tar.gz s3://MY_BUCKET/weekly/
```

Muita viitteitä elinkaaren asettamiseksi:

* [RedHat developer guide Ceph storage](https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/3/html-single/developer_guide/index#s3-api-bucket-lifecycle).
* [Creating an intelligent object storage system with Ceph’s Object Lifecycle Management](https://shopnpaz.medium.com/creating-an-intelligent-object-storage-system-with-cephs-object-lifecycle-management-112e2e46d490)
* [Multiple lifecycles - s3cmd](https://stackoverflow.com/questions/49615977/multiple-lifecycles-s3cmd)
* Yllä olevalle yllättävä merkintä [cloud.blog.csc.fi](http://cloud.blog.csc.fi/2019/02/cpouta-cloud-object-storage-service-has.html)

## Rajoita ämpärin pääsyä tiettyihin IP-osoitteisiin {#limit-bucket-access-to-specific-ip-addresses}

Voit rajoittaa pääsyn ämpäriin tiettyihin IP-osoitteisiin määrittelemällä käytännön.

!!! Varoitus
    Muista olla estämättä omaa pääsyäsi ämpäriin, et voi käyttää ämpäriä tai korjata käytäntöä, jos teet niin.

Seuraavassa IP-käytäntöesimerkissä sallimme pääsyn ämpäriin POLICY-EXAMPLE-BUCKET IP-aliverkosta 86.50.164.0/24. Nimetään käytäntötiedosto `myippolicy.json`.

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

Asettaaksemme tämän IP-käytännön ämpäriimme käytämme `setpolicy`-alakomento:

```bash
s3cmd setpolicy myippolicy.json s3://POLICY-EXAMPLE-BUCKET
```

Nykyisen käytännön voi tarkistaa `info`-alakomennolla.

Voimme poistaa nykyisen käytännön `delpolicy`-alakomennolla:

```bash
s3cmd delpolicy s3://POLICY-EXAMPLE-BUCKET
s3://POLICY-EXAMPLE-BUCKET/: Policy deleted
