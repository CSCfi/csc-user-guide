# Saatavilla olevat eräajon osiot { #available-batch-job-partitions }

CSC:n supertietokoneilla ohjelmia ajetaan lähettämällä ne osioihin, jotka ovat SLURM-työkuormanhallinnan hallinnoimia loogisia solmuryhmiä. Tällä sivulla luetellaan Puhti- ja Mahti-supertietokoneiden saatavilla olevat SLURM-osiot sekä selitetään niiden käyttötarkoitukset. Alla ovat yleiset ohjeet osioiden käyttöön järjestelmissämme:

1. Käytä osioita `test` ja `gputest` koodisi testaamiseen, älä tuotantoon.
   Näissä osioissa on vähemmän resursseja kuin muissa osioissa, mutta niihin lähetetyillä töillä on korkeampi prioriteetti ja ne saavat siten resursseja ennen muita töitä.
2. Varaa useampia CPU-ytimiä vain, jos tiedät ohjelmasi tukevan rinnakkaislaskentaa.
   Useamman ytimen varaaminen ei automaattisesti nopeuta työtäsi. Ohjelman on oltava kirjoitettu siten, että laskenta voidaan suorittaa useissa säikeissä tai prosesseissa. Pelkkä ytimien lisääminen ei tee mitään muuta kuin pidentää jonotusaikaa.
3. Käytä GPU-osioita vain, jos tiedät ohjelmasi pystyvän hyödyntämään GPU:ita.
   Laskennan suorittaminen yhdellä tai useammalla GPU:lla on erittäin tehokas rinnakkaistusmenetelmä tietyille sovelluksille, mutta ohjelman on oltava konfiguroitu käyttämään CUDA-alustaa. Jos olet epävarma, on parempi lähettää työ CPU-osioon, koska saat resurssit todennäköisesti nopeammin. Voit myös aina [ottaa yhteyttä CSC Service Deskiin](../../support/contact.md), jos epäröit.

Seuraavilla komennoilla saat tietoa käytettävissä olevista osioista:

```bash
# Display a summary of available partitions
$ sinfo --summarize

# Display details about a specific partition:
$ scontrol show partition <partition_name>
```

!!! info "LUMI-osiot"
    Saatavilla olevat LUMI-eräajon osiot löytyvät [LUMI documentation] -sivulta.

## Puhti-osiot { #puhti-partitions }

Seuraavat ohjeet koskevat Puhdin SLURM-osioita:

1. Varaa vain tarvitsemasi määrä muistia. Muisti voi helposti muodostua resurssienjaon pullonkaulaksi. Vaikka haluttu määrä GPU:ita ja/tai CPU-ytimiä olisi jatkuvasti vapaana, työsi odottaa jonossa niin kauan, että pyydetty määrä muistia vapautuu. Siksi on suositeltavaa pyytää vain työn suorittamiseen tarvittava muistimäärä. Lisäksi työn kuluttamien CPU/GPU-laskutusyksikköjen määrä riippuu pyydetystä muistista, ei tosiasiallisesta käytöstä. Katso ohjeet: [how to estimate your memory requirements](../../support/faq/how-much-memory-my-job-needs.md).
2. Käytä `longrun`-osioita vain tarvittaessa. Osioilla `longrun` ja `hugemem_longrun` on vähemmän resursseja ja alempi prioriteetti kuin muilla osioilla, joten niitä suositellaan käytettäväksi vain töihin, jotka todella vaativat hyvin pitkän ajoajan (esim. kun laskentaa ei voi checkpointata ja jatkaa).

### Puhdin CPU-osiot { #puhti-cpu-partitions }

Puhdissa on seuraavat osiot töiden lähettämiseen CPU-solmuille:

| Osio             | Aika<br>raja | Enintään CPU-<br>ytimiä | Enintään<br>solmuja | [Solmutyypit](../systems-puhti.md) | Enimmäismuisti<br>per solmu | Enimmäispaikallinen tallennus<br>([NVMe]) per solmu |
|------------------|--------------|-------------------------|---------------------|-------------------------------------|-----------------------------|-----------------------------------------------------|
| `test`           | 15 minuuttia | 80                      | 2                   | M                                   | 185 GiB                     | n/a                                                 |
| `small`          | 3 päivää     | 40                      | 1                   | M, L, IO                            | 373 GiB                     | 3600 GiB                                            |
| `large`          | 3 päivää     | 1040                    | 26                  | M, L, IO                            | 373 GiB                     | 3600 GiB                                            |
| `longrun`        | 14 päivää    | 40                      | 1                   | M, L, IO                            | 373 GiB                     | 3600 GiB                                            |
| `hugemem`        | 3 päivää     | 160                     | 4                   | XL, BM                              | 1496 GiB                    | 1490 GiB (XL), 5960 GiB (BM)                        |
| `hugemem_longrun`| 14 päivää    | 40                      | 1                   | XL, BM                              | 1496 GiB                    | 1490 GiB (XL), 5960 GiB (BM)                        |

### Puhdin GPU-osiot { #puhti-gpu-partitions }

Puhdissa on seuraavat osiot töiden lähettämiseen GPU-solmuille:

| Osio     | Aika<br>raja | Enintään<br>GPU:ita | Enintään CPU-<br>ytimiä | Enintään<br>solmuja | [Solmutyypit](../systems-puhti.md) | Enimmäismuisti<br>per solmu | Enimmäispaikallinen tallennus<br>([NVMe]) per solmu |
|----------|--------------|---------------------|--------------------------|---------------------|-------------------------------------|-----------------------------|-----------------------------------------------------|
| `gputest`| 15 minuuttia | 8                   | 80                       | 2                   | GPU                                 | 373 GiB                     | 3600 GiB                                            |
| `gpu`    | 3 päivää     | 80                  | 800                      | 20                  | GPU                                 | 373 GiB                     | 3600 GiB                                            |

!!! info "GPU-solmujen oikeudenmukainen käyttö Puhtissa" 
    Varaa enintään 10 CPU-ydintä per GPU.

### Puhdin `interactive`-osio { #puhti-interactive-partition }

Puhdin `interactive`-osio mahdollistaa [interaktiivisten töiden](./interactive-usage.md) ajamisen CPU-solmuilla. Jos haluat ajaa interaktiivisen työn GPU-solmulla, käytä `sinteractive`-komentoa [valitsimen `-g` kanssa](./interactive-usage.md#sinteractive-on-puhti), jolloin työ lähetetään `gpu`-osioon. Huomaa, että Puhdin `interactive`-osiossa voi ajaa enintään kaksi samanaikaista työtä.

| Osio          | Aika<br>raja | Enintään CPU-<br>ytimiä | Enintään<br>solmuja | [Solmutyypit](../systems-puhti.md) | Enimmäismuisti<br>per solmu | Enimmäispaikallinen tallennus<br>([NVMe]) per solmu |
|---------------|--------------|-------------------------|---------------------|-------------------------------------|-----------------------------|-----------------------------------------------------|
| `interactive` | 7 päivää     | 8                       | 1                   | IO                                  | 76 GiB                      | 720 GiB                                             |

## Mahti-osiot { #mahti-partitions }

### Mahtin CPU-osiot solmupohjaisella varauksella { #mahti-cpu-partitions-with-node-based-allocation }

Mahtissa on seuraavat osiot töiden lähettämiseen CPU-solmuille. Näihin osioihin lähetetyt työt varaavat [kaikki solmun resurssit](../systems-mahti.md#compute-nodes) ja estävät muiden töiden pääsyn solmuun. Siksi työn tulisi mielellään kyetä käyttämään tehokkaasti kaikki varatun solmun 128 ydintä. Vaikka joissain tilanteissa voi olla järkevää [alivarata solmuja](creating-job-scripts-mahti.md#undersubscribing-nodes), huomaa, että laskutus perustuu varattujen solmujen määrään, ei CPU-ytimiin.

Jotkin osiot ovat käytettävissä vain erityisin ehdoin. `large`-osio on käytettävissä vain projekteille, jotka ovat [suorittaneet skaalautuvuustestin](../../accounts/how-to-access-mahti-large-partition.md) ja osoittaneet hyvän resurssien hyödyntämisen. `gc`-osio, jolla voi ajaa erittäin suuria simulointeja, on käytettävissä vain [Grand Challenge projects] -projekteille.

| Osio     | Aika<br>raja | CPU-ytimiä<br>per solmu | Solmuja<br>per työ | [Solmutyypit](../systems-mahti.md) | Muisti<br>per solmu | Enimmäispaikallinen tallennus<br>([NVMe]) per solmu | Vaatimukset                  |
|----------|--------------|-------------------------|--------------------|-------------------------------------|---------------------|-----------------------------------------------------|------------------------------|
| `test`   | 1 tunti      | 128                     | 1–2                | CPU                                 | 256 GiB             | n/a                                                 | n/a                          |
| `medium` | 36 tuntia    | 128                     | 1–20               | CPU                                 | 256 GiB             | n/a                                                 | n/a                          |
| `large`  | 36 tuntia    | 128                     | 20–200             | CPU                                 | 256 GiB             | n/a                                                 | [scalability test]           |
| `gc`     | 36 tuntia    | 128                     | 200–700            | CPU                                 | 256 GiB             | n/a                                                 | [Grand Challenge project]    |

### Mahtin CPU-osiot ydinpohjaisella varauksella { #mahti-cpu-partitions-with-core-based-allocation }

Kaksi Mahtin CPU-osiota mahdollistaa ytimien varaamisen kokonaisen solmun sijaan: `small` ja `interactive`. Näissä osioissa töille myönnetään 1,875 GiB muistia jokaista varattua CPU-ydintä kohti, ja ainoa tapa saada enemmän muistia on varata enemmän ytimiä. Näissä osioissa voi myös varata solmukohtaista paikallista tallennustilaa. On tärkeää pyytää paikallista tallennusta vain, jos osaat hyödyntää sitä, eikä enempää kuin tarvitset. Koska paikallinen tallennus on rajallinen resurssi, suuri varaus voi lisätä jonotusaikaa.

Mahtin `interactive`-osio on tarkoitettu [interaktiivisiin esi- ja jälkikäsittelytehtäviin](./interactive-usage.md). Se mahdollistaa CPU-resurssien varaamisen ilman, että koko solmu varataan, mikä tarkoittaa, että samaan solmuun voidaan sijoittaa myös muita töitä. Voit ajaa `interactive`-osiossa enintään 8 samanaikaista työtä ja varata enintään 32 ydintä, eli esimerkiksi yhden työn 32 ytimellä, 8 työtä 4 ytimellä tai mitä tahansa siltä väliltä.

`small`-osio on tarkoitettu pienten CPU-laskentatöiden eräajoon, kun koko solmua ei tarvita. Se soveltuu myös sovelluksille, jotka hyötyvät paikallisesta tallennuksesta. Monet työt, jotka ovat perinteisesti käyttäneet Puhtia, voivat hyötyä tästä osiosta.

| Osio          | Aika<br>raja | Enintään CPU-<br>ytimiä | Enintään<br>solmuja | [Solmutyypit](../systems-mahti.md) | Enimmäismuisti<br>per solmu | Enimmäispaikallinen tallennus<br>([NVMe]) per solmu |
|---------------|--------------|-------------------------|---------------------|-------------------------------------|-----------------------------|-----------------------------------------------------|
| `small`       | 3 päivää     | 128                     | 1                   | CPU with NVMe                       | 240 GiB                     | 3500 GiB                                            |
| `interactive` | 7 päivää     | 32                      | 1                   | CPU, CPU with NVMe                  | 60 GiB                      | 3500 GiB                                            |

### Mahtin GPU-osiot { #mahti-gpu-partitions }

Mahtissa on seuraavat osiot töiden lähettämiseen GPU-solmuille. Ellei toisin mainita, työlle myönnetään 122,5 GiB muistia jokaista varattua GPU:ta kohti.

| Osio        | Aika<br>raja | Enintään<br>GPU:ita | Enintään CPU-<br>ytimiä | Enintään<br>solmuja | [Solmutyypit](../systems-mahti.md) | Enimmäismuisti<br>per solmu | Enimmäispaikallinen tallennus<br>([NVMe]) per solmu |
|-------------|--------------|---------------------|--------------------------|---------------------|-------------------------------------|-----------------------------|-----------------------------------------------------|
| `gputest`   | 15 minuuttia | 4                   | 128                      | 1                   | GPU                                 | 490 GiB                     | 3500 GiB                                            |
| `gpusmall`  | 36 tuntia    | 2                   | 64                       | 1                   | GPU                                 | 490 GiB                     | 3500 GiB                                            |
| `gpumedium` | 36 tuntia    | 24                  | 768                      | 6                   | GPU                                 | 490 GiB                     | 3500 GiB                                            |

!!! info "GPU-solmujen oikeudenmukainen käyttö Mahtissa"
    Varaa enintään 32 CPU-ydintä per GPU.

#### GPU-viipaleet { #gpu-slices }

Osa Mahtin `gpusmall`-osion Nvidia A100 -GPU:ista on jaettu yhteensä 28 pienemmäksi GPU-viipaleeksi, joilla on yhden seitsemäsosan laskenta- ja muistikapasiteetti täydestä A100-GPU:sta. GPU-viipaletta käytettäessä voit varata enintään 4 CPU-ydintä. Lisäksi työlle myönnetään 17,5 GiB muistia, eikä määrää voi muuttaa. Lopuksi voit varata vain yhden GPU-viipaleen per työ. GPU-viipaleet on tarkoitettu erityisesti interaktiiviseen käyttöön, joka vaatii GPU-kapasiteettia.

Varataksesi GPU-viipaleen käytä `sinteractive`-komentoa valitsimen `-g` kanssa tai lisää `--gres=gpu:a100_1g.5gb:1` yhdessä `gpusmall`-osion määrittelyn kanssa eräajon skriptiin. Lisätietoja: [creating GPU batch jobs on Mahti](creating-job-scripts-mahti.md#gpu-batch-jobs).

<!-- Links -->
[Grand Challenge project]: https://research.csc.fi/grand-challenge-proposals
[LUMI documentation]: https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/
[NVMe]: ../disk.md#compute-nodes-with-local-ssd-nvme-disks
[scalability test]: ../../accounts/how-to-access-mahti-large-partition.md
<!-- Links -->