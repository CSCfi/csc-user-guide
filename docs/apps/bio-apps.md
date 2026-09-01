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

!!! warning "Bio-apps environment is not yet fully tested"
    Some software in the bio-apps environment is not yet fully tested, and might not
    have a corresponding page in Docs CSC yet. Use these apps with caution, and reach out to
    [CSC Service Desk](../support/contact.md) for any issues that you face.

## Available

Bio-apps is available on Roihu:

* `bio-apps/v202603`

The same `bio-apps/v202603` command works on both **CPU** and **GPU (GH200)** nodes.
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

The following modules are included in `bio-apps/v202603` on Roihu **CPU** nodes:

```text
abyss/2.3.10
admixtools/8.0.2
admixture/1.4.0
angsd/0.940
antismash/8.0.4
astral/5.7.1
augustus/3.5.0
bamtools/2.5.2
barrnap/0.9
bbmap/39.59
bcftools/1.23.1
beast2/2.6.7
bedops/2.4.42
bedtools2/2.31.1
blast-plus/2.17.0
boost/1.86.0
bowtie/1.3.1
bowtie2/2.5.4
bracken/2.9
braker4/0.5.0-beta
busco/5.4.3
busco/6.1.0
bwa/0.7.19
bwa-mem2/2.3
canu/2.2
cdhit/4.8.1
checkm2/1.1.0
clumpp/1.1.2
clustal-omega/1.2.4
clustalw/2.1
cufflinks/2.2.1
diamond/2.1.10
eggnog-mapper/2.1.15
emboss/6.6.0
exonerate/2.4.0
fastp/1.0.1
fastqc/0.12.1
fastx-toolkit/0.0.14
freebayes/1.3.6
gapseq/2.1.0
gatk/4.5.0.0
getorganelle/1.7.7.0
getorganelle/1.7.7.1
hisat2/2.2.1
hmmer/3.4
htslib/1.23.1
humann/4.0.0a2
hybpiper/2.3.4
hyphy/2.5.51hf
igv/2.19.7
iq-tree/2.4.0
jellyfish/2.2.7
kraken2/2.17.1
mafft/7.525
mash/2.3
megahit/1.2.9
meme/5.5.7
metabat/2.15
minimap2/2.30
mmseqs2/18-8cc5c
mothur/1.48.0
mrbayes/3.2.7a
mummer4/4.0.1
muscle/3.8.31
muscle5/5.1.0
ncbi-toolkit/28_0_12
nextflow/25.10.2-standalone
openmpi/5.0.10-gcc14.3.0
perl-bioperl/1.7.8
phylip/3.697
picard/3.3.0
plink/1.07
plink2/2.0.0-a.6.9
prodigal/2.6.3
py-biopython/1.85
py-cutadapt/4.7
py-dbcan/5.2.9
py-deeptools/3.5.3
py-htseq/2.0.3
py-instrain/1.6.3
py-ipyrad/0.9.102
py-metaphlan/4.2.4
py-micom/0.39.0
py-multiqc/1.28
py-steadiercom/0.1.5
raxml/8.2.12
raxml-ng/2.0.2
roary/3.13.0
samtools/1.21
seqkit/2.10.0
seqtk/1.4
snakemake/7.32.4
snakemake/9.14.0
sortmerna/7.0.0
spades/4.2.0
sra-tools/3.3.0
sratoolkit/3.0.0
star/2.7.11b
strauto/1.0
stringtie/3.0.3
structure/2.3.4
structureharvester/0.7
tophat/2.1.2
trimmomatic/0.39
trinity/2.15.1.FULL
vcftools/0.1.17
vsearch/2.22.1
```

### GPU nodes (GH200)

On Roihu **GPU** nodes, `bio-apps/v202603` provides a small set of
GPU-accelerated tools:

```text
dorado/2.1.1
mmseqs2/18-8cc5c
nextflow/25.10.2-standalone
py-medaka/2.2.2
snakemake/7.32.4
snakemake/9.14.0
```

## License

The applications included in Bio-apps are distributed under their own
licenses. Most are free and open-source software, but license and citation
requirements differ between applications.

Consult the documentation and license information of each application before
using or redistributing it.

## Citation

See above. See each application page for citation guidelines.

## Support

Application-specific usage instructions will be made available on the corresponding
page in the [CSC application catalog](by_discipline.md#biosciences).

For problems related to the Bio-apps module tree or an included application,
[contact CSC Service Desk](../support/contact.md).
