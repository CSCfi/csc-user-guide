# Whisper

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of 
diverse audio and is also a multitasking model that can perform multilingual speech recognition, 
speech translation, and language identification.

*   [Whisper home page](https://github.com/openai/whisper)

Whisper can be installed to a SD Desktop virtual machine with [SD Software installer](../../sensitive-data/sd-desktop-software.md#customisation-via-sd-software-installer).

The version provided for SD Desktop is based on [Faster-Whisper-XXL](https://github.com/Purfview/whisper-standalone-win).

After installation Whisper is available as a command line tool in SD Desktop. 

Sample commands:

```text
whisper audio.mp3 --model medium --threads 4
```

Sample command with diarization enabled:

```text
whisper interview.mp4 --model large --language French --threads 4 --diarize pyannote_v3.0 --diarize_threads 4 --num_speakers 2 -o interview_results
```

**Update on 5.5. 2025**

Before the latest update the SD tool installer provided [WhisperDO](https://github.com/nicholasgcotton/WhisperDO) based Whisper installation.
Faster-Whisper-XXL provides now new features, like diarization, and better performance compared to the old WhisperDO. 

If you want to upgrade your old WhisperDO installation to the new Faster-Whisper-XXL, you need to first remove the old version with commands:

```text
rm /shared-directory/sd-tools/apptainer/whisper.sif
rm /shared-directory/sd-tools/bin/whisper
```
After that you can use the SD tool installer to install the new version of Whisper.
 
