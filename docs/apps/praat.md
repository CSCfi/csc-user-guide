---
tags:
  - Free
catalog:
  name: Praat
  description: Toolkit for annotating, processing and analysing speech and other audio samples
  license_type: Free
  disciplines:
    - Language Research and Other Digital Humanities and Social Sciences
  available_on:
    - Puhti
    - Roihu
---

# Praat

[Praat](https://www.fon.hum.uva.nl/praat/) is a toolkit for annotating,
processing and analysing speech and other audio samples. It is widely used in
phonetics and speech research for tasks such as labelling recordings, measuring
pitch, formants and intensity, and manipulating and synthesising speech.

## Available

* Puhti: 6.4
* Roihu: 6.4

## License

Praat is free software, licensed under the
[GNU General Public License, version 3 or later](https://praat.org/manual/General_Public_License__version_3.html).

## Usage

Initialize Praat with:

```bash
module load praat
```

Praat is primarily a graphical application; the best way to run it remotely is
through the [Puhti web interface remote desktop](../computing/webinterface/desktop.md).
It can also be run without a graphical interface for scripted batch processing:

```bash
praat --run script.praat
```

## More information

* [Praat home page](https://www.fon.hum.uva.nl/praat/)
* [Praat on GitHub](https://github.com/praat/praat)
* [Metadata record in the Language Bank of Finland](http://urn.fi/urn:nbn:fi:lb-2024032101)
