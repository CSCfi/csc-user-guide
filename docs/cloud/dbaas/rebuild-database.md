# Rebuilding database instances

## What is a rebuild?
Rebuilding a database instance in Pukki essentially means recreating the virtual machine which
the database runs on, without modifying any of the user's data. This is occasionally necessary
because of changes which couldn't otherwise be provisioned, such as when a component approaches
its end-of-life and cannot be replaced without downtime.

Rebuilding usually causes about five minutes of downtime, but it's still a good idea to reserve
some extra time for the procedure.

## Things to be aware of when performing a rebuild
* A rebuild is probably the most complex operation users are allowed to do in Pukki. Because of
  this it's a good idea to do it during office hours so Pukki admins can assist with any
  unforeseen issues.
* If the rebuild takes longer than 15 minutes, feel free to open a ticket with
  [servicedesk@csc.fi](mailto:servicedesk@csc.fi) so we know who to contact in case of issues that
  require more debugging.
* The database instance's status will show `Building` while the rebuild is in progress.
* It's only possible to rebuild instances specifically marked as requiring a rebuild from
  the web GUI. To rebuild other database instances, you have to use the command-line tools.


## Rebuilding database instances using the web GUI interface

1. Go to the [database instances list view](https://pukki.dbaas.csc.fi/project/).
2. Ensure that you have chosen the correct project from the dropdown in the upper left corner in
case you are a member of several projects.
3. In the database instances list view, any instances requiring a rebuild should show
'Rebuild Instance' as the default action on the button in the rightmost column of the table.
If the default action reads something else (usually 'Create Backup'), the instance is not in need
of a rebuild.
4. To rebuild the instance press the 'Rebuild Instance' button. Expected downtime for the
operation is around 5 minutes.
5. After a successful rebuild, the default action should no longer read 'Rebuild Instance'.


## Rebuilding database instances using the OpenStack command-line client
!!! info "Be aware"
    With the command-line tools, it is possible to perform a rebuild on any database instances,
    including ones not marked as requiring one.


1. Use the `show` command with a `-c rebuild_required` flag to find out if the instance needs
rebuilding:

```txt
openstack database instance show -c rebuild_required $INSTANCE_ID
```

The output should look something like this:

```txt
+------------------+-------+
| Field            | Value |
+------------------+-------+
| rebuild_required | True  |
+------------------+-------+
```

A value of `True` indicates the database instance is in need of a rebuild.

2. Use the `rebuild` command to rebuild the instance:

```txt
openstack database instance rebuild $INSTANCE_ID latest
```

It should then take about 5 minutes until the rebuild is done and the instance's
`operating_status` is `HEALTHY` and `status` is `ACTIVE`.

To check these values, use the `show` command:

```txt
openstack database instance show $INSTANCE_ID
```

3. Once the instance's `status` is `ACTIVE`, you can again use the `-c rebuild_required` flag
with the `show` command to confirm that the instance no longer requires a rebuild:

```txt
openstack database instance show -c rebuild_required $INSTANCE_ID
+------------------+-------+
| Field            | Value |
+------------------+-------+
| rebuild_required | False |
+------------------+-------+
```

!!! info "Pro tip"
    You can also use `openstack database instance list -vv` to get more verbose output from the
    list command, and then search for `"rebuild_required": true` in the output.
