---
tags:
  - Free
---

# VirusDetect

VirusDetect is a software for analyzing large-scale sRNA datasets for
virus identification. The program performs reference-guided assembly by
aligning sRNA reads to the known virus reference database (GenBank
gbvrl) as well as *de novo* assembly using _Velvet_ with automated
parameter optimization. The assembled contigs are compared to the
reference virus sequences for virus identification. The contigs were
treated as undetermined contigs if they are not hit to any known
viruses. The siRNA profile of these undetermined contigs are provided as
guidance to discovery novel viruses which do not show sequence
similarity with known viruses.

[TOC]

## License

Developers state that the software is free to use and open source, but no specific
license is specified.

## Available

* Puhti: 1.7, 1.8
* Chipster graphical user interface

## Usage

To use VirusDetect on Puhti, you first need to load `biokit` and `virusdetect` modules.

```bash
module load biokit
module load virusdetect
```

After that, you can start VirusDetect with the command `virus_detect.pl`.
For example:

```bash
virus_detect.pl --reference vrl_plant reads.fastq
```

The developers of VirusDetect recommend removing ribosomal RNA (rRNA)
sequences from the input sequences before running VirusDetect. This can
be done by aligning the sRNA reads against Silva rRNA database using
Bowtie. On Puhti, the Silva database is available in path:

```bash
/appl/data/bio/biodb/production/silva/Silva_rRNA_database
```

The actual cleaning command could look like:

```bash
bowtie -v 1 -k 1 --un cleaned_reads.fastq -f -q /appl/data/bio/biodb/production/silva/Silva_rRNA_database reads.fastq sRNA_rRNA_match
```

If possible, it is recommended that you use `--host_reference` option
to filter out the sRNA originating from the host organism. This
filtering is done by running a BWA mapping against the genome of the
host organism. CSC does not maintain BWA indexes on Puhti,
but you can use `chipster_genomes` to retrieve BWA indexes used by the 
Chipster service.

```bash
chipster_genomes bwa
```

The command above lists the available indexes and asks you to pick one.
If a suitable species is not available, then you need to do indexing for their host
organism genome before running VirusDetect.

For example, for _Triticum aestivum_, the required BWA indexes can be
created with the commands:

```bash
ensemblfetch.sh triticum_aestivum
mv Triticum_aestivum.IWGSC.dna.toplevel.fa triticum_aestivum.fa
bwa index -p triticum_aestivum triticum_aestivum.fa
```

Note that generating BWA indexes for plant genomes can take several hours.

Once you have the BWA index for the host genome available, you can launch the VirusDetect job with the command:

```bash
virus_detect.pl --reference vrl_plant --host_reference triticum_aestivum.fa cleaned_reads.fastq
```

VirusDetect is mainly used for detecting plant viruses (`vrl_plant`), but you can use it for other viruses too. The `--reference` option defines the
reference virus sequence dataset to be used. The available reference datasets are:

```text
vrl_algae
vrl_bacteria
vrl_fungus
vrl_invertebrates
vrl_plants
vrl_vertebrates
```

Both the VirusDetect and BWA indexing tasks often require significant
computing capacity. Because of that, you should use batch jobs for 
running VirusDetect jobs. Below is a
sample batch job file for running VirusDetect with 8 computing cores
and 8 GB of memory. The maximum running time in the job below is set to
10 hours.
 
```bash
#!/bin/bash -l
#SBATCH --job-name=VirusDetect
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --account=your_project_name
#SBATCH --time=10:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
#SBATCH --partition=small
#SBATCH --mem=8000

module load biokit
module load virusdetect

virus_detect.pl --thread_num 8 --reference vrl_plants --host_reference triticum_aestivum.fa reads_123.fastq
```

The batch job file above can be submitted to the batch job system with the
command:

```bash
sbatch batch_job_file.sh
```

More information about running batch jobs on Puhti can be found from the
[batch job instruction pages](../computing/running/getting-started.md).

VirusDetect writes the analysis results to a new directory, named after the query dataset `result_<queryfile>`. VirusDetect produces a large number of result files. The most essential files are:

* `blastn.html` Table listing reference viruses that have corresponding virus contigs identified by BLASTN.
* `blastx.html` Table listing reference viruses that have corresponding virus contigs identified by BLASTX. 
* `<query>.blastn.xls` Table of BLASTN matches to the reference virus database.
* `<query>.blastx.xls` Table of BLASTX matches to the reference virus database.
* `undetermined.html` Table listing the length, siRNA size distribution and 21-22nt percentage of undetermined contigs. Potential virus contigs (21-22 nt > 50%) are indicated in green.
* `undetermined_blast.html` Table listing contigs having hits in the virus reference database but not assigned to any reference viruses because they did not meet the coverage or depth criteria.

As many of the output files are in HTML format, it may be difficult to study them on Puhti.
One option to study the results is to move them to a public bucket on Allas. For example
(replace `projnum` with your own project number):

```bash
module load allas
allas-conf
rclone copy -P results_cleaned_reads.fastq allas:virusdetect_projnum/results_cleaned_reads.fastq/
a-publish -b virusdetect_projnum -index dynamic
```

Now you can study the results with your browser in URL:

```bash
https://a3s.fi/virusdetect_projnum/index.html
```

## More information

* [VirusDetect home page](http://virusdetect.feilab.net/cgi-bin/virusdetect/index.cgi)
