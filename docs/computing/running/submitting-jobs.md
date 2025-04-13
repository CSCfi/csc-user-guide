
# Eräajon lähettäminen {#submitting-a-batch-job}

Lähetä työ jonoon komennolla `sbatch`:

```bash
sbatch <batch_job_file>
```

Esimerkiksi:

```bash
sbatch job.sh
```

Kun työ on lähetetty onnistuneesti, komento tulostaa lähetetyn työn ID-numeron.
Esimerkiksi `Submitted batch job 3609650`.

Tarkistaaksesi, onko työsi suorituksessa oikein:

```bash
squeue -u $USER
```

tai

```bash
squeue --me
```

Sinun pitäisi nähdä työsi ID ja muita tietoja näkyvissä päätteessä.

Peruuttaaksesi lähetetyn erätyön:

```bash
scancel <jobid>
```

Esimerkiksi,

```bash
scancel 3609650
```

Saadaksesi lisätietoa töistäsi:

```bash
sacct
```

Tiedot sisältävät työn tilan (`PENDING`, `RUNNING`, `COMPLETED`, `FAILED`, jne.) ja työn ID:n. Oletusarvoisesti `sacct`-komento
näyttää tietoa käyttäjän omista töistä, jotka on lähetetty jonoon kuluvana päivänä. Komennolla on myös laaja valikoima vaihtoehtoja ja
parametreja, joita voi käyttää valitsemaan, mitä tietoja näytetään. 
[Katso kaikki `sacct`-vaihtoehdot ja -parametrit](https://slurm.schedmd.com/sacct.html).

!!! varoitus "Vältä liiallista datan kyselyä `sacct`:llä"
    Älä kysy työn tietoja pitkältä aikaväliltä `sacct`:llä. `sacct` hakee tietonsa Slurm-kirjanpito tietokannasta, ja suurilla kyselyillä
    operaatio voi olla raskas järjestelmälle. Erityisesti vältä komennon suorittamista nopeasti monta kertaa peräkkäin. Voit ohjata
    tuotosdatan tiedostoon ja etsiä siitä tarvitsemasi tiedot analysoitavaksi.
    Esimerkiksi, tallentaaksesi edellisten 7 päivän tiedot tiedostoon `sacct-output.txt`:

    ```bash
    sacct --starttime now-7days > sacct-output.txt
    ```

## Lisätietoa {#more-information}

- [Puhti-erätöiden luominen](creating-job-scripts-puhti.md)
- [Mahti-erätöiden luominen](creating-job-scripts-mahti.md)
- [Saatavilla olevat erätyöosastot](batch-job-partitions.md)

