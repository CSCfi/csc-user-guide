---
tags:
  - Other
catalog:
  name: VASP
  description: Ab initio DFT electronic structures
  description_fi: Ab initio -DFT -pohjaiset elektroniset rakenteet
  license_type: Other
  disciplines:
    - Physics
    - Chemistry
  available_on:
    - Puhti
    - Mahti
---

# VASP { #vasp }

[VASP](https://www.vasp.at/) on ab initio -DFT-ohjelma, jolla voidaan laskea
enintään muutamien satojen atomien elektronisia rakenteita.

Tällä sivulla kuvataan lyhyesti VASP:n käyttö mahti.csc.fi-järjestelmässä. Käyttö
puhti.csc.fi:ssä on hyvin samankaltaista. VASP:n käyttö edellyttää kuitenkin
jonkin verran kokemusta; uusien VASP-käyttäjien suositellaan aloittavan
ohjaajan tai kokeneen kollegan kanssa.

## Saatavilla { #available }

Katso saatavilla olevat VASP-versiot komennolla

```console
module avail vasp
```

## Lisenssi { #license }

VASP:n käyttö edellyttää lisenssiä, joka on hankittava suoraan
ohjelmiston kehittäjiltä.

!!! warning ""
    Lisenssin hankkimisen jälkeen lähetä sähköpostia
    [CSC Service Desk](../support/contact.md) -palveluun ja kerro
    VASP-lisenssiin rekisteröimäsi sähköpostiosoite sekä CSC-käyttäjätunnuksesi.

## Käyttö { #usage }

Esikäännetyt VASP-suoritettavat ja pseudopotentiaalit ovat saatavilla
moduuliympäristön kautta. Käytä komentoa

```console
module show vasp
```

saadaksesi tarkempia tietoja.

### Esimerkkieräajon skripti pientä testiä varten { #an-example-batch-job-script-for-a-small-test }

```bash
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --partition=test
#SBATCH --ntasks=4
#SBATCH --mem-per-cpu=1GB
#SBATCH --account=<project>

module load vasp
srun vasp_std
```

Lisää vaihtoehtoja ja yksityiskohtia: katso ohjeet eräajon skriptien
luomiseen palveluille
[Puhti](../computing/running/creating-job-scripts-puhti.md) ja
[Mahti](../computing/running/creating-job-scripts-mahti.md).

### VASP-oppaat JupyterLabissa { #vasp-tutorials-in-jupyterlab }

[VASP-oppaat](https://www.vasp.at/tutorials/latest/) voidaan myös käydä
läpi JupyterLabissa
[Mahti-verkkokäyttöliittymän](https://www.mahti.csc.fi) kautta. Avaa
sovellus *Jupyter*, ja kohdasta *Settings* -> *Python* valitse
*Custom module* ja kirjoita *py4vasp*. Kun lähetät töitä JupyterLabin
terminaali-ikkunasta laskentanoodeille, lataa ensin moduuli `vasp`,
ja käytä sitten esimerkiksi komentoa

```console
srun -p test -A <project> -t 5 -n 2 vasp_std
```

oppaassa esitetyn `mpirun ...` -komennon sijaan.

### Suorituskyvyn optimointi { #performance-optimization }

Ensinnäkin VASP:n suorituskyky riippuu ratkaisevasti INCAR-tiedoston
parametreista, jotka määräävät, miten k-pisteet, kaistat ja FFT-kertoimet
jaetaan MPI-tehtäville, sekä siitä, että suoritettavan oikea versio
(std/gam/ncl) on käytössä.

Toiseksi tarjolla olevat esikäännetyt suoritettavat on rakennettu
mahdollisimman “vanilla”-muotoon ja tarjoavat kohtuullisen lähtötason.
Suorituskyvyn optimointi suuriin ajoihin kannattaa tehdä tapauskohtaisesti.
Komennot, joilla esikäännetyt suoritettavat on luotu, löytyvät tiedostosta
`$VASPDIR/README.sh`, ja niitä voi käyttää lähtökohtana
optimoidumpien ja/tai muuten muokattujen suoritettavien rakentamiseen.