
---
tags:
  - Academic
---

# GOLD

GOLD on telakointiohjelma, joka ennustaa, miten joustavat molekyylit sitoutuvat proteiineihin. GOLD käyttää geneettistä algoritmimenetelmää proteiini-ligandi-telakointiin ja mahdollistaa sekä ligandien että proteiinien osittaisen joustavuuden.

## Available {#available}

- Puhti: 2022.2, 2023.2
- Lataa ja asenna paikallisesti

Suorita `module spider ccdc` nähdäksesi moduuliversiot ja kuinka ne ladataan.

## License {#license}

Lisenssi kattaa **akateemisen käytön** yliopistoissa ja voittoa tavoittelemattomissa tutkimuslaitoksissa. Katso lisätietoja [CSD-sivultamme](csd.md).

## Usage {#usage}

GOLD on osa Cambridgen kiteytystietokantajärjestelmää. Katso [CSD-sivultamme](csd.md) asennus- ja aktivointiohjeet.

GOLDia voidaan käyttää joko komentoriviltä tai graafisen käyttöliittymän (GUI) kautta, jota kutsutaan nimellä Hermes. Paras tapa suorittaa GUI etänä Puhti-järjestelmässä on käyttää [Puhti web-käyttöliittymää työpöydällä](../computing/webinterface/desktop.md). GOLD-interaktiivisen ympäristön asettamiseksi avaa terminaali ja suorita:

```bash
module load ccdc
```

Tämä lataa uusimman version CSD:stä ja GOLDista. Voit suorittaa GOLDin kirjoittamalla joko `hermes` ja siirtymällä GOLD-välilehteen tai vaihtoehtoisesti suorittamalla `gold`, joka avaa suoraan Hermeksen GOLD-opastajan. Huomaa, että GUI:n suorituskyky voi olla hieman hitaampi verrattuna paikalliseen asennukseen.

Pidemmät (ei-interaktiiviset) työt on parasta suorittaa eräajoina:

```bash
#!/bin/bash -l
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --account=<project>
#SBATCH --time=0:30:00    # time as `hh:mm:ss`

module load ccdc

gold_auto gold.conf
```

!!! Huom
    Useiden ligandien telakointiin rinnakkain, tutustu Python-skriptiin `gold_multi` [CSD Python API skriptivarastossa](https://github.com/ccdc-opensource/csd-python-api-scripts).

## More information {#more-information}

- [CSC CSD -Sivu](csd.md)
- [GOLD kotisivu](https://www.ccdc.cam.ac.uk/solutions/software/gold/)
- [GOLD verkko-dokumentaatio](https://www.ccdc.cam.ac.uk/support-and-resources/documentation-and-resources/?category=All%20Categories&product=GOLD&type=All%20Types)
