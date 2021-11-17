# Bioconda

Conda is a package management tool that is used to distribute and install software tools together with their dependencies. In Puhti, the __bioconda module__
takes in use a CSC maintained Conda environment (Python3 based miniconda3) together with channel settings that enable easy usage of the Bioconda repository.

The Bioconda environment is used for two purposes in Puhti:

-    Some software tools, maintained by CSC, are installed and used as Conda environments.
-    Puhti users can use bioconda module to install tools, available in Bioconda repository, to their own personal Conda environments.

[TOC]

## License

Bioconda is free to and open source under [MIT License](https://raw.githubusercontent.com/bioconda/bioconda-common/master/LICENSE).

## Available

-   Puhti: miniconda3 and miniconda2



## Usage

### 1. Using tools installed with bioconda

To use software environments that are installed to Puhti using Conda (either by CSC or yourself),  first 
define environment variable PROJAPPL to point to a directry of the project that you wish to use for your own 
conda environments. 

Typically this is your _/projappl/project_name_ directory, but you can use scratch too.
This definition is made with command _export_ . For example for _project_012345_ the command would be:

```text
export PROJAPPL=/projappl/project_12345
```
Next, load bioconda module:
```text
module load bioconda
```
This load miniconda3 based conda environment that is compatible with Python3 and gcc 7.4.0.
If you wish to use Python2 based miniconda2, set up the conda environment with:
```text
module load bioconda/2
```

Then you can list the available Conda environments
```text
conda env list
```
And activate a Conda environment

```text
source activate env_name
```

Later on you can deactivate the environment with command:
```text
conda deactivate
```

### 2. Installing software for your own use with bioconda

You can use the bioconda module to install software packages available in the Bioconda and other conda repositories to your personal Conda environments. Not that you can't install new Conda packages to the base environment of bioconda, but you must create your own conda environment for installations.

In the example below a new Conda environment, containing _bedops_ package is created:
```text
export PROJAPPL=/projappl/project_xxxxxx
module load bioconda
conda create -n my_biotools bedops
source activate my_biotools
```
After this, commands included in Bedops tools can be used. For example:
```text
vcf2bed
```
To deactivate the current Conda environment, run command:

```text
conda deactivate
```
Next time you need to use `vcf2bed`, it is enough that you run the set-up commands:

```text
export PROJAPPL=/projappl/project_xxxxxx
module load bioconda
source activate my_biotools
vcf2bed
```

!!! Note

    You should **not** use _conda init_ in Puhti. This applies to both
    Bioconda and your own Conda installations.
    
    _conda init_ modifyes your account so that it takes the Conda environment automatically in use. 
    This is in principle handy, but in practice it will often cause problems when you 
    try to use software that were not installed with your default Conda environment.
    



## Support

servicedesk@csc.fi

## Manual


*    [Conda home page](https://conda.io/en/latest/)
*    [Bioconda home page](https://bioconda.github.io/)



