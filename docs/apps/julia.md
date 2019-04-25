## Julia

### Description

Julia is a high-level, high-performance dynamic programming language for
numerical computing. It provides a sophisticated compiler, distributed
parallel execution, numerical accuracy, and an extensive mathematical
function library.

On Puhti Julia uses Intel's MKL library.

For a quick introduction and tutorial see <https://github.com/csc-training/julia-introduction> 

------------------------------------------------------------------------

### Available

##### Version on CSC's Servers

Puhti:

1.1.0 (default)

1.0.2

DEV (newest unstable version of Julia)

------------------------------------------------------------------------

### Usage

To load the stable version of Julia use the following command

~~~~ western
 module load julia-env
~~~~

To load the newest version of Julia use the following command

~~~~ western
module load julia-env/DEV
~~~~

To load a specific version of Julia use

~~~~ western
module load julia-env/x.y.z
~~~~

where x.y.z is the version number.

#### Interactive use

After loading the Julia module, Julia can be run interactively simply by
typing

~~~~ western
 julia
~~~~

If more resources are required, one can request an interactive node
directly on a computing node on taito with

~~~~ western
srun -c 1 -t 00:10:00 --mem=1G --pty julia
~~~~

Here <kbd>-c</kbd> is the number of cores,  <kbd>-t</kbd> is the time limit in hh:mm:ss,  <kbd>--mem</kbd> is the minimum memory and  <kbd>--pty</kbd> enables the interactive run.

#### Installing packages

To show what packages are installed run

After adding a packge, it can be used by running

~~~~ western
using "PackageName"
~~~~

Packages are by default installed in ~/.julia/, but the package
directory  
can be changed with the shell command

~~~~ western
export JULIA_PKGDIR=/your/directory
~~~~

**NOTE:** Packages that work for one version of Julia might not work at all for another. Check the required version number.

#### Serial batch job

Sample single-processor Julia batch job on Taito

~~~~ western
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
~~~~

Where <kbd>-J</kbd> is our jobname, <kbd>-o</kbd> is our output file, <kbd>-e</kbd> is our error file, <kbd>-p</kbd> is the partition we are running on,
 <kbd>-t</kbd> is the maxium time for the run  <kbd>--ntasks</kbd> is the number of times we run our script <kbd>--nodes</kbd> is how many nodes we require and <kbd>--mem-per-cpu</kbd> is the memory requested for each cpu.

This runs the script my\_script.jl one time using one cpu-core.

#### Parallel batch jobs

Sample multi-processor Julia batch job on Taito

~~~~ western
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
~~~~

<span style="font-weight: normal">This runs the script my\_script.jl one
time using four cpu-cores </span><span style="font-weight: normal">(the
-c option)</span>  
Changing --ntask=4 and removing the -c option would run the script four
times on one cpu-core each.

For more details about the batch jobs see Taito user guide.

**Running julia on Taito using multiple workers**

Using some packages, we can run multiple Julia workers on separate nodes
that are able to communicate with each other.  

We start by allocating resources

~~~~ western
salloc --nodes=4 --cpus-per-task 2 -p parallel
~~~~

After this we submit a batch job, which will start our Julia instances

~~~~ western
sbatch julia.sbatch
~~~~

where 

<span style="font-size:14px;">**julia.sbatch**</span>

~~~~ western
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
~~~~

and the main script

<span style="font-size:14px;">**slurm.jl**</span>

~~~~ western
try
        using ClusterManagers
catch
        Pkg.add("ClusterManagers")
        using ClusterManagers
end

# Arguments to the Slurm srun(1) command can be given as keyword
# arguments to addprocs.  The argument name and value is translated to
# a srun(1) command line argument as follows:
# 1) If the length of the argument is 1 => "-arg value",
#    e.g. t="0:1:0" => "-t 0:1:0"
# 2) If the length of the argument is > 1 => "--arg=value"
#    e.g. time="0:1:0" => "--time=0:1:0"
# 3) If the value is the empty string, it becomes a flag value,
#    e.g. exclusive="" => "--exclusive"
# 4) If the argument contains "_", they are replaced with "-",
#    e.g. mem_per_cpu=100 => "--mem-per-cpu=100"

np = 4 #
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

# The Slurm resource allocation is released when all the workers have
# exited
for i in workers()
        rmprocs(i)
end
~~~~

This particular scrip prints the hostname of the worker node and the
process id  
for the Julia instance.

 

 

------------------------------------------------------------------------

### Discipline

------------------------------------------------------------------------

### References

------------------------------------------------------------------------

### Support

servicedesk@csc.fi

------------------------------------------------------------------------

### Manual

-   <https://julialang.org/> for general information
-   <https://docs.julialang.org/en/stable/> for Julia documentation

 

------------------------------------------------------------------------
