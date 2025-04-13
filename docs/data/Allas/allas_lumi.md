
# Allaksen ja LUMI-O:n käyttö LUMI-supertietokoneelta

Tässä asiakirjassa kuvaamme, kuinka voit asentaa yleisesti käytettyjä objektitallennuksen asiakasohjelmia LUMI:lle ja kuinka voit määrittää yhteyden Allas-objektitallennuspalveluihin.

## Allaksen käyttö LUMI-supertietokoneelta {#using-allas-from-lumi-supercomputer}

LUMI:ssä voit määrittää yhteyden Allakseen seuraavilla komennoilla:

```text
module use /appl/local/csc/modulefiles
module load allas
allas-conf
```

Sen jälkeen Allas on käytettävissä samalla tavalla kuin Puhtissa ja Mahtissa. Käytettävissä olevia komentorivityökaluja ovat muun muassa:

*   a-komennot
*   allas-backup
*   rclone
*   swift
*   s3cmd
*   restic

## LUMI-O:n käyttö Allas-työkalujen kanssa {#using-lumi-o-with-allas-tools}

Työkaluja, jotka tarjoaa [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils/), voidaan käyttää tiedon lataamiseen ja lataamiseen LUMI-O:sta. Komennon `allas-conf` ajaminen Puhtissa, Mahtissa tai LUMI:ssa alkaa normaali konfigurointiprosessi swift-pohjaiselle yhteydelle Allakseen:

```text
allas-conf
```

Jos haluat määrittää yhteyden LUMI-O:hon sen sijaan, että Allakseen, sinun on lisättävä komentoosi `--lumi`-vaihtoehto:

```text
allas-conf --lumi
```

Jos sinulla on allas-cli-utils asennettuna paikalliseen ympäristöösi, konfiguraatiokomento olisi jotain sellaista kuin:

```text
source allas-cli-utils/allas_conf --lumi
```

Konfigurointiprosessi pyytää sinua yhdistämään selaimellasi LUMI-O-konfigurointipalvelimeen, luomaan tunnisteet siellä ja kopioimaan projektinumeron ja avaimet asennustyökalulle. LUMI-O:n asennusprosessi luo ympäristömuuttujat, joita tarvitaan _S3_-komennolle ja konfigurointitiedostoille `s3cmd` ja `rclone`. Lisäksi voit määritellä, että `a-komennot` käyttävät oletuksena LUMI-O-tallennuspalvelinta Allaksen sijaan. Sen jälkeen sellaiset komennot kuin `a-list`, `a-put` tai `a-get` käyttävät LUMI-O-tallennustasi. Jos et määritä LUMI-O:ta oletustallennuspalveluksi, voit lisätä `--lumi`-vaihtoehdon a-komennoille käyttääksesi LUMI-O:ta Allaksen sijasta.

`rclone` tuo mukanaan kaksi _rclone-etäkohdetta_: _lumi-o:_ ja _lumi-pub:_. Kullakin _lumi-pub_:n käyttämällä kauhalla on julkinen näkyvyys URL:issa: `https://<project-number>.lumidata.eu/<bucket_name>`.

Huomaa, että voit yhtä aikaa olla yhdistettynä sekä LUMI-O:hon että Allakseen.

Esimerkiksi, jos avaat ensin Allas-yhteyden käskyllä:

```text
allas-conf
```

Ja sitten avaat LUMI-O-yhteyden seuraavasti:

```text
allas-conf --lumi
```

(Tällä kertaa sallimme, että LUMI-O on oletuspalvelin a-komennoille.)

Nyt voit listata LUMI-O:ssa olevat saatavilla olevat kauhat käskyillä:

```text
a-list
```

tai 

```text
rclone lsd lumi-o:
```

Ja samaan aikaan voit listata kauhat Allaksessa seuraavilla komennoilla:

```text
a-list --allas
```

tai 

```text
rclone lsd allas:
```

Tiedon kopioiminen Allaksesta LUMI-O:hon voitaisiin nyt tehdä komennolla:

```text
rclone copyto -P allas:bucket-in-allas/object lumi-o:bucket-in-lumi-o/object
```

Ylläoleva komento toimii vain tiedostoille, jotka ovat pienempiä kuin 5 GB.
