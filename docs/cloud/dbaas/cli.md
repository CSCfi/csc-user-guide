# Using DBaaS with CLI

The DBaaS is using OpenStack on the backend, which means that you can use the OpenStack CLI in a similar way as in Pouta. It is important to note that even if Pouta uses the same command-line it does not mean that you are connected to Pouta. This is especially important if you are automating things in both Pouta and DBaaS since you need to connect to different Keystone endpoints.

## Getting started

1. First make sure that you have `python3` installed.
2. Then, install the command-line tools:

	```sh
	pip3 install python-openstackclient python-troveclient
	```

3. You need to download your `openrc` file from [Pukki](https://pukki.dbaas.csc.fi) and choose the correct project number. Then, go to `API Access` and `Download OpenStack RC file` and choose `OpenStack RC file`.
4. Once you have downloaded the file you can source it by running:

	```sh
	source $FILENAME
	```

5. After that you should be able to verify that it works by listing available datastores (available types of databases):

	```sh
	openstack datastore list
	```

Remember that you can use the help command as `openstack help database` and the flag `--help` to find out more about the different commands.

## Creating a database instance

1. Make sure that you have sourced the openrc file that you downloaded from [Pukki](https://pukki.dbaas.csc.fi).
2. Before creating a database it is a good idea to know what kind of settings you want to use. These are the main things that you want to collect:
	* The `name` of your new database instance. In this example we will use `my_database_instance`.
	* What `databases` you want to create. In this example we will just use `my_first_database`.
	* `IP addresses` from where you would like to access your database. You can usually find out your IP by googling what is my IP or using a homepage like this from CLI:

		```sh
		curl ifconfig.me
		```

	* `Flavor`, for example `standard.small` . You can list available flavors with:

		```sh
		openstack database flavor list
		```

	* `Datastore`, suggestion: `postgresql`. You can find datastores with:

		```sh
		openstack datastore list
		```

	* `datastore version`. This depends on the datastore you have chosen and you should usually choose the latest. If you use PostgreSQL you can probably use `14.5`. You can find out the available datastore versions with:

		```sh
		openstack datastore version list postgresql
		```

	* How large `volume` in GiB you want to use to store your database. If this is your first time testing DBaaS you will get by with `1` GiB.

	* What `username` and `password` you want to use. In this example we will use `databaseuser` and `myPassword568`.

3. Once you've gathered the data you want to use to create your database you can do it by running the following command. Please update the variables how you see fit, especially `MY_IP`. You can also use the flag `--allowed-cidr` multiple times to add multiple IP-addresses. By default the database instance are created without any `allowed-cidr` which means that you won't be able to connect to your database.

	```sh
	openstack database instance create my_database_instance \
	--flavor standard.small \
	--databases my_first_database \
	--users databaseuser:myPassword568 \
	--datastore postgresql \
	--datastore-version 14.5 \
	--is-public \
	--size 1 \
	--allowed-cidr ${MY_IP}/32
	```

	If you have any issues don't hesitate using the `openstack database instance create --help` command.

4. Now you need to wait a couple of minutes until the database instances have been created and received a public IP. Once the instances have received a `HEALTHY` state the public IP should be visible. Note that it will show you a private and public IP, you are only interested in the public IP. The following command will show you info about the instance:

	```sh
	openstack database instance show $INSTANCE_ID
	```

5. If you are not happy with the firewalls (`--allowed-cidr`) you can update them with:

	```sh
	openstack database instance update $INSTANCE_ID --allowed-cidr $NEW_IP_RANGE
	```

It is a good idea to check out what the command options are with `openstack database instance update --help`.

More information about how to connect to databases can be found in the `Databases` section in the left hand side navigation.

### Restoring from backups

You can use the same command as when creating a backup, but you need to use the flag and the backup id you want to use for restoring the backup, `--backup $BACKUP_ID`.

###  Additional useful commands

#### Create additional database in database instance

This is similar to do a `CREATE DATABASE db_name;`

```
openstack database db create $INSTANCE_ID $DB_NAME
```

#### Adding users to a database

List existing users in the database:

```
openstack database user list $INSTANCE_ID
```

Create a new user (`--databases` is optional):

```
openstack database user create $INSTANCE_ID $USER_NAME $PASSWORD --databases $DATABASE_NAME
```

### Removing users from a database

Deleting an user can be done by running:

```
openstack database user delete $INSTANCE_ID $USER_NAME
```

#### Delete instance

Figure out what database instance you would like to delete:

```
openstack database instance list
```

Delete the instances:

```
openstack database instance delete $INSTANCE_ID
```

#### Supported functionality

These are the available commands at the moment:

| Openstack command | status | Comments |
|--- |:---:|:---|
| openstack database backup create 			| Supported	|	All flags are not tested |
| openstack database backup delete 			| Supported 	|       Might be removed in future |
| openstack database backup execution delete 		| Not available | 	Not supported in DBaaS |
| openstack database backup list 			| Supported	||
| openstack database backup list instance 		| Supported 	||
| openstack database backup show 			| Supported	||
| openstack database backup strategy create 		| Not available	|	Only available for admins|
| openstack database backup strategy delete 		| Not available	|	Only available for admins|
| openstack database backup strategy list 		| Not available	| 	Only available for admins|
| openstack database cluster create 			| Not available | 	Not investigated yet|
| openstack database cluster delete 			| Not available | 	Not investigated yet|
| openstack database cluster force delete 		| Not available | 	Not investigated yet|
| openstack database cluster grow 			| Not available | 	Not investigated yet|
| openstack database cluster list 			| Not available | 	Not investigated yet|
| openstack database cluster list instances 		| Not available | 	Not investigated yet|
| openstack database cluster modules 			| Not available | 	Not investigated yet|
| openstack database cluster reset status 		| Not available | 	Not investigated yet|
| openstack database cluster show 			| Not available | 	Not investigated yet|
| openstack database cluster shrink 			| Not available | 	Not investigated yet|
| openstack database cluster upgrade 			| Not available | 	Not investigated yet|
| openstack database configuration attach 		| Supported     ||
| openstack database configuration create 		| Supported     ||
| openstack database configuration default 		| Supported     ||
| openstack database configuration delete 		| Supported     ||
| openstack database configuration detach 		| Supported     ||
| openstack database configuration instances 		| Supported     ||
| openstack database configuration list 		| Supported     ||
| openstack database configuration parameter list	| Supported     ||
| openstack database configuration parameter set 	| Supported     ||
| openstack database configuration parameter show 	| Supported     ||
| openstack database configuration set 			| Supported     ||
| openstack database configuration show 		| Supported     ||
| openstack database db create 				| Supported 	||
| openstack database db delete 				| Supported 	||
| openstack database db list 				| Supported 	||
| openstack database flavor list 			| Supported 	||
| openstack database flavor show 			| Supported 	||
| openstack database instance create 			| Supported 	||
| openstack database instance delete 			| Supported 	||
| openstack database instance detach 			| Not available ||
| openstack database instance eject 			| Not available ||
| openstack database instance force delete 		| Only admins 	||
| openstack database instance list 			| Supported 	||
| openstack database instance promote 			| Not available ||
| openstack database instance reboot 			| Only admins 	||
| openstack database instance rebuild 			| Only admins 	||
| openstack database instance reset status 		| Only admins 	||
| openstack database instance resize flavor 		| Supported     |	Be aware that this causes downtime |
| openstack database instance resize volume 		| Not supported	| 	Does not work without admin intervention |
| openstack database instance restart 			| Supported 	|	Restart the database container - limited benefit |
| openstack database instance show 			| Supported 	||
| openstack database instance update 			| Supported 	|	Subset of the flags are supported. Flags that are supported: --name , --allowed-cidr|
| openstack database instance upgrade 			| Supported 	| 	Upgrading the database instance. This command will cause downtime. |
| openstack database limit list 			| Supported 	||
| openstack database log list 				| Supported     |	Allows to view instance logs. This API is unstable and might get changed, it does not do the same thing as upstream |
| openstack database log save 				| Not available ||
| openstack database log set 				| Not available ||
| openstack database log show 				| Not available ||
| openstack database log tail 				| Not available ||
| openstack database quota show 			| Only admins 	||
| openstack database quota update 			| Only admins 	||
| openstack database root disable 			| Supported 	||
| openstack database root enable 			| Supported 	|	For most cases root enable is not necessary but if you want to do advanced permission configuration it is probably necessary. |
| openstack database root show 				| Supported 	||
| openstack database user create 			| Supported 	||
| openstack database user delete 			| Supported 	||
| openstack database user grant access 			| Supported 	||
| openstack database user list 				| Supported 	||
| openstack database user revoke access 		| Supported 	||
| openstack database user show 				| Supported 	||
| openstack database user show access 			| Supported 	||
| openstack database user update attributes 		| Supported 	||
| openstack datastore delete  				| Only admins 	||
| openstack datastore list 				| Supported 	||
| openstack datastore show 				| Supported 	||
| openstack datastore version create 			| Only admins 	||
| openstack datastore version delete 			| Only admins 	||
| openstack datastore version list 			| Supported	||
| openstack datastore version set 			| Only admins 	||
| openstack datastore version show 			| Supported	||
