# RStudio IDE

RStudio is an integrated development environment (IDE) for R. More information on RStudio can be found on the [RStudio website](https://rstudio.com/). 

## Available

The `rstudio` module on Puhti supports the following RStudio Desktop versions:

- 1.2.5019

## Licenses

The RStudio Desktop installation on Puhti is based on the [Open Source Edition](https://rstudio.com/products/rstudio/#rstudio-desktop) (available under the [AGPL v3 license)](https://github.com/rstudio/rstudio/blob/master/COPYING). The RStudio End User License Agreement can be found [here](https://rstudio.com/about/eula/).

## Usage

#### Loading the module

To use this module on Puhti, first start a shell session on the `interactive` partition using the `sinteractive` command. As an example, the following command would launch a session with 8 GiB of memory and 100 GiB of local scratch space. It is also possible to specify several other options, including the running time ([see the `sinteractive` documentation](../computing/running/interactive-usage.md)). Maximal reservations in the `interactive` partition include: 1 core, 16 GB of memory, 7 days of time and 160 GB of local scratch space. If these limits are too restrictive, `sinteractive` can also be used to launch interactive jobs in the `small` partition ([see here for information on Puhti partitions](../computing/running/batch-job-partitions.md)).

```bash
sinteractive --account <project> --mem 8000 --tmp 100
```

Once you have opened an interactive shell session, the `rstudio` module can be launched after loading the `r-env` module. RStudio can then be started using the command `rstudio`. Note that after running the `rstudio` command, it may take a while for RStudio to initialize.

```
module load r-env
module load rstudio
rstudio
```

For information on `r-env`, see the user documentation [here](./r-env.md).

## Citation

Citation information for RStudio is available via the following command:

```r
RStudio.Version()
```

## Further information

- [About RStudio](https://rstudio.com/about/) (RStudio website)

- [RStudio](https://github.com/rstudio/rstudio) (GitHub)
