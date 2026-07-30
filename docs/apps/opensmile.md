---
tags:
  - Non-commercial
catalog:
  name: openSMILE
  description: Toolkit for extracting audio features for speech and music analysis
  license_type: Non-commercial
  disciplines:
    - Language Research and Other Digital Humanities and Social Sciences
  available_on:
    - Puhti
    - Roihu
---

# openSMILE

[openSMILE](https://www.audeering.com/research/opensmile/) (open-source Speech
and Music Interpretation by Large-space Extraction) is a toolkit for extracting
audio features. It is widely used in speech processing, affective computing and
music information retrieval to compute large feature sets from audio signals.

## Available

* Puhti: 3.0.2
* Roihu: 3.0.2

## License

openSMILE follows a dual-licensing model. The open-source version is freely
available for private, research and educational use only; commercial use
requires a separate commercial license from audEERING. See the
[openSMILE license](https://github.com/audeering/opensmile/blob/master/LICENSE)
for the current terms.

## Usage

Initialize openSMILE with:

```bash
module load openSMILE
```

The main command-line tool is `SMILExtract`, which is driven by a configuration
file describing the features to extract:

```bash
SMILExtract -C config.conf -I input.wav -O output.csv
```

You can check the version with:

```bash
SMILExtract -h
```

## More information

* [openSMILE home page](https://www.audeering.com/research/opensmile/)
* [openSMILE documentation](https://audeering.github.io/opensmile/)
* [openSMILE on GitHub](https://github.com/audeering/opensmile)
