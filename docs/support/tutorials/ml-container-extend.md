# Extend CSC-based ML containers using sandbox on Roihu
This guide is also part of our [Machine learning guide](ml-guide.md).
## Motivation

Using the [pre-installed PyTorch modules on Roihu](../../apps/pytorch.md) is convenient for many workflows. However, when working with different libraries, users may need PyTorch versions or other libraries that have not been installed by CSC.

For example, the latest `fairchem-core` release requires a recent PyTorch version. In this guide, we demonstrate how to build a custom Apptainer container based on the CSC `ml-base` image and install **PyTorch 2.13.0 with CUDA 13.0** together with **`fairchem-core` 2.22.0**.

The workflow uses an Apptainer **sandbox** as a writable environment during installation. Once the required software has been installed, the sandbox is converted into a portable `.sif` image that can be used for subsequent FairChem workloads.

!!! info "Note"

    The commands below are intended to be run on **Roihu**, but it should be easily adaptable to other clusters.

## Allocate Resources

Start an interactive GPU job with the required resources, here we ask for 1 GPU for 1 hour, we do not encourage users to ask more than what they need since GPUs are valuable resources:

```bash
salloc --account=project_***** \
    --nodes=1 \
    --ntasks-per-node=1 \
    --cpus-per-task=72 \
    --time=01:00:00 \
    --partition=gpuinteractive \
    --gres=gpu:gh200:1 
```

## Set the Apptainer Cache Directory

Set the Apptainer cache directory to `$TMPDIR` to avoid filling your home directory:

```bash
export APPTAINER_CACHEDIR="$TMPDIR/apptainer-cache"
```

## Create a Writable Sandbox from `ml-base`

Initialize an Apptainer sandbox using the CSC `ml-base` image:

```bash
apptainer build --fakeroot --sandbox "$TMPDIR/mlbase" \
    docker://satama.csc.fi/r_installation_aida/ml-base:rocky9.7_gcc12_py3.12_cuda13
```

After a successful build, you should see a message similar to:

```text
INFO:    Build complete: /tmp/shanshan/715617/mlbase
```

The exact path will depend on your `$TMPDIR`.

The `--sandbox` option creates a writable directory containing the extracted container filesystem. This allows you to install and modify software interactively before creating the final SIF image.

!!! warning

    Do not create a sandbox on the shared Lustre file system (for example on `/scratch`, `/projappl` or `/home`) as [it will create a lot of small files which can slow down the system for all users](../../computing/lustre.md#best-practices)!

## Create the Users Directory

Create the `users` directory inside the sandbox:

```bash
mkdir -p "$TMPDIR/mlbase/users"
```

## Enter the Sandbox 

Start a writable shell inside the sandbox. The `--nv` option makes the NVIDIA GPU and relevant NVIDIA libraries available inside the container:

```bash
apptainer shell --fakeroot --writable --nv \
    --contain --cleanenv \
    --bind="$TMPDIR:/tmp" \
    "$TMPDIR/mlbase"
```

You are now working inside the writable `mlbase` sandbox.

## Configure the pip Cache

Inside the container, configure pip to use a cache directory under `/tmp`:

```bash
export PIP_CACHE_DIR=/tmp/pip-cache
```

Because `$TMPDIR` is bound to `/tmp` inside the container, the pip cache is stored outside the container image.

## Work Around `useradd` and `groupadd`

If package installation fails because `useradd` or `groupadd` cannot be executed in the sandbox, replace these commands with `/usr/bin/true`:

```bash
cp /usr/bin/true /usr/sbin/useradd
cp /usr/bin/true /usr/sbin/groupadd
```

This prevents package installation scripts from failing when they attempt to create system users or groups.

## Install PyTorch 2.13.0 with CUDA 13.0

Install PyTorch 2.13.0 and `torchvision` using the CUDA 13.0 PyTorch wheel index:

```bash
pip install torch==2.13.0 torchvision \
    --index-url https://download.pytorch.org/whl/cu130
```

Optionally, verify the installation:

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

The output should show the installed PyTorch version and indicate whether CUDA is available.

## Install `fairchem-core 2.22.0`

```bash
pip install fairchem-core==2.22.0
```

Verify:

```bash
python -c "from fairchem.core import pretrained_mlip, FAIRChemCalculator; print('fairchem ok')"
```

## Exit the Sandbox

Once all required software has been installed, exit the container:

```bash
exit
```

You should now be back in the host environment.

## Build the SIF Image

Convert the writable sandbox into a standard Apptainer SIF image:

```bash
apptainer build --fakeroot fairchem.sif "$TMPDIR/mlbase"
```

The resulting image will be in the file `fairchem.sif`. The SIF format is a portable, read-only Apptainer image that can be used for subsequent jobs.

## Verify the SIF Image

Check the size of the generated container:

```bash
ls -lh fairchem.sif
```

The SIF file will typically be several GB in size, depending on the packages installed in the container.

## Test the Container

Finally, verify that both FairChem and PyTorch can be imported from the generated SIF image:

```bash
apptainer exec fairchem.sif \
    python -c "import fairchem.core, torch; print(torch.__version__)"
```

In order to access the GPU, add the `--nv` flag. In addition, on Roihu, we can use `csc-common-bind` command to list the bind mounts to common disk areas such as `/scratch` and `/projappl`:

```bash
apptainer exec --bind="$(csc-common-bind)" --nv fairchem.sif \
    python -c "import torch; print('PyTorch:', torch.__version__); print('CUDA available:', torch.cuda.is_available())"
```
If the commands complete successfully, the custom FairChem container has been built successfully. You can move the resulting SIF file to the proper location such as in the project's directory in `/projappl`.

