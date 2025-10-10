# Työskentely suurten kielimallien kanssa supertietokoneilla { #working-with-large-language-models-on-supercomputers }

Tämä opas antaa esimerkkejä ja vinkkejä siitä, miten suurten kielimallien (LLM) kanssa työskennellään CSC:n supertietokoneilla. Se on osa [koneoppimisopastamme](ml-guide.md).

## LLM:t ja GPU-muisti { #llms-and-gpu-memory }

Jos teet inferenssiä (käytät mallia, etkä kouluta sitä), voit joissain tapauksissa pärjätä ilman GPU:ta, esimerkiksi jos malli on riittävän pieni tai sitä on pienennetty kvantisoinnilla. Useimmissa muissa tapauksissa tarvitset kuitenkin GPU:n.

Jotta LLM:ää (tai mitä tahansa neuroverkkoa) voidaan käyttää GPU:lla, malli on ladattava GPU-muistiin (VRAM). LLM:t voivat olla hyvin suuria, ja tällöin GPU-muistin koko on kriittinen. Voit katsoa tarkemmat tiedot [GPU-tilastoistamme](gpu-ml.md#puhti-mahti-or-lumi), mutta GPU:idemme VRAM-muistit ovat seuraavat:

- 32 GB Puchtissa (NVIDIA V100)
- 40 GB Mahtissa (NVIDIA A100)
- 64 GB LUMIssa (yhden GCD:n AMD MI250x)

Mallin koko muistissa riippuu siitä, miten painot tallennetaan. Tyypillisesti tavallinen liukuluku tallennetaan muodossa fp32, joka käyttää 32 bittiä muistia eli 4 tavua (muista: 8 bittiä = 1 tavu). Syväoppimisessa 16-bittisiä liukulukumuotoja (fp16 tai bf16) on käytetty pitkään nopeuttamaan osaa laskennasta. Nämä käyttävät 2 tavua muistia per paino. Viime aikoina, kun mallien koot ovat kasvaneet, vielä pienempää tarkkuutta käyttävät muodot, aina 8 tai jopa 4 bittiin, ovat yleistyneet. Yleisiä kvantisointimenetelmiä ovat [GPTQ](https://arxiv.org/abs/2210.17323), [SpQR](https://arxiv.org/abs/2306.03078) ja [GGML/GGUF](https://huggingface.co/docs/hub/en/gguf). Jos kvantisointi ei ole tuttua, katso esimerkiksi [tämä verkkoguide kvantisoinnista LLM:ille](https://www.datacamp.com/tutorial/quantization-for-large-language-models).

Mallin koko muistissa on parametrien lukumäärä kerrottuna yhden painon tallentamiseen tarvittavien tavujen määrällä. Esimerkiksi 30 miljardin parametrin malli fp16-muodossa vie 60 GB muistia. Käytännössä [inferenssissä on jopa 20 % overheadia][1], joten saatat tarvita noin 70 GB muistia, eikä edes yksi GCD LUMIssa välttämättä riitä esimerkkimallille. Jos sen sijaan tallennat mallin 4 bitin kvantisoinnilla, se on noin 0,5 tavua parametria kohden, eli noin 15 GB esimerkissämme (tai noin 18 GB overheadin kanssa).

Koulutuksessa muistia tarvitaan huomattavasti enemmän, koska mallin lisäksi myös optimoijan tilat, gradientit ja aktivoinnit on säilytettävä. Hyvin karkeana arviona hienosäätöön tarvitaan noin 4–6 kertaa mallin koko (GB), mutta tämä riippuu paljon yksityiskohdista. Esimerkin 30B parametrin fp16-mallille tämä voisi tarkoittaa 60 GB x 6 = 360 GB GPU-muistia koulutusta varten! Käsittelemme keinoja ratkaista tätä ongelmaa alla. Katso myös [EleutherAI:n Transformer Math 101 -blogikirjoitus][1].

## LLM:ien hienosäätö { #fine-tuning-llms }

Meillä on [git-repositorio, jossa on esimerkkiskriptejä LLM:ien hienosäätöön Puhtissa, Mahtissa tai LUMIssa][2]. Esimerkki käyttää [Hugging Face (HF) -kirjastoja][3] ja erityisesti HF Traineria kouluttamaan tietty malli (HF:n mallirepositorioista) IMDb-elokuva-arvosteluaineistolla. Itse tehtävä ei välttämättä ole järin mielekäs, vaan tarkoitus on demonstroida mallin hienosäädön teknistä toteutusta annetulla aineistolla.

Esimerkit käyttävät oletuksena [EleutherAI/gpt-neo-1.3B][4] -mallia, koska se mahtuu yhden GPU:n muistiin Puhtissa. Koska kyseessä on 1,37 miljardin parametrin malli 32-bittisillä painoilla, peukalosääntömme mukaan se saattaa vaatia jopa 1,37x4x6 = 32 GB muistia koulutuksessa, joten sen pitäisi juuri ja juuri mahtua Puhtin V100:n 32 GB maksimimuistiin (jos olemme onnekkaita).

Repositoriossa on peruskäynnistysskriptit Puhtiin, Mahtiin ja LUMIin yhdelle GPU:lle, kokonaiselle solmulle (4 GPU:ta Puhtissa/Mahtissa ja 8 GPU:ta LUMIssa) ja kahdelle kokonaiselle solmulle (vastaavasti 8 tai 16 GPU:ta). Slurm-skriptit ovat käytännössä samoja kuin missä tahansa PyTorch DDP -ajoissa; katso [oppaamme monen GPU:n ja monen solmun ML:stä](ml-multi.md#pytorch-ddp) esimerkkejä tai vilkaise suoraan [GitHub-repositorion skriptejä][2]:

- [`run-finetuning-puhti-gpu1.sh`](https://github.com/CSCfi/llm-fine-tuning-examples/blob/master/run-finetuning-puhti-gpu1.sh) – hienosäätö Puhtissa yhdellä GPU:lla
- [`run-finetuning-puhti-gpu4.sh`](https://github.com/CSCfi/llm-fine-tuning-examples/blob/master/run-finetuning-puhti-gpu4.sh) – hienosäätö Puhtissa yhdellä kokonaisella solmulla (4 GPU:ta)
- [`run-finetuning-puhti-gpu8.sh`](https://github.com/CSCfi/llm-fine-tuning-examples/blob/master/run-finetuning-puhti-gpu8.sh) – hienosäätö Puhtissa kahdella kokonaisella solmulla (yhteensä 8 GPU:ta)

(Repositoriossa on myös skriptejä Mahtiin ja LUMIin; katso [tiedostolistausta][2].)

Perus monen GPU:n versiot käyttävät kaikki PyTorch Distributed Data Parallel (DDP) -tilaa, jossa jokaisella GPU:lla on täysi kopio mallista. Vain koulutusdata jaetaan eri GPU:ille. Tämä tarkoittaa, että koko mallin on mahduttava yhdelle GPU:lle.

Jos mallisi ei mahdu yhdelle GPU:lle Puhtissa, se saattaa toimia Mahtissa tai LUMIssa, mutta tarkista ensin yllä mainitulla peukalosäännöllä, onko se edes mahdollista! Jollei, lue eteenpäin PEFT- ja FSDP-lähestymistavoista.

### PEFT ja LoRA { #using-peft-and-lora }

Vaikka mallisi mahtuisi GPU-muistiin, on silti mahdollista, että hienosäätöprosessin vaatima lisämuisti ei mahdu (tämän huomaa nopeasti, kun ohjelma kaatuu CUDA- tai ROCm out-of-memory -virheeseen!). Tällöin ratkaisuna voi olla [Parameter Efficient Fine-Tuning (PEFT)][5] -kirjasto, joka kouluttaa pienemmän määrän lisäparametreja ja vähentää näin koulutuksen overheadia merkittävästi. PEFT tukee monia menetelmiä, kuten [LoRA](https://arxiv.org/abs/2106.09685) ja [QLoRA](https://arxiv.org/abs/2305.14314).

PEFT:llä parametrien määrä on tyypillisesti noin 10 % alkuperäisestä, mutta GPU-muistin säästö vaihtelee tilanteen mukaan. Olemme nähneet säästöjä 5–60 %.

PEFT on hyvin helppo ottaa käyttöön; katso [PEFT quicktour][6] esimerkkiä varten. Yllä olevaan esimerkkiin PEFT voidaan ottaa käyttöön lisäämällä lippu `--peft`. Kannattaa myös [perehtyä hieman syvemmin esimerkiksi LoRA:n hyviin parametreihin][8].

### Accelerate ja FSDP { #using-accelerate-and-fsdp }

Suuremmille malleille, jotka eivät mahdu GPU-muistiin (edes inferenssissä), tarvitset lähestymistavan, joka jakaa itse mallin (sekä koulutuksen overheadin) useille GPU:ille. Emme voi enää pitää täyttä kopiota mallista jokaisessa GPU:ssa.

Hyvä lähestymistapa, jota PyTorch tukee natiivisti, on [Fully Sharded Data Parallel (FSDP)][7]. FSDP:ssä mallin parametreja, gradientteja ja optimoijan tiloja ei säilytetä kokonaan jokaisessa GPU:ssa, vaan ne jaetaan (shardataan) kaikkien GPU:iden kesken ja kootaan yhteen vain silloin, kun niitä tarvitaan kulloisessakin koulutusvaiheessa.

Ehkä helpoin tapa ottaa FSDP käyttöön suurilla kielimalleilla on käyttää Hugging Facen Accelerate-kehystä. PyTorch-skriptiin ei tarvita muutoksia; riittää, että vaihdetaan `accelerate`-käynnistimeen. [GitHub-repositoriossamme][2] on esimerkkiskriptit ajamiseen yhdellä tai kahdella täydellä solmulla Puhtissa:

- [`run-finetuning-puhti-gpu4-accelerate.sh`](https://github.com/CSCfi/llm-fine-tuning-examples/blob/master/run-finetuning-puhti-gpu4-accelerate.sh) – hienosäätö Puhtissa yhdellä kokonaisella solmulla Acceleratella
- [`run-finetuning-puhti-gpu8-accelerate.sh`](https://github.com/CSCfi/llm-fine-tuning-examples/blob/master/run-finetuning-puhti-gpu8-accelerate.sh) – hienosäätö Puhtissa kahdella kokonaisella solmulla Acceleratella

(Repositoriossa on myös skriptejä Mahtiin ja LUMIin; katso [tiedostolistausta][2].)

[Moni-GPU- ja monisolmu-ML-oppaassamme](ml-multi.md#accelerate) on myös Slurm-esimerkkiskriptejä Acceleraten ja FSDP:n käyttöön.

Kaksi huomioitavaa asiaa Acceleratea käytettäessä:

1. `accelerate`-käynnistin odottaa konfiguraatio-YAML-tiedostoa. Olemme tarjonneet kaksi esimerkkiä GitHub-repositoriossa: `accelerate_config.yaml` perusesimerkkinä ja `accelerate_config_fsdp.yaml` FSDP:tä varten. Nämä konfigit käyttävät järkeviä oletusparametreja, mutta niitä voi olla hyödyllistä säätää – erityisesti [tutustu FSDP:n parametreihin][9].

2. Monisolmuajoissa `accelerate`-käynnistin pitää käynnistää erikseen jokaisessa solmussa asettamalla `--machine_rank`-argumentti solmun järjestysluvun mukaan (0=ensimmäinen solmu, 1=toinen solmu jne.). Voimme käyttää `$SLURM_NODEID`-muuttujaa tämän asettamiseen, mutta tarvitsemme shell-kikan, jotta arvoa ei evaluoida ennen kuin komento ajetaan kyseisessä solmussa. (Katso skripti [`run-finetuning-puhti-gpu8-accelerate.sh`](https://github.com/CSCfi/llm-fine-tuning-examples/blob/master/run-finetuning-puhti-gpu8-accelerate.sh) esimerkkinä siitä, miten tämä tehdään.)

Voit käyttää myös PEFT:iä (LoRA) Acceleraten kanssa lisäämällä `--peft` esimerkkiskriptiimme.

### Vaihtoehtoiset trainerit { #alternative-trainers }

Vaihtoehto Hugging Facen perinteiselle Trainerille LLM:ien hienosäätöön on [TRL](https://huggingface.co/docs/trl/index)-kirjaston [SFTTrainer](https://huggingface.co/docs/trl/main/en/sft_trainer). Näitä ei käsitellä tässä oppaassa. Suosittelemme tutustumaan esimerkiksi [tähän Hugging Facen hienosäätöoppaaseen](https://huggingface.co/blog/mlabonne/sft-llama3), joka kattaa myös [Unsloth-kirjaston](https://github.com/unslothai/unsloth).

## Kvantisoinnin käyttäminen { #using-quantization }

`bitsandbytes`-kirjaston avulla voit käyttää myös 4-bittistä kvantisointia. [Kvantisointi on integroitu myös Hugging Face Transformersiin](https://huggingface.co/blog/4bit-transformers-bitsandbytes).

```python
from transformers import BitsAndBytesConfig
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_storage=torch.bfloat16,
)

model = AutoModelForCausalLM.from_pretrained(
    args.model,
    quantization_config=bnb_config,
    ...
)
```

Esimerkkiskriptissämme tätä voi kokeilla `--4bit`-argumentilla. Tämä pienentää muistivaatimuksia entisestään.

## Retrieval-augmented generation (RAG) { #retrieval-augmented-generation-(rag) }

[Retrieval-augmented generation (RAG)][RAG] on tapa käyttää valmiiksi koulutettua suurta kielimallia yhdessä käyttäjän oman aineiston kanssa ilman laskennallisesti kallista hienosäätöä tai mallin uudelleenkoulutusta. Lyhyesti: tämä toimii tekemällä haun aineistoon ja käyttämällä parhaita tuloksia lisäkontekstina kielimallille.

RAG:ssa haku on järjestelmän kriittinen osa, sillä epäonnistunut haku antaa LLM:lle väärän kontekstin, mikä helposti johtaa epäolennaiseen generointiin. Tehokasta hakua varten voi hyödyntää upotusmalleja (embedding) ja nopeita vektorihautamenetelmiä. Katso [RAG-60K-repositoriomme][RAG-60K] esimerkkinä siitä, miten supertietokoneita hyödynnetään Faiss-vektorivaraston valmistelussa huippuluokan upotusmalleilla.

## Inferenssi { #inference }

Inferenssi, eli mallin käyttäminen sen kouluttamisen sijaan, on yleensä paljon yksinkertaisempaa. [Esimerkkirepositoriossamme][2] on inferenssiesimerkki tiedostoissa `inference-demo.py` ja `run-inference-puhti.sh`. Jos mallisi ei mahdu yhdelle GPU:lle, voit yksinkertaisesti varata useampia GPU:ita ja antaa Hugging Facen hoitaa jaon asettamalla `device_map='auto'` mallia ladatessa, esimerkiksi:

```python
model = AutoModelForCausalLM.from_pretrained(args.model, device_map='auto')
```

### Inferenssi Ollaamalla { #inference-with-ollama }

[Ollama](https://ollama.com/) on suosittu työkalu LLM:ien käyttöön, sillä se tukee [useita huipputason malleja](https://ollama.com/library), joihin pääsee käsiksi API:n kautta. Ollama on suunniteltu ajettavaksi palveluna, joten se ei suoraan sovellu eräajoon supertietokoneilla. Sitä voi kuitenkin ajaa osana eräajoa käynnistämällä palvelun työn alussa ja pysäyttämällä sen työn lopussa.

Ensin voit asentaa Ollaman projektikansioosi näin:

```bash
cd /projappl/project_2001234  # korvaa sinulle sopivalla polulla
mkdir ollama
cd ollama
wget https://ollama.com/download/ollama-linux-amd64.tgz
tar xzf ollama-linux-amd64.tgz
rm ollama-linux-amd64.tgz
```

LUMIssa sinun on tehtävä lisäksi seuraavat vaiheet (samassa hakemistossa kuin yllä). Huomaa, että lisätyillä ROCm-tiedostoilla asennus vie 14 GB levytilaa!

```bash
wget https://ollama.com/download/ollama-linux-amd64-rocm.tgz
tar xzf ollama-linux-amd64-rocm.tgz
rm ollama-linux-amd64-rocm.tgz
```

Eräajossasi sinun tarvitsee sitten vain käynnistää palvelu komennolla `ollama serve`. Tämän jälkeen työsi voi käyttää APIa `localhostissa` portissa `11434`. On myös hyvä asettaa ympäristömuuttuja `OLLAMA_MODELS` osoittamaan projektin scratchiin, koska muuten suuret mallipaketit latautuvat kotihakemistoosi. Katso [esimerkkimme Slurm-skriptistä `run-ollama.sh` Ollaaman ajamiseen][11].

Repositoriossa [`ai-inference-examples`][14] on myös esimerkkejä Ollaaman ajamisesta kokonaisella solmulla, jossa on 4 GPU:ta Puhtissa ja 8 GPU:ta LUMIssa.

### Inferenssi vLLM:llä { #inference-with-vllm }

[vLLM][12] on toinen kirjasto LLM-inferenssiin. vLLM tukee [offline-eräajoin tehtävää inferenssiä][13], mikä on supertietokoneajoon parhaiten sopiva tila. Tämä ajetaan kuten tavallinen Python-eräajo.

Tässä on käyttäjän toimittama esimerkki suuren aineiston tehokkaaseen käsittelyyn vLLM:llä: <https://github.com/TurkuNLP/ECCO-ocr-large-run>.

Joissain tilanteissa tarvitaan silti OpenAI-yhteensopivaa palvelinta, esimerkiksi kun rajapintoja käytetään muihin ohjelmiin. [Esimerkkiskriptit vLLM:n ajamiseen Puhtissa, Mahtissa ja LUMIssa löytyvät `ai-inference-examples` -repositoriostamme][14]. Siellä on myös esimerkki ajosta usealla solmulla Rayn avulla.

[1]: https://blog.eleuther.ai/transformer-math/
[2]: https://github.com/CSCfi/llm-fine-tuning-examples
[3]: https://huggingface.co/docs/transformers/en/index
[4]: https://huggingface.co/EleutherAI/gpt-neo-1.3B
[5]: https://huggingface.co/docs/peft/index
[6]: https://huggingface.co/docs/peft/quicktour
[7]: https://pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api/
[8]: https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms
[9]: https://huggingface.co/docs/transformers/fsdp
[10]: https://huggingface.co/docs/peft/en/accelerate/fsdp#the-important-parts
[11]: https://github.com/CSCfi/machine-learning-scripts/blob/master/slurm/run-ollama.sh
[12]: https://docs.vllm.ai/en/latest/
[13]: https://docs.vllm.ai/en/latest/getting_started/quickstart.html#offline-batched-inference
[14]: https://github.com/CSCfi/ai-inference-examples
[RAG]: https://en.wikipedia.org/wiki/Retrieval-augmented_generation
[RAG-60K]: https://github.com/CSCfi/RAG-60K/tree/main