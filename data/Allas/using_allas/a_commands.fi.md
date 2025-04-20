# a-komennot, helppoa ja turvallista {#a-commands-easy-and-safe}

Allas-objektitallennusjärjestelmää voidaan käyttää monin eri tavoin ja moniin tarkoituksiin. Monissa tapauksissa Allaksen tehokas hyödyntäminen edellyttää, että käyttäjä tuntee sekä objektitallennusjärjestelmän että sen ohjelmiston tai protokollan ominaisuudet, jonka avulla Allasta hallitaan.

Käyttäjille, jotka haluavat vain tallentaa dataa CSC:n laskentaympäristössä olevaan Allakseen, CSC tarjoaa joukon komentoja datan hallintaan ja siirtämiseen CSC:n laskentaympäristön ja Allaksen välillä:


| a-komento | ohjeteksti | Toiminto |
| :--- | :--- | :--- |
| [a-put](#a-put)| [ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-put.md)|Lähetä tiedosto tai hakemisto Allakseen |
| [a-check](#a-check) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-check.md)| Tarkista löytyvätkö kaikki ne objektit, jotka a-putin pitäisi olla luonut Allaksesta |
| [a-list](#a-list) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-list.md)| Listaa Allaksen säiliöt ja objektit |
| [a-publish](#a-publish) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-publish.md)|Lähetä tiedosto Allakseen säiliöön, joka sallii julkisen pääsyn internetin yli |
| [a-flip](#a-flip) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-flip.md)|Lähetä tiedosto tilapäisesti Allakseen säiliöön, joka sallii julkisen pääsyn internetin yli |
| [a-get](#a-get) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-get.md)| Lataa tallennettu tietoaineisto (objekti) Allaksesta |
| [a-find](#a-find)|[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-find.md)|Etsi ja paikanna a-putilla ladattua dataa |
| [a-delete](#a-delete) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-delete.md)| Poista objekti Allaksesta |
| [a-info](#a-info) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-info.md)| Näytä tietoja objektista Allaksessa |
| [a-access](#a-access) |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-access.md)| Hallitse Allaksen säiliön käyttöoikeuksia |
| a-stream |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-stream.md)|Virtaa objektin sisältöä standarditulosteeseen |
| a-encrypt |[ohje](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-encrypt.md)|Tee Allakseen ladatusta objektista salattu kopio |

Yllä mainittujen komentojen lisäksi on olemassa erillisiä työkaluja muihin tarkoituksiin:

 * __allas_conf__ : Yhdisty ja avaa yhteys Allakseen
 * [__allas-backup__](./a_backup.md) : Luo varmuuskopio paikallisesta aineistosta Allaksen varmuuskopiovarastoon.
 * __allas-mount__ : Liitä Allaksen säiliö paikalliseen ympäristöön vain luku -hakemistoksi.
 * __allas-health-check__ : Tarkista Allaksen yli 5 GB:n objektien eheys.
 * [__allas-dir-to-bucket__](https://github.com/CSCfi/allas-cli-utils/blob/master/help/allas-dir-to-bucket.md) : kopioi paikallinen tiedosto tai hakemisto Allakseen. Yli 5GB tiedostoille käytetään rinnakkaisia lähetysprosesseja.
 
Jos käytät a-komentoja supertietokoneiden ulkopuolella, tarkista [allas-cli-utilien dokumentaatio](https://github.com/CSCfi/allas-cli-utils/blob/master/README.md) näiden työkalujen asennustavasta.

Alla käsitellään lyhyesti a-komentojen yleisimpiä ominaisuuksia. A-komentoihin lisätään ajoittain uusia ominaisuuksia eivätkä ne välttämättä näy alla olevissa esimerkeissä. Tarkista komennon kohtaiset tiedot käyttämällä ohjevalintaa `--help`. Esimerkiksi:
```text
a-put --help
```

# Esimerkki: Datan tallennus scratch-hakemistosta Allakseen {#example-saving-data-from-scratch-directory-to-allas}

## Yhteyden avaaminen {#opening-a-connection}

Näiden työkalujen käyttämiseksi Puhti- ja Mahti-koneissa lataa ensin a-komennot:
```text
module load allas
```
Avaa sitten yhteys Allakseen:
```text
allas-conf
```
Yhteys on auki kahdeksan tuntia. Voit suorittaa _allas-conf_-komennon uudelleen milloin tahansa
jatkaaksesi yhteyden voimassaoloa kahdeksalla tunnilla tai vaihtaaksesi toiseen Allas-projektiin.

Oletuksena _allas-conf_ listaa projektit, joilla sinulla on pääsy Allakseen, mutta jos tiedät projektin nimen, voit
antaa sen myös parametrina:
```text
allas-conf project_201234
```
Huomaa, että Allas-projektin ei tarvitse olla sama kuin projektin, jota käytät Puhtissa tai Mahtissa.

Jos ajat suuria, monivaiheisia prosesseja (esim. ajotöitä), saattaa datanhallintasi viedä yli kahdeksan tuntia. Näissä tapauksissa voit lisätä valinnan `-k` _allas-conf_-komentoon.
```text
allas-conf -k
```
Tämä valinta tallentaa salasanan ympäristömuuttujaan OS_PASSWORD. A-komennot tunnistavat tämän ympäristömuuttujan ja suoritettaessa päivittävät automaattisesti voimassaolevan Allas-yhteyden.

## Datan kopiointi Puhtin scratch-hakemiston ja Allaksen välillä {#copying-data-between-puhti-scratch-directory-and-allas}

Datan kopiointi hakemistosta _/scratch/project_201234/dataset_3_ Allakseen:

```text
cd /scratch/project_201234
a-put dataset_3
```
Hakemiston _dataset_3_ data tallennetaan oletussäiliöön _201234-puhti-SCRATCH_ objektina: _dataset_3.tar_.
Saatavilla olevat datasäiliöt Allaksessa voidaan listata komennolla:

```text
a-list
```
Ja 201234-puhti-SCRATCH-säiliön sisällön saat komennolla:

```
a-list 201234-puhti-SCRATCH
```
Allakseen tallennettu hakemisto voidaan hakea takaisin Puhtiin komennolla:

```text
a-get 201234-puhti-SCRATCH/dataset_3.tar
```

# A-komennot tarkemmin {#a-commands-in-more-detail}

## a-put lataa dataa Allakseen {#a-put}

`a-put`-komentoa käytetään datan lähettämiseen Mahti- ja Puhti-levyympäristöstä Allas-tallennusympäristöön. Komennon perussyntaksi:
```text
a-put hakemisto_tai_tiedosto
```

Oletuksena työkalu suorittaa seuraavat toiminnot:

1. Varmistaa, että Allas-tallennuspalveluun on toimiva yhteys sekä
määrittää datan tallennusprojektin.

2. Hakemistotapauksissa hakemiston sisältö pakataan yhdeksi tiedostoksi
käyttämällä `tar`-komentoa.

3. Pakattu data ladataan Allakseen _rclone_-komennolla ja _Swift_-protokollalla.

Oletusarvoisesti a-put käyttää vakiosäiliötä ja objektinimiä, jotka määräytyvät käyttäjätunnuksen, projektin ja ladatun datan sijainnin mukaan:

*    a) Puhtin /scratch:ista data ladataan säiliöön _projectNumber-puhti-SCRATCH_
*    b) Mahtin /scratch:ista data ladataan säiliöön _projectNumber-mahti-SCRATCH_
*    c) Puhtin /projappl:ista data ladataan säiliöön _projectNumber-puhti-PROJAPPL_ 
*    d) Mahtin /projappl:ista data ladataan säiliöön _projectNumber-mahti-PROJAPPL_ 
*    e) Puhtin $LOCAL_SCRATCH:ista data ladataan säiliöön _projectNumber-puhti-LOCAL_SCRATCH_
*    f) Muissa tapauksissa data ladataan säiliöön _username-projectNumber-MISC_

Esimerkiksi käyttäjällä _kkayttaj_, joka kuuluu projektiin _12345_, HOME-hakemistossa sijaitseva data ladataan säiliöön _kkayttaj-12345-MISC_.

Jos haluat käyttää muuta kuin oletussäiliötä, voit määrittää säiliön nimen valinnalla _-b_ tai  
_--bucket_.

Pakatun aineiston objektin nimi määräytyy tiedoston nimen ja sijainnin mukaan. Mahdollinen alihakemiston polku Puhtissa tai Mahtissa sisällytetään objektin nimeen, esim. tiedosto _test_1.txt_ Puhtin /scratch/project_2012345:ssa voidaan tallentaa komennoilla:
```text
cd /scratch/project_2012345
a-put test_1.txt
```

Tällöin tiedosto tallennetaan säiliöön _2012345-puhti-SCRATCH_
objektiksi _test_1.txt_

Jos sinulla on toinen tiedosto nimeltä _test_1.txt_ _/scratch/project_2012345/kkayttaj/project2/_-hakemistossa,
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
Tällöin tiedosto tallennetaan säiliöön _2012345-puhti-SCRATCH_ 
objektiksi _kkayttaj/project2/test_1.txt_.

Varsinaisen dataobjektin lisäksi luodaan toinen objekti, joka sisältää metadataa. Tällä metatietokohteella on
sama nimi kuin pääobjektilla, lisättynä pääteellä *_ameta*. Tätä metatiedostoa käyttävät muut *a-komennot*, ja sitä ei normaalisti näytetä käyttäjälle, mutta jos tutkit säiliöitä esimerkiksi _swift_- tai _rclone_-työkaluilla, näet myös nämä metatieto-objektit.

Jos haluat käyttää oletusobjektinimestä poikkeavaa nimeä, voit määrittää sen valinnalla _-o_ tai  
_--object_:
```text
cd /scratch/project_2012345
a-put project2/test_1.txt -b newbucket1 -o case1.txt -c
```

Yllä oleva komento lataa tiedoston *test_1.txt* Allakseen säiliöön _newbucket1_ objektina _case1.txt.zst_.
Koska valinta _-c_ on käytössä, data tallennetaan zstd-pakatussa muodossa.

Voit antaa useita tiedosto- tai hakemistonimiä _a-put_-komennolle ja käyttää *-merkkiä jokerimerkkinä. Huomioi, että näissä tapauksissa jokainen kohde (tiedosto tai hakemisto) tallennetaan omaksi objektikseen. Esimerkiksi, jos hakemisto _job123_ sisältää tiedostot _input1.txt_, _input2.txt_ ja _program.py_, sekä hakemistot _output_dir_1_ ja _output_dir_2_.

Komento:
```text
a-put job123/output_dir_1 jobs123/input1.txt
```
lataa _output_dir_1_-hakemiston sisällön objektiksi _job123/output_dir_1.tar_ ja _input1.txt_-tiedoston objektiksi _job123/input1.txt_.

Vastaavasti komento
```text
a-put job123/output_dir*
```
lataa _output_dir_1_-hakemiston objektiksi _job123/output_dir_1.tar_ ja _output_dir_2_-hakemiston objektiksi _job123/output_dir_2.tar_.

Lähetyksen yhteydessä yli 5 GB kokoiset aineistot jaetaan automaattisesti useaan objektiin. Tämä tehdään automaattisesti säiliöön, jonka nimeen lisätään _segments-pääte alkuperäisen säiliön nimeen. Esimerkiksi, jos lataat suuren tiedoston säiliöön _kkayttaj-12345-MISC_, varsinainen data tallennetaan useana osana säiliöön _kkayttaj-12345-MISC_segments_. Kohdesäiliö (_kkayttaj-12345-MISC_) sisältää vain ns. etuobjektin, joka sisältää tiedot segmenteistä. Etuobjektille tehtävät operaatiot heijastuvat automaattisesti segmentteihin. Yleensä käyttäjän ei tarvitse käsitellä segmenttien säiliöitä ollenkaan eikä niitä tulisi poistaa tai muokata.

## a-check {#a-check}

Tämä komento käy läpi Allaksen objekti nimet, jotka vastaava `a-put`-komento loisi, ja tarkistaa, löytyykö samalla nimellä jo objekti Allaksesta. Komennon pääasiallinen tarkoitus on tarkistaa, onnistuiko suuri `a-put`-komento. `a-check` hyväksyy samat komentorivivalinnat kuin `a-put`.

Jos aineisto ladataan komennolla:
```text
a-put job123/*
```
Voit tarkistaa latauksen komennolla: 
```text
a-check job123/*
```
_a-check_ vertaa ladattavien nimien vastaavuutta Allaksen objekteihin.
Ne tiedostot tai hakemistot, joita ei löydy kohdeobjektina Allaksesta, raportoidaan ja tallennetaan tiedostoon: missing_bucket-name_number. Jos jokin objekti yllä olevissa esimerkeissä puuttuisi, a-check listaisi puuttuvat tiedostot ja hakemistot tiedostossa `missing_job123_67889` (loppunumero on satunnainen).

Tätä puuttuvien tiedostojen listaa voidaan käyttää _a-put_-komennon --input-list-vaihtoehdon kanssa epäonnistuneen latauksen jatkamiseksi:
```text
a-put --input-list missing_job123_67889
```

Huomioi, että _a-check_ ei tarkista varsinaisen objektin sisällön oikeellisuutta. Se tarkistaa vain objektien nimet, jotka voivat olla muualtakin kuin omasta latauksestasi.

Tarkistuksen lisäksi _a-check_-komentoa voidaan käyttää tekemään "dry-run"-testin _a-put_-komennolle, jotta näet, mitä objekteja luodaan tai korvataan ennen varsinaista _a-put_-ajoa. 

## a-list {#a-list}

a-list-komennolla voit näyttää Allakseen tallennettujen säiliöiden ja objektien nimet. a-list on suunniteltu käytettäväksi a-putilla ladattuihin objekteihin, mutta näyttää myös muut aputyökaluilla ladatut objektit. Se ei kuitenkaan näytä a-putin luomia _ameta_-metatiedostotiedostoja, jotta listaukset olisivat lyhyempiä.

### a-list esimerkkejä {#a-list-examples}

Listaa kaikki projektiin kuuluvat säiliöt:
```text
a-list
```
Näytä säiliön sisältämät objektit:
```text
a-list säiliön_nimi
```
Objektin nimen osalla saat listattua vain tietyt objektit:
```text
a-list säiliön_nimi/objektin_alku
```
Tarkemman listauksen, joka sisältää koot ja päivämäärät, saat valinnalla `-l`:
```text
a-list -l 
```
Valinta `-d` tulkitsee /-merkit objektinimissä hakemistorakenteiden erottimeksi:
```text
a-list -d 
```

## a-publish {#a-publish}

`a-publish` kopioi tiedoston Allakseen säiliöön, johon on julkinen pääsy. Tällöin kuka tahansa, jolla on datan osoite (URL), voi lukea ja ladata aineiston verkkoselaimella tai työkaluilla kuten _wget_ ja _curl_.
a-publish toimii pitkälti kuten a-put, mutta joillakin eroilla: 

1) a-publish voi ladata vain tiedostoja, ei hakemistoja.
2) Kohdesäiliön käyttöoikeudet muutetaan julkisesti saataville, vain luku -tilassa.

Perussyntaksi:
```text
a-publish tiedoston_nimi
```
Oletuksena tiedosto ladataan säiliöön _username-projectNumber_-pub. Voit määrittää toisen säiliön nimen valinnalla _-b_. Huomaa, että tämä komento tekee koko kohdesäiliön datasta julkisesti saatavilla, mukaan lukien jo aiemmin sinne ladatut tiedostot.

Julkisen datan objektille muodostuva URL on:
`https://a3s.fi/username-projectNumber-pub/object_name`

_a-publish_-komennolla ladattu objekti voidaan poistaa Allaksesta _a-delete_-komennolla.

Esimerkki _a-publish_-komennon käytöstä dokumentin _presentation.pdf_ lähettämisessä oletusjulkiseen säiliöön:

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

## a-flip {#a-flip}

`a-flip` on työkalu, jolla voi tehdä yksittäisen tiedoston väliaikaisesti saataville internetiin. Se on tarkoitettu tilanteisiin, joissa haluat hetkeksi julkaista tiedoston, esim. siirtääksesi sen toiselle alustalle työkaverin kanssa.

a-flip kopioi tiedoston Allakseen säiliöön, johon on julkinen pääsy. Tällöin kuka tahansa, jolla on datan osoite (URL), voi lukea ja ladata tiedoston verkkoselaimella tai työkaluilla kuten _wget_ ja _curl_. 
a-flip toimii pitkälti kuten a-publish, mutta eroaa siinä:

1. Vain ennalta määriteltyä säiliön nimeä (_username-projectNumber_-flip) voidaan käyttää.
1. Suorittaessaan tarkistaa flip-säiliön sisällön ja poistaa yli kaksi päivää vanhat objektit.

Perussyntaksi:
```text
a-flip tiedoston_nimi
```
Tiedosto ladataan säiliöön _username-projectNumber_-flip. Ladatun objektin URL on:
```text
https://a3s.fi/username-projectNumber-flip/file_name
```

## a-find {#a-find}

`a-find`-komento listaa ja paikantaa Allakseen `a-put`:lla ladattua dataa.

Perussyntaksi:
```text
a-find hakuehto
```

Hakuehto vertaillaan Allakseen ladattujen tiedostojen nimiin ja alkuperäisiin polkuihin,
ja vastaavat objektit listataan (mutta niitä ei ladata).

Hakusana tulkitaan säännöllisenä lausekkeena, jossa tietyillä merkeillä, kuten pisteellä (.), on erityismerkitys.
Tämä ontäysin sama kuin esimerkiksi _grep_-, _awk_- ja _sed_ -komennoissa.
Yleisimmät erikoismerkit:

- Piste (**.**) tarkoittaa mitä tahansa yksittäistä merkkiä.
- **^** merkitsee rivin alkua.
- **$** merkitsee rivin loppua.
- **[ ]** osuu mihin tahansa hakasulkeissa olevaan merkkiin. Esim. [abc] osuu a:han, b:hen tai c:hen.
- **[^ ]** osuu mihin tahansa muuhun kuin hakasulkeissa olevaan merkkiin.   
    Esimerkiksi [^abc] valitsee rivit, joissa on muita merkkejä kuin a, b tai c.
- ** * ** tarkoittaa nolla tai useampia edellisen merkin tai lausekkeen esiintymiä.
    `\{n,m\}` osuu n–m kertaa edelliseen merkkiin tai lausekkeeseen.

Valinnat:


- **-a**, **--all**  Oletuksena haetaan vain vakiosäiliöt, joita a-put käyttää. Valinnalla `--all` mukaan otetaan kaikki projektin säiliöt.
- **-f**, **--files** Listaa vastaavien objektien sisällä olevat tiedostojen nimet objektinimien lisäksi.
- **-p**,**--project _project_ID_** Hae annetun projektin säiliöistä nykyisen projektin sijasta. 
- **-b**, **--bucket _bucket_name_** Oletuksena haetaan vain kaikki a-putin käyttämät vakiosäiliöt. Valinnalla _-bucket_ voi määrittää yhden säiliön haulle. Käytä tätä myös kun olet tallentanut dataa epästandardiin säiliöön.
- **-s**, **-silent** Tulosta vain objekinimet ja osumien määrä. Jos _-f_ on käytössä, tulostaa riville objektinimen ja vastaavat tiedostot.

## a-info näyttää tiedot ladatusta aineistosta {#a-info-shows-information-about-an-uploaded-dataset}
                             
Komennolla `a-info` saat tietoja Allakseen `a-put`-komennolla ladatusta aineistosta.   

```text
a-info bucket/object_name
```           
Ilman objektin nimeä komento listaa kaikkien projektisi objektien perustiedot sekä kokonaistilastot siitä paljonko dataa ja objekteja projektillasi on Allaksessa.
```text
a-info 
```   

## a-get palauttaa tallennetun datan {#a-get}

Tällä työkalulla ladataan Allas-palveluun a-put-komennolla ladattua dataa.
Perussyntaksi:
```text
a-get objektin_nimi
```
Oletuksena objekti ladataan, puretaan ja sijoitetaan siihen hakemistoon tai tiedostoihin, joista se on ladattu. Jos samalla nimellä oleva hakemisto tai tiedosto on jo olemassa, se on ensin poistettava tai palautettavalle datalle on määriteltävä uusi kohdehakemisto valinnalla `-target`.

Valinnat:

- **-p**, **--project _project_ID_** Hae dataa määritetyn projektin säiliöistä nykyisen projektin sijasta. 
- **-f**, **--file _file_name_** Palauta vain tietty tiedosto tai hakemisto aineistosta. **Huom:** Anna palautettavan tiedoston/hakemiston koko polku aineiston sisällä.
- **-d** **--target_dir** <dir_name> Jos tämä on määritetty, luodaan uusi kohdehakemisto ja data palautetaan sinne.
- **-t** **--target_file** <file_name> Määritä ladattavalle objektille tiedostonimeksi tämä nimi.
- **-l** **--original_location**       Palauta data hakemistorakenteessaan alkuperäiseen paikkaan.
- **--asis**                        Lataa objekti purkamatta taria tai zst-pakkausta.
- **--s3cmd**                       Käytä S3-protokollaa ja s3cmd-työkalua tiedonsiirtoon Swift-protokollan/rclonen sijaan.

Tällä hetkellä _a-get_ pystyy lataamaan vain yhden objektin kerrallaan. Jos haluat ladata monta objektia, voit käyttää silmukoita. Esimerkiksi kaikki objektit säiliössä _bucket_123_ voidaan ladata komennoilla:

```text
#luo listan objekteista
a-list bucket_123 > object_list_bucket123

#käytä listaa silmukassa
for ob in $(cat object_list_bucket123)
do
  a-get $ob
done  

#poista objektien lista
rm object_list_bucket123
```

## a-delete {#a-delete}
a-delete poistaa datan, joka on ladattu Allakseen a-put-komennolla.
Komennon perussyntaksi:
<pre>a-delete objektin_nimi</pre>

Oletuksena _a-delete_ pyytää käyttäjältä varmistuksen objektin poistamisesta. Varmistuksen voi ohittaa valinnalla `-f`.

Säiliön poistamiseksi käytä valintaa `--rmb`. Oletuksena _a-delete --rmb_ poistaa vain tyhjät säiliöt. Jos haluat poistaa ei-tyhjän säiliön, lisää komennolle valinta `--FORCE`.

## a-access {#a-access}

Oletuksena vain projektin jäsenet voivat lukea ja kirjoittaa säiliön dataa.
Projektin jäsenet voivat antaa luku- tai kirjoitusoikeuden säiliöön ja sen sisältöön muille Allas-projekteille tai sallia julkisen pääsyn internetiin.

**a-access** on työkalu kori- (bucket-) oikeuksien hallintaan Allaksessa (swift-protokolla).

Syntaksi 
```text
a-access +/-type project_id bucket
```
Valinnat:

- **+r**,  **+read** <project_id>        Anna projektin jäsenille lukuoikeus säiliöön.
- **+w**,  **+write** <project_id>       Anna projektin jäsenille kirjoitusoikeus säiliöön.
- **+rw**, **+read-write**  <project_id> Anna projektin jäsenille luku- ja kirjoitusoikeus säiliöön.
- **-r**,  **-read** <project_id>        Poista lukuoikeus säiliöltä.
- **-w**,  **-write** <project_id>       Poista kirjoitusoikeus säiliöltä.
- **-rw**, **-read-write**  <project_id> Poista luku- ja kirjoitusoikeus projektilta säiliössä.
- **+p**,  **+public**                   Aseta säiliö julkiseksi vain luku -oikeudella.
- **-p**,  **-public**                   Poista säiliöltä julkinen vain luku -oikeus.

Esimerkiksi, jotta projektin _project_2001234_ jäsenet saavat lukuoikeuden säiliöön _my_data_bucket_, käytä komentoa:
```text
a-access +r project_2001234  my_data_bucket
```
Oikeudet asetetaan vastaavasti myös segmentti-säiliölle.

Huomioi, että säiliöiden listauskomennot eivät näytä muiden projektien säiliöiden nimiä,
vaikka projektille olisi annettu luku- tai kirjoitusoikeuksia.

Tässä tapauksessa käyttäjä, joka kuuluu projektiin _project_2001234_, 
ei näe _my_data_bucket_-säiliötä komennolla:
```text  
a-list
```
mutta voi silti listata säiliön sisällön komennolla:  
```text
a-list my_data_bucket
```
ja ladata objektin a-getillä.

a-access hallitsee oikeuksia vain projektin ja säiliön tasolla.
Monimutkaisempaan oikeuksien hallintaan käytä **swift post** -komentoa.

Jos suoritat _a-access_-komennon ilman valintoja, se näyttää säiliön nykyiset asetukset.

### A-komentojen asetukset {#configuring-your-a-commands}

Käyttäjä voi muokata a-komentojen oletusasetuksia tekemällä **.a_tools_conf** -nimisen konfiguraatiotiedoston **kotihakemistoonsa**. Tällä tiedostolla voi asettaa monien toimintojen oletusarvot, jotka muutoin annettaisiin a-put-komennon valinnoilla.

Jos tyypillisesti työskentelet datan kanssa, jossa pakkauksesta on hyötyä, voit käyttää _--compress_-valintaa a-putissa. Jos haluat tästä oletuksen, tee .a_tools_conf -tiedosto, jossa on asetus:

```text
compression=1
```
Nyt komento:
```text
a-put my_data.b
```
pakkaa datan siirron yhteydessä (mikä ei ole oletus). Voit kuitenkin ohittaa pakkauksen valinnalla _--nc_.

```text
a-put --nc my_data.b
```
 
Yleisimmät asetukset löydät tästä esimerkkitiedostosta [.a_tools_conf](https://github.com/CSCfi/allas-cli-utils/edit/master/.a_tools_conf). Kopioi esimerkkitiedosto kotihakemistoosi ja poista kommenttimerkit sekä määritä haluamasi muuttujat.