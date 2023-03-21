# Advanced DBaaS features
!!! error "Closed Beta"
    Pukki DBaaS is in closed beta. This means that services is probably not suitable for most users
    and there might be breaking changes. If you are still interested in using the service you can
    [contact us](../../support/contact.md) to see if the service would be suitable for you.

## Application credentials

You can create application credentials instead of using username and passwords. This is especially useful if you want to automate your database management. This could be used in a CI/CD environment where you might want to create a new database for each commit. Application credentials could also be used if you are building a services that uses the DBaaS as a backend component for example creates new database users on-demand for new users.

## Configuration groups

You can modify your database parameter through `configuration groups` . Configuration groups are a
concept to store your database settings in way so that you can apply the same settings to multiple
databases. Some of the parameters does requires restart. The parameters depends on the database
engine. The configuration groups can be modified from the web-GUI as well as the CLI-tool.

### Example how to create a configuration group with the CLI


1. Figure out which datastore, datastore-version and what values you want to create a configuration
group for. In this example we will use datastore `postgresql` and datastore-version:  `14.4` as an
example.

2. Figure out which parameters that can be modified:
```
openstack database configuration parameter list --datastore postgresql 14.4
```
Note that some parameters will require to restart the database instance.

3. Create a configuration group. We want to call this group "group-name" and we want to modify
`max_connections` to `234`.
```
openstack database configuration create group-name --datastore postgresql --datastore-version 14.4 '{"max_connections": 200 }'
```

4. You can see the configuration group by
```
openstack database configuration show group-name
```

5. You can also update the configuration group. But note that you need to use the group's `ID` and
you also need to define all parameters otherwise the old parameters will be removed. This might be
easier to modify from the WEB-GUI.
```
openstack database configuration set $GROUP_ID '{"min_wal_size": 160, "max_connections": 234 }'
```

6. Once you are happy with your configuration group you can attach it to an instance.
```
openstack database configuration attach $INSTANCE_ID $CONFIGURATION_GROUP_ID
```

7. If your configuration group contained changes that requires a restart you will need to restart
your database instance. Note that you won't be able to attach a new configuration group before
restarting the instance if you detached a configuration that requires restart. Also only one
configuration group can be attach at the same time. Note that no new backups will be taken of the
instance before the restart have been done.
```
openstack database instance restart $INSTANCE_ID
```

