# Installing packages from Bioconda using Tykky

[Bioconda](https://bioconda.github.io/index.html) is a popular
Conda channel for bioinformatics software. It provides an easy
method to install thousands of software packages related to biomedical
research.

CSC has deprecated the direct usage of Conda installations on shared file systems
of supercomputers (Puhti and Mahti) due to performance
issues, but you can easily install packages from Bioconda using the
[Tykky](../../computing/containers/tykky.md) tool instead.

All packages in Bioconda have a ready-made Docker container image available. While
those images could be pulled and used directly, Tykky provides an easy method to
install them in a way that they are usable without any special container commands.

## Example: Installing MetaBAT2 from Bioconda

In this example we install MetaBAT2 package from Bioconda. To find a software in
Bioconda you can
[browse them alphabetically](https://bioconda.github.io/conda-package_index.html)
or use the search. For our example we choose
[MetaBAT2 package](https://bioconda.github.io/recipes/metabat2/README.html).

In the page find the command to use Docker. In this case:

```bash
docker pull quay.io/biocontainers/metabat2:<tag>
```

From the command we need the Docker address:

```bash
quay.io/biocontainers/metabat2
```

From the Tags page select the desired version. In this case we choose the latest
(the topmost) version:

```bash
2.15--h986a166_1
```

Combine the address and tag to form Docker URL:

```bash
docker://quay.io/biocontainers/metabat2:2.15--h986a166_1
```

Load the Tykky module:

```bash
module load tykky
```

We will use the Tykky
[wrap-container](../../computing/containers/tykky.md#container-based-installations)
command.

The `-w` parameter is needed to specify the installation directory inside the
container. For containers from Bioconda this is always `/usr/local/bin`. For
containers from other sources, please see below.

The `--prefix` parameter indicates the directory where we want to install the
environment on the shared file system (outside the container). The directory
needs to exist, so we we need to create it first. For example:

```bash
mkdir -p /projappl/project_2001234/metabat-2.15
```

We can now install the software with:

```bash
wrap-container -w /usr/local/bin docker://quay.io/biocontainers/metabat2:2.15--h986a166_1 --prefix /projappl/project_2001234/metabat-2.15
```

After the installations finishes, the executables for the program will be in directory
`metabat-2.15/bin`. It should be noted that these are not the actual commands, but
rather wrapper scripts for the commands inside the container. You can, however, use
them as if they were the actual commands. For example:

```bash
/projappl/project_2001234/metabat-2.15/bin/metabat --help
```

Adding the `bin` directory to your `$PATH` will work similarly as activating the
Conda environment in case of a direct Conda installation. When the `wrap-container`
command finishes, it will show you the `export` command to do this. The actual command
will depend on the installation directory, but will be something like:

```bash
export PATH="/projappl/project_2001234/metabat-2.15/bin:$PATH"
```

After this you can simply do:

```bash
metabat --help
```

!!! note
    It is generally a bad idea to add Tykky installations permanently to your `$PATH`
    by e.g. editing your `.bashrc` file. The installation directories often contain
    common commands like `python` or `perl`. These are specific for each installation,
    and having them in your default `$PATH` will cause problems with running other
    software. It's best to add the installation directory to your `$PATH` only when
    you are using the program. You can e.g. add the `export` command to your
    [batch job script](../../computing/running/creating-job-scripts-puhti.md).

## Containers from other source

You can use similar steps to create wrappers for containers from other sources, such
as the [BioContainer registry](https://biocontainers.pro/) or local image files.
The software installation location inside the container may vary, so it should be
checked in order to set `-w` parameter correctly. In this example we'll use a container
for `mono`.

First build a local container image:

```bash
apptainer build mono.sif docker://mono:6.12.0.182-slim
```

You can now run command `which` inside the container to find out the installation
location.

```bash
apptainer exec mono.sif which mono
```

In this case the directory is `/usr/bin`. To install you could use the Docker address
above or specify the local image file just created (`mono.sif`).

```bash
wrap-container -w /usr/bin mono.sif --prefix mono
```

In some cases the installation location is not in `$PATH` inside the container, so
`which` won't work. In those cases you could try running `find` inside the container
instead:

```bash
apptainer exec mono.sif find / \( -type f -o -type l \) -name mono 2> /dev/null
```

In this case we search starting from the root directory(`/`) for either a file
(`-type f`) or (`-o`) a symbolic link (`-type l`) named `mono` (`-name mono`).
