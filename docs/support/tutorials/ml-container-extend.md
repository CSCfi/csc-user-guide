# Build Your Own ML Container on Top of the Base Images Using Apptainer Sandbox on Roihu

## Motivation

Using the pre-installed PyTorch modules on Roihu is convenient for many workflows. However, when working with different repositories, users may need different PyTorch versions or specific libraries that depend on a particular PyTorch version.

For example, the latest `fairchem-core` release requires a recent PyTorch version. In this guide, we demonstrate how to build a custom Apptainer container based on the CSC `ml-base` image and install **PyTorch 2.13.0 with CUDA 13.0** together with **`fairchem-core` 2.22.0**.

The workflow uses an Apptainer **sandbox** as a writable environment during installation. Once the required software has been installed, the sandbox is converted into a portable `.sif` image that can be used for subsequent FairChem workloads.

> **Note:** The commands below are intended to be run on **Roihu**, but it should be easily adaptable to other clusters.

## 1. Allocate Resources

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

## 2. Set the Apptainer Cache Directory

Set the Apptainer cache directory to `$TMPDIR` to avoid filling your home directory:

```bash
export APPTAINER_CACHEDIR="$TMPDIR/apptainer-cache"
mkdir -p "$APPTAINER_CACHEDIR"
```

## 3. Create a Writable Sandbox from `ml-base`

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

## 4. Create the Users Directory

Create the `users` directory inside the sandbox:

```bash
mkdir -p "$TMPDIR/mlbase/users"
```

## 5. Enter the Sandbox 

Start a writable shell inside the sandbox. The `--nv` option makes the NVIDIA GPU and relevant NVIDIA libraries available inside the container:

```bash
apptainer shell --fakeroot --writable --nv \
    --contain --cleanenv \
    --bind="$TMPDIR:/tmp" \
    "$TMPDIR/mlbase"
```

You are now working inside the writable `mlbase` sandbox.

## 6. Configure the pip Cache

Inside the container, configure pip to use a cache directory under `/tmp`:

```bash
export PIP_CACHE_DIR=/tmp/pip-cache
mkdir -p /tmp/pip-cache
```

Because `$TMPDIR` is bound to `/tmp` inside the container, the pip cache is stored outside the container image.

## 7. Work Around `useradd` and `groupadd`

If package installation fails because `useradd` or `groupadd` cannot be executed in the sandbox, replace these commands with `/usr/bin/true`:

```bash
cp /usr/bin/true /usr/sbin/useradd
cp /usr/bin/true /usr/sbin/groupadd
```

This prevents package installation scripts from failing when they attempt to create system users or groups.

## 8. Install PyTorch 2.13.0 with CUDA 13.0

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

## 9. Install `fairchem-core 2.22.0`

```bash
pip install fairchem-core==2.22.0
```

Verify:

```bash
python -c "from fairchem.core import pretrained_mlip, FAIRChemCalculator; print('fairchem ok')"
```

## 10. Exit the Sandbox

Once all required software has been installed, exit the container:

```bash
exit
```

You should now be back in the host environment.

## 11. Build the SIF Image

Convert the writable sandbox into a standard Apptainer SIF image:

```bash
apptainer build --fakeroot fairchem.sif "$TMPDIR/mlbase"
```

The resulting image will be:

```text
fairchem.sif
```

The SIF format is a portable, read-only Apptainer image that can be used for subsequent jobs.

## 12. Verify the SIF Image

Check the size of the generated container:

```bash
ls -lh fairchem.sif
```

The SIF file will typically be several GB in size, depending on the packages installed in the container.

## 13. Test the Container

Finally, verify that both FairChem and PyTorch can be imported from the generated SIF image:

```bash
apptainer exec fairchem.sif \
    python -c "import fairchem.core, torch; print(torch.__version__)"
```

You can also check CUDA availability with flag --nv. In addition, on Roihu, we can use csc-common-bind command to bind mounts the common disk areas such as "`/users`, `/projappl`, `/scratch`, `$TMPDIR`,`$LOCAL_SCRATCH`":

```bash
apptainer exec --bind="$(csc-common-bind)" --nv fairchem.sif \
    python -c "import torch; print('PyTorch:', torch.__version__); print('CUDA available:', torch.cuda.is_available())"
```
If the commands complete successfully, the custom FairChem container has been built successfully.

