# DBaaS flavors and prices

!!! error "Closed Beta"
    Pukki DBaaS is in closed beta. This means that the service is probably not suitable for most users
    and there might be breaking changes. If you are still interested in using the service you can
    [contact us](../../support/contact.md) to see if the service would be suitable for you.

The database instances are hosted on top of cPouta. The billing is based on the flavor (database instance size), volume size of the database and how much backup you are using.

!!! warning "Note"
    The prices have not yet been decided on, but they will be finalized before public beta.

## Flavor types

| Flavor | Cores | Memory (GiB) | Billing Units / hour |
|--- |:---:|:---:|:---:|
| standard.small   | 2 | 1.9  | 2 |
| standard.medium  | 3 | 3.9 | 4 |
| standard.large   | 4 | 7.8 | 7 |
| standard.xlarge  | 6 | 15  | 13 |
| standard.xxlarge | 8 | 31  | 25 |
| standard.3xlarge | 8 | 62  | 50 |
| hpc.5.16core    | 16 | 58  | 60 |
<!-- should this flavor exist here: | hpc.6.32core    | 32 | 116 | 120 | -->
<!--- We should probably remove standard.3xlarge in favor of supporting hpc.5.16core -->


## Volumes

| Resource type | Unit | Billing Units / GiB hour |
|--- |:---:|:---:|
| Volumes | GiB reserved | 0.01 |




## Backups
| Resource type | Unit | Billing Units / GiB hour |
|--- |:---:|:---:|
| Backups | GiB usage | 0.003 |


Note that backups are taken automatically once a day and are stored for 90 days. This means that
after 90 days you will have consistently 90 backups per instance. This means that each backup
will in practice cost 6.48 Billing Units / GiB. Another way of thinking about it is that having
backups costs 0.27 BU per hour if your average backup size is 1 GiB.


## Quotas

Defaults Quotas

| Resource type | Amount |
|--- |:---:|
| Maximum manual backups               | 1000      |
| Maximum number of database instances  | 5         |
| Maximum memory usage                 | 20000 MiB |
| Maximum volume reservation           | 50 GiB    |

If you need to run more or bigger database than what the default quota allows you can always send a
request to [ServiceDesk](mailto:servicedesk@csc.fi) .
