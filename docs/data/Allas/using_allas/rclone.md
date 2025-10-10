# Allaksen käyttö Rclonen kanssa { #using-allas-with-rclone }

Tässä luvussa on ohjeet Allaksen käyttämiseen [Rclonen](https://rclone.org/) kanssa Puhti- ja Mahti-laskentaympäristöissä. _Rclone_ tarjoaa erittäin tehokkaan ja monipuolisen tavan käyttää Allasta ja muita objektitallennuspalveluita. Se osaa käyttää sekä S3- että Swift-protokollia (sekä monia muita). Tällä hetkellä Swift on oletusprotokolla CSC:n palvelimilla. 

> **VAROITUS:** Rclonea ei tule käyttää objektien kopioimiseen, siirtämiseen tai nimeämiseen uudelleen **Allaksen sisällä**. Rclone tarjoaa komennot näihin toimenpiteisiin, mutta ne eivät toimi oikein yli 5 Gt:n kokoisille tiedostoille.
> 
> **VAROITUS:** Jos yli 5 Gt:n tiedoston rclone-lataus keskeytyy, poista osittain ladattu objekti ennen latauksen uudelleenkäynnistystä. Muutoin rclone saattaa joskus ilmoittaa latauksen onnistuneeksi, vaikka kaikkia tietoja ei ole kopioitu Allakseen.



Rclonen perussyntaksi:
<pre>
rclone <i>subcommand options source:path dest:path</i> 
</pre>

Yleisimmät Rclone-komennot:

*    [rclone copy]( https://rclone.org/commands/rclone_copy/) – Kopioi tiedostot lähteestä kohteeseen ohittaen jo kopioidut.
*    [rclone sync](https://rclone.org/commands/rclone_sync/) – Saattaa lähteen ja kohteen identtisiksi muokkaamalla vain kohdetta.
*    [rclone move](https://rclone.org/commands/rclone_move/) – Siirtää tiedostot lähteestä kohteeseen.
*    [rclone delete](https://rclone.org/commands/rclone_delete/) – Poistaa polun sisällön.
*    [rclone mkdir](https://rclone.org/commands/rclone_mkdir/) – Luo polun, jos sitä ei vielä ole.
*    [rclone rmdir](https://rclone.org/commands/rclone_rmdir/) – Poistaa polun.
*    [rclone check](https://rclone.org/commands/rclone_check/) – Tarkistaa, täsmäävätkö lähteen ja kohteen tiedostot.
*    [rclone ls](https://rclone.org/commands/rclone_ls/) – Listaa kaikki objektit polussa, mukaan lukien koko ja polku.
*    [rclone lsd](https://rclone.org/commands/rclone_lsd/) – Listaa kaikki hakemistot/kontit/bucketit polussa.
*    [rclone lsl](https://rclone.org/commands/rclone_lsl/) – Listaa kaikki objektit polussa, mukaan lukien koko, muokkausaika ja polku.
*    [rclone lsf](https://rclone.org/commands/rclone_lsf/) – Listaa objektit niiden nimiin perustuvan virtuaalihakemistorakenteen mukaan.
*    [rclone cat](https://rclone.org/commands/rclone_cat) – Ketjuttaa tiedostot ja lähettää ne stdoutiin.
*    [rclone copyto](https://rclone.org/commands/rclone_copyto/) – Kopioi tiedostot lähteestä kohteeseen ohittaen jo kopioidut.
*    [rclone moveto](https://rclone.org/commands/rclone_moveto/) – Siirtää tiedoston tai hakemiston lähteestä kohteeseen.
*    [rclone copyurl](https://rclone.org/commands/rclone_copyurl/) – Kopioi URL-osoitteen sisällön kohteeseen tallentamatta sitä tmp-välivarastoon.

Laajempi luettelo löytyy [Rclonen ohjesivuilta](https://rclone.org/docs/) tai kirjoittamalla komento `rclone` Puhtissa.

## Tunnistautuminen CSC:n supertietokoneilla { #authentication-on-csc-supercomputers }

Alla kuvataan, miten Rclonea käytetään CSC:n laskentaympäristössä (Puhti ja Mahti). Voit käyttää [Rclonea myös omalla tietokoneellasi](./rclone_local.md). 


Ensimmäinen vaihe on määrittää yhteys Allaksen projektiin. Rclone voi käyttää sekä Swift- että S3-protokollaa, mutta nämä yhteydet saavat eri nimet rclone-komennoissa. 


 [`allas-conf`](allas-conf.md#allas-conf-configure-connection) lisätietoja ja lisäasetuksia varten.

### Rclone ja Swift { #rclone-with-swift }

Allaksen oletusprotokolla on Swift. Puhtissa ja Mahtissa Swift-pohjainen Allas-yhteys aktivoidaan komennoilla:
```text
module load allas
allas-conf
```
Rclone-komennoissa tähän Swift-pohjaiseen yhteyteen viitataan etänimellä `allas:`. 

### Rclone ja S3 { #rclone-with-s3 }

Jos haluat käyttää Allasta S3-protokollalla, suorita:
```text
module load allas
allas-conf --mode S3
```
Tämä komento avaa pysyvän S3-pohjaisen yhteyden Allakseen. Rclone voi nyt viitata tähän yhteyteen etänimellä `s3allas:`.
Alla olevissa esimerkeissä käytetään Swift-pohjaista etämäärittelyä `allas:`, mutta jos olet määrittänyt S3-yhteyden, voit korvata sen muodolla `s3allas:`. 

Huomaa, että sekä `allas:` että `s3allas:` voivat olla toiminnassa samanaikaisesti ja ne voivat käyttää eri Allas-projekteja. Vältä kuitenkin protokollien sekoittamista. Jos objekti on ladattu käyttäen `allas:`-yhteyttä, tee myös kaikki toimenpiteet sillä.  



## Luo bucketteja ja lataa objekteja { #create-buckets-and-upload-objects }

Allaksen data on järjestetty säilöihin, joita kutsutaan bucketeiksi. Voit ajatella niitä juuritason hakemistoina. Kaikilla Allaksen bucketeilla on oltava yksilölliset nimet – et voi luoda buckettia, jos jokin toinen projekti on jo käyttänyt samaa nimeä. Hyvä nyrkkisääntö on sisällyttää bucketin nimeen jotain projekti- tai käyttäjäkohtaista, esim. _2000620-raw-data_. Katso [tarkistuslista](../introduction.md#naming-buckets-and-objects) ohjeista bucketin nimeämiseen.

Rclonella bucketin luominen:
```text
rclone mkdir allas:2000620-raw-data
```
Lataa tiedosto komennolla ```rclone copy```:
```text
rclone copy file.dat allas:2000620-raw-data/
```
Yllä oleva komento luo objektin _file.dat_ bucketiin _2000620-raw-data_.
Jos käytät `rclone move`-komentoa `rclone copy`n sijaan, ladatun tiedoston paikallinen versio (file.dat)
poistetaan kopioinnin jälkeen.

Alikomennot _copy_ ja _move_ toimivat vain tiedostoille. Jos haluat kopioida kaikki tiedostot hakemistosta, käytä alikomentoja _copyto_ tai _moveto_.

Latauksen aikana yli 5 Gt:n tiedostot pilkotaan ja tallennetaan useina objekteina. Objektit tallennetaan automaattisesti erilliseen bucketiin nimellä `<bucket-nimi>_segments`. Jos esimerkiksi lataat suuren tiedoston bucketiin  `2000620-raw-data`, varsinainen data tallentuu useaan osaan bucketiin `2000620-raw-data_segments`. Kohdebucketissa (`2000620-raw-data`) on vain manifest-objekti, joka kertoo, mitkä segmentit muodostavat tallennetun tiedoston. Manifest-objektiin kohdistetut toiminnot heijastuvat automaattisesti segmentteihin. Yleensä käyttäjien ei tarvitse toimia segments-bucketien kanssa lainkaan, eikä niiden sisäisiä objekteja tule poistaa tai muokata.

## Listaa bucketit ja objektit { #list-buckets-and-objects }

Listaa kaikki projektiin kuuluvat bucketit:
<pre><b>rclone lsd allas:</b>
0 2019-06-06 14:43:40         0 2000620-raw-data
</pre>

Listaa bucketin sisältö: 
<pre><b>rclone ls allas:2000620-raw-data</b>
677972 file.dat
</pre>

## Lataa objekteja { #download-objects }

Käytä samoja `rclone copy`- ja `rclone copyto` -komentoja tiedoston lataamiseen:
```text
rclone copy allas:2000620-raw-data/file.dat
```

Jos lisäät kohdeparametrin latauskomentoon, Rclone luo latausta varten hakemiston:
```text
rclone copy allas:2000620-raw-data/file.dat doh
```

<pre><b>ls doh</b>
file.dat</pre>

<pre><b>ls -ld doh</b>
drwxr-xr-x  3 user  staff  96 Jun  6 14:58 doh
</pre>

## Hakemiston synkronointi { #synchronizing-a-directory }

Yksi tapa siirtää dataa Allaksen ja laskentaympäristön välillä on synkronointi. Kopioinnin ja synkronoinnin ero on, että kopiointi vain lisää uusia objekteja tai tiedostoja lähteestä kohteeseen, kun taas synkronointi voi myös poistaa dataa kohteesta, jotta kohde vastaa lähdettä. Tämä tekee synkronoinnista tehokasta mutta potentiaalisesti myös vaarallista.

Esimerkiksi hakemistolla nimeltä _mydata_ on seuraava rakenne:
<pre>
<b>ls -R mydata</b>

mydata/:
file1.txt  setA  setB

mydata/setA:
file2.txt

mydata/setB:
file3.txt  file4.txt
</pre>

Esimerkki _sync_-komennon käytöstä (huomaa, että kohdeparametriin tarvitaan kansion nimi (_mydata_)):

```text
rclone sync mydata allas:2000620-raw-data/mydata
```

<pre><b>rclone ls allas:2000620-raw-data</b>
   677972 mydata/file1.txt
    10927 mydata/setA/file2.txt
     1116 mydata/setB/file3.txt
     5075 mydata/setB/file4.txt
</pre>

Oletetaan, että tallennamme uutta dataa (_file5.txt_ ja _file6.txt_) alihakemistoon _mydata/setC_ ja poistamme samalla tiedoston _mydata/setB/file3.txt_. Kun _rclone sync_ -komento suoritetaan uudelleen, uusi data lisätään Allakseen ja objekti _mydata/setB/file3.txt_ poistetaan.

<pre><b>rclone sync mydata allas:2000620-raw-data/mydata</b>

<b>rclone ls allas:2000620-raw-data</b>
   677972 mydata/file1.txt
    10927 mydata/setA/file2.txt
     5075 mydata/setB/file4.txt
     1265 mydata/setC/file5.txt
     4327 mydata/setC/file6.txt
</pre>

Yllä olevissa esimerkeissä Allasta on käytetty muutettavana kohteena. Komentoa voidaan kuitenkin käyttää myös toiseen suuntaan:
```text
rclone sync allas:2000620-raw-data/mydata mydata
```

Tämä komento palauttaa Allakseen ladatun datan takaisin _mydata_-hakemistoon. Huomaa kuitenkin, että jos olet lisännyt uutta dataa hakemistoon _mydata_ sen synkronoinnin jälkeen Allaksen kanssa, nämä tiedot poistetaan.

## Tiedostojen kopiointi suoraan objektitallennusten välillä { #copying-files-directly-between-object-storages }

Rclonea voidaan käyttää myös tiedostojen suoraan kopioimiseen toisesta objektitallennuksesta (esim. [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), [Google Cloud](https://cloud.google.com/learn/what-is-object-storage), [CREODIAS](https://creodias.eu/cloud/cloudferro-cloud/storage-2/object-storage/),...) Allakseen. Tätä varten molemmat käyttöoikeustiedot on tallennettava käyttäjän kotihakemiston Rclone-määritystiedostoon (`.config/rclone/rclone.conf`). Alla on esimerkki:

```
[s3allas]
type = s3
provider = Other
env_auth = false
access_key_id = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
secret_access_key = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
endpoint = a3s.fi
acl = private

[otherobjectstorage]
type = s3
provider = Other
env_auth = false
access_key_id = yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
secret_access_key = yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
endpoint = yourotherendpoint.com
acl = private
```
Allaksen määritys lisätään automaattisesti, kun Allas konfiguroidaan s3-tilassa 

`source allas_conf --mode s3cmd` .

Tämän tiedoston luomisen tai päivittämisen jälkeen Rclonea voidaan käyttää tiedostojen kopioimiseen

`rclone copy otherobjectstorage:bucket-x/object-y  s3allas:bucket-z/object-a`

tai listamaan tiedostoja joko Allaksesta tai toisesta objektitallennuksesta käyttämällä vastaavaa nimeä

`rclone lsf otherobjectstorage: `.