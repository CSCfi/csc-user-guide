
# Levykiintiö ylitetty {#disk-quota-exceeded}

Tämä varoitus tarkoittaa, että olet ylittänyt levytilakiintiösi tai sinulla on
liian monta tiedostoa levyalalla. Nähdäksesi mikä kiintiö on käytössä, kirjoita:

```bash
csc-workspaces
```

Esimerkki tulosteesta on alla:

```text
Henkilökohtainen kotikansio  Kiintiö
--------------------------------------------------------------------------
/users/jdoe                 Kapasiteetti:     653M/10G   Tiedostot:    .68k/100k

Projektisovellukset         Kiintiö
--------------------------------------------------------------------------
/projappl/project_2000040   Kapasiteetti:   283.5M/50G   Tiedostot:    .37k/100k

Projektin raakatila         Kiintiö
--------------------------------------------------------------------------
/scratch/project_2000040    Kapasiteetti:   1.098T*/1T   Tiedostot:   .02k/1000k
```

Tähti (`*`) osoittaa, mikä kiintiö on ylitetty. Jotta voisit luoda uusia
tiedostoja tälle levylle, sinun täytyy poistaa tai siirtää tiedostoja muualle,
esimerkiksi [Allas](../../data/Allas/index.md). Jos tietojen siirtäminen/poistaminen
ei ole mahdollista, voit [hakea lisää kiintiötä](../../accounts/how-to-increase-disk-quotas.md).

!!! warning "Conda"
    Yleinen syy `$HOME` tai `/projappl` levykiintiön ylitykseen on Conda-pohjaisten
    asennusten käyttö. Conda-ympäristöt luovat suuren määrän tiedostoja, mikä aiheuttaa
    ylimääräistä kuormitusta HPC-ympäristössä käytetyllä Lustre-rinnakkaistiedostojärjestelmällä.
    Tämä ilmenee pidentyneinä käynnistysaikoina ja levyn hitaudena, mikä vaikuttaa
    kaikkiin käyttäjiin.

    Jos sinun täytyy käyttää Condaa CSC:n superkoneilla, vaadimme, että
    [konttikerroit](../../computing/containers/overview.md) ympäristösi, katso
    [käyttöpolitiikka](../../computing/usage-policy.md#conda-installations).
    Helposti Conda-ympäristöiesi konttikerroittamiseen ole hyvä ja tutustu
    [Tykky konttiympäristötyökaluun](../../computing/containers/tykky.md).

Jos olet uusi konttien käytössä, voit tutustua seuraaviin tärkeisiin osioihin,
jotka on kerätty osina aikaisempia CSC-kursseja:

- [Using CSC HPC Environment Efficiently kurssi](https://csc-training.github.io/csc-env-eff/)
- [Containers and Workflows in Bioinformatics kurssi](https://yetulaxman.github.io/containers-workflows/)

## Olen poistanut monia tiedostoja, mutta saan silti levykiintiön ylitysvaroituksen? {#i-have-deleted-many-files-but-still-get-disk-quota-exceeded-warning}

On yleistä, että jotkin ohjelmistot luovat piilotettuja hakemistoja, jotka alkavat \\
pisteellä (`.`), kuten `.cache`, `.cargo` tai `.local`. Näitä luodaan usein
auto- maattisesti henkilökohtaiseen kotikansioosi ja ne voivat aiheuttaa hämmennystä,
jos ne saavat sinut ylittämään levykiintiösi. Koska piilotettuja tiedostoja ei näytetä
tavallisella `ls` komennolla, saattaa näyttää siltä, että suurimman osan kansioista/tiedostoista
siirtäminen/poistaminen ei vaikuta.

Nähdäksesi myös kaikki piilotetut tiedostot/hakemistot tietyssä kansiossa, sinun
täytyy käyttää `ls -a` vaihtoehtoa. [LUE (Lustre Usage Explorer)](../tutorials/lue.md)
on toinen suositeltu työkalu löytääksesi, missä sinulla on paljon tietoa; se
tarkistaa oletuksena myös piilotetut tiedostot ja hakemistot. Ole hyvä ja käytä sitä,
jos ylität levykiintiösi ja sinulla on vaikeuksia selvittää, missä tiedostot saattavat
olla. Esimerkiksi:

```bash
module load lue
lue $HOME
```

[Katso myös tämä LUE-opas](https://csc-training.github.io/csc-env-eff/hands-on/disk-areas/disk-areas-tutorial-lue.html).
