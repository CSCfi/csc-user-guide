# Milloin erätyöni suoritetaan? {#when-will-my-batch-job-run}

Tarkka aika on mahdoton ennustaa. Fair share -tila jakaa resursseja työn prioriteetin perusteella, mutta työn aloitus riippuu myös pyydettyjen resurssien saatavuudesta sekä muiden käyttäjien työtehtävien prioriteeteista. Nykyisten töiden ja niiden pyytämien resurssien perusteella voidaan kuitenkin tehdä karkea ennuste. Näet kaikki työsi ja niiden työnumerot antamalla:

```bash
squeue -u $USER
```

Arvio mahdolliselle ajalle, milloin työ suoritetaan (jos uusia töitä ei ole lisätty ja jos kaikki käynnissä ja jonoissa olevat työt käyttävät kaiken pyytämänsä ajan), voidaan näyttää työnumerolle 22425300 seuraavasti:

```bash
[username@puhti-login12 ~]$ squeue -j 22425300 --start
   JOBID PARTITION     NAME     USER ST          START_TIME  NODES SCHEDNODES           NODELIST(REASON)
22425300     small cool_job username PD 2024-07-26T06:27:12      1 r05c49               (Resources)
```

`Priority` syynä odottamiseen tarkoittaa, että jonossa on muita korkeammalla prioriteetilla olevia töitä. `Resources` puolestaan tarkoittaa, että työ odottaa pyydettyjen resurssien vapautumista, ja se suoritetaan heti kun resurssit vapautuvat. Jos näet syyn

```
Nodes required for job are DOWN, DRAINED or reserved for jobs in higher priority partitions
```

älä huolestu. Tämä "syy" voi näyttää hälyttävältä, mutta yleensä solmut, joita työsi tarvitsee, ovat vain muiden töiden käytössä, kuten viesti sanoo, ja työsi jonottaa odotetusti.

Voit myös tarkastella töiden prioriteetteja seuraavasti:

```bash
squeue -u $USER -o "%.18i %.9P %.8j %.8u %.8T %.10M %.9l %.6D %Q"
```

Jonotuksen minimoinniksi, katso myös:

* [Kuinka arvioida, kuinka paljon muistia erätyöni tarvitsee](how-much-memory-my-job-needs.md)
* [Miksi erätyöni jonottaa niin pitkään?](why-is-my-job-queueing-so-long.md)