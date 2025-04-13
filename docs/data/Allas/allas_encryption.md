# Asiakaspuolen salaustyökalut Allakselle {#tools-for-client-side-encryption-for-allas}

Allasta ei ole sertifioitu korkeatasoiseksi turvallisuusalustaksi, joten sitä ei pidä käyttää luottamuksellisen datan tallentamiseen luettavassa muodossa. Kuitenkin, jos luottamuksellinen data salataan asianmukaisesti ennen sen siirtämistä objektivarastoon, sitä voidaan tallentaa Allakseen.

Luottamuksellisen datan osalta suosittelemme yleensä [SD Connect -palvelua](../sensitive-data/sd_connect.md), joka tarjoaa verkkokäyttöliittymiä ja komentorivitoimintoja, jotka salaavat datan automaattisesti sen tallennuksen yhteydessä Allakseen. 

Jos jostain syystä et halua käyttää SD Connectia, alla on joitain vaihtoehtoisia lähestymistapoja luottamuksellisen datasi tallentamiseen Allakseen. Kun käytät Allasta näiden salausvälineiden kanssa, muista, että:

1. Voit tallentaa salattua luottamuksellista dataa Allakseen, mutta sen purkaminen on sallittua vain riittävän turvallisissa ympäristöissä. Esimerkiksi CSC:n HPC-ympäristö (eli Puhti, Mahti, LUMI) **ei** ole tarpeeksi turvallinen luottamukselliselle datalle.

2. Käytä tarpeeksi vahvoja salasanastoja salaukseen ja säilytä ne turvassa.

3. Jos unohdat salasanan, data on menetetty. CSC ei voi antaa sinulle uutta salasanaa datasi lukemiseen, koska salasana on määritetty sinun eikä CSC:n toimesta.

## 1. Yksittäisen tiedoston tai hakemiston salaaminen `a-put`:lla {#1-encrypting-a-single-file-or-directory-with-a-put}

Jos asennat [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils/) koneeseen, jota käytät, voit käyttää `a-put`:ia vaihtoehdolla _--encrypt_ salataksesi tiedoston tai hakemiston, jonka haluat ladata Allakseen. Voit käyttää joko symmetristä (eli salasanan) salausta [**gpg**](https://gnupg.org/) avulla tai epäsymmetristä avainpohjaista salausta [**crypt4gh**](https://crypt4gh.readthedocs.io/en/latest/) avulla. Gpg on saatavilla useimmissa linux-järjestelmissä, kun taas crypt4gh ei ole niin laajalti käytössä, joten saatat joutua asentamaan sen paikalliseen järjestelmääsi, jos haluat käyttää epäsymmetristä salausta.

Huomaa, että oletuksena `a-put` luo lisämetatiedosto-objektin, joka sisältää tietoa ladatuista tiedostoista. Kun _--encrypt_ vaihtoehtoa käytetään, varsinainen datasisältö salataan, mutta metatieto-objekteja (_\_ameta_ tiedostot) ei salata. Jos tiedostonimiä ei tule tallentaa luettavassa muodossa, metatieto-objektien luonti tulisi kytkeä pois päältä käyttämällä `a-put`:ia vaihtoehdolla _--no-ameta_.

### Symmetrinen gpg-salaus {#symmetric-gpg-encryption}

Symmetrinen gpg-salaus voidaan suorittaa komennolla:

```text
a-put --encrypt gpg data_dir -b my_allas_bucket
```

Kun vaihtoehto _--encrypt gpg_ on käytössä, data salataan `gpg`-komennolla käyttämällä _AES256_ salausalgoritmia, jota yleensä pidetään riittävän hyvänä luottamukselliselle datalle. Kun suoritat komennon, se kysyy salaus salasanaa ja salasana varmistusta. Tässä lähestymistavassa vain tiedoston tai hakemiston sisältö salataan. Objektin nimi ja metatiedot jäävät ihmisen luettavaan muotoon.

Kun haet dataa `a-get`:lla, sinulta kysytään salaus salasanaa, jotta objekti voidaan purkaa latauksen jälkeen.

```text
a-get my_allas_bucket/data_dir.tar.zst.gpg
```

### Epäsymmetrinen crypt4gh-salaus {#asymmetric-crypt4gh-encryption}

Jos haluat käyttää epäsymmetristä `crypt4gh`-salausta, sinulla on oltava julkinen avaintiedosto salausta varten ja salainen avaintiedosto purkamista varten.
Puhtissa sinun täytyy ensin tehdä `crypt4gh` käytettäväksi komennolla:
```text
module load allas
```
Nyt voit luoda avaimet komennolla:
```text
crypt4gh-keygen --sk allaskey.sec --pk allaskey.pub
```
Data voidaan nyt ladata Allakseen komennolla:
```text
a-put --encrypt c4gh --pk allaskey.pub data_dir -b my_allas_bucket
```
Yllä oleva komento salaa ensin datan käyttäen `crypt4gh`:ta ja julkista avainta ja sitten lataa salatun datan Allakseen. Huomaa, että salaus ei tarvitse salaisuutta avainta. Voit toimittaa julkisen avaimen toiselle palvelimelle (ja toiselle käyttäjälle) niin, että data voidaan turvallisesti ladata Allakseen ulkoisesta turvallisesta sijainnista. Salainen avain tarvitaan vain ympäristössä, johon data ladataan alas Allaksesta:
```text
a-get --sk allaskey.sec my_allas_bucket/data_dir.tar.zst.c4gh
```
Yllä oleva komento lataa salatun objektin Allaksesta, kysyy salaisen avaimen salasanaa ja purkaa sitten datan luettavaan muotoon.

## 2. Salausarkiston luominen rclone:lla {#creating-encrypted-repository-with-rclone}

`rclone`:lla on asiakaspuolen salausominaisuus, joka mahdollistaa salatun data-arkiston luomisen Allakseen. Tässä lähestymistavassa sinun on ensin määritettävä salattu `rclone`-yhteys Allakseen, ja kun tätä yhteyttä käytetään, kaikki siirrettävä data salataan automaattisesti. `rclone`:n automaattinen salaus perustuu _Salsa20_ suoravirta-salaimeen. Salsa20 ei ole yhtä laajalti käytetty kuin AES256, mutta se on yksi niistä salausvälineistä, joita Euroopan [eSTREAM](https://www.ecrypt.eu.org/stream/) projekti on suositellut.

Tässä esimerkissä oletetaan, että käytät palvelinta, jossa sinulla on [rclone](https://rclone.org/) ja [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils/) asennettu. Ensimmäinen tehtäväsi on määrittää normaali, salaamaton Swift-yhteys Allakseen. Tämä voidaan tehdä _allas-cli-utils_ pakettiin sisältyvällä `allas-conf` skriptillä:
```text
source allas-cli-utils/allas_conf -u your-csc-username -p your-csc-project-name
```

Kun olet määrittänyt normaalin Swift-yhdyskäytävän Allakseen, voit määrittää salatun säiliön Allas-alueellesi. Alkaaksesi määritysprosessin, suorita komento `rclone config`.

`allas-conf` skripti on jo luonut `rclone`-määritystiedoston, jossa `rclone remote` on nimetty _allas_.

Ensimmäisenä vaiheena valitse vaihtoehto: _n_ luodaksesi _uuden remote_:n. Määritysprosessi pyytää nimeämään uuden rclone _remote_:n. Tässä tapauksessa uusi remote nimetään _allas-crypt_:ksi.

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
Seuraavaksi määritysprosessi kysyy, määritätkö tallennustyypin. Valitse vaihtoehto 10 _Encrypt/Decrypt a remote_.
<pre>
Storage> <b>10</b>
</pre>
Seuraavassa vaiheessa sinun pitää määrittää Allaksen säiliö, jota käytetään salattua dataa varten. Kun määrität säiliön, huomaa, että sinun on määritettävä sekä säiliö että sivusto (eli rclone-yhteyden nimi), jossa säiliö sijaitsee. Allaksen tapauksessa etäyhteyden nimi on _allas:_. Varsinainen säiliön nimi tulee olla ainutlaatuinen kaikkien Allas-käyttäjien kesken. Tässä tapauksessa käytämme määritelmää _allas:2001659-crypt_, joka määrittelee, että salattu data tallennetaan Allakseen säiliöön _2001659-crypt_.

<pre>
Remote to encrypt/decrypt.
Normally should contain a ':' and a path, eg "myremote:path/to/dir",
"myremote:bucket" or maybe "myremote:" (not recommended).
Enter a string value. Press Enter for the default ("").
remote> <b>allas:2001659-crypt</b>
</pre>
Seuraavaksi määritysprosessi kysyy, salataanko objektien ja hakemistojen nimet. Tässä tapauksessa salaa nimet, joten valitset _1_ molemmissa tapauksissa.

Tämän jälkeen sinun täytyy määritellä kaksi salasanaa: pääsalisana ja niin sanottu _suola_salasana. Tätä salasanojen paria käytetään salaukseen. Voit määrittää nämä salasanat itse tai antaa määritysprosessin luoda ne. Joka tapauksessa säilytä käytetyt salasanat turvallisesti. Muut käyttäjät ja palvelimet saattavat tarvita niitä myös. Nyt asetus on valmis ja `rclone remote`:lle on määritelty uusi etäyhteys nimeltä _allas-crypt_. Voit nyt sulkea määritysprosessin.

Nykyiset etäyhteydet:
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

Nyt arkisto on valmis käytettäväksi. Sanotaan, että sinulla on hakemisto nimeltä _job_6_, joka sisältää joitain tiedostoja ja hakemistoja:
<pre>
[kkayttaj@puhti-login11 ~]$ <b>ls job_6</b>
hello.xrsl  results  results.1601291937.71  runhello.sh
</pre>

Voit nyt ladata tämän hakemiston sisällön salattuun säiliöön.
```text
rclone copy job_6 allas-crypt:job_6
```
Data on nyt kopioitu Allakseen ja voit tarkistaa ladatut tiedostot komennolla:
<pre><b>rclone ls allas-crypt:job_6</b>
       77 runhello.sh
       11 results.1601291937.71/std.out
       86 results.1601291937.71/std.err
      117 hello.xrsl
       11 results/std.out
       86 results/std.err
</pre>

`allas-crypt remote` kääntää datan salatusta säiliöstä (allas:2001659-crypt) automaattisesti luettavaan muotoon. Jos kuitenkin tutkit suoraan salatun säiliön sisältöä, huomaat, että objektin nimet sekä tallennettu data ovat salatussa muodossa:

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
Lataa ja purkaa salatun _hello.xrsl_-tiedoston Allaksesta paikalliselle levylle.

Allas-yhteyksien määritykset tallennetaan oletuksena rclone-määritystiedostoon `$HOME/.config/rclone/rclone.conf`-hakemistoon.

Tässä tapauksessa _allas-crypt_ määrittävä osa määritystiedostossa voisi näyttää tältä:
```text
[allas-crypt]
type = crypt
remote = allas:2001659-crypt
filename_encryption = standard
directory_name_encryption = true
password = A_JhQdTOEIx0ajyWb1gCvD2z0gBrEVzy41s
password2 = UgmByNqlnb8vCZrFgpaBtUaQrgJkx30
```
Määritys sellaisenaan ei ole sidottu mihinkään tiettyyn palvelimeen tai käyttäjätunnukseen. Yhteyden salaamaan säiliöön voi avata kuka tahansa, jolla on 1) pääsy Allas-projektiin ja 2) samat asetukset (mukaan lukien salasanat) omassa rclone-määritystiedostossaan. Tämä on kätevää, kun tarvitaan salattua tietovarastoa, jota voivat käyttää useat luotetut henkilöt ja sivustot. Tämä aiheuttaa kuitenkin potentiaalisia turvallisuusongelmia, koska samaa salasanaa käyttää useat käyttäjät. Lisäksi määritystiedostossa salasanat ovat vain _hämärretyt_, mutta eivät salattuja.

Turvallisuuden parantamiseksi `rclone`-määritystiedosto voidaan salata. Tämä voidaan tehdä suorittamalla `rclone conf`-komento uudelleen. Tässä tapauksessa valitse _s_ siirtyäksesi _Set configuration password_ -kohtaan ja sitten _a_ lisätäksesi salasanan. Salasanan asettamisella on kaksi vaikutusta:

1. `rclone`-määritystiedosto muunnetaan salattuun muotoon.
2. Jokaisella `rclone`-komennolla, sinun on annettava määritystiedoston salasana, jotta `rclone` voi lukea asetukset.

Toinen ominaisuus voi olla melko ärsyttävää, erityisesti jos käytät pääasiassa normaalia, salaamatonta Allas-yhteyttä. Tästä syystä voi olla järkevämpää luoda erillinen rclone-määritystiedosto salattua Allas-käyttöä varten ja sitten, kun salausta tarvitaan, määritellä salatun määritystiedoston käyttö rclone-vaihtoehdolla _--config_.

Esimerkiksi:

Tee kopio olemassa olevasta `rclone`-määritystiedostosta (ennen kuin määrität yllä kuvatun salatun yhteyden).

```text
cp $HOME/.config/rclone/rclone.conf $HOME/rc-encrypt.conf
```
Suorita sitten `rclone config`-komento lisätäksesi salatulle Allas-säiliölle määritystiedot ja sitten salataksesi määritystiedoston. Voit tehdä molemmat vaiheet yhdessä `rclone config`-sessiossa.
```text
rclone config --config $HOME/rc-encrypt.conf
```
Määritystiedoston salausavain voi ja sen tulee olla henkilökohtainen.

Nyt voit käyttää suojattua määritystiedostoasi `rclone`-komennon kanssa. Esimerkiksi:

```text
rclone copy --config $HOME/rc-encrypt.conf job_6 allas-crypt:job_6
```

## Restic - Varmuuskopiointityökalu, joka sisältää salauksen {#restic-backup-tool-that-includes-encryption}

[Restic](https://restic.net/) on varmuuskopiointiohjelma, joka voi käyttää Allasta varmuuskopioidun datan tallennustilana. Sen sijaan, että data tuodaan suoraan, `restic` tallentaa datan hash-kokoelmina. Tämä ominaisuus mahdollistaa datasetien tehokkaan tallennuksen, jotka sisältävät pieniä muutoksia. Näin datasetin eri versiot voidaan tallentaa niin, että uuden datasetin version myötä vain muutokset edelliseen versioon verrattuna on tallennettava. Tämä lähestymistapa mahdollistaa myös aiempien versioiden hakemisen, ei vain uusimman version.

Hashauksen lisäksi `restic` salaa datan käyttääen AES256-salainta. Allas-spesifi varmuuskopiointityökalu, `allas-backup` (saatavilla Puhtissa ja Mahtissa) perustuu `restic`:iin, mutta käyttää kiinteää, ennalta määriteltyä salasanointia, jota ei tule käyttää, jos korkeaa turvallisuustasoa vaaditaan. Tällaisissa tapauksissa voit käyttää `restic`:ia suoraan.

Käyttääksesi Allasta `restic`:in tallennuspaikkana, avaa ensin yhteys Allakseen. Kun aloitat `restic`:in käytön ensimmäistä kertaa, sinun täytyy määrittää `restic`-arkisto.
Arkiston määrittely sisältää protokollan (`swift` tässä tapauksessa), sijainnin, joka on säiliön nimi Allaksen tapauksessa, ja ennakkomäärityksen tallennetuille dataobjekteille. Esimerkiksi:
<pre><b>restic init --repo swift:123_restic:/backup</b>
enter password for new repository: <b>************</b>
enter password again: <b>************</b>

created restic repository a70df2ced1 at swift:123_restic:/backup

Please note that knowledge of your password is required to access
the repository. Losing your password means that your data is
irrecoverably lost.
</pre>

Alustamisprosessi kysyy salasanointia arkistoon.

Nyt voit varmuuskopioida tiedoston tai hakemiston Restic-arkistoon Allaksessa. Alla olevassa esimerkissä hakemisto _my_data_ on varmuuskopioitu.

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

Muokattuasi yhtä tiedostoa _my_data_ hakemistossa teemme toisen varmuuskopion:
<pre><b>restic backup --repo swift:123_restic:/backup my_data/</b>
enter password for repository: <b>************</b>
repository a70df2ce opened successfully, password is correct

Files:           0 new,     1 changed,   257 unmodified
Dirs:            0 new,     0 changed,     0 unmodified
Added to the repo: 1.154 KiB

processed 258 files, 2.027 MiB in 0:00
snapshot e3b46fe2 saved
</pre>

Komennolla `restic snapshots` voimme nähdä, että meillä on kaksi versiota my_data:sta varmuuskopioarkistossa:

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

Jos haluaisimme palauttaa ensimmäisen version, voisimme ladata sen snapshot-id:llä ja komennolla `restic restore`.

<pre><b>restic restore --repo swift:123_restic:/backup a706c054 --target ./ </b>
enter password for repository: <b>************</b>
repository a70df2ce opened successfully, password is correct
found 3 old cache directories in /users/kkmattil/.cache/restic, run `restic cache --cleanup` to remove them
restoring <Snapshot a706c054 of [/run/nvme/job_4891841/data/my_data] at 2021-02-12 14:43:03.215110283 +0200 EET by kkayttaj@r07c52.bullx> to ./
</pre>

Varsinainen data tallennetaan salattuina hash-objekteina, jotka ovat käytettävissä muille Allas-työkaluille. Esimerkiksi data, joka tallennettiin `restic`:lla säiliöön
_123_restic_ yllä olevassa esimerkissä näyttää tältä, kun se listataan `rclone`:lla:
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

