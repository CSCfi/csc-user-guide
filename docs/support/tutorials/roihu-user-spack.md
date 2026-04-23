# Using Spack to install software in Roihu

Roihu's scientific software stack is maintained using Spack package
manager.  This document describes how regular users can use Spack
to install additional software, libraries and applications, on top of
the already installed software.

Throughout this document, we use a package `eccodes` as an example,
and assume that the commands are run in user's custom software install
root, usually somewhere under `/projappl/<project>/$USER`.

In addition to this tutorial style documentation, please refer to the
full
[Spack documentation](https://spack.readthedocs.io/en/v1.1.1/index.html).
For example, term "environment" in this document specifically refers to
[Spack environments](https://spack.readthedocs.io/en/latest/environments.html).


## When to install with Spack

Spack installation is a viable option for "traditional" HPC software,
parallel applications and the libraries they depend on, especially
when Spack package recipies already exist. Using Spack is an
alternative to traditional "manual" installation, loading modules,
running configure or cmake, and make, for the application and it's
dependencies.

Usually containers are better approach when the number of files in the
installation goes to tens of thousands, which is often the case for
Python and R environments, for example.


## What software is available as a Spack package

The Spack packages can be searched from
[Spack Packages](https://packages.spack.io) (the latest versions), or
directly from Roihu directory
`/appl/soft/spack/v2026_03/spack-packages/repos/spack_repo/builtin/packages`,
which contains almost 9000 package definitions.


## How to set up Spack

First, let's initialize Spack. In here we set Spack cache directory to
temporary directory, which is fine for one shot installations, and
isolate Spack from system and user configuration scopes, so that no
settings from those scopes leak into our setup. See
[Overriding local configuration](https://spack.readthedocs.io/en/v1.1.1/configuration.html#overriding-local-configuration)
for details.

```console
$ source /appl/soft/spack/v2026_03/spack/share/spack/setup-env.sh
$ source /appl/soft/spack/v2026_03/spack/share/spack/bash/spack-completion.bash
$ export SPACK_USER_CACHE_PATH=$TMPDIR/spack
$ export SPACK_DISABLE_LOCAL_CONFIG=true
```


## How the Spack system installation is organised, and what is installed already

The different versions of Spack itself are installed in
`/appl/soft/spack`. At the time of writing this, the latest installed
Spack version is in

`/appl/soft/spack/v2026_03`

The corresponding core environments and the application environments
(built on top of the core environments) are in directories

```
/appl/soft/spack/core/v2026_03/$target_family
/appl/soft/spack/apps/v2026_03/$target_family
```

where `$target_family` is either `x86_64` or `aarch64`, referring to
the processor architecture on the CPU or the GPU nodes, respectively.

In general, the core environments provide a good base, "upstream"
package environment, to build on. Core environments contain compilers
and most common libraries, such as MPI libraries, already configured
work efficiently.

The available environments can be listed for example with

```console
ls /appl/soft/spack/core/v2026_03/x86_64/
```

```output
aocc50_ec  compilers_ce  compilers_ec  gcc152_ec
```

The name of the environment gives a hint what is available in the
environment, for example `gcc152_ec` has GNU version 15.2 compiler
collection, and the most commonly used libraries built with the
compiler for the CPU nodes.

The packages in the upstream environment can be listed, for example,
with command

```console
$ spack -c 'upstreams:gcc152_ec:install_tree:/appl/soft/spack/core/v2026_03/x86_64/gcc152_ec/install_dir' find
-- linux-rhel9-x86_64 / %c=gcc@15.2.0 ---------------------------
knem@1.1.4

-- linux-rhel9-x86_64 / no compilers ----------------------------
gcc@15.2.0  glibc@2.34  lustre@2.14.0  rdma-core@54.0  slurm@25.05.3

-- linux-rhel9-zen5 / %c,cxx,fortran=gcc@15.2.0 -----------------
openblas@0.3.30  openmpi@5.0.10  papi@7.2.0

-- linux-rhel9-zen5 / %c,cxx=gcc@15.2.0 -------------------------
berkeley-db@18.1.40  c-blosc@1.21.6  eigen@5.0.1  gettext@1.0  krb5@1.22.2   lz4@1.10.0      ncurses@6.6     openssl@3.6.1  ucx@1.20.0
bison@3.8.2          cmake@3.31.11   expat@2.7.4  hwloc@2.4.1  libaec@1.1.4  m4@1.4.21       nghttp2@1.67.1  python@3.14.3  zlib-ng@2.3.3
boost@1.88.0         curl@8.18.0     ffmpeg@7.1   icu4c@74.2   libffi@3.5.2  mimalloc@3.2.7  openssh@10.2p1  snappy@1.2.1   zstd@1.5.7

-- linux-rhel9-zen5 / %c,fortran=gcc@15.2.0 ---------------------
fftw@3.3.10  netcdf-fortran@4.6.2  netlib-lapack@3.12.1  netlib-scalapack@2.2.2

-- linux-rhel9-zen5 / %c=gcc@15.2.0 -----------------------------
alsa-lib@1.2.15.3  diffutils@3.12    gmake@4.4.1  libbsd@0.12.2         libiconv@1.18    libtool@2.5.4    nasm@2.16.03    perl@5.42.0    readline@8.3   util-linux-uuid@2.41
automake@1.18.1    findutils@4.10.0  gsl@2.8      libedit@3.1-20240808  libmd@1.1.0      libxcrypt@4.5.2  netcdf-c@4.9.3  pigz@2.8       sqlite@3.51.2  xz@5.8.2
bzip2@1.0.8        gdbm@1.26         hdf5@1.14.6  libevent@2.1.12       libsigsegv@2.15  libxml2@2.15.1   numactl@2.0.19  pkgconf@2.5.1  tar@1.35

-- linux-rhel9-zen5 / %cxx=gcc@15.2.0 ---------------------------
kokkos@5.0.2

-- linux-rhel9-zen5 / no compilers ------------------------------
autoconf@2.72  compiler-wrapper@1.0  gcc-runtime@15.2.0
==> 73 installed packages
```


## How to set up a custom environment for the installs

The overall plan is to set up a custom environment that uses as many
already existing installed packages from the system core environment
(upstream) as possible, and installs the missing ones in a custom
install tree. Multiple environments can use the same install trees.

The commands

```console
$ spack env create environments/mygcc152_ec
$ spack env activate -p environments/mygcc152_ec
```

create the initial version of the file defining the environment,
`environments/mygcc152_ec/spack.yaml`, and make the following spack
commands to act within the environment. If you plan to install multiple
versions of the same packages in the environment, consider adding
option `--without-view` option to
[spack env activate](https://spack.readthedocs.io/en/v1.1.1/environments.html#activating-an-environment)
command.

Similar to defining `SPACK_USER_CACHE_PATH`, we need to override some
default settings, so that they do not point to default
system locations (which are not writable by users):

```console
[mygcc152_ec] $ spack config add 'config:source_cache:$spack_user_cache/source-cache'
```

The chosen upstream environment and the location of our custom environment's
actual software install root can be added to environment configuration
(`spack.yaml` file) with commands

```console
[mygcc152_ec] $ spack config add 'upstreams:gcc152_ec:install_tree:/appl/soft/spack/core/v2026_03/x86_64/gcc152_ec/install_dir'
[mygcc152_ec] $ spack config add 'config:install_tree:root:$PWD/mygcc152_ec-install'
```

Optionally, you can also add other configuration settings, for example
flatten the default hierarchy in the install tree and use short
hashes:

```console
[mygcc152_ec] $ spack config add 'config:install_tree:projections:all:"{name}-{version}-{hash:7}"'
```

The final step in the custom environment configuration is to define what to install to the environment:

```console
[mygcc152_ec] $ spack add eccodes
```

In Spack terminology `eccodes` above is a
[spec](https://spack.readthedocs.io/en/v1.1.1/spec_syntax.html),
defining the exact
configuration of the software to be installed. Obviously `eccodes` is
quite abstract, yet. Next we will refine it.


## Refining the spec and installing

Often the defaults are ok, but it is always best to check the
concretized spec before installing:

```console
[mygcc152_ec] $ spack concretize
==> Fetching https://ghcr.io/v2/spack/bootstrap-buildcache-v2.2/blobs/sha256:2010a2a50b9620c2bda7c5fa4e9ce137a115dbba35094857fecc819d9a00a789
==> Fetching https://ghcr.io/v2/spack/bootstrap-buildcache-v2.2/blobs/sha256:31f1649728e2d58902eb62d1c2e37b1cfc73e007089322a17463b3cb5777cb98
==> Installing "clingo-bootstrap@=spack~apps~docs+ipo+optimized+python+static_libstdcpp build_system=cmake build_type=Release commit=2a025667090d71b2c9dce60fe924feb6bde8f667 generator=make patches:=bebb819,ec99431 platform=linux os=centos7 target=x86_64" from a buildcache
==> Concretized 1 spec:
 -   bc5ld7m  eccodes@2.45.0+aec~fortran~ipo~memfs~netcdf~openmp~png~pthreads+shared~tools build_system=cmake build_type=Release extra_definitions:=none generator=make jp2k=openjpeg platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  zwnvbda      ^cmake@3.31.11~doc+ncurses+ownlibs~qtgui build_system=generic build_type=Release platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  lrippm6          ^curl@8.18.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2+nghttp2 build_system=autotools libs:=shared,static tls:=openssl platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  45i4fsq              ^nghttp2@1.67.1 build_system=autotools platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  wxvpbhd                  ^diffutils@3.12 build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  3n6hlmz                      ^libiconv@1.18 build_system=autotools libs:=shared,static platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  gouvek3              ^openssl@3.6.1~docs+shared build_system=generic certs=system platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  lo2oqga                  ^perl@5.42.0+cpanm+opcode+open+shared+threads build_system=generic platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  osujnxv                      ^berkeley-db@18.1.40+cxx~docs+stl build_system=autotools patches:=26090f4,b231fcc platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  tmpzrkl                      ^bzip2@1.0.8~debug~pic+shared build_system=generic platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  nc55qc5                      ^gdbm@1.26 build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  lr4bql4                          ^readline@8.3 build_system=autotools patches:=21f0a03 platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  5psyrcf              ^pkgconf@2.5.1 build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[e]  i7ouzvl          ^gcc@15.2.0+binutils+bootstrap~graphite+libsanitizer~mold~nvptx~piclibs~profiled~strip build_system=autotools build_type=RelWithDebInfo languages:='c,c++,fortran,jit' platform=linux os=rhel9 target=x86_64
[^]  yi5ecvd          ^gcc-runtime@15.2.0 build_system=generic platform=linux os=rhel9 target=zen5
[^]  kztfkls          ^ncurses@6.6~symlinks+termlib abi=none build_system=autotools patches:=7a351bc platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  turbkrl          ^zlib-ng@2.3.3+compat+new_strategies+opt+pic+shared build_system=autotools platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  iglv3xy      ^compiler-wrapper@1.0 build_system=generic platform=linux os=rhel9 target=zen5
[e]  fx7oixv      ^gcc@15.2.0+binutils+bootstrap~graphite+libsanitizer~mold~nvptx~piclibs~profiled~strip build_system=autotools build_type=RelWithDebInfo languages:='c,c++,fortran' platform=linux os=rhel9 target=x86_64
 -   szq7ch3      ^gcc-runtime@15.2.0 build_system=generic platform=linux os=rhel9 target=zen5
[e]  45if5qv      ^glibc@2.34 build_system=autotools platform=linux os=rhel9 target=x86_64
[^]  jvnmnyr      ^gmake@4.4.1~guile build_system=generic platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  elazd5o      ^libaec@1.1.4~ipo+shared build_system=cmake build_type=Release generator=make platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
 -   szh7ud6      ^openjpeg@2.3.1~codec~ipo build_system=cmake build_type=Release generator=make platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0

==> Updating view at /users/jlento/user-spack/environments/mygcc152_ec/.spack-env/view
```

There are some keypoints to check in the concretized spec. First,
we need to check that the variant (build options) are what we
want. In the case of eccodes we can compare the current spec

```
eccodes@2.45.0+aec~fortran~ipo~memfs~netcdf~openmp~png~pthreads+shared~tools build_system=cmake build_type=Release extra_definitions:=none generator=make jp2k\
=openjpeg platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
```

against the spec of the eccodes installation in Mahti

```
eccodes@2.34.0+aec+fortran~ipo+memfs~netcdf+openmp+png~pthreads+shared~tools build_system=cmake build_type=Release extra_definitions=none generator=make jp2k=jasper
```

We notice the version number update, which is fine, but then we notice
that variants `fortran` (fortran interface), `memfs` (some definition
data in the library/memory instead of in small files on disc),
`openmp` (thread support), `png` are marked with `~`, which means that
those configuration options (variants) are not set. In addition, we'd
like to include variant `tools`, which builds command line tools with
the library. The last thing we notice is that the compression library
is openjpeg instead of jasper (fine?).

Let's update the variant information, and reconcretize (omitting the output):

```console
[mygcc152_ec] $ spack change 'eccodes@2.45.0+aec+fortran~ipo+memfs~netcdf+openmp+png~pthreads+shared+tools'
[mygcc152_ec] $ spack concretize
```

Now the variant is correct. Next we check that Spack is actually using
the packages that are already installed in the upstream
environment. The information is in the first column of the concretized
spec. Entry ` - ` means that the package will be installed, `[^]`
tells Spack will use the already existing upstream installation, and
`[e]` stands for "external", defined separately in configuration. Here
all looks fine, and we can proceed to installation

```console
[mygcc152_ec] $ spack install
```

## Using the environment

The actual software installs are in the directory
`$PWD/mygcc152_ec-install` that we set earlier in the environment
configuration:

```console
[mygcc152_ec] $ ls mygcc152_ec-install/
bin  eccodes-2.45.0-4fi3e5d  gcc-runtime-15.2.0-szq7ch3  libpng-1.6.55-dhucqwk  openjpeg-2.3.1-szh7ud6
```

If the environment was activated with the view, the installed software and libraries
are also accessible through environment's
[view](https://spack.readthedocs.io/en/latest/environments.html#environment-views),
which in this tutorial example is in `environments/mygcc152_ec/.spack-env/view`.

Command

```console
[mygcc152_ec] $ spack env deactivate
```

will deactivate the current Spack environment.

