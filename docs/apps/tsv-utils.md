---
tags:
  - Free
catalog:
  name: eBay's tsv-utils
  description: Utilities for manipulating large tabular data files
  license_type: Free
  disciplines:
    - Language Research and Other Digital Humanities and Social Sciences
  available_on:
    - Puhti
    - Roihu
---

# eBay's tsv-utils

[eBay's tsv-utils](https://github.com/eBay/tsv-utils) is a collection of
command-line utilities for manipulating large tabular data files, such as
tab-separated value (TSV) and CSV files. The tools are designed for filtering,
summarising, joining and otherwise processing large data files efficiently.

## Available

* Puhti: 2.2.0
* Roihu: 2.2.0

## License

eBay's tsv-utils is open source, licensed under the
[Boost Software License 1.0](https://github.com/eBay/tsv-utils/blob/master/LICENSE.txt).

## Usage

Initialize the tools with:

```bash
module load tsv-utils
```

The collection includes commands such as `tsv-filter`, `tsv-select`,
`tsv-summarize` and `csv2tsv`. For example, to keep rows where the third column
is greater than 100:

```bash
tsv-filter --gt 3:100 input.tsv
```

## More information

* [tsv-utils on GitHub](https://github.com/eBay/tsv-utils)
* [tsv-utils documentation](https://github.com/eBay/tsv-utils/blob/master/docs/ToolReference.md)
* [Metadata record in the Language Bank of Finland](http://urn.fi/urn:nbn:fi:lb-202006081)
