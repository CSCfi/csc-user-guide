# Julia

## Description

Julia is a high-level, high-performance dynamic programming language for
numerical computing. It provides a sophisticated compiler, distributed
parallel execution, numerical accuracy, and an extensive mathematical
function library.

For a quick introduction and tutorial, see https://github.com/csc-training/julia-introduction 

[TOC]

## Available

### Puhti
-   1.1.1 compiled with Intel Math Kernel Library (MKL)
-   1.1.1 from pre-compiled binaries

## License
Free and open source under [MIT license](https://github.com/JuliaLang/julia/blob/master/LICENSE.md).

## Usage

### Loading Modules

To load a module for a stable version of Julia, use the following command

```bash
$ module load julia
```

To use the pre-compiled binaries, load the corresponding module with

```bash
$ module load julia/1.1.1-pre-compiled
```

### Interactive use

After loading the Julia module, it can be run interactively simply by
typing

```bash
$ julia
```

If more resources are required, one can request an interactive node
directly on a computing node on Puhti with

```bash
$ srun -c 1 -t 00:10:00 --mem=1G --pty --account=project_id julia 
```

where <var>-c</var> is the number of cores,  <var>-t</var> is the time limit in hh:mm:ss,  <var>--mem</var> is the minimum memory, <var>--pty</var> enables the interactive run and <var>--account=project_id</var> specifies the billing project, respectively.

### Installing packages

You can access to the package manager by pressing "]" during the interactive session. The packages are added to the project with an 'add' command.

```bash
julia> ]
(v1.1) pkg>
(v1.1) pkg> add Example
```

After adding a packge, it can be loaded in Julia:

```bash
julia> using Example
```

Packages are by default installed in the directory '~/.julia/', but the target can be changed with an environmental variable 'JULIA_PKGDIR'.

```bash
$ export JULIA_PKGDIR=/your/directory
```

**NOTE:** Packages that work for one version of Julia might not work at all for another. Check the required version number.

More information about Julia's package manager you can found from its [documentation](https://julialang.github.io/Pkg.jl/v1/).

### Serial batch job

Sample single-processor Julia batch job on Puhti

```bash
#!/bin/bash -l
#SBATCH -J julia_single
#SBATCH -o output_%j.txt
#SBATCH -e errors_%j.txt
#SBATCH -p test
#SBATCH --account=project_id
#SBATCH -t 00:05:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1000

module load julia
srun julia my_script.jl
```

Where <var>-J</var> is our jobname, <var>-o</var> is our output file, <var>-e</var> is our error file, <var>-p</var> is the partition we are running on,
 <var>-t</var> is the maxium time for the run  <var>--ntasks</var> is the number of times we run our script <var>--nodes</var> is how many nodes we require and <var>--mem-per-cpu</var> is the memory requested for each cpu.

This runs the script <var>my\_script.jl</var> one time using one cpu-core.

### Parallel batch jobs

Sample multi-processor Julia batch job on Taito

```bash
#!/bin/bash -l
#SBATCH -J julia_multi_core
#SBATCH -o output_%j.txt
#SBATCH -e errors_%j.txt
#SBATCH -p test
#SBATCH -t 00:05:00
#SBATCH --account=project_id
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH -c 4
#SBATCH --mem-per-cpu=1000

module load julia-env 
srun julia my_script.jl
```

This runs the script <var>my\_script.jl</var> one time using four cpu-cores. Changing <var>--ntask=4</var> and removing the <var>-c</var> option would run the script four times on one cpu-core each.

For more details about the batch jobs, see Puhti documentation.

## More information

* [Julia home page](https://julialang.org )
* [Documentation](https://docs.julialang.org)
