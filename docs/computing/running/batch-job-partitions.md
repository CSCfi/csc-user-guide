# Available batch job partitions

Currently, the following batch are available in **Puhti** for normal nodes:


| Partition      |  Time Limit   | Max tasks | Max nodes | Max memory per node |
|----------------|---------------|-----------|-----------|---------------------|
|test            |  0.5 hour     | 160       |   4       |    382 GiB          |
|small           |  3 days       | 40        |   1       |    382 GiB          | 
|large           |  3 days       | 4000      |   100     |    382 Gib          |
|longrun         |  14 days      | 40        |   1       |    382 GiB          |
|hugemem         |  3 days       | 160       |   4       |    766 GiB          | 
|hugemem_longrun |  14 days      | 40        |   1       |    1534 GiB         |

For GPU nodes the following partitions exist:


| Partition      |  Time Limit   | Max GPUs  | Max nodes | Max memory per node|
|----------------|---------------|-----------|-----------|--------------------|
|gpu_test        |  0.5 hour     |  8        |   2       |    382 GiB         |
|gpu             |   3 days      |  80       |   20      |    382 GiB         |






