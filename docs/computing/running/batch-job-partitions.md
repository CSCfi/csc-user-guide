
# Käytettävissä olevat erätyöosastot {#available-batch-job-partitions}

CSC:n supertietokoneilla ohjelmia ajetaan lähettämällä ne osastoille,
jotka ovat SLURM-työkuormanhallinnan hallinnoimia loogisia solmuryhmiä.
Tämä sivu listaa Puhtin ja Mahtin supertietokoneiden käytettävissä olevat
SLURM-osastot sekä selittää niiden suunnitellut käyttötarkoitukset. Alla
ovat yleiset ohjeet SLURM-osastojen käyttämiseen järjestelmissämme:

1. **Käytä `test`- ja `gputest`-osastoja koodisi testaamiseen, ei tuotantoon.**
   Nämä osastot tarjoavat pääsyn vähempiin resursseihin kuin muut osastot,
   mutta niille lähetetyt työt saavat korkeamman etusijan ja saavat siten
   resursseja muiden töiden edellä.
2. **Pyydä useampia prosessoriytimiä vain, jos tiedät ohjelmasi tukevan
   rinnakkaista käsittelyä.** Useiden ytimien varaaminen ei automaattisesti
   nopeuta työtäsi. Ohjelmasi on kirjoitettava siten, että laskennan voi
   suorittaa useilla säikeillä tai prosesseilla. Useampien ytimien varaaminen
   itsessään ei tee muuta kuin pidentää jonotus aikaa.
3. **Käytä GPU-osastoja vain, jos tiedät ohjelmasi hyödyntävän GPU:ta.**
   Laskennan suorittaminen yhdellä tai useammalla GPU:lla on erittäin tehokas
   rinnakkaistamismenetelmä tiettyihin sovelluksiin, mutta ohjelmasi tulee
   olla konfiguroitu käyttämään CUDA-alustaa. Jos et ole varma, onko näin,
   on parempi lähettää se CPU-osastolle, koska sinulle osoitetaan resursseja
   nopeammin. Voit myös aina
   [ottaa yhteyttä CSC:n palvelupisteeseen](../../support/contact.md) kun olet
   epävarma.

Seuraavia komentoja voidaan käyttää näyttämään tietoa käytettävissä olevista
osastoista:

```bash
# Näyttää yhteenveto käytettävissä olevista osastoista
$ sinfo --summarize

# Näyttää tarkempia tietoja tietystä osastosta:
$ scontrol show partition <partition_name>
```

!!! info "LUMI-osastot"
    Käytettävissä olevat LUMI-erätyöosastot löytyvät
    [LUMI-dokumentaatiosta].

## Puhti osastot {#puhti-partitions}

Seuraavat ohjeet koskevat SLURM-osastoja Puhtilla:

1. **Pyydä vain tarvitsemasi muisti.** Muisti voi helposti muodostua
   resurssien jakelun pullonkaulaksi. Jopa jos haluttu määrä GPU:ta ja/tai
   CPU-ytimiä on jatkuvasti saatavilla, työsi istuu jonossa niin kauan kunnes
   pyydetty määrä muistista vapautuu. Siksi on suositeltavaa pyytää vain
   määrä, joka on tarpeen työsi suorittamiseen. Lisäksi, työn kuluttamien
   laskentayksikköjen määrä riippuu pyydetystä muistimäärästä, ei käytetystä.
   Katso lisää [kuinka arvioida muistitarpeesi](../../support/faq/how-much-memory-my-job-needs.md).
2. **Käytä `longrun`-osastoja vain tarpeen mukaan.** `longrun` ja
   `hugemem_longrun`-osastot tarjoavat pääsyn vähempiin resursseihin ja
   niillä on alhaisempi prioriteetti kuin muilla osastoilla, joten on
   suositeltavaa käyttää niitä vain töihin, jotka *todella* vaativat erittäin
   pitkän suorituksen (esim. jos ei ole tapaa keskeyttää ja uudelleenkäynnistää
   laskentaa).

### Puhti CPU-osastot {#puhti-cpu-partitions}

Puhti tarjoaa seuraavat osastot CPU-solmuille osoitettavien töiden
lähettämiseen:

| Osasto          | Aika<br>raja | Max CPU<br>ytimet | Max<br>solmut | [Solmutyypit](../systems-puhti.md) | Max muisti<br>per solmu | Max paikallinen tallennus<br>([NVMe]) per solmu |
|-----------------|-------------|---------------------|--------------|-------------------------------------|--------------------------|-----------------------------------------------|
| `test`          | 15 minuuttia| 80                  | 2            | M                                   | 185 GiB                  | ei koske                                     |
| `small`         | 3 päivää    | 40                  | 1            | M, L, IO                            | 373 GiB                  | 3600 GiB                                     |
| `large`         | 3 päivää    | 1040                | 26           | M, L, IO                            | 373 GiB                  | 3600 GiB                                     |
| `longrun`       | 14 päivää   | 40                  | 1            | M, L, IO                            | 373 GiB                  | 3600 GiB                                     |
| `hugemem`       | 3 päivää    | 160                 | 4            | XL, BM                              | 1496 GiB                 | 1490 GiB (XL), 5960 GiB (BM)                 |
| `hugemem_longrun` | 14 päivää | 40                  | 1            | XL, BM                              | 1496 GiB                 | 1490 GiB (XL), 5960 GiB (BM)                 |

### Puhti GPU-osastot {#puhti-gpu-partitions}

Puhti tarjoaa seuraavat osastot GPU-solmuille osoitettavien töiden
lähettämiseen:

| Osasto   | Aika<br>raja | Max<br>GPU:t | Max CPU<br>ytimet | Max<br>solmut | [Solmutyypit](../systems-puhti.md) | Max muisti<br>per solmu | Max paikallinen tallennus<br>([NVMe]) per solmu |
|----------|-------------|---------------|---------------------|--------------|-------------------------------------|--------------------------|-----------------------------------------------|
| `gputest`| 15 minuuttia| 8             | 80                  | 2            | GPU                                 | 373 GiB                  | 3600 GiB                                     |
| `gpu`    | 3 päivää    | 80            | 800                 | 20           | GPU                                 | 373 GiB                  | 3600 GiB                                     |

!!! info "Tasapuolinen GPU-solmujen käyttö Puhtilla"
    Sinun tulisi varata **enintään 10 CPU-ytimeä per GPU**.

### Puhti `interactive`-osasto {#puhti-interactive-partition}

`interactive`-osasto Puhtilla mahdollistaa
[interaktiivisten töiden](./interactive-usage.md) suorittamisen CPU-solmuilla.
Jos haluat suorittaa interaktiivisen työn GPU-solmulla, käytä `sinteractive`-
komentoa [`-g`-valinnan kanssa](./interactive-usage.md#sinteractive-on-puhti),
joka lähettää työn `gpu`-osastolle sen sijaan. Huomaa, että voit suorittaa
vain kaksi samanaikaista työtä Puhtin `interactive`-osastolla.

| Osasto       | Aika<br>raja | Max CPU<br>ytimet | Max<br>solmut | [Solmutyypit](../systems-puhti.md) | Max muisti<br>per solmu | Max paikallinen tallennus<br>([NVMe]) per solmu |
|--------------|-------------|---------------------|--------------|-------------------------------------|--------------------------|-----------------------------------------------|
| `interactive`| 7 päivää    | 8                   | 1            | IO                                  | 76 GiB                   | 720 GiB                                       |

## Mahti osastot {#mahti-partitions}

### Mahti CPU-osastot solmupohjaisella allokoinnilla {#mahti-cpu-partitions-with-node-based-allocation}

Mahti tarjoaa seuraavat osastot CPU-solmuille osoitettavien töiden
lähettämiseen. Näille osastoille lähetetyt työt vievät
[kaikki solmulla käytettävissä olevat resurssit](../systems-mahti.md#compute-nodes)
ja tekevät siitä muille töille saavuttamattoman. Siten työn tulisi ideaalisti
pystyä hyödyntämään kaiken varatun solmun 128 ytimen tehosesti. Vaikka
tietyissä tilanteissa voi olla hyödyllistä
[vajaa-allokoida solmuja](creating-job-scripts-mahti.md#undersubscribing-nodes),
huomaa, että työsi kuluttaa silti laskentayksiköitä varattujen *solmujen*
mutta ei CPU-ytimien perusteella.

Jotkut osastot ovat saatavilla vain erityisillä ehdoilla. `large`-osasto on
vain niiden projektien käytössä, jotka ovat
[suorittaneet skaalautuvuustestin](../../accounts/how-to-access-mahti-large-partition.md)
ja osoittaneet hyvää osastoresurssien käyttöä. `gc`-osasto, joka mahdollistaa
käyttäjien suorittaa erittäin suuria simulaatioita, on vain
[Grand Challenge -projektien](https://research.csc.fi/grand-challenge-proposals)
käytettävissä.

| Osasto   | Aika<br>raja | CPU ytimet<br>per solmu | Solmut<br>per työ | [Solmutyypit](../systems-mahti.md) | Muisti<br>per solmu | Max paikallinen tallennus<br>([NVMe]) per solmu | Vaatimukset                        |
|----------|-------------|--------------------------|--------------------|-------------------------------------|----------------------|-----------------------------------------------|----------------------------------|
| `test`   | 1 tunti     | 128                      | 1–2                | CPU                                 | 256 GiB              | ei koske                                     | ei koske                         |
| `medium` | 36 tuntia   | 128                      | 1–20               | CPU                                 | 256 GiB              | ei koske                                     | ei koske                         |
| `large`  | 36 tuntia   | 128                      | 20–200             | CPU                                 | 256 GiB              | ei koske                                     | [skaalautuvuustesti]             |
| `gc`     | 36 tuntia   | 128                      | 200–700            | CPU                                 | 256 GiB              | ei koske                                     | [Grand Challenge -projekti]     |

### Mahti CPU-osastot ydinpohjaisella allokoinnilla {#mahti-cpu-partitions-with-core-based-allocation}

Maktilla on kaksi CPU-osastoa, jotka mahdollistavat ytimien varaamisen koko
solmujen sijasta. Nämä ovat `small`-osasto ja `interactive`-osasto. Näissä
osastoissa töille allokoidaan 1.875 GiB muistia jokaista varattua CPU-ydintä
kohti, ja ainoa tapa varata enemmän muistia on varata lisää ytimiä. Nämä
osastot ovat myös erityisiä, koska voit varata paikallista tallennustilaa
solmulla. On tärkeää, että pyydät paikallista tallennustilaa vain, jos
voidaan hyödyntää sitä, eikä enempää kuin tarvitset. Koska paikallista
tallennustilaa on rajoitetusti, suuren määrän tallennustilan pyytäminen voi
lisätä jonotusaikaa.

`interactive`-osasto Mahtilla on tarkoitettu
[interaktiivisiin esikäsittely- ja jälkikäsittelytehtäviin](./interactive-usage.md).
Se mahdollistaa varata CPU-resursseja ilman, että koko solmu on käytössä, mikä
tarkoittaa, että muutkin työt voivat käyttää samaa solmua. Voit suorittaa jopa
8 samanaikaista työtä `interactive`-osastossa ja varata enintään 32 ydintä,
eli sinulla voi olla yksi työ, joka käyttää 32 ydintä, 8 työtä, jotka
käyttävät 4 ydintä kukin, tai mitä tahansa näiden välillä.

`small`-osasto on tarkoitettu pienimuotoisten CPU-laskentatehtävien
eräkäsittelyyn, jotka eivät tarvitse koko solmua. Se voi myös tukea
sovelluksia, jotka tarvitsevat paikallista tallennusta toimiakseen optimaalisesti.
Monet työt, jotka ovat perinteisesti käyttäneet Puhtia, voivat hyötyä tästä
osastosta.

| Osasto       | Aika<br>raja | Max CPU<br>ytimet | Max<br>solmut | [Solmutyypit](../systems-mahti.md) | Max muisti<br>per solmu | Max paikallinen tallennus<br>([NVMe]) per solmu |
|--------------|-------------|---------------------|--------------|-------------------------------------|--------------------------|-----------------------------------------------|
| `small`      | 3 päivää    | 128                 | 1            | CPU NVMe:llä                        | 240 GiB                  | 3500 GiB                                     |
| `interactive`| 7 päivää    | 32                  | 1            | CPU, CPU NVMe:llä                   | 60 GiB                   | 3500 GiB                                     |

### Mahti GPU-osastot {#mahti-gpu-partitions}

Mahti tarjoaa seuraavat osastot GPU-solmuille osoitettavien töiden
lähettämiseen. Elle muuta mainittu, työlle allokoidaan 122.5 GiB muistia jokaista
varattua GPU:ta kohden.

| Osasto     | Aika<br>raja | Max<br>GPU:t | Max CPU<br>ytimet | Max<br>solmut | [Solmutyypit](../systems-mahti.md) | Max muisti<br>per solmu | Max paikallinen tallennus<br>([NVMe]) per solmu |
|------------|-------------|---------------|---------------------|--------------|-------------------------------------|--------------------------|-----------------------------------------------|
| `gputest`  | 15 minuuttia| 4             | 128                 | 1            | GPU                                 | 490 GiB                  | 3500 GiB                                     |
| `gpusmall` | 36 tuntia   | 2             | 64                  | 1            | GPU                                 | 490 GiB                  | 3500 GiB                                     |
| `gpumedium`| 36 tuntia   | 24            | 768                 | 6            | GPU                                 | 490 GiB                  | 3500 GiB                                     |

!!! info "Tasapuolinen GPU-solmujen käyttö Mahtilla"
    Sinun tulisi varata **enintään 32 CPU-ytimeä per GPU**.

#### GPU-viipaleet {#gpu-slices}

Osa Mahtin `gpusmall`-osaston Nvidia A100 GPU:ista on jaettu yhteensä 28
pienemmäksi GPU-viipaleeksi, joilla on seitsemäsosa A100 GPU:n laskenta- ja
muistikapasiteetista. Käyttäessäsi GPU-viipaletta voit varata korkeintaan 4
CPU-ydintä. Lisäksi työlle allokoidaan 17.5 GiB muistia, eikä sitä voi
pyytää muuta määrää. Lopuksi voit varata vain yhden GPU-viipaleen per työ.
GPU-viipaleet on erityisesti tarkoitettu interaktiiviseen käyttöön, joka vaatii
GPU-kapasiteettia.

Varataksesi GPU-viipaleen käytä `sinteractive` `-g`-valinnalla tai lisää
`--gres=gpu:a100_1g.5gb:1` vaihtoehto määrittäessäsi `gpusmall`-osaston eräskriptissäsi.
Katso lisätietoja ohjeista [GPU-erätöiden luomisesta Mahtilla](creating-job-scripts-mahti.md#gpu-batch-jobs).

<!-- Linkit -->
[Grand Challenge -projekti]: https://research.csc.fi/grand-challenge-proposals
[LUMI-dokumentaatio]: https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/
[NVMe]: ../disk.md#compute-nodes-with-local-ssd-nvme-disks
[skaalautuvuustesti]: ../../accounts/how-to-access-mahti-large-partition.md
<!-- Linkit -->

