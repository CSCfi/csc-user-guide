# Swift-asiakasohjelma { #the-swift-client }

Python-pohjainen Swift-asiakasohjelma on komentorivityökalu objektivarastojen, kuten Allaksen, käyttöön. Jos käytät Allasta Puhtilla tai Mahtilla, kaikki tarvittavat paketit ja ohjelmistot ovat jo asennettuina.
```text
module load allas

```
Avaa yhteys Allakseen:
```text
allas-conf
```

Lisätietoja ja lisävalintoja: katso [`allas-conf`](allas-conf.md).

Tässä luvussa on ohjeet seuraaviin toimenpiteisiin:

| Swift-komento | Toiminto |
| :---- | :---- |
| post | Luo bucket |
| upload | Lataa objekti |
| list | Listaa objektit ja bucketit |
| download | Lataa objektit ja bucketit |
| copy | Siirrä objekti |
| delete | Poista objekteja tai bucket |
| download --all | Lataa koko projekti |
| delete --all | Poista koko projekti |
| md5sum | Hae tarkistussumma |
| stat | Näytä metatiedot |
| stat --meta | Lisää metatietoja |
| tempurl | Luo väliaikainen URL |
| post -r, -w, --read-acl | Hallitse käyttöoikeuksia |
| upload --use-slo | Lataa yli 5 GB:n tiedostoja |

Voit asentaa ja käyttää Swiftiä myös CSC:n laskentaympäristön ulkopuolella. Varmista, ettei Swift-versiosi ole vanhentunut, sillä vanhemmat versiot eivät välttämättä toimi Allaksen kanssa.

## Luo bucketteja ja lataa objekteja { #create-buckets-and-upload-objects }

Luo uusi tyhjä bucket:
```text
swift post <new_bucket_name>
```

Luo uusi bucket ja lisää siihen tiedosto:
```text
swift upload <new_bucket_name> <file_name>
```

Lisää tiedosto olemassa olevaan buckettiin:
```text
swift upload <old_bucket_name> <file_name>
```
**Huomautus:** Tämä voi aiheuttaa varoituksen "_409 Conflict: BucketAlreadyExists_", mutta se ei välttämättä tarkoita, että lataus epäonnistui. 
Jos seuraavalla rivillä näytetään tiedoston nimi, tiedosto ladattiin onnistuneesti olemassa olevaan bucketiin.

```text
$ swift upload my_fishbucket my_fish.jpg
Warning: failed to create container 'my_fishbucket': 409 Conflict: BucketAlreadyExists
my_fish.jpg
```

## Listaa objektit ja bucketit { #list-objects-and-buckets }

Listaa projektin kaikki bucketit:
```text
$ swift list
my_fishbucket
my_bigfishes
```
Listaa bucketin sisältö:
```text
$ swift list my_fishbucket
my_fish.jpg
salmon.jpg
bass.png
```

## Lataa objekteja ja bucketteja { #download-objects-and-buckets }

Lataa objekti:
```text
swift download <bucket_name> <file_name>
```
Jos haluat nimetä objektin uudelleen latauksen yhteydessä, lisää komennon loppuun *-o new_name*:
```text
swift download <bucket_name> <file_name> -o <new_name>
```
Lataa koko bucket:
```text
swift download <bucket_name>
```

## Siirrä objekteja { #move-objects }

Voit kopioida dataa bucketista toiseen komennolla `swift copy`. Alla oleva komento kopioi _file.txt_:n _bucket1_:stä _bucket2_:een.
```text
swift copy --destination /bucket2 bucket1 file.txt
```
**Huomautus:** Jos buckettia nimeltä _bucket2_ ei ole, Swift luo uuden bucketin kyseisellä nimellä. Jos _bucket2_ on jo olemassa, Swift silti väittää luoneensa uuden bucketin, vaikka se vain kopioi tiedoston olemassa olevaan bucketiin:
```text
$ swift copy --destination /other_bucket my_bigfishes bigfish.jpg
created container other_bucket
my_bigfishes/bigfish.jpg copied to /other_bucket/bigfish.jpg
$ swift list other_bucket
bigfish.jpg
other_file.txt
```

Nimeä tiedosto uudelleen kopioinnin yhteydessä:
```text
$ swift copy --destination /new_bucket/newname.jpg my_fishbucket my_fish.jpg
created container new_bucket
my_fishbucket/my_fish.jpg copied to /new_bucket/newname.jpg
```

Lisätietoja komennosta _swift copy_ on [OpenStack-dokumentaatiossa](https://docs.openstack.org/python-swiftclient/latest/cli/index.html#swift-copy).

## Poista objekteja ja bucketit { #remove-objects-and-buckets }

Poista objekteja ja bucketteja komennolla `swift delete`:
```text 
swift delete <bucket_name> <object_name>
```
Esimerkiksi:
```bash
$ swift delete my_fishbucket useless_fish.jpg
useless_fish.jpg
```

Toisin kuin web-asiakkaalla ja s3cmd:llä, Swiftillä voit **poistaa koko bucketin kerralla**:
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
**Huomaa:** Tämä poistaa bucketin pysyvästi ja tiedot menetetään. Varmista ennen komennon käyttöä, ettet enää tarvitse tietoja tai että sinulla on niistä kopio.

## Lataa tai poista projekteja { #download-or-delete-projects }

Lataa koko projekti:
```text
swift download --all
```

Poista koko projekti:
```text
swift delete --all
```
**Huomaa:** Ole varovainen tämän komennon kanssa, sillä se poistaa projektin koko sisällön. Varmista ennen käyttöä, ettet enää tarvitse tietoja tai että sinulla on niistä kopio.

## Pseudokansiot ja tarkistussummat { #pseudo-folders-and-checksums }

Jos haluat tarkistaa, onko objekti muuttunut, käytä [tarkistussummaa](../terms_and_concepts.md#checksum) komennolla ```md5sum```.

Pseudokansioita voi käsitellä lisäämällä pseudokansion nimen tiedostonimen eteen: <i>my_pseudo_folder_name/my_file</i>

Luo pseudokansio nimeltä _pictures_ bucketiin <i>my_bigfishes</i> ja lisää siihen objekti _bass.png_:
```text
$ swift upload my_bigfishes/pictures bass.png
pictures/bass.png
```

Alla oleva esimerkki lataa tiedoston _salmon.jpg_ pseudokansioon _fishes_ bucketissa _my_fishbucket_. Tiedosto ladataan tämän jälkeen.
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
**Huomautus:** Objektin <i>salmon.jpg</i> ja uudelleennimetyn version <i>my_renamed_salmon.jpg</i> tarkistussummat ovat samat, koska tiedosto on sama eikä ole muuttunut. 

## Metatiedon hallinta { #managing-metadata }

Määritä objektille metatietoja:
```text
swift post my_fishbucket my_fish.jpg --meta foo:bar
```

Näytä bucketin tiedot:
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

Aseta bucket kaikille luettavaksi (sisältö näkyy osoitteessa: <i>a3s.fi/bucket_name/object_name</i>) oletuksen (yksityinen projektille) sijaan:
```text
swift post my_fishbucket --read-acl ".r:*"
```

Lisätietoja käyttöoikeuksien hallinnasta kohdassa [Toisen projektin luku- ja kirjoitusoikeuksien antaminen bucketiin](#giving-another-project-read-and-write-access-to-a-bucket).

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

Huomaa, että yllä oleva tiedosto ladattiin _s3cmd_-asiakkaalla, joten siinä on lisämetatieto _S3Cmd-Attrs_ verrattuna Swiftille tai S3:lle ladattuun tiedostoon. _ETag_ vastaa _hash_-arvoa, kun tarkastelet tiedoston tietoja Pouta-hallintanäkymässä.

## Toisen projektin luku- ja kirjoitusoikeuksien antaminen bucketiin { #giving-another-project-read-and-write-access-to-a-bucket }

Anna projektille _project1_ lukuoikeus bucketiin <i>my_fishbucket</i>:
```text
swift post my_fishbucket -r "project1:*"
```

Kirjoitusoikeus annetaan vastaavasti korvaamalla _-r_ (_read_) valitsimella _-w_ (_write_):
```text
swift post my_fishbucket -w "project1:*"
```

Projektin nimen jälkeen oleva merkki _*_ tarkoittaa, että kaikki projektin jäsenet saavat oikeudet.

Vaihtoehtoisesti voit antaa luku- ja kirjoitusoikeudet vain tietyille toisen projektin jäsenille:
```text
swift post my_fishbucket -r "project2:member1"
swift post my_fishbucket -w \
   "project3:member1,project3:member2,project5:member1,project6:*"
```

**Huomaa:** Jos olet myöntänyt oikeuksia tietyille projekteille, jaetun projektin asettaminen julkiseksi ja sitten taas yksityiseksi poistaa aiemmin myönnetyt käyttöoikeudet.

Jos annat toiselle projektille _-w_-oikeuden, toisen projektin jäsenet voivat ladata tiedostoja buckettiisi ja poistaa tiedostojasi. Et kuitenkaan näe ladattuja tiedostoja ennen kuin joko sinä tai lähettäjä jaatte bucketin projektillesi:
```text
swift post <your_bucket_name> -r "your_project:*"
```

Esimerkiksi:
```text
swift post my_fishbucket -r "project_1234:*,project_4567:*"
```

Vaihtoehtoisesti voit asettaa projektin julkiseksi ja sen jälkeen käyttää tiedostoa.

## Yli 5 GB:n kokoiset tiedostot { #files-larger-than-5-gb }

Swiftissä yksittäisen objektin kokoraja on 5 GiB. Tätä suurempien tiedostojen lataamiseksi on luotava suuri objekti, joka koostuu pienemmistä segmenteistä. Tämän voi tehdä lataamalla niin sanotun _Static Large Objectin_ (SLO).

Yritä ladata suuri tiedosto:
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

Lataus epäonnistuu viestillä `EntityTooLarge`, joten tee näin:
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

Tämä luo uuden bucketin:
```text
$ swift list |grep my_bigfishes
my_bigfishes
my_bigfishes_segments
```

Tässä tapauksessa kohde-bucket (my_bigfishes) sisältää vain etuobjektin, joka sisältää tiedon siitä, mitkä segmentit, jotka on tallennettu segments-bucketiin (my_bigfishes_segments), muodostavat tallennetun tiedoston. Etuobjektiin kohdistetut toiminnot heijastuvat automaattisesti segmentteihin. Yleensä käyttäjien ei tarvitse toimia segments-buckettien kanssa lainkaan, eikä näiden buckettien sisällä olevia objekteja tulisi poistaa tai muokata.

Lataa koko 6GB.zero:

```text
$ swift download my_bigfishes tmp/6GB.zero -o /tmp/6GB.zero
tmp/6GB.zero [auth 0.594s, headers 0.881s, total 74.467s, 86.969 MB/s]
$ md5sum 6GB.zero
9e6a77a2d5650b2e2a710a08e9e61a81  6GB.zero
```