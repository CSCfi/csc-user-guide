---
editor_options: 
  markdown: 
    wrap: 100
---

# RStudio

The RStudio application will launch an RStudio session on Puhti with the specified resources using
the selected R environment ([r-env](../../apps/r-env.md#available)) version. Currently, the latest available r-env
(and R) version is **4.4.0**.

The user is automatically logged in to the RStudio session when pressing the **Connect to RStudio
Server** button.

Selecting **Multithreaded** will set the environment variable `OMP_NUM_THREADS`, controlling the number
of OpenMP threads, to the number of requested CPU cores. See [r-env documentation on
threading](../../apps/r-env.md#improving-performance-using-threading) for more details.

!!! note "When to use RStudio?"
    RStudio sessions on Puhti are meant for interactive work, for example R script development and running light and medium-heavy analyses up to a few hours. Long, 
    memory-intensive, or otherwise resource-heavy tasks are best carried out as [non-interactive batch jobs](../../apps/r-env.md#non-interactive-use).

## Frequently asked questions about RStudio

### RStudio is not starting and I see a grey screen. What should I do?

If an RStudio session fails to start or RStudio is extremely slow, first try resetting your
RStudio user state as described below. These steps will clean up leftover data from previous interrupted RStudio
sessions in two hidden folders in the user's home directory.

Use the file viewer in the Puhti web interface (click **show dotfiles**) or a terminal to rename or
delete these folders :

`~/.config/rstudio`  
`~/.local/share/rstudio`

If after this RStudio still fails to start or remains very slow, please contact [CSC Service
Desk](../../support/contact.md).

### How do I install an R package?

The R environment on Puhti has over 1400 pre-installed R packages packages ready to use. The easiest
way to check if a package is available is to try to load it with `library(packagename)`. If a
package is missing, you can install it yourself for your project by following the [instructions for R package
installation](../../apps/r-env.md#r-package-installations), or you can contact [CSC Service
Desk](../../support/contact.md) for a general installation available to all users.

### How do I change the directory shown in the RStudio files panel?

By default, the files panel shows your home directory on Puhti. To change the directory, click the three dots on the top right of the panel. In the box that appears, type the target directory, for example `/scratch/<project>`.

## More information

For more information on the R environment on Puhti, see the [r-env
documentation](../../apps/r-env.md). If you have a question, contact [CSC Service
Desk](../../support/contact.md). 
