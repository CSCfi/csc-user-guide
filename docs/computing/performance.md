
# Suorituskyvyn Analysointi

## Nopean Aloituksen Oppaasta: Tehokkuusraportti `seff` {#quick-start-efficiency-report-with-seff}

Slurm-työn tehokkuusraportti (komento: `seff`) antaa nopean yhteenvedon pyydetyistä ja käytetyistä resursseista sekä käynnissä oleville että päättyneille erätehtäville.

```bash
seff <JOBID>
```

Se on helppo tapa saada yleiskuva siitä, kuinka tehokkaasti suorittimia käytettiin (CPU-tehokkuus) ja kuinka paljon varatusta muistista käytettiin todellisuudessa (muistitehokkuus).

!!! note "Vihje"
    Voit lisätä `seff`-komennon erätehtäväskriptisi loppuun, jotta saat aina tehokkuusraportin tehtävillesi: `seff $SLURM_JOBID`

Esimerkkiulostulo yhden solmun tehtävästä:
```bash
puhti-login12:~$ seff 366910
Job ID: 366910
Cluster: puhti
User/Group: louhivuo/louhivuo
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 40
CPU Utilized: 01:13:41
CPU Efficiency: 94.47% of 01:18:00 core-walltime
Job Wall-clock time: 00:01:57
Memory Utilized: 22.13 GB (estimated maximum)
Memory Efficiency: 14.16% of 156.25 GB (3.91 GB/core)
Job consumed 1.81 CSC billing units based on following used resources
CPU BU: 1.30
Mem BU: 0.51
```

Saadaksesi tarkempaa tietoa ohjelman suorituskyvystä, sinun tulisi käyttää jotain saatavilla olevista profilointityökaluista (katso alla).

## Profilointityökalut {#profiling-tools}

Hyvät profilointityökalut voivat auttaa saamaan täyden kuvan ohjelman laskennallisista ja viestintämalleista ja tunnistamaan mahdollisia suorituskyvyn pullonkauloja. CSC:lla on saatavilla useita profilointityökaluja:

* [Intel VTune Profiler](../apps/vtune.md) on tehokas profilointityökalu, jota voidaan käyttää suorituskykytietojen keräämiseen sovelluksesta ja se soveltuu sekä sarja- että monisäikeisille koodeille
* [Scalasca](../apps/scalasca.md) on jälkiperusteinen rinnakkaisen suorituskyvyn analyysityökalu MPI-, OpenMP- ja hybridiohjelmille MPI+OpenMP
* [Intel Trace Analyzer and Collector](../apps/itac.md) on MPI-profilointi- ja jäljitystyökalu rinnakkaisille ohjelmille
* [cProfile](../apps/cProfile.md) on suositeltu, sisäänrakennettu profilointityökalu Python-ohjelmille
* [nvprof](../apps/nvprof.md) on komentorivillä käytettävä CUDA-profilointi- ja jäljitystyökalu CUDA-ohjelmille
* [nsys](../apps/nsys.md) on Nsight Systems -ohjelmiston komentorajapinta, järjestelmätason suorituskykyanalyysityökalu, joka on suunniteltu visualisoimaan sovelluksen algoritmeja
* [ncu](../apps/ncu.md) on Nsight Compute -ohjelman komentorajapinta, työkalu alla koodien virheenkorjaukseen ja optimointiin.