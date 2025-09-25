---
tags:
  - Free
catalog:
  name: Whisper
  description: General-purpose speech recognition model
  description_fi: Yleistarkoituksinen puheentunnistusmalli
  license_type: Free
  disciplines:
    - Data Analytics and Machine Learning
  available_on:
    - Puhti
---

# Whisper { #whisper }

Whisper on yleistarkoituksinen puheentunnistusmalli. Se on koulutettu laajalla, monipuolisella ääniaineistolla, ja se on myös monitehtävämalli, joka osaa suorittaa monikielistä puheentunnistusta, puheen käännöstä ja kielen tunnistusta.

* [Whisperin kotisivu](https://github.com/openai/whisper)

## Saatavilla { #available }

Faster-Whisper-XXL r245.4 on saatavilla Puhtissa.

## Lisenssi { #license }

Faster-Whisper-XXL on lisensoitu
[MIT-lisenssillä](https://github.com/SYSTRAN/faster-whisper/blob/master/LICENSE).

## Käyttö { #usage }

CSC:n käyttäjät voivat helposti asentaa Whisperin
[omiin Python-virtuaaliympäristöihinsä](../support/tutorials/python-usage-guide.md#creating-your-own-python-environments)
Puhtissa ja Mahtissa. Lisäksi Puhtissa on esiasennettu
[Faster-Whisper-XXL](https://github.com/Purfview/whisper-standalone-win)
-versio Whisperistä. Tämä Whisper-ympäristö voidaan aktivoida Puhtissa komennolla:

```bash
module load whisper
```

Esimerkkikomento:

```bash
whisper audio.mp3 --model medium 
```

Esimerkkikomento, jossa puhe-erottelu (diarization) käytössä:

```bash
whisper interview.mp4 --model large --language French --threads 4 --diarize pyannote_v3.0 --diarize_threads 4 --num_speakers 2 -o interview_results
```

### Esimerkkieräskripti { #example-batch-script }

Whisper osaa hyödyntää GPU-laskentaa tehokkaasti. Alla oleva esimerkkieräskripti varaa yhden GPU:n Whisper-ajoa varten.

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G
#SBATCH --time=1:00:00
#SBATCH --gres=gpu:v100:1
    
module load whisper
srun whisper interview.mp4 --model large --language French --threads 4 --diarize pyannote_v3.0 --diarize_threads 4 --num_speakers 2 -o interview_results
```

## Lisätietoja { #more-information }

* [OpenAI Whisper](https://github.com/openai/whisper)
* [Faster-Whisper-XXL](https://github.com/Purfview/whisper-standalone-win)