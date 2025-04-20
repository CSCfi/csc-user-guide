# Työkalut asiakaspuolen salaukseen Allas-palvelussa {#tools-for-client-side-encryption-for-allas}

Allas ei ole sertifioitu korkeatasoinen tietoturvavarasto, joten sitä ei tule käyttää arkaluonteisen tiedon tallentamiseen luettavassa muodossa. Kuitenkin arkaluonteisia tietoja voidaan tallentaa Allas-palveluun, jos ne salataan asianmukaisesti ennen tallennusta objektitallennuspalveluun.

Arkaluonteista tietoa varten suosittelemme yleisesti [SD Connect -palvelua](../sensitive-data/sd_connect.md), joka tarjoaa selain- ja komentorivikäyttöliittymät ja salaa tiedot automaattisesti, kun ne tallennetaan Allasiin. 

Jos et halua käyttää SD Connectia, alla esittelemme joitakin vaihtoehtoisia tapoja tallentaa arkaluonteisia tietoja Allasiin. Kun käytät Allaasta näiden salaustyökalujen kanssa, huomioi seuraavat:

1. Voit tallentaa salattua arkaluonteista tietoa Allasiin, mutta sinulla on oikeus purkaa salaus ainoastaan riittävän turvallisissa ympäristöissä. Esimerkiksi CSC:n HPC-ympäristö (eli Puhti, Mahti, LUMI) **ei** ole riittävän turvallinen arkaluonteisille tiedoille.

2. Käytä riittävän vahvoja salaus salasanoja ja säilytä ne turvallisesti.

3. Jos unohdat salauksen salasanan, data menetetään. CSC ei voi antaa sinulle uutta salasanaa tiedostojesi lukemiseen, sillä salasana on asetettu sinun toimestasi, ei CSC:n.

## 1. Yksittäisen tiedoston tai kansion salaaminen `a-put`:lla {#1-encrypting-a-single-file-or-directory-with-a-put}

Jos asennat [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils/)-paketin käyttämällesi koneelle, voit käyttää `a-put`:ia _--encrypt_-valinnalla salataksesi tiedoston tai kansion, jonka haluat ladata Allasiin. Voit käyttää joko symmetristä (eli salasanaan perustuvaa) salausta [**gpg**](https://gnupg.org/) -ohjelmalla tai epäsymmetristä avainpohjaista salausta [**crypt4gh**](https://crypt4gh.readthedocs.io/en/latest/) -ohjelmalla. Gpg on saatavilla useimmissa linux-järjestelmissä, kun taas crypt4gh ei ole vielä laajasti käytössä, joten se on asennettava erikseen, jos haluat käyttää epäsymmetristä salausta.

Huomaa, että oletuksena `a-put` luo lisämetatiedon objektin, joka sisältää tiedostojen tiedot. Kun _--encrypt_-vaihtoehtoa käytetään, itse data salataan, mutta metatieto-objektia (eli _\_ameta_tiedostoja) ei salata. Jos tiedostonimet eivät saa olla selväkielisiä, tulee metatiedon luominen kytkeä pois päältä _--no-ameta_-valinnalla.

### Symmetrinen gpg-salaus {#symmetric-gpg-encryption}

Symmetrinen gpg-salaus onnistuu komennolla:

```text
a-put --encrypt gpg data_dir -b my_allas_bucket
```
Kun käytössä on _--encrypt gpg_ -valinta, data salataan `gpg`-komennolla käyttäen _AES256_-salausalgoritmia, jota pidetään yleisesti riittävän hyvänä arkaluonteisille tiedoille. Komennon suoritus pyytää salasanaa ja sen vahvistusta salaukseen. Tässä tavassa vain tiedoston tai kansion sisältö salataan – objektin nimi ja metatiedot säilyvät selväkielisinä.

Kun noudat datan `a-get`-komennolla, salasanaa kysytään, jotta objekti voidaan purkaa latauksen jälkeen.

```text
a-get my_allas_bucket/data_dir.tar.zst.gpg
```

### Epäsymmetrinen crypt4gh-salaus {#asymmetric-crypt4gh-encryption}

Jos haluat käyttää epäsymmetristä `crypt4gh`-salausta, tarvitset julkisen avaimen tiedoston salaukseen ja salaisen avaimen tiedoston purkamiseen.
Puhti-ympäristössä crypt4gh otetaan käyttöön komennolla:
```text
module load allas
```
Avaimet voidaan luoda esimerkiksi komennolla:
```text
crypt4gh-keygen --sk allaskey.sec --pk allaskey.pub
```
Data voidaan nyt ladata Allasiin komennolla:
```text
a-put --encrypt c4gh --pk allaskey.pub data_dir -b my_allas_bucket
```
Yllä oleva komento salaa ensin datan käyttäen `crypt4gh`:tä ja julkista avainta ja lataa sitten salatun datan Allasiin. Huomaa, että salausvaiheessa et tarvitse salaista avainta. Voit toimittaa julkisen avaimen toiselle palvelimelle (ja käyttäjälle), jotta data voidaan ladata turvallisesti ulkoisesta, suojatusta ympäristöstä Allasiin. Salainen avain tarvitaan vain siinä ympäristössä, jossa data palautetaan Allasista:
```text
a-get --sk allaskey.sec my_allas_bucket/data_dir.tar.zst.c4gh
```
Yllä oleva komento lataa salatun objektin Allasista, kysyy salaisen avaimen salasanan ja purkaa datan luettavaan muotoon.

## 2. Salatun tallennusrepositorion luominen rclone:lla {#2-creating-encrypted-repository-with-rclone}

`rclone` tarjoaa asiakaspuolen salausominaisuuden, jonka avulla voit luoda salatun datavaraston Allasiin. Tässä menetelmässä määritellään kerran salattu `rclone`-yhteys Allasiin ja kun tämä yhteys on käytössä, kaikki siirrettävä data salataan automaattisesti. `rclone`-työkalun automaattinen salaus perustuu _Salsa20_-virtasalaukseen. Salsa20 ei ole yhtä yleinen kuin AES256, mutta se on yksi [eSTREAM](https://www.ecrypt.eu.org/stream/)-projektin suosittelema salausalgoritmi Euroopassa.

Tässä esimerkissä oletamme, että käytössäsi on palvelin, johon on asennettu sekä [rclone](https://rclone.org/) että [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils/). Ensin sinun tulee konfiguroida tavallinen, salaamaton swift-yhteys Allasiin. Tämä onnistuu _allas-cli-utils_-paketin mukana tulevalla `allas-conf`-skriptillä:
```text
source allas-cli-utils/allas_conf -u your-csc-username -p your-csc-project-name
```

Kun tavallinen swift-yhteys Allasiin on tehty, voit määritellä salatun bucketin Allas-alueellesi. Konfiguraation aloitus tapahtuu komennolla `rclone config`. 

`allas-conf`-skripti on jo luonut `rclone`-asetustiedoston ja `rclone remote` on nimetty _allas_:ksi.

Ensimmäisessä vaiheessa valitse _n_ uuden _remoten_ luomiseksi.
Konfigurointi pyytää nimeä uudelle rclone _remotelle_.
Tässä tapauksessa uusi remote nimetään _allas-crypt_.

<pre>
[kkayttaj@puhti-login11 ~]$ <b>rclone config</b>
Current remotes:

Name                 Type
====                 ====
allas                swift

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> <b>n</b>
name> <b>allas-crypt</b>
</pre>
Seuraavaksi pyydetään valitsemaan tallennustyyppi.
Valitse vaihtoehto 10 _Encrypt/Decrypt a remote_.
<pre>
Storage> <b>10</b>
</pre>
Tässä vaiheessa määritetään Allas-bucketi, jota tullaan käyttämään salatulle datalle. Määrittäessä bucketia, huomioi että on määriteltävä sekä bucketin nimi että _site_ (eli rclone-yhteyden nimi), jossa bucket sijaitsee. Allasin tapauksessa remoten nimi on _allas:_. Itse bucketin nimi tulee olla uniikki kaikkien Allas-käyttäjien kesken. Tässä esimerkissä käytetään määrittelyä _allas:2001659-crypt_, joka tarkoittaa, että salattu data tallennetaan Allasiin bucketiin _2001659-crypt_.
<pre>
Remote to encrypt/decrypt.
Normally should contain a ':' and a path, eg "myremote:path/to/dir",
"myremote:bucket" or maybe "myremote:" (not recommended).
Enter a string value. Press Enter for the default ("").
remote> <b>allas:2001659-crypt</b>
</pre>
Konfigurointi kysyy seuraavaksi, salataanko objektin ja kansion nimet. Tässä tapauksessa nimet salataan, joten valitse _1_ molempiin kohtiin.

Tämän jälkeen sinun tulee määritellä kaksi salasanaa: pääsalasana ja ns. _suolattu salasana_ (_salt password_). Tämä salasanapari käytetään salaukseen. Voit määritellä salasanat itse tai antaa konfiguraation luoda ne puolestasi. Joka tapauksessa säilytä salasanat turvallisesti; muutkin käyttäjät ja palvelimet voivat tarvita niitä. Nyt määritys on valmis ja uusi rclone-remote nimeltään _allas-crypt_ on luotu. Voit poistua konfiguroinnista.

Current remotes:
<pre>
Name                 Type
====                 ====
allas                swift
allas-crypt          crypt

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q><b>q</b>
</pre>

Nyt repository on käyttövalmis. Oletetaan, että sinulla on kansio nimeltä _job_6_, joka sisältää tiedostoja ja hakemistoja:
<pre>
[kkayttaj@puhti-login11 ~]$ <b>ls job_6</b>
hello.xrsl  results  results.1601291937.71  runhello.sh
</pre>

Voit nyt ladata kansion sisällön salattuun bucketiin.
```text
rclone copy job_6 allas-crypt:job_6
```
Data on nyt kopioitu Allasiin ja voit tarkistaa siirretyt tiedostot komennolla:
<pre><b>rclone ls allas-crypt:job_6</b>
       77 runhello.sh
       11 results.1601291937.71/std.out
       86 results.1601291937.71/std.err
      117 hello.xrsl
       11 results/std.out
       86 results/std.err
 </pre>

`allas-crypt`-remote tulkkaa datan salatusta bucketista (allas:2001659-crypt) automaattisesti luettavaan muotoon. Jos kuitenkin tarkastelet salattua buckettia suoraan, näet että objektien nimet sekä tallennettu data ovat salatussa muodossa:

<pre>[kkayttaj@puhti-login11 ~]$ <b>rclone ls allas:2001659-crypt</b>
      125 4lpbj55pc5v8t119q0tp2o6k58/36sb832och3tde30k9nlks3dpo
       59 4lpbj55pc5v8t119q0tp2o6k58/90alcaodph3386197agf252t5b97f144n88e99m9ire5tcpqu380/flqitnrsrc8iloggbc4ouagukg
      134 4lpbj55pc5v8t119q0tp2o6k58/90alcaodph3386197agf252t5b97f144n88e99m9ire5tcpqu380/gvie6dv3s50v32qptl30960me4
      405 4lpbj55pc5v8t119q0tp2o6k58/a6rlk2hr489roehagfu6iest38
      165 4lpbj55pc5v8t119q0tp2o6k58/kmqnruv14agevg6okod0io2fl0
       59 4lpbj55pc5v8t119q0tp2o6k58/o515vd0l1bp270v7gdc7m3tpbo/flqitnrsrc8iloggbc4ouagukg
      134 4lpbj55pc5v8t119q0tp2o6k58/o515vd0l1bp270v7gdc7m3tpbo/gvie6dv3s50v32qptl30960me4
      352 4lpbj55pc5v8t119q0tp2o6k58/p87n5ins7g0hvfh06r6o6a91n0
</pre>

Vastaavasti komento:
```text
rclone copy allas-crypt:job_6/hello.xrsl ./
```
Lataa ja purkaa salatun tiedoston _hello.xrsl_ Allasista paikalliselle levylle.

Allas-yhteyksien asetukset tallennetaan oletuksena rclone:n asetustiedostoon sijaintiin `$HOME/.config/rclone/rclone.conf`

Tässä tapauksessa _allas-crypt_-osuuden asetustiedosto näyttää esimerkiksi tältä:
```text
[allas-crypt]
type = crypt
remote = allas:2001659-crypt
filename_encryption = standard
directory_name_encryption = true
password = A_JhQdTOEIx0ajyWb1gCvD2z0gBrEVzy41s
password2 = UgmByNqlnb8vCZrFgpaBtUaQrgJkx30
```
Asetus ei sellaisenaan ole sidottu mihinkään tiettyyn palvelimeen tai käyttäjään. Yhdistäminen salattuun bucketiin onnistuu siis keneltä tahansa, jolla on 1) pääsy kyseiseen Allas-projektiin sekä 2) samat asetukset (mukaan lukien salasanat) omassa rclone-asetustiedostossaan. Tämä on kätevää, kun tarvitset salatun tallennustilan, jota käyttää useampi luotettu henkilö tai paikka. Tämä aiheuttaa kuitenkin mahdollisia tietoturvariskejä, sillä salasanat jaetaan usean käyttäjän kesken. Lisäksi asetustiedostossa salasanat ovat vain _naamioituja_, eivät salattuja.

Turvallisuuden parantamiseksi `rclone`-asetustiedosto voidaan salata. Tämä onnistuu ajamalla uudestaan `rclone conf` -komento.
Valitse tällöin _s_ kohdasta _Set configuration password_ ja sitten _a_ lisätäksesi salasanan. Salasanan määrittelyllä on kaksi vaikutusta:

1. `rclone`-asetustiedosto muutetaan salattuun muotoon.
2. Joka kerta kun suoritat jonkin `rclone`-komennon, sinun on annettava asetustiedoston salasana, jotta rclone voi lukea asetukset.

Jälkimmäinen saattaa olla hieman hankalaa, varsinkin jos käytät lähinnä normaalia, salaamatonta Allas-yhteyttä. Tämän vuoksi onkin usein järkevämpää luoda erillinen rclone-asetustiedosto salattua Allas-käyttöä varten ja sitten tarvittaessa käyttää _--config_-valintaa encrypted-konfiguraation kanssa.

Esimerkiksi:

Kopioi nykyinen `rclone`-asetustiedosto (ennen salatun yhteyden määrittelyä).

```text
cp $HOME/.config/rclone/rclone.conf $HOME/rc-encrypt.conf
```
Sitten suorita `rclone config` komento lisätäksesi salatun Allas-bucketin tiedot ja salaamalla asetustiedosto. Molemmat toimenpiteet voi tehdä yhdessä `rclone config` -istunnossa.
```text
rclone config --config $HOME/rc-encrypt.conf
```
Asetustiedoston salausavain voi ja kuuluu olla henkilökohtainen.

Nyt voit käyttää suojattua asetustiedostoa `rclone`-komennon kanssa. Esimerkiksi:

```text
rclone copy --config $HOME/rc-encrypt.conf job_6 allas-crypt:job_6
```

## Restic – Varmuuskopiointityökalu, jossa on sisäänrakennettu salaus {#restic---backup-tool-that-includes-encryption}

[Restic](https://restic.net/) on varmuuskopiointiohjelma, joka voi käyttää Allaasta varmuuskopioitavan datan tallennuspaikkana. Datan sijaan `restic` tallentaa tiedot kokoelmana hasheja. Tämä mahdollistaa tehokkaan tallennuksen aineistoille, joissa on vain pieniä muutoksia. Näin ollen datasetistä voidaan tallentaa eri versioita siten, että uuden version tapauksessa tallennetaan vain muutokset edelliseen verrattuna. Tämä mahdollistaa myös sen, että datasta voidaan palauttaa paitsi viimeisin myös aiempia varmuuskopioituja versioita.

Pilatun lisäksi `restic` salaa datan käyttäen AES256-salausalgoritmia. Allaasiin tarkoitetussa erityistyökalussa, `allas-backup` (saatavilla Puhti- ja Mahti-koneissa) on kiinteä, ennalta määritelty salaus-salasana, joten sitä ei tulisi käyttää, jos vaaditaan korkea tietoturvataso. Niissä tapauksissa voit käyttää `restic`-ohjelmaa suoraan.

Jotta voit käyttää Allaasta `restic`-tallennuspaikkana, avaa ensin yhteys Allaasiin. Kun käytät `restic`:iä ensimmäistä kertaa, sinun tulee luoda `restic`-repository.
Repositoryn määrittelyssä annetaan protokolla (tässä tapauksessa `swift`), sijainti (eli bucketin nimi Allasissa) ja prefiksi tallennettaville datoille. Esimerkiksi: 
<pre><b>restic init --repo swift:123_restic:/backup</b>
enter password for new repository: <b>************</b>
enter password again: <b>************</b>

created restic repository a70df2ced1 at swift:123_restic:/backup

Please note that knowledge of your password is required to access
the repository. Losing your password means that your data is
irrecoverably lost.
</pre>

Alustusprosessi kysyy repositoriesi salaus-salasanaa. 

Nyt voit varmuuskopioida tiedoston tai kansion Restic-repositoryyn Allasissa. Alla olevassa esimerkissä kansio _my_data_ varmuuskopioidaan.

<pre> <b>restic backup --repo swift:123_restic:/backup my_data/</b>
enter password for repository: <b>************</b>
repository a70df2ce opened successfully, password is correct
created new cache in /users/kkayttaj/.cache/restic

Files:         258 new,     0 changed,     0 unmodified
Dirs:            0 new,     0 changed,     0 unmodified
Added to the repo: 2.018 MiB

processed 258 files, 2.027 MiB in 0:00
snapshot a706c054 saved
</pre>

Muutettuasi yhtä tiedostoa _my_data_-kansiossa tehdään toinen varmuuskopio:
<pre><b>restic backup --repo swift:123_restic:/backup my_data/</b>
enter password for repository: <b>************</b>
repository a70df2ce opened successfully, password is correct

Files:           0 new,     1 changed,   257 unmodified
Dirs:            0 new,     0 changed,     0 unmodified
Added to the repo: 1.154 KiB

processed 258 files, 2.027 MiB in 0:00
snapshot e3b46fe2 saved
</pre>

Komennolla `restic snapshots` nähdään, että my_data:sta on repositoryssa kaksi eri versiota:

<pre><b>restic snapshots --repo swift:123_restic:/backup</b> 
enter password for repository: <b>************</b>
repository a70df2ce opened successfully, password is correct
ID        Time                 Host          Tags        Paths
-------------------------------------------------------------------------------------------
a706c054  2021-02-12 14:43:03  r07c52.bullx              /run/nvme/job_4891841/data/my_data
e3b46fe2  2021-02-12 14:47:18  r07c52.bullx              /run/nvme/job_4891841/data/my_data
-------------------------------------------------------------------------------------------
2 snapshots
</pre>

Jos haluamme palauttaa ensimmäisen version, voimme ladata sen snapshot-id:llä ja komennolla `restic restore`.

<pre><b>restic restore --repo swift:123_restic:/backup a706c054 --target ./ </b>
enter password for repository: <b>************</b>
repository a70df2ce opened successfully, password is correct
found 3 old cache directories in /users/kkmattil/.cache/restic, run `restic cache --cleanup` to remove them
restoring <Snapshot a706c054 of [/run/nvme/job_4891841/data/my_data] at 2021-02-12 14:43:03.215110283 +0200 EET by kkayttaj@r07c52.bullx> to ./
</pre>

Varsinainen data tallennetaan salattuina hash-objekteina, jotka eivät ole suoraan käytettävissä muilla Allas-työkaluilla. Esimerkiksi yllä olevassa esimerkissä `restic` tallentamaa dataa bucketissa
_123_restic_ voidaan katsella esimerkiksi `rclone`-komennolla:
```
rclone ls allas:123_restic
      155 backup/config
     1349 backup/data/26/263a8a412486d0fe6278ec1992c3b2dc64352041ca4236de0ddab07a30e7f725
  2133179 backup/data/46/4643d0d98ef90363629561828a3c113c2ca1acbdefcd3ef0f548724501c1e8f3
   108646 backup/data/77/77f36c6b6f7b346010d76e6709c8e3e4a61a7bc25dce4ffee726fe2a9b208e48
      895 backup/data/b7/b757b4f8b370a3f7199d717128f8bcb90139c589b761d2d6e683cbb3943c32e9
      550 backup/index/3b824311bf222eb9131e83dc22b76ee1686a41deff8db73912a6ec4b58ec7c9c
    32326 backup/index/9e7e8858bc9e8cdcd96f7020ad9f1246629e3a80b2008c1debec30ac21c2b717
      458 backup/keys/9f47c0adcdaa29d1e89eab4763fbcf9269c834b6590b45fd9a0ac079e2ee483e
      272 backup/snapshots/a706c054a77edba31337669ebd851c80f34dfbc3ca92255dee1ff0c0cad8cedf
      348 backup/snapshots/e3b46fe293fae187a53296f8cde25f7aec9f896e4586d96ac4df78ba27cdd911
```
