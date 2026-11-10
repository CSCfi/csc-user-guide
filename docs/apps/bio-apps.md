---
tags:
  - Free
catalog:
  name: Bio-apps
  description: Access module to a collection of applications and software often used in biosciences
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Bio-apps

Bio-apps provides access to a large collection of bioinformatics applications on
Roihu, installed as environment modules. It is the successor to the `biokit`
collection on the decommissioned Puhti and Mahti systems.

Bio-apps is **opt-in**: loading the `bio-apps` module adds the bioinformatics
application module tree to your `MODULEPATH`, after which you can find and load
individual applications with the normal module commands. Loading `bio-apps` does
**not** load any application itself — it only makes them available for loading.

!!! info "Not all bioinformatics tools are in bio-apps"
    The applications in bio-apps are installed with [Spack](https://spack.io/). Some
    tools are better suited to being installed as
    [containers](../computing/containers/overview.md) or with
    [Tykky](../computing/containers/tykky.md). These are provided as separate modules
    outside bio-apps, and you do not need to load `bio-apps` to use them. See the
    application's page in the [CSC application catalog](by_discipline.md#biosciences)
    for how to load it.

## Available

Bio-apps is available on Roihu:

* `bio-apps/v202603`

The same `bio-apps/v202603` module works on both **CPU** and **GPU (GH200)** nodes.
The node you are on selects the matching software: a broad set of applications on
CPU nodes, and a small set of GPU-accelerated tools on GPU nodes.

## Usage

Load the bioinformatics application module tree with:

```bash
module load bio-apps/v202603
```

Loading `bio-apps` makes the application modules available, but does not load
the applications themselves.

List the available bioinformatics modules with:

```bash
module avail
```

Search for a particular application with `module spider`. For example:

```bash
module spider samtools
```

Load the required application after loading bio-apps:

```bash
module load samtools/1.21
```

You can then use the application normally:

```bash
samtools --version
```

To remove an application from your environment, unload its module:

```bash
module unload samtools
```

When you no longer need the bioinformatics module tree, unload `bio-apps`:

```bash
module unload bio-apps
```

See the specific application documentation for more
information about finding, loading and using individual software modules in bio-apps.

## Included applications

The collection contains applications for, among other things:

* sequence quality control and preprocessing
* sequence alignment and read mapping
* genome and transcriptome assembly
* SAM, BAM, BED and VCF processing
* variant calling
* genome annotation and gene prediction
* metagenomics and taxonomic classification
* phylogenetics and population genetics
* multiple sequence alignment
* workflow management
* access to biological sequence archives

### CPU nodes

The following modules are included in `bio-apps/v202603` on Roihu **CPU** nodes.
Each entry shows the module name and its versions; load a version with
`module load <name>/<version>`. Names with a link have a documentation page.

<div class="tool-columns" markdown>

- [abyss](abyss.md) 2.3.10
- [admixtools](admixtools.md) 8.0.2
- [admixture](admixture.md) 1.4.0
- [angsd](angsd.md) 0.940
- [antismash](antismash.md) 8.0.4
- [aster](aster.md) 1.25
- [astral](astral.md) 5.7.1
- [augustus](augustus.md) 3.5.0
- [bamtools](bamtools.md) 2.5.2
- [barrnap](barrnap.md) 0.9
- [basespace-cli](bs.md) 1.7.1
- [bayescan](bayescan.md) 2.1
- [bbmap](bbmap.md) 39.59
- [bcftools](bcftools.md) 1.23.1, 1.24
- beast2 2.6.7
- [bedops](bedops.md) 2.4.42
- [bedtools2](bedtools2.md) 2.31.1
- [blast-plus](blast.md) 2.17.0
- [bowtie](bowtie.md) 1.3.1
- [bowtie2](bowtie2.md) 2.5.4
- [bracken](bracken.md) 2.8, 2.9
- [braker4](braker.md) 0.5.0-beta
- [busco](busco.md) 5.4.3, 6.1.0
- [bwa](bwa.md) 0.7.19
- [bwa-mem2](bwa-mem2.md) 2.3
- [canu](canu.md) 2.2
- [cdhit](cd-hit.md) 4.8.1
- [checkm2](checkm2.md) 1.1.0
- [clumpp](clumpp.md) 1.1.2
- [clustal-omega](clustal-omega.md) 1.2.4
- [clustalw](clustalw.md) 2.1
- [comebin](comebin.md) 1.1.0
- [cufflinks](cufflinks.md) 2.2.1
- [demix-check](demix-check.md) 1.0.20250120
- [diamond](diamond.md) 2.1.10
- [eggnog-mapper](eggnog-mapper.md) 2.1.15
- [emboss](emboss.md) 6.6.0
- [entrezdirect](edirect.md) 26.6.20261102
- [exonerate](exonerate.md) 2.4.0
- [famsa](famsa.md) 2.5.2
- [fastp](fastp.md) 1.0.1, 1.3.6
- [fastqc](fastqc.md) 0.12.1
- [fastx-toolkit](fastx-toolkit.md) 0.0.14
- [freebayes](freebayes.md) 1.3.6
- [gapseq](gapseq.md) 2.1.0
- [gatk](gatk.md) 4.5.0.0, 4.7.0.0
- [genomescope2](genomescope2.md) 2.1.0
- [getorganelle](getorganelle.md) 1.7.7.1
- [gone2](gone2.md) 2.0.2
- [hifiasm](hifiasm.md) 0.25.0
- [hisat2](hisat2.md) 2.2.1
- [hmmer](hmmer.md) 3.4
- [humann](humann.md) 3.9, 4.0.0a2
- [hybpiper](hybpiper.md) 2.3.4
- [hyphy](hyphy.md) 2.5.51hf
- [igv](igv.md) 2.19.7
- [interproscan](interpro.md) 5.76-107.0
- [iq-tree](iq-tree.md) 2.4.0
- [iqtree3](iq-tree.md) 3.1.4
- [jellyfish](jellyfish.md) 2.2.7
- [kraken2](kraken.md) 2.17.1, 2.17.2
- [mafft](mafft.md) 7.525
- [magscot](magscot.md) 1.1
- [mash](mash.md) 2.3
- [megahit](megahit.md) 1.2.9
- [meme](meme.md) 5.5.7
- [metabat](metabat.md) 2.15
- [minibwa](minibwa.md) 0.7
- [minimap2](minimap2.md) 2.30
- [mmseqs2](mmseqs2.md) 18-8cc5c
- [mothur](mothur.md) 1.48.0
- [mrbayes](mrbayes.md) 3.2.7a
- [mummer4](mummer4.md) 4.0.1
- [muscle](muscle.md) 3.8.31
- [muscle5](muscle5.md) 5.1.0
- [ncbi-toolkit](ncbi-toolkit.md) 28_0_12
- [nextflow](nextflow.md) 25.10.2-standalone, 26.04.6-standalone
- [ngs-primerplex](ngs-primerplex.md) 1.3.4
- [perl-bioperl](bioperl.md) 1.7.8
- [phylip](phylip.md) 3.697
- [phylonet](phylonet.md) 3.8.5
- [phyparts](phyparts.md) 0.0.1
- [picard](picard.md) 3.3.0
- [plink](plink.md) 1.9.0
- [plink2](plink.md) 2.0.0-a.6.9, 2.0.0-b.1.3
- [prodigal](prodigal.md) 2.6.3
- [prokka](prokka.md) 1.15.6
- [py-bakta](bakta.md) 1.11.4
- [py-biopython](biopython.md) 1.85
- [py-clipkit](clipkit.md) 2.12.1, 2.14.0
- [py-concoct](concoct.md) 1.1.0
- [py-cutadapt](cutadapt.md) 4.7, 5.1, 5.2
- [py-dbcan](dbcan.md) 5.2.9
- [py-deeptools](deeptools.md) 3.5.3
- [py-fdstools](fdstools.md) 2.2.1
- [py-gtdbtk](gtdbtk.md) 2.7.2
- [py-htseq](htseq.md) 2.0.3, 2.1.2
- [py-instrain](instrain.md) 1.6.3
- [py-ipyrad](ipyrad.md) 0.9.102
- [py-macs2](macs2.md) 2.2.9.1
- [py-macs3](macs2.md) 3.0.4, 3.1.0
- [py-metaphlan](metaphlan.md) 4.2.4
- [py-micom](micom.md) 0.39.0
- [py-multiqc](multiqc.md) 1.28, 1.35
- [py-phykit](phykit.md) 2.1.94, 2.8.0
- [py-samestr](samestr.md) 1.2025.111
- [py-semibin](semibin.md) 2.6.0
- [py-steadiercom](steadiercom.md) 0.1.5
- [raxml](raxml.md) 8.2.12
- [raxml-ng](raxml-ng.md) 2.0.2
- [revbayes](revbayes.md) 1.4.1
- [roary](roary.md) 3.13.0
- [salmon](salmon.md) 2.8.0
- [sambamba](sambamba.md) 1.0.1
- [samtools](samtools.md) 1.21, 1.24
- [sanspanz](pannzer.md) 3.20250512
- [seqkit](seqkit.md) 2.10.0, 2.13.0
- [seqtk](seqtk.md) 1.4
- [snakemake](snakemake.md) 7.32.4, 9.14.0
- [sortmerna](sortmerna.md) 7.0.0
- [spades](spades.md) 4.2.0, 4.3.0
- [sra-tools](sra-tools.md) 3.3.0
- [star](star.md) 2.7.11b
- [strauto](strauto.md) 1.0
- [stringtie](stringtie.md) 3.0.3
- [structure](structure.md) 2.3.4
- [structureharvester](structureharvester.md) 0.7
- [tophat](tophat.md) 2.1.2
- [transdecoder](transdecoder.md) 5.7.1
- [treemix](treemix.md) 1.13
- [trimmomatic](trimmomatic.md) 0.39
- [trinity](trinity.md) 2.15.1.FULL, 2.15.2.FULL
- [trinotate](trinotate.md) 4.0.2
- [vcftools](vcftools.md) 0.1.17
- [vsearch](vsearch.md) 2.22.1
- [wtdbg2](wtdbg2.md) 2.5
- [xhmm](xhmm.md) 20160104
- [yak](yak.md) 0.1

</div>

### GPU nodes (GH200)

On Roihu **GPU** nodes, `bio-apps/v202603` provides a small set of
GPU-accelerated tools:

<div class="tool-columns" markdown>

- [comebin](comebin.md) 1.1.0
- [dorado](dorado.md) 2.1.1
- [foldseek](foldseek.md) 10-941cd33
- [mhm2](mhm2.md) 2.2.2.0-20260904
- [mmseqs2](mmseqs2.md) 18-8cc5c
- [mrbayes](mrbayes.md) 3.2.8
- [nextflow](nextflow.md) 25.10.2-standalone, 26.04.6-standalone
- [py-medaka](medaka.md) 2.2.2
- [snakemake](snakemake.md) 7.32.4, 9.14.0

</div>

## License

The applications included in Bio-apps are distributed under their own
licenses. Most are free and open-source software, but license and citation
requirements differ between applications.

Consult the documentation and license information of each application before
using or redistributing it.

## Citation

See each application's page for citation guidelines.

## Support

Usage instructions are on each application's page, linked in the lists above and in
the [CSC application catalog](by_discipline.md#biosciences).

For problems related to the Bio-apps module tree or an included application,
[contact CSC Service Desk](../support/contact.md).

<style>
.tool-columns > ul {
  columns: 16rem auto;
  column-gap: 2rem;
}
.tool-columns li {
  break-inside: avoid;
}
</style>
