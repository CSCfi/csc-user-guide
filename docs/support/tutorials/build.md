# Building software from sources

Building software can be tedious, but it is not difficult &mdash; if you are
familiar with the basic concepts. This document explains the basic concepts.

The material here is only relevant for compiled languages such as C, C++, and
Fortran. Just checking ;-)

## Directories

Usually three directories are involved,

- the *source* root,
- the *build* root, and
- the *install* root.

Source root contains the source code, and is kept intact during the build
process. It is usually created by cloning a source repository or by unpacking a
source tar-file. Build root is a temporary directory where the build is actually
done, and in where the build process writes required temporary files. Install
root is where the final results of the build are copied from the build
directory. Keeping these three separate is a recommended practice.

## Configure, compile, link, and install

### Build tools

Almost all software packages use some build tool (framework) to orchestrate the
different steps in the build process.

The most common build tools are GNU autotools and CMake. The details of
using these is beyond the scope of this document. Usually following the
instructions that come with the software are enough. If you see a file
`configure` or `CMakeLists.txt` in the root of the source directory, the
build tool is likely GNU autotools or CMake, respectively.

There exist a plethora of other build tools and scripts written in Bash, Python,
etc. Often these are a sign of trouble.

A simple, well documented project can sometimes manage well without a build
tool. It all depends on the complexity of the software, the size of the source
code base, the number of external software dependencies, and the number of
supported platforms.

### Configuring a build

The preparation step before actually building a software is called
configuration. In the configuration step, several details are determined:

- which optional features of the software are enabled/disabled
- build tools' and support libraries' locations
- other platform dependent details
- final install location

In a best case scenario, the build tool can figure out all the details, and the
user is only required to tell where the software should finally be installed,

```
./configure --prefix=install-root
```

or

```
cmake source-root -DCMAKE_INSTALL_PREFIX=install-root
```

for GNU Autotools and CMake, respectively. More commonly, one needs to get a bit
more familiar with the build tool in use.

### Compiling

In the compilation step the compiler translates the source language (files with
suffix `.c`, `.cpp`, `.f90`, `.F90`, etc.) to CPU instructions, object/machine
code (files with suffix `.o`). Since different CPU models may have different
instruction sets, and different operating systems have different conventions for
object files (binaries), object files are not necessarily transferable from one
machine to the next.

#### Pre-processing

Just before compiling the source code, the compilers usually run a preprocessing
step, which basically does textual replacements to the source code according to
the preprocessing instructions (source code lines starting with `#`). Common
preprocessing instructions are inclusion of other source code file into the
current source code file (`#include ...`), conditional inclusion or exclusion of
the source code (`#ifdef ...`), and definition of preprocessor textual
replacements and macros (`#define ...`).

#### Compiling object files

Each source file is translated separately to the object code. The mechanism that
the compiler uses to check the interfaces, basically subroutine arguments and
user defined types that are used and defined in different files, differs
slightly between C/C++ and Fortran. C and C++ compilers simply include header
source code files (suffix `.h`), containing the interface declarations, during
the preprocessing step. Fortran compilers generate the interface declarations,
module files (`.mod`), as part of the compilation step. In Fortran this imposes
a dependency between the object files, that needs to be taken care if several
source files are to be compiled in parallel.

| Language | Source files | Compiled files |
| -------  | ------------ | -------------- |
| C        | `.h` `.c`    | `.o`           |
| C++      | `.h` `.cpp`  | `.o`           |
| Fortran  | `.f90`       | `.mod` `.o`    |

Please note, in general *only* C language object files are compatible between
different C compilers and compiler versions, even in the same machine. With
Fortran and C++ it is safest to compile all objects, also in all libraries that
the current project depends on, with the same compiler.

#### Common compiler options

Here I will use the GNU compiler suite as an example, other compilers have
similar options, possibly with slightly different names.

The options that tell the compiler where to find the *include files* and how to
*preprocess* the source code are

- `-I<directory search path>` for include files `.h` and `.mod`
- `-D<PREPROCESSOR OPTION>`

When *developing* a code, turn on all the warnings and runtime checks, including
but not limited to

- `-g` include symbols for debugging, may turn off performance optimizations
- `-fbounds-check` check that array indices are within the bounds in Fortran
- `-Wall`

Also, when developing the code, it is a very good practice to compile the code
with as many different compilers and platforms as possible, to catch as many
bugs as possible with the help of the compilers.

Choosing the best *performance optimization* options is beyond the scope of this
document, but

- `-O2` is usually a good first guess
- `-fopenmp` enables OpenMP thread parallel code generation

The options that change how the compiler treats loosely defined language
constructs, such as `-fdefault-real-8` for Fortran, are usually a "code smell",
something that should be changed in the source code and not "fixed" at compile
time. In general, the less compiler options you need to give, the better.

### Linking

### Installing

### Compiler wrappers

### Common issues

#### Library dependencies

Is the required support library (version) already installed? If not, building it
from the sources is a recursion of this topic...

#### Build tools

What compilation and linking commands the build tool actually runs?

How to tell the build tool which options to add to the compile and link
commands?

- location of the library header files (.h, .mod) and object libraries (.a,
  .so)
- names of the compiler and linker to use
- other compiler and linker options
