# Available Compilers
C, C++ and Fortran are frequently used programming languages in scientific computing. In CSC clusters these languages can be mainly used through two compiler suites. The default compiler package is the Intel Parallel Studio XE. Also GNU Compiler collection is available. The installed intel and gnu compiler releases can be seen by giving these commands:
```
module spider intel
module spider gcc
```
For example to swap the default Intel compiler to the default GNU compiler, give command:
```
module swap intel gcc 
```
Compiler suites information

| Compiler suite           | Module  | Man pages C/C++ , Fortran | Documentation |
| :------------- |:-------------| :-----| :----- |
| [GNU Compiler Collection](https://gcc.gnu.org)  | gcc  | man gcc , man gfortran | [gcc](https://gcc.gnu.org/onlinedocs) |
| [Intel Parallel Studio](https://software.intel.com/en-us/parallel-studio-xe/documentation/get-started)  | intel  | man icc , man ifort | [intel](https://software.intel.com/en-us/node/685016) |

To read a man page of a specific compiler, execute the <var>man</var> command only after having switched to the relevant programming environment.

For Intel Parallel Studio the extensive documentation can be found from the Intel Software pages. The C/C++ documentation under product name [Intel C/C++ Compiler Developer Guide and Reference](https://software.intel.com/en-us/cpp-compiler-developer-guide-and-reference) and the Fortran documentation under product name [Intel Fortran Compiler Developer Guide and Reference](https://software.intel.com/en-us/fortran-compiler-developer-guide-and-reference).

The Intel compiler commands.

| language  | compiler | OpenMPI wrapper | IntelMPI wrapper | 
| :------------- |:-------------| :-----| :-----|
| Fortran   | ifort    | mpifort  | mpiifort |
| C         | icc      | mpigcc   | mpiicc |
| C++       | icpc     | mpic++   | mpiicpc |

The Gnu compiler commands.

| language  | compiler | OpenMPI wrapper | IntelMPI wrapper | 
| :------------- |:-------------| :-----| :-----|
| Fortran   | gfortran | mpifort  | mpif90 |
| C         | gcc      | mpigcc   | mpigcc |
| C++       | g++      | mpic++   | mpigxx |

There are two important factors that should be taken into account when choosing between the compilers: correctness and performance of the compiled program.

* **Correctness:** Some programs may only produce correct results when compiled with a particular compiler. It is also possible that the program produces wrong results when compiled using aggressive compiler optimizations. It is thus of key importance to always check that the compiled program actually produces correct results.
* **Performance:** Choose the compiler giving the best performance, while still producing correct results. It is impossible to know ahead of time which compiler is the best for a particular program. Find the best compiler and its optimal compiler options using a 'generate and check' method.

Intel and GNU compilers use different compiler options. Detailed list of options for Intel and GNU compiler can be found from man pages when corresponding programming environment is loaded, or in the compiler manuals on the Web (see links above).

Table below lists some good optimization flags for the installed compilers. It is best to start from the safe level and then move up to intermediate or even aggressive, while making sure that the results are correct and that the program has better performance.

| Optimisation level  | 	Intel  | 	GNU  | 
| :------------- |:-------------| :-----|
| **Safe**  | -O2 -fp-model precise -fp-model source <br/> (Use all three options. Also options <br/> -fp-model precise -fp-model source with **intermediate** and **aggressive** flags to can be utilized to improve the consistency and reproducibility of floating-point results) | -O2	  | 
| **Intermediate**  | -O2 -xHost	  | -O3 -march=native  | 
| **Aggressive**  | -O3 -xHost -opt-prefetch -unroll-aggressive <br/> -no-prec-div -fp-model fast=2	  | -O3 -march=native <br/> -ffast-math -funroll-loops   | 

Link time optimization methods are available on Intel and GNU compilers. In GNU case read more from [link](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html) (see option -flto) and in Intel case this [link](https://software.intel.com/en-us/articles/step-by-step-optimizing-with-intel-c-compiler) (see IPO optimization).

Basic options that are common for both Intel and GNU compilers:


| Option  | Description  | 
| :------------- |:-------------|
| -c | Compiles only, produces unlinked object *filename*.o   | 
| -o*filename*   | Gives the name filename for the executable. Default:**a.out**  |
| -g  | Produces symbolic debug information |
| -I*dirname*  | Searches directory dirname for for library files specified by -l  |
| -L*dirname*  | Searches directory dirname for for library files specified by -L  |
| -l*libname*  | Searches the specified library file with the name **lib***libname*.a  |
| -O*[level]*  |  Specifies whether to optimize or not and at which level *level*, for example -O0 means turning off optimizations |


