---
tags:
  - Free
---

# InterProScan



InterProScan is a tool that compares protein or nucleotide sequence against a set of protein signature databases.
The results obtained from different databases are given in uniform format. The InterProScan5 installation at CSC can
be used to search protein signatures from following databases:

   * TIGRFAM (15.0)
   * SFLD (4)
   * SUPERFAMILY (1.75)
   * PANTHER (15.0)
   * Gene3D (4.3.0)
   * Hamap (2020_05)
   * Coils (2.2.1)
   * ProSiteProfiles (2021_01)
   * SMART (7.1)
   * CDD (3.18)
   * PRINTS (42.0)
   * PIRSR (2021_05)
   * ProSitePatterns (2021_01)
   * AntiFam (7.0)
   * Pfam (34.0)
   * MobiDBLite (2.0)
   * PIRSF (3.10)


## License

Free to use and open source under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Available

*   Puhti: 5.55-88.0, 5.67-90.0

## Usage

In Puhti, first load interproscan module with commands:

```bash
module load biokit
module load interproscan
```

After that you can submit  InterProScan jobs using command `cluster_interproscan`. Cluster_interproscan
is a help tool that automatically runs your InterProScan task using the batch job system of Puhti.
If your query file contains several sequences the cluster_interproscan tool also automatically splits
the InterProScan tasks to several subtasks that are run simultaneously in Puhti.

cluster_interproscan accepts all the normal InterProScan options. To check the available options, give command:

```bash
cluster_interproscan -h
```

Below is two sample InterProScan commands

1. Running InterProScan search for a nucleotide sequence set  against all InterProScan databases.
Results are reported in XML format.

```bash
cluster_interproscan -i nucleotides.fasta -o results.xml -f XML -t n
```

2. Running InterProScan search for protein sequence set against PfamA databases. Results are reported in GFF3 format. GFF3 conversion needs more memory that what is available in the login nodes of Puhti. Because of that you should submit the interporosacn task from an interactive batch job with least 4 GiB of memory reserved.

```bash
sinteractive -m 4000
cluster_interproscan -i proteins.fasta -o results.gff3 -f GFF3 -appl PfamA
```


## More information

*   [InterPro home page](https://www.ebi.ac.uk/interpro/)
