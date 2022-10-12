# Using user Spack module for software installations

Spack is a package manager for supercomputers, Linux and MacOS. It
that can be used to install complicated scientific software packages
easily. CSC installs the development stack, including compilers, MPI
libraries and also many other libraries and applications using
Spack. CSC provides also a user module for customers that enables
per-project software installations using Spack.

!!! note
    Spack is an advanced tool and it requires understanding of
    compiling and linking programs.

## Creating a Spack instance

When Spack module is run for the first time, you have to prepare an
installation location that can reside on either `/projappl` of
`/scratch` area. You also have to set up environment variable that
denotes the location of the Spack instance.

For example, if you want to create a Spack instance on the `/projappl`
directory, you can initialize the environment as follows:

```bash
[maijam@puhti-login11 ~]$ module purge
The following modules were not unloaded:
  (Use "module --force purge" to unload all):

  1) csc-tools
[maijam@puhti-login11 ~]$ export USER_SPACK_ROOT=/projappl/project_2001234/spack-instance-1
[maijam@puhti-login11 ~]$ mkdir -p ${USER_SPACK_ROOT}
[maijam@puhti-login11 ~]$ module load spack/v0.18-user
Run user-spack-init to initialize user installation in /projappl/project_2001234/spack-instance-1
[maijam@puhti-login11 ~]$ user-spack-init
[INFO] USER_SPACK_GROUP not set, defaulting to project_2001234 based on target directory
```

!!! note
    You have to purge all default environment compiler and
    library modules as they may interfere with Spack builds.
!!! note
    You can have several Spack instances under same project. The
    instance is selected by the USER_SPACK_ROOT environment variable
    that points to the root directory of the instance.
!!! note When
    the Spack instance is accessed for the first time, you have to
    initialize it with `user-spack-init` command.

## Using the Spack instance

An initialized instance can be activated by cleaning up the module
environment, setting the root path of the instance and loading the
Spack module:

```bash
[maijam@puhti-login11 ~]$ module purge
The following modules were not unloaded:
  (Use "module --force purge" to unload all):

  1) csc-tools
[maijam@puhti-login11 ~]$ export USER_SPACK_ROOT=/projappl/project_2001234/spack-instance-1
[maijam@puhti-login11 ~]$ module load spack/v0.18-user
Found existing user spack installation at /projappl/project_2001234/spack-instance-1
[maijam@puhti-login11 ~]$
```

Example build:
```bash
[maijam@puhti-login11 ~]$ spack spec -I --reuse kakoune
Input spec
--------------------------------
 -   kakoune

Concretized
--------------------------------
 -   kakoune@2021.11.08%gcc@11.3.0 arch=linux-rhel8-cascadelake
[^]      ^ncurses@6.2%gcc@11.3.0~symlinks+termlib abi=none arch=linux-rhel8-cascadelake
[^]          ^pkgconf@1.8.0%gcc@11.3.0 arch=linux-rhel8-cascadelake
[maijam@puhti-login11 ~]$ spack install --reuse kakoune
[+] /appl/spack/v018/install-tree/gcc-11.3.0/pkgconf-1.8.0-2hkydh
[+] /appl/spack/v018/install-tree/gcc-11.3.0/ncurses-6.2-n4phtn
==> Installing kakoune-2021.11.08-yh4nmfid4st4l7gsmuzqv43o6qt6ckrm
==> No binary for kakoune-2021.11.08-yh4nmfid4st4l7gsmuzqv43o6qt6ckrm found: installing from source
==> Using cached archive: /local_scratch/maijam/spack-build-project_2002567/source-cache/_source-cache/archive/aa/aa30889d9da11331a243a8f40fe4f6a8619321b19217debac8f565e06eddb5f4.tar.bz2
==> No patches needed for kakoune
==> kakoune: Executing phase: 'edit'
==> kakoune: Executing phase: 'build'
==> kakoune: Executing phase: 'install'
==> kakoune: Successfully installed kakoune-2021.11.08-yh4nmfid4st4l7gsmuzqv43o6qt6ckrm
  Fetch: 0.00s.  Build: 34.31s.  Total: 34.31s.
[+] /projappl/project_2001234/spack-instance-1/install_tree/gcc-11.3.0/kakoune-2021.11.08-yh4nmf
```

## Using modules with user Spack installations

By default the modules are installed under `$USER_SPACK_ROOT/modules`
and you can add that path to module path with command:
```bash
module use ${USER_SPACK_ROOT}/modules
```

After the `module use` command you can see the modules with regular
`module avail` and `module spider` commands. For example, the kakoune
editor build of the previous example can be loaded with command

```bash
module load kakoune
```

## Further reading

- Spack documentation: [https://spack.readthedocs.io/en/latest/index.html](https://spack.readthedocs.io/en/latest/index.html)
- Spack tutorial: [https://spack.readthedocs.io/en/latest/tutorial.html](https://spack.readthedocs.io/en/latest/tutorial.html)
- Spack github repository: [https://github.com/spack/spack](https://github.com/spack/spack)
