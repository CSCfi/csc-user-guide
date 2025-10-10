# Whisper { #whisper }

Whisper on yleiskäyttöinen puheentunnistusmalli. Se on koulutettu suurella ja monipuolisella ääniaineistolla, ja se on myös monitehtäväinen malli, joka pystyy monikieliseen puheentunnistukseen, puheen käännökseen ja kielen tunnistukseen.

* [Whisperin kotisivu](https://github.com/openai/whisper)

Whisper voidaan asentaa SD Desktop -virtuaalikoneeseen [SD Software -asentimella](../../sensitive-data/sd-desktop-software.md#customisation-via-sd-software-installer).

SD Desktopille toimitettava versio perustuu projektiin [Faster-Whisper-XXL](https://github.com/Purfview/whisper-standalone-win).

Asennuksen jälkeen Whisper on käytettävissä komentorivityökaluna SD Desktopissa. 

Esimerkkikomennot:

```bash
whisper audio.mp3 --model medium --threads 4
```

Esimerkkikomento puhujien erottelulla (diarization):

```bash
whisper interview.mp4 --model large --language French --threads 4 --diarize pyannote_v3.0 --diarize_threads 4 --num_speakers 2 -o interview_results
```

**Päivitys 5.5.2025**

Ennen viimeisintä päivitystä SD Software -asennin tarjosi [WhisperDO](https://github.com/nicholasgcotton/WhisperDO) -pohjaisen Whisper-asennuksen.
Faster-Whisper-XXL tarjoaa nyt uusia ominaisuuksia, kuten puhujien erottelun, sekä paremman suorituskyvyn verrattuna vanhaan WhisperDO:hon.

Jos haluat päivittää vanhan WhisperDO-asennuksesi uuteen Faster-Whisper-XXL:ään, sinun on ensin poistettava vanha versio seuraavilla komennoilla:

```bash
rm /shared-directory/sd-tools/apptainer/whisper.sif
rm /shared-directory/sd-tools/bin/whisper
```

Tämän jälkeen voit käyttää SD Software -asenninta Whisperin uuden version asentamiseen.