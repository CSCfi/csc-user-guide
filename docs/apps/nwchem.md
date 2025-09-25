---
tags:
  - Free
catalog:
  name: NWChem
  description: A computational chemistry software package designed to perform well on parallel HPC systems
  description_fi: Laskennallisen kemian ohjelmistopaketti, joka on suunniteltu toimimaan hyvin rinnakkaisissa HPC-järjestelmissä
  license_type: Free
  disciplines:
    - Chemistry
  available_on:
    - Puhti
    - Mahti
---

# NWChem { #nwchem }

NWChem tarjoaa monia eri menetelmiä molekyyli- ja jaksollisten järjestelmien ominaisuuksien laskemiseen käyttäen elektronisen aaltotoiminnon tai tiheyden tavanomaisia kvanttimekaanisia kuvauksia. Lisäksi NWChem pystyy suorittamaan klassista molekyylidynamiikkaa ja vapaenergiasimulaatioita. Näitä lähestymistapoja voidaan yhdistää suorittamaan sekä kvanttimekaniikkaan että molekyylimekaniikkaan perustuvia sekasimulointeja.

## Saatavilla { #available }

-   Puhti: 7.0.0
-   Mahti: 7.0.0

## Lisenssi { #license }

- Koodi on jaettu avoimena lähdekoodina [Educational Community License versio 2.0 (ECL 2.0)](https://opensource.org/license/ecl-2-0/) -lisenssin ehdoilla.

## Käyttö { #usage }

Tarkista suositellut versiot:

```bash
module avail nwchem
```

### Eräajon skriptiesimerkki Puhtille { #batch-script-example-for-puhti }

```bash
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed 
#SBATCH --time=00:10:00           # time as `hh:mm:ss`

module load nwchem/7.0.0
export NWCHEM_RUN=$PWD/NWCHEM_RUN_$SLURM_JOB_ID
mkdir -p $NWCHEM_RUN
export SCRATCH_DIR=$NWCHEM_RUN
srun $NWCHEM_EXE test.nw > test_$SLURM_NPROCS.out
seff $SLURM_JOBID
```

!!! note
    Erityisesti jotkin edistyneemmistä elektronikorrelaatiolaskuista voivat olla hyvin levy-I/O-intensiivisiä. Tällaiset ajot hyötyvät Puhtin nopean paikallistallennuksen käytöstä. Paikallislevyn käyttö tällaisissa töissä vähentää myös kuormitusta Lustre-rinnakkaistiedostojärjestelmässä.

### Eräajon skriptiesimerkki Puhtille paikallislevyä käyttäen { #batch-script-example-for-puhti-using-local-disk }

```bash
#!/bin/bash
#SBATCH --partition=large
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed
#SBATCH --time=00:10:00      # time as `hh:mm:ss`
#SBATCH --gres=nvme:100      # requested local disk space in GB 

module load nwchem/7.0.0
export NWCHEM_RUN=$LOCAL_SCRATCH
mkdir -p $NWCHEM_RUN
export SCRATCH_DIR=$NWCHEM_RUN
srun $NWCHEM_EXE test.nw > test_$SLURM_NPROCS.out
seff $SLURM_JOBID
```

### Eräajon skriptiesimerkki Mahtille { #batch-script-example-for-mahti }

```bash
#!/bin/bash -l
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=128
#SBATCH --account=<project>  # insert here the project to be billed
#SBATCH --time=00:10:00      # time as `hh:mm:ss`

module load nwchem/7.0.0
export NWCHEM_RUN=$PWD/NWCHEM_RUN_$SLURM_JOB_ID
mkdir -p $NWCHEM_RUN
export SCRATCH_DIR=$NWCHEM_RUN
srun $NWCHEM_EXE test.nw > test_$SLURM_NPROCS.out
```

Lähetä eräajo komennolla:

```bash
sbatch nwchem_job.bash
```

## Viitteet { #references }

Viittaa seuraavaan lähteeseen julkaistaessa NWChemillä saatuja tuloksia:

E. Aprà, E. J. Bylaska, W. A. de Jong, N. Govind, K. Kowalski, T. P. Straatsma, M. Valiev,
H. J. J. van Dam, Y. Alexeev, J. Anchell, V. Anisimov, F. W. Aquino, R. Atta-Fynn, J. Autschbach,
N. P. Bauman, J. C. Becca, D. E. Bernholdt, K. Bhaskaran-Nair, S. Bogatko, P. Borowski, J. Boschen,
J. Brabec, A. Bruner, E. Cauẽt, Y. Chen, G. N. Chuev, C. J. Cramer, J. Daily, M. J. O. Deegan,
T. H. Dunning Jr., M. Dupuis, K. G. Dyall, G. I. Fann, S. A. Fischer, A. Fonari, H. Früchtl,
L. Gagliardi, J. Garza, N. Gawande, S. Ghosh, K. Glaesemann, A. W. Götz, J. Hammond, V. Helms,
E. D. Hermes, K. Hirao, S. Hirata, M. Jacquelin, L. Jensen, B. G. Johnson, H. Jónsson,
R. A. Kendall, M. Klemm, R. Kobayashi, V. Konkov, S. Krishnamoorthy, M. Krishnan, Z. Lin,
R. D. Lins, R. J. Littlefield, A. J. Logsdail, K. Lopata, W. Ma, A. V. Marenich,
J. Martin del Campo, D. Mejia-Rodriguez, J. E. Moore, J. M. Mullin, T. Nakajima, D. R. Nascimento,
J. A. Nichols, P. J. Nichols, J. Nieplocha, A. Otero-de-la-Roza, B. Palmer, A. Panyala,
T. Pirojsirikul, B. Peng, R. Peverati, J. Pittner, L. Pollack, R. M. Richard, P. Sadayappan,
G. C. Schatz, W. A. Shelton, D. W. Silverstein, D. M. A. Smith, T. A. Soares, D. Song,
M. Swart, H. L. Taylor, G. S. Thomas, V. Tipparaju, D. G. Truhlar, K. Tsemekhman, T. Van Voorhis,
Á. Vázquez-Mayagoitia, P. Verma, O. Villa, A. Vishnu, K. D. Vogiatzis, D. Wang, J. H. Weare,
M. J. Williamson, T. L. Windus, K. Woliński, A. T. Wong, Q. Wu, C. Yang, Q. Yu, M. Zacharias,
Z. Zhang, Y. Zhao, and R. J. Harrison, "NWChem: Past, present, and future",
The Journal of Chemical Physics 152, 184102 (2020). DOI: 10.1063/5.0004997

## Lisätietoja { #more-information }

-   [NWChem: Pääsivu](https://nwchemgit.github.io/)
-   [NWChem-käyttäjädokumentaatio](https://nwchemgit.github.io/Home.html)
-   [NWChem-yhteisöfoorumi (vaatii rekisteröitymisen)](https://nwchemgit.github.io/Forum.html)