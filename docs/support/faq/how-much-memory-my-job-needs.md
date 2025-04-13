
# Kuinka arvioida, kuinka paljon muistia erätehtäväni tarvitsee? {#how-to-estimate-how-much-memory-my-batch-job-needs}

On vaikeaa arvioida työtehtävien resurssivaatimuksia etukäteen. Tarkista ensin
ohjelmiston dokumentaatiosta, antavatko kehittäjät mitään tietoa tyypillisestä
muistin käytöstä. Voit myös käyttää aiempaa tietoa samanlaisista valmiista
tehtävistä.

## seff - Slurm EFFiciency {#seff---slurm-efficiency}

`seff` tulostaa yhteenvedon pyydetyistä ja käytetyistä resursseista sekä
käynnissä oleville että valmistuneille erätehtäville:

```
seff <slurm jobid>
```

Voit myös lisätä `seff`-komennon eräkäsikirjoituksesi loppuun tulostamaan
muistin käytön työn lopussa stdoutiin.

```
seff $SLURM_JOBID
```

Huomaa, että `seff` ei näytä tietoja *käynnissä* olevista tehtävistä, jotka on
käynnistetty ilman `srun`-komentoa, mutta tilastot ovat hyviä, kun työ päättyy.
`seff` näyttää myös koottuja tietoja GPU:n käytön tehokkuudesta.

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
Job consumed 4.27 CSC billing units based on following used resources
Billed project: project_2001234
CPU BU: 4.19
Mem BU: 0.08
```

Yllä olevien tietojen huomiot: CPU-tehokkuus on ollut erittäin hyvä (96 %) ja
muistitehokkuus 71 %. Tämä on hyvä, sillä vain noin 2 GB jäi käyttämättä. On
suositeltavaa jättää muutaman GB turvamarginaali kokonaismuistin suhteen.

## Räätälöidyt kyselyt Slurm-laskutukseen {#custom-queries-to-slurm-accounting}

Voit tarkistaa suoritetun työn ajan ja muistin käytön myös `sacct`-komennolla:

```bash
sacct -o jobid,reqmem,maxrss,averss,elapsed -j <slurm jobid>
```

missä `-o`-lippu määrittää tulosteen seuraavasti:

* `jobid` = Slurm-työn ID jatkeineen työn vaiheille.
* `reqmem` = Muisti, jota pyysit Slurmista.
* `maxrss` = Suurin määrä muistia, jota joku prosessi on käyttänyt missä tahansa
  työn kohdassa. Tämä pätee suoraan sarjatyötehtäviin. Rinnakkaisille töille
  sinun on kerrottava ytimien lukumäärällä (max. 40 Puhti-koneella, koska tämä 
  raportoidaan vain siitä solmusta, jossa käytettiin eniten muistia).
* `averss` = Keskimääräinen muistin käyttö per prosessi (tai ydin). Kokonaismuistin
  käytön saamiseksi kerro tämä ytimien lukumäärällä (max. 40 Puhti-koneella, eli
  täydellä nodella) siinä tapauksessa, että pyydät muistia
  `--mem=<value>` etkä `--mem-per-cpu=<value>`.
* `elapsed` = Aika, joka kului työn suorittamiseen.

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

Huomioi seuraavat asiat:

* Rivillä, jotka sisältävät `.ba+` ja `.ex+`-päätteitä, liittyvät erätehtävän
  asetuksiin, sinun ei tarvitse huolehtia niistä tässä vaiheessa.
* Olet pyytänyt 200 MB per ydin eli yhteensä 40 x 200 MB = 8000 MB 
  (= 7.81 GB kuten `seff` raportoi).
* Tehtäväsi on käyttänyt enintään 145493 KB muistia, eli 142 MB per ydin. 
  Kertomalla tämä ytimien lukumäärällä (40) saadaan kokonaismuistin käyttöön
  5683 MB = 5.55 GB (kuten myös `seff` raportoi).
* Kuuden minuutin erätehtävä on liian lyhyt! Jos sinulla on monta tällaista 
  työtä, suorita ne peräkkäin samassa työssä erillisinä työnvaiheina. Nyt
  työn perustamiskustannukset ovat merkittävät verrattuna varsinaiseen
  laskentaan.

!!! info "Muistiyksiköistä huomautus"
    Muistiyksiköissä käytetään binäärisiä etuliitteitä. Esimerkiksi 1 GB = 1024 MB = 
    1024² KB. Siksi yksikkömuunnokset voivat tuntua hämmentäviltä.

## Yleisiä ohjeita ja vinkkejä {#general-guidelines-and-tips}

Muista, että samanlainen mutta silti uusi työ saattaa tarvita viime kädessä
erilaisia resursseja. Jos yliarvioit tarvittavan suoritusajan, työ saattaa
joutua jonoon pidemmäksi aikaa kuin olisi tarpeen. Mitään resursseja ei kuitenkaan
haaskata tai laskuteta. Tässä huomattava ero (jonotuksen kannalta) on se, onko
työ alle 3 päivää vai enemmän. `longrun`-osaston töillä on alhaisempi prioriteetti
ja ne ovat jonossaan pidempään.

Kuitenkin, **jos yliarvioit muistin tarpeen, resursseja haaskataan**. Mieti
tätä: jos työsi käyttää vain 4 ydintä, mutta koko solmun muistin, niin muut
työt eivät mahdu siihen solmuun ja jäljelle jäävät *N* - 4 ydintä jäävät
käyttämättä. Myös koko muistivaatimus - käytetty tai ei - laskutetaan laskenta-
kiintiöstäsi.

Huomaa, että jos työsi **tarvitsee** muistia, on täysin sallittua varata koko
solmun muisti, mutta älä varaa sitä "varmuuden vuoksi" tai siksi, ettet tiedä,
kuinka paljon työ tarvitsee. Voit saada arvion aiemmista samanlaisista töistä
kysymällä tämän tiedon yllä näytettyjen komentojen avulla. Tarvitset vain
Slurm-työn tunnuksen näiden töiden kohdalla.
