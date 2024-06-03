# Running containers

If you are familiar with [Docker containers](https://en.wikipedia.org/wiki/Docker_(software)), [Apptainer containers](https://apptainer.org/) (formerly known as Singularity) are essentially the same thing, but are better suited for multi-user systems such as CSC's supercomputers. Containers provide an isolated software environment for each application, which makes it easier to install complex applications. On shared file systems, such as those used on CSC's supercomputers, launch times can also be much shorter for containers compared to alternatives such as conda.

For more information, read our [overview page on containers](overview.md) or [the Apptainer user guide](https://apptainer.org/docs/user/main/).

## Running Apptainer

CSC's supercomputers Puhti and Mahti both support running Apptainer containers. For many use cases, CSC's staff has provided ready-made containers that can be used simply by loading the corresponding module. Please check the [application pages](../../apps/index.md) if a pre-installed container is already available for the application you are interested in. See that specific application's page for detailed instructions on how to use it.

If you find that some container is missing that you think could be generally useful, you can ask us to install it by contacting [CSC's Service Desk](../../support/contact.md).  Otherwise you can also look into [building your own container images](creating.md).

### Using `apptainer_wrapper`

Unless otherwise specified in the application-specific documentation, all CSC's Apptainer-based applications can be easily used with the `apptainer_wrapper` command. In many cases also other common commands, such as `python` or `R`, have also been wrapped to make the user experience seamless. See the [individual application documentation pages](../../apps/index.md) for details.

When you load a container-based module it sets appropriate values to the `SING_IMAGE` and `SING_FLAGS` shell environment variables which are used by `apptainer_wrapper` to set all the appropriate options automatically for running Apptainer.

The typical way to run something using the activated container is as follows:

```bash
module load modulename
apptainer_wrapper exec command_to_run
```

Another useful command is `apptainer_wrapper shell` which starts a shell session inside the container.

Inside the container, the root directory in general is read-only, i.e., you cannot change the image itself. Common paths such as `/projappl`, `/scratch` and users' home directories are "bound" to the real (host) paths and can thus be read from and written to as usual from inside the container.

You can also use `apptainer_wrapper` with containers that you have created yourself. You just need to set the `SING_IMAGE` to point to the correct Apptainer image file. For example:

```bash
export SING_IMAGE=/path/to/apptainer_image.sif

apptainer_wrapper exec command_to_run
```

You can also set additional Apptainer options via the `SING_FLAGS` variable. For example to use GPUs:

```bash
export SING_FLAGS=--nv
```


### Running Apptainer directly

You can also run Apptainer directly if the `apptainer_wrapper` script for some reason isn't appropriate for you.  Then you need to provide the path to the container image yourself and bind any paths that you need to be able to access from inside the image. Note that by default some paths such as `HOME` and `CWD` are [bound automatically](https://apptainer.org/docs/user/main/bind_paths_and_mounts.html#system-defined-bind-paths).

Usage examples:

```bash
apptainer exec -B /scratch:/scratch /path/to/apptainer_image.sif command_to_run
apptainer shell /path/to/apptainer_image.sif
```

If you need GPU support, add the `--nv` flag to your command.

### Mounting datasets with SquashFS 

A common problem with supercomputers is that accessing datasets with a huge number of files on the shared file system is very inefficient. For more details, please read [our technical description of the Lustre file system](../lustre.md). Using Apptainer, one potential solution to this problem would be [accessing the dataset using a SquashFS image](https://sylabs.io/guides/3.7/user-guide/bind_paths_and_mounts.html#squashfs-image-files). 

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

Next, you would mount this image to your Apptainer execution so that it appears as a normal directory inside the container.  We simply need to add a bind mount option to the Apptainer command: `-B /scratch/project/my_dataset.sqfs:/data:image-src=/`. If you are using the `apptainer_wrapper` you can do this by adding it to the `SING_FLAGS environment variable:

```
export SING_FLAGS="-B /scratch/project/my_dataset.sqfs:/data:image-src=/ $SING_FLAGS"
```

After this the dataset will be available under the `/data` path inside the container.
