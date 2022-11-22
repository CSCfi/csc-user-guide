# Backups

The backups are stored encrypted in Allas. There will two kind of backups; automatic and manual.

You can manage your backups from the CLI and web-interface.

## Risks

Be aware the backup feature is still in the development phase and should not be used for anything remotely sensitive nor important.

* Backups are stored encrypted in Allas. This is worth to keep in mind if you want to take your own backup that you should not store it in Allas.
* When "restoring" a backup it will create a new instance with a new IP. So be aware that you might need to update your egress firewalls in your service.
* If you have any concern do not hesitate taking contact with servicedesk@csc.fi
* All your database data backups included is stored in the CSC Kajaani datacenter, if the datacenter burns down you will lose all your data.
* If you are using the DBaaS services for really important stuff it is worth consider to also take your own backups that are stored somewhere else than CSC in case of disaster.

## Automatic Backups

Automatic backups have not been developed yet.

* Automatic backups will be enabled by default and can not be disabled.
* Automatic backups will be automatically deleted after 30 or 90 days.
* Users will not be able to delete their own backups.

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

