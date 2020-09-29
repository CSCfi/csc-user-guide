# mpiP: Lightweight MPI Profiler

## Available
    Puhti: 3.4.1
    Mahti: 3.4.1
    
[mpiP](http://mpip.sourceforge.net/) is a lightweight MPI profiler which uses statistical sampling to record profiling data. It generates less overhead and much less data than tracing tools. In order to use no code changes are require, only a re-link is needed. For both Mahti and Puhti, in addition to the required modules, one has the load the mpiP module: 
```
module load mpip
```
Next the code is compiled as normal, but with addition of the `-g` flag and the link to the libraries. For Mahti one should use:
```
-lmpiP -lm -lbfd -liberty -L<path-to-unwind-lib>-lunwind
```
The path to the unwind library on mahti is `/appl/spack/v014/install-tree/gcc-9.3.0/libunwind-1.3.1-otflii/lib`. 
Similarly for Puhti the relink is done with :
```
-lmpiP -lm -L<path-to-iberty-lib>  -liberty -L<path-to-unwind-lib> -lunwind
```
The path to the iberty library is `/appl/spack/install-tree/intel-19.0.4/libiberty-2.31.1-o4es74/lib/`, while the path to unwind library is `/appl/spack/install-tree/intel-19.0.4/libunwind-1.2.1-45uplb/lib/`. 
The above re-link will only work if it appears the last in the compiling line. 
Next the code is ran as a usual batch job. The follwing additions are needed to the job script:
```
module load mpip
export LD_LIBRARY_PATH=<path-to-unwind-lib>:<path-to-iberty-lib>:$LD_LIBRARY_PATH
```
For running instead we replace `srun` by `srun -ppdebug`. 
This will create profiling for all code in a file which is indicated in the standard output before the programs's own output. Here is an example of a output at the beginning of the execution of a code:

```
mpiP: Set the report print threshold to [10.00%].
mpiP: Set the callsite stack traceback depth to [2].
mpiP: 
mpiP: mpiP: mpiP V3.4.1 (Build Aug 28 2020/11:57:54)
mpiP: Direct questions and errors to mpip-help@lists.sourceforge.net
mpiP: 
mpiP: Storing mpiP output in [./TwoDMPIPFC.256.181196.1.mpiP].
mpiP:
``` 
The profiling data is stored in the `.mpiP`file indicated above. Below is an example: 

```
@ mpiP
@ Command : /users/cristian/MahtimpiPTest/./TwoDMPIPFC 
@ Version                  : 3.4.1
@ MPIP Build date          : Aug 28 2020, 11:57:54
@ Start time               : 2020 08 28 16:38:05
@ Stop time                : 2020 08 28 16:38:14
@ Timer Used               : PMPI_Wtime
@ MPIP env var             : -t 10.0 -k 2
@ Collector Rank           : 0
@ Collector PID            : 181196
@ Final Output Dir         : .
@ Report generation        : Single collector task
@ MPI Task Assignment      : 0 c1101.mahti.csc.fi
@ MPI Task Assignment      : 1 c1101.mahti.csc.fi
...
---------------------------------------------------------------------------
@--- MPI Time (seconds) ---------------------------------------------------
---------------------------------------------------------------------------
Task    AppTime    MPITime     MPI%
   0       8.12       4.12    50.75
   1       8.11        4.2    51.72
   2       8.11       4.17    51.40
   ...
   *   2.08e+03   1.05e+03    50.36
---------------------------------------------------------------------------
@--- Callsites: 8 ---------------------------------------------------------
---------------------------------------------------------------------------
 ID Lev File/Address        Line Parent_Funct             MPI_Call
  1   0 TwoDMPIPFC.f         432 forward_fft.3905         Alltoall
  1   1 TwoDMPIPFC.f         184 update                   
  2   0 TwoDMPIPFC.f         176 energy.3915              Reduce
  2   1 TwoDMPIPFC.f         127 MAIN__                   
  3   0 TwoDMPIPFC.f         545 backward_fft.3901        Alltoall
  3   1 TwoDMPIPFC.f         214 update                   
  4   0 TwoDMPIPFC.f         432 forward_fft.3905         Alltoall
  4   1 TwoDMPIPFC.f         189 update                   
  5   0 TwoDMPIPFC.f         545 backward_fft.3901        Alltoall
  5   1 TwoDMPIPFC.f         171 energy.3915              
  6   0 TwoDMPIPFC.f         432 forward_fft.3905         Alltoall
  6   1 TwoDMPIPFC.f         147 energy.3915              
  7   0 TwoDMPIPFC.f         176 energy.3915              Reduce
  7   1 TwoDMPIPFC.f         109 MAIN__                   
  8   0 TwoDMPIPFC.f         384 fft_init                 Barrier
  8   1 TwoDMPIPFC.f         138 main                     
---------------------------------------------------------------------------
@--- Aggregate Time (top twenty, descending, milliseconds) ----------------
---------------------------------------------------------------------------
Call                 Site       Time    App%    MPI%     COV
Alltoall                6    4.6e+05   22.16   44.00    0.03
Alltoall                5   2.18e+05   10.50   20.85    0.09
Alltoall                1   1.16e+05    5.57   11.05    0.06
Alltoall                3   1.15e+05    5.54   11.00    0.02
Alltoall                4   1.14e+05    5.50   10.92    0.02
Barrier                 8   2.19e+04    1.06    2.10    0.87
Reduce                  7        713    0.03    0.07    3.71
Reduce                  2        110    0.01    0.01    3.87
---------------------------------------------------------------------------
@--- Aggregate Sent Message Size (top twenty, descending, bytes) ----------
---------------------------------------------------------------------------
Call                 Site      Count      Total       Avrg  Sent%
Alltoall                1        512   6.71e+07   1.31e+05  20.00
Alltoall                3        512   6.71e+07   1.31e+05  20.00
Alltoall                5        512   6.71e+07   1.31e+05  20.00
Alltoall                4        512   6.71e+07   1.31e+05  20.00
Alltoall                6        512   6.71e+07   1.31e+05  20.00
Reduce                  2        256   2.05e+03          8   0.00
Reduce                  7        256   2.05e+03          8   0.00
---------------------------------------------------------------------------
@--- Callsite Time statistics (all, milliseconds): 2048 -------------------
---------------------------------------------------------------------------
Name              Site Rank  Count      Max     Mean      Min   App%   MPI%
Alltoall             1    0      2      220      217      213   5.34  10.52
Alltoall             1    1      2      237      233      229   5.75  11.11
...
Alltoall             1    *    512      342      226      200   5.57  11.05

Alltoall             3    0      2      225      219      214   5.41  10.66
Alltoall             3    1      2      233      227      222   5.60  10.83
...
Alltoall             3    *    512      250      225      205   5.54  11.00

Alltoall             4    0      2      222      219      216   5.41  10.66
Alltoall             4    1      2      228      225      221   5.54  10.71
...
Alltoall             4    *    512      250      223      206   5.50  10.92

Alltoall             5    0      2      589      393      196   9.68  19.07
Alltoall             5    1      2      602      409      215  10.07  19.47
...
Alltoall             5    *    512      838      426      126  10.50  20.85

Alltoall             6    0      2 1.62e+03      915      212  22.55  44.45
Alltoall             6    1      2 1.63e+03      924      213  22.78  44.04
...
Alltoall             6    *    512 1.83e+03      898      178  22.16  44.00

Barrier              8    *    256      161     85.7     10.7   1.06   2.10

Reduce               2    *    256     16.9     0.43  0.00985   0.01   0.01

Reduce               7    *    256      101     2.79   0.0364   0.03   0.07
---------------------------------------------------------------------------
@--- Callsite Message Sent statistics (all, sent bytes) -------------------
---------------------------------------------------------------------------
Name              Site Rank   Count       Max      Mean       Min       Sum
Alltoall             1    0       2 1.311e+05 1.311e+05 1.311e+05 2.621e+05
Alltoall             1    1       2 1.311e+05 1.311e+05 1.311e+05 2.621e+05
...
Alltoall             1    *     512 1.311e+05 1.311e+05 1.311e+05 6.711e+07

Alltoall             3    0       2 1.311e+05 1.311e+05 1.311e+05 2.621e+05
Alltoall             3    1       2 1.311e+05 1.311e+05 1.311e+05 2.621e+05
...
Alltoall             3    *     512 1.311e+05 1.311e+05 1.311e+05 6.711e+07

Alltoall             4    0       2 1.311e+05 1.311e+05 1.311e+05 2.621e+05
Alltoall             4    1       2 1.311e+05 1.311e+05 1.311e+05 2.621e+05
...
Alltoall             4    *     512 1.311e+05 1.311e+05 1.311e+05 6.711e+07

Alltoall             5    0       2 1.311e+05 1.311e+05 1.311e+05 2.621e+05
Alltoall             5    1       2 1.311e+05 1.311e+05 1.311e+05 2.621e+05
...
Alltoall             5    *     512 1.311e+05 1.311e+05 1.311e+05 6.711e+07

Alltoall             6    0       2 1.311e+05 1.311e+05 1.311e+05 2.621e+05
Alltoall             6    1       2 1.311e+05 1.311e+05 1.311e+05 2.621e+05
...
Alltoall             6    *     512 1.311e+05 1.311e+05 1.311e+05 6.711e+07

Reduce               2    0       1         8         8         8         8
Reduce               2    1       1         8         8         8         8
...
Reduce               2    *     256         8         8         8      2048

Reduce               7    0       1         8         8         8         8
Reduce               7    1       1         8         8         8         8
...
Reduce               7    *     256         8         8         8      2048
---------------------------------------------------------------------------
@--- End of Report --------------------------------------------------------
---------------------------------------------------------------------------
```
In the first part of the file are shown basic information about the performance experiment, followed by various statistics per invidual task and as aggregated. 
If one wants to focus only on specific regions the profilling can be switched on/off. For example in a Fortran code one could do:

```
call MPI_INIT( ierr )
call MPI_PCONTROL( 0 )      
[ ... ]                    
call MPI_PCONTROL( 1 )      
               
[ ... ]       ! Region of interest              

call MPI_PCONTROL( 0 )      
[ ... ]                     
call MPI_FINALIZE( ierr )
```
In the above code the debugging is first disabled after the MPI initialization (with `call MPI_CONTROL(0)`)  and later it is switched back for the region of interest.  At the end of the region the profiling is disabled again. In this case the profiler will only collect information for the region between the lines  `call MPI_CONTROL(1)` and  `call MPI_CONTROL(0)`.
Finally, mpiP has several configurable parameters  can set via the environment variable MPIP. For more details, please consult the related documentation at (http://mpip.sourceforge.net/#Runtime_Configuration).
