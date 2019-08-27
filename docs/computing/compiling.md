# Compiling C/C++ and Fortran applications

In CSC clusters C/C++ and Fortran applications can be build with Intel or GNU compiler 
suites. The Intel module is loaded by default, and it can changed to GNU with the command:
```
module swap intel gcc 
```
Different applications function better with different suites, so selection needs to be done on case
by case basis.

The actual compiler commands for building serial application with the two suites are:

| Compiler suite           | C  | C++ | Fortran |
| :------------- |:-------------| :-----| :----- |
| [Intel](https://software.intel.com/en-us/parallel-studio-xe/documentation/get-started)  | icc  | icpc | ifort |
| [GNU](https://gcc.gnu.org)  | gcc  | g++ | gfortran | 

Intel and GNU compilers use different compiler options, table below lists recommended basic 
optimization flags. It is best to start from the safe level and then move up to intermediate or 
even aggressive, while making sure that the results are correct and that the program has better 
performance.

| Optimisation level  | 	Intel  | 	GNU  | 
| :------------- |:-------------| :-----|
| **Safe**  | -O2 -fp-model precise -fp-model source <br/> (Use all three options. Also options <br/> -fp-model precise -fp-model source with **intermediate** and **aggressive** flags to can be utilized to improve the consistency and reproducibility of floating-point results) | -O2	  | 
| **Intermediate**  | -O2 -xHost	  | -O3 -march=native  | 
| **Aggressive**  | -O3 -xHost -opt-prefetch -unroll-aggressive <br/> -no-prec-div -fp-model fast=2	  | -O3 -march=native <br/> -ffast-math -funroll-loops   | 

Detailed list of options for Intel and GNU compiler can be found from man pages (`man icc/ifort`, 
`man gcc/gfortran` when corresponding programming environment is loaded, or in the compiler 
manuals on the Web (see links above).

All available versions of the compiler suites can be found with

```
module spider intel
module spider gcc
```

## Building MPI applications

There are currently three MPI environments available: **hpcx-mpi**, **mpich**, and **intel-mpi**. 
We recommend to start with **hpcx-mpi**, and try then others if your applications does not work or 
performs badly. All MPI implementations can be used with both Intel and GNU compiler suites. The
MPI environment is taken into use with `module`, i.e.

```
module load hpcx-mpi
```

When building MPI applications, one should use *mpixxx* compiler wrappers, which differ depending
on the compiler suite and MPI environment (XXX table is not correct yet XXX):

| Compiler suite  | hpcx-mpi wrapper | mpich wrapper | intel-mpi wrapper |
| :------------- |:-------------| :-----| :-----|
| Intel          | mpifort     |mpifort, mpiicc, mpi  | mpiifort |
| GNU         | mpigcc, mpig++, mpif90 | mpigcc   | mpiicc |


## Building OpenMP and hybrid applications

Additional compiler and linker flags are needed when building OpenMP or MPI/OpenMP hybrid 
applications:






