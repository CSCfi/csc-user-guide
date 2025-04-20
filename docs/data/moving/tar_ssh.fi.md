# Tarin käyttäminen SSH:n yli useiden tiedostojen siirtoon {#using-tar-over-ssh-to-move-many-files}

Linux-työkalut kuten `scp` ja `rsync` ovat yleisesti käytettyjä tiedostojen siirtämiseen etäpalvelimen ja paikallisen koneen välillä. Nämä työkalut eivät kuitenkaan ole kovin käytännöllisiä pienien tiedostojen suuren määrän siirrossa.

Yksinkertainen ja huomattavasti nopeampi ratkaisu on kirjoittaa (pakattu) tar-paketti, joka sisältää tiedot, suoraan kohdejärjestelmään. Tämä saavutetaan ohjaamalla `tar`-komennon ulostulo `ssh`-yhteyden kautta. Arkiston kirjoittaminen suoraan kohteeseen auttaa myös säästämään levytilaa lähdejärjestelmässä.

Yleistä tietoa tarista löytyy kohdasta
[Pakkaus- ja pakkaustyökalut](../../support/tutorials/env-guide/packing-and-compression-tools.md).

## Esimerkkejä {#examples}

Kaikki seuraavat komennot suoritetaan paikallisella työasemalla, jonka oletetaan sisältävän tarvittavat työkalut (`tar`, `ssh` ja tarvittaessa `gzip`/`bzip2`). Puhti toimii esimerkkinä etäpalvelimesta.

Yleinen syntaksi on:

```bash
tar c <directory_to_transfer> | ssh <username>@puhti.csc.fi 'cat > <target_path_on_puhti>'
```

Esimerkiksi, komento jolla kansio `myfiles` kopioidaan paikalliselta koneeltasi hakemistoon `/scratch/project_2001234` Puhtissa, olisi:

```bash
tar c myfiles | ssh <username>@puhti.csc.fi 'cat > /scratch/project_2001234/myfiles.tar'
```

Jos haluat purkaa tar-arkiston samanaikaisesti, vaihda `cat`-komento seuraavasti:

```bash
tar c myfiles | ssh <username>@puhti.csc.fi 'tar x -C /scratch/project_2001234'
```

Vastaavasti, voit myös kopioida etäpalvelimella sijaitsevaa dataa paikalliselle koneellesi komennolla:

```bash
ssh <username>@puhti.csc.fi 'tar c -C <parent_directory_on_puhti> <directory_to_transfer>' > <archive_on_local_machine>
```

Esimerkiksi, komento jolla kansio `myfiles`, joka sijaitsee hakemistossa `/scratch/project_2001234`, kopioidaan omalle koneellesi, olisi:

```bash
ssh <username>@puhti.csc.fi 'tar c -C /scratch/project_2001234 myfiles' > myfiles.tar
```

Arkiston purkaminen samanaikaisesti onnistuu näin:

```bash
ssh <username>@puhti.csc.fi 'tar c -C /scratch/project_2001234 myfiles' | tar x
```

!!! info "Ota pakkaus käyttöön"
    Yllä olevissa komennoissa ei käytetty pakkausta. Vaihda `tar c` (`tar x`) muotoon
    `tar cz` tai `tar cj` (`tar xz` tai `tar xj`), jos haluat käyttää gzip- tai bzip2-
    pakkausta (purkamista). Huomioi, että jotkut tiedostot eivät hyödy
    pakkauksesta (esimerkiksi binääritiedostot tai jo valmiiksi pakatut tiedostot), jolloin tiedostojen siirtäminen ilman pakkausta on nopeampaa.

!!! info "Vältä yksityiskohtaista tulostetta"
    `v`-valitsimen lisääminen (esim. `tar czv`) tuottaa yksityiskohtaisen tulosteen, eli listaa käsiteltävät tiedostot konsolissa. Tämä hidastaa siirtoa, kun siirretään paljon pieniä tiedostoja, joten sen käyttöä kannattaa välttää.

## Suorituskykyvertailu {#performance-comparison}

Alla on karkea vertailu siirtoajoista, kun hakemisto sisältää paljon pieniä tiedostoja ja siirretään Puhtiin. Jokaisen tiedoston koko on 100 KiB, eikä pakkausta käytetä.

| Tiedostojen määrä      | `tar` + `ssh` | `scp`    |
|-----------------------:|--------------:|---------:|
| 100                    | 0,5 s         | 2,4 s    |
| 1000                   | 1,3 s         | 20,5 s   |
| 10000                  | 9,4 s         | 201,2 s  |

## Lisätietoa {#more-information}

- [Pakkaus- ja pakkaustyökalut](../../support/tutorials/env-guide/packing-and-compression-tools.md)