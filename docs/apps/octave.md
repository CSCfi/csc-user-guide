## GNU Octave

### Description

GNU Octave is a high-level interpreted language, primarily intended for
numerical computations. It provides capabilities for the numerical
solution of linear and nonlinear problems, and for performing other
numerical experiments. It also provides extensive graphics capabilities
for data visualization and manipulation. Octave is normally used through
its interactive command line interface, but it can also be used to write
non-interactive programs. The Octave language is quite similar to Matlab
so that most programs are easily portable.

------------------------------------------------------------------------

### Available

##### Version on CSC's Servers

Taito

-   4.0
-   4.0.1
-   4.2.0
-   4.2.2

------------------------------------------------------------------------

### Usage

##### Interactive Use

Interactive use with GUI on taito-shell:

    module load octave-env
    octave

or without GUI with a --no-gui option

    octave --no-gui

[NoMachine] client is recommended to make the usage of the GUI fluent.

##### Installing Packages from Octave Forge

1.  Log in to taito.csc.fi
2.  Load Octave module and start Octave without GUI
3.  Give command  
    octave:&gt; pkg install -forge package\_name
4.  Before using the package, it have to be loaded  
    octave:&gt; pkg load package\_name

##### Octave Batch Jobs

Taito batch job system is described in Taito User Guide, [chapter 3.
Batch Jobs]. Below is an example of a simple serial job for Octave.

    #!/bin/bash -l
    #octave_example.sh
    #SBATCH --constraint="snb|hsw"
    #SBATCH -o output.out
    #SBATCH -e stderr.err
    #SBATCH -p serial
    #SBATCH -n 1
    #SBATCH -t 00:05:00
    #SBATCH --mem-per-cpu=1000
    module load octave-env
    octave --no-gui/wrk/user_name/example.m
    used_slurm_resources.bash

    [user@taito-login1]$ sbatch octave_example.sh

------------------------------------------------------------------------

### Discipline

Mathematics and Statistics  

------------------------------------------------------------------------

### References

In view of the many contributions made by numerous developers over many
years it is common courtesy to cite Octave in publications when it has
been used during the course of research or the preparation of figures.
The citation function can automatically generate a recommended citation
text for Octave or any of its packages. See the help text below on how
to use citation.

    citation
    citation package

Display instructions for citing GNU Octave or its packages in
publications. When called without an argument, display information on
how to cite the core GNU Octave system. When given a package name
package, display information on citing the specific named package. Note
that some packages may not yet have instructions on how to cite them.

------------------------------------------------------------------------

### Support

servicedesk@csc.fi

------------------------------------------------------------------------

### Manual

<https://www.gnu.org/software/octave/doc/interpreter/>

------------------------------------------------------------------------

  [NoMachine]: https://research.csc.fi/-/nomachine
  [chapter 3. Batch Jobs]: https://research.csc.fi/taito-batch-jobs
