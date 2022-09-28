# DBaaS flavors and prices

The database instances are hosted on top of cPouta. The billing is based on the Flavor (database instances size), how big volume for the database and how much backup you are using.

TODO the prices have not been decided on, in internal beta the services is free.

## Flavor types
|Flavor|Cores|Memory<br/>(GiB)|Billing<br/>Units<br/>/h|
|--- |:---:|:---:|:---:|
| standard.small   | 2 | 2   | 4 |
| standard.medium  | 3 | 4   | 7 |
| standard.large   | 4 | 7   | 11 |
| standard.xlarge  | 6 | 15  | 21 |
| standard.xxlarge | 8 | 30  | 38 |
| standard.3xlarge | 8 | 60  | 68 |
| hpc.5.16core    | 16 | 55  | 61 |
<!--- We should probably remove standard.3xlarge in favor of supporting hpc.5.16core -->

## Other resources

|Resource type| Unit | Price |
|--- |:---:|:---:|
| Volumes | GiB reserved | 0.1 BU/GiB |
| Backups | GiB usage | 0.1 BU/GiB |

