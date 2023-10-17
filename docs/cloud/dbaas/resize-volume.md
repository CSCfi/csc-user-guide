# Resize instance volume

!!! error "Closed Beta"  
    Pukki DBaaS is in closed beta. This means that the service is probably not suitable for most users
    and there might be breaking changes. If you are still interested in using the service you can
    [contact us](../../support/contact.md) to see if the service would be suitable for you.  

When you first create an instance, you specify the size of the volume the instance has in use. If you later on notice that the size is not enough, you can resize the volume either from the web interface or from the CLI. Note that you can only increase the size of the volume, not decrease.  

## Resize volume for database instance  

### From web interface

In the column on the left hand side you can go to `Database` -> `Instances` and press
the arrow icon next to `Create Backup` -button that can be found on the right hand side of the select instance, and select `Resize Volume` from the drop-down list.  

From there you can specify the new volume size for the database instance. Note that the new value must be greater than the existing volume size.

Confirm the change with `Resize Database Volume`.

The change should take 1-2 minutes, if the web interface does not automatically update the status from `Resizing` to `Active`, try to reload the page.

If the status is `Resizing` for over 5 minutes, check the `I'm having problems with resizing the volume`.  