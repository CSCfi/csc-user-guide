# IPM

## Available
    Puhti: 2.0.6
## Usage  
[IPM](http://ipm-hpc.sourceforge.net/) is a portable profiling infrastructure for parallel codes. It has extremely low overhead, it is scalable and it is easy to use as no source code modifications are required. The level of detail can be selected at runtime, and the profile is presented through a variety of text and web reports.  In order to use IPM, only a re-link is needed. First, one has the load the IPM module:
```
module load ipm
```

Next, the code is build as normal, but with the additional linker flags for IPM: 
```
-lipmf -lipm
```
The above options need to be the last linker flags. After the applications is build with IPM, it is ran as a usual batch job with the following additions 
in the job script:
```
module load ipm
export IPM_REPORT=full
```
This profile for all code, and results are displayed at the end of the stdout of the job. Here is an example of the beginning of the output:
```
##IPMv2.0.6########################################################
#
# command   : ./myexe
# start     : Mon Oct 05 19:08:19 2020   host      : r07c01.bullx    
# stop      : Mon Oct 05 19:08:24 2020   wallclock : 5.35
# mpi_tasks : 40 on 1 nodes              %comm     : 12.72
# files     :                            %i/o      : 0.00
# mem [GB]  : 32.38                      gflop/sec : 0.00
#
#           :       [total]        <avg>          min          max
# wallclock :        213.01         5.33         5.32         5.35 
# MPI       :         27.08         0.68         0.66         0.70 
# I/O       :          0.00         0.00         0.00         0.00 
# %wall     :
#   MPI     :                      12.72        12.35        13.22 
#   I/O     :                       0.00         0.00         0.00 
# #calls    :
#   MPI     :           760           19           19           19
#   I/O     :             0            0            0            0
# mem [GB]  :         32.38         0.81         0.81         0.81 
#
#                             [time]        [count]        <%wall>
# MPI_Alltoall                 26.94            400          12.65
# MPI_Barrier                   0.11             40           0.05
# MPI_Reduce                    0.03             80           0.01
# MPI_Comm_rank                 0.00             80           0.00
# MPI_Comm_size                 0.00             80           0.00
# MPI_Init                      0.00             40           0.00
# MPI_Finalize                  0.00             40           0.00
#
###################################################################
```
IPM provides information about the total wall clock time, and the time spent in the MPI calls, both cumulative and for each individual call. It also generates an XML file that can be used for generating a graphical web page.
