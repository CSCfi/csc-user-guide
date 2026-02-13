# DBaaS flavors and prices

The database instances are hosted on top of cPouta. The billing is based on the flavor (database instance size), volume size of the database and how much backup you are using. All these resources consume **Cloud Billing Units**, for more information about Billing in CSC, visit the [Billing](../../accounts/billing.md) page.

## Flavor types

| Flavor | Cores | Memory (MB) | Cloud Billing Units / hour |
|--- |:---:|:---:|:---:|
| standard.small   | 2 | 2000  | 4  |
| standard.medium  | 3 | 4000  | 7  |
| standard.large   | 4 | 8000  | 12 |
| standard.xlarge  | 6 | 16000 | 22 |
| standard.xxlarge | 8 | 32000 | 40 |
| standard.3xlarge | 8 | 64000 | 52 |
| hpc.5.16core    | 16 | 59392 | 60 |
<!-- should this flavor exist here: | hpc.6.32core    | 32 | 116 | 120 | -->
<!--- We should probably remove standard.3xlarge in favor of supporting hpc.5.16core -->


## Volumes

| Resource type | Unit | Cloud Billing Units / GiB hour |
|--- |:---:|:---:|
| Volumes | GiB reserved | 0.02 |

The maximum volume size per database instance is currently 200 GiB.



## Backups
| Resource type | Unit | Cloud Billing Units / GiB hour |
|--- |:---:|:---:|
| Backups | GiB usage  | 0.005 |

Automatic daily backups are stored for 90 days and they consume Cloud Billing Units based on total backup usage.


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
