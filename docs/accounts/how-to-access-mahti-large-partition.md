# How to get access to Mahti large partition

Projects running well-scaling codes can get access to the large partition
(20-200 nodes) on Mahti in three steps. First, a 30-day test period for the
large partition is requested. Second, during the test period, the scalability
and parallel performance of the code is demonstrated with appropriate test
runs. Finally, the results are submitted for evaluation by the project manager.

The process is described in detail below.

## Test access to the large partition on Mahti

To request the 30-day test period, proceed as follows:

1. Login to [MyCSC](https://my.csc.fi) and in the _Projects_ menu select the
   project you want to modify.
2. In the _Services_ list, click open the settings for **Mahti** service
   (_Configure_). This opens a page where the project manager can modify the
   settings for disk quotas (_Quota settings_) and request access to the large
   partition (_Large partition settings_). Click open
   _Large partition settings_.
3. Click the _Apply for trial access_ button. After the access has been
   granted, you will be able to submit jobs to the large partition.

## Scalability testing

In the second phase, test runs demonstrating the scalability are to be
performed. Here are some general guidelines for scalability testing.

* Testing should be done for at least three different node counts up to the
  target in production (for example with 20, 40, 60, and 80 nodes).
* Tests are run through the batch job system.
* The test runs should reflect real production runs, i.e. the number of atoms,
  number of grid points, disk I/O load etc. should be similar.
* The input data set must be the same for each run.
* The running time in tests should be reduced as much possible, for example, by
  running only few time steps, iterations etc.
* The running time should still be long enough that initialization does not
  affect results. Typically, a few minutes for the shortest run time (largest
  node count) is fine.
* Parameters affecting the scalability can, and are encouraged to be, changed.
  Note also the
  [performance checklist](../computing/running/performance-checklist.md).
* Minimum requirement is 75 % parallel efficiency (i.e. speedup of 1.5 when
  doubling the number of nodes).

## Reporting

The scalability report should contain a short description of the software and
the test case, as well as wall-times for each node count. If the software is
not pre-installed by CSC, describe briefly also the parallelization strategy
used in the software and include details about the I/O implementation and load.

Attach to the report a representative batch job script, and if the application
was run with hybrid MPI/OpenMP parallelization, attach also the `stderr` of a
single run where the following settings are applied:

```bash
export OMP_AFFINITY_FORMAT="Process %P level %L thread %0.3n affinity %A"
export OMP_DISPLAY_AFFINITY=true
```

Reporting the results of the test runs or applicable previous scalability data
is done through [MyCSC portal](https://my.csc.fi) as follows:

1. Login to [MyCSC](https://my.csc.fi) and in the _Projects_ menu select the
   project you want to modify.
2. In the _Services_ list, click open the settings for **Mahti** service
   (_Configure_). This opens a page where the project manager can modify the
   settings for disk quotas (_Quota settings_) and request access to the large
   partition (_Large partition settings_). Click open
   _Large partition settings_.
3. For the results and justification, there is a text box and possibility to
   attach documents (please remember to upload the documents after you have
   selected them). Multiple documents can be attached. Finally, submit the
   justification.
4. CSC experts will evaluate the results and grant production access to the
   large partition. If there is a problem with the code performance, the
   project manager will be contacted.

## Assistance

CSC's experts can help users in performing scalability tests if needed and also
provide hints for improving the performance of their software.
[Contact CSC Service Desk](../support/contact.md) if you need assistance with
your software.
