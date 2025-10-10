# Suorituskyvyn analysointi { #performance-analysis }

## Pikaopas: tehokkuusraportti seff-komennolla { #quick-start-efficiency-report-with-seff }

Slurm-työn tehokkuusraportti (komento: `seff`) antaa nopean yhteenvedon
pyydetyistä ja käytetyistä resursseista sekä käynnissä oleville että päättyneille eräajotöille.

```bash
seff <JOBID>
```

Tämä on helppo tapa saada kokonaiskuva siitä, kuinka tehokkaasti CPU-resurssia
käytettiin (CPU Efficiency) ja kuinka paljon varatusta muistista todellisuudessa
käytettiin (Memory Efficiency).

!!! note "Vinkki"
    voit lisätä `seff`-komennon eräajotyösi skriptin loppuun, jotta saat aina
    työn tehokkuusraportin: `seff $SLURM_JOBID`

Esimerkkituloste yksisolmuisesta työstä (huom: esimerkki viittaa vanhoihin CSC BU -yksiköihin; päivitetään myöhemmin):

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
Job consumed 1.81 CSC Billing Units based on following used resources
CPU BU: 1.30
Mem BU: 0.51
```

Jos haluat tarkempaa tietoa ohjelmasi suorituskyvystä, käytä jotakin saatavilla
olevista profilointityökaluista (ks. alla).


## Profilointityökalut { #profiling-tools }

Hyvät profilointityökalut auttavat muodostamaan kokonaiskuvan ohjelman laskenta-
ja viestintäkuvioista sekä tunnistamaan mahdolliset suorituskyvyn pullonkaulat.
CSC:llä on käytössä useita profilointityökaluja:

* [Intel VTune Profiler](../apps/vtune.md) on tehokas profilointityökalu, jolla voidaan
  kerätä sovelluksesi suorituskykytietoja; sopii sekä sarja- että monisäikeisille ohjelmille
* [Scalasca](../apps/scalasca.md) on tapahtumajälkiin perustuva rinnakkaisen suorituskyvyn analysointityökalu MPI-,
  OpenMP- ja hybridi MPI+OpenMP -ohjelmille
* [Intel Trace Analyzer and Collector](../apps/itac.md) on MPI-profilointi- ja
  jäljitystyökalu rinnakkaisohjelmille
* [cProfile](../apps/cProfile.md) on suositeltu, sisäänrakennettu profilointityökalu
  Python-ohjelmille
* [nvprof](../apps/nvprof.md) on komentorivipohjainen CUDA-profilointi- ja jäljitystyökalu
  CUDA-ohjelmille
* [nsys](../apps/nsys.md) on Nsight Systemsin komentorivikäyttöliittymä – järjestelmätason suorituskyvyn analysointityökalu, joka on suunniteltu visualisoimaan sovelluksen algoritmeja
* [ncu](../apps/ncu.md) on Nsight Computen komentorivikäyttöliittymä; työkalu CUDA-ydinten virheenkorjaukseen ja optimointiin