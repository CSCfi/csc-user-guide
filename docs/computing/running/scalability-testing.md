# Scalability testing

In order to use the `large` partition in Mahti (more than 20 nodes), the
project needs to perform a scalability test and report the
results. Project manager can apply at [MyCSC
portal](https://my.csc.fi) a temporary (30 day) access to `large`
partition for carrying out the testing. 

## Guidelines for scalability testing

Here are some general guidelines for scalability testing.

* Testing should be done at minimum three different node counts up to
target in production (for example with 25, 50, and 100 nodes).
* Tests are run through the batch job system.
* The test runs should reflect real production runs, i.e. the number of
atoms, number of grid points, disk IO load etc. should be similar. 
* The input data set must be the same for each run.
* The running time in tests should be reduced as much possible, for
example by running only few times steps, iterations etc.
* The running time should still be long enough that initialization does
not affect results, typically few minutes for the shortest run time
(largest node count) is fine.
* Parameters affecting the scalability can, and are encouraged to be,
changed.

If the parallel performance of a software is self-evident, based on
earlier tests carried out on Mahti or other supercomputer, no further
tests are required. Reporting the earlier results through [MyCSC
portal](https://my.csc.fi) is
sufficient in such a case. Note however, that even if a software is
shown to scale well with a certain data set, not all jobs (e.g. smaller
data sets) scale as well. In order to use the resources efficiently it
is good to test scalability for each job type before extensive simulations.

## Assistance

CSC's experts can help users in performing scalability tests if needed
and also provide hints for improving the performance of their software.
Contact CSC Service Desk if you need assistance with your software.


## Reporting

The scalability report should contain a short description of the
software and the test case, as well as wall times with each node count.
If software is not installed by CSC describe briefly also the
parallelization strategy used in the software including details about
the IO implementation and load.

Attach to the report a representative batch job script, and if the
application is run with hybrid MPI/OpenMP parallelization, attach also
`stderr` of single run where the following settings are applied:

```
export OMP_AFFINITY_FORMAT="Process %P level %L thread %0.3n affinity %A"
export OMP_DISPLAY_AFFINITY=true
```

The report is submitted via [MyCSC portal](https://my.csc.fi).
