# Backups

All databases in DBaaS get automatically backed up about every 24 hours. Users can also manually
backup their instances but that means that the next automatic backup will be taken about 24 hours
after the last backup. All backups are stored for 90 days after which they get automatically
deleted, backups can not be manually deleted by the user.

The backups are stored encrypted in Allas.

The web interface is currently only showing the latest 20 backups. If you want to see all your
backups you need to use the CLI-tool.

## Risks

Be aware that the backup feature is still in development and should not be used for anything remotely sensitive or important.

* Backups are stored encrypted in Allas. This is worth to keep in mind if you want to take your own backup (you should probably store them somewhere else than Allas nor cPouta).
* When "restoring" a backup it will create a new instance with a new IP. So be aware that you might need to update your egress firewalls in your service.
* If you have any concerns, do not hesitate to contact [CSC Service Desk](../../support/contact.md).
* All your database data and backups are stored in the CSC Kajaani datacenter. If the datacenter has catastrophic data loss, you may lose all your data.
* If you are using the DBaaS service for really important projects/data, it is worth considering to also take your own backups that are stored somewhere else than CSC in case of disaster.

## Manual backups

Backups can be made manually.

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
