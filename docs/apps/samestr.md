---
tags:
  - Free
catalog:
  name: SameStr
  description: Strain-level sharing analysis from metagenomic SNV profiles
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# SameStr

SameStr identifies shared microbial strains between pairs of metagenomic samples
based on the similarity of single-nucleotide-variant (SNV) profiles. It works
downstream of taxonomic profilers such as [MetaPhlAn](metaphlan.md): it takes the
per-sample marker alignments those tools produce, converts them to SNV profiles,
and calls species for which two samples share a strain.

[TOC]

## License

Free and open source under the
[GNU Affero General Public License v3](https://github.com/danielpodlesny/samestr/blob/master/LICENSE).

## Available

* Roihu-CPU: 1.2025.111 (module `py-samestr`), via the `bio-apps` module.

## Usage

SameStr is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the SameStr module:

```bash
module load bio-apps/v202603
module load py-samestr/1.2025.111
```

You can list the subcommands with:

```bash
samestr --help
```

### How it works

SameStr does not profile reads itself — it consumes the **marker alignments**
produced by MetaPhlAn (or mOTUs) and processes them through a fixed sequence of
subcommands:

| step | subcommand | purpose |
|---|---|---|
| 1 | `samestr db` | build the SameStr marker database from a MetaPhlAn marker set |
| 2 | `samestr convert` | turn MetaPhlAn `*.sam.bz2` alignments into SNV profiles |
| 3 | `samestr filter` | apply coverage / alignment thresholds |
| 4 | `samestr compare` | pairwise, clade-specific comparison of profiles |
| 5 | `samestr summarize` | call shared strains and build co-occurrence tables |

(`samestr extract` and `samestr stats` are optional helpers for adding reference
genomes and reporting coverage/diversity.)

### Reference database

`samestr db` is built from the **same MetaPhlAn marker set** that generated your
profiles — the marker-metadata `.pkl` and marker-sequence `.fna.bz2` that live in
the shared MetaPhlAn database. On Roihu that database is provided centrally and
exposed through `$METAPHLAN_DB_DIR`. That variable is set by the **MetaPhlAn
module**, so load it alongside SameStr (see the
[MetaPhlAn](metaphlan.md#database) page); pick the index you profiled against and
write the SameStr database to your own `/scratch` directory:

```bash
module load py-metaphlan/4.2.4   # provides $METAPHLAN_DB_DIR
cd /scratch/<project>/samestr_run

samestr db \
    --markers-info  $METAPHLAN_DB_DIR/mpa_vJan26_CHOCOPhlAnSGB_202605.pkl \
    --markers-fasta $METAPHLAN_DB_DIR/mpa_vJan26_CHOCOPhlAnSGB_202605_SGB.fna.bz2 \
    --db-version "$METAPHLAN_DB_DIR/mpa_latest"
    --output-dir    samestr_db/
```

!!! important "Keep the database version consistent"
    The MetaPhlAn index you use for `samestr db` **must** match the one used to
    produce the alignments in the next step. Mixing marker versions gives
    meaningless comparisons.

### Producing the input alignments

SameStr's input is the SAM output of a MetaPhlAn run. Add MetaPhlAn's `-s`
(`--samout`) option so it writes a `*.sam.bz2` alignment per sample, using the
matching index:

```bash
module load py-metaphlan/4.2.4
metaphlan sample1.fastq.gz --input_type fastq \
    --index mpa_vJan26_CHOCOPhlAnSGB_202605 \
    --nproc 8 \
    -s out_align/sample1.sam.bz2 \
    -o out_profile/sample1_profile.txt
```

### Example pipeline

Run SameStr from a working directory on **`/scratch`**. It parallelises with
`--nprocs`, so an [interactive session](../computing/running/interactive-usage.md)
or a `small`-partition batch job fits well. Starting from the alignments in
`out_align/` and the database in `samestr_db/`:

```bash
module load bio-apps/v202603 py-samestr/1.2025.111

samestr convert \
    --input-files out_align/*.sam.bz2 \
    --marker-dir  samestr_db/ \
    --nprocs 8 --min-vcov 5 \
    --output-dir out_convert/

samestr merge \
    --input-files out_convert/*.npy \
    --marker-dir samestr_db/ \
    --nprocs 8 \
    --output-dir out_merge/

samestr filter \
    --input-files out_merge/*.npy \
    --input-names out_merge/*.names.txt \
    --marker-dir  samestr_db/ \
    --nprocs 8 \
    --output-dir out_filter/

samestr compare \
    --input-files out_filter/*.npy \
    --marker-dir  samestr_db/ \
    --output-dir out_compare/

samestr summarize \
    --input-dir  out_compare/ \
    --marker-dir samestr_db/ \
    --output-dir out_summarize/
```

The shared-strain calls and co-occurrence tables are written to `out_summarize/`.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [SameStr on GitHub](https://github.com/danielpodlesny/samestr)
* [SameStr publication (Podlesny et al. 2022)](https://doi.org/10.1186/s40168-022-01251-w)
