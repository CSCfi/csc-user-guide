# Advanced DBaaS features

## Application credentials

You can create application credentials instead of using usernames and passwords. This is especially useful if you want to automate your database management. This could be used in a CI/CD environment where you might want to create a new database for each commit. Application credentials could also be used if you are building a service that uses the DBaaS as a backend component for example for creating new database users on-demand for new users.

## Configuration groups

You can modify your database parameter through `configuration groups`. Configuration groups are a
concept to store your database settings in way so that you can apply the same settings to multiple
databases. Some of the parameters require a restart. The parameters depend on the database
engine. The configuration groups can be modified from the web-GUI as well as the CLI-tool.

### Example how to create a configuration group with the CLI

1. Figure out which datastore, datastore-version and what values you want to create a configuration
group for. In this example we will use datastore `postgresql` and datastore-version `14.4`.
2. Figure out which parameters can be modified:
    
    ```bash
    openstack database configuration parameter list --datastore postgresql 14.4
    ```
    
    Note that some parameters require restarting the database instance.

3. Create a configuration group. We want to call this group `group-name` and we want to modify
`max_connections` to `234`.

    ```
    openstack database configuration create group-name --datastore postgresql \
        --datastore-version 14.4 '{"max_connections": 234 }'
    ```

4. You can see the configuration group with:

    ```
    openstack database configuration show group-name
    ```

5. You can also update the configuration group. Note that you need to use the group's `ID` and
you also need to define all parameters. Otherwise the old parameters will be removed. This might be
easier to modify from the web-GUI.

    ```
    openstack database configuration set $GROUP_ID '{"min_wal_size": 160, "max_connections": 234 }'
    ```

1. Once you are happy with your configuration group you can attach it to an instance:

    ```
    openstack database configuration attach $INSTANCE_ID $CONFIGURATION_GROUP_ID
    ```

2. If your configuration group contained changes that require a restart, you will need to restart
your database instance.

    ```
    openstack database instance restart $INSTANCE_ID
    ```

    !!! info "Note"
        You will not be able to attach a new configuration group before restarting the instance if you detached a configuration that requires a restart. Also, only one configuration group can be attached at the same time.

    !!! info "Note"
        No new backups will be taken of the instance before the restart has been done.
