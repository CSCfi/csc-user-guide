# The Swift client {#the-swift-client}

Python Swift -asiakas on komentorivityökalu objektitallennusjärjestelmien, kuten Allaksen, käyttämiseen. Jos käytät Allasta Puhtilla tai Mahtilla, kaikki tarvittavat paketit ja ohjelmistot on jo asennettu.
```text
module load allas

```
Avaa yhteys Allakseen:
```text
allas-conf
```

Yllä oleva _allas-conf_-komento kysyy CSC-salasanaasi (sama, jota käytät kirjautuessasi CSC:n palvelimille). Se listaa Allas-projektisi ja pyytää määrittelemään, mitä projektia käytetään. _allas-conf_ luo ja todentaa yhteyden valittuun projektiin Allaksessa. Todennustiedot tallennetaan shell-muuttujiin *OS_AUTH_TOKEN* ja *OS_STORAGE_URL*, jotka ovat voimassa jopa kahdeksan tuntia. Voit kuitenkin päivittää todennuksen milloin tahansa suorittamalla _allas-conf_-komennon uudelleen. Ympäristömuuttujat ovat saatavilla vain kyseisessä kirjautumissessiossa. Jos avaat uuden session, sinun täytyy todennustautua uudelleen päästäksesi Allakseen.

Tämä luku sisältää ohjeita seuraaviin toimenpiteisiin:

| Swift-komento | Toiminto |
| :---- | :---- |
| post | Luo ämpäri |
| upload | Lataa objekti |
| list | Listaa objektit ja ämpärit |
| download | Lataa objekteja ja ämpäreitä |
| copy | Siirrä objekti |
| delete | Poista objekteja tai ämpäri |
| download --all | Lataa koko projekti |
| delete --all | Poista koko projekti |
| md5sum | Hae tarkistussumma |
| stat | Näytä metadata |
| stat --meta | Lisää metadataa |
| tempurl | Luo väliaikainen URL |
| post -r, -w, --read-acl | Hallitse käyttöoikeuksia |
| upload --use-slo | Lataa tiedostoja, jotka ovat yli 5 GB |

Voit myös asentaa ja käyttää Swiftiä CSC:n laskentaympäristön ulkopuolella. Varmista, että Swiftin versiosi ei ole vanhentunut, sillä vanhemmat Swift-versiot eivät välttämättä toimi Allaksen kanssa.

## Create buckets and upload objects {#create-buckets-and-upload-objects}

Luo uusi tyhjä ämpäri:
```text
swift post <new_bucket_name>
```

Luo uusi ämpäri ja lisää siihen tiedosto:
```text
swift upload <new_bucket_name> <file_name>
```

Lisää tiedosto olemassa olevaan ämpäriin:
```text
swift upload <old_bucket_name> <file_name>
```
**Huom:** Tämä voi aiheuttaa varoituksen "_409 Conflict: BucketAlreadyExists_", mutta se ei välttämättä tarkoita, että lataus olisi epäonnistunut. 
Jos seuraava rivi näyttää tiedoston nimen, tiedosto on ladattu onnistuneesti olemassa olevaan ämpäriin.

```text
$ swift upload my_fishbucket my_fish.jpg
Warning: failed to create container 'my_fishbucket': 409 Conflict: BucketAlreadyExists
my_fish.jpg
```

## List objects and buckets {#list-objects-and-buckets}

Listaa kaikki projektin ämpärit:
```text
$ swift list
my_fishbucket
my_bigfishes
```
Listaa ämpärin sisältö:
```text
$ swift list my_fishbucket
my_fish.jpg
salmon.jpg
bass.png
```

## Download objects and buckets {#download-objects-and-buckets}

Lataa objekti:
```text
swift download <bucket_name> <file_name>
```
Jos haluat nimetä objektin uudelleen latauksen yhteydessä, voit lisätä komentoon *-o new_name*:
```text
swift download <bucket_name> <file_name> -o <new_name>
```
Lataa koko ämpäri:
```text
swift download <bucket_name>
```

## Move objects {#move-objects}

Voit kopioida tietoja ämpäristä toiseen komennolla `swift copy`. Alla oleva komento kopioi _file.txt_-tiedoston _bucket1_:stä _bucket2_:een.
```text
swift copy --destination /bucket2 bucket1 file.txt
```
**Huom:** Jos _bucket2_-nimistä ämpäriä ei ole olemassa, Swift luo uuden ämpärin sillä nimellä. Vaikka _bucket2_ olisi jo olemassa, Swift väittää luoneensa uuden, vaikka oikeasti se vain kopioi tiedoston olemassa olevaan ämpäriin:
```text
$ swift copy --destination /other_bucket my_bigfishes bigfish.jpg
created container other_bucket
my_bigfishes/bigfish.jpg copied to /other_bucket/bigfish.jpg
$ swift list other_bucket
bigfish.jpg
other_file.txt
```

Nimeä tiedosto uudelleen sitä kopioidessa:
```text
$ swift copy --destination /new_bucket/newname.jpg my_fishbucket my_fish.jpg
created container new_bucket
my_fishbucket/my_fish.jpg copied to /new_bucket/newname.jpg
```

Lisätietoja komennosta _swift copy_ löytyy [OpenStack-dokumentaatiosta](https://docs.openstack.org/python-swiftclient/latest/cli/index.html#swift-copy).

## Remove objects and buckets {#remove-objects-and-buckets}

Poista objekteja ja ämpäreitä komennolla `swift delete`:
```text 
swift delete <bucket_name> <object_name>
```
Esimerkiksi:
```bash
$ swift delete my_fishbucket useless_fish.jpg
useless_fish.jpg
```

Toisin kuin web-asiakkaalla ja s3cmd:llä, Swiftillä voit **poistaa koko ämpärin kerralla**:
```text
swift delete <my_old_bucket>
```
Esimerkiksi:
```text
$ swift delete old_fishbucket
old_fish.png
useless_salmon.jpg
too_tiny_bass.jpg
$ swift list old_fishbucket
Container u'old_fishbucket' not found
```
**Huomioithan:** Tämä poistaa ämpärin pysyvästi ja data katoaa. Varmista ennen tämän komennon käyttöä, että et enää tarvitse dataa tai että siitä on olemassa kopio.

## Download or delete projects {#download-or-delete-projects}

Lataa koko projekti:
```text
swift download --all
```

Poista koko projekti:
```text
swift delete --all
```
**Huomioithan:** Ole varovainen tämän komennon kanssa, koska se poistaa koko projektin sisällön. Varmista ennen tämän komennon käyttöä, että et enää tarvitse dataa tai että siitä on olemassa kopio.

## Pseudo folders and checksums {#pseudo-folders-and-checksums}

Jos haluat tarkistaa, onko objekti muuttunut, käytä [tarkistussummaa](../terms_and_concepts.md#checksum) komennolla ```md5sum```.

Pseudokansioita voi käsitellä lisäämällä pseudokansion nimen tiedostonimen eteen: <i>my_pseudo_folder_name/my_file</i>

Luo pseudokansio nimeltä _pictures_ ämpäriin <i>my_bigfishes</i> ja lisää siihen objekti _bass.png_:
```text
$ swift upload my_bigfishes/pictures bass.png
pictures/bass.png
```

Alla olevassa esimerkissä ladataan tiedosto nimeltä _salmon.jpg_ pseudokansioon _fishes_ ämpäriin _my_fishbucket_ ja ladataan se sieltä takaisin.
```text
$ md5sum salmon.jpg
22e44aa2b856e4df892b43c63d15138a  salmon.jpg
$ swift upload my_fishbucket/fishes salmon.jpg
fishes/salmon.jpg
$ swift list my_fishbucket
fishes/salmon.jpg
my_fish.jpg
$ swift download my_fishbucket fishes/salmon.jpg -o my_renamed_salmon.jpg
fishes/salmon.jpg [auth 0.664s, headers 0.925s, total 0.969s, 3.605 MB/s]
$ md5sum my_renamed_salmon.jpg
22e44aa2b856e4df892b43c63d15138a  my_renamed_salmon.jpg
```
**Huom:** Objektin <i>salmon.jpg</i> ja uudelleennimetyn version <i>my_renamed_salmon.jpg</i> tarkistussummat ovat samat, koska tiedosto on sama eikä ole muuttunut.

## Managing metadata {#managing-metadata}

Määritä metadataa objektille:
```text
swift post my_fishbucket my_fish.jpg --meta foo:bar
```

Näytä tietoja ämpäristä:
```text
$ swift stat my_fishbucket
                      Account: AUTH_$PROJECT_UUID
                    Container: my_fishbucket
                      Objects: 4
                        Bytes: 2162342
                     Read ACL:
                    Write ACL:
                      Sync To:
                     Sync Key:
                Accept-Ranges: bytes
                   X-Trans-Id: txUUID-cpouta-production-kaj
             X-Storage-Policy: default-placement
X-Container-Bytes-Used-Actual: 1167360
                  X-Timestamp: 1516776076.95812
```

Aseta ämpäri koko maailmalle luettavaksi (tekee sisällön näkyväksi osoitteessa: <i>a3s.fi/bucket_name/object_name</i>) oletusasetuksen (vain projektin sisäinen) sijaan:
```text
swift post my_fishbucket --read-acl ".r:*"
```

Lisätietoja käyttöoikeushallinnasta löydät kohdasta [Giving another project read and write access to a bucket](#giving-another-project-read-and-write-access-to-a-bucket).

Lisätietoja tiedostosta:
```text
$ swift stat my_fishbucket fishes/salmon.jpg
         Account: AUTH_$PROJECT_ID
       Container: my_fishbucket
          Object: fishes/salmon.jpg
    Content Type: image/jpeg
  Content Length: 63220
   Last Modified: Wed, 24 Jan 2018 10:17:03 GMT
            ETag: a38f8db198e3fea43c83c465ffb0283b
Meta S3Cmd-Attrs: atime:1516788402/ctime:1513681753/gid:$LOCALGID/gname:$LOCALGROUP/md5:a38f8db198e3fea43c83c465ffb0283b/mode:33188/mtime:1513681747/uid:$LOCALUID/uname:$LOCALUSER
   Accept-Ranges: bytes
     X-Timestamp: 1516789023.84380
      X-Trans-Id: tx0000000000000000001d6-q-q-cpouta-production-kaj
```

Huomaa, että yllä oleva tiedosto on ladattu _s3cmd-asiakkaalla_, ja siksi siinä on lisämetatietoa _S3Cmd-Attrs_ verrattuna Swifillä tai S3:lla ladattuun tiedostoon. _ETag_ on _hash_-arvo, kun tiedoston tietoja tarkastellaan Pouta-hallintapaneelista.

## Giving another project read and write access to a bucket {#giving-another-project-read-and-write-access-to-a-bucket}

Anna projektille _project1_ lukuoikeudet ämpäriin <i>my_fishbucket</i>:
```text
swift post my_fishbucket -r "project1:*"
```

Kirjoitusoikeudet voidaan antaa vastaavasti korvaamalla _-r_ (_read_) muodolla _-w_ (_write_):
```text
swift post my_fishbucket -w "project1:*"
```

Merkki _*_ projektin nimen jälkeen tarkoittaa, että kaikki projektin jäsenet saavat kyseiset oikeudet.

Vaihtoehtoisesti voit antaa luku- ja kirjoitusoikeudet vain tietyille toisen projektin jäsenille:
```text
swift post my_fishbucket -r "project2:member1"
swift post my_fishbucket -w \
   "project3:member1,project3:member2,project5:member1,project6:*"
```

**Huomioithan:** Jos olet antanut oikeudet tietyille projekteille, jaat ja perut julkisuuden, kaikki aiemmat käyttöoikeudet poistuvat.

Jos annat toiselle projektille _-w_-oikeudet, toisen projektin jäsenet voivat ladata tiedostoja ämpäriisi ja poistaa sinun tiedostojasi. Sinulla ei kuitenkaan ole oikeutta ladattuihin tiedostoihin ennen kuin joko sinä itse tai lähettäjä jaatte ämpärin sinun projektisi kanssa:
```text
swift post <your_bucket_name> -r "your_project:*"
```

Esimerkiksi:
```text
swift post my_fishbucket -r "project_1234:*,project_4567:*"
```

Vaihtoehtoisesti voit asettaa projektin julkiseksi ja päästä näin tiedostoon käsiksi.

## Files larger than 5 GB {#files-larger-than-5-gb}

Swiftissä yksittäisten objektien koko on rajoitettu 5 GiB:iin. Yli tämän suuruisia tiedostoja ladattaessa sinun tulee muodostaa suurempi objekti pienemmistä segmenteistä. Tämän saavuttamiseksi voit käyttää Swifiä ladataksesi niin sanotun _Static Large Objectin_ (SLO).

Kokeile ladata suuri tiedosto:
```text
$ md5sum /tmp/6GB.zero
9e6a77a2d5650b2e2a710a08e9e61a81  /tmp/6GB.zero
$ stat /tmp/6GB.zero
File: '/tmp/6GB.zero'
Size: 6424625152      Blocks: 12548104   IO Block: 4096   regular file
...
$ swift upload my_bigfishes /tmp/6GB.zero
Object PUT failed: https://a3s.fi:443/swift/v1/my_bigfishes/tmp/6GB.zero 400 Bad Request   EntityTooLarge
```

Se epäonnistuu viestillä `EntityTooLarge`, joten tee näin:
```text
$ swift upload my_bigfishes --use-slo --segment-size 1G /tmp/6GB.zero
tmp/6GB.zero segment 3
tmp/6GB.zero segment 5
tmp/6GB.zero segment 1
tmp/6GB.zero segment 0
tmp/6GB.zero segment 4
tmp/6GB.zero segment 2
tmp/6GB.zero
```

Tämä luo uuden ämpärin:
```text
$ swift list |grep my_bigfishes
my_bigfishes
my_bigfishes_segments
```

Tässä tapauksessa kohdeämpäri (my_bigfishes) sisältää vain etuobjektin, joka sisältää tiedot siitä, mitkä segmentit (talletettu segments-ämpäriin, my_bigfishes_segments) muodostavat tallennetun tiedoston. Etuobjektiin kohdistetut toimenpiteet heijastuvat automaattisesti myös segmentteihin. Yleensä käyttäjien ei tarvitse työskennellä segmenttiämpärien kanssa, eikä näissä ämpäreissä olevia objekteja tulisi poistaa tai muokata.

Lataa koko 6GB.zero:

```text
$ swift download my_bigfishes tmp/6GB.zero -o /tmp/6GB.zero
tmp/6GB.zero [auth 0.594s, headers 0.881s, total 74.467s, 86.969 MB/s]
$ md5sum 6GB.zero
9e6a77a2d5650b2e2a710a08e9e61a81  6GB.zero
```