
---
tags:
  - Free
---

# Qiskit-on-iqm

Qiskit on IQM on avoimen lähdekoodin qiskit-sovitin IQM:n kvanttitietokoneille. Se on asennettu nimellä `helmi_qiskit` LUMI:lle. Sitä käytetään kvanttipiirien ajamiseen [Helmissä](../computing/quantum-computing/helmi/running-on-helmi.md).

## Saatavilla {#available}

Tällä hetkellä tuetut [qiskit-on-iqm](https://iqm-finland.github.io/qiskit-on-iqm/) versiot:

| Versio | Moduuli                              | LUMI  | Huomautuksia     |
|:-------|:-------------------------------------|:-----:|------------------|
| 15.5   | `helmi_qiskit/15.5`                  | X     |                  |

Kaikki moduulit perustuvat Tykkyyn käyttäen LUMI-container-wrapperia. Kääreskriptit on tarjottu niin, että yleiset komennot kuten `python`, `python3`, `pip` ja `pip3` toimivat normaalisti. Lisätietoja: [LUMI container wrapper](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/).

Moduuli sisältää python-paketteja, joita usein käytetään qiskitin kanssa, kuten qiskit-experiments, matplotlib, numpy ja jupyterlab.

## Lisenssi {#license}

qiskit-on-iqm on lisensoitu [Apache License 2.0](https://github.com/iqm-finland/qiskit-on-iqm/blob/main/LICENSE) -lisenssillä.

## Käyttö {#usage}

Käyttääkseen `helmi_qiskit` LUMI:ssa, alusta se komennolla:

```bash
module use /appl/local/quantum/modulefiles
```

ja 

```bash
module load helmi_qiskit
```

Tämä komento näyttää myös, kuinka `helmi_qiskit` ladataan:

```bash
module avail helmi_qiskit
```

### Esimerkkipartition-skripti {#example-batch-script}

Esimerkkipartition-skripti kvanttityön ajamiseen Helmillä:

```bash title="LUMI"
#!/bin/bash -l

#SBATCH --job-name=helmijob     # Työn nimi
#SBATCH --output=helmijob.o%j   # Stdout-lähtötiedoston nimi
#SBATCH --error=helmijob.e%j    # Stderr-virhetiedoston nimi
#SBATCH --partition=q_fiqci     # Partitio (jono) nimi
#SBATCH --ntasks=1              # Yksi tehtävä (prosessi)
#SBATCH --cpus-per-task=1       # Ytimien (säikeiden) määrä
#SBATCH --mem-per-cpu=1G        # Muistin allokointi
#SBATCH --time=00:15:00         # Suoritusaika (hh:mm:ss)
#SBATCH --account=project_xxx   # Projekti laskutusta varten

module use /appl/local/quantum/modulefiles
module load helmi_qiskit

python -u quantum_job.py
```

Lähetä skripti komennolla `sbatch <script_name>.sh`.

## Lisää tietoa {#more-information}

- [Qiskit-IQM-dokumentaatio](https://iqm-finland.github.io/qiskit-on-iqm/)
- [Kvanttitietokoneet](../computing/quantum-computing/helmi/running-on-helmi.md)

