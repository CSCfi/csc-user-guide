---
tags:
  - Academic
catalog:
  name: GOLD
  description: Protein Ligand Docking Software
  description_fi: Proteiini-ligandi-telakointiohjelmisto
  license_type: Academic
  disciplines:
    - Chemistry
    - Biosciences
  available_on:
    - Puhti
---

# GOLD { #gold }

GOLD on telakointiohjelma, jolla ennustetaan, miten joustavat molekyylit sitoutuvat proteiineihin. GOLD käyttää geneettiseen algoritmiin perustuvaa menetelmää proteiini-ligandi-telakoinnissa ja sallii ligandin täydellisen ja proteiinin osittaisen joustavuuden.

## Saatavilla { #available }

- Puhti: 2022.2, 2023.2
- Lataa ja asenna paikallisesti

Suorita `module spider ccdc` nähdäksesi moduuliversiot ja ohjeet niiden lataamiseen.

## Lisenssi { #license }

Lisenssi kattaa akateemisen käytön yliopistoissa ja voittoa tavoittelemattomissa tutkimuslaitoksissa. Katso lisätiedot [CSD-sivultamme](csd.md).

## Käyttö { #usage }

GOLD on osa Cambridge Crystallographic Database System -kokonaisuutta.
Katso asennus- ja aktivointiohjeet [CSD-sivultamme](csd.md).

GOLDia voi käyttää joko komentoriviltä tai Hermes-nimisellä graafisella käyttöliittymällä (GUI). Paras tapa ajaa GUI-etäistuntoa Puhtilla on käyttää [Puhtin selainpohjaista työpöytää](../computing/webinterface/desktop.md). GOLDin interaktiivisen ympäristön käynnistämiseksi avaa pääte ja suorita:

```bash
module load ccdc
```

Tämä lataa uusimman CSD- ja GOLD-version. Voit ajaa GOLDin kirjoittamalla `hermes` ja siirtymällä GOLD-välilehdelle, tai vaihtoehtoisesti suorittamalla `gold`, joka avaa suoraan Hermeksen GOLD-ohjatun toiminnon. Huomaa, että GUI:n suorituskyky voi olla jonkin verran hitaampi kuin paikallisessa asennuksessa.

Pidemmät (ei-interaktiiviset) ajot kannattaa ajaa eräajoina:

```bash
#!/bin/bash -l
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --account=<project>
#SBATCH --time=0:30:00    # time as `hh:mm:ss`

module load ccdc

gold_auto gold.conf
```

!!! Note
    Useiden ligandien rinnakkaista telakointia varten katso Python-skriptiä `gold_multi` [CSD Python API -skriptien repositoriossa](https://github.com/ccdc-opensource/csd-python-api-scripts).

## Lisätietoja { #more-information }

- [CSC:n CSD-sivu](csd.md)
- [GOLDin kotisivu](https://www.ccdc.cam.ac.uk/solutions/software/gold/)
- [GOLDin verkkodokumentaatio](https://www.ccdc.cam.ac.uk/support-and-resources/documentation-and-resources/?category=All%20Categories&product=GOLD&type=All%20Types)