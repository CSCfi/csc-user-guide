---
tags:
  - Free
catalog:
  name: HADDOCK3
  description: High Ambiguity Driven biomolecular DOCKing
  license_type: Free
  disciplines:
    - Chemistry
    - Biosciences
  available_on:
    - LUMI
---

# HADDOCK3

HADDOCK (High Ambiguity Driven protein-protein DOCKing) is a widely used computational
tool for the integrative modeling of biomolecular interactions.  The software integrates
various types of experimental data, biochemical, biophysical, bioinformatic prediction 
and knowledge to guide the docking process.

HADDOCK, developed by researchers at BonvinLab at Utrecht University, is a flagship software
in the EU H2020 [BioExcel Center of Excellence for Biomolecular Research](https://bioexcel.eu/). 

[TOC]

## Available

=== "LUMI"
    | Version | Available modules | Notes |
    |:-------:|:------------------|:-----:|
    | 2025.5.0   |`haddock3/2025.5.0-mpi`| MPI-enabled module available
    | 2025.8.1   |`haddock3/2025.8.1-mpi`| MPI-enabled module available
  
## License

HADDOCK3 is free and open-source software, licensed under the 
[Apache License 2.0](https://github.com/haddocking/haddock3/blob/main/LICENSE)
Commercial entities should verify and secure a license for CNS if needed. For this,
please contact the main developer
[Alexandre Bonvin](https://www.bonvinlab.org/software/haddock3/) for details.

## Usage

Load HADDOCK3 module on LUMI as the following:

   ```text
    module use  /appl/local/csc/modulefiles/
    module load  haddock3/2025.8.1-mpi 
   ```

### LUMI

It is easy to try out the software on LUMI. First, download tutorial inputs by
cloning this repository in your scratch folder:

```
  git clone https://github.com/haddocking/haddock3.git
```

HADDOCK will automatically dispatch subjobs, within the slurm allocation, also
spanning multiple nodes (second example).
Note, that you need to create the batch job in and launch it from the _correct
subfolder_ (mentioned in each example batch script).

!!! note "Match the Slurm and cfg requirements"

    Make sure that the number of cores (`ncores`) in the input.`cfg`
    script matches what you ask from SLURM with `--ntasks-per-node=XX` (or
    `--nodes=YY` times that for the mpi-job). For these examples you need to
    edit also the `.cfg` files!

=== "Haddock3 batch script example"
 
  ```text
  #!/bin/bash
  #SBATCH --account=project_xxxxxxxx
  #SBATCH --partition=standard
  #SBATCH --time=00:15:00
  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=32
  #SBATCH --job-name=haddock3job

  module use  /appl/local/csc/modulefiles/
  module load  haddock3/2025.8.1-mpi

  # create this batch script file in and submit it from
  # haddock3/examples/docking-protein-ligand
  # and make sure the requested cores match the ncores in *.cfg file

  haddock3 docking-protein-ligand-test.cfg
  ```

=== "Haddock3 multi node job batch script example"

  ```text
  #!/bin/bash
  #SBATCH --account=project_xxxxxxxx
  #SBATCH --partition=standard
  #SBATCH --time=02:00:00
  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=128
  #SBATCH --job-name=haddock3mpi

  module use  /appl/local/csc/modulefiles/
  module load  haddock3/2025.8.1-mpi

  # create this batch script file in and submit it from
  # haddock3/examples/docking-antibody-antigen
  # and make sure the requested cores match the ncores in *.cfg file

  # execute
  haddock3 docking-antibody-antigen-CDR-accessible-clt-full-mpi.cfg
  ```

The first job should complete in a few minutes, while the second job should finish in an hour.
The second job has multiple stages executed as separate job steps. You can monitor
their progress e.g. with `sacct -j <JOBID> -o jobid,alloc,elapsed,maxrss`. In addition
to these subjobs, the workflow has a final analysis stage which takes longer with increasing
cores used in the computation. In practice, it will limit the reasonable amount of
resources to 2 nodes for this case.


## References

Cite your work with the following references:

> - M. Giulini, V. Reys, J.M.C. Teixeira, B. Jiménez-García, 
    R.V. Honorato, A. Kravchenko, X. Xu, R. Versini, A. Engel, S. Verhoeven, A.M.
    J.J. Bonvin, HADDOCK3: A modular and versatile platform for integrative modelling 
    of biomolecular complexes Journal of Chemical Information and Modeling (2025). doi: 10.1021/acs.jcim.5c00969
> - M.C. Teixeira, J., Vargas Honorato, R., Giulini, M., Bonvin, A., 
    Alidoost, S., Reys, V., Jimenez, B., Schulte, D., van Noort, C., Verhoeven, S., Vreede, B., SSchott, 
    & Tsai, R. (2024). haddocking/haddock3: v3.0.0-beta.5 (Version 3.0.0-beta.5) 


## More information

- [HADDOCK3 home page](https://www.bonvinlab.org/software/haddock3/) and [documentation](https://www.bonvinlab.org/haddock3-user-manual/)
- [BioExcel-3 CoE HADDOCK page](https://bioexcel.eu/haddock-new/)
