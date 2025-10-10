---
title: GPU-accelerated machine learning
title_fi: GPU-kiihdytetty koneoppiminen
---

# GPU-kiihdytetty koneoppiminen { #gpu-accelerated-machine-learning }

Tässä oppaassa käydään läpi GPU:iden käytön perusteet CSC:n supertietokoneissa. Tämä on osa [koneoppimisopastamme](ml-guide.md).


## Puhti, Mahti vai LUMI? { #puhti-mahti-or-lumi }

Puhti ja Mahti ovat CSC:n kaksi kansallista supertietokonetta. Näistä Puhtissa
on enemmän GPU:ita (NVIDIA V100) ja laajin valikoima valmiiksi asennettuja
ohjelmistoja, kun taas Mahtissa on vähemmän mutta uudemman sukupolven ja
nopeampia NVIDIA A100 -GPU:ita. CSC:n isännöimä eurooppalainen supertietokone
[LUMI](https://docs.lumi-supercomputer.eu/hardware/) tarjoaa valtavan GPU-resurssin
AMD:n GPU:iden pohjalta.

Tärkeimmät GPU:ihin liittyvät tiedot on koottu alla olevaan taulukkoon.

|       | GPU-tyyppi         | GPU-muisti  | GPU-solmut | GPU:ta/solmu | GPU:ta yhteensä |
|-------|--------------------|-------------|------------|--------------|-----------------|
| Puhti | NVIDIA Volta V100  | 32 GB       | 80         | 4            | 320             |
| Mahti | NVIDIA Ampere A100 | 40 GB       | 24         | 4            | 96              |
| LUMI  | AMD MI250x         | 64 (128) GB | 2978       | 8 (4)        | 23824 (11912)   |

!!! info "Huom."
    Jokaisessa LUMI-solmussa on 4 MI250x-GPU:ta, mutta Slurmin kautta näkyy 8
    GPU:ta, koska MI250x-kortissa on 2 GPU-sirua (GCD). Taulukossa on esitetty
    GCD-kohtaiset luvut; MI250x-korttikohtaiset luvut on esitetty
    sulkeissa.

Lue [GPU-solmujen käyttöpolitiikka](../../computing/usage-policy.md#gpu-nodes).
Huomioi myös, että Slurmin jonotilanne voi vaihdella eri aikoina eri
supertietokoneilla, joten vaihtoehtoja kannattaa vertailla. Esimerkiksi LUMIssa
on erittäin paljon GPU:ita saatavilla ja jonotusajat ovat hyvin lyhyitä
(tilanne kesällä 2023).

Huomaa, että jokaisella supertietokoneella on oma erillinen tiedostojärjestelmä,
joten jos vaihdat järjestelmää, sinun on kopioitava tiedostot manuaalisesti.
**Jos olet epävarma, mitä supertietokonetta käyttää, Puhti on hyvä oletusvalinta,**
koska sen ohjelmistotuki on laajempi.


## Saatavilla oleva koneoppimisohjelmisto { #available-machine-learning-software }

Tuemme [useita sovelluksia](../../apps/by_discipline.md#data-analytics-and-machine-learning)
GPU-kiihdytettyä koneoppimista varten CSC:n supertietokoneilla, mukaan lukien
[TensorFlow](../../apps/tensorflow.md) ja [PyTorch](../../apps/pytorch.md).
Lue tarkemmat ohjeet sinua kiinnostavasta sovelluksesta.

Sovelluksen lataamiseen tulee käyttää [moduulijärjestelmää](../../computing/modules.md),
esimerkiksi:

```bash
module load tensorflow/2.12
```

Huomaa, että moduuleihimme sisältyvät jo CUDA- ja cuDNN-kirjastot, joten erillisiä
cuda- ja cudnn-moduuleja ei tarvitse ladata!

LUMIssa sinun täytyy ensin ottaa käyttöön CSC:n asennusten moduulivarasto:

```bash
module use /appl/local/csc/modulefiles/
```

Puhtissa tarjoamme lisäksi joitakin erikoissovelluksia, jotka eivät näy oletuksena
moduulijärjestelmässä. Nämä on tuotu saataville käyttäjäpyyntöjen perusteella,
mutta niille on rajallinen tuki. Saat ne näkyviin komennolla:

```bash
module use /appl/soft/ai/singularity/modulefiles/
```

### Oman ohjelmiston asentaminen { #installing-your-own-software }

Monissa tapauksissa olemassa olevat moduulimme tarjoavat tarvittavan alustan,
mutta joitakin paketteja voi puuttua. Tällöin voit usein ladata sopivan moduulin
ja sen jälkeen [asentaa lisäpaketteja omaan käyttöön `pip`-paketinhallinnalla](./python-usage-guide.md#installing-python-packages-to-existing-modules).

Monimutkaisemmissa tarpeissa suosittelemme käyttämään
[tykkyä](../../computing/containers/tykky.md) tai [luomaan oman
Apptainer-kontin](../../computing/containers/overview.md#building-container-images).


## GPU-ajojen suorittaminen { #running-gpu-jobs }

GPU-ajon lähettämiseksi Slurm-työnhallintaan käytä Puhtissa `gpu`-osiota tai
Mahtissa `gpusmall`- tai `gpumedium`-osiota, ja määritä tarvittava GPU-tyyppi
ja -määrä `--gres`-lipulla.

LUMIssa tulee käyttää jotakin GPU-osioista, kuten `dev-g`, `small-g` tai `standard-g`.

Alla on esimerkkieräajotiedostot, jotka varaavat yhden GPU:n sekä vastaavan
osuuden solmun CPU-ytimistä ja muistista:

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

Mahtin `gpusmall`-osio tukee vain 1–2 GPU:n ajoja. Jos tarvitset enemmän
GPU:ita, käytä `gpumedium`-osiota. Voit lukea lisää [usean GPU:n ja usean solmun
ajoista erillisestä oppaastamme](ml-multi.md).

Lisätietoja eri osioista löydät sivuilta
[CSC:n supertietokoneiden eräajo-osiot](../../computing/running/batch-job-partitions.md)
sekä [Slurmin osiot LUMIssa](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/).

## GPU:n hyödyntäminen { #gpu-utilization }

GPU:t ovat verrattain kalliita resursseja CPU:ihin nähden, joten ne tulisi
hyödyntää mahdollisimman tehokkaasti, kun ne on varattu. Tarjoamme työkaluja
GPU-ajojen hyödyntämisen seurantaan eri supertietokoneilla. Ihannetilanteessa
GPU:n käyttöaste on lähellä 100 %. Jos käyttöaste on jatkuvasti matala
(esimerkiksi alle 50 %), syitä voi olla useita:

- Prosessoinnissa voi olla pullonkaula. Esimerkiksi datan lataamiseen kannattaa
  käyttää tarkoitukseen tehtyä kehystä (ja varata siihen riittävästi CPU-ytimiä),
  jotta GPU saa dataa tarpeeksi nopeasti. [Katso ohjeemme usean CPU-ytimen
  käyttämisestä datan lataukseen](#using-multiple-cpus-for-data-pre-processing).
  
- Vaihtoehtoisesti ongelma voi yksinkertaisesti olla GPU:lle ”liian pieni”,
  esimerkiksi jos neuroverkko on melko yksinkertainen. Tämä ei sinänsä ole
  ongelma, mutta jos käyttöaste on todella matala, harkitse, olisiko CPU:iden
  käyttö kustannustehokkaampaa.

Kuten aina, ota rohkeasti [yhteyttä palvelupisteeseemme](../contact.md), jos sinulla
on kysyttävää GPU:n hyödyntämisestä.

### Työkalut GPU:n hyödyntämisen seurantaan { #tools-for-monitoring-gpu-utilization }

#### `seff`-komento valmistuneelle ajolle (Puhti ja Mahti) { #seff-command-for-a-completed-job-puhti-and-mahti }

Helpoin tapa tarkistaa valmistuneen ajon GPU:n käyttöaste on `seff`-komento:

```bash
seff <job_id>
```

Tässä esimerkissä nähdään, että enimmäiskäyttöaste on 100 %, mutta keskiarvo on
92 % (tämä on hyvä taso):

```
GPU load 
     Hostname        GPU Id      Mean (%)    stdDev (%)       Max (%) 
       r01g07             0         92.18         19.48           100 
------------------------------------------------------------------------
GPU memory 
     Hostname        GPU Id    Mean (GiB)  stdDev (GiB)     Max (GiB) 
       r01g07             0         16.72          1.74         16.91 
```

#### `nvidia-smi` käynnissä olevalle ajolle (Puhti ja Mahti) { #nvidia-smi-for-a-running-job-puhti-and-mahti }

Kun ajo on käynnissä, voit suorittaa `nvidia-smi`-komennon `ssh`:n kautta
solmussa, jossa ajo pyörii. Solmun nimen näet komennolla `squeue --me`.
Tuloste voi näyttää esimerkiksi tältä:

```
   JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
17273947       gpu puhti-gp mvsjober  R       0:07      1 r01g06
```

Solmun nimen näet sarakkeesta `NODELIST`; tässä tapauksessa se on `r01g06`.
Voit nyt tarkistaa GPU:n käyttöasteen komennolla (korvaa `<nodename>` omalla
solmun nimelläsi):

```bash
ssh <nodename> nvidia-smi
```

Tuloste näyttää suunnilleen tältä:

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

Tästä nähdään, että prosessi käyttää noin 5 Gt (32 Gt:sta) GPU-muistia ja
tämänhetkinen GPU:n käyttöaste on 100 % (mikä on erittäin hyvä).

Jos haluat jatkuvasti päivittyvän näkymän:

```bash
ssh r01g06 -t watch nvidia-smi
```

Tämä päivittyy 2 sekunnin välein; poistu painamalla Ctrl-C.

#### `rocm-smi` käynnissä olevalle ajolle (LUMI) { #rocm-smi-for-a-running-job-lumi }

LUMI käyttää AMD:n GPU:ita, joten komento on hieman erilainen: `rocm-smi`.
[LUMIssa sinun tulee käyttää `srun`-komentoa kirjautuaksesi solmuun, jossa ajosi on käynnissä](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/interactive/#using-srun-to-check-running-jobs):

```bash
srun --interactive --pty --jobid=<jobid> rocm-smi
```

Korvaa `<jobid>` oikealla Slurm-työn tunnisteella. Voit käyttää myös
`watch rocm-smi` -komentoa jatkuvasti päivittyvään näkymään.

### Usean CPU-ytimen käyttäminen datan esikäsittelyyn { #using-multiple-cpus-for-data-pre-processing }

Yksi yleinen syy matalaan GPU:n käyttöasteeseen on se, että CPU ei ehdi ladata ja
esikäsitellä dataa tarpeeksi nopeasti, jolloin GPU joutuu odottamaan seuraavaa
erää. Tällöin on tavallista varata enemmän CPU-resursseja datan lataamiseen ja
esikäsittelyyn useassa rinnakkaisessa säikeessä tai prosessissa. Hyvä nyrkkisääntö
Puhtissa on **varata 10 CPU:ta per GPU** (koska solmussa on 4 GPU:ta ja 40 CPU:ta).
Mahtissa voit varata enintään 32 ydintä, mikä vastaa 1/4 solmusta. LUMIssa
suosittelemme käyttämään 7 CPU-ydintä, sillä 63 ydintä jakautuu 8 GPU:lle.
**Muista, että CPU:t ovat paljon halvempia resursseja kuin GPU:t!**

Olet ehkä huomannut, että noudatimme tätä ohjetta jo esimerkkiajoissamme:

```bash
#SBATCH --cpus-per-task=10
```

Myös koodisi on tuettava rinnakkaista esikäsittelyä. Useimmat korkean tason
koneoppimiskehykset tukevat tätä valmiiksi. Esimerkiksi
[TensorFlow’ssa voit käyttää `tf.data`](https://www.tensorflow.org/guide/data)
ja asettaa `num_parallel_calls` varattujen CPU:iden määräksi sekä käyttää `prefetch`-ominaisuutta:

```python
dataset = dataset.map(..., num_parallel_calls=10)
dataset = dataset.prefetch(buffer_size)
```

[PyTorchissa voit käyttää
`torch.utils.DataLoader`ia](https://pytorch.org/docs/stable/data.html),
joka tukee datan latausta usealla prosessilla:

```python
train_loader = torch.utils.data.DataLoader(..., num_workers=10)
```

Jos käytät useita datalataajia ja lataus on silti hidasta, on mahdollista, että
jaettua tiedostojärjestelmää käytetään tehottomasti. Yleinen virhe on lukea
valtava määrä pieniä tiedostoja. Lue lisää siitä, [miten data kannattaa tallentaa
ja ladata koneoppimista varten erillisessä oppaassamme](ml-data.md).

### Profilointityökalut { #profilers }

[TensorFlow Profiler](https://www.tensorflow.org/guide/profiler) ja
[PyTorch Profiler](https://pytorch.org/tutorials/intermediate/tensorboard_profiler_tutorial.html)
ovat saatavilla TensorBoard-lisäosina. Ne löytyvät TensorBoardin välilehdiltä
PROFILE ja PYTORCH_PROFILER. Huomaa, että välilehdet eivät välttämättä ole
näkyvissä oletuksena, mutta ne löytyvät käyttöliittymän oikean reunan
pudotusvalikosta. Profilointityökaluilla voidaan tunnistaa resurssien käyttöä ja
ratkoa suorituskyvyn pullonkauloja, erityisesti datan syöttöputkessa.

Katso myös:

- [TensorBoardin käynnistäminen Puhtin selainkäyttöliittymästä](../../computing/webinterface/apps.md)
- [PyTorchin profiler-opas](../../apps/pytorch.md#pytorch-profiler)

## GPU-energian kulutus { #gpu-energy-usage }

Ekologisista ja taloudellisista syistä koneoppimisajojen energiankulutusta on
usein tarpeen seurata. Yksittäisen ajon kokonaisenergiankulutuksen (CPU- ja
GPU-laskenta, verkotus ja jäähdytys) mittaaminen on yleisesti ottaen hankalaa,
koska resursseja jaetaan monien ajojen kesken ja ne riippuvat monista ajosta
riippumattomista tekijöistä. Onneksi pelkkien GPU:iden energiankulutuksen
mittaaminen on helpompaa, koska niitä ei tyypillisesti jaeta monien ajojen
kesken. Koska GPU on selvästi suurin energiankuluttaja, se antaa hyvän
likiarvon kokonaiskulutuksesta.

### Työkalut GPU-energian kulutuksen seurantaan { #tools-for-monitoring-gpu-energy-usage }

#### `seff`-komento valmistuneelle ajolle (Puhti ja Mahti) { #seff-command-for-a-completed-job-puhti-and-mahti }

Puhtissa ja Mahtissa voit käyttää `seff`-työkalua valmistuneelle ajolle:

```bash
seff <job_id>
```

Huomaa, että GPU-energian kulutus lasketaan vasta ajon päätyttyä, joten
käynnissä olevalle ajolle ei tulosteta väliaikatietoja.

Esimerkkituloste, jossa on käytetty yhtä solmua ja 4 GPU:ta:

```
GPU energy
      Hostname        GPU Id   Energy (Wh)
        r01g01             0         58.30
        r01g01             1         56.63
        r01g01             2         44.87
        r01g01             3         62.21
```

### `gpu-energy`-työkalu (LUMI) { #gpu-energy-tool-lumi }

LUMIssa ei ole `seff`-komentoa, mutta käytettävissä on alustava työkalu, jolla
voi lukea AMD:n GPU-kortin energiarekisterit. Työkalu ja sen dokumentaatio löytyvät täältä:
<https://github.com/mvsjober/gpu-energy-amd>.

Se on esiasennettu LUMIssa polkuun `/appl/local/csc/soft/ai/bin/gpu-energy`.

Tyypillinen käyttö Slurm-skriptissä:

```
gpu-energy --save

# run job here

gpu-energy --diff
```

Esimerkkituloste:

```
GPU 0: 46.64 Wh, avg power: 377.81 W (444.43 s)
GPU 2: 46.47 Wh, avg power: 376.46 W (444.43 s)
GPU 4: 46.18 Wh, avg power: 374.04 W (444.43 s)
GPU 6: 46.62 Wh, avg power: 377.62 W (444.43 s)
TOTAL: 185.91 Wh
```

Huomaa, että energia tulostetaan vain parillisille GCD:ille. Tämä johtuu siitä,
että AMD:n GPU-energiamittari tuottaa vain yhden arvon koko MI250x-kortille.

!!! warning "Mittaa GPU-energian kulutus aina täydellä LUMI-solmulla!"
    GPU-energian mittaus LUMIssa on tehtävä täydellä solmulla, jotta tulokset
    ovat tarkkoja. Syy on se, että MI250x-GPU:ssa on 2 GPU-sirua (GCD),
    mutta energiamittari antaa yhden arvon koko MI250x-kortille. Jos varaat
    vain yhden GCD:n, toinen ajo voi käyttää toista GCD:tä. Vaikka varaisit
    2 GCD:tä, ei voida taata, että ne ovat samalta kortilta.

Katso myös [README.md-tiedosto lisäkäyttöesimerkkejä varten](https://github.com/mvsjober/gpu-energy-amd/blob/master/README.md).