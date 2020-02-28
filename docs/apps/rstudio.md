# RStudio IDE

RStudio is an integrated development environment (IDE) for R. More information on RStudio can be found on the [RStudio website](https://rstudio.com/). 

## Available

The `rstudio` module on Puhti supports the following RStudio Desktop versions:

- 1.2.5019

## Licenses

The RStudio Desktop installation on Puhti is based on the [Open Source Edition](https://rstudio.com/products/rstudio/#rstudio-desktop) (available under the [AGPL v3 license)](https://github.com/rstudio/rstudio/blob/master/COPYING). The RStudio End User License Agreement can be found [here](https://rstudio.com/about/eula/).

## Usage

#### Loading the module

To use this module on Puhti, first start a shell session on the `interactive` partition using the `sinteractive` command. As an example, the following command would launch a session with 8 GiB of memory and 100 GiB of local scratch space. It is also possible to specify the number of cores and the running time among other options ([see the `sinteractive` documentation](../computing/running/interactive-usage.md)).

```bash
sinteractive -p <project> --mem 8000 --tmp 100
```

Once you have opened an interactive shell session, you can start RStudio after loading the `r-env` module (note that `r-env` needs to be loaded in order to use `rstudio`):

```
module load r-env
module load rstudio
rstudio
```

!!! note Note that it may take some time to initialize RStudio after running the `rstudio` command.  

For information on `r-env`, see the user documentation [here](./r-env.md).

## Citation

Citation information for RStudio is available via the following command:

```r
RStudio.Version()
```

## Further information

- [About RStudio](https://rstudio.com/about/) (RStudio website)

- [RStudio](https://github.com/rstudio/rstudio) (GitHub)
