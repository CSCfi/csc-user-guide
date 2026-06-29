---
tags:
  - Free
catalog:
  name: trankit
  description: Transformer-based Python toolkit for multilingual Natural Language Processing (NLP)
  license_type: Free
  disciplines:
    - Language Research and Other Digital Humanities and Social Sciences
  available_on:
    - Puhti
    - Roihu
---

# trankit

[trankit](https://github.com/nlp-uoregon/trankit) is a light-weight
transformer-based Python toolkit for multilingual Natural Language Processing
(NLP). It provides trainable pipelines for fundamental NLP tasks such as
sentence segmentation, tokenization, part-of-speech tagging, morphological
feature tagging, lemmatization and dependency parsing across many languages.

## Available

* Puhti: 1.1.0
* Roihu: 1.1.0

## License

trankit is open source, licensed under the
[Apache License 2.0](https://github.com/nlp-uoregon/trankit/blob/master/LICENSE).

## Usage

Initialize trankit with:

```bash
module load trankit
```

On CSC systems trankit is run from the command line with `python -m trankit`. It
parses plain text files (UTF-8) from a flat input directory and writes one JSON
output file per input file into an empty output directory. Three input formats
are supported: `plaindoc` (plain text), `plainsen` (one sentence per line) and
`pretok` (pretokenized, one token per line, sentences separated by blank lines).

The shared language models are provided in the `$LB_MODELS` directory. For
example, to parse Finnish text:

```bash
python -m trankit --input /directory/with/input/files \
  --output_dir /directory/with/output/files \
  --input_format plaindoc \
  --cache_dir $LB_MODELS \
  --lang finnish
```

trankit produces JSON output. The companion script `trankit2conllu` converts it
to CoNLL-U format:

```bash
trankit2conllu --input /path/to/trankit/output \
  --output_dir /path/to/conllu-output
```

For more help once the module is loaded, run `module help trankit`. trankit can
also be used as a Python library; see the upstream documentation.

## More information

* [trankit on GitHub](https://github.com/nlp-uoregon/trankit)
* [trankit documentation](https://trankit.readthedocs.io/)
* [Metadata record in the Language Bank of Finland](http://urn.fi/urn:nbn:fi:lb-2026011401)
