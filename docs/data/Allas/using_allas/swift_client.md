# Swift-asiakas {#the-swift-client}

Python Swift -asiakas on komentorivityökalu kohteena olevien tallennusjärjestelmien, kuten Allas, käyttöön. Jos käytät Allasta Puhtilla tai Mahtilla, kaikki tarvittavat paketit ja ohjelmistot on jo asennettu.
```text
module load allas
```
Avaa yhteys Allakseen:
```text
allas-conf
```

Yllä oleva _allas-conf_-komento pyytää CSC-salasanaasi (samaa, jota käytät kirjautuessasi CSC:n palvelimille). Se listaa projektisi Allaksessa ja pyytää sinua määrittelemään käytettävän projektin. _allas-conf_ luo ja todentaa yhteyden valittuun projektiin Allaksessa. Autentikointitiedot tallennetaan shellin muuttujiin *OS_AUTH_TOKEN* ja *OS_STORAGE_URL*, jotka ovat voimassa jopa kahdeksan tuntia. Kuitenkin voit päivittää autentikoinnin milloin tahansa ajamalla _allas-conf_ uudelleen. Ympäristömuuttujat ovat käytettävissä vain kyseiselle kirjautumiskerralle. Jos avaat toisen istunnon, sinun on autentikoitava uudelleen päästäksesi Allakseen.

Tämä luku sisältää ohjeet seuraaville toiminnoille:

| Swift-komento | Toiminto |
| :---- | :---- |
| post | Luo säilö |
| upload | Lataa objekti |
| list | Listaa objektit ja säilöt |
| download | Lataa objektit ja säilöt |
| copy | Siirrä objekti |
| delete | Poista objektit tai säilö |
| download --all | Lataa koko projekti |
| delete --all | Poista koko projekti |
| md5sum | Hanki tarkistussumma |
| stat | Näytä metadata |
| stat --meta | Lisää metadata |
| tempurl | Luo tilapäinen URL |
| post -r, -w, --read-acl | Hallitse käyttöoikeuksia |
| upload --use-slo | Lataa yli 5 GB:n tiedostot |

Voit myös asentaa ja käyttää Swiftiä CSC:n laskentaympäristön ulkopuolella. Varmista, ettei Swift-versiosi ole vanhentunut, sillä vanhemmat Swift-versiot eivät välttämättä toimi Allaksen kanssa.

## Luo säilöjä ja lataa objekteja {#create-buckets-and-upload-objects}

Luo uusi tyhjä säilö:
```text
swift post <new_bucket_name>
```

Luo uusi säilö ja lisää siihen tiedosto:
```text
swift upload <new_bucket_name> <file_name>
```

Lisää tiedosto olemassa olevaan säilöön:
```text
swift upload <old_bucket_name> <file_name>
```
**Huom:** Tämä voi laukaista varoituksen "_409 Conflict: BucketAlreadyExists_", mutta se ei välttämättä tarkoita, että lataus epäonnistui.
Jos seuraavalla rivillä näkyy tiedostonimi, tiedosto ladattiin onnistuneesti olemassa olevaan säilöön.

```text
$ swift upload my_fishbucket my_fish.jpg
Warning: failed to create container 'my_fishbucket': 409 Conflict: BucketAlreadyExists
my_fish.jpg
```

## Listaa objektit ja säilöt {#list-objects-and-buckets}

Listaa kaikki projektiin kuuluvat säilöt:
```text
$ swift list
my_fishbucket
my_bigfishes
```
Listaa säilön sisältö:
```text
$ swift list my_fishbucket
my_fish.jpg
salmon.jpg
bass.png
```

## Lataa objektit ja säilöt {#download-objects-and-buckets}

Lataa objekti:
```text
swift download <bucket_name> <file_name>
```
Jos haluat nimetä objektin uudelleen latauksen yhteydessä, voit lisätä *-o new_name* komennon loppuun:
```text
swift download <bucket_name> <file_name> -o <new_name>
```
Lataa kokonainen säilö:
```text
swift download <bucket_name>
```

## Siirrä objekteja {#move-objects}

Voit kopioida tietoa säilöstä toiseen käyttämällä komentoa `swift copy`. Alla oleva komento kopioi _file.txt_:n _bucket1_:stä _bucket2_:een.
```text
swift copy --destination /bucket2 bucket1 file.txt
```
**Huom:** Jos säilöä nimeltä _bucket2_ ei ole, Swift luo uuden säilön sillä nimellä. Kuitenkin, vaikka säilö nimeltä _bucket2_ olisi olemassa, Swift väittää luoneensa uuden, vaikka se vain kopioi tiedoston olemassa olevaan säilöön:
```text
$ swift copy --destination /other_bucket my_bigfishes bigfish.jpg
created container other_bucket
my_bigfishes/bigfish.jpg copied to /other_bucket/bigfish.jpg
$ swift list other_bucket
bigfish.jpg
other_file.txt
```

Nimeä tiedosto uudelleen kopion yhteydessä:
```text
$ swift copy --destination /new_bucket/newname.jpg my_fishbucket my_fish.jpg
created container new_bucket
my_fishbucket/my_fish.jpg copied to /new_bucket/newname.jpg
```

Lisätietoa komennosta _swift copy_ löydät [OpenStackin dokumentaatiosta](https://docs.openstack.org/python-swiftclient/latest/cli/index.html#swift-copy).

## Poista objektit ja säilöt {#remove-objects-and-buckets}

Poista objekteja ja säilöjä komennolla `swift delete`:
```text 
swift delete <bucket_name> <object_name>
```
Esimerkiksi:
```bash
$ swift delete my_fishbucket useless_fish.jpg
useless_fish.jpg
```

Toisin kuin verkkokäyttöliittymässä ja s3cmd:ssä, Swiftillä voit **poistaa koko säilön kerralla**:
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
**Huomio:** Tämä poistaa säilön pysyvästi ja data häviää. Varmista ennen tämän komennon käyttöä, ettet tarvitse dataa enää tai että sinulla on siitä kopio.

## Lataa tai poista projekteja {#download-or-delete-projects}

Lataa koko projekti:
```text
swift download --all
```

Poista koko projekti:
```text
swift delete --all
```
**Huomio:** Ole varovainen tämän komennon kanssa, sillä se poistaa koko projektin sisällön. Varmista ennen tämän komennon käyttöä, ettet tarvitse dataa enää tai että sinulla on siitä kopio.

## Pseudokansiot ja tarkistussummat {#pseudo-folders-and-checksums}

Jos haluat seurata, onko objekti muuttunut, käytä [tarkistussummaa](../terms_and_concepts.md#checksum) komennolla ```md5sum```.

Pseudokansioita voidaan käsitellä lisäämällä pseudokansion nimi tiedostonimen eteen: <i>my_pseudo_folder_name/my_file</i>

Luo pseudokansio nimeltä _pictures_ säilöön <i>my_bigfishes</i> ja lisää siihen objekti _bass.png_:
```text
$ swift upload my_bigfishes/pictures bass.png
pictures/bass.png
```

Alla oleva esimerkki lataa tiedoston nimeltä _salmon.jpg_ pseudokansioon nimeltä _fishes_ säilön _my_fishbucket_ sisällä. Tiedosto ladataan sitten.
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

## Metadatan hallinta {#managing-metadata}

Määrittele metatietoja objektille:
```text
swift post my_fishbucket my_fish.jpg --meta foo:bar
```

Näytä tiedot säilöstä:
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

Aseta säilö vain luku -tilaan koko maailmalle (tee sisältö näkyväksi URL:lla <i>a3s.fi/bucket_name/object_name</i>) oletustoiminnan (yksityinen projektille) sijaan:
```text
swift post my_fishbucket --read-acl ".r:*"
```

Lisätietoja käyttöoikeuksien hallinnasta löytyy kohdasta [Toisen projektin luku- ja kirjoitusoikeuksien antaminen säilöön](#giving-another-project-read-and-write-access-to-a-bucket).

Tarkempia tietoja tiedostosta:
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

Huomaa, että yllä oleva tiedosto ladattiin _s3cmd_-asiakkaan avulla, ja siksi siinä on lisämetatietoa _S3Cmd-Attrs_ verrattuna tiedostoon, joka on ladattu Swiftillä tai S3:lla. _ETag_ on _hash_, kun tarkastelet tiedostotietoja Pouta-hallintapaneelissa.

## Toisen projektin luku- ja kirjoitusoikeuksien antaminen säilöön {#giving-another-project-read-and-write-access-to-a-bucket}

Anna projektille _project1_ lukuoikeudet säilöön <i>my_fishbucket</i>:
```text
swift post my_fishbucket -r "project1:*"
```

Kirjoitusoikeudet voidaan antaa samalla tavalla korvaamalla _-r_ (_read_) _-w_:llä (_write_):
```text
swift post my_fishbucket -w "project1:*"
```

Merkki _*_ projektin nimen jälkeen määrittelee, että kaikki projektin jäsenet saavat oikeudet.

Vaihtoehtoisesti voit antaa luku- ja kirjoitusoikeudet vain tietyille toisen projektin jäsenille:
```text
swift post my_fishbucket -r "project2:member1"
swift post my_fishbucket -w \
   "project3:member1,project3:member2,project5:member1,project6:*"
```

**Huomio:** Jos olet myöntänyt pääsyn tietyille projekteille, jaat projektin julkiseksi ja muutat sen sitten jälleen yksityiseksi, kaikki aiemmat käyttöoikeudet poistetaan.

Jos annat _-w_ käyttöoikeuden toiselle projektille, toisen projektin jäsenet voivat ladata tiedostoja säilöösi ja poistaa tiedostojasi. Sinulla ei kuitenkaan ole pääsyä ladattuihin tiedostoihin, ennen kuin joko sinä tai lähettäjä jakaa säilön projektillesi:
```text
swift post <your_bucket_name> -r "your_project:*"
```

Esimerkiksi:
```text
swift post my_fishbucket -r "project_1234:*,project_4567:*"
```

Vaihtoehtoisesti voit asettaa projektin julkiseksi ja sitten käyttää tiedostoa.

## Yli 5 GB:n tiedostot {#files-larger-than-5-gb}

Swiftillä on yksittäisen objektin kokorajoitus 5 GiB. Jotta voisit ladata tätä suurempia tiedostoja, sinun on luotava suuri objekti, joka koostuu pienemmistä segmenteistä. Tämän saavuttamiseksi voit käyttää Swiftiä ladataksesi niin kutsutun _Static Large Object_:n (SLO).

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

Se epäonnistuu viestillä `EntityTooLarge`, joten sen sijaan:
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

Tämä luo uuden säilön:
```text
$ swift list |grep my_bigfishes
my_bigfishes
my_bigfishes_segments
```

Tässä tapauksessa kohdesäilö (my_bigfishes) sisältää vain etuobjektin, joka sisältää tiedon siitä, mitkä segmentit, tallennettuna segmenttien säilössä (my_bigfishes_segments), muodostavat tallennetun tiedoston. Etuobjektille tehdyt toiminnot heijastuvat automaattisesti segmentteihin. Yleensä käyttäjien ei tarvitse käsitellä segmenttisäilöitä lainkaan, eikä näiden säilöjen objekteja pitäisi poistaa tai muokata.

Lataa koko 6GB.zero:

```text
$ swift download my_bigfishes tmp/6GB.zero -o /tmp/6GB.zero
tmp/6GB.zero [auth 0.594s, headers 0.881s, total 74.467s, 86.969 MB/s]
$ md5sum 6GB.zero
9e6a77a2d5650b2e2a710a08e9e61a81  6GB.zero

