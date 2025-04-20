# Allas-palvelun käyttö Rclonella {#using-allas-with-rclone}

Tämä luku sisältää ohjeet Allas-palvelun käyttämisestä [Rclone](https://rclone.org/)-ohjelmalla Puhti- ja Mahti-laskentaympäristöissä. _Rclone_ tarjoaa hyvin tehokkaan ja monipuolisen tavan käyttää Allasta ja muita objektitallennuspalveluita. Se tukee sekä S3- että Swift-protokollia (ja monia muita). Tällä hetkellä Swift-protokolla on oletusvaihtoehto CSC:n palvelimilla.

> **VAROITUS:** Rclonea ei tule käyttää kohteiden kopioimiseen, siirtämiseen tai uudelleennimeämiseen **Allaksen sisällä**. Rclone tarjoaa käskyt näihin operaatioihin, mutta ne eivät toimi oikein yli 5 GB kokoisille tiedostoille.
> 
> **VAROITUS:** Jos rclone-siirtoprosessi yli 5 GB tiedoston latauksessa keskeytyy, poista osittain ladattu objekti ennen uuden latauksen aloittamista. Muutoin rclone saattaa ilmoittaa siirron onnistuneeksi, vaikka kaikkia tietoja ei ole kopioitu Allakseen.

Rclonen perussyntaksi:
<pre>
rclone <i>subcommand options source:path dest:path</i> 
</pre>

Useimmin käytetyt Rclone-komennot:

*    [rclone copy](https://rclone.org/commands/rclone_copy/) – Kopioi tiedostot lähteestä kohteeseen, ohittaa jo siirretyt.
*    [rclone sync](https://rclone.org/commands/rclone_sync/) – Saattaa lähteen ja kohteen identtisiksi, muokkaa vain kohdetta.
*    [rclone move](https://rclone.org/commands/rclone_move/) – Siirtää tiedostot lähteestä kohteeseen.
*    [rclone delete](https://rclone.org/commands/rclone_delete/) – Poistaa polun sisällön.
*    [rclone mkdir](https://rclone.org/commands/rclone_mkdir/) – Luo polun, jos sitä ei ole.
*    [rclone rmdir](https://rclone.org/commands/rclone_rmdir/) – Poistaa polun.
*    [rclone check](https://rclone.org/commands/rclone_check/) – Tarkistaa, täsmäävätkö lähteen ja kohteen tiedostot.
*    [rclone ls](https://rclone.org/commands/rclone_ls/) – Listaa kaikki polun objektit, koko ja polku.
*    [rclone lsd](https://rclone.org/commands/rclone_lsd/) – Listaa kaikki kansiot/kontit/bucketit polussa.
*    [rclone lsl](https://rclone.org/commands/rclone_lsl/) – Listaa kaikki polun objektit, mukaan lukien koko, muokkausaika ja polku.
*    [rclone lsf](https://rclone.org/commands/rclone_lsf/) – Listaa objektit käyttäen virtuaalista hakemistorakennetta objektien nimien perusteella.
*    [rclone cat](https://rclone.org/commands/rclone_cat) – Yhdistää tiedostot ja lähettää ne stdoutiin.
*    [rclone copyto](https://rclone.org/commands/rclone_copyto/) – Kopioi tiedostot lähteestä kohteeseen, ohittaa jo siirretyt.
*    [rclone moveto](https://rclone.org/commands/rclone_moveto/) – Siirtää tiedoston tai kansion lähteestä kohteeseen.
*    [rclone copyurl](https://rclone.org/commands/rclone_copyurl/) – Kopioi URL-osoitteen sisällön kohteeseen ilman että sitä tallennetaan tmp-varastoon.

Laajempi listaus löytyy [Rclonen ohjesivuilta](https://rclone.org/docs/) tai antamalla komento `rclone` Puhtissa.

## Autentikointi {#authentication}

Ensimmäinen vaihe on kirjautuminen projektiin Allaksessa. Rclone voi käyttää sekä Swift- että S3-protokollaa, mutta nämä yhteydet nimetään eri tavoin rclone-komennoissa.

Tässä ohjeessa kuvataan, miten Rclonea käytetään CSC:n laskentaympäristössä (Puhti ja Mahti). Voit käyttää rclonea myös omalla tietokoneellasi. Ohjeet paikallisesti asennetun Rclonen konfiguroimiseen löydät täältä

   * [Paikallinen Rclone-konfigurointi Allakselle](./rclone_local.md)

### Rclone ja swift CSC:n supertietokoneilla {#rclone-with-swift-on-csc-supercomputers}

Allaksen oletusprotokolla on Swift. Puhtissa ja Mahdissa Swift-pohjainen Allas-yhteys aktivoidaan komennoilla:
```text
module load allas
allas-conf
```
Komento `allas-conf` kysyy CSC-salasanaasi (Yliopisto/Haka-tunnukset eivät toimi tässä). Se listaa projektisi Allaksessa ja pyytää valitsemaan, mitä projektia käytetään. Tämän jälkeen _allas-conf_ luo Rclonen konfiguraatiotiedoston Allas-palvelulle ja autentikoi yhteyden valittuun projektiin. Rclone-komentojen yhteydessä tätä Swift-pohjaista yhteyttä kutsutaan nimellä `allas:`. Autentikointitiedot tallennetaan shell-muuttujiin `OS_AUTH_TOKEN` ja `OS_STORAGE_URL`, jotka ovat voimassa jopa kahdeksan tuntia. Voit kuitenkin uusia autentikoinnin milloin tahansa ajamalla _allas-conf_ uudelleen. Ympäristömuuttujat ovat voimassa vain kyseisellä istunnolla; jos kirjaudut Puhtiin toisessa rinnakkaisessa istunnossa, sinun täytyy autentikoida uudelleen päästäksesi Allakseen.

### Rclone ja S3 CSC:n supertietokoneilla {#rclone-with-s3-on-csc-supercomputers}

Jos haluat käyttää Allasta S3-protokollalla, aja komento `allas-conf` valitsimella `--mode S3`.
```text
module load allas
allas-conf --mode S3
```
Tämä komento avaa pysyvän S3-pohjaisen yhteyden Allakseen. Rclone voi nyt viitata tähän yhteyteen nimellä `s3allas:`.
Alla olevissa esimerkeissä käytetään Swift-pohjaista `allas:`-etäyhteyttä, mutta jos olet määritellyt S3-yhteyden, voit korvata sen `s3allas:`-etäyhteydellä. Huomaa, että molemmat `allas:` ja `s3allas:` voivat olla käytössä samanaikaisesti ja niissä voi olla eri Allas-projektit. Protokollien sekoittamista tulisi kuitenkin välttää. Jos objekti ladataan käyttäen `allas:`, tee kaikki operaatiot samalla etäyhteydellä.

## Bucketien luonti ja objektien lataaminen {#create-buckets-and-upload-objects}

Allaksen data on järjestetty säiliöihin, joita kutsutaan buckets. Voit ajatella niitä juuritason hakemistoina. Kaikilla Allaksen bucket-nimillä pitää olla yksilöllinen nimi – et voi luoda buckettia, jos jonkin muun projektin käytössä on jo sama nimi. Hyvä käytäntö on käyttää projekti- tai käyttäjäkohtaista tunnistetta bucket-nimessä, esim. _2000620-raw-data_. Tarkista [tarkistuslista](../introduction.md#naming-buckets) bucketin nimeämiseen.

Rclonen tapauksessa buckettin luonti:
```text
rclone mkdir allas:2000620-raw-data
```
Tiedoston lataus komennolla ```rclone copy```:
```text
rclone copy file.dat allas:2000620-raw-data/
```
Yllä oleva komento luo objektin _file.dat_ bucketiin _2000620-raw-data_.
Jos käytät komentoa `rclone move` `rclone copy`n sijasta, lähetetyn tiedoston paikallinen versio (file.dat)
poistetaan kopioinnin jälkeen.

_Copy_- ja _move_-alikomennot toimivat vain tiedostoihin. Jos haluat kopioida kaikki tiedostot hakemistosta, käytä _copyto_- tai _moveto_-alikomentoja.

Ladatessa yli 5 GB kokoiset tiedostot pilkotaan ja tallennetaan useana objektina. Objektit tallennetaan automaattisesti erilliseen bucketiin nimeltä `<bucket-nimi>_segments`. Esimerkiksi jos lataat suuren tiedoston bucketiin `2000620-raw-data`, varsinainen data tallennetaan osiin bucketiin `2000620-raw-data_segments`. Kohdebucketiin (`2000620-raw-data`) tulee pelkästään manifest-objekti, joka ilmoittaa, mitkä segmentit kuuluvat tallennettuun tiedostoon. Manifest-objektille tehdyt operaatiot heijastuvat automaattisesti segmentteihin. Normaalisti käyttäjien ei tarvitse operoida segmenttien buckettien kanssa ollenkaan, eikä niiden sisältämiä objekteja tule poistaa tai muokata.

## Bucketien ja objektien listaus {#list-buckets-and-objects}

Listaa kaikki projektiin kuuluvat bucketit:
<pre><b>rclone lsd allas:</b>
0 2019-06-06 14:43:40         0 2000620-raw-data
</pre>

Listaa bucketin sisältö:
<pre><b>rclone ls allas:2000620-raw-data</b>
677972 file.dat
</pre>

## Objektien lataus {#download-objects}

Käytä samoja `rclone copy` ja `rclone copyto`-komentoja tiedoston lataamiseen:
```text
rclone copy allas:2000620-raw-data/file.dat
```

Jos latauskomentoon lisää kohdekansion parametrina, Rclone luo lataukselle kansion:
```text
rclone copy allas:2000620-raw-data/file.dat doh
```

<pre><b>ls doh</b>
file.dat</pre>

<pre><b>ls -ld doh</b>
drwxr-xr-x  3 user  staff  96 Jun  6 14:58 doh
</pre>

## Hakemiston synkronointi {#synchronizing-a-directory}

Yksi tapa siirtää tietoa Allaksen ja laskentaympäristön välillä on synkronointi. Kopioinnin ja synkronoinnin ero on, että kopiointi vain lisää uusia objekteja tai tiedostoja lähteestä kohteeseen, mutta synkronointi voi lisäksi poistaa dataa kohteesta, jotta se vastaa lähdettä. Tämä tekee synkronoinnista tehokasta, mutta myös mahdollisesti vaarallista.

Esimerkiksi _mydata_-kansio sisältää seuraavan rakenteen:
<pre>
<b>ls -R mydata</b>

mydata/:
file1.txt  setA  setB

mydata/setA:
file2.txt

mydata/setB:
file3.txt  file4.txt
</pre>

Esimerkki _sync_-toiminnon käytöstä (huomaa, että kohdeparametri vaatii kansion nimen (_mydata_)):

```text
rclone sync mydata allas:2000620-raw-data/mydata
```

<pre><b>rclone ls allas:2000620-raw-data</b>
   677972 mydata/file1.txt
    10927 mydata/setA/file2.txt
     1116 mydata/setB/file3.txt
     5075 mydata/setB/file4.txt
</pre>

Oletetaan, että tallennamme uusia tiedostoja (_file5.txt_ ja _file6.txt_) alihakemistoon _mydata/setC_ ja samanaikaisesti poistetaan tiedosto _mydata/setB/file3.txt_. Kun _rclone sync_ ajetaan uudelleen, uusi data lisätään Allakseen ja objekti _mydata/setB/file3.txt_ poistetaan.

<pre><b>rclone sync mydata allas:2000620-raw-data/mydata</b>

<b>rclone ls allas:2000620-raw-data</b>
   677972 mydata/file1.txt
    10927 mydata/setA/file2.txt
     5075 mydata/setB/file4.txt
     1265 mydata/setC/file5.txt
     4327 mydata/setC/file6.txt
</pre>

Yllä olevissa esimerkeissä Allasta on käytetty muutettavaan kohteeseen. Komentoa voi kuitenkin käyttää myös päinvastaisessa suunnassa:
```text
rclone sync allas:2000620-raw-data/mydata mydata
```

Tämä palauttaa Allakseen ladatun datan _mydata_-kansioon. Huomaa kuitenkin, että mikäli olet lisännyt uutta dataa _mydata_-kansioon synkronoinnin jälkeen, tämä uusi data poistetaan synkronoinnin yhteydessä.