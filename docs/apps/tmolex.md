# TmoleX

The free TmoleX Client version is designed to run TURBOMOLE on remote Linux/Unix systems from your local Windows, Linux, or MacOS desktop.

Import or build/modify structures on your local desktop. Run TURBOMOLE jobs on external systems or submit them to a queuing system on remote Linux servers. Let TmoleX Client copy results back to your local machine to analyze and visualize.

## Available

- Can be freely downloaded from
 [http://www.cosmologic.de/support-download/downloads/tmolex-client.html](http://www.cosmologic.de/support-download/downloads/tmolex-client.html)   

## License

TBD


## Usage

Install the TmoleX client on your local workstation. For details, see, [http://www.cosmologic.de/turbomole/tmolex.html](http://www.cosmologic.de/turbomole/tmolex.html). You can build your actual job locally and then submit the job to Puhti. With the client you can monitor how the job proceeds. When the job has completed you can retrieve the output and use your local client to analyze the results.

 Below some example queue settings that can be used in TmoleX:
![Slurm settings](/img/tmolex_submit.png)
   
Where the complete script to be inserted in  the field "Script before job execution" looks like (modify according to your actual needs):
```
#SBATCH --partition=test
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed 
#SBATCH --time=00:10:00      # time as hh:mm:ss

ulimit -s unlimited
export PARA_ARCH=MPI         # use MPI 
export MPI_USESRUN=1
export SLURM_MPI_TYPE=pmi2
export SLURM_CPU_BIND=none
export I_MPI_PIN_DOMAIN=auto,compact
module load turbomole/7.4.1
export PARNODES=$SLURM_NTASKS # for MPI
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH

```

## More information
-   [TmoleX features](http://www.cosmologic.de/turbomole/tmolex/tmolex-features.html)
-   [TmoleX tutorial video](http://www.cosmologic.de/turbomole/tmolex/online-video-tutorial.html)

