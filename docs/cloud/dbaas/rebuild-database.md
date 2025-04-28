# Rebuilding database instance

## Description
Sometimes your database is running on a really old servers that requires updated that can not be
provisioned without restarts or reinstall or when upgrades would take unnecessary long, in those
cases Pukki uses rebuild to ensure that upgrades can be down with minimal downtime.

Rebuild basically means that your database instance gets reinstalled without modifying your data.
Rebuilds takes usually around 5 minutes but it is still a good idea to reserve more time for the
rebuild procedure.

## Things to be aware of when doing a rebuild
* If you do a rebuild it is a good idea to do it inside office hours so that you can quickly get
  helps if something goes wrong.
* If the rebuild takes longer than 15 minutes feel free to open a ticket with
  [servicedesk@csc.fi](mailto:servicedesk@csc.fi) so that we know who we can contact in case there
  are any issues that requires more debugging.
* Rebuild is probably the most advanced operation in Pukki that the users are allowed to do, it is
  a good idea to do the rebuild inside office hours in case there are any issue the Pukki-admins
  can assist you quickly.
* The database instance will get the status `Building` while the instance is rebuilding.
* From the web-GUI you can only rebuild instances that the Pukki-service have marked as need to be
  rebuilt. From the openstack-cli you are allowed to rebuild any instance even if it does not
  require rebuilding.


## Rebuilding database instances using the Web GUI interface

1. Go to your [project instance view](https://pukki.dbaas.csc.fi/project/).
2. Ensure that you have chosen the correct computing project if you have multiple computing projects.
3. In your database instance project view your database instances that requires rebuild have a 
visible button that says `Rebuild instance` if the database instance requires rebuild. If the button
is not visible then it does not requires rebuild.
4. To rebuild the instance press the `Rebuild instance` button. After that you will need to wait
around 5 minutes before the instances have completed rebuilding.
5. Once the instances have completed rebuilding the `Rebuild instance` option will no longer be
available.


## Rebuild database instances using the openstack-CLI tool
!!! info "Be aware"
   Compared with the web GUI users can rebuild their database instances even if there is no need
   with the openstack-cli tool.

1. To find out if your instance needs to be rebuilt you need to run this command

```txt
openstack database instance show -c rebuild_required $INSTNACE_ID
```

if it shows

```txt
+------------------+-------+
| Field            | Value |
+------------------+-------+
| rebuild_required | True  |
+------------------+-------+
```

Then you know it requires rebuild. If it returns

```txt
+------------------+-------+
| Field            | Value |
+------------------+-------+
| rebuild_required | False |
+------------------+-------+
```
then you knows that it does not requires rebuilding
3. To rebuild your database instances you can run this command:

```txt
openstack database instance rebuild $INSTNACE_ID latest
```
then you need to wait about 5 minutes until the instances `operating_status` is `HEALTHY` and
`status` is `ACTIVE` . You can show the instances status by doing 

```txt
openstack database instance show $INSTANCE_ID
```
4. Once the `status` is `ACTIVE` you can verify that the instance does not requires rebuild by
```txt
openstack database instance show -c rebuild_required $INSTNACE_ID
+------------------+-------+
| Field            | Value |
+------------------+-------+
| rebuild_required | False |
+------------------+-------+
```

!!! info "Pro tip"
   You can also list all database instances with verbose flag and searching for
   `"rebuild_required": true` in the output by doing:
   `openstack database instance list -vv`

