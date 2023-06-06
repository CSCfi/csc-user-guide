# DBaaS flavors and prices

!!! error "Closed Beta"
    Pukki DBaaS is in closed beta. This means that the service is probably not suitable for most users
    and there might be breaking changes. If you are still interested in using the service you can
    [contact us](../../support/contact.md) to see if the service would be suitable for you.

The database instances are hosted on top of cPouta. The billing is based on the flavor (database instance size), volume size of the database and how much backup you are using.

!!! warning "Note"
    The prices have not yet been decided on, but they will be finalized before public beta.

## Flavor types

| Flavor | Cores | Memory<br/>(GiB) | Billing Units / hour |
|--- |:---:|:---:|:---:|
| standard.small   | 2 | 2   | 2 |
| standard.medium  | 3 | 4   | 4 |
| standard.large   | 4 | 7   | 7 |
| standard.xlarge  | 6 | 15  | 13 |
| standard.xxlarge | 8 | 30  | 25 |
| standard.3xlarge | 8 | 60  | 50 |
| hpc.5.16core    | 16 | 55  | 60 |
<!-- should this flavor exist here: | hpc.6.32core    | 32 | 110 | 120 | -->
<!--- We should probably remove standard.3xlarge in favor of supporting hpc.5.16core -->

## Other resources

| Resource type | Unit | Billing Units / GiB hour |
|--- |--- |--- |
| Volumes | GiB reserved | 0.01 |
| Backups | GiB usage | 0.003 |
