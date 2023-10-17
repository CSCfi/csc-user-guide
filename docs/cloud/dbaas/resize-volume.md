# Resize instance volume

!!! error "Closed Beta"  
    Pukki DBaaS is in closed beta. This means that the service is probably not suitable for most users
    and there might be breaking changes. If you are still interested in using the service you can
    [contact us](../../support/contact.md) to see if the service would be suitable for you.  

When you first create an instance, you specify the size of the volume the instance has in use. If you later on notice that the size is not enough, you can resize the volume either from the web interface or from the CLI. Note that you can only increase the size of the volume, not decrease.  

## Resize volume for database instance  

### From web interface

In the column on the left hand side you can go to `Database` -> `Instances` and locate the instance you want to resize the volume of.  

On the right hand side of the select row, next to `Create Backup` -button, press the `arrow icon` to open up a drop-down list, and select `Resize Volume`.

From there you can specify the new volume size for the database instance. Note that the new value must be greater than the existing volume size.

Confirm the change with `Resize Database Volume`.

The change should take 1-2 minutes, if the web interface does not automatically update the status from `Resizing` to `Active`, try to reload the page.

If the status is `Resizing` for over 5 minutes, check the `I'm having problems with resizing the volume`.  

### From the CLI

1. Locate the `instance ID` for the instance you want to resize the volume of:

    ```sh
    openstack database instance list
    ```

2. `Resize the volume` of the instance:

    ```sh
    openstack database instance resize volume $INSTANCE_ID $NEW_VOLUME_SIZE
    ```

    for example:  
    openstack database instance resize volume `f37a8ea6-5ed7-4982-8a71-9131756f04ae` `5`

3. You can check the `status of the instance`:

    ```sh
    openstack database instance show $INSTANCE_ID
    ```  

    After 1-2 minutes, the command should return the status as `ACTIVE`  
    If the status is `Resizing` for over 5 minutes, check the `I'm having problems with resizing the volume`.  
