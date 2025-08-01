# Examples
Examples of building and running containers on Puhti and Mahti.

## Rockylinux

```sh title="rockylinux.def"
Bootstrap: docker
From: rockylinux/rockylinux:8.10

%post
    cp /usr/bin/true /usr/sbin/useradd
    cp /usr/bin/true /usr/sbin/groupadd

    dnf -y update
    dnf -y install epel-release curl
    dnf -y clean all
```

```bash
apptainer build --fakeroot rockylinux.sif rockylinux.def
```

## Applications

- [Miniforge](https://github.com/CSCfi/singularity-recipes/tree/main/miniforge)
- [uv (Python)](https://github.com/CSCfi/singularity-recipes/tree/main/python-uv)
- [MATLAB](https://github.com/CSCfi/singularity-recipes/tree/main/matlab/r2024b)
- [Macaulay2](https://github.com/CSCfi/singularity-recipes/tree/main/macaulay2)
