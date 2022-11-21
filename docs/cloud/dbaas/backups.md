# Backups

The backups are stored TODO encrypted in Allas. There are TODO two different kind of backups automatic and manual. Automatic backups are taken once a day and are stored for 90 days. When taking a backup, the backup can not be deleted for 90 days TODO.

Managing backups from the web interface is not possible at this point.

## Risks

TODO backup are still in the development phase and should not be used for anything remotely sensitive nor important.

* Backups are stored in Allas. This is worth to keep in mind if you want to take your own backup that you should not store it in Allas.
* Backups are not encrypted ATM. (This will change before going to public-beta)
* When "restoring" a backup it will create a new instance with a new IP. So be aware that you might need to update your egress firewalls in your service.
* If you have any concern do not hesitate taking contact with \#DBaaS-team
* All your database data backups included is stored in the CSC Kajaani datacenter, if the datacenter burns down you will lose all your data.
* If you are using the DBaaS services for really important stuff it is worth consider to also take your own backups that are stored somewhere else than CSC in case of disaster.

## Automatic Backups TODO

Automatic backups are enabled by default and can not be disabled.

## Manual backups

Backups can be taken manually. 

1. Creating a backup

    openstack database backup create --instance $INSTANCE_ID $USER_FRIENDLY_NAME_OF_BACKUP

(suitable name might be the name of the instance)

2. Now you can list all your backups

     openstack database backup list

You can also show more information about the backup,

    openstack database backup show $BACKUP_ID

## Restoring and/or verify backup

Restoring backup is the same process as creating a new instances, this can be done from the [web interface](web-interface.md) as well as the [CLI](cli.md) .

