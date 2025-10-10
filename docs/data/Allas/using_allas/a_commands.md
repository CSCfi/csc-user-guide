# a-komennot, helppo ja turvallinen { #a-commands-easy-and-safe }

Allas-objektivarastoa voidaan käyttää monin tavoin ja moneen tarkoitukseen. Monissa tapauksissa Allaksen tehokas käyttö edellyttää, että käyttäjä tuntee sekä objektivarastojärjestelmän ominaisuudet että Allaksessa olevan datan hallintaan käytettävän ohjelmiston tai protokollan.

Käyttäjille, jotka haluavat yksinkertaisesti säilyttää CSC:n laskentaympäristössä olevaa dataa Allaksessa, CSC tarjoaa joukon komentoja datan hallintaan ja siirtämiseen CSC:n laskentaympäristön ja Allaksen välillä:


| a-komento | ohjeteksti | Toiminto |
| :--- | :--- | :--- |
| [a-put](#a-put)| [ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-put.md)|Lataa tiedoston tai hakemiston Allakseen |
| [a-check](#a-check) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-check.md)| Tarkistaa, löytyvätkö kaikki ne objektit Allaksesta, jotka a-putin olisi pitänyt luoda |
| [a-list](#a-list) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-list.md)| Listaa bucketit ja objektit Allaksessa |
| [a-publish](#a-publish) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-publish.md)|Lataa tiedoston Allakseen bucketiin, joka sallii julkisen internet-käytön |
| [a-flip](#a-flip) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-flip.md)|Lataa tiedoston väliaikaisesti Allakseen bucketiin, joka sallii julkisen internet-käytön |
| [a-get](#a-get) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-get.md)| Lataa Allakseen tallennettu aineisto (objekti) |
| [a-find](#a-find)|[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-find.md)|Hae ja paikanna a-putilla ladattua dataa |
| [a-delete](#a-delete) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-delete.md)| Poista objekti Allaksesta |
| [a-info](#a-info) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-info.md)| Näytä tietoja Allaksen objektista |
| [a-access](#a-access) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-access.md)| Hallitse Allaksen bucketin käyttöoikeuksia |
| a-stream |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-stream.md)|Virtauta objektin sisältö standarditulosteeseen |
| a-encrypt |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-encrypt.md)|Luo salattu kopio Allakseen ladatusta objektista |

Edellä mainittujen komentojen lisäksi on erillisiä työkaluja muihin tarkoituksiin:

 - [__allas_conf__](allas-conf.md) : Määritä ja avaa yhteys Allakseen
 - [__allas-backup__](./a_backup.md) : Luo paikallisesta datasetistä varmuuskopio Allaksen backup-repositorioon.
 - __allas-mount__ : Liitä Allaksen bucket paikallisympäristöön luettavissa olevaksi hakemistoksi.
 - __allas-health-check__ : Tarkista yli 5 GB kokoisten objektien eheys Allaksessa.
 - [__allas-dir-to-bucket__](https://github.com/CSCfi/allas-cli-utils/blob/master/help/allas-dir-to-bucket.md) : kopioi paikallinen tiedosto tai hakemisto Allakseen. Yli 5 GB tiedostoille käytetään rinnakkaisia latausprosesseja.
 
Jos käytät a-komentoja superkoneiden ulkopuolella, katso työkalujen asennusohjeet: [allas-cli-utils documentation](https://github.com/CSCfi/allas-cli-utils/blob/master/README.md).

Alla käsitellään lyhyesti a-komentojen useimmin käytettyjä ominaisuuksia. a-komentoihin lisätään ajoittain uusia ominaisuuksia, eivätkä alla olevat esimerkit välttämättä kata niitä. Käytä `--help`-optiota komennon kohtaisiin tietoihin. Esimerkiksi:
```text
a-put --help
```


# Esimerkki: Datan tallentaminen scratch-hakemistosta Allakseen { #example-saving-data-from-scratch-directory-to-allas }

## Yhteyden määrittäminen superkoneissa { #configuring-a-connection-in-supercomputers }

Jotta voit käyttää näitä työkaluja Puhtissa ja Mahtissa, lataa ensin a-komennot:
```text
module load allas
```

Määritä Allas-yhteys komennolla [`allas-conf`](allas-conf.md).

```text
allas-conf
```

## Datan kopiointi Puhtin scratch-hakemiston ja Allaksen välillä { #copying-data-between-puhti-scratch-directory-and-allas }

Datan kopiointi hakemistosta _/scratch/project_201234/dataset_3_ Allakseen:

```text
cd /scratch/project_201234
a-put dataset_3
```
Hakemiston _dataset_3_ data tallennetaan oletusbucketiin _201234-puhti-SCRATCH_ objektina: _dataset_3.tar_.
Allaksessa olevat bucketit voi listata komennolla:

```text
a-list
```
Ja bucketin 201234-puhti-SCRATCH sisällön voi listata komennolla:

```
a-list 201234-puhti-SCRATCH
```
Allakseen tallennettu hakemisto voidaan noutaa takaisin Puhtiin komennolla:

```text
a-get 201234-puhti-SCRATCH/dataset_3.tar
```


# A-komennot tarkemmin { #a-commands-in-more-detail }

## a-put lataa dataa Allakseen { #a-put-uploads-data-to-allas }<a name="a-put"></a>

`a-put`-komennolla ladataan dataa Mahtin ja Puhtin levyympäristöstä Allas-tallennusympäristöön. Komennon perussyntaksi:
```text
a-put directory_or_file
```

Oletuksena työkalu tekee seuraavaa:

1.    Varmistaa toimivan yhteyden Allas-palveluun ja määrittää projektin, johon data tallennetaan.

2.    Hakemiston tapauksessa kootaan hakemiston sisältö yhdeksi tiedostoksi `tar`-komennolla. Jos dataa on paljon, tämä ei välttämättä ole hyvä vaihtoehto; harkitse tällöin jonkin muun [Allas-asiakasohjelman](../accessing_allas.md) käyttöä, joka ei pakkaa tiedostoja.

3.    Pakattu data ladataan Allakseen `rclone`-komennolla käyttäen _Swift_-protokollaa.


Oletuksena a-put käyttää vakiobucketteja ja objektinimiä, jotka riippuvat käyttäjänimestä, projektista ja ladattavan datan sijainnista:

*    a) Puhtin /scratch -polulta data ladataan bucketiin _projectNumber-puhti-SCRATCH_
*    b) Mahtin /scratch -polulta data ladataan bucketiin _projectNumber-mahti-SCRATCH_
*    c) Puhtin /projappl -polulta data ladataan bucketiin _projectNumber-puhti-PROJAPPL_ 
*    d) Mahtin /projappl -polulta data ladataan bucketiin _projectNumber-mahti-PROJAPPL_ 
*    e) Puhtin $LOCAL_SCRATCH -polulta data ladataan bucketiin _projectNumber-puhti-LOCAL_SCRATCH_
*    f) Muissa tapauksissa data ladataan bucketiin _username-projectNumber-MISC_

Esimerkiksi käyttäjällä _kkayttaj_, joka kuuluu projektiin _12345_, HOME-hakemistossa oleva data
tallennetaan bucketiin _kkayttaj-12345-MISC_.

Jos haluat käyttää muuta kuin oletusbucketia, voit määrittää bucketin nimen optiolla _-b_ tai  
_--bucket_.

Pakattu datasetti tallennetaan yhtenä objektina. Oletuksena objektin nimi riippuu tiedoston nimestä ja sijainnista. Mahdollinen alihakemistopolku Puhtissa tai Mahtissa sisällytetään objektin nimeen. Esim. tiedosto _test_1.txt_ hakemistossa /scratch/project_2012345 Puhtissa voidaan tallentaa komennoilla:
```text
cd /scratch/project_2012345
a-put test_1.txt
```

Tällöin tiedosto tallennetaan bucketiin _2012345-puhti-SCRATCH_
objektina _test_1.txt_

Jos sinulla on toinen tiedosto nimeltä _test_1.txt_ polussa _/scratch/project_2012345/kkayttaj/project2/_,
voit tallentaa sen komennoilla
```text
cd /scratch/project_2012345/kkayttaj/project2/
a-put test_1.txt
```
tai
```text
cd /scratch/project_2012345/kkayttaj
a-put project2/test_1.txt
```
Tällöin tiedosto tallennetaan bucketiin _2012345-puhti-SCRATCH_ 
objektina _kkayttaj/project2/test_1.txt_.

Varsinaisen dataobjektin lisäksi luodaan toinen objekti, joka sisältää metadataa. Tällä metadataobjektilla on sama nimi kuin pääobjektilla, mutta laajennus *_ameta*. Tätä metadataa käyttävät muut *a-komennot*, eikä sitä normaalisti näytetä käyttäjälle, mutta jos tarkastelet bucketteja työkaluilla kuten _swift_ tai _rclone_, näet myös nämä metadataobjektit.

Jos haluat käyttää oletuksesta poikkeavaa objektinimeä, voit määrittää sen optiolla _-o_ tai  
_--object_:
```text
cd /scratch/project_2012345
a-put project2/test_1.txt -b newbucket1 -o case1.txt -c
```

Yllä oleva komento lataa tiedoston *test_1.txt* Allakseen bucketiin _newbucket1_ objektina _case1.txt.zst_.
Koska optio _-c_ on käytössä, data tallennetaan zstd-pakattuna.

Voit antaa _a-put_-komennolle useita tiedosto- tai hakemistonimiä ja käyttää *-merkkiä jokerina ladattavan datan nimissä. Huomaa, että näissä tapauksissa kukin kohde (tiedosto tai hakemisto) tallennetaan erillisenä objektina. Esimerkiksi: hakemistossa _job123_ on tiedostot _input1.txt_, _input2.txt_ ja _program.py_. Lisäksi on hakemistot _output_dir_1_ ja _output_dir_2_ .

Komento:
```text
a-put job123/output_dir_1 jobs123/input1.txt
```
lataa hakemiston _output_dir_1_ sisällön objektiksi _job123/output_dir_1.tar_ ja _input1.txt_-tiedoston objektiksi _job123/input1.txt_.

Vastaavasti komento
```text
a-put job123/output_dir*
```
lataa hakemiston _output_dir_1_ sisällön objektiksi _job123/output_dir_1.tar_ ja hakemiston _output_dir_2_ sisällön objektiksi _job123/output_dir_2.tar_. 

Latauksen aikana yli 5 GB kokoiset datasetit jaetaan automaattisesti useaan osaan ja tallennetaan useiksi objekteiksi. Tämä tehdään automaattisesti bucketissa, jonka nimi muodostetaan lisäämällä alkuperäisen bucketin nimen perään `_segments`. Esimerkiksi jos lataat suuren tiedoston bucketiin _kkayttaj-12345-MISC_, varsinainen data tallennetaan useina paloina bucketiin _kkayttaj-12345-MISC_segments_. Kohdebucketissa (_kkayttaj-12345-MISC_) on tällöin vain etuobjekti, joka sisältää tiedon siitä, mitkä segmentit muodostavat tallennetun datasetin. Etuobjektiin kohdistetut toimenpiteet heijastuvat automaattisesti segmentteihin. Yleensä käyttäjien ei tarvitse toimia segmenttibuckettien kanssa lainkaan, eikä näiden bucketien sisältöä tulisi poistaa tai muokata.


## a-check { #a-check }<a name="a-check"></a>

Tämä komento käy läpi ne Allaksen objektinimet, jotka vastaava `a-put`-komento loisi, ja tarkistaa, onko samanniminen objekti jo Allaksessa. Komennon päätarkoitus on tarjota työkalu suuren `a-put`-ajon onnistumisen tarkistamiseen. `a-check` hyväksyy samat komentorivioptiot kuin `a-put`.

Esimerkiksi, jos datasetti on ladattu komennolla:
```text
a-put job123/*
```
Lataus voidaan tarkistaa komennolla: 
```text
a-check job123/*
```
Komento _a-check_ vertaa ladattavien kohteiden nimiä Allaksessa oleviin vastaaviin objekteihin.
Tiedostot tai hakemistot, joille ei löydy kohdeobjektia Allaksesta, raportoidaan ja tallennetaan tiedostoon:
missing_bucket-name_number. Jos joitain yllä olevien esimerkkien objekteista puuttuisi, _a-check_ listaisi puuttuvat tiedostot ja hakemistot tiedostoon `missing_job123_67889` (lopun numero on satunnainen).

Tätä puuttuvien kohteiden tiedostoa voi käyttää a-putin _--input-list_-optiolla epäonnistuneen latauksen jatkamiseksi:
```text
a-put --input-list missing_job123_67889
```

Huomaa, että _a-check_ ei tarkista objektin varsinaisen sisällön oikeellisuutta. Se tarkistaa vain objektien nimet, jotka voivat olla peräisin muista lähteistä.

Tarkistamisen lisäksi _a-check_-komentoa voi käyttää a-putin "kuivan ajon" testaukseen, jotta näet etukäteen, mitkä objektit luotaisiin tai korvattaisiin ennen varsinaisen _a-put_-komennon suorittamista. 


## a-list { #a-list }<a name="a-list"></a>

a-list-komennolla näytetään Allakseen tallennettujen bucketien ja objektien nimet. a-list on suunniteltu käytettäväksi _a-putilla_ ladattujen objektien kanssa, mutta se näyttää myös muilla työkaluilla ladattuja objekteja. Se ei kuitenkaan näytä a-putin luomia _ameta_-metadataobjekteja, jotta listaukset pysyvät lyhyempinä.

### a-list-esimerkkejä { #a-list-examples }

Listaa kaikki projektiin kuuluvat bucketit:
```text
a-list
```
Näytä bucketin sisältämät objektit:
```text
a-list bucket_name
```
Kirjoittamalla osan objektin nimestä listaat osajoukon objekteja:
```text
a-list bucket_name/beginning_of_the_object
```
Yksityiskohtaisemman listauksen, joka sisältää koon ja päivämäärän, saa optiolla `-l`
```text
a-list -l 
```
Optio `-d` saa a-listin tulkitsemaan objektinimien /-merkit pseudokansioiden erottimina.
```text
a-list -d 
```

## a-publish { #a-publish }<a name="a-publish"></a>

`a-publish` kopioi tiedoston Allakseen bucketiin, jota voidaan käyttää julkisesti. Näin kuka tahansa, jolla on ladatun objektin osoite (URL), voi lukea ja ladata datan selaimella tai työkaluilla kuten _wget_ ja _curl_. 
a-publish toimii samankaltaisesti kuin a-put, mutta seuraavin erotuksin: 

1) a-publish voi ladata vain tiedostoja, ei hakemistoja. 
2) Kohdebucketin käyttöoikeudet asetetaan siten, että kuka tahansa voi lukea sen (vain luku).

Perussyntaksi:
```text
a-publish file_name
```
Oletuksena tiedosto ladataan bucketiin _username-projectNumber_-pub. Voit määrittää muita bucketin nimiä optiolla _-b_. Huomaa, että tämä komento tekee kaiken kohdebucketissa olevan datan julkisesti saataville, myös aiemmin sinne ladatun datan.

Objektin julkinen URL on:
`https://a3s.fi/username-projectNumber-pub/object_name`

_a-publish_-komennolla ladatun objektin voi poistaa Allaksesta komennolla _a-delete_.

Esimerkki _a-publish_-komennon käytöstä: ladataan dokumentti _presentation.pdf_ Allaksen oletusjulkiseen bucketiin:

<pre><b>a-publish presentation.pdf</b> 
Files to be uploaded:  presentation.pdf
Bucket: kkayttaj-1234567-pub
Processing: presentation.pdf
Checking total size of presentation.pdf. Please wait.

Uploading data to allas.
Transferred:        4.188M / 4.188 MBytes, 100%, 7.700 MBytes/s, ETA 0s
Errors:                 0
Checks:                 0 / 0, -
Transferred:            1 / 1, 100%
Elapsed time:       500ms
Confirming upload...
presentation.pdf OK

Adding metadata for uploaded presentation.pdf
presentation.pdf uploaded to kkayttaj-1234567-pub
Publick link: https://a3s.fi/kkayttaj-1234567-pub/presentation.pdf

Upload ready

</pre>

## a-flip { #a-flip }<a name="a-flip"></a>

`a-flip` on työkalu, jolla yksittäiset tiedostot voi tehdä tilapäisesti saataville internetissä. Se on tarkoitettu tilanteisiin, joissa haluat hetkellisesti jakaa tiedoston internetissä esimerkiksi kopiointia varten toiselle alustalle, jota jaat työkaverin kanssa.

a-flip kopioi tiedoston Allakseen bucketiin, jota voidaan käyttää julkisesti. Näin kuka tahansa, jolla on ladatun objektin osoite (URL), voi lukea ja ladata datan selaimella tai työkaluilla kuten _wget_ ja _curl_. 
a-flip toimii samankaltaisesti kuin a-publish, mutta seuraavin erotuksin:

1. Vain ennalta määritettyä bucketin nimeä (_username-projectNumber_-flip) voidaan käyttää.
1. Suoritettaessa se tarkistaa flip-bucketin sisällön ja poistaa yli kaksi päivää vanhat objektit.

Perussyntaksi:
```text
a-flip file_name
```
Tiedosto ladataan bucketiin _username-projectNumber_-flip. Ladatun objektin URL:
```text
https://a3s.fi/username-projectNumber-flip/file_name
```


## a-find { #a-find }<a name="a-find"></a>

Komento `a-find` listaa ja paikantaa dataa, joka on ladattu Allakseen komennolla `a-put`.

Perussyntaksi:
```text
a-find query_term
```

Hakutermiä verrataan Allakseen ladattujen tiedostojen nimiin ja alkuperäisiin polkuihin ja raportoidaan osumat (mutta ei ladata niitä).

Hakutermi tulkitaan säännöllisenä lausekkeena, jossa joillain merkeillä, esim. pisteellä (.), on erityismerkitys.
Sama regulaarilausekkeen syntaksi on käytössä esim. _grep_-, _awk_- ja _sed_-komennoissa.
Yleisimpiä erikoismerkkejä:

- Piste (**.**) vastaa mitä tahansa yksittäistä merkkiä.
- **^** merkitsee rivin alkua.
- **$** merkitsee rivin loppua.
- **[ ]** vastaa mitä tahansa hakasulkeiden sisällä olevista merkeistä. Esimerkiksi [abc] vastaa a, b tai c.
- **[^ ]** vastaa mitä tahansa merkkiä, joka ei ole hakasulkeiden sisällä.   
    Esimerkiksi [^abc] valitsee kaikki rivit, jotka sisältävät muita kuin a, b ja c.
- **\*** vastaa nolla tai useampaa edeltävää merkkiä tai lauseketta.
    `\{n,m\}` vastaa n–m esiintymää edeltävästä merkistä tai lausekkeesta.

Optiot:


- **-a**, **--all**  Oletuksena haetaan vain a-putin käyttämistä vakiobucketeista. Optio `--all` laajentaa haun koskemaan projektin kaikkia bucketteja.
- **-f**, **--files** Listaa osumia sisältävien objektien lisäksi myös objektien sisäisten tiedostojen nimet.
- **-p**,**--project _project_ID_** Hae osumat määritetyn projektin bucketeista nykyisen sijaan. 
- **-b**, **--bucket _bucket_name_** Oletuksena haetaan kaikista a-putin käyttämistä vakiobucketeista. Optiolla _-bucket_ voit rajata haun yhteen bucketiin. Käytä tätä myös, jos olet tallentanut dataa muulla kuin vakiobucketin nimellä.
- **-s**, **-silent** Tulosta vain objektien nimet ja osumien määrä. Jos käytetään optiota _-f_, tulosta samalla rivillä objektin nimi ja osuvat tiedostonimet.

## a-info näyttää tiedot ladatusta datasetistä { #a-info-shows-information-about-an-uploaded-dataset }<a name="a-info"></a>
                             
Komennolla `a-info` saat tietoa datasetistä, joka on ladattu Allakseen komennolla `a-put`.   

```text
a-info bucket/object_name
```           
Jos suoritat komennon ilman objektin nimeä, se listaa perustiedot kaikista nykyisen projektin objekteista ja yhteenvedon siitä, kuinka paljon dataa ja objekteja projektisi Allaksessa sisältää.
```text
a-info 
```   

                             
## a-get noutaa tallennetun datan { #a-get-retrieves-stored-data }<a name="a-get"></a>

Tällä työkalulla ladataan dataa, joka on ladattu Allakseen komennolla `a-put`.
Perussyntaksi:
```text
a-get object_name
```
Oletuksena objekti noudetaan, puretaan pakkauksesta ja avataan siihen tiedostoon tai hakemistoon, jota käytettiin latauksessa. Jos samanniminen hakemisto tai tiedosto on jo olemassa, se on poistettava tai määritettävä uusi kohdehakemisto optiolla `-target`.

Optiot:

- **-p**, **--project _project_ID_** Nouda data määritetyn projektin bucketeista nykyisen sijaan. 
- **-f**, **--file _file_name_** Nouda vain tietty tiedosto tai hakemisto tallennetusta datasetistä. Huom: määritä tiedoston tai hakemiston täysi polku tallennetun objektin sisällä.
- **-d** **--target_dir** <dir_name> Jos tämä optio määritetään, luodaan uusi kohdehakemisto ja data noudetaan sinne.
- **-t** **--target_file** <file_name> Määritä objektille ladattava tiedostonimi.
- **-l** **--original_location**       Nouda data alkuperäiseen sijaintiinsa hakemistorakenteessa.
- **--asis**                        Lataa objekti purkamatta tar-tiedostoja ja purkamatta zst-pakkausta.
- **--s3s3cmd**                       Käytä noudossa S3-protokollaa ja s3cmd-työkalua Swiftin ja rclonen sijaan.

Tällä hetkellä _a-get_ voi ladata vain yhden objektin kerrallaan. Jos tarvitset suuren määrän objektien lataamista, käytä silmukkaa. Esimerkiksi ladataksesi kaikki objektit bucketista _bucket_123_, voit käyttää komentoja:

```text
#tee lista objekteista
a-list bucket_123 > object_list_bucket123

#käytä listaa for-silmukassa
for ob in $(cat object_list_bucket123)
do
  a-get $ob
done  

#poista listatiedosto
rm object_list_bucket123
```


## a-delete { #a-delete }<a name="a-delete"></a>
a-delete-komennolla poistetaan dataa, joka on ladattu Allakseen a-put-komennolla.
Komennon perussyntaksi on:
<pre>a-delete object_name</pre>

Oletuksena _a-delete_ pyytää käyttäjältä vahvistuksen objektin poistolle. Tämän tarkistuksen voi ohittaa optiolla `-f`.

Jos haluat poistaa bucketin, voit käyttää optiota `--rmb`. Oletuksena _a-delete --rmb_ poistaa vain tyhjät bucketit. Jos haluat poistaa ei-tyhjän bucketin, lisää komentoosi optio `--FORCE`.

## a-access { #a-access }<a name="a-access"></a>

Oletuksena vain projektin jäsenet voivat lukea ja kirjoittaa bucketin dataa.
Projektin jäsenet voivat myöntää luku- ja kirjoitusoikeuksia bucketiin ja sen sisältämiin objekteihin muille Allas-projekteille tai tehdä bucketista julkisesti internetin kautta luettavan.

**a-access** on työkalu Allaksen bucketin käyttöoikeuksien (swift-protokolla) hallintaan.

Syntaksi 
```text
a-access +/-type project_id bucket
```
Optiot:

- **+r**,  **+read** <project_id>        Myönnä lukuoikeus bucketiin projektille.
- **+w**,  **+write** <project_id>       Myönnä kirjoitusoikeus bucketiin projektille.
- **+rw**, **+read-write**  <project_id> Myönnä luku- ja kirjoitusoikeus bucketiin projektille.
- **-r**,  **-read** <project_id>        Poista lukuoikeus bucketista.
- **-w**,  **-write** <project_id>       Poista kirjoitusoikeus bucketista.
- **-rw**, **-read-write**  <project_id> Poista luku- ja kirjoitusoikeus bucketista projektilta.
- **+p**,  **+public**                   Anna julkinen vain luku -oikeus bucketiin.
- **-p**,  **-public**                   Poista julkinen vain luku -oikeus bucketista.

Esimerkiksi salliaksesi projektin _project_2001234_ jäsenille lukuoikeuden bucketiin _my_data_bucket_, voit käyttää komentoa:
```text
a-access +r project_2001234  my_data_bucket
```
Käyttöoikeudet asetetaan vastaavasti myös bucketin _segments_-vastineeseen.

Huomaa, että bucketien listaus työkalut eivät näytä muiden projektien bucketien nimiä,
eivätkä silloinkaan, kun projektille on myönnetty luku- ja/tai kirjoitusoikeus bucketiin.

Esimerkiksi tässä tapauksessa käyttäjä, joka kuuluu projektiin _project_2001234_, 
ei näe _my_data_bucket_-buckettia komennon tuottamassa listassa:
```text  
a-list
```
mutta käyttäjä voi silti listata tämän bucketin sisällön komennolla:  
```text
a-list my_data_bucket
```
Ja ladata bucketista objekteja komennolla a-get.

a-access hallitsee käyttöoikeuksia vain projekti- ja buckettitasolla.
Käytä **swift post** -komentoa monipuolisempaan käyttöoikeuksien hallintaan.

Jos ajat _a-access_-komennon bucketille ilman muutosoptioita,
se tulostaa bucketin nykyiset asetukset.


### a-komentojen konfigurointi { #configuring-your-a-commands }

Käyttäjä voi muokata a-komentojen oletusasetuksia luomalla **.a_tools_conf**-nimisen konfiguraatiotiedoston **kotihakemistoonsa**. Tässä tiedostossa voit asettaa oletusarvoja monille toiminnoille, jotka määritetään a-put-komennon optioilla.

Esimerkiksi jos työskentelet enimmäkseen tiedostojen kanssa, jotka hyötyisivät pakkauksesta, saatat haluta käyttää _--compress_-optiota a-putin kanssa. Jos haluat tästä oletusasetuksen, voit luoda .a_tools_conf -tiedoston,
joka sisältää asetuksen:

```text
compression=1
```
Nyt komento:
```text
a-put my_data.b
```
pakkaa datan latauksen aikana (mikä ei normaalisti olisi oletus). Voit kuitenkin edelleen ohittaa pakkauksen optiolla _--nc_.

```text
a-put --nc my_data.b
```
 
Voit tarkistaa yleisimmät asetukset tästä esimerkkitiedostosta [.a_tools_conf](https://github.com/CSCfi/allas-cli-utils/edit/master/.a_tools_conf). Kopioi esimerkkitiedosto kotihakemistoosi ja poista kommenttimerkki sekä määritä haluamasi muuttujat.