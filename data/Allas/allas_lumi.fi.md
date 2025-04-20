# Allas- ja LUMI-O-palvelujen käyttäminen LUMI-supertietokoneella {#using-allas-and-lumi-o-from-lumi-supercomputer}

Tässä dokumentissa kuvaamme, kuinka voit asentaa yleisesti käytettyjä objektitallennusohjelmia LUMI-järjestelmään ja kuinka konfiguroida yhteys Allas-objektitallennuspalveluun.

## Allaksen käyttäminen LUMI-supertietokoneella {#using-allas-from-lumi-supercomputer}

LUMI-järjestelmässä voit muodostaa yhteyden Allakseen seuraavilla komennoilla:

```text
module use /appl/local/csc/modulefiles
module load allas
allas-conf
```

Tämän jälkeen Allasta voi käyttää samalla tavoin kuin Puhdilta ja Mahtilta. Käytettävissä olevia komentorivityökaluja ovat mm.:

*   a-commands
*   allas-backup
*   rclone
*   swift
*   s3cmd
*   restic

## LUMI-O:n käyttäminen Allas-työkaluilla {#using-lumi-o-with-allas-tools}

[allas-cli-utils](https://github.com/CSCfi/allas-cli-utils/):n tarjoamia työkaluja voidaan käyttää datan siirtämiseen LUMI-O-palveluun ja sieltä pois. Komennon `allas-conf` suorittaminen Puhtilla, Mahtilla tai LUMIlla käynnistää normaalin konfiguraatioprosessin, jolla muodostetaan swift-pohjainen yhteys Allakseen:

```text
allas-conf
```

Jos haluat konfiguroida yhteyden LUMI-O:hon Allaksen sijaan, lisää komennolle optio `--lumi`:

```text
allas-conf --lumi
```

Jos sinulla on allas-cli-utils asennettuna omaan ympäristöösi, konfigurointikomento olisi esimerkiksi:

```text
source allas-cli-utils/allas_conf --lumi
```

Konfigurointiprosessi pyytää sinua yhdistämään selaimella LUMI-O-konfigurointipalvelimeen, luomaan käyttöoikeustiedot siellä ja kopioimaan projekinumeron sekä avaimet asennustyökalua varten. LUMI-O:n asennus luo tarvittavat ympäristömuuttujat _S3_-komentoa sekä konfiguraatiotiedostot `s3cmd`- ja `rclone`-työkaluille. Lisäksi voit määritellä, että `a-commands` käyttää oletuksena LUMI-O-tallennuspalvelinta Allaksen sijaan. Tämän jälkeen komennot kuten `a-list`, `a-put` tai `a-get` käyttävät LUMI-O-tallennustilaasi. Jos et aseta LUMI-O:ta oletustallennuspalveluksi, voit lisätä komennoille `a-commands` option `--lumi`, jolloin käytetään LUMI-O:ta Allaksen sijaan.

`rclone`-työkalulle LUMI-O-konfiguraatio luo kaksi _rclone remotea_: _lumi-o:_ ja _lumi-pub:_. _lumi-pub_:n kautta käytetyt bucketit ovat julkisesti nähtävillä osoitteessa: `https://<project-number>.lumidata.eu/<bucket_name>`.

Huomaa, että voit olla samanaikaisesti yhteydessä sekä LUMI-O:hon että Allakseen.

Esimerkiksi, jos avaat ensin Allas-yhteyden komennolla:

```text
allas-conf
```

Ja avaat sitten LUMI-O-yhteyden komennolla:

```text
allas-conf --lumi
```

(Suorittaessasi jälkimmäisen komennon hyväksyt, että LUMI-O on oletuspalvelin a-commands-komennoille.)

Nyt voit listata LUMI-O:ssa olevat bucketit komennoilla:

```text
a-list
```

tai

```text
rclone lsd lumi-o:
```

Ja samanaikaisesti voit listata Allaksessa olevat bucketit komennoilla:

```text
a-list --allas
```

tai

```text
rclone lsd allas:
```

Datan kopiointi Allaksesta LUMI-O:hon onnistuu nyt komennolla:

```text
rclone copyto -P allas:bucket-in-allas/object lumi-o:bucket-in-lumi-o/object
```

Yllä oleva komento toimii vain tiedostoille, jotka ovat alle 5 GB kokoisia.