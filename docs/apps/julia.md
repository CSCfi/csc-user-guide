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

* 1.1.0 (default)
* DEV (newest unstable version of Julia)

## License
Free and open source under [MIT license](https://github.com/JuliaLang/julia/blob/master/LICENSE.md).

## Usage

To load a module for a stable version of Julia, use the following command

```bash
$ module load julia-env
```

To load the newest unstable development version of Julia, type

```bash
$ module load julia-env/DEV
```

And, for a specific version of Julia, use

```bash
$ module load julia-env/x.y.z
```

where x.y.z is the version number.

### Interactive use

After loading the Julia module, it can be run interactively simply by
typing

```bash
$ julia
```

If more resources are required, one can request an interactive node
directly on a computing node on Puhti with

```bash
$ srun -c 1 -t 00:10:00 --mem=1G --pty julia
```

where <var>-c</var> is the number of cores,  <var>-t</var> is the time limit in hh:mm:ss,  <var>--mem</var> is the minimum memory and  <var>--pty</var> enables the interactive run, respectively.

### Installing packages

You can access to the package manager by pressing "]". The packages are added to the project with an 'add' command.

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
#SBATCH -t 00:05:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1000

module load julia-env
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
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH -c 4
#SBATCH --mem-per-cpu=1000

module load julia-env 
srun julia my_script.jl
```

This runs the script <var>my\_script.jl</var> one time using four cpu-cores. Changing <var>--ntask=4</var> and removing the <var>-c</var> option would run the script four times on one cpu-core each.

For more details about the batch jobs, see Puhti documentation.

#### Running julia on Puhti using multiple workers

Using some packages, we can run multiple Julia workers on separate nodes
that are able to communicate with each other.

We start by allocating resources

```bash
$ salloc --nodes=4 --cpus-per-task 2 -p parallel
```

After this, we submit a batch job, which will start our Julia instances

```bash
$ sbatch julia.sbatch
```

where <var>julia.sbatch</var> contains

```bash
#!/bin/sh
#SBATCH --time=00:15:00
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=1
#SBATCH --partition parallel
# the resources requested above must be within the allocation

# we need to load the julia module so that the paths are set up right.
module load julia-env/0.6.2

# this starts the julia script which will srun its own processes
julia slurm.jl
```

and the main script <var>slurm.jl</var>

```bash
try
        using ClusterManagers
catch
        Pkg.add("ClusterManagers")
        using ClusterManagers
end

#Arguments to the Slurm srun(1) command can be given as keyword
#arguments to addprocs.  The argument name and value is translated to
#a srun(1) command line argument as follows:
#1) If the length of the argument is 1 => "-arg value",
#e.g. t="0:1:0" => "-t 0:1:0"
#2) If the length of the argument is > 1 => "--arg=value"
#e.g. time="0:1:0" => "--time=0:1:0"
#3) If the value is the empty string, it becomes a flag value,
#e.g. exclusive="" => "--exclusive"
#4) If the argument contains "_", they are replaced with "-",
#e.g. mem_per_cpu=100 => "--mem-per-cpu=100"

np = 4
addprocs(SlurmManager(np), t="00:5:00")
hosts = []
pids = []
println("We are all connected and ready.")
@parallel for i in workers()
        host, pid = fetch(@spawnat i (gethostname(), getpid()))
        println(host, pid)
        push!(hosts, host)
        push!(pids, pid)
        println(host,tt)
end

#The Slurm resource allocation is released when all the workers have
#exited
for i in workers()
        rmprocs(i)
end
```

This particular scrip prints the hostname of the worker node and the
process id for the Julia instance.

## More information

* [Julia home page](https://julialang.org )
* [Documentation](https://docs.julialang.org)
