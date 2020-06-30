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
bowtie -v 1 -k 1 --un cleaned_reads.fastq  -f -q /appl/data/bio/biodb/production/silva reads.fastq  sRNA_rRNA_match
```

If possible, it is recommended that you use _--host_reference_ option
to filter out the sRNA originating from the host organism. This
filtering is done by running a BWA mapping against the genome of the
host organism. CSC is not maintaining BWA indexes in Taito environment.
This means that users have to do the BWA indexing for their host
organism genome before running VirusDetect.

For example for *Arabidopsis  thaliana* the required BWA indexes can be
created with commands:

    ensemblfetch arabidopsis_thaliana
    mv Arabidopsis_thaliana.TAIR10.dna.toplevel.fa a_thaliana.fa
    bwa index -p a_thaliana a_thaliana.fa

After which you can launch the virus detect job with command:

    virus_detect.pl --reference vrl_plant --host_reference a_thaliana.fa cleaned_reads.fastq

Both the Virus Detect and BWA indexing task require often significant
computing capacity. Because of that, you should use either batch jobs or
taito-shell.csc.fi environment for running Virus Detect jobs. Below is a
sample batch job file for running Virus Detect with 4 computing cores
and 8 GB of memory. The maximum running time in the job below is set to
10 hours.

 

    #!/bin/bash -l
    #SBATCH -J Virus_detect
    #SBATCH -o output_%j.txt
    #SBATCH -e errors_%j.txt
    #SBATCH -t 10:00:00
    #SBATCH -n 1
    #SBATCH --nodes=1
    #SBATCH --cpus-per-task=4
    #SBATCH -p serial
    #SBATCH --mem=8000
    #

    module load biokit

    virus_detect.pl --thread_num 4 --reference vrl_plant --host_reference a_thaliana.fa reads.fastq

The batch job file above can be submitted to the batch job system with
command:

    sbatch batch_job_file.sh

More information about running batch jobs in Taito can be found from
[Chapter 3 of the Taito user guide].

------------------------------------------------------------------------

### Discipline

Biosciences  

------------------------------------------------------------------------

### References

------------------------------------------------------------------------

### Support

------------------------------------------------------------------------

### Manual

<http://bioinfo.bti.cornell.edu/cgi-bin/virusdetect>

------------------------------------------------------------------------

  [GenBank gbvrl]: ftp://ftp.ncbi.nih.gov/genbank/
  [Velvet]: https://www.ebi.ac.uk/%7Ezerbino/velvet/
  [Chapter 3 of the Taito user guide]: https://research.csc.fi/taito-batch-jobs
