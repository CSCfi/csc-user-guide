# Multi-GPU ja monisolmuinen koneoppiminen {#multi-gpu-ja-monisolmuinen-koneoppiminen}

Tämä opas selittää, miten hyödyntää useita GPU:ita ja useita solmuja koneoppimissovelluksissa CSC:n supertietokoneilla. Se on osa meidän [koneoppimisopasta](ml-guide.md).

Ensiksi selitämme yleiset periaatteet, kuten yksi- ja monisolmuiset työt sekä mekanismit monien prosessien suorittamiseen. Sen jälkeen käsittelemme joitakin yleisiä ohjelmistokehityksen ympäristöjä ja miten niitä käytetään CSC:n supertietokoneilla: [PyTorch DDP:n](#pytorch-ddp), [DeepSpeedin](#deepspeed) sekä lyhyesti [Horovodin](#horovod) ja [TensorFlow'n
`tf.distribute.Strategy`](#tensorflows-tfdistributestrategy).

## Solmut ja tehtävät {#nodes-and-tasks}

### GPU-solmut {#gpu-nodes}

Jokaisella erillisellä GPU-solmulla (eli klusterin yksittäisellä tietokoneella) on kiinteä määrä GPU:ita. Puhtissa ja Mahtissa on 4 GPU:ta solmua kohden, ja LUMIssa 8 GPU:ta solmua kohden. (Teknisesti LUMI-solmulla on 4 GPU-korttia, mutta 8 GPU-piirilevyä.) Koko supertietokoneella voi olla kymmeniä tai jopa tuhansia GPU-solmuja. Katso [GPU:lla kiihdytetty koneoppiminen](gpu-ml.md) lisätietoja varten, erityisesti taulukko, joka kuvaa eri GPU:ida CSC:n eri supertietokoneissa, saattaa olla mielenkiintoinen.

Jos tarvitset 1-4 GPU:ta (tai 1-8 LUMIssa), sinun tulisi aina varata **yksisolmuinen työ**. Jos tarvitset yli 4 GPU:ta (tai 8 LUMIssa), sinun pitää varata **monisolmuinen työ**. Vaikka on teknisesti mahdollista varata, esim. kaksi GPU:ta yhdestä solmusta ja kaksi toista solmusta, tätä ei suositella kuin testaustarkoituksiin, sillä kommunikointi solmujen välillä on aina hitaampaa kuin solmun sisällä.

### MPI-tehtävät {#mpi-tasks}

Kun rinnakkaistetaan useille GPU:ille, on yleistä allokoida erillinen CPU-prosessi jokaisen GPU:n kommunikointia varten. Tämä per-GPU-tehtävien jako voidaan hoitaa ohjelman itsensä toimesta, esimerkiksi käyttämällä [Pythonin multiprocessing-kirjastoa](https://docs.python.org/3/library/multiprocessing.html) erillisten prosessien suorittamiseen. Toinen tapa on käyttää Slurmin MPI-toiminnallisuutta suorittamaan **useita MPI-tehtäviä**. Se, käytetäänkö MPI-tehtäviä, riippuu usein käytetystä ohjelmistokehyksestä.

### Slurm-esimerkit {#slurm-examples}

Tässä osiossa annamme Slurm-eräskriptin esimerkkejä yksi- tai monisolmuisten töiden suorittamiseksi, MPI:lla tai ilman sitä.

!!! warning "Huomautus"
    
    Varmista, että koodisi tosiasiallisesti hyödyntää useita GPU:ita, sillä tämä vaatii yleensä joitakin muutoksia ohjelmaan. **Pelkkä useamman GPU:n varaaminen ei riitä!**

Voit [seurata, käyttääkö ohjelmasi kaikkia varattuja GPU:ita](gpu-ml.md#gpu-utilization) samoilla mekanismeilla, jotka on kuvattu GPU:lla kiihdytetyn koneoppimisoppassa. Ainoa ero on, että sinun pitäisi nyt nähdä useamman kuin yhden GPU:n tilastot.

#### Yksi solmua käyttävä ajo 2 GPU:lla, ei MPI {#single-node-run-using-2-gpus-no-mpi}

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=20
    #SBATCH --mem=160G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:2
        
    srun python3 myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpusmall
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=64
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:2
    
    srun python3 myprog.py <options>
    ```

    Huomaa, että Mahtissa `gpusmall`-osaston maksimimäärä on 2 GPU:ta. 3 tai 4 GPU:ta tai useampaa varten sinun täytyy käyttää `gpumedium`-osastoa.

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=14
    #SBATCH --gpus-per-node=2
    #SBATCH --mem=120G
    #SBATCH --time=1:00:00
    
    srun python3 myprog.py <options>
    ```

Yllä oleva esimerkki on helposti muutettavissa käyttämään enemmän kuin 2 GPU:ta muuttamalla `--gres`-asetus (Puhti ja Mahti) tai `--gpus-per-node`-asetus (LUMI) -parametrissa olevaa numeroa. Enimmäismäärä yksisolmuiselle työlle on 4 GPU:ta (Puhti ja Mahti) tai 8 GPU:ta (LUMI).

Jos lisäät GPU:iden määrää, saatat haluta myös lisätä varattujen CPU-ydinten lukumäärää ja muistimäärää. Esimerkeissämme olemme käyttäneet **nyrkkisääntöä varata CPU-ytimet ja muisti samassa suhteessa kuin GPU:iden määrä**.

Esimerkiksi Puhtissa on 4 GPU:ta, 40 CPU-ydintä ja 384 GB muistia solmua kohden. Jokaista GPU:ta kohden varaisimme näin ollen 10 CPU-ydintä ja noin 95 G muistia (muistille pyöristämme hieman alaspäin, koska yksiköt eivät ole niin tarkkoja).

[LUMI:ssa käytä enintään 7 CPU-ydintä ja 60 Gt/GPU](https://lumi-supercomputer.github.io/LUMI-training-materials/User-Updates/Update-202308/responsible-use/#core-and-memory-use-on-small-g-and-dev-g).

#### Yksi solmu käyttämällä kaikkia GPU:ita, käyttäen MPI {#single-node-using-all-gpus-using-mpi}

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=320G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    srun python3 myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=32
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    srun python3 myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=8
    #SBATCH --cpus-per-task=7
    #SBATCH --gpus-per-node=8
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00
    
    srun python3 myprog.py <options>
    ```

#### Monisolmu kahdella täydellä solmulla, ei MPI:tä {#multi-node-with-2-full-nodes-no-mpi}

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=320G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    srun python3 myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=128
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    srun python3 myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=56
    #SBATCH --gpus-per-node=8
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00
    
    srun python3 myprog.py <options>
    ```

Huomaa, että `--gres`-asetus määrittää aina yksisolmuisten *GPU:iden määrän*, jopa monisolmuskenaariossa. Joten jos varaamme 8 GPU:ta kahdelle solmulle Puhtissa, se tarkoittaa 4 GPU:ta jokaiselle solmulle, eli `--gres=gpu:v100:4`.

#### Monisolmu kahdella täydellä solmulla käyttäen MPI:tä {#multi-node-with-2-full-nodes-using-mpi}

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=320G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    srun python3 myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=32
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    srun python3 myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=8
    #SBATCH --cpus-per-task=7
    #SBATCH --gpus-per-node=8
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00
    
    srun python3 myprog.py <options>
    ```

## Saatavilla olevat kehykset {#available-frameworks}

On olemassa useita kehyksiä monigpu- ja monisolmuiseen koneoppimiseen. Jotkin kehykset ovat tiiviisti yhdistettyjä tiettyyn kehykseen, kuten PyTorchin `DistributedDataParallel`, DeepSpeed tai TensorFlow'n `tf.distribute.Strategy`, kun taas toiset ovat yleisempiä, kuten Horovod.

Riippumatta siitä, minkä kehyksen valitset, kiinnitä huomiota työn suorittamismenetelmään. Esimerkiksi Horovodia käytettäessä on yleistä käyttää MPI:tä, kun taas DeepSpeed voidaan konfiguroida käyttämään MPI:tä tai omaa rinnakkaismekanismiaan. Joissakin kehyksissä suoritusmekanismi voi myös vaihdella sen mukaan, onko kyseessä yksisolmuinen vai monisolmuinen työ.

Kaikkien kehysten tulisi käyttää
[NCCL:tä](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/overview.html)
(NVIDIA) tai [RCCL:ää](https://github.com/ROCmSoftwarePlatform/rccl) (AMD)
nopeaan GPU-laitteiden väliseen viestintään, vaikka MPI:tä käytettäisiinkin yhteyksien muodostamiseen.

### PyTorch DDP {#pytorch-ddp}

[PyTorch
distributed](https://pytorch.org/tutorials/beginner/dist_overview.html),
ja erityisesti `DistributedDataParallel` (DDP), tarjoaa mukavan tavan
suorittaa monigpu- ja monisolmuista PyTorch-työtä. Valitettavasti
PyTorch-dokumentaatio on ollut jossain määrin puutteellista tällä
alueella, ja verkosta löytyvät esimerkit voivat usein olla
vanhentuneita. Siksi, jotta DDP:n käyttö CSC:n supertietokoneilla
olisi helpompaa, olemme luoneet [joukon esimerkkejä, miten
suorittaa yksinkertaisia DDP-töitä klusterissa](https://github.com/CSCfi/pytorch-ddp-examples).
Esimerkeissä käytämme
[rendezvous](https://pytorch.org/docs/stable/elastic/rendezvous.html)
-mekanismia kommunikaation asettamiseen solmujen välille, ei MPI:tä.

Esimerkki Slurm-erätyöstä, jolla ajetaan PyTorch DDP:tä yhdellä
täydellä solmulla:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=320G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    module purge
    module load pytorch
    
    srun python3 -m torch.distributed.run --standalone --nnodes=1 --nproc_per_node=4 \
        myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=128
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    module purge
    module load pytorch

    srun python3 -m torch.distributed.run --standalone --nnodes=1 --nproc_per_node=4 \
        myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=56
    #SBATCH --gpus-per-node=8
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00
    
    module purge
    module use /appl/local/csc/modulefiles
    module load pytorch
    
    srun python3 -m torch.distributed.run --standalone --nnodes=1 --nproc_per_node=8 \
        myprog.py <options>
    ```

Esimerkki PyTorch DDP:n ajamisesta kahdella täydellä solmulla:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=320G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    export RDZV_HOST=$(hostname)
    export RDZV_PORT=29400
    
    module purge
    module load pytorch

    srun python3 -m torch.distributed.run \
        --nnodes=$SLURM_JOB_NUM_NODES \
        --nproc_per_node=4 \
        --rdzv_id=$SLURM_JOB_ID \
        --rdzv_backend=c10d \
        --rdzv_endpoint="$RDZV_HOST:$RDZV_PORT" \
        myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=128
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    export RDZV_HOST=$(hostname)
    export RDZV_PORT=29400
    
    module purge
    module load pytorch

    srun python3 -m torch.distributed.run \
        --nnodes=$SLURM_JOB_NUM_NODES \
        --nproc_per_node=4 \
        --rdzv_id=$SLURM_JOB_ID \
        --rdzv_backend=c10d \
        --rdzv_endpoint="$RDZV_HOST:$RDZV_PORT" \
        myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=56
    #SBATCH --gpus-per-node=8
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00
    
    export RDZV_HOST=$(hostname)
    export RDZV_PORT=29400
    
    module purge
    module use /appl/local/csc/modulefiles
    module load pytorch

    srun python3 -m torch.distributed.run \
        --nnodes=$SLURM_JOB_NUM_NODES \
        --nproc_per_node=8 \
        --rdzv_id=$SLURM_JOB_ID \
        --rdzv_backend=c10d \
        --rdzv_endpoint="$RDZV_HOST:$RDZV_PORT" \
        myprog.py <options>
    ```

Jos et käytä CSC:n kehittämää PyTorch-modulia LUMIssa, sinun täytyy ehkä asettaa ympäristömuuttuja `NCCL_SOCKET_IFNAME=hsn` ja muutamia muita asetuksia parhaan suorituskyvyn saamiseksi. Katso [PyTorch-esimerkki LUMI-dokumentaatiosta kaikkien tarvittavien ympäristömuuttujien saamiseksi](https://docs.lumi-supercomputer.eu/software/packages/pytorch/#example). Nämä asetetaan automaattisesti CSC:n PyTorch-modulissa.

Jos muunnet vanhaa PyTorch-ohjelmaa, on muutamia toimenpiteitä, joita sinun täytyy tehdä:

1. Alusta `init_process_group()`:llä, esimerkiksi:

    ```python
    import torch.distributed as dist

    dist.init_process_group(backend='nccl')

    local_rank = int(os.environ['LOCAL_RANK'])
    torch.cuda.set_device(local_rank)
    ```

2. Kääri mallisi `DistributedDataParallel`:llä:

    ```python
    from torch.nn.parallel import DistributedDataParallel

    model = DistributedDataParallel(model, device_ids=[local_rank])
    ```

3. Käytä `DistributedSampler`:ia `DataLoader`:issasi:

    ```python
    from torch.utils.data.distributed import DistributedSampler

    train_sampler = DistributedSampler(train_dataset)
    train_loader = DataLoader(dataset=train_dataset, sampler=train_sampler, ...)
    ```

Käyttökelpoinen esimerkki Puhtille löytyy meidän [`pytorch-ddp-examples`-arkistostamme](https://github.com/CSCfi/pytorch-ddp-examples):

- [mnist_ddp.py](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/mnist_ddp.py) näyttää Python-koodin yksinkertaisen CNN-mallin opettamiseen MNIST-datalla käyttäen PyTorch DDP:tä
- [run-ddp-gpu4.sh](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/run-ddp-gpu4.sh) sisältää Slurm-skriptin harjoituksen suorittamiseksi 4 GPU:lla yksittäisellä solmulla
- [run-ddp-gpu8.sh](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/run-ddp-gpu8.sh) näyttää saman kahdelle täydelle solmulle, yhteensä 8 GPU:lle


### PyTorch Lightning DDP:n kanssa {#pytorch-lightning-with-ddp}

[PyTorch Lightning](https://lightning.ai/) on suosittu korkean tason kehys, joka on suunniteltu helpottamaan PyTorchin käyttöä. Monigpu- ja monisolmuisten töiden suorittaminen Lightningin kanssa on melko helppoa. Jos haluat muuntaa nykyisen PyTorch-ohjelmasi Lightningiksi, viittaamme [viralliseen PyTorch Lightning -ohjeeseen](https://lightning.ai/docs/pytorch/stable/).

Suosittelemme käyttämään DistributedDataParallel (DDP): tä monigpu- ja monisolmuiseen käyttöön. Sinun tarvitsee vain lisätä nämä vaihtoehdot Lightning Traineriin:

```python
trainer = pl.Trainer(devices=args.gpus,
                     num_nodes=args.nodes,
                     accelerator='gpu',
                     strategy='ddp',
                     ...)
```

Sinun täytyy antaa asianmukaiset arvot `devices` (GPU:den määrä *solmua kohden*) ja `num_nodes`. Suosittelemme antamaan nämä komentoriviparametreina:

```python
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--gpus', default=1, type=int,
                        help='number of GPUs per node')
    parser.add_argument('--nodes', default=1, type=int,
                        help='number of nodes')
    # any other command line arguments here
    args = parser.parse_args()
```

PyTorch Lightning Slurm-skripti yhden solmun käyttöön käyttäen kaikkia GPU:ita:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=320G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    module purge
    module load pytorch

    srun python3 myprog.py --gpus=4 --nodes=1 <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=32
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4

    module purge
    module load pytorch
    
    srun python3 myprog.py --gpus=4 --nodes=1 <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=8
    #SBATCH --cpus-per-task=7
    #SBATCH --gpus-per-node=8
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00

    module purge
    module use /appl/local/csc/modulefiles
    module load pytorch

    srun python3 myprog.py --gpus=8 --nodes=1 <options>
    ```

<br/>
PyTorch Lightning Slurm-skripti kahtena täydellisenä solmuna kaikkia GPU:ita käyttäen:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=320G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    module purge
    module load pytorch
    
    srun python3 myprog.py --gpus=4 --nodes=2 <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=32
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    module purge
    module load pytorch

    srun python3 myprog.py --gpus=4 --nodes=2 <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=8
    #SBATCH --cpus-per-task=7
    #SBATCH --gpus-per-node=8
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00
    
    module purge
    module use /appl/local/csc/modulefiles
    module load pytorch

    srun python3 myprog.py --gpus=8 --nodes=2 <options>
    ```

### Accelerate {#accelerate}

Hugging Facen
[Accelerate](https://huggingface.co/docs/transformers/accelerate) on
suosittu kehys suurten kielimallien kouluttamiseen, ja sen avulla
huomattavasti monimutkaisempien koulutusalgojen, kuten FSDP:n,
käyttäminen on hyvin helppoa. Acceleratella työn suorittaminen
poikkeaa hieman PyTorch DDP:stä, koska meidän täytyy käyttää
acceleraten käynnistäjää ja lisäksi tarjota Accelerate-konfiguraatiotiedosto.

Toimiva [esimerkki LLM:ien hienosäädöstä löytyy tästä GitHub
repositoriosta](https://github.com/CSCfi/llm-fine-tuning-examples)
(tutustu tiedostoihin, jotka päättyvät `-accelerate.sh`). Katso myös
oppaan kenttä [käyttämisestä supertietokoneilla](ml-llm.md).

Esimerkki Accelerate käyttämisestä kaikilla GPU:illa yhdellä solmulla:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=320G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    module purge
    module load pytorch

    srun accelerate launch \
     --config_file=accelerate_config.yaml \
     --num_processes=4 \
     --num_machines=1 \
     --machine_rank=0 \
     myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=128
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    module purge
    module load pytorch

    srun accelerate launch \
     --config_file=accelerate_config.yaml \
     --num_processes=4 \
     --num_machines=1 \
     --machine_rank=0 \
     myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=56
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00
    #SBATCH --gpus-per-node=8
    
    module purge
    module use /appl/local/csc/modulefiles/
    module load pytorch

    srun accelerate launch \
     --config_file=accelerate_config.yaml \
     --num_processes=8 \
     --num_machines=1 \
     --machine_rank=0 \
     myprog.py <options>
    ```

Esimerkki Accelerate suorittamisesta 2 täydellä solmulla (8 GPU:ta).

=== "Puhti"

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --mem=320G
#SBATCH --time=1:00:00
#SBATCH --gres=gpu:v100:4

module purge
module load pytorch

GPUS_PER_NODE=4
NUM_PROCESSES=$(expr $SLURM_NNODES \* $GPUS_PER_NODE)
MAIN_PROCESS_IP=$(hostname -i)

RUN_CMD="accelerate launch \
                    --config_file=accelerate_config.yaml \
                    --num_processes=$NUM_PROCESSES \
                    --num_machines=$SLURM_NNODES \
                    --machine_rank=\$SLURM_NODEID \
                    --main_process_ip=$MAIN_PROCESS_IP \
                    myprog.py <options>"

srun bash -c "$RUN_CMD"
```

=== "Mahti"

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gpumedium
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=128
#SBATCH --time=1:00:00
#SBATCH --gres=gpu:a100:4

module purge
module load pytorch

GPUS_PER_NODE=4
NUM_PROCESSES=$(expr $SLURM_NNODES \* $GPUS_PER_NODE)
MAIN_PROCESS_IP=$(hostname -i)

RUN_CMD="accelerate launch \
                    --config_file=accelerate_config.yaml \
                    --num_processes=$NUM_PROCESSES \
                    --num_machines=$SLURM_NNODES \
                    --machine_rank=\$SLURM_NODEID \
                    --main_process_ip=$MAIN_PROCESS_IP \
                    myprog.py <options>"

srun bash -c "$RUN_CMD"
```

=== "LUMI"

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=small-g
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=56
#SBATCH --gpus-per-node=8
#SBATCH --mem=480G
#SBATCH --time=1:00:00

module purge
module use /appl/local/csc/modulefiles
module load pytorch

NUM_PROCESSES=$(expr $SLURM_NNODES \* $SLURM_GPUS_PER_NODE)
MAIN_PROCESS_IP=$(hostname -i)

RUN_CMD="accelerate launch \
                    --config_file=accelerate_config.yaml \
                    --num_processes=$NUM_PROCESSES \
                    --num_machines=$SLURM_NNODES \
                    --machine_rank=\$SLURM_NODEID \
                    --main_process_ip=$MAIN_PROCESS_IP \
                    myprog.py <options>"

srun bash -c "$RUN_CMD"
```

Huomaa jonkin verran kankea tapa määrittää komento `\$SLURM_NODEID`
-muuttujan kanssa paeta niin, että se arvioidaan vain kyseisellä
solmulla, missä se suoritetaan. Normaalisti kaikki muuttujat
arvioidaan ensimmäisellä solmulla, mutta `\$SLURM_NODEID`:n tulee olla
eri arvo jokaisella solmulla, jotta hajautettu asetus toimisi
oikein.

Molemmat esimerkit käyttävät tätä `accelerate_config.yaml`-tiedostoa:

```yaml
compute_environment: LOCAL_MACHINE
debug: false
distributed_type: MULTI_GPU
downcast_bf16: 'no'
gpu_ids: all
main_training_function: main
main_process_port: 29500
mixed_precision: bf16
num_processes: 1
rdzv_backend: static
same_network: true
tpu_env: []
tpu_use_cluster: false
tpu_use_sudo: false
use_cpu: false
```

Jos haluat käyttää FSDP:tä, käytä yksinkertaisesti Accelerate-konfiguraatiota, joka on samanlainen kuin tämä:

```yaml
compute_environment: LOCAL_MACHINE
debug: false
distributed_type: FSDP
downcast_bf16: 'no'
fsdp_config:
  fsdp_auto_wrap_policy: TRANSFORMER_BASED_WRAP
  fsdp_backward_prefetch_policy: BACKWARD_PRE
  fsdp_forward_prefetch: false
  fsdp_cpu_ram_efficient_loading: true
  fsdp_offload_params: false
  fsdp_sharding_strategy: FULL_SHARD
  fsdp_state_dict_type: SHARDED_STATE_DICT
  fsdp_sync_module_states: true
  fsdp_use_orig_params: true
gpu_ids: all
main_training_function: main
main_process_port: 29500
mixed_precision: bf16
num_processes: 1
rdzv_backend: static
same_network: true
tpu_env: []
tpu_use_cluster: false
tpu_use_sudo: false
use_cpu: false
```

Katso [GitHub repositoriomme saadaksesi lisää
esimerkkejä](https://github.com/CSCfi/llm-fine-tuning-examples).

### DeepSpeed {#deepspeed}

[DeepSpeed](https://www.deepspeed.ai/) on optimointiohjelmistopaketti
PyTorchille, joka auttaa skaalaamaan sekä harjoittelua että
mallien käyttöä suurten syväoppimismallien kanssa. DeepSpeed on
tuettu [PyTorchin
modeleissa Puhtissa ja Mahtissa](../../apps/pytorch.md) versiosta
1.10 alkaen. DeepSpeed ei ole vielä täysin tuettu LUMIssa.

Esimerkki DeepSpeedin käyttämisestä yhdellä täydellisellä solmulla käyttäen
`deepspeed`-käynnistintä:

=== "Puhti"

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=40
#SBATCH --mem=320G
#SBATCH --time=1:00:00
#SBATCH --gres=gpu:v100:4

module purge
module load pytorch

srun apptainer_wrapper exec deepspeed myprog.py \
    --deepspeed --deepspeed_config my_ds_config.json \
    <further options>
```

=== "Mahti"

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gpumedium
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=128
#SBATCH --time=1:00:00
#SBATCH --gres=gpu:a100:4

module purge
module load pytorch

srun apptainer_wrapper exec deepspeed myprog.py \
    --deepspeed --deepspeed_config my_ds_config.json \
    <further options>
```

=== "LUMI"

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=small-g
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=56
#SBATCH --gpus-per-node=8
#SBATCH --mem=480G
#SBATCH --time=1:00:00

module purge
