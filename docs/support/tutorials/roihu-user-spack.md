# Using Spack to install software in Roihu

Roihu's scientific software stack is maintained using Spack package
manager.  This document describes how regular users can use Spack
to install additional software, libraries and applications, on top of
the already installed software.

Throughout this document, we assume that the commands are run in user's
custom software install root, usually somewhere under `/projappl/<project>/${USER}`.

In addition to this tutorial style documentation, please refer to the
full
[Spack documentation](https://spack.readthedocs.io/en/v1.1.1/index.html).
For example, term "environment" in this document specifically refers to
[Spack environments](https://spack.readthedocs.io/en/latest/environments.html).

!!! warning "Work in progress"
    This section is a work in progress. Some steps may be outdated,
    incomplete, or not fully tested in the current Roihu environment.
    Use with caution and report any issues you encounter.


## When to install with Spack

Spack installation is a viable option for "traditional" HPC software,
parallel applications and the libraries they depend on, especially
when Spack package recipes already exist. Using Spack is an
alternative to traditional "manual" installation, loading modules,
running configure or cmake, and make, for the application and its
dependencies.

Usually containers are a better approach when the number of files in the
installation goes to tens of thousands, which is often the case for
Python and R environments, for example.


## What software is available as a Spack package

The Spack packages can be searched from
[Spack Packages](https://packages.spack.io) (the latest versions), or
directly from the Roihu directory
`/appl/soft/spack/v2026_03/spack-packages/repos/spack_repo/builtin/packages`,
which contains almost 9000 package definitions.


## How to set up Spack

First, let's initialize Spack. In here we set the Spack cache directory to
temporary directory, which is fine for one-shot installations, and
isolate Spack from system and user configuration scopes, so that no
settings from those scopes leak into our setup. See
[Overriding local configuration](https://spack.readthedocs.io/en/v1.1.1/configuration.html#overriding-local-configuration)
for details.

```console
export SPACK_USER_CACHE_PATH=$TMPDIR/spack
export SPACK_DISABLE_LOCAL_CONFIG=true
source /appl/soft/spack/v2026_03/spack/share/spack/setup-env.sh
source /appl/soft/spack/v2026_03/spack/share/spack/bash/spack-completion.bash
```


## How the Spack system installation is organised, and what is installed already

The different versions of Spack itself are installed in
`/appl/soft/spack`. At the time of writing this, the latest installed
Spack version is in `/appl/soft/spack/v2026_03`.

The corresponding core environments and the application environments
(built on top of the core environments) are in directories

```
/appl/soft/spack/core/v2026_03/${target_family}
/appl/soft/spack/apps/v2026_03/${target_family}
```

where `$target_family` is either `x86_64` or `aarch64`, referring to
the processor architecture on the CPU or the GPU nodes, respectively.

In general, the core environments provide a good base, "upstream"
package environment, to build on. Core environments contain compilers
and most common libraries, such as MPI libraries, already configured to
work efficiently.

The available environments can be listed, for example, with

```console
ls /appl/soft/spack/core/v2026_03/x86_64/
```

which (at the time of writing this) gives

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
spack -E -c 'upstreams:gcc152_ec:install_tree:/appl/soft/spack/core/v2026_03/x86_64/gcc152_ec/install_dir' find -l
```

which gives

```output
-- linux-rhel9-x86_64 / %c=gcc@15.2.0 ---------------------------
vshzxn2 knem@1.1.4

-- linux-rhel9-x86_64 / no compilers ----------------------------
nsx4vac gcc@15.2.0  45if5qv glibc@2.34  jix3h7v lustre@2.14.0  aeadm2n rdma-core@54.0  fkinzg5 slurm@25.05.3

-- linux-rhel9-zen5 / %c,cxx,fortran=gcc@15.2.0 -----------------
2d66cws hdf5@1.14.6  qskucwe openblas@0.3.30  jtu4mle openmpi@5.0.10  ad53otu papi@7.2.0  msn34e2 parallel-netcdf@1.14.1

-- linux-rhel9-zen5 / %c,cxx=gcc@15.2.0 -------------------------
5jgdak6 berkeley-db@18.1.40  5huzpbm curl@8.18.0  ctjvy35 hwloc@2.4.1   gavswuq lz4@1.10.0      n2yix5u openssh@10.2p1              35almze ucx@1.20.0
bwi6e4z bison@3.8.2          qjlzhxn eigen@5.0.1  sa7jjuo icu4c@74.2    57nb6no m4@1.4.21       3a2xrgw openssl@3.6.1               siciate zlib-ng@2.3.3
niyho5a boost@1.88.0         m3d4hr2 expat@2.7.4  ro346yy krb5@1.22.2   b5ymicp mimalloc@3.2.7  be236m7 osu-micro-benchmarks@7.5.2  pvz4ljc zstd@1.5.7
dhosjnx c-blosc@1.21.6       bkrrw3k ffmpeg@7.1   5ddtnbo libaec@1.1.4  ezw6kfg ncurses@6.6     qvwhx54 python@3.14.3
dkj6m2a cmake@3.31.11        sgerwwx gettext@1.0  6neer47 libffi@3.5.2  zj62cb6 nghttp2@1.67.1  xjllls2 snappy@1.2.1

-- linux-rhel9-zen5 / %c,fortran=gcc@15.2.0 ---------------------
gafrwzb fftw@3.3.10  ilpb6cd netcdf-fortran@4.6.2  lagqyzt netlib-lapack@3.12.1  stnq2qp netlib-scalapack@2.2.2

-- linux-rhel9-zen5 / %c=gcc@15.2.0 -----------------------------
w5oytoe alsa-lib@1.2.15.3  rd2uuxx gdbm@1.26             kcjhrtc libevent@2.1.12  ddibcjq libxcrypt@4.5.2  ejivk2i perl@5.42.0    rzwegeu tar@1.35
os67qlb automake@1.18.1    3jmx5cd gmake@4.4.1           anayviw libiconv@1.18    6mr7zcy libxml2@2.15.1   b5e6x6u pigz@2.8       it55vd4 util-linux-uuid@2.41
an5rzrc bzip2@1.0.8        lsilpvy gsl@2.8               i3l5zsd libmd@1.1.0      jwkph32 nasm@2.16.03     btxv56s pkgconf@2.5.1  vk7ckqw xz@5.8.2
72jfleb diffutils@3.12     dl3mtdk libbsd@0.12.2         qurnpw5 libsigsegv@2.15  pcod7dd netcdf-c@4.9.3   lf5ljls readline@8.3
p4i5zpo findutils@4.10.0   vbo25pf libedit@3.1-20240808  dbbnpoy libtool@2.5.4    zvxjta5 numactl@2.0.19   3m5q6wh sqlite@3.51.2

-- linux-rhel9-zen5 / %cxx=gcc@15.2.0 ---------------------------
t4kg5zu kokkos@5.0.2

-- linux-rhel9-zen5 / no compilers ------------------------------
5e4345x autoconf@2.72  iglv3xy compiler-wrapper@1.0  uaq7tuq gcc-runtime@15.2.0
==> 75 installed packages
```

The seven character string in front of the package name is a hash that we can use to refer to particular concretized spec or install.


## How to set up a custom environment for the installs

The overall plan is to set up a custom environment that uses as many
already existing installed packages from the system core environment
(upstream) as possible, and installs the missing ones in a custom
install tree. Multiple environments can use the same install trees.

The basic setup for different custom environments is very similar. I'll set a shell variable
`${upstream}` to point to selectted upstream core environment, and use
[Spack specific variable](https://spack.readthedocs.io/en/v1.1.1/configuration.html#config-file-variables),
such as ${target_family}`, which Spack expands when interpreting it's configuration files.
The quoting in the examples prevents shell from expanding Spack specific variables.

```console
upstream=gcc152_ec
```

The commands

```console
spack env create environments/my_${upstream}
spack env activate -p environments/my_${upstream}
```

create the initial version of the file defining the environment,
`environments/my_gcc152_ec/spack.yaml`, and make the following spack
commands to act within the environment. If you plan to install multiple
versions of the same packages in the environment, consider adding
option `--without-view` option to
[spack env activate](https://spack.readthedocs.io/en/v1.1.1/environments.html#activating-an-environment)
command.

Next, we set up the environment configuration, by defining

- the upstream environment
- the packages that should be treated specially (configuration taken from the upstream environment)
- the location of our custom environment's actual software install root
- the source cache directory (the default one is not writable by regular users)
- flatten the default hierarchy in the install tree and use short hashes

```console
spack config add upstreams:${upstream}:install_tree:/appl/soft/spack/core/v2026_03/'${target_family}'/${upstream}/install_dir
spack config add 'include:[/appl/soft/spack/v2026_03/spackconf/config_${target_family}/packages.yaml]'
spack config add config:install_tree:root:$PWD/my_${upstream}-install
spack config add config:source_cache:source-cache
spack config add 'config:install_tree:projections:all:"{name}-{version}-{hash:7}"'
```

All these commands simply change the file `environments/my_gcc152_ec/spack.yaml`.
Alternatively, you can make the changes editing the file directly.

The final step in the custom environment configuration is to define what to install to the environment:

```console
spack add eccodes
```

In Spack terminology `eccodes` above is a
[spec](https://spack.readthedocs.io/en/v1.1.1/spec_syntax.html),
defining the exact
configuration of the software to be installed. Obviously `eccodes` is
quite abstract, yet. Next we will refine it.


## Refining the spec and installing

Often the defaults are ok, but it is always best to check the
concretized spec before installing. Command

```console
spack concretize
```

shows the concretized spec

```output
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

There are some key points to check in the concretized spec. First,
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

Let's update the variant information, and reconcretize (the output of
the command is omitted as it is similar to the previous output from
`spack concretize` command):

```console
spack change 'eccodes@2.45.0+aec+fortran~ipo+memfs~netcdf+openmp+png~pthreads+shared+tools'
spack concretize
```

Now the variant is correct. Next, we check that Spack is actually using
the packages that are already installed in the upstream
environment. The information is in the first column of the concretized
spec. Entry ` - ` means that the package will be installed, `[^]`
tells Spack will use the already existing upstream installation, and
`[e]` stands for "external", defined separately in configuration. Here
all looks fine, and we can proceed to installation

```console
spack install
```


## What to do when concretization is not using an upstream dependency

Sometimes there are `-` entries in the concretization for the dependency
packages that would be available in the upstream. The concretization of
`eccodes` used packages installed in the upstream, so let's try to install something
slightly more difficult:

```console
spack add 'vasp+hdf5+openmp'
spack concretize
```

```output
 -   rfhap2d  vasp@6.5.1~cuda+fftlib+hdf5~libbeef~libxc+openmp+shmem~wannier90 build_system=makefile platform=linux os=rhel9 target=zen5 %c,cxx,fortran=gcc@15.2.0
[^]  iglv3xy      ^compiler-wrapper@1.0 build_system=generic platform=linux os=rhel9 target=zen5
 -   bska4tv      ^fftw@3.3.10+mpi+openmp~pfft_patches+shared build_system=autotools patches:=872cff9 precision:=double,float platform=linux os=rhel9 target=zen5 %c,fortran=gcc@15.2.0
[e]  jzf6h3h      ^gcc@15.2.0+binutils+bootstrap~graphite+libsanitizer~mold~nvptx~piclibs~profiled~strip build_system=autotools build_type=RelWithDebInfo languages:='c,c++,fortran' platform=linux os=rhel9 target=x86_64
 -   qgv5zle      ^gcc-runtime@15.2.0 build_system=generic platform=linux os=rhel9 target=zen5
[e]  45if5qv      ^glibc@2.34 build_system=autotools platform=linux os=rhel9 target=x86_64
[^]  3jmx5cd      ^gmake@4.4.1~guile build_system=generic platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[e]  nsx4vac          ^gcc@15.2.0+binutils+bootstrap~graphite+libsanitizer~mold~nvptx~piclibs~profiled~strip build_system=autotools build_type=RelWithDebInfo languages:='c,c++,fortran,jit' platform=linux os=rhel9 target=x86_64
[^]  uaq7tuq          ^gcc-runtime@15.2.0 build_system=generic platform=linux os=rhel9 target=zen5
 -   qlknyrh      ^hdf5@1.14.6~cxx+fortran~hl~ipo~java~map+mpi+shared~subfiling~szip~threadsafe+tools api=default build_system=cmake build_type=Release generator=make platform=linux os=rhel9 target=zen5 %c,fortran=gcc@15.2.0
[^]  dkj6m2a          ^cmake@3.31.11~doc+ncurses+ownlibs~qtgui build_system=generic build_type=Release platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  5huzpbm              ^curl@8.18.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2+nghttp2 build_system=autotools libs:=shared,static tls:=openssl platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  zj62cb6                  ^nghttp2@1.67.1 build_system=autotools platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  ezw6kfg              ^ncurses@6.6~symlinks+termlib abi=none build_system=autotools patches:=7a351bc platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  btxv56s          ^pkgconf@2.5.1 build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  siciate          ^zlib-ng@2.3.3+compat+new_strategies+opt+pic+shared build_system=autotools platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
 -   yswx35z      ^netlib-scalapack@2.2.2~ipo~pic+shared build_system=cmake build_type=Release generator=make platform=linux os=rhel9 target=zen5 %c,fortran=gcc@15.2.0
[^]  qskucwe      ^openblas@0.3.30~bignuma~consistent_fpcsr+dynamic_dispatch+fortran~ilp64+locking+pic+shared build_system=makefile symbol_suffix=none threads=openmp platform=linux os=rhel9 target=zen5 %c,cxx,fortran=gcc@15.2.0
 -   zxmpyf5      ^openmpi@5.0.10+atomics~cuda~debug+fortran~gpfs~internal-hwloc~internal-libevent~internal-pmix~ipv6~java~lustre~memchecker~openshmem~rocm~romio+rsh~static~two_level_namespace+vt+wrapper-rpath build_system=autotools fabrics:=none romio-filesystem:=none schedulers:=none platform=linux os=rhel9 target=zen5 %c,cxx,fortran=gcc@15.2.0
[^]  5e4345x          ^autoconf@2.72 build_system=autotools platform=linux os=rhel9 target=zen5
[^]  57nb6no              ^m4@1.4.21+sigsegv build_system=autotools platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  72jfleb                  ^diffutils@3.12 build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  qurnpw5                  ^libsigsegv@2.15 build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  os67qlb          ^automake@1.18.1 build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  ctjvy35          ^hwloc@2.4.1~cairo~cuda~gl~level_zero~libudev+libxml2~netloc~nvml~opencl~pci~rocm build_system=autotools libs:=shared,static platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  6mr7zcy              ^libxml2@2.15.1+pic~python+shared build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  vk7ckqw                  ^xz@5.8.2~pic build_system=autotools libs:=shared,static platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  kcjhrtc          ^libevent@2.1.12+openssl build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  dbbnpoy          ^libtool@2.5.4 build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  p4i5zpo              ^findutils@4.10.0 build_system=autotools patches:=440b954 platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  sgerwwx                  ^gettext@1.0+bzip2+curses+git~libunistring+libxml2+pic+shared+tar+xz build_system=autotools platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  rzwegeu                      ^tar@1.35 build_system=autotools zip=pigz platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  b5e6x6u                          ^pigz@2.8 build_system=makefile platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  zvxjta5          ^numactl@2.0.19 build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  n2yix5u          ^openssh@10.2p1+gssapi build_system=autotools platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  ro346yy              ^krb5@1.22.2+shared build_system=autotools platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  bwi6e4z                  ^bison@3.8.2~color build_system=autotools platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  vbo25pf              ^libedit@3.1-20240808 build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  ddibcjq              ^libxcrypt@4.5.2~obsolete_api build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  ejivk2i          ^perl@5.42.0+cpanm+opcode+open+shared+threads build_system=generic platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  5jgdak6              ^berkeley-db@18.1.40+cxx~docs+stl build_system=autotools patches:=26090f4,b231fcc platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  an5rzrc              ^bzip2@1.0.8~debug~pic+shared build_system=generic platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  rd2uuxx              ^gdbm@1.26 build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  lf5ljls                  ^readline@8.3 build_system=autotools patches:=21f0a03 platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
 -   utr7ymg          ^pmix@6.1.0~munge~python build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
 -   ccotrup          ^prrte@4.1.0 build_system=autotools schedulers:=none platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
 -   syzfpop              ^flex@2.6.3+lex~nls build_system=autotools platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
 -   24qltll      ^rsync@3.4.1 build_system=autotools platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  gavswuq          ^lz4@1.10.0+pic build_system=makefile libs:=shared,static platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  3a2xrgw          ^openssl@3.6.1~docs+shared build_system=generic certs=system platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
 -   m2nrnpe          ^popt@1.19 build_system=autotools platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
[^]  anayviw              ^libiconv@1.18 build_system=autotools libs:=shared,static platform=linux os=rhel9 target=zen5 %c=gcc@15.2.0
 -   fre4ogj          ^xxhash@0.8.3 build_system=makefile platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
[^]  pvz4ljc          ^zstd@1.5.7+programs build_system=makefile compression:=none libs:=shared,static platform=linux os=rhel9 target=zen5 %c,cxx=gcc@15.2.0
```

The above concretization shows that if we would
proceed to `spack install`, spack would rebuild and install `fftw`, `hdf5` and `openmpi`
packages, among some others, that should come from the upstream. Usually it is best to start
fixing from the first such package in the concretization, here `fftw`.

Let's first verify that the upstream package actually is suitable, by comparing
the spec of the upstream package and the spec in the concretization. A particular upstream
package spec can printed referring it's hash (note the syntax with `/`):

```console
spack -E -c 'upstreams:gcc152_ec:install_tree:/appl/soft/spack/core/v2026_03/x86_64/gcc152_ec/install_dir' spec /gafrwzb
```

In this case the specs for the `fftw` packages in the environment concretization and in the upstream look identical,
so the upstream package should be fine.

Let's update the vasp spec in the environment by specifying which exact `fftw` package to use as a dependency.
For some reason `spack change` does not work here, but we can update the `spack.yaml` file in the environment
with two commands (or alternatively edit the `spack.yaml` file directly):

```console
spack remove vasp
spack add 'vasp+hdf5+openmp ^*/gafrwzb'
```

Notice the syntax how to specify the dependency using it's hash.

In this case fixing the first dependency also fixed all the others in the concretized spec, and
we can proceed to `spack install`.


## Using the environment

The actual software installs are in the directory
`$PWD/mygcc152_ec-install` that we set earlier in the environment
configuration. Command

```console
ls mygcc152_ec-install
```

shows the install roots:

```output
bin  eccodes-2.45.0-4fi3e5d  gcc-runtime-15.2.0-szq7ch3  libpng-1.6.55-dhucqwk  openjpeg-2.3.1-szh7ud6
```

Different versions (variants, anything different in the concretized spec) of the packages
are installed with unique hashes.

If the environment was activated with the view, the installed software and libraries
are also accessible through environment's
[view](https://spack.readthedocs.io/en/latest/environments.html#environment-views),
which in this tutorial example is in `environments/mygcc152_ec/.spack-env/view`.

Command

```console
spack env deactivate
```

will deactivate the current Spack environment.

