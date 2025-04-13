
# Tarin käyttö SSH:n kautta monien tiedostojen siirtämiseen {#using-tar-over-ssh-to-move-many-files}

Linux-työkaluja, kuten `scp` ja `rsync`, käytetään yleisesti tiedostojen siirtämiseen etäpalvelimen ja paikallisen koneen välillä. Kuitenkaan nämä työkalut eivät ole kovin käytännöllisiä, kun siirrettävänä on paljon pieniä tiedostoja.

Yksinkertainen, paljon nopeampi ratkaisu on kirjoittaa (pakattu) tar-paketti, joka sisältää datasi suoraan kohdejärjestelmälle. Tämä saavutetaan ohjaamalla `tar`-komennon lähtö `ssh`-yhteyden yli. Arkiston kirjoittaminen suoraan kohteeseen auttaa myös säästämään levytilaa lähtöjärjestelmässä.

Yleistä tietoa tarista löytyy kohdasta
[Pakkaus- ja pakkaustyökalut](../../support/tutorials/env-guide/packing-and-compression-tools.md).

## Esimerkit {#examples}

Kaikki seuraavat komennot suoritetaan paikalliselta työasemalta, jolle oletetaan olevan tarvittavat työkalut (`tar`, `ssh` ja mahdollisesti `gzip`/`bzip2`) asennettuna. Puhti on käytössä esimerkkinä etäpalvelimesta.

Yleinen syntaksi on:

```bash
tar c <directory_to_transfer> | ssh <username>@puhti.csc.fi 'cat > <target_path_on_puhti>'
```

Esimerkiksi komento kopioida hakemisto `myfiles` paikalliselta koneelta hakemistoon `/scratch/project_2001234` Puhtissa olisi:

```bash
tar c myfiles | ssh <username>@puhti.csc.fi 'cat > /scratch/project_2001234/myfiles.tar'
```

Purkaaksesi tar-arkiston samanaikaisesti, korvaa `cat`-komento seuraavasti:

```bash
tar c myfiles | ssh <username>@puhti.csc.fi 'tar x -C /scratch/project_2001234'
```

Vastaavasti voit kopioida tiedot etäpalvelimelta paikalliselle koneellesi komennolla kuten:

```bash
ssh <username>@puhti.csc.fi 'tar c -C <parent_directory_on_puhti> <directory_to_transfer>' > <archive_on_local_machine>
```

Esimerkiksi komento kopioida kansio `myfiles`, joka sijaitsee
`/scratch/project_2001234` hakemistoon paikalliselle koneellesi:

```bash
ssh <username>@puhti.csc.fi 'tar c -C /scratch/project_2001234 myfiles' > myfiles.tar
```

Purkaaksesi arkiston samanaikaisesti:

```bash
ssh <username>@puhti.csc.fi 'tar c -C /scratch/project_2001234 myfiles' | tar x
```

!!! info "Ota käyttöön pakkaus"
    Yllä olevat komennot eivät käytä pakkausta. Korvaa `tar c` (`tar x`) `tar cz` tai `tar cj` (`tar xz` tai `tar xj`) mahdollistamaan gzip- tai bzip2-pakkaus (purku). Huomaa, että jotkin tiedostot eivät hyödy pakkauksesta (esim. binääritiedostot tai tiedostot, jotka ovat jo pakattuja), jolloin on nopeampaa siirtää ilman pakkausta.

!!! info "Vältä yksityiskohtaista tulostusta"
    `v`-vaihtoehdon lisääminen (esim. `tar czv`) tuottaa yksityiskohtaista tulostusta eli listaa käsitellyt tiedostot konsolissa. Tämä hidastaa siirtoprosessia, kun siirretään monia pieniä tiedostoja, joten on suositeltavaa välttää sen käyttöä.

## Suorituskyvyn vertailu {#performance-comparison}

Alla on karkea vertailu siitä, kuinka kauan kestää siirtää hakemisto, jossa on paljon pieniä tiedostoja Puhdille. Jokainen tiedosto on kooltaan 100 KiB ja pakkausta ei ole käytetty.

| Tiedostojen määrä      | `tar` + `ssh` | `scp`    |
|-----------------------:|--------------:|---------:|
| 100                    | 0.5 s         | 2.4 s    |
| 1000                   | 1.3 s         | 20.5 s   |
| 10000                  | 9.4 s         | 201.2 s  |

## Lisätietoa {#more-information}

- [Pakkaus- ja pakkaustyökalut](../../support/tutorials/env-guide/packing-and-compression-tools.md)
