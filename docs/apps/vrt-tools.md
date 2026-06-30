---
tags:
  - Free
catalog:
  name: vrt-tools
  description: Tools for converting VRT (Vertical Text) corpus files
  license_type: Free
  disciplines:
    - Language Research and Other Digital Humanities and Social Sciences
  available_on:
    - Puhti
    - Roihu
---

# vrt-tools

vrt-tools is a collection of tools for working with VRT (Vertical Text) format
corpus files. It currently contains a single tool, `vrt-to-json`, which converts
VRT files into JSON.

`vrt-to-json` reads VRT input where field names for token lines are given in
special comments, and where the `text`, `paragraph` and `sentence` levels of
structure are properly nested. It writes the data out as JSON objects, with each
token becoming a JSON object of named fields (or an array of values in
positional mode). The output can be split into a hierarchy of files with a token
limit per file.

## Available

* Puhti: 1.0
* Roihu: 1.0

## License

vrt-tools is open source, licensed under the MIT License.

## Usage

Initialize vrt-tools with:

```bash
module load vrt-tools
```

Convert a VRT file into JSON, splitting the output into numbered files of about
one million tokens each:

```bash
vrt-to-json --out=/path/to/##/part-##.json --limit=1000000 --nat=ref,dephead input.vrt
```

The `#` characters in the output path are replaced with counter digits. Multiple
VRT files can also be concatenated into a single JSON object via standard input.

## More information

* [vrt-to-json source and documentation](https://github.com/CSCfi/Kielipankki-utilities/tree/master/json)
