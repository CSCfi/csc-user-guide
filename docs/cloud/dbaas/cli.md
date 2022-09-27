# Using DBaaS with CLi

## Getting started
The DBaaS is using openstack on the background this means that you can use the openstack CLI in a similar way as Pouta. It is important to note that even if Pouta uses the same command line it does not mean that you are connecting to Pouta.

1. First make sure that you have `python3` installed.
2. Then install the command line tools 

    pip3 install python-openstackclient python-troveclient

3. You need to download your openrc file from the https://pukki.dbaas.csc.fi and choose correct project number then go to `API Access` and `Download OpenStack RC file` choose `OpenStack RC file`.
4. Once you have downloaded the file you can source it by running 

    source $FILENAME

5. After that you should be able to verify that it works by listing available datastores (available types of databases)

    openstack datastore list

Remember that you can use the help command like: `openstack help database` and the flag `--help` to find out more about the different commands.

## Creating a  database instances
1. Make sure that you have sourced the openrc file that you donwloaded from https://pukki.dbaas.csc.fi

2. Before creating a database it is a good idea to know what kind of setting you want to use. These are the main things that you want to collect:

The `name` of your new database instance. (In this example we will use `my_database_instance`)

What `databases` you want to create (in this example we will just use `my_first_database`)

`IP addresses` form where you would like to access your database. You can usally find out your IP by googling what is my IP or using a homepage like this from CLI

    curl ifconfig.me

`Flavor` for example `standard.small` . You can list avialble flavors by:

     openstack database flavor list

`Datastore` Suggestion: `postgresql` You can find datastores by:

    openstack datastore list

`datastore version` This depends on the datstore you have choosen and you should usally choose the latest. If you use postgresql you can proabably use `14.2`. You can find out the avialable datastore versions by:

    openstack datastore version list postgresql

How big `volume` in GiB you want to use to store your database. If this is your first time testing DBaaS you will get by `1` GiB.

What `username` and `password` you want to use. (In this example we will use `databaseuser` and `myPassword568`

3. Once you gather the data you want to use to crate your database you can do it by running the following command. Please update the variables how you see fit, especially `MY_IP` . You can also use the flag `--allowed-cidr` multiple times to add multiple IP-addresses.

    openstack database instance create my_database_instance \
    --flavor standard.small \
    --databases my_first_database
    --users databaseuser:myPassword568 \
    --datastore postgresql
    --datastore-version 14.2 \
    --is-public \
    --size 1 \
    --allowed-cidr ${MY_IP}/32

If you have any issues don't hesitate using the `openstack database instance create --help` command.

8. Now you need to wait a couple of minutes until the database instances have been created and received a public IP. Once the instances have recivced an `HEALTHY` state the public IP should be visible. The following command will show you info about the instance: 

    openstack database instance show $INSTANCE_ID

9. If you are not happy with the firewalls ( `--allowed-cidr` ) you can update them by:

    openstack database instance update $INSTANCE_ID --allowed-cidr $NEW_IP_RANGE

It is a good idea to check out what the command options are by `openstack database instance update --help`


More information about how to connect to database can be found in the `Databases` section on the left hand side.


##  Additional useful commands

##### Create additional database in database instance
This is similar to do a CREATE DATABASE db_name;

    openstack database db create $INSTANCE_ID $DB_NAME 

##### Add user to your database and update permissions

List existing users in the database

    openstack database user list $INSTANCE_ID

Create user (--databases is not necessary)

    openstack database $INSTANCE_ID $USER_NAME $PASSWORD --databases $DB_NAME

Add access to database (you can add multiple databases or remove)

    openstack database $INSTNACE_ID $USER_NAME $DATABASE_NAME

##### Delete instance

Figure out what database instance you would like to delete

    openstack database instance list

Delete the instances

    openstack database instance delete $INSTANCE_ID

##### Supported functionallity

| Openstack command | supported | Comments |
|--- |:---:|:---|
| openstack database backup create 			| DONE		|	All flags are not tested |
| openstack database backup delete 			| DONE 	 	|                           |
| openstack database backup execution delete 		| Not avialable | 	Not investigated yet|
| openstack database backup list 			| DONE 		|                           |
| openstack database backup list instance 		| DONE 	 	|                           |
| openstack database backup show 			| DONE 		|                           |
| openstack database backup strategy create 		| DONE 	 	|                           |
| openstack database backup strategy delete 		| DONE 	 	|                           |
| openstack database backup strategy list 		| DONE 	 	|                           |
| openstack database cluster create 			| Not avialable | 	Not investigated yet|
| openstack database cluster delete 			| Not avialable | 	Not investigated yet|
| openstack database cluster force delete 		| Not avialable | 	Not investigated yet|
| openstack database cluster grow 			| Not avialable | 	Not investigated yet|
| openstack database cluster list 			| Not avialable | 	Not investigated yet|
| openstack database cluster list instances 		| Not avialable | 	Not investigated yet|
| openstack database cluster modules 			| Not avialable | 	Not investigated yet|
| openstack database cluster reset status 		| Not avialable | 	Not investigated yet|
| openstack database cluster show 			| Not avialable | 	Not investigated yet|
| openstack database cluster shrink 			| Not avialable | 	Not investigated yet|
| openstack database cluster upgrade 			| Not avialable | 	Not investigated yet|
| openstack database configuration attach 		| Not avialable | 	Not investigated yet|
| openstack database configuration create 		| Not avialable | 	Not investigated yet|
| openstack database configuration default 		| Not avialable | 	Not investigated yet|
| openstack database configuration delete 		| Not avialable | 	Not investigated yet|
| openstack database configuration detach 		| Not avialable | 	Not investigated yet|
| openstack database configuration instances 		| Not avialable | 	Not investigated yet|
| openstack database configuration list 		| Not avialable | 	Not investigated yet|
| openstack database configuration parameter list	| Not avialable | 	Not investigated yet|
| openstack database configuration parameter set 	| Not avialable | 	Not investigated yet|
| openstack database configuration parameter show 	| Not avialable | 	Not investigated yet|
| openstack database configuration set 			| Not avialable | 	Not investigated yet|
| openstack database configuration show 		| Not avialable | 	Not investigated yet|
| openstack database db create 				| DONE ||
| openstack database db delete 				| DONE | |
| openstack database db list 				| DONE || 
| openstack database flavor list 			| DONE 	 ||
| openstack database flavor show 			| DONE 	 ||
| openstack database instance create 			| DONE 	 ||
| openstack database instance delete 			| DONE 	 ||
| openstack database instance detach 			| Not avialable | 	 |
| openstack database instance eject 			| Not avialable | 	 |
| openstack database instance force delete 		| Not avialable | 	Only admins can force delete|
| openstack database instance list 			| DONE 	 ||
| openstack database instance promote 			| Not avialable | 	 |
| openstack database instance reboot 			| Not avialable | 	Only admins can reboot DB instances|
| openstack database instance rebuild 			| Not avialable | 	Only admins can rebuild DB instances|
| openstack database instance reset status 		| Not avialable | 	Only admins modify the status|
| openstack database instance resize flavor 		| Not avialable | 	Works but not recommended by DBaaS team|
| openstack database instance resize volume 		| Not avialable | 	Does not work without admin intervention, require hard reboot.|
| openstack database instance restart 			| DONE 	 ||
| openstack database instance show 			| DONE 	 ||
| openstack database instance update 			| DONE 		| 	Subset of the flags are supported. Flags that are supported: --name , --allowed-cidr|
| openstack database instance upgrade 			| Not avialable | 	 
| openstack database limit list 			| Not avialable | 	Command works but unclear how it should be used|
| openstack database log list 				| Not avialable | 	 |
| openstack database log save 				| Not avialable | 	 |
| openstack database log set 				| Not avialable | 	 |
| openstack database log show 				| Not avialable | 	 |
| openstack database log tail 				| Not avialable | 	 |
| openstack database quota show 			| Not avialable | 	Only admins can see this|
| openstack database quota update 			| Not avialable | 	Only admins can see this|
| openstack database root disable 			| DONE 	||
| openstack database root enable 			| DONE 		| 	It is not recommended to enable root you might break the DBaaS integration|
| openstack database root show 				| DONE 	 ||
| openstack database user create 			| DONE 	 ||
| openstack database user delete 			| DONE 	 ||
| openstack database user grant access 			| DONE 	 ||
| openstack database user list 				| DONE 	 ||
| openstack database user revoke access 		| DONE 	 ||
| openstack database user show 				| DONE 	 ||
| openstack database user show access 			| DONE 	 ||
| openstack database user update attributes 		| DONE 	 ||
| openstack datastore delete  				| Not avialable |	Only admins|
| openstack datastore list 				| DONE 	 	||
| openstack datastore show 				| DONE 	 	||
| openstack datastore version create 			| Not avialable | 	Only admins|
| openstack datastore version delete 			| Not avialable | 	Only admins|
| openstack datastore version list 			| DONE 		||
| openstack datastore version set 			| Not avialable	| 	Only admins |
| openstack datastore version show 			| DONE		||
