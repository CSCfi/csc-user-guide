---
tags:
  - Other
---

# Gaussian

Gaussian is a versatile program package providing various capabilities for electronic
structure modeling.

[TOC]

## Available

- Puhti: G16RevC.02
- Mahti: G16RevC.02

## License

CSC has acquired a full commercial license for Gaussian. Gaussian is available for use by
all approved account holders, subject to some license restrictions. To be able to use
Gaussian at CSC **your user-id has to be added to Gaussian users group. Send a request to
[CSC Service Desk](../support/contact.md).**

## Usage

Initialize the Gaussian environment:

```bash
module load gaussian/G16RevC.02
```

Standard jobs are then conveniently submitted by using the `subg16` script:

```bash
subg16 time jobname <billing project id>
```

Run the plain subg16 command for details.

For optimal performance of Gaussian jobs on CSC's servers it is beneficial to make some
efficiency considerations. Some hints on how to estimate memory and disk requirements can
be found [here](http://gaussian.com/running/?tabid=3).

### Using local disk on Puhti

Particularly some wave function-based electron correlation methods can
be very disk I/O intensive. Such jobs benefit from using the fast
[NMVE local disk](../../computing/running/creating-job-scripts-puhti/#local-storage)
on Puhti. Using local disk for such jobs will also reduce the overall load on the
Lustre parallel file system.

On Puhti, you can request your Gaussian job to use local disk by submitting the
job with the `subg16_nvme` script:

```bash
subg16_nvme time jobname <billing project id> diskspace
```

The requested disk space is given in GB.

## Performance considerations

Here we give a brief example on what type of resources can affect the performance
of Gaussian and how these should be taken into consideration. We are using
[α-Tocopherol](https://en.wikipedia.org/wiki/%CE%91-Tocopherol) (a type of vitamin
E) as input structure.

For a `b3lyp/cc-pVDZ, %mem=10GB` single-point calculation the results are:

| platform/cores      | wall time (hh:mm:ss) |  billing units       |
| ------------------: | -------------------: |  ------------------: |
| Puhti/10            | 00:04:19             |  0.73                |
| mem=20/10           | 00:04:11             |  0.85                |
|      /20            | 00:02:16             |  0.80                |
|      /40            | 00:01:14             |  0.85                |
| Mahti/128           | 00:00:53             |  1.47                |

For this particular case, the scaling is reasonable up to a full Puhti node. Increasing
the memory reservation from 10 GB to 20 GB, doesn't speed up the calculation but only
increases its cost. The job is slightly faster on Mahti using 128 cores compared to
40 cores on Puhti, but the cost is significantly higher.

If we do the same calculation but increase the size of the basis set to `b3lyp/cc-pVTZ`
the results are:

| platform/cores      | wall time (hh:mm:ss) |  billing units       |
| ------------------: | -------------------: |  ------------------: |
| Puhti/40            | 00:12:48             |  10.27               |
| Mahti/128           | 00:06:30             |  10.83               |

Here we notice that the calculation on Mahti is twice as fast as on Puhti, but the cost
is about the same.

For a wave function-based method like `MP2/cc-pVDZ`, the reserved memory (mem=), as
well as use of local disk (nvme) significantly affects the performance:

| platform/cores      | wall time (hh:mm:ss) |  billing units       |
| ------------------: | -------------------: |  ------------------: |
| Puhti, mem=40/10    | 00:37:55             |  8.94                |
|        mem=80/10    | 00:19:32             |  5.91                |
|        mem=80/20    | 00:16:08             |  7.57                |
|        mem=160/20   | 00:16:25             |  9.89                |
|  nvme, mem=80/20    | 00:12:40             |  7.57                |
|        mem=160/40   | 00:11:21             | 10.62                |
|        mem=80/40    | 00:11:59             |  9.62                |
|  nvme, mem=160/40   | 00:09:29             |  9.06                |
|  nvme, mem=80/40    | 00:09:23             |  7.72                |
| Mahti/128           | 00:14:30             | 24.17                |

From these results we conclude that 80 GB seems to be the optimal memory allocation and
that the use of local disk clearly improves the performance. The speedup when going from
20 to 40 cores, and using local disk is 1.35, that is below the
[recommended minimum of 1.5](../../accounts/how-to-access-mahti-large-partition/#scalability-testing).
Hence, the most efficient resource usage would correspond to 20 cores, 80 GB of memory and local disk
on Puhti. For this type of calculation Mahti isn't the optimal choice.

## References

- [How to cite Gaussian](http://gaussian.com/citation_b01/) in your publications.

## More information

- [Online Gaussian user reference](http://gaussian.com/man/)
- [Using Gabedit as GUI for Gaussian jobs on Puhti](../support/tutorials/gabedit_gaussian.md)
- [Farming Gaussian jobs with HyperQueue](https://csc-training.github.io/csc-env-eff/hands-on/throughput/gaussian_hq.html)
