# InterProScan

## Description

InterProScan is a tool that compares protein or nucleotide sequence against a set of protein signature databases. 
The results obtained from different databases are given in uniform format. The InterProScan5 installation at CSC can 
be used to search protein signatures from following databases:

    TIGRFAM
    PIRSF
    ProDom
    SMART
    PrositeProfiles
    PrositePatterns
    HAMAP
    PfamA
    PRINTS
    SuperFamily
    Coils
    Gene3d
    
## Version

*   InterProScan version 5.47-82.0 is available in Puhti

## Usage 

In Puhti, first load interproscan module with commands:
```text
module load biokit
module load interproscan
```

After that you can submit  InterProScan jobs using command `cluster_interproscan`. Cluster_interproscan 
is a help tool that automatically runs your InterProScan task using the batch job system of Puhti. 
If your query file contains several sequences the cluster_interproscan tool also automatically splits 
the InterProScan tasks to several subtasks that are run simultaneously in Puhti. 

cluster_interproscan accepts all the normal InterProScan options. To check the available options, give command:

```text
cluster_interproscan -h
```

Below is two sample InterProScan commands

1. Running InterProScan search for a nucleotide sequence set  against all InterProScan databases. 
Results are reported in XML format.
```text
cluster_interproscan -i nucleotides.fasta -o results.xml -f XML -t n
```

2. Running InterProScan search for protein sequence set against PfamA databases. Results are reported in GFF3 format.
```text
cluster_interproscan -i proteins.fasta -o results.gff3 -f GFF3 -appl PfamA
```


## More information

*   [InterPro home page](https://www.ebi.ac.uk/interpro/)
