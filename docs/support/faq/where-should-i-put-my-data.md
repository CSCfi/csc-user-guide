#Where should I put my data?

To use the computing environment in Puhti, use the parallel file system Lustre.

Puhti has three main disk areas: _home_, _projappl_ and _scratch_. Please familiarize yourself with the [disk areas and their specific purposes](/computing/disk/) before using Puhti. The _home_ directory is the only user-specific directory in Puhti. All other directories are project-specific. If you are a member of several projects, you also have access to several scratch or projappl directories, but still have only one home directory.

You should change to your project's _scratch_ directory when working with Puhti because the home directory is not intended for data analysis or computing. Its purpose is to store configuration files and other minor personal data. A home directory exceeding its capacity causes various account problems.

!!! note
     Note that the directories in Puhti are NOT backed up, which means that data accidentally deleted by the user cannot be recovered. Also keep in mind that the files in _scratch_ are automatically removed after 90 days. Store the data that is not in active use in Allas.

One of the main use cases of Allas is to store data that is not in active in the HPC systems. Before working on the data, stage stage it in. When the data is no longer actively used, it can be staged out. 

Read more about [common use cases of Allas](/data/Allas/using_allas/common_use_cases/) and see the [example of hosting data set](/data/Allas/allas_project_example/).

