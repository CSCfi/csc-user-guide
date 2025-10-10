# Levykiintiö ylitetty { #disk-quota-exceeded }

Tämä varoitus tarkoittaa, että olet ylittänyt levytilakiintiösi tai että levyalueella on liikaa tiedostoja. Nähdäksesi, mikä kiintiö on täynnä, kirjoita:

```bash
csc-workspaces
```

Esimerkkituloste on alla:

```text
[kkayttaj@puhti-login11 ~]$ csc-workspaces 

Disk area               Capacity(used/max)  Files(used/max)  Cleanup
----------------------------------------------------------------------
Personal home folder

/users/kkayttaj                 4.4G/10G         24K/100K        n/a
----------------------------------------------------------------------
Project: project_2000123 "Project X"

/projappl/project_2000123        24G/50G         36K/100K        n/a
/scratch/project_2000123        103G/1.0T       389K/1.0M       180d
----------------------------------------------------------------------
Project: project_2001234 "Project Y"

/projappl/project_2001234        85G/100G       282K/600K        n/a
/scratch/project_2001234       7.2T*/7.0T       2.7M/5.0M        90d
----------------------------------------------------------------------
```

Tähti (`*`) osoittaa, mikä kiintiö on ylitetty. Jotta voit luoda uusia tiedostoja tälle levyalueelle, sinun on poistettava tai siirrettävä tiedostoja muualle, esim. [Allakseen](../../data/Allas/index.md). Jos datan siirtäminen/poistaminen ei ole mahdollista, voit [hakea lisää kiintiötä](../../accounts/how-to-increase-disk-quotas.md).

!!! warning "Conda"
    Yleinen syy `$HOME`- tai `/projappl`-levykiintiön ylittymiseen on Condaan perustuvien asennusten käyttö. Conda-ympäristöt synnyttävät erittäin suuren määrän tiedostoja, mikä kuormittaa HPC-ympäristössä käytettävää Lustre-rinnakkaistiedostojärjestelmää. Tämä näkyy pidentyneinä käynnistysaikoina ja levyhitautena, mikä vaikuttaa kaikkiin käyttäjiin.

    Jos sinun täytyy käyttää Condaa CSC:n supertietokoneilla, edellytämme, että [kontitat](../../computing/containers/overview.md) ympäristösi; katso [käyttöpolitiikka](../../computing/usage-policy.md#conda-installations). Conda-ympäristöjen helppoon kontittamiseen tutustu [Tykky-konttikääretyökaluun](../../computing/containers/tykky.md).

Jos kontit ovat sinulle uusia, voit tutustua seuraaviin aiheeseen liittyviin ohjeosion kohtiin, jotka on koottu aiempien CSC-kurssien materiaaleista:

* [CSC HPC -ympäristön tehokas käyttö -kurssi](https://csc-training.github.io/csc-env-eff/)
* [Kontit ja työnkulut bioinformatiikassa -kurssi](https://yetulaxman.github.io/containers-workflows/)

## Olen poistanut paljon tiedostoja, mutta saan silti levykiintiö ylitetty -varoituksen? { #i-have-deleted-many-files-but-still-get-disk-quota-exceeded-warning }

On tavallista, että jotkin ohjelmistot luovat pisteellä (`.`) alkavia piilohakemistoja, kuten `.cache`, `.cargo` tai `.local`. Nämä syntyvät usein oletuksena omaan kotihakemistoosi ja voivat aiheuttaa hämmennystä, jos ne saavat levykiintiösi ylittymään. Koska piilotiedostoja ei näytetä tavallisella `ls`-komennolla, voi näyttää siltä, ettei kansioiden/tiedostojen siirtäminen tai poistaminen vaikuta mitään.

Nähdäksesi myös kaikki piilotiedostot ja -hakemistot tietyssä kansiossa, käytä `ls -a` -valintaa. [LUE (Lustre Usage Explorer)](../tutorials/lue.md) on toinen suositeltava työkalu sen selvittämiseen, missä sinulla on paljon dataa; se tarkistaa oletuksena myös piilotiedostot ja -hakemistot. Käytä sitä, jos levykiintiösi ylittyy etkä löydä helposti, mihin tiedostot ovat kertyneet. Esimerkiksi:

```bash
module load lue
lue $HOME
```

[Katso myös tämä LUE-ohje](https://csc-training.github.io/csc-env-eff/hands-on/disk-areas/disk-areas-tutorial-lue.html).

Jos käytät Pythonia ja huomaat, että `.cache/pip` vaikuttaa syylliseltä, katso UKK-artikkelimme siitä, [miten pip-välimuisti konfiguroidaan](../faq/python-pip-cache.md).