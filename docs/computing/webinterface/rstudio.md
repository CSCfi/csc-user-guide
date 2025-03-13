# RStudio

The RStudio application will launch an RStudio session on Puhti with the specified resources using
the selected [R environment (r-env) version](../../apps/r-env.md#available)). Currently, the latest available r-env
(and R) version is **4.4.2**.

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
sessions in two hidden folders in the user's home directory: `.config/rstudio` and `.local/share/rstudio`. These folders can be either renamed (to keep the contents) or deleted (if you are sure the contents are not needed).

**Option 1:** Use the file viewer in the Puhti web interface:

1. In the top left corner of the Puhti web interface dashboard, choose **Files** and **Home Directory**.
2. Click **Show dotfiles**.
3. Delete or rename the `rstudio` folders under `.config` and `.local` -> `share`. 

**Option 2:** Use a terminal (for example a login node shell in the Puhti web interface) to delete or rename these folders. Here is an example how renaming would work:

`mv ~/.config/rstudio ~/.config/rstudio-old`  
`mv ~/.local/share/rstudio ~/.local/share/rstudio-old`

If after this RStudio still fails to start or remains very slow, please [contact CSC Service
Desk](../../support/contact.md).

### How do I install an R package?

The R environment on Puhti has over 1400 pre-installed R packages packages ready to use. The easiest
way to check if a package is available is to try to load it with `library(packagename)`. If a
package is missing, you can install it yourself for your project by following the [instructions for R package
installation](../../apps/r-env.md#r-package-installations), or you can [contact CSC Service
Desk](../../support/contact.md) for a general installation available to all users.

### How do I change the directory shown in the RStudio files panel?

By default, the files panel shows your home directory on Puhti. To change the directory, click the three dots on the top right of the panel. In the box that appears, type the target directory, for example `/scratch/<project>`.

![Changing RStudio Files panel directory](../../img/rstudio_change_directory.png 'Changing RStudio Files panel directory')

## More information

For more information on the R environment on Puhti, see the [r-env
documentation](../../apps/r-env.md). If you have a question, please [contact CSC Service
Desk](../../support/contact.md). 
