---
tags:
  - Non-commercial
catalog:
  name: UDPipe
  description: Trainable pipeline for tokenization, tagging, lemmatization and dependency parsing
  license_type: Non-commercial
  disciplines:
    - Language Research and Other Digital Humanities and Social Sciences
  available_on:
    - Puhti
    - Roihu
---

# UDPipe

[UDPipe](https://ufal.mff.cuni.cz/udpipe/1) is a trainable pipeline for
tokenization, tagging, lemmatization and dependency parsing of natural language
text. It is developed at the Institute of Formal and Applied Linguistics (ÚFAL),
Charles University, and works with pre-trained models for the
[Universal Dependencies](https://universaldependencies.org/) treebanks, covering
a wide range of languages.

## Available

* Puhti: 1.4.0
* Roihu: 1.4.0

## License

The UDPipe software is licensed under the
[Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/). The
pre-trained language models are distributed under the
[CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) license and
are therefore restricted to **non-commercial use**; some models may carry
additional conditions from their original training data.

## Usage

Initialize UDPipe with:

```bash
module load udpipe
```

The pre-trained models are available in the `$UD_MODELS` directory. List the
installed models with:

```bash
ls $UD_MODELS
```

To tag and parse text, give UDPipe a model file and the input. For example, to
process Finnish text given one sentence per line (horizontal input):

```bash
echo "Hän istuu." | udpipe --tag --parse --input=horizontal --immediate \
  $UD_MODELS/finnish-ftb-ud-2.5-191206.udpipe
```

## More information

* [UDPipe 1 user's manual](https://ufal.mff.cuni.cz/udpipe/1/users-manual)
* [UDPipe home page](https://ufal.mff.cuni.cz/udpipe/1)
* [Metadata record in the Language Bank of Finland](http://urn.fi/urn:nbn:fi:lb-201902131)
