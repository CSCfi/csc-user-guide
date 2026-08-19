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

Bio-apps provides access to a collection of bioinformatics software modules on Roihu-CPU.

The module adds the bioinformatics application module tree to your `MODULEPATH`. After loading
`bio-apps`, you can use the normal module commands to find and load individual applications.

The `bio-apps` module does **not** load any specific bioinformatics programs into the system, it just makes them available for loading.

!!! warning "Bio-apps environment is not yet fully tested"
    Some software in the bio-apps environment are not yet fully tested, and might not
    have corresponding pages in Docs CSC yet. Use these apps with caution, and reach out to
    [CSC Service Desk](../support/contact.md) for any issues that you face.

## Available

Bio-apps is available on Roihu-CPU:

* bio-apps/v202603

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

See the sepcific application documentation for more
information about finding, loading and using individual software modules in bio-apps.

## Included applications

The collection contains applications for, among other things:

- sequence quality control and preprocessing
- sequence alignment and read mapping
- genome and transcriptome assembly
- SAM, BAM, BED and VCF processing
- variant calling
- genome annotation and gene prediction
- metagenomics and taxonomic classification
- phylogenetics and population genetics
- multiple sequence alignment
- workflow management
- access to biological sequence archives

The following modules are included in `bio-apps/v202603`:

```text
abyss/2.3.10
admixtools/8.0.2
admixture/1.4.0
angsd/0.940
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
busco/5.4.3
bwa-mem2/2.3
bwa/0.7.19
canu/2.2
cdhit/4.8.1
clustal-omega/1.2.4
clustalw/2.1
cufflinks/2.2.1
diamond/2.1.10
emboss/6.6.0
fastp/1.0.1
fastqc/0.12.1
fastx-toolkit/0.0.14
freebayes/1.3.6
gatk/4.5.0.0
hisat2/2.2.1
hmmer/3.4
htslib/1.23.1
hybpiper/2.3.4
hyphy/2.5.51hf
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
py-deeptools/3.5.3
py-htseq/2.0.3
py-ipyrad/0.9.102
py-multiqc/1.28
raxml-ng/2.0.2
raxml/8.2.12
roary/3.13.0
samtools/1.21
seqkit/2.10.0
seqtk/1.4
snakemake/9.14.0
spades/4.2.0
sra-tools/3.3.0
sratoolkit/3.0.0
star/2.7.11b
stringtie/3.0.3
tophat/2.1.2
trimmomatic/0.39
vcftools/0.1.17
vsearch/2.22.1
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
