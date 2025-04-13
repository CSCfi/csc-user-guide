
# Whisper

Whisper on yleiskäyttöinen puheentunnistusmalli. Se on koulutettu suurella monipuolisen äänen tietojoukolla ja se on myös monitehtävämalli, joka voi suorittaa monikielistä puheentunnistusta, puheen kääntämistä ja kielen tunnistusta.

*   [Whisper kotisivu](https://github.com/openai/whisper)

Whisper voidaan asentaa SD Desktop -virtuaalikoneeseen [SD Software -asentajalla](../../sensitive-data/sd-desktop-software.md#customisation-via-sd-software-installer).

SD Desktopille tarjottu versio perustuu [WhisperDO:hon](https://github.com/nicholasgcotton/WhisperDO).

Asennuksen jälkeen Whisper on saatavilla komentorivityökaluna SD Desktopissa. Esimerkkikäsky:

```text
whisper audio.mp3 --model medium --threads 4
```
