
# a-komennot, helppo ja turvallinen

Allas-objektivarastojärjestelmää voidaan käyttää monin tavoin ja moniin tarkoituksiin. Usein Allaksen tehokas käyttö vaatii, että käyttäjä tuntee sekä objektivarastojärjestelmän että sen ohjelmiston tai protokollan ominaisuudet, joita käytetään Allaksen datanhallintaan.

Käyttäjille, jotka haluavat yksinkertaisesti käyttää Allasta CSC:n laskentaympäristössä olevan datan tallentamiseen, CSC tarjoaa joukon komentoja datan hallintaan ja siirtämiseen CSC:n laskentaympäristön ja Allaksen välillä:

| a-komento | ohjeteksti | Toiminto |
| :--- | :--- | :--- |
| [a-put](#a-put)| [help](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-put.md)|Lataa tiedosto tai hakemisto Allakseen |
| [a-check](#a-check) |[help](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-check.md)| Tarkista, löytyvätkö kaikki objektit, jotka a-put -komennon pitäisi luoda, Allaksesta |
| [a-list](#a-list) |[help](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-list.md)| Listaa ämpärit ja objektit Allaksessa |
| [a-publish](#a-publish) |[help](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-publish.md)|Lataa tiedosto Allakseen ämpäriin, joka sallii julkisen pääsyn internetin kautta |
| [a-flip](#a-flip) |[help](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-flip.md)|Lataa tiedosto tilapäisesti Allakseen ämpäriin, joka sallii julkisen pääsyn internetin kautta |
| [a-get](#a-get) |[help](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-get.md)| Lataa tallennettu datasetti (objekti) Allaksesta |
| [a-find](#a-find)|[help](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-find.md)|Etsi ja paikanna *a-put*:lla ladattua dataa |
| [a-delete](#a-delete) |[help](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-delete.md)| Poista objekti Allaksesta |
| [a-info](#a-info) |[help](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-info.md)| Näytä tietoja Allaksen objektista |
| [a-access](#a-access) |[help](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-access.md)| Hallitse ämpärin käyttöoikeuksia Allaksessa |
| a-stream |[help](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-stream.md)|Striimaa objektin sisältö standardilähtöön |
| a-encrypt |[help](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-encrypt.md)|Tee salattu kopio Allakseen ladatusta objektista |

Lisäksi on erillisiä työkaluja muita tarkoituksia varten:

 * __allas_conf__ : Määritä ja avaa yhteys Allakseen
 * [__allas-backup__](./a_backup.md) : Luo varmuuskopio paikallisesta datasetistä Allaksen varmuusvarastoon.
 * __allas-mount__ : Liitä Allaksen ämpäri käytettäväksi vain luku -hakemistona paikallisympäristössä.
 * __allas-health-check__ : Tarkista yli 5 GB objekti

eista Allaksen eheys.
 * [__allas-dir-to-bucket__](https://github.com/CSCfi/allas-cli-utils/blob/master/help/allas-dir-to-bucket.md) : kopioi paikallinen tiedosto tai hakemisto Allakseen. Rinnakkaisia latausprosesseja käytetään yli 5GB kokoisille tiedostoille.
 
Jos käytät a-komentoja superkoneiden ulkopuolella, tarkista [allas-cli-utils dokumentointi](https://github.com/CSCfi/allas-cli-utils/blob/master/README.md) näiden työkalujen asentamisesta.

Alla keskustellaan lyhyesti a-komentojen yleisimmin käytetyistä ominaisuuksista. Uusia ominaisuuksia lisätään a-komentoihin silloin tällöin, eikä niitä välttämättä käsitellä alla olevissa esimerkeissä. Käytä ohje-vaihtoehtoa `--help` tarkistaaksesi komennon erityistiedot. Esimerkiksi:
```text
a-put --help
```

# Esimerkki: Datan tallentaminen työtilahakemistosta Allakseen

## Yhteyden avaaminen

Jotta voit käyttää näitä työkaluja Puhtissa ja Mahtissa, lataa ensin a-komennot:
```text
module load allas
```
Avaa sitten yhteys Allakseen:
```text
allas-conf
```
Yhteys pysyy auki kahdeksan tuntia. Voit ajaa _allas-conf_ -komennon milloin tahansa uudelleen
jatkaaksesi yhteyden voimassaoloa uudestaan kahdeksan tuntia tai siirtyäksesi toiseen Allas 
projektiin. 

Oletuksena, _allas-conf_ listaa projektisi, joilla on pääsy Allakseen, mutta jos tiedät projektin nimen,
voit myös antaa sen argumenttina:
```text
allas-conf project_201234
```
Huomaa, että Allas-projektin ei tarvitse olla sama kuin projekti, jota käytät Puhtissa tai Mahtissa.

Jos suoritat suuria, monivaiheisia prosesseja (esim. erätöitä), voi olla, että datanhallintaputkesi kestää yli kahdeksan tuntia. Näissä tapauksissa voit lisätä -k -vaihtoehdon `allas-conf` komentoon.
```text
allas-conf -k
```
Kun tämä asetus on käytössä, salasana tallennetaan ympäristömuuttujaan OS_PASSWORD. A-komennot tunnistavat tämän ympäristömuuttujan ja suoritettaessa ne automaattisesti päivittävät nykyisen Allas-yhteyden.

## Datan kopioiminen Puhti scratch -hakemiston ja Allaksen välillä

Datan kopioiminen hakemistosta _/scratch/project_201234/dataset_3_ Allakseen:

```text
cd /scratch/project_201234
a-put dataset_3
```
Hakemiston _dataset_3_ data tallennetaan oletusämpäriin _201234-puhti-SCRATCH_ objektina: _dataset_3.tar_.
Allaksen saatavilla olevat dataämpärit voidaan listata komennolla:

```text
a-list
```
Ja komentaa 201234-puhti-SCRATCH voidaan listata komennolla:

```
a-list 201234-puhti-SCRATCH
```
Hakemisto, joka tallennettiin Allakseen, voidaan hakea takaisin Puhtille komennolla:

```text
a-get 201234-puhti-SCRATCH/dataset_3.tar
```

# A komennot tarkemmin

## a-put lataa dataa Allakseen<a name="a-put"></a>

Komennolla `a-put` ladataan dataa Mahtin ja Puhtin levy-ympäristöstä 
Allas-tallennusympäristöön. Komennon perussyntaksi:
```text
a-put hakemisto_tai_tiedosto
```

Oletuksena tämä työkalu tekee seuraavat toimenpiteet:

1.    Varmista, että Allas-tallennuspalveluun on toimiva yhteys ja 
määritä projekti, jota käytetään datan tallennukseen.

2.    Hakemiston tapauksessa hakemiston sisältö kerätään yhdeksi tiedostoksi
käyttäen `tar`-komentoa.

3.    Pakattu data ladataan Allakseen käyttäen `rclone`-komentoa ja _Swift_-protokollaa.


Oletuksena a-put käyttää vakioämpäri- ja objektinimiä, jotka riippuvat käyttäjätunnuksesta, projektista ja ladatun datan sijainnista:

*    a) Data Puhtin /scratch:sta ladataan ämpäriin _projectNumber-puhti-SCRATCH_
*    b) Data Mahtin /scratch:sta ladataan ämpäriin _projectNumber-mahti-SCRATCH_
*    c) Data Puhtin /projappl:sta ladataan ämpäriin _projectNumber-puhti-PROJAPPL_ 
*    d) Data Mahtin /projappl:sta ladataan ämpäriin _projectNumber-mahti-PROJAPPL_ 
*    e) Data Puhtin $LOCAL_SCRATCH:sta ladataan ämpäriin _projectNumber-puhti-LOCAL_SCRATCH_
*    f) Muissa tapauksissa data ladataan _username-projectNumber-MISC_

Esimerkiksi käyttäjälle _kkayttaj_, joka on projektin _12345_ jäsen, HOME-hakemistoon sijoitettu data ladataan ämpäriin _kkayttaj-12345-MISC_.

Jos haluat käyttää jotain muuta kuin vakioämpäriä, voit määrittää ämpärin nimen vaihtoehdolla _-b_ tai  
_--bucket_.

Pakatut datasetit tallennetaan yhtenä objektina. Oletuksena objektin nimi riippuu tiedoston nimestä ja sijainnista. Mahdollinen alihakemistopolku Puhtissa tai Mahtissa sisällytetään objektin nimeen, esim. tiedosto nimeltä _test_1.txt_ Puhtin /scratch/project_2012345 -hakemistossa voidaan tallentaa käyttämällä seuraavia komentoja:
```text
cd /scratch/project_2012345
a-put test_1.txt
```

Tässä tapauksessa tiedosto tallennetaan ämpäriin _2012345-puhti-SCRATCH_.
objektiksi _test_1.txt_

Jos sinulla on toinen tiedosto nimeltä _test_1.txt_ sijainnissa _/scratch/project_2012345/kkayttaj/project2/_,
voit tallentaa sen seuraavilla komennoilla
```text
cd /scratch/project_2012345/kkayttaj/project2/
a-put test_1.txt
```
tai
```text
cd /scratch/project_2012345/kkayttaj
a-put project2/test_1.txt
```
Tässä tapauksessa tiedosto tallennetaan ämpäriin _2012345-puhti-SCRATCH_ 
objektina _kkayttaj/project2/test_1.txt_.

Varsinaisen dataobjektin lisäksi luodaan toinen objekti, joka sisältää metadataa. Tämä metadataobjekti 
on samaa nimeä kuin pääobjekti lisällä *_ameta*. Tätä metatiedostoa käytetään 
muissa *a-komentoissa*, ja normaalisti sitä ei näytetä käyttäjälle, mutta jos tarkastelet ämpäreitä
työkaluilla kuten _swift_ tai _rclone_, näet myös nämä metatiedot.

Jos haluat käyttää nimeä, joka poikkeaa vakiomuotoisesta objektinimestä, voit määrittää sen vaihtoehdolla _-o_ tai  
_--object_:
```text
cd /scratch/project_2012345
a-put project2/test_1.txt -b newbucket1 -o case1.txt -c
```

Yllä oleva komento lataa tiedoston *test_1.txt* Allakseen ämpäriin _newbucket1_ objektina _case1.txt.zst_.
Koska vaihtoehtoa _-c_ käytetään, data tallennetaan zstd-pakatussa muodossa. 

Voit antaa _a-put_ -komennolle useita tiedosto- tai hakemistonnimiä ja käyttää * merkkiä jokerina ladattavan datan nimeämisessä. Huomaa, että näissä tapauksissa jokainen kohde (tiedosto tai hakemisto) tallennetaan erillisenä objektina. Esimerkiksi, sanotaan, että meillä on _job123_ -hakemisto, joka sisältää tiedostot _input1.txt_, _input2.txt_ ja _program.py_. Lisäksi on hakemistot _output_dir_1_ ja _output_dir_2_.

Komento:
```text
a-put job123/output_dir_1 jobs123/input1.txt
```
lataa _output_dir_1_:n sisällön objektiksi _job123/output_dir_1.tar_ ja _input1.txt_:n _job123/input1.txt_.

Vastaavasti komento:
```text
a-put job123/output_dir*
```
lataa _output_dir_1_:n sisällön objektiksi _job123/output_dir_1.tar_ ja _output_dir_2_:n sisällön objektiksi _job123/output_dir_2.tar_. 

Jos datasetit ovat suurempia kuin 5 GB, ne jaetaan ja tallennetaan useina objekteina. Tämä tapahtuu automaattisesti ämpäriin, jonka nimi on lisätty alkuperäiseen ämpärin nimeen laajennos _segments_. Esimerkiksi, jos ladattaisiin suuri tiedosto ämpäriin _kkayttaj-12345-MISC_ tosiasiassa dataa tallennettaisiin useina osina ämpäriin _kkayttaj-12345-MISC_segments_. Kohdeämpäriin (_kkayttaj-12345-MISC_) jää ainoastaan etuobjekti, joka sisältää tiedot siitä, mitkä segmentit muodostavat tallennetun datasetin. Toimintojen suorittaminen etuobjektille heijastuu automaattisesti segmentteihin. Käyttäjien ei normaalisti tarvitse toimia segmenttiämpäreiden kanssa, eikä näiden ämpärien objekteja pitäisi poistaa tai muokata.

## a-check<a name="a-check"></a>

Tämä komento käy läpi Allaksessa objektinimet, jotka vastaava `a-put` -komento loisi, ja tarkistaa, löytyykö samalla nimellä oleva objekti jo Allaksesta. Komennon pääasiallinen tarkoitus on tarjota työkalu suuren `a-put` -komennon onnistumisen tarkistamiseksi. `a-check` hyväksyy samat komentorivivaihtoehdot kuin `a-put`.

Esimerkiksi, jos datasetti ladataan komennolla:
```text
a-put job123/*
```
Lataus voidaan tarkistaa komennolla: 
```text
a-check job123/*
```
_a-check_ -komento vertaa ladattavien kohteiden nimiä Allas-objekteihin.
Kohteet, joilla ei ole kohdeobjektia Allaksessa, raportoidaan ja tallennetaan tiedostoon: missing_bucket-name_number. Jos jokin kohteista yllä olevassa esimerkissä puuttuisi, niin
a-check listaisi puuttuvat tiedostot ja hakemistot tiedostossa `missing_job123_67889` (suorassa numerossa lopussa on vain satunnainen numero).

Tätä puuttuvien kohteiden tiedostoa voidaan käyttää a-put-vaihtoehdon --input-list kanssa jatkamaan epäonnistunutta latausprosessia:
```text
a-put --input-list missing_job123_67889
```

Huomaa, että _a-check_ ei tarkista, onko varsinaisen objektin sisältö oikein. Se tarkistaa vain objektinimet, jotka saattavat olla peräisin joistakin muista lähteistä.

Paitsi että _a-check_ tarkistaa, oliko lataus onnistunut, sitä voidaan käyttää myös "kuiva-ajo" -testiin ennen varsinaisen _a-put_ -komennon suorittamista, jotta nähdään, mitä objekteja luodaan tai korvataan. 


## a-list<a name="a-list"></a>

a-list -komennolla näytetään tiedot Allakseen tallennettujen ämpäreiden ja objektien nimistä. a-list on suunniteltu käytettäväksi a-puta -komennolla ladatuille objekteille, mutta se näyttää kuitenkin myös muiden työkalujen avulla ladatut objektit. Se ei kuitenkaan näytä a-put:n luomia _ameta_ -metatiedostoja pitääkseen objektin listaukset lyhyinä.

### a-list esimerkkejä

Listaa projektin kaikki ämpärit:
```text
a-list
```
Näytä ämpäriin sisältyvät objektit:
```text
a-list bucket_name
```
Kirjoittamalla osa objektin nimestä listaa osajoukkoa objekteista:
```text
a-list bucket_name/beginning_of_the_object
```
Tarkemman listauksen saamiseksi, joka sisältää objektin koon ja päivämäärän, voit käyttää vaihtoehtoa `-l`
```text
a-list -l 
```
Vaihtoehto `-d` saa a-listin tulkitsemaan /-merkit objektin nimissä pseudokansion erottimina.
```text
a-list -d 
```

## a-publish<a name="a-publish"></a>

`a-publish` kopioi tiedoston Allakseen ämpäriin, johon on julkinen pääsy. Täten kuka tahansa ladatun dataobjektin osoitteen (URL) omaava henkilö voi lukea ja ladata datan joko verkkoselaimen tai työkalujen kuten _wget_ ja _curl_ avulla. a-publish toimii samankaltaisesti kuin a-put, muutamilla eroilla: 

1) a-publish voi ladata vain tiedostoja, ei hakemistoja. 
2) Kohdeämpärin käyttöoikeudet asetetaan siten, että se on saatavilla jokaiselle käyttäjälle vain luku -tilassa.

Perussyntaksi:
```text
a-publish tiedosto_nimi
```
Oletuksena tiedosto ladataan ämpäriin _username-projectNumber_-pub. Voit määrittää muut ämpärien nimet käyttämällä vaihtoehtoa _-b_. Huomaa, että tämä komento tekee kaiken datan kohdeämpärissä julkisesti saataville, mukaan lukien jo aiemmin ämpäriin ladatun datan.

Dataobjektin julkinen URL on:
`https://a3s.fi/username-projectNumber-pub/tiedosto_nimi`

Objektin, joka ladattiin _a-publish_ -komennolla, voi poistaa Allaksesta käyttämällä _a-delete_ -komentoa.

Näytteen istunto _a-publish_ -komennon kanssa, esitellessä dokumentin _presentation.pdf_ lataamista oletusarvoiseen julkiseen ämpäriin Allakseen:

<pre><b>a-publish presentation.pdf</b> 
Ladattavat tiedostot:  presentation.pdf
Ämpäri: kkayttaj-1234567-pub
Käsittely: presentation.pdf
Tarkistetaan presentation.pdf:n koko. Odota hetki.

Data ladataan ollakseen valmis kaikille.
Siirretty:        4.188M / 4.188 MBytes, 100%, 7.700 MBytes/s, ETA 0s
Virheet:                  0
Tarkistukset:        0 / 0, -
Siirrettyä:        1 / 1, 100%
Kulunut aika:        500ms
Latauksen vahvistus...
presentation.pdf OK

Lisätään metadata ladatulle presentation.pdf:lle
presentation.pdf ladattu kkayttaj-1234567-pub
Julksinen linkki: https://a3s.fi/kkayttaj-1234567-pub/presentation.pdf

Lataus valmis

</pre>

## a-flip<a name="a-flip"></a>

`a-flip` on työkalu yksittäisten tiedostojen tilapäiseen saatavuuteen internetin kautta. Se on tarkoitettu tilanteisiin, joissa halutaan tehdä tiedostosta kopio, joka on näkyvissä internetissä esimerkiksi toisen alustan kopioimista varten yhdessä työtoverin kanssa.

a-flip kopioi tiedoston Allakseen ämpäriin, johon on julkinen pääsy. Näin ollen kuka tahansa ladatun dataobjektin osoitteen (URL) omaava voi lukea ja ladata datan joko verkkoselaimen tai työkalujen kuten _wget_ ja _curl_ avulla. a-flip toimii samankaltaisesti a-publish:n kanssa, mutta muutamilla eroilla:

1. Vain ennalta määritelty ämpärin nimi (_username-projectNumber_-flip) voidaan käyttää.
2. Suoritettaessa se tarkistaa flip-ämpärin sisällön ja poistaa yli kaksi päivää vanhat objektit.

Perussyntaksi:
```text
a-flip tiedosto_nimi
```
Tiedosto ladataan ämpäriin _username-projectNumber_-flip. Ladatun objektin osoite:
```text
https://a3s.fi/username-projectNumber-flip/tiedosto_nimi
```

## a-find<a name="a-find"></a>

Komennolla `a-find` listataan ja paikannetaan data, joka on ladattu Allakseen `a-put` -komennolla.

Perussyntaksi:
```text
a-find hakutermi
```

Hakutermiä verrataan Allakseen ladattujen tiedostojen nimiin ja alkuperäisiin polkuihin ja vastaavat objektit raportoidaan (mutta ei ladattuina).

Hakutermi prosessoidaan säännöllisenä ilmaisuna, jossa joillakin merkkeillä, kuten pisteellä (.), on erityinen merkitys. Sama säännöllisten lausekkeiden syntaksi käytetään esimerkiksi _grep_, _awk_ ja _sed_ -komennoissa. Yleisimmin esiintyvät erikoismerkit:

- Piste (**.**) käytetään minkä tahansa yksittäisen merkin määrittelemiseen.
- **^** merkitsee rivin alkua.
- **$** merkitsee rivin loppua.
- **[ ]** vastaa mitä tahansa merkkiä hakasulkeiden sisällä. Esimerkiksi [abc] vastaisi a, b tai c.
- **[^ ]** vastaa mitä tahansa merkkiä lukuun ottamatta hakasulkeiden sisäisiä merkkejä.   
    Esimerkiksi [^abc] valitsisi kaikki rivit, jotka sisältävät merkkejä, jotka eivät ole a, b ja c.
- ** * ** vastaa nollaa tai useampaa edeltävää merkkiä tai ilmaisua.
    `\{n,m\}` vastaa n:stä m:ään edeltäviä merkkejä tai ilmauksia.

Vaihtoehdot:


- **-a**, **--all**  Oletuksena vain a-put:n käyttämät vakiämpärit ets

itään. Vaihtoehto `--all` määrittelee, että kaikki projektin ämpärit sisällytetään etsintään.
- **-f**, **--files** Listaa nimien lisäksi hakulausekkeen raamatullisista hakuparametreista vastaavat tiedostot.
- **-p**,**--project _project_ID_**  Etsi vastineet määritetyn projektin ämpäreistä nykyisen konfiguroidun projektin sijaan. 
- **-b**, **--bucket _bucket_name_** Oletuksena kaikki _a-put_ -komennon käyttämät vakiämpärit ets

itään. Vaihtoehto _-bucket_ mahdollistaa yksittäisen ämpärin määrittelemisen etsintään. Käytä tätä vaihtoehtoa myös tilanteissa, joissa olet tallentanut dataa epätavanomaisella nimellä olevaan ämpäriin.
- **-s**, **-silent** Tulosta vain objektinimet ja osumien lukumäärä. Jos _-f_ -vaihtoehtoa käytetään, tulosta objektin nimi ja vastaavat tiedostonimet yhdellä rivillä.


## a-info näyttää tietoa ladatusta datasetistä<a name="a-info"></a>
                             
Komennolla `a-info` voi saada tietoa datasetistä, joka on ladattu Allakseen käyttämällä `a-put` -komentoa.   

```text
a-info bucket/objekti_nimi
```           
Jos suoritat tämän komennon ilman objektinimeä, se listaa perusinfot kaikista tämänhetkisen projektin objekteista ja vikasta yhteenvetotietoa siitä, kuinka paljon dataa ja objekteja Allas-projektisi sisältää.
```text
a-info 
```   

                             
## a-get hakee tallennettua dataa<a name="a-get"></a>

Tätä työkalua käytetään ladatun datan lataamiseen, joka on ladattu Allas-palveluun käyttämällä `a-put` -komentoa.
Perussyntaksi:
```text
a-get objekti_nimi
```
Objekti haetaan oletuksena, puretaan pakatusta tiedostosta ja sen data palautetaan tiedostoon tai hakemistoon, jota käytettiin latauksessa. Jos olemassa oleva tiedosto tai hakemisto on jo olemassa samalla nimellä, sinun on joko poistettava olemassa oleva tiedosto tai hakemisto tai määritettävä ladatulle datalle uusi hakemisto _-target_ -vaihtoehdon avulla.

Vaihtoehdot:

- **-p**, **--project _project_ID_** Hae data projektin ämpäreistä nykyisen konfiguroidun projektin sijasta. 
- **-f**, **--file _file_name_** Hae vain tietty tiedosto tai hakemisto tallennetusta datasetistä. **Huom:** Määritä koko polku tiedoston tai hakemiston sijainnille tallennetun objektin sisällä.
- **-d** **--target_dir** <dir_name> Jos tätä vaihtoehtoa käytetään, luodaan uusi kohdehakemisto ja data haetaan sinne.
- **-t** **--target_file** <file_name> Määritä tiedostonnimi ladattavalle objektille.
- **-l** **--original_location**       Hae data alkuperäiseen sijaintiin hakemistorakenteessa.
- **--asis**                        Lataa objekti ilman tar-tiedoston purkamista ja zst-pakatun datan avattamista.
- **--s3cmd**                       Käytä S3-protokollaa ja s3cmd-komentoa datan hakemiseen Swift-protokollan ja rclone-komennon sijaan.

Tällä hetkellä _a-get_ voi ladata vain yhden objektin kerrallaan. Jos sinun tarvitsee ladata suuri määrä objekteja, sinun tarvitsee käyttää silmukoita. Esimerkiksi ladataksesi kaikki objektit ämpäristä _bucket_123_ , voit käyttää komentoja:

```text
#tee listaus objekteista
a-list bucket_123 > object_list_bucket123

#käytä listaa for-silmukassa
for ob in $(cat object_list_bucket123)
do
  a-get $ob
done  

#poista objektilista
rm object_list_bucket123
```

## a-delete<a name="a-delete"></a>
a-delete komennolla poistetaan dataa, joka on ladattu Allakseen a-put -komennolla.
Komennon perussyntaksi on:
<pre>a-delete objektin_nimi</pre>

Oletuksena _a-delete_ kysyy käyttäjältä vahvistusta objektin poistamiseen. Tämän tarkistuksen voi ohittaa vaihtoehdolla `-f`.

Jos haluat poistaa ämpärin, voit käyttää vaihtoehtoa `--rmb`. Oletuksena _a-delete --rmb_ poistaa vain tyhjät ämpärit. Jos haluat poistaa muita kuin tyhjiä ämpäreitä, sinun on lisättävä _--forcE_.

## a-access<a name="a-access"></a>

Oletuksena vain projektin jäsenet voivat lukea ja kirjoittaa ämpärin dataa.
Projektin jäsenet voivat avata luku- ja kirjoitusoikeudet ämpäriin ja 
sen sisältämiin objekteihin, muille Allas-projekteille tai tehdä ämpäri julkisesti
saatavaksi internetiin.

**a-access** on työkalu hallita ämpärin käyttöoikeuksia (swift protokolla) Allaksessa.

Syntaksi 
```text
a-access +/-tyyppi projektin_nro ämpäri_nimi
```
Vaihtoehdot:

- **+r**,  **+read** <project_id>        Anna projektin lukuoikeus ämpäriin.
- **+w**,  **+write** <project_id>       Anna projektin kirjoitusoikeus ämpäriin.
- **+rw**, **+read-write**  <project_id> Anna projektin luku- ja kirjoitusoikeus ämpäriin.
- **-r**,  **-read** <project_id>        Poista projektin lukuoikeus ämpäristä.
- **-w**,  **-write** <project_id>       Poista projektin kirjoitusoikeus ämpäristä.
- **-rw**, **-read-write**  <project_id> Poista projektin luku- ja kirjoitusoikeudet ämpäristä.
- **+p**,  **+public**                   Anna julkinen lukuoikeus ämpäriin.
- **-p**,  **-public**                   Poista julkinen lukuoikeus ämpäristä.

Esimerkiksi, jotta projektin: _project_2001234_ jäsenet voisivat saada lukuoikeuden ämpäriin: _my_data_bucket_, voit käyttää komentoa:
```text
a-access +r project_2001234  my_data_bucket
```
Käyttöoikeudet asetetaan samalla tavalla myös väliämpärille segments bucket.

Huomaa, että ämpärin listauksen työkalut eivät näytä muiden projektien ämpärien nimiä, 
edes siinä tapauksessa, että projektilla on luku- ja/tai kirjoitusoikeudet ämpäriin.

Esimerkiksi tässä tapauksessa käyttäjän, joka kuuluu projektiin _project_2001234_, 
ei näe _my_data_bucket_ -ämpäriä ämpärin listauksessa komennolla:
```text  
a-list
```
mutta käyttäjä voi silti listata ämpärin sisällön komennolla:  
```text
a-list my_data_bucket
```
Ja ladata kohteita ämpäristä a-get:llä.

a-access hallitsee käyttöoikeuksia vain projektin ja ämpärin tasolla.
Käytä **swift post** -komentoa monimutkaisempaan käyttöoikeuksien hallintaan.

Jos suoritat _a-access_ -komennon ämpärille ilman muutoksia vaihtoehtoja,
se näyttää ämpärin nykyiset asetukset.

### a-komentojen konfigurointi

Userit voivat muokata a-komentojen oletusasetuksia tekemällä konfiguraatiotiedoston nimeltä **.a_tools_conf** kotihakemistoonsa. Tässä tiedostossa voi asettaa oletusasetuksia monille a-put -komennon vaihtoehtojen määrittelemille toiminnoille.

Esimerkiksi, jos työskentelet pääasiassa tiedostojen kanssa, jotka hyötyvät pakkauksesta, saatat haluta käyttää _--compress_ -vaihtoehtoa a-put -komennossa. Jos haluat tämän olevan oletusasetus, voit luoda .a_tools_conf -tiedoston, joka sisältää:

```text
compression=1
```
Nyt komento:
```text
a-put my_data.b
```
pakkkaisi datan latauksen aikana (mikä ei normaalisti ole tilanne). Kuitenkin, voit silti ohittaa pakkauksen vaihtoehdolla _--nc_.

```text
a-put --nc my_data.b
```
 
Voit tarkistaa yleisimmin käytetty vertaileja tästä esimerkistä [.a_tools_conf](https://github.com/CSCfi/allas-cli-utils/edit/master/.a_tools_conf). Kopioi esimerkkitiedosto kotihakemistoosi ja aktivoi ja määritä haluamasi muuttujat.

