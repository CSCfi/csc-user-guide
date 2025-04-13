
# Allaksen käyttö Rclonella {#using-allas-with-rclone}

Tämä luku sisältää ohjeet Allaksen käyttämiseen [Rclonen](https://rclone.org/) kanssa Puhti- ja Mahti-laskentaympäristöissä. _Rclone_ tarjoaa erittäin tehokkaan ja monipuolisen tavan käyttää Allasta ja muita objektitallennuspalveluja. Se pystyy käyttämään sekä S3- että Swift-protokollia (ja monia muita). Tällä hetkellä CSC-palvelimissa Swift-protokolla on oletusvaihtoehto. 

> **VAROITUS:** Rclonella ei tulisi kopioida, siirtää tai nimetä uudelleen objekteja **Allaksen sisällä**. Rclone tarjoaa komentoja näihin toimenpiteisiin, mutta ne eivät toimi oikein yli 5 GB kokoisille tiedostoille.
> 
> **VAROITUS:** Jos Rclone-datan latausprosessi yli 5 GB kokoiselle tiedostolle keskeytyy, poista osittain ladattu objekti ennen uudelleen käynnistämistä. Muuten Rclone saattaa joskus ilmoittaa onnistuneesta datan latauksesta, vaikka kaikkea tietoa ei ole kopioitu Allakseen.

Rclonen perussyntaksi:
<pre>
rclone <i>käsky vaihtoehdot lähde:polku kohde:polku</i> 
</pre>

Useimmiten käytetyt Rclone-komennot:

*    [rclone copy]( https://rclone.org/commands/rclone_copy/) – Kopioi tiedostoja lähteestä kohteeseen, ohittaa jo kopioituja.
*    [rclone sync](https://rclone.org/commands/rclone_sync/) – Tekee lähteestä ja kohteesta identtisiä, muokkaa vain kohdetta.
*    [rclone move](https://rclone.org/commands/rclone_move/) – Siirtää tiedostoja lähteestä kohteeseen.
*    [rclone delete](https://rclone.org/commands/rclone_delete/) – Poistaa sisällön polusta.
*    [rclone mkdir](https://rclone.org/commands/rclone_mkdir/) – Luo polun, jos se ei jo ole olemassa.
*    [rclone rmdir](https://rclone.org/commands/rclone_rmdir/) – Poistaa polun.
*    [rclone check](https://rclone.org/commands/rclone_check/) – Tarkistaa, vastaavatko tiedostot lähteissä ja kohteissa.
*    [rclone ls](https://rclone.org/commands/rclone_ls/) – Listaa kaikki objektit polussa, mukaan lukien koko ja polku.
*    [rclone lsd](https://rclone.org/commands/rclone_lsd/) – Listaa kaikki hakemistot/säiliöt/sanko polussa.
*    [rclone lsl](https://rclone.org/commands/rclone_lsl/) – Listaa kaikki objektit polussa, mukaan lukien koko, muokkausaika ja polku.
*    [rclone lsf](https://rclone.org/commands/rclone_lsf/) – Listaa objektit virtuaalisen hakemistorakenteen mukaisesti objektin nimien perusteella.
*    [rclone cat](https://rclone.org/commands/rclone_cat) – Yhdistää tiedostot ja lähettää ne stdout:lle.
*    [rclone copyto](https://rclone.org/commands/rclone_copyto/) – Kopioi tiedostoja lähteestä kohteeseen, ohittaa jo kopioituja.
*    [rclone moveto](https://rclone.org/commands/rclone_moveto/) – Siirtää tiedoston tai hakemiston lähteestä kohteeseen.
*    [rclone copyurl](https://rclone.org/commands/rclone_copyurl/) – Kopioi URL:n sisällön kohteeseen tallentamatta sitä tmp-tallennukseen.

Laajempi luettelo löytyy [Rclonen manuaalisivuilta](https://rclone.org/docs/) tai kirjoittamalla Puhtiin komento `rclone`.

## Autentikointi {#authentication}

Ensimmäinen askel on autentikoitua projektiin Allaksessa. Rclone voi käyttää sekä Swift- että S3-protokollia, mutta näillä yhteyksillä on eri nimet rclone-komennoissa.

Tässä dokumentissa kuvataan, miten Rclonea käytetään CSC:n laskentaympäristössä (Puhti ja Mahti). Voit käyttää rclonea myös paikallisella tietokoneellasi. Ohjeet paikallisesti asennetun Rclonen konfigurointiin ovat täällä

* [Paikallinen Rclone-konfiguraatio Allekse](./rclone_local.md)

### Rclone Swift-protokollalla CSC:n supertietokoneilla {#rclone-with-swift-on-csc-supercomputers}

Allaksen oletusprotokolla on Swift. Puhti- ja Mahti-ympäristöissä Swift-pohjainen Allas-yhteys aktivoidaan komentoja käyttäen:
```text
module load allas
allas-conf
```
`allas-conf`-komento pyytää CSC-salasanaasi (yliopiston/Haka-salasana ei toimi tässä). Se listaa projektisi Allaksessa ja pyytää määrittämään käytettävän projektin. Sitten _allas-conf_ luo Rclone-konfiguraatiotiedoston Allas-palvelulle ja autentikoi yhteyden valittuun projektiin. Rclone-komennossa tämä Swift-pohjainen yhteys mainitaan etäyhteyden nimellä `allas:`. Autentikointitiedot tallennetaan kuori- muuttujissa `OS_AUTH_TOKEN` ja `OS_STORAGE_URL`, jotka ovat voimassa jopa kahdeksan tuntia. Kuitenkin, voit päivittää autentikoinnin milloin vain suorittamalla _allas-conf_ uudelleen. Ympäristömuuttujat ovat saatavilla vain kyseiselle sisäänkirjautumissessioille, joten jos kirjaudut Puhdille toisessa istunnossa, sinun on autentikoiduttava uudelleen päästäksesi Allakseen.

### Rclone S3-protokollalla CSC:n supertietokoneilla {#rclone-with-s3-on-csc-supercomputers}

Jos haluat käyttää Allasta S3-protokollalla, suorita `allas-conf`-komento `--mode S3` -valinnalla.
```text
module load allas
allas-conf --mode S3
```
Tämä komento avaa pysyvän S3-pohjaisen yhteyden Allakseen. Rclone voi nyt viitata tähän yhteyteen etäyhteyden nimellä `s3allas:`. Alla olevissa esimerkeissä käytetään Swift-pohjaista `allas:`-etämääritelmää, mutta jos olet määrittänyt S3-yhteyden, voit korvata sen `s3allas:`. Huomaa, että voit käyttää samanaikaisesti sekä `allas:` että `s3allas:` ja että ne voivat silti käyttää eri Allas-projekteja. Vältä kuitenkin protokollien sekoittamista. Jos objekti ladataan käyttäen `allas:`, tee myös kaikki toiminnot `allas:` kanssa.

## Luo sankoja ja lataa objekteja {#create-buckets-and-upload-objects}

Allaksen data on järjestetty kontteihin, joita kutsutaan sankoiksi. Voit pitää niitä juuritason hakemistoina. Kaikilla sankoilla Allaksessa on oltava yksilölliset nimet – et voi luoda sankoa, jos joku muu projekti on jo käyttänyt kyseistä sankonimeä. On hyvä nyrkkisääntö lisätä jotain projekti- tai käyttäjäkohtaista sankonimeen kuten _2000620-raw-data_. Katso [tarkistuslistan](../introduction.md#naming-buckets) ohjeet kuinka nimetä sanko.

_Rclonella_: luodaan sanko:
```text
rclone mkdir allas:2000620-raw-data
```
Ladataksesi tiedoston käytä komentoa ```rclone copy```:
```text
rclone copy file.dat allas:2000620-raw-data/
```
Yllä oleva komento luo objektin _file.dat_ sankoon _2000620-raw-data_.
Jos käytät `rclone move` sen sijaan että `rclone copy`, ladatun tiedoston (file.dat)
paikallinen versio poistetaan kopioinnin jälkeen.

_copy_ ja _move_ käskyt toimivat vain tiedostoilla. Jos haluat kopioida kaikki tiedostot hakemistosta, käytä _copyto_ tai _moveto_ käskyjä.

Latauksen aikana, tiedostot jotka ovat suurempia kuin 5 GB pilkotaan ja tallennetaan useiksi objekteiksi. Objektit tallennetaan automaattisesti erilliseen sankoon nimeltä `<sanko-nimi>_segments`. Esimerkiksi, jos lataisit suuren tiedoston `2000620-raw-data`, todellinen data tallennetaan useiksi paloiksi sankoon `2000620-raw-data_segments`. Kohdesanko (`2000620-raw-data`) sisältää vain manifesti-objektin, joka kertoo mitkä segmentit muodostavat tallennetun tiedoston. Toimet manifesti-objektissa heijastuvat automaattisesti segmentteihin. Normaalisti käyttäjien ei tarvitse käsitellä segmentti-sankoja lainkaan, ja näiden sankojen sisällä olevia objekteja ei pitäisi poistaa tai muokata.

## Listaa sankoja ja objekteja {#list-buckets-and-objects}

Listaa kaikki projektiin kuuluvat sangot:
<pre><b>rclone lsd allas:</b>
0 2019-06-06 14:43:40         0 2000620-raw-data
</pre>

Listaa sankon sisältö: 
<pre><b>rclone ls allas:2000620-raw-data</b>
677972 file.dat
</pre>

## Lataa objekteja {#download-objects}

Käytä samoja `rclone copy` ja `rclone copyto` komentoja tiedoston lataamiseen:
```text
rclone copy allas:2000620-raw-data/file.dat
```

Jos sisällytät kohdeparametrin latauskomentoon, Rclone luo hakemiston latausta varten:
```text
rclone copy allas:2000620-raw-data/file.dat doh
```

<pre><b>ls doh</b>
file.dat</pre>

<pre><b>ls -ld doh</b>
drwxr-xr-x  3 user  staff  96 Jun  6 14:58 doh
</pre>

## Kansion synkronointi {#synchronizing-a-directory}

Yksi tapa siirtää tietoa Allaksen ja laskentaympäristön välillä on synkronointi. Kopioinnin ja synkronoinnin ero on, että kun kopiointi vain lisää uusia objekteja tai tiedostoja lähteestä kohteeseen, synkronointi voi myös poistaa dataa kohteesta, jotta kohde vastaa lähdettä. Tämä ominaisuus tekee synkronoinnista erittäin tehokkaan mutta myös potentiaalisesti erittäin vaarallisen.

Esimerkiksi kansiolla nimeltä _mydata_ on seuraava rakenne:
<pre>
<b>ls -R mydata</b>

mydata/:
file1.txt  setA  setB

mydata/setA:
file2.txt

mydata/setB:
file3.txt  file4.txt
</pre>

Esimerkki _sync_:in käyttämisestä (huomaa, että kohdeparametri vaatii kansion nimen (_mydata_)):

```text
rclone sync mydata allas:2000620-raw-data/mydata
```

<pre><b>rclone ls allas:2000620-raw-data</b>
   677972 mydata/file1.txt
    10927 mydata/setA/file2.txt
     1116 mydata/setB/file3.txt
     5075 mydata/setB/file4.txt
</pre>

Oletetaan, että tallennamme uutta dataa (_file5.txt_ ja _file6.txt_) alihakemistoon _mydata/setC_ ja samalla poistamme tiedoston _mydata/setB/file3.txt_. Kun _rclone sync_-komento suoritetaan uudelleen, uusi data lisätään Allakseen ja objekti _mydata/setB/file3.txt_ poistetaan.

<pre><b>rclone sync mydata allas:2000620-raw-data/mydata</b>

<b>rclone ls allas:2000620-raw-data</b>
   677972 mydata/file1.txt
    10927 mydata/setA/file2.txt
     5075 mydata/setB/file4.txt
     1265 mydata/setC/file5.txt
     4327 mydata/setC/file6.txt
</pre>

Yllä olevissa esimerkeissä Allasta on käytetty kohteena jota muutetaan. Komentoa voidaan käyttää myös toiseen suuntaan:
```text
rclone sync allas:2000620-raw-data/mydata mydata
```

Tämä komento palauttaa ladatun datan Allaksesta _mydata_-kansioon. Huomaa kuitenkin, että jos olet lisännyt uusia tietoja _mydata_:an synkronoinnin jälkeen Allaksen kanssa, nämä tiedot poistetaan.
