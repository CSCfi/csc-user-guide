# DBaaS flavors and prices

The database instances are hosted on top of cPouta. The billing is based on the flavor (database instance size), volume size of the database and how much backup you are using.

## Flavor types

| Flavor | Cores | Memory (MB) | Billing Units / hour |
|--- |:---:|:---:|:---:|
| standard.small   | 2 | 2000  | 2  |
| standard.medium  | 3 | 4000  | 4  |
| standard.large   | 4 | 8000  | 7  |
| standard.xlarge  | 6 | 16000 | 13 |
| standard.xxlarge | 8 | 32000 | 25 |
| standard.3xlarge | 8 | 64000 | 50 |
| hpc.5.16core    | 16 | 59392 | 60 |
<!-- should this flavor exist here: | hpc.6.32core    | 32 | 116 | 120 | -->
<!--- We should probably remove standard.3xlarge in favor of supporting hpc.5.16core -->


## Volumes

| Resource type | Unit | Billing Units / GiB hour |
|--- |:---:|:---:|
| Volumes | GiB reserved | 0.01 |

The maximum volume size per database instance is currently 200 GiB.



## Backups
| Resource type | Unit | Billing Units / GiB hour |
|--- |:---:|:---:|
| Backups | GiB usage | 0.003 |

Automatic daily backups are stored for 90 days and they consume billing units based on total backup usage.


## Quotas

Defaults Quotas

| Resource type | Amount |
|--- |:---:|
| Maximum manual backups               | 1000      |
| Maximum number of database instances | 5         |
| Maximum memory usage                 | 20000 MB |
| Maximum volume reservation           | 50 GiB    |

If you need to run more or bigger database than what the default quota allows you can always send a
request to [ServiceDesk](mailto:servicedesk@csc.fi) .
