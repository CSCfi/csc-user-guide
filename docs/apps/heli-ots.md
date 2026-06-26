---
tags:
  - Free
catalog:
  name: HeLI-OTS
  description: Off-the-shelf language identifier with language models for 220 languages
  license_type: Free
  disciplines:
    - Language Research and Other Digital Humanities and Social Sciences
  available_on:
    - Puhti
    - Roihu
---

# HeLI-OTS

[HeLI-OTS](https://github.com/tosaja/HeLI) (Helsinki Language Identification
method — Off-The-Shelf) is a language identifier that detects which language a
text is written in. It ships with language models for 220 languages, identified
by their ISO 639-3 codes, and can process on the order of hundreds to over a
thousand sentences per second on a single CPU core.

## Available

* Puhti: 2.0
* Roihu: 2.0

## License

HeLI-OTS is licensed under the
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
license. If you use it in academic work, please cite:

> Tommi Jauhiainen, Heidi Jauhiainen and Krister Lindén (2022). HeLI-OTS,
> Off-the-shelf Language Identifier for Text. *Proceedings of the Language
> Resources and Evaluation Conference (LREC 2022)*, pages 3912–3922.

## Usage

Initialize HeLI-OTS with:

```bash
module load heliots
```

HeLI-OTS is a Java application; on CSC systems the module provides a `heliots`
wrapper command. It reads text from an input file and writes the identified
language for each line to an output file:

```bash
heliots -r input.txt -w output.txt
```

Useful options include `-c` (confidence scores), `-t` (several ranked language
guesses), `-l` (restrict to a subset of languages) and `-s` (language-set
detection). Once the module is loaded, run `module help heliots` for the details
of the CSC installation.

## More information

* [HeLI-OTS 2.0 on Zenodo](https://zenodo.org/records/10907468)
* [HeLI-OTS on GitHub](https://github.com/tosaja/HeLI)
* [HeLI-OTS in the Language Bank of Finland](https://www.kielipankki.fi/tools/heli-ots/)
* [Metadata record in the Language Bank of Finland](http://urn.fi/urn:nbn:fi:lb-2024040301)
