# RStudio IDE

RStudio is an integrated development environment (IDE) for R. More information on RStudio can be found on the [RStudio website](https://rstudio.com/). 

## Available

The `rstudio` module on Puhti supports the following RStudio Desktop versions:

- 1.2.5019

## Licenses

The RStudio Desktop installation on Puhti is based on the [Open Source Edition](https://rstudio.com/products/rstudio/#rstudio-desktop) (available under the [AGPL v3 license)](https://github.com/rstudio/rstudio/blob/master/COPYING). The RStudio End User License Agreement can be found [here](https://rstudio.com/about/eula/).

## Usage

#### Loading the module

To use this module on Puhti, initialize it after loading the `r-env` module (note that `r-env` needs to be loaded in order to use `rstudio`):

```
module load r-env
module load rstudio
```

For information on `r-env`, see the user documentation [here](./r-env.md). Note that Puhti login nodes are [not intended for heavy computing](../computing/overview.md). To use RStudio in Puhti, please request an interactive job on a compute node.

#### Interactive use

To interactively use RStudio on Puhti's compute nodes, run the following command. This will request a single-processor R session. Note that you will need to modify the requested duration, memory, project ID and partition as required:

```
srun --ntasks=1 --time=hh:mm:ss --x11=first --mem=4G --pty --account=project_id --partition=partition rstudio --no-save
```

For information on available partitions, see [here](../computing/running/batch-job-partitions.md).

## Citation

Citation information for RStudio is available via the following command:

```r
RStudio.Version()
```

## Further information

- [About RStudio](https://rstudio.com/about/) (RStudio website)

- [RStudio](https://github.com/rstudio/rstudio) (GitHub)
