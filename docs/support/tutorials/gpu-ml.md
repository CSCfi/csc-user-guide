
---
title: GPU-luotettu koneoppiminen
---

# GPU-luotettu koneoppiminen

Tämä opas selittää GPU:iden käytön perusteet CSC:n supertietokoneissa. Se on osa
[Machine learning guide](ml-guide.md) -opastamme.


## Puhti, Mahti vai LUMI? {#puhti-mahti-or-lumi}

Puhti ja Mahti ovat CSC:n kaksi kansallista supertietokonetta. Puhtissa on
enemmän GPU:ita (NVIDIA V100) ja laajin valikoima asennettua ohjelmistoa, kun
taas Mahti sisältää pienemmän määrän nopeampia uuden sukupolven NVIDIA A100
GPU:ita. CSC:n isännöimä Eurooppalainen supertietokone
[LUMI](https://docs.lumi-supercomputer.eu/hardware/) tarjoaa valtavan GPU-
resurssin, joka perustuu AMD GPU:ihin.

Pääasialliset GPU-aiheiset tilastot on kerätty alla olevaan taulukkoon.

|       | GPU-tyyppi         | GPU-muisti | GPU-solmut | GPU:ta/solmu | Yhteensä GPU:ta |
|-------|--------------------|------------|------------|--------------|-----------------|
| Puhti | NVIDIA Volta V100  | 32 GB      | 80         | 4            | 320             |
| Mahti | NVIDIA Ampere A100 | 40 GB      | 24         | 4            | 96              |
| LUMI  | AMD MI250x         | 64 (128) GB| 2978       | 8 (4)        | 23824 (11912)   |

!!! info "Huomio"

    Jokaisessa LUMI-solmussa on 4 MI250x GPU:ta, mutta Slurmin
    kautta saatavilla on 8 GPU:ta, koska MI250x kortissa on 2 GPU-sirua
    (GCD). Taulukko näyttää GPU-siruun liittyvät numerot, MI250x korttinumerot
    on merkitty suluilla.

Lue [GPU-solmujen käyttöpolitiikkamme](../../computing/usage-policy.md#gpu-nodes).
Huomioi myös, että eri supertietokoneiden välillä on erilaisia jonotustilanteita. 
Ota siis huomioon kaikki vaihtoehdot. Esimerkiksi LUMI:ssa on paljon GPU:ita, 
ja jonotusajat ovat lyhyitä (kesällä 2023).

Huomaa, että kaikissa supertietokoneissa on erilliset tiedostojärjestelmät, 
joten sinun on kopioitava tiedostosi manuaalisesti, jos haluat vaihtaa järjestelmää. 
***Jos et ole varma, mitä supertietokonetta käyttää, Puhti on hyvä oletus***, 
koska siinä on laajempi ohjelmistotuki.

## Saatavilla oleva koneoppimisohjelmisto {#available-machine-learning-software}

Tuemme [useita
sovelluksia](../../apps/by_discipline.md#data-analytics-and-machine-learning)
GPU-luotetulle koneoppimiselle CSC:n supertietokoneissa, mukaan lukien [TensorFlow](../../apps/tensorflow.md)
ja [PyTorch](../../apps/pytorch.md). Lue tarkemmat ohjeet haluamasi sovelluksen
kohdalla.

Sinun on käytettävä [moduulijärjestelmää](../../computing/modules.md) ladataksesi
haluamasi sovellus, esimerkiksi:

```bash
module load tensorflow/2.12
```

Huomioithan, että moduuleihimme sisältyvät jo CUDA- ja cuDNN-kirjastot, joten 
cuda- ja cudnn-moduuleita ei tarvitse ladata erikseen!

LUMI:ssa sinun on ensin otettava käyttöön CSC:n asennusten moduulivarasto:

```bash
module use /appl/local/csc/modulefiles/
```

Lopuksi, Puhtissa tarjoamme joitakin erityissovelluksia, jotka eivät oletuksena 
näy moduulijärjestelmässä. Nämä on otettu käyttöön käyttäjien pyynnöstä, mutta niillä
on rajallinen tuki. Ne voidaan ottaa käyttöön suorittamalla:

```bash
module use /appl/soft/ai/singularity/modulefiles/
```

### Oman ohjelmiston asentaminen {#installing-your-own-software}

Monissa tapauksissa olemassa olevat moduulit tarjoavat tarvittavan kehyksen, mutta 
jotkut paketit puuttuvat. Tässä tapauksessa voit usein ladata oikean moduulin ja 
sitten [asentaa lisäpaketteja henkilökohtaiseen käyttöön `pip`-paketinhallinnan avulla](./python-usage-guide.md#installing-python-packages-to-existing-modules).

Monimutkaisempia ohjelmistovaatimuksia varten suosittelemme käyttämään 
[tykkyä](../../computing/containers/tykky.md) tai [luomaan oman
Apptainer-kontin](../../computing/containers/creating.md).


## GPU-tehtävien suorittaminen {#running-gpu-jobs}

Lähettääksesi GPU-tehtävän Slurm-työkuorman hallintaan, sinun on käytettävä
`gpu`-osuutta Puhtissa tai `gpusmall` tai `gpumedium` osuutta Mahtissa, ja määritä
tarvittavien GPU:iden tyyppi ja määrä `--gres`-lipulla.

LUMI:ssa sinun on käytettävä yksi GPU-osuuksista, kuten `dev-g`,
`small-g` tai `standard-g`.

Alla on esimerkki eräskripteistä yhden GPU:n ja vastaavan määrän CPU-ytimiä 
ja muistia varaamiseen yhdellä solmulla:

=== "Puhti"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=64G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:1
        
    srun python3 myprog.py <options>
    ```

=== "Mahti"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpusmall
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=32
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:1
    
    srun python3 myprog.py <options>
    ```

=== "LUMI"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=7
    #SBATCH --gpus-per-node=1
    #SBATCH --mem=60G
    #SBATCH --time=1:00:00
    
    srun python3 myprog.py <options>
    ```

Mahtin `gpusmall`-osuus tukee vain tehtäviä 1-2 GPU:lla. Jos tarvitset 
lisää GPU:ita, käytä `gpumedium`-jonoa. Voit lukea lisää 
[moni-GPU ja moni-solmu-tehtävistä opastamme](ml-multi.md).

Lisätietoja eri osuuksista löytyy sivuiltamme
[saatavilla olevista erätehtäväosuuksista CSC:n supertietokoneilla](../../computing/running/batch-job-partitions.md) ja [Slurm- osuudet LUMI:ssa](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/).

## GPU-käyttöaste {#gpu-utilization}

GPU:t ovat erittäin kallis resurssi verrattuna suorittimiin, joten 
GPU:ita tulisi hyödyntää mahdollisimman paljon, kun ne on varattu. Tarjoamme 
jotakin työkaluja suorittamaan GPU-työkuorman
seuraamiseksi eri supertietokoneissa. GPU-käyttöasteen tulisi 
ihanteellisesti olla lähellä 100%. Jos käyttöasteesi on jatkuvasti alhainen 
(esimerkiksi alle 50%) se voi johtua useista syistä:

- Sinulla saattaa olla pullonkaula prosessoinnissa, esimerkiksi sinun pitäisi
  käyttää tiedon latauskehystä (ja varata tarpeeksi CPU-ytimiä siihen)
  voidaksesi syöttää GPU:lle tietoa tarpeeksi nopeasti. [Katso
  dokumentaatiomme moniytimisten CPU:iden käytöstä tiedon
  esikäsittelyyn](#using-multiple-cpus-for-data-pre-processing).

- Vaihtoehtoisesti voi yksinkertaisesti olla, että laskentaongelma 
  on "liian pieni" GPU:lle, esimerkiksi jos
  hermoverkko on suhteellisen yksinkertainen. Tämä ei ole ongelma sinänsä, mutta 
  jos käyttöasteesi on todella alhainen, voit harkita, olisiko CPU:iden käyttäminen
  kustannustehokkaampi ratkaisu.

Kuten aina, älä epäröi [ottaa yhteyttä palvelupisteeseemme](../contact.md)
jos sinulla on kysymyksiä koskien GPU-käyttöä.

### Työkalut GPU-käyttäytymisen seurantaan {#tools-for-monitoring-gpu-utilization}

#### `seff`-komento suoritetulle työlle (Puhti ja Mahti) {#seff-command-for-a-completed-job}

Helpoin tapa tarkistaa suoritetun työn GPU-käyttöaste on
`seff`-komento:

```bash
seff <job_id>
```

Tässä esimerkissä voimme nähdä, että maksimi käyttöaste on 100%, mutta
keskimääräinen on 92% (tämä on hyvä taso):

```
GPU load 
     Hostname        GPU Id      Mean (%)    stdDev (%)       Max (%) 
       r01g07             0         92.18         19.48           100 
------------------------------------------------------------------------
GPU memory 
     Hostname        GPU Id    Mean (GiB)  stdDev (GiB)     Max (GiB) 
       r01g07             0         16.72          1.74         16.91 
```

#### `nvidia-smi` käynnissä olevalle työlle (Puhti ja Mahti) {#nvidia-smi-for-a-running-job}

Kun työ on käynnissä voit suorittaa `nvidia-smi`-komennon `ssh`:n 
kautta solmulla, jossa se on käynnissä. Näet solmun isäntänimen 
`squeue --me`-komennolla. Tuloste voi näyttää tältä:

```
   JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
17273947       gpu puhti-gp mvsjober  R       0:07      1 r01g06
```

Näet solmun isäntänimen `NODELIST`-sarakkeesta, tässä tapauksessa se on
`r01g06`. Voit nyt tarkistaa GPU-käytön seuraavasti
(korvaa `<nodename>` oikealla solmun isäntänimelläsi):

```bash
ssh <nodename> nvidia-smi
```

Tuloste näyttää tältä:

```
Wed Jun 14 09:53:11 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 515.105.01   Driver Version: 515.105.01   CUDA Version: 11.7     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  On   | 00000000:89:00.0 Off |                    0 |
| N/A   57C    P0   232W / 300W |   5222MiB / 32768MiB |    100%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A   2312753      C   /appl/soft/ai/bin/python3        5219MiB |
+-----------------------------------------------------------------------------+
```

Tästä näemme, että prosessimme käyttää noin 5GB (32GB:sta) GPU-muistista, ja nykyinen
GPU-käyttöaste on 100% (mikä on erittäin hyvä).

Jos haluat jatkuvasti päivittyvän näkymän:

```bash
ssh r01g06 -t watch nvidia-smi
```

Tämä päivittyy joka toinen sekunti, poistu painamalla Ctrl-C.

#### `rocm-smi` käynnissä olevalle työlle (LUMI) {#rocm-smi-for-a-running-job}

LUMI:ssä käytetään AMD GPU:ita, joten komento on hieman
eri: `rocm-smi`. [LUMI:ssä sinun on käytettävä `srun`-komentoa kirjautuaksesi solmuun, jossa sinulla on käynnissä oleva työ](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/interactive/#using-srun-to-check-running-jobs):

```bash
srun --interactive --pty --jobid=<jobid> rocm-smi
```

Korvaa `<jobid>` oikealla Slurm tehtävän tunnuksella. Voit myös käyttää 
`watch rocm-smi` saadaksesi jatkuvasti päivittyvän näkymän.

   
### Usean CPU:n käyttäminen datan esikäsittelyyn {#using-multiple-cpus-for-data-pre-processing}

Yksi yleinen syy GPU-käytön alhaisuuteen on silloin, kun
CPU ei voi ladata ja esikäsitellä tietoja tarpeeksi nopeasti, ja GPU:n on
odotettava seuraavaa erää käsiteltäväksi. On tällöin yleistä
käytäntöä varata enemmän CPU:ita suorittamaan tietojen lataus ja
esikäsittely useissa rinnakkaisissa säikeissä tai prosesseissa. Hyvä nyrkkisääntö 
Puhtissa on **varata 10 CPU:ta per GPU** (koska jokaisessa solmussa on 4 GPU:ta 
ja 40 CPU:ta). Mahtissa voit varata enintään 32 ydintä, sillä se
vastaa 1/4 solmusta. LUMI:ssa suosittelemme varaamaan 7 CPU-ydintä, koska 
siellä on 63 ydintä 8 GPU:lle. **Muista, että CPU:t ovat paljon halvempia 
resursseja kuin GPU!**

Saatat huomata, että olemme jo noudattaneet tätä neuvoa esimerkissämme
työskriptit:

```bash
#SBATCH --cpus-per-task=10
```

Ohjelmakoodisi on myös
tuettava esikäsittelyä usealla säikeellä.
Useimmat korkean tason koneoppimiskehykset tukevat tätä valmiiksi. Esimerkiksi
[TensorFlow:ssä voit käyttää `tf.data`](https://www.tensorflow.org/guide/data) ja asettaa `num_parallel_calls`
CPU:iden määrälle ja hyödyntää `prefetch`:

```python
dataset = dataset.map(..., num_parallel_calls=10)
dataset = dataset.prefetch(buffer_size)
```

[PyTorch:ssa voit käyttää
`torch.utils.DataLoader`](https://pytorch.org/docs/stable/data.html), 
joka tukee tietojen lataamista useilla prosesseilla:

```python
train_loader = torch.utils.data.DataLoader(..., num_workers=10)
```

Jos käytät useita tietolatureita, mutta datan lataus on edelleen hidasta, 
on myös mahdollista, että käytät jaettua tiedostojärjestelmää 
tehottomasti. Yleinen virhe on lukea valtava määrä pieniä tiedostoja. 
Voit lukea lisää [miten tallentaa ja ladata tietoja 
tehokkaimmin koneoppimiseen erillisestä opastamme](ml-data.md).

### Profilointityökalut {#profilers}

[TensorFlow Profiler](https://www.tensorflow.org/guide/profiler) ja
[PyTorch
Profiler](https://pytorch.org/tutorials/intermediate/tensorboard_profiler_tutorial.html)
ovat saatavilla TensorBoard-liitännäisinä. Profiilit löytyvät 
*PROFILE* ja *PYTORCH_PROFILER* välilehdillä TensorBoardissa,
vastaavasti. Huomaa, että välilehdet eivät välttämättä ole
näkyvissä oletuksena, mutta ne löytyvät pudotusvalikosta
käyttöliittymän oikeasta yläkulmasta. Profiilityökalut voidaan
käyttää tunnistamaan resurssien kulutusta ja ratkomaan
suorituskykyongelmia, erityisesti tiedonsyöttöputken osalta.

Katso myös:

- [Kuinka käynnistää TensorBoard käyttäen Puhdin verkkokäyttöliittymää](../../computing/webinterface/apps.md)
- [PyTorch profiler -opastus](../../apps/pytorch.md#pytorch-profiler)

## GPU-energiankulutus {#gpu-energy-usage}

Ekologisista ja taloudellisista syistä on usein tarpeellista seurata
koneoppimistehtävien energiankulutusta. Yksittäisen tehtävän, mukaan
lukien CPU- ja GPU-prosessointi, verkkoyhteydet ja jäähdytys, 
kokonaisenergiankulutuksen mittaaminen on melko vaikeaa
yleisesti, koska ne resurssit jaetaan monen tehtävän kesken ja
voivat riippua useista tekijöistä, jotka eivät liity
seurattavaan työhön. Onneksi vain GPU-iden energiankulutuksen
mittaaminen on helpompaa, koska niitä ei yleensä jaeta
monen tehtävän kesken. Koska GPU on ylivoimaisesti suurin
energiankuluttaja, se antaa hyvän arvion kokonaisenergiankulutuksesta.

### Työkalut GPU-energiankulutuksen seuraamiseen {#tools-for-monitoring-gpu-energy-usage}

#### `seff`-komento suoritetulle työlle (Puhti ja Mahti) {#seff-command-for-a-completed-job}

Puhti- ja Mahti-järjestelmissä voit käyttää `seff` työkalua
suoritetulle työlle:

```bash
seff <job_id>
```

Huomaa, että GPU-energiankulutus lasketaan vain työn
suorituksen jälkeen, joten ajon aikana ei tulosteta
välivaiheita.

Esimerkki tulosteesta, jossa olemme käyttäneet yhtä solmua neljällä
GPU:lla:

```
GPU energy
      Hostname        GPU Id   Energy (Wh)
        r01g01             0         58.30
        r01g01             1         56.63
        r01g01             2         44.87
        r01g01             3         62.21
```

### `gpu-energy`-työkalu (LUMI) {#gpu-energy-tool}

LUMI:lla ei ole `seff`-komentoa, mutta siellä on kokeellinen
työkalu, jota voidaan käyttää lukemaan AMD GPU-kortin
löytymät energiankulutusmittarit. Työkalu ja dokumentointi
löytyvät täältä: <https://github.com/mvsjober/gpu-energy-amd>.

Se on esiasennettu LUMI-järjestelmään
polkuun `/appl/local/csc/soft/ai/bin/gpu-energy`.

Tyypillinen käyttö Slurm-skriptissä:

```
gpu-energy --save

# suoritettavan tehtävän koodi tähän

gpu-energy --diff
```

Esimerkki tulosteesta:

```
GPU 0: 46.64 Wh, avg power: 377.81 W (444.43 s)
GPU 2: 46.47 Wh, avg power: 376.46 W (444.43 s)
GPU 4: 46.18 Wh, avg power: 374.04 W (444.43 s)
GPU 6: 46.62 Wh, avg power: 377.62 W (444.43 s)
TOTAL: 185.91 Wh
```

Huomaa, että se tulostaa energian vain parillisilla GCD-numeroilla, 
sillä AMD GPU-energiankulutusmittari antaa yhden luvun koko MI250x-kortille.

!!! warning "Mittaa aina GPU:n käyttö täyden solmun ajan LUMI:ssa!"

    GPU-energian mittaaminen LUMI:ssa on tehtävä täydellä solmulla, jotta tulokset
    saadaan tarkkoina. Syynä on, että MI250x GPU:ssa on 2 GPU-sirua
    (GCD), mutta energiankulutusmittari antaa yhden luvun koko
    MI250x:lle. Jos varaat yhden GCD:n, toinen ajo saattaa käyttää
    toista GCD:ta. Varaamalla 2 GCD:tä ei voida taata, että saat ne
    samalta kortilta.

Katso [README.md-tiedostosta lisäkäyttöesimerkkejä](https://github.com/mvsjober/gpu-energy-amd/blob/master/README.md).
