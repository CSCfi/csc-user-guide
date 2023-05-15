# Backups

!!! error "Closed Beta"
    Pukki DBaaS is in closed beta. This means that the service is probably not suitable for most users
    and there might be breaking changes. If you are still interested in using the service you can
    [contact us](../../support/contact.md) to see if the service would be suitable for you.

All databases in DBaaS get automatically backed up about every 24 hours. Users can also manually
backup their instances but that means that the next automatic backup will be taken about 24 hours
after the last backup. All backups are stored for 90 days after which they get automatically
deleted (not yet implemented). In the future, it will only be possible to delete backups automatically,
users will not be able to manually delete their own backups.

The backups are stored encrypted in Allas. 

You can manage your backups from the CLI and the web-interface.

## Risks

Be aware that the backup feature is still in development and should not be used for anything remotely sensitive or important.

* Backups are stored encrypted in Allas. This is worth to keep in mind if you want to take your own backup (you should not store it in Allas).
* When "restoring" a backup it will create a new instance with a new IP. So be aware that you might need to update your egress firewalls in your service.
* If you have any concerns, do not hesitate to contact [CSC Service Desk](../../support/contact.md).
* All your database data and backups are stored in the CSC Kajaani datacenter. If the datacenter burns down you will lose all your data.
* If you are using the DBaaS service for really important projects/data, it is worth considering to also take your own backups that are stored somewhere else than CSC in case of disaster.

## Manual backups

Backups can be taken manually. 

1. Creating a backup:

    ```
    openstack database backup create --instance $INSTANCE_ID $USER_FRIENDLY_NAME_OF_BACKUP
       # suitable name might be the name of the instance
    ```

2. Now you can list all your backups:

    ```
    openstack database backup list
    ```

3. You can also show more information about the backup:

    ```
    openstack database backup show $BACKUP_ID
    ```

## Restoring and/or verifying backup

Restoring a backup is the same process as creating a new instance. This can be done from the [web interface](web-interface.md) as well as the [CLI](cli.md) .
