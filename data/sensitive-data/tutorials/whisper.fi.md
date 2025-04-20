# Whisper {#whisper}

Whisper on yleiskäyttöinen puheentunnistusmalli. Se on koulutettu monipuolisella ääniaineistolla ja on myös monitehtäväinen malli, joka pystyy suorittamaan monikielistä puheentunnistusta, puheen käännöstä sekä kielen tunnistusta.

*   [Whisperin kotisivu](https://github.com/openai/whisper)

Whisper voidaan asentaa SD Desktop -virtuaalikoneeseen [SD Software installerin](../../sensitive-data/sd-desktop-software.md#customisation-via-sd-software-installer) avulla.

SD Desktopille tarjottu versio perustuu [WhisperDO:hon](https://github.com/nicholasgcotton/WhisperDO).

Asennuksen jälkeen Whisper on saatavilla komentorivityökaluna SD Desktopissa.
Esimerkki komennosta:

```text
whisper audio.mp3 --model medium --threads 4
```