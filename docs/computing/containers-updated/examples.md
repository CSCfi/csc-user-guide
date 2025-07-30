# Examples
Examples of building and running containers on Puhti and Mahti.

## Python

```sh title="python.def"
Bootstrap: docker
From: rockylinux/rockylinux:8.10

%post
    cp /usr/bin/true /usr/sbin/useradd
    cp /usr/bin/true /usr/sbin/groupadd

    dnf -y update
    dnf -y install python3.11 python3.11-pip
    dnf -y clean all

    # install packages with pip
```

```bash
apptainer build --fakeroot python.sif python.def
```

## Miniforge

```sh title="miniforge.def"
Bootstrap: docker
From: rockylinux/rockylinux:8.10

%post
    cp /usr/bin/true /usr/sbin/useradd
    cp /usr/bin/true /usr/sbin/groupadd

    dnf -y update
    dnf -y install curl
    dnf -y clean all

    curl --location --output /opt/miniforge3.sh "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    sh /opt/miniforge3.sh -b -p /opt/miniforge3
    rm -f /opt/miniforge3.sh

    export MAMBA_ROOT_PREFIX=/opt/miniforge3
    /opt/miniforge3/bin/mamba shell hook --shell bash > /opt/mamba-hook.sh
    . /opt/mamba-hook.sh

    # install packages with mamba

%environment
    export MAMBA_ROOT_PREFIX=/opt/miniforge3

%runscript
    . /opt/mamba-hook.sh
    eval "$@"
```

```bash
apptainer build --fakeroot miniforge.sif miniforge.def
```

## Other

- [MATLAB](https://github.com/CSCfi/singularity-recipes/tree/main/matlab/r2024b)
- [Macaulay2](https://github.com/CSCfi/singularity-recipes/tree/main/macaulay2)
