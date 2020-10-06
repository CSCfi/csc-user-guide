# IPM

## Available
    Puhti: 2.0.6
## Usage  
[IPM](http://ipm-hpc.sourceforge.net/) is a portable profiling infrastructure for parallel codes. It has extremely low overhead, is scalable and easy to use requiring no source code modification. The level of detail is selectable at runtime and presented through a variety of text and web reports.  In order to use no code changes are require, only a re-link is needed. In addition to the required modules, one has the load the IPM module:
```
module load ipm
```

Next, the code is compiled as normal, but with addition  the link to the libraries. 
```
-lipmf -lipm
```
The above re-link will only work if it appears the last in the compiling line. 
Next the code is ran as a usual batch job. The follwing additions are needed to the job script:
```
module load ipm
export IPM_REPORT=full
```
This will create profiling for all cod, displayed at the end of the  programs's own output. Here is an example of a output at the beginning of the execution of a code:
```
##IPMv2.0.6########################################################
#
# command   : /users/cristian/PuhtiIPM/./TwoDMPIPFC 
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

