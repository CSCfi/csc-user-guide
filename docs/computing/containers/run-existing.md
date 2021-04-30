# Running Singularity containers

## Background

If you are familiar with [Docker containers](https://en.wikipedia.org/wiki/Docker_(software)), [Singularity containers](https://sylabs.io/singularity/) are essentially the same thing, but are better suited for multi-user systems such as CSC's supercomputers. Containers provide an isolated software environment for each application, which makes it easier to install complex applications. On shared file systems, such as those used on CSC's supercomputers, launch times can also be much shorter for containers compared to alternatives such as conda.

You can [read more about Singularity in the official user guide](https://sylabs.io/guides/3.6/user-guide/).

## Running Singularity

CSC's supercomputers Puhti and Mahti both support running Singularity containers. For many use cases, CSC's staff has provided ready-made containers that can be used simply by loading the corresponding module. Please check the [application pages](../../apps/index.md) if a pre-installed container is already available for the application you are interested in. See that specific application's page for detailed instructions on how to use it.

If you find that some Singularity container is missing that you think could be generally useful, you can ask us to install it by contacting [CSC's Service Desk](https://www.csc.fi/en/contact-info).  Otherwise you can also look into [building your own Singularity container images](creating.md).

### Using `singularity_wrapper`

Unless otherwise specified in the application-specific documentation, all CSC's Singularity-based applications can be easily used with the `singularity_wrapper` command. In many cases also other common commands, such as `python` or `R`, have also been wrapped to make the user experience seamless. See the [individual application documentation pages](../../apps/index.md) for details.

When you load a Singularity-based module it sets appropriate values to the `SING_IMAGE` and `SING_FLAGS` shell environment variables which are used by `singularity_wrapper` to set all the appropriate options automatically for running Singularity.

The typical way to run something using the activated container is as follows:

```bash
module load modulename
singularity_wrapper exec command_to_run
```

Another useful command is `singularity_wrapper shell` which starts a shell session inside the container.

Inside the container, the root directory in general is read-only, i.e., you cannot change the image itself. Common paths such as `/projappl`, `/scratch` and users' home directories are "bound" to the real paths and can thus be read from and written to as usual from inside the container.

You can also use `singularity_wrapper` with containers that you have created yourself. You just need to set the `SING_IMAGE` to point to the correct Singularity image file. For example:

```bash
export SING_IMAGE=/path/to/singularity_image.sif

singularity_wrapper exec command_to_run
```

You can also set additional Singularity options via the `SING_FLAGS` variable.

### Running Singularity directly

You can also run Singularity directly if the `singularity_wrapper` script for some reason isn't appropriate for you.  Then you need to provide the path to the Singularity image yourself and bind any paths that you need to be able to access from inside the image.

Usage examples:

```bash
singularity exec /path/to/singularity_image.sif -B /scratch:/scratch command_to_run
singularity shell /path/to/singularity_image.sif
```

### Mounting datasets with SquashFS 

A common problem with supercomputers is that accessing datasets with a huge number of files on the shared file system is very inefficient. For more details, please read [our technical description of the Lustre file system](../lustre.md). Using Singularity, one potential solution to this problem would be [accessing the dataset using a SquashFS image](https://sylabs.io/guides/3.7/user-guide/bind_paths_and_mounts.html#squashfs-image-files). 

First, create a SquashFS image of your dataset, thus reducing it to one big file. We recommend doing this in an [interactive session](../running/interactive-usage.md) using the fast local drive for temporary storage. For example, to launch an interactive session with 100 GiB local drive (adjust size as needed) you can run:

```bash
sinteractive --time 1:00:00 --tmp 100 --cores 4
```

Then in the interactive session:
```bash
# Extract individual files to local drive
cd $LOCAL_SCRATCH
tar xf /scratch/project/my_dataset.tar
# Create squashfs file
mksquashfs my_dataset my_dataset.sqfs -processors 4
# Move the resulting squashfs file back to the shared drive
mv my_dataset.sqfs /scratch/project/
```

In the commands above we assume you have your dataset stored in a tar-package, and it extracts to a directory called `my_dataset`. Adjust the commands to your own situation.

Next, you would mount this image to your Singularity execution so that it appears as a normal directory inside the container.  We simply need to add a bind mount option to the Singularity command: `-B /scratch/project/my_dataset.sqfs:/data:image-src=/`. If you are using the `singularity_wrapper` you can do this by adding it to the `SING_FLAGS environment variable:

```
export SING_FLAGS="-B /scratch/project/my_dataset.sqfs:/data:image-src=/ $SING_FLAGS"
```

After this the dataset will be available under the `/data` path inside the container.
