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

HADDOCK, standing for High Ambiguity Driven protein-protein DOCKing, is a widely used computational tool for the integrative modeling of biomolecular interactions. Developed by researchers at Utrecht University in the BonvinLab for more than 20 years, it integrates various types of experimental data, biochemical, biophysical, bioinformatic prediction and knowledge to guide the docking process.

HADDOCK v3.0 is a bottom-up reimagination of the long standing time-proven HADDOCK used for integrative modeling of biomolecular complexes. This young and still very experimental (use it at your own risk!) aims to modularize and extend HADDOCK’s core functions.

HADDOCK is one of the flagship software in the EU H2020 BioExcel Center of Excellence for Biomolecular Research 

[TOC]

## Available

=== "LUMI"
    | Version | Available modules | Notes |
    |:-------:|:------------------|:-----:|
    | 2025.5.0   |`haddock3/2025.5.0`<br>`haddock3/2025.5.0-mpi`| MPI-enabled module available
  

- To access modules on LUMI, first load the CSC module tree into use with
  `module use /appl/local/csc/modulefiles`


## License

HADDOCK3 is a free software available under Apache-2.0 license

## Usage

Load HADDOCK3 module  on LUMI like this:

   ```text
    module use  /appl/local/csc/modulefiles/
    module load  haddock3/2025.5.0
    module load  haddock3/2025.5.0-mpi    # works also for MPI jobs

   ```

### LUMI

=== "Haddock3 batch script example"
 
  ```text
    #!/bin/bash
    #SBATCH --account=project_xxxxxxxx
    #SBATCH --partition=standard
    #SBATCH --time=00:60:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=128
    #SBATCH --job-name=haddock3job

    module use  /appl/local/csc/modulefiles/
    module load  haddock3/2025.5.0-mpi

  # clone haddock3 repository
    git clone https://github.com/haddocking/haddock3.git

  # go to the example directory   
    cd haddock3/docking-protein-ligand
    haddock3 docking-protein-ligand-test.cfg
  ```

=== "mpi job in batch script example"

  ```text
    #!/bin/bash
    #SBATCH --account=project_xxxxxxxx
    #SBATCH --partition=standard
    #SBATCH --time=03:00:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=128
    #SBATCH --job-name=haddock3mpi

    module use  /appl/local/csc/modulefiles/
    module load  haddock3/2025.5.0-mpi

  # clone haddock3 repository
    git clone https://github.com/haddocking/haddock3.git

  # go to the example directory
    cd haddock3/examples/docking-antibody-antigen

  # execute
    haddock3 docking-antibody-antigen-CDR-accessible-clt-full-mpi.cfg
    ```

## References

Cite your work with the following references:

> - M. Giulini, V. Reys, J.M.C. Teixeira, B. Jiménez-García, 
    R.V. Honorato, A. Kravchenko, X. Xu, R. Versini, A. Engel, S. Verhoeven, A.M.
    J.J. Bonvin, HADDOCK3: A modular and versatile platform for integrative modelling 
    of biomolecular complexes Journal of Chemical Information and Modeling (2025). 
    doi: 10.1021/acs.jcim.5c00969
> - M.C. Teixeira, J., Vargas Honorato, R., Giulini, M., Bonvin, A., 
    SarahAlidoost,Reys, V., Jimenez, B., Schulte, D., van Noort, C., Verhoeven, S., Vreede, B., SSchott, 
    & Tsai, R. (2024). haddocking/haddock3: v3.0.0-beta.5 (Version 3.0.0-beta.5) 


## More information

- [HADDOCK3 home page](https://www.bonvinlab.org/software/haddock3/) and [documentation](https://www.bonvinlab.org/haddock3-user-manual/)
