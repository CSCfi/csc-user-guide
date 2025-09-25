---
tags:
  - Free
catalog:
  name: Quantum ESPRESSO
  description: Electronic-structure calculations and materials modeling at the nanoscale
  description_fi: Elektronirakenteen laskenta ja materiaalien mallinnus nanoskaalassa
  license_type: Free
  disciplines:
    - Chemistry
  available_on:
    - Puhti
    - Mahti
    - LUMI
---

# Quantum ESPRESSO { #quantum-espresso }

Quantum ESPRESSO on avoimen lähdekoodin tietokoneohjelmien kokonaisuus elektronirakenteen laskentaan ja materiaalien mallinnukseen nanoskaalassa. Se perustuu tiheysfunktionaaliteoriaan, tasoaaltoihin ja pseudopotentiaaleihin.

## Saatavilla { #available }

Seuraavat versiot ovat saatavilla:

* Puhti: 7.4.1
* Mahti: 7.4.1
* LUMI: 7.4.1-cpu

## Lisenssi { #license }

Quantum ESPRESSO on vapaa ohjelmisto, joka on julkaistu
[GNU General Public License](https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt) -lisenssillä.

## Käyttö { #usage }

!!! info "Rajoitettu tuki saatavilla"
    CSC tarjoaa Quantum ESPRESSOlle vain rajallista tukea. Esiasennetut moduulit
    ovat käytettävissä ainoastaan käyttäjien mukavuuden vuoksi. Syvällisempää apua Quantum ESPRESSOn
    käyttöön saat lukemalla
    [virallista dokumentaatiota](https://www.quantum-espresso.org/documentation)
    tai ottamalla yhteyttä
    [Quantum ESPRESSO -yhteisöön](https://www.quantum-espresso.org/users-forum).

### Eräajon skriptiesimerkkejä { #batch-script-examples }

=== "Puhti"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=01:00:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=40
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=2G

    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

    module purge
    module load quantum-espresso/7.4.1

    srun pw.x < input.in > input.out
    ```

=== "Mahti"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=01:00:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=128
    #SBATCH --cpus-per-task=1

    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

    module purge
    module load quantum-espresso/7.4.1

    srun pw.x < input.in > input.out
    ```

=== "LUMI-C"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=standard
    #SBATCH --time=01:00:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=128
    #SBATCH --cpus-per-task=1
    #SBATCH --mem=0

    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

    module use /appl/local/csc/modulefiles
    module load quantum-espresso/7.4.1-cpu

    srun pw.x < input.in > input.out
    ```

### Huomioita rinnakkaistamisesta ja suorituskyvystä { #notes-on-parallelization-and-performance }

Oletusrinnakkaistus tehdään tasoaalloille, ellei muita vaihtoehtoja ole määritetty. Tämän parantamiseksi k‑pisteet (jos niitä on useampi kuin yksi) voidaan jakaa "pools"-ryhmiin `-npools`-lipulla. Lisäksi, kun ajoa suoritetaan useilla sadoilla ytimillä, skaalautuvuutta voidaan laajentaa edelleen jakamalla kukin pool "task groups" -ryhmiin, mikä jakaa Kohn–Sham-tiloihin liittyvän Fast Fourier -muunnosten (FFT) työkuorman. Tämä tehdään `-ntg`-lipulla.

Hyvän kuormantasauksen saavuttamiseksi MPI-prosessien välillä k‑pistepoolien lukumäärän tulisi olla k‑pisteiden määrän kokonaislukujakaja, ja FFT-rinnakkaistukseen käytettävien prosessorien lukumäärän tulisi olla smooth FFT -ruudukon kolmannen ulottuvuuden kokonaislukujakaja (tämän voi tarkistaa tulostiedostosta komennolla `grep "Smooth grid" *.out`).

Lisää rinnakkaistamisen tasoja esitellään
[Quantum ESPRESSO -dokumentaatiossa](https://www.quantum-espresso.org/Doc/user_guide/node20.html).

## Viitteet { #references }

Quantum ESPRESSO -jakelua hyödyntävässä tieteellisessä työssä tulisi viitata seuraaviin julkaisuihin:

> P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D.
> Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. Fabris,
> G. Fratesi, S. de Gironcoli, R. Gebauer, U. Gerstmann, C. Gougoussis, A.
> Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S.
> Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero,
> A. P. Seitsonen, A. Smogunov, P. Umari, R. M. Wentzcovitch, J. Phys.:
> Condens. Matter 21, 395502 (2009).

sekä

> P. Giannozzi, O. Andreussi, T. Brumme, O. Bunau, M. Buongiorno Nardelli, M.
> Calandra, R. Car, C. Cavazzoni, D. Ceresoli, M. Cococcioni, N. Colonna, I.
> Carnimeo, A. Dal Corso, S. de Gironcoli, P. Delugas, R. A. DiStasio Jr, A.
> Ferretti, A. Floris, G. Fratesi, G. Fugallo, R. Gebauer, U. Gerstmann, F.
> Giustino, T. Gorni, J Jia, M. Kawamura, H.-Y. Ko, A. Kokalj, E. Küçükbenli,
> M. Lazzeri, M. Marsili, N. Marzari, F. Mauri, N. L. Nguyen, H.-V. Nguyen, A.
> Otero-de-la-Roza, L. Paulatto, S. Poncé, D. Rocca, R. Sabatini, B. Santra, M.
> Schlipf, A. P. Seitsonen, A. Smogunov, I. Timrov, T. Thonhauser, P. Umari, N.
> Vast, X. Wu, S. Baroni, J. Phys.: Condens. Matter 29, 465901 (2017).

GPU-kiihdytetyn version käyttäjien tulisi lisäksi viitata seuraavaan artikkeliin:

> P. Giannozzi, O. Baseggio, P. Bonfà, D. Brunato, R. Car, I. Carnimeo, C.
> Cavazzoni, S. de Gironcoli, P. Delugas, F. Ferrari Ruffino, A. Ferretti, N.
> Marzari, I. Timrov, A. Urru, S. Baroni, J. Chem. Phys. 152, 154105 (2020).

Huomaa, että tekstissä ohjelmistoon viitattaessa muoto on "Quantum ESPRESSO". Katso myös pakettikohtainen dokumentaatio lisäsuositelluista viittauksista.
Pseudopotentiaalit tulisi viitata esimerkiksi seuraavasti:

> Käytimme pseudopotentiaaleja C.pbe-rrjkus.UPF ja O.pbe-vbc.UPF lähteestä
> <https://www.quantum-espresso.org>.

## Lisätietoja { #more-information }

* [Quantum ESPRESSO -verkkosivusto](https://www.quantum-espresso.org)
* [Quantum ESPRESSO -dokumentaatio](https://www.quantum-espresso.org/Doc/user_guide/)
* [Quantum ESPRESSO -foorumit](https://lists.quantum-espresso.org/mailman/listinfo/users)