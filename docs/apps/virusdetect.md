# VirusDetect

## Description

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


## Available


*   Version 1.7  is available in Puhti and in Chipster


### Usage

To use VirusDetect in Puhti you first need to load _biokit_ and _virusdetect_ modules.
```text
module load biokit
module load virusdetect
```
After that you can start Virus Detect with command `virus_detect.pl`.
For example:
```text
virus_detect.pl --reference vrl_plant reads.fastq
```
The developers of VirusDetect recommend to remove ribosomal RNA (rRNA)
sequences from the input sequences before running VirusDetect. This can
be done by aligning the sRNA reads against Silva rRNA database using
Bowtie. In Taito the Silva database is available in path:

```text
/appl/data/bio/biodb/production/silva/Silva_rRNA_database
```    

The actual clening command could look like:
```text
bowtie -v 1 -k 1 --un cleaned_reads.fastq  -f -q /appl/data/bio/biodb/production/silva/Silva_rRNA_database reads.fastq  sRNA_rRNA_match
```

If possible, it is recommended that you use _--host_reference_ option
to filter out the sRNA originating from the host organism. This
filtering is done by running a BWA mapping against the genome of the
host organism. CSC is not maintaining BWA indexes in Puhti environment,
but you can use `chipster_genomes` to retriew bwa indexes used by the Chipster service.

```text
chipster_genomes bwa
```
The command above lists the available indexes and asks you to pick one.
If a suitable species is not available, then you need to do indexing for their host
organism genome before running VirusDetect.

For example for _Triticum aestivum_ the required BWA indexes can be
created with commands:
```text
ensemblfetch.sh triticum_aestivum
mv Triticum_aestivum.IWGSC.dna.toplevel.fa triticum_aestivum.fa
bwa index -p triticum_aestivum triticum_aestivum.fa
```
Note that generating BWA indexes for plant genomes can take several hours.

After which you can launch the virus detect job with command:

```text
virus_detect.pl --reference vrl_plant --host_reference a_thaliana.fa cleaned_reads.fastq
```

VirusDetect is mainly used for detecting plant viruses (_vrl_plant_), but you can use it for other viruses too. The `--reference` option defines the
reference virus sequence dataset to be used. The available rederence datasets are:
```text
vrl_algae
vrl_bacteria
vrl_fungus
vrl_invertebrate
vrl_plant
vrl_vertebrate
```

Both the Virus Detect and BWA indexing task require often significant
computing capacity. Because of that, you should use batch jobs for 
running Virus Detect jobs. Below is a
sample batch job file for running Virus Detect with 8 computing cores
and 8 GB of memory. The maximum running time in the job below is set to
10 hours.

 
```text
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
#

module load biokit
module load virusdetect

virus_detect.pl --thread_num 8 --reference vrl_plant --host_reference a_thaliana.fa reads.fastq
```

The batch job file above can be submitted to the batch job system with
command:
```text
sbatch batch_job_file.sh
```
More information about running batch jobs in Puhti can be found from
[batch job instruction pages](../computing/running/getting-started.md).



### More information

*   [VirusDetect home page](http://bioinfo.bti.cornell.edu/cgi-bin/virusdetect)

