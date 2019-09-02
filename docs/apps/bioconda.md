# Bioconda

Conda is a package management tool that is used to distribute and install software tools together with their dependencies. In Puhti, the __bioconda module__
takes in use a CSC maintained Conda environment (Python3 based miniconda3) together with channel settings that enable easy usage of the Bioconda repository.

The Bioconda environment is used for two purposes in Puhti:

-    Some software tools, maintained by CSC, are installed and used as Conda environments.
-    Puhti users can use bioconda module to install tools, available in Bioconda repository, to their own personal Conda environments.



## Available

-   Puhti: miniconda3



## Usage

### 1. Using tools installed with bioconda

To use software environments that are installed to Puhti using Conda (either by CSC or yourself),  first load bioconda module:
```text
module load bioconda
```

Then list the available Conda environments
```text
conda env list
```
Next activate a Conda environment

```text
source activate env_name
```

Later on you can deactivate the environment with command:
```text
conda deactivate
```

### 2. Installing software for your own use with bioconda

You can use the bioconda module to install software packages available in the Bioconda repository to your personal Conda environments. 
In the example below a new Conda environment, containing _bedops_ package is created:
```
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
module load bioconda
source activate my_biotools
vcf2bed
```

## Support

servicedesk@csc.fi

## Manual


*    [Conda home page](https://conda.io/en/latest/)
*    [Bioconda home page](https://bioconda.github.io/)



