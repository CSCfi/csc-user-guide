# Using user Spack module for software installations

Spack is a package manager for supercomputers, Linux and macOS. It can be used
to install complicated scientific software packages easily. CSC installs the
development stack, including compilers, MPI libraries and also many other
libraries and applications using Spack. CSC provides also a user module for
customers that enables per-project software installations using Spack.

!!! warning "Note"
    Spack is an advanced tool and it requires understanding of
    compiling and linking programs.

!!! info "Available versions"
    This tutorial assumes you are on Puhti, which has `spack/v0.18-user`
    installed. Mahti has two versions of Spack available for users,
    `spack/v0.17-user` and `spack/v0.20-user`. Aside from the module versions,
    the outlined procedure is identical on the two systems.

## Creating a Spack instance

Before running the Spack module for the first time, you have to prepare an
installation location that can reside either on `/projappl` or `/scratch` disk
areas. You also have to set an environment variable that points to the location
of the Spack instance.

For example, if you want to create a Spack instance in the `/projappl`
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

!!! info "Purge before loading"
    Before loading Spack, you have to run `module purge` to purge all default
    environment compilers and library modules as they may interfere with Spack
    builds.

!!! info "Several Spack instances"
    You can have several Spack instances under the same project. The used
    instance is specified with the `$USER_SPACK_ROOT` environment variable that
    points to the root directory of the instance.

!!! info "Initializing"
    Before accessing the Spack instance for the first time, you have to
    initialize it by running the `user-spack-init` command.

## Using the Spack instance

An initialized instance can be activated by purging the module environment,
setting the root path of the instance and loading the Spack module:

```bash
[maijam@puhti-login11 ~]$ module purge
The following modules were not unloaded:
  (Use "module --force purge" to unload all):

  1) csc-tools
[maijam@puhti-login11 ~]$ export USER_SPACK_ROOT=/projappl/project_2001234/spack-instance-1
[maijam@puhti-login11 ~]$ module load spack/v0.18-user
Found existing user spack installation at /projappl/project_2001234/spack-instance-1
```

### Example build

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
```

The `spack spec` command shows what would be installed given a certain input.
It is good practice to run it before installing to ensure that the build looks
like intended. The `-I` flag is used to display the current install status of
the package and its dependencies, while the `--reuse` flag is provided in order
to reuse already installed dependencies whenever possible. Actual installation
is then performed via the `spack install` command:

```bash
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

!!! info "Spec syntax"
    The string that specifies which package should be installed (the *spec*)
    can be simply just the package name, as above, but often you might want to
    install a specific version, perhaps using a specific compiler and with some
    optional installation flags (e.g. a GPU-enabled version of the software).
    Spack uses a special syntax for specifying this information as explained in
    the official
    [documentation](https://spack.readthedocs.io/en/latest/basic_usage.html#specs-dependencies).

## Using modules with user Spack installations

By default, Spack creates module files under `$USER_SPACK_ROOT/modules`
and you can add that path to your `$MODULEPATH` with the command:

```bash
[maijam@puhti-login11 ~]$ module use ${USER_SPACK_ROOT}/modules
```

After installing a new package, you may need to regenerate the module files.
For example:

```bash
[maijam@puhti-login11 ~]$ spack module tcl refresh kakoune
```

Now you can see the modules with regular `module avail` and `module spider`
commands. For example, the `kakoune` editor built in the previous example can be
searched and loaded with:

```bash
[maijam@puhti-login11 ~]$ module spider kakoune

--------------------------------
  kakoune: kakoune/2021.11.08-gcc-11.3.0-yh4n
--------------------------------

    This module can be loaded directly: module load kakoune/2021.11.08-gcc-11.3.0-yh4n

[maijam@puhti-login11 ~]$ module load kakoune/2021.11.08-gcc-11.3.0-yh4n
```

## Further reading

- [Official Spack documentation](https://spack.readthedocs.io/en/latest/index.html)
- [Spack tutorial](https://spack.readthedocs.io/en/latest/tutorial.html)
- [Spack GitHub repository](https://github.com/spack/spack)
