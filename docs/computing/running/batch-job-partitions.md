# Available batch job partitions

Currently, the following batch are available in **Puhti**:


| Partition          |  Time Limit   |Job node limit | Number of nodes | Memory | Cores/GPUs node   |
|----------------|---------------|---------------|-----------------|--------|-------------------|
|Serial\*\*      |  3 days       | 1 node        |     532         | 190G   | 40 cores          |
|                |               |               |     132         | 382G   |                   |
|                |               |               |     12          | 764G   |                   |
|parallel\*\*    |  3 days       | 100 nodes     |     532         | 190G   | 40 cores          |
|                |               |               |     132         | 382G   |                   |
|                |               |               |     12          | 764G   |                   |
|hugemem         |  3 days       |  1 node       |     6           | 1532G  | 40 cores          |
|gputest         |  30 minutes   |  2 nodes      |     2           | 382G   | 40 cores + 4 GPUs |
|gpu             |  3 days       |  160 GPUs     |     78          | 382G   | 40 cores + 4 GPUs |


