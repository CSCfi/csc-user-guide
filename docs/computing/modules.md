# Modulijärjestelmä {#the-module-system}

Modulijärjestelmä mahdollistaa useiden keskenään yhteensopimattomien ohjelmistoympäristöjen hallinnan yhdellä tietokoneella. Käytä `module`-komentoa saatavilla olevien sovellusten, kirjastojen tai kääntäjäkokonaisuuksien kyselyyn ja niiden dynaamiseen alustamiseen.
Modulijärjestelmää kannattaa käyttää sekä interaktiivisissa että eräkäsittelytöissä.

**Ympäristömoduulit** tarjoavat kätevän tavan asentaa kaikki tarvittava tietyn sovelluksen käyttöön. Modulijärjestelmä muokkaa käyttäjän shellin ympäristömuuttujia niin, että oikeat suoritettavat tiedostot löytyvät polusta ja linkittäjä löytää oikean version vaadituista kirjastoista. Esimerkiksi komento `mpicc` viittaa eri kääntäjiin ladatusta modulista riippuen.

CSC käyttää **Lmod**-ympäristömoduuleita. Ne on kehitetty Texas Advanced Computing Centerissä (TACC) ja toteutettu _Lua_-ohjelmointikielellä. Lisätekniset tiedot löytyvät [Lmodin kotisivulta].

[TOC]

## Peruskäyttö {#basic-usage}

Moduulikomennon syntaksi:

```text
module command modulename
```

Ladattujen moduulien (myös nykyisen ympäristösi) listaaminen:

```text
module list
```

Komento `module help` antaa yleistä tietoa moduulista. Esimerkiksi saadaksesi lisätietoa moduulista `intel-oneapi-compilers`, käytä komentoa:

```text
module help intel-oneapi-compilers
```

Lataa uusia moduuleja ympäristöösi komennolla `load`. Esimerkiksi ladataksesi `intel-oneapi-mpi`-moduulin, käytä komentoa:

```text
module load intel-oneapi-mpi
```

Huomaa, että voit ladata vain moduuleja, jotka ovat yhteensopivia muiden ladattujen moduulien kanssa. Eli et voi ladata moduuleja, jotka ovat ristiriidassa aiemmin ladattujen moduulien kanssa tai moduuleja, jotka riippuvat moduuleista, jotka eivät ole ladattuja.

Moduulit, joita ei tarvita tai jotka ovat ristiriidassa muiden moduulien kanssa, voidaan purkaa `unload`-komennolla:

```text
module unload intel-oneapi-mkl
```

### Yleisimmin käytetyt moduulikomennot {#module-commands-table}

| Moduulikomento                        | Kuvaus                                                                                            |
|-----------------------------------|--------------------------------------------------------------------------------------------------|
| module help *modulename*          | Tietoa moduulista.                                                                                |
| module load *modulename*          | Lataa ympäristömoduulin oletusversion.                                                            |
| module load *modulename/version*  | Lataa tietyn version moduulista.                                                                  |
| module unload *modulename*        | Purkaa annetun ympäristömoduulin.                                                                 |
| module list                       | Listaa ladatut moduulit.                                                                          |
| module avail                      | Listaa kaikki moduulit, jotka voivat olla ladattavissa (eli yhteensopivat nykyisen ympäristösi kanssa). |
| module spider                     | Listaa kaikki olemassa olevat moduulit.                                                           |
| module spider *modulename*        | Etsi kaikki olemassa olevat moduulit tietyn nimen perusteella.                                    |
| module spider *modulename/version*| Antaa tietoa moduulin lataamiseen liittyvistä asioista (esim. esivaatimukset).                    |
| module swap *modulename1 modulename2* | Korvaa moduulin toisella (ja yrittää ladata uudelleen yhteensopivat versiot muista ladatuista moduuleista). |
| module show *modulename*          | Näytä komennot moduulitiedostossa.                                                                |
| module purge                      | Purkaa kaikki moduulit.                                                                           |

### Moduulien löytäminen {#finding-modules}

Voit listata moduulit, jotka ovat yhteensopivia nykyisen modulijoukkosi kanssa käyttämällä:

```text
module avail
```

_Lmod_-järjestelmän hierarkkisen rakenteen vuoksi ei ole mahdollista ladata kaikkia asennettuja moduuleja yksinkertaisesti käyttämällä yksittäistä `module load`-komentoa. `avail`-komento ei näytä moduuleja, joita ei voida ladata yhteensopimattomuuksien tai täyttämättömien riippuvuuksien vuoksi. Nämä suojarajoitukset estävät yhteensopimattomien moduliyhdistelmien lataamisen.

Listaa kaikki asennetut ohjelmistopaketit:

```text
module spider
```

Listaa moduulit nimen perusteella:

```text
module spider int
```

Yllä oleva komento listaa kaikki moduulit, joiden nimessä on merkkijono _int_. Yksityiskohtaisempi kuvaus moduulista voidaan tulostaa käyttämällä koko modulien nimeä ja versionumeroa:

```text
module spider intel-oneapi-mkl/2022.1.0
```

### Moduuliriippuvuuksien ratkaiseminen {#solving-module-dependencies}

Jotkut moduulit riippuvat muista moduuleista. Jos vaadittua moduulia ei ole, modulijärjestelmä tulostaa virheilmoituksen:

```text
$ module load parallel-netcdf

Lmod has detected the following error:  These module(s) exist but
cannot be loaded as requested: "parallel-netcdf"
Try: "module spider parallel-netcdf" to see how to load the module(s).

$ module spider parallel-netcdf

----------------------------------------------------------------------------
  parallel-netcdf:
----------------------------------------------------------------------------
     Versions:
        parallel-netcdf/1.12.2

----------------------------------------------------------------------------
  For detailed information about a specific "parallel-netcdf" module
  (including how to load the modules) use the module's full name.
  For example:

$ module spider parallel-netcdf/1.12.2
----------------------------------------------------------------------------
```

Tällaisissa tapauksissa `module avail`-komento jättää moduulin pois listalta, eikä `module load`-komento löydä sitä. Helpoin tapa löytää vaadittu ympäristö on käyttää `module spider`-komentoa version tiedoilla. Esimerkiksi:

```text
$ module spider parallel-netcdf/1.12.2
------------------------------------------------------------------
 parallel-netcdf: parallel-netcdf/1.12.2
------------------------------------------------------------------
 You will need to load all module(s) on any one of the lines below before
 the "parallel-netcdf/1.12.2" module is available to load.

  gcc/11.3.0  openmpi/4.1.4
  gcc/9.4.0  openmpi/4.1.4
  intel-oneapi-compilers-classic/2021.6.0  intel-oneapi-mpi/2021.6.0
...
```

Tässä tapauksessa sinun on ladattava yksi listatuista ympäristöistä ennen `module load`-komennon käyttämistä.

## Kehittyneet aiheet {#advanced-topics}

Yleisesti ottaen sovellukset ja niiden riippuvuudet tulisi kääntää ja linkittää samoilla kääntäjillä. Joissakin tapauksissa tämä on pakollinen vaatimus. Esimerkiksi et voi käyttää _MPI Fortran90_-moduulia, joka on käännetty Intel-kääntäjillä, _gfortran_:n kanssa. Ympäristömoduuleilla on useita mekanismeja, jotka estävät käyttäjää asettamasta yhteensopimatonta ympäristöä.

Modulihierarkia auttaa pitämään kääntäjän ja MPI-kirjaston asetukset keskenään yhteensopivina. Käytännössä jokaiselle tuetulle kääntäjälle on moduuli tuetulle MPI-kirjastolle. Kun käyttäjä vaihtaa kääntäjämoduulia, modulijärjestelmä yrittää löytää oikeat versiot ladatuista moduuleista:

```text
$ module list
Currently Loaded Modules:
 1) gcc/11.3.0   2) openmpi/4.1.4   3) parallel-netcdf/1.12.2

$ module swap gcc intel-oneapi-compilers-classic

Inactive Modules:
 1) parallel-netcdf/1.12.2

Due to MODULEPATH changes the following modules have been reloaded:
 1) openmpi/4.1.4

$ module list
Currently Loaded Modules:
 1) intel-oneapi-compilers-classic/2021.6.0   2) openmpi/4.1.4

Inactive Modules:
 1) parallel-netcdf/1.12.2
```

Jos oikeaa versiota ei löydy, modulijärjestelmä _deaktivoi_ nämä moduulit (katso yllä). Käytännössä moduuli puretaan, mutta se merkitään niin, että kun kääntäjä/MPI-kokoonpanoa muutetaan, järjestelmä yrittää löytää oikean version automaattisesti.

Tämä hierarkia toteutetaan muuttamalla `$MODULEPATH`-muuttujaa. Jokainen kääntäjämoduuli lisää oman polkunsa modulipolkuun niin, että tietyn kääntäjän kanssa yhteensopivat ohjelmistomoduulit voidaan listata. Kun kääntäjämoduuli puretaan, tämä polku poistetaan modulipolulta. Sama pätee myös MPI-moduuleihin.

### Omien moduulitiedostojen käyttäminen {#using-your-own-module-files}

Jos haluat hallita moduuleilla itse asentamiasi ohjelmistopaketteja, voit sijoittaa omat moduulitiedostosi kotihakemistoosi. Esimerkiksi, jos sisällytät moduulitiedostoja hakemistoon `$HOME/modulefiles`, voit käyttää niitä lisäämällä polun modulihakupolkuun komennolla:

```text
module use $HOME/modulefiles
```

Jos haluat tutkia olemassa olevia moduulitiedostoja, `module show <modulename>` näyttää myös moduulitiedoston nimen.

[Lmodin kotisivulta]: https://lmod.readthedocs.io/en/latest/