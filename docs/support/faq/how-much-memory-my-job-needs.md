# Kuinka arvioida, kuinka paljon muistia eräajoni tarvitsee? { #how-to-estimate-how-much-memory-my-batch-job-needs }

Työn tarkkojen resurssivaatimusten arvioiminen etukäteen on hankalaa. Aloita tarkistamalla ohjelmiston dokumentaatio: kertovatko kehittäjät tyypillisestä muistin käytöstä. Voit hyödyntää myös aiempien, vastaavien valmiiden ajojen tietoja.

## seff - Slurmin tehokkuus { #seff-slurm-efficiency }

`seff` tulostaa yhteenvedon pyydetyistä ja käytetyistä resursseista sekä käynnissä oleville että päättyneille eräajoille:

```
seff <slurm jobid>
```

Voit myös lisätä `seff`-komennon eräajon skriptin loppuun, jolloin muistin käyttö tulostuu työn päättyessä standarditulosteeseen.

```
seff $SLURM_JOBID
```

Huomaa, että `seff` ei näytä tietoja käynnissä olevista ajoista, jotka on käynnistetty ilman `srun`-komentoa, mutta tilastot ovat saatavilla työn päätyttyä. `seff` näyttää myös koosteita GPU-käytön tehokkuudesta.

```
[user@puhti-login11 ~]$ seff 22361601
Job ID: 22361601
Cluster: puhti
User/Group: user/user
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 40
CPU Utilized: 04:01:36
CPU Efficiency: 96.13% of 04:11:20 core-walltime
Job Wall-clock time: 00:06:17
Memory Utilized: 5.55 GB (estimated maximum)
Memory Efficiency: 71.04% of 7.81 GB (200.00 MB/core)
Job consumed 4.27 CSC Billing Units based on following used resources
Billed project: project_2001234
CPU BU: 4.19
Mem BU: 0.08
```

Huomioita yllä olevista tiedoista: Suorittimen tehokkuus on ollut erittäin hyvä (96 %) ja muistin tehokkuus 71 %. Tämä on hyvä, sillä käyttämättä jäi vain noin 2 GB. Kokonaismuistille suositellaan muutaman gigatavun varmuusmarginaalia.

Huomaa, että yllä oleva esimerkkituloste viittaa CSC:n vanhoihin BU:ihin.

## Mukautetut haut Slurmin kirjanpitoon { #custom-queries-to-slurm-accounting }

Voit tarkistaa päättyneen työn ajan ja muistin käytön myös `sacct`-komennolla:

```bash
sacct -o jobid,reqmem,maxrss,averss,elapsed -j <slurm jobid>
```

missä `-o`-valitsin määrittelee tulosteen seuraavasti:

- `jobid` = Slurmin työn tunniste, johon sisältyvät myös työn vaiheiden laajenteet.
- `reqmem` = Muistimäärä, jonka pyysit Slurmilta.
- `maxrss` = Suurin minkä tahansa prosessin kyseisessä työssä milloinkin käyttämä muistimäärä. Tämä pätee suoraan sarja-ajoihin. Rinnakkaisajoissa arvo on kerrottava ytimien lukumäärällä (Puhdissa enintään 40), koska tieto raportoidaan vain siltä solmulta, joka käytti eniten muistia.
- `averss` = Prosessia (tai ydintä) kohti keskimäärin käytetty muisti. Kokonaismuistin käytön saat kertomalla tämän ydinten määrällä (Puhdissa enintään 40, eli koko solmu), jos pyydät muistia muodossa `--mem=<value>` etkä `--mem-per-cpu=<value>`.
- `elapsed` = Aika, joka työn valmistumiseen kului.

Esimerkiksi sama työ kuin yllä:

```
[user@puhti-login11 ~]$ sacct -j 22361601 -o jobid,reqmem,maxrss,averss,elapsed
JobID            ReqMem     MaxRSS     AveRSS    Elapsed 
------------ ---------- ---------- ---------- ---------- 
22361601          8000M                         00:06:17 
22361601.ba+                 7286K      7286K   00:06:17 
22361601.ex+                 2349K      2349K   00:06:17 
22361601.0                 145493K  139994035   00:06:17 
```

Huomaa seuraavat seikat:

- Rivit, joiden job step -tunnisteet päättyvät `.ba+` ja `.ex+`, liittyvät eräajon alustukseen; sinun ei tarvitse tässä vaiheessa välittää niistä.
- Olet pyytänyt 200 MB per ydin, eli yhteensä 40 × 200 MB = 8000 MB (= 7,81 GB `seff`-raportin mukaan).
- Työsi on käyttänyt enimmillään 145493 KB, eli 142 MB muistia per ydin. Kertomalla ytimien määrällä (40) saadaan kokonaismuistin käytöksi 5683 MB = 5,55 GB (kuten `seff` myös raportoi).
- 6 minuutin eräajo on liian lyhyt! Jos sinulla on monta tällaista ajoa, suorita ne peräkkäin samassa työssä erillisinä job steppeinä. Muuten työn alustuksen aiheuttama overhead on merkittävä suhteessa varsinaiseen laskentaan.

!!! info "Huomio muistiyksiköistä"
    Muistiyksiköissä käytetään binäärisiä etuliitteitä. Esimerkiksi 1 GB = 1024 MB =
    1024² KB. Tämän vuoksi yksikkömuunnokset voivat vaikuttaa hämmentäviltä.

## Yleisiä ohjeita ja vinkkejä { #general-guidelines-and-tips }

Muista, että samankaltaisellakin, mutta uudella ajolla voi lopulta olla erilaiset tarpeet. Jos yliarvioit tarvittavan ajoajan, työsi saattaa jonottaa tarpeettoman pitkään. Resursseja ei kuitenkaan tuhlata eikä laskuteta. Jonotuksen kannalta merkittävä raja on, onko työn kesto alle vai yli 3 päivää. `longrun`-partitiossa olevilla töillä on alempi prioriteetti ja ne jonottavat pidempään.

Sen sijaan, jos yliarvioit muistin tarpeen, resursseja tuhlataan. Mieti tätä: jos työsi käyttää vain 4 ydintä, mutta kaiken solmun muistin, muille töille ei jää tilaa ja solmun jäljelle jäävät *N* - 4 ydintä jäävät tyhjäkäynnille. Lisäksi koko pyydetty muistimäärä – käytit sitä tai et – veloitetaan laskentakiintiöstäsi.

Huomaa, että jos työsi tarvitsee muistia, on täysin ok varata koko solmun muisti. Älä kuitenkaan varaa sitä ”varmuuden vuoksi” tai siksi, ettet tiedä, kuinka paljon työ tarvitsee. Saat arvion aiemmista samankaltaisista ajoista kysymällä tiedot yllä esitetyillä komennoilla. Tarvitset vain niiden töiden Slurm-työtunnuksen.