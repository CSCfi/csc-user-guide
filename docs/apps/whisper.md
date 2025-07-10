---
tags:
  - Free
catalog:
  name: Whisper
  description:  General-purpose speech recognition model.
  license_type: Free
  disciplines:
    - AI
  available_on:
    - Puhti
---
## Available
Faster-Whisper-XXL r245.4 is available in Puhti.

## License
Faster-Whisper-XXL is licenced using [MIT-licence](https://github.com/SYSTRAN/faster-whisper/blob/master/LICENSE).

## Whisper

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of 
diverse audio and is also a multitasking model that can perform multilingual speech recognition, 
speech translation, and language identification.

* [Whisper home page](https://github.com/openai/whisper)

## Usage

CSC users can easily install Whisper in their own python virtual environments in Puhti and Mahti.
I addition, Puhti has a pre-installed [Faster-Whisper-XXL](https://github.com/Purfview/whisper-standalone-win) version of Whisper.
This Whisper environment can be activated in Puhti with command:

```text
module load whisper
```

Sample commands:

```bash
whisper audio.mp3 --model medium 
```

Sample command with diarization enabled:

```bash
whisper interview.mp4 --model large --language French --threads 4 --diarize pyannote_v3.0 --diarize_threads 4 --num_speakers 2 -o interview_results
```

### Example batch script

Whisper can use utilize GPU computing effectively. Example batch script below reserves one GPU for a Whisper job. 

```
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

## More information

   * [Open AI Whisper](https://github.com/openai/whisper)
   * [Faster-Whisper-XXL](https://github.com/Purfview/whisper-standalone-win)
