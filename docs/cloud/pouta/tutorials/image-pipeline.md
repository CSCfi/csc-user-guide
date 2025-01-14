# Setting up a pipeline for images

## Objectives

* Get familiarity on how to use multiple cloud services together.
* Get familiarity on how to use cloud services using their command-line interfaces.

The tutorial focuses on the following services:

* Allas
* cPouta
* Pukki

## Introduction

We want to set up a simple pipeline which transforms the images that are given in input to it.

![image-pipeline-diagram](../../img/image-pipeline-diagram.png)

We use Allas as the place where to upload our images in input.
The pipeline uploads its transformed images to Allas too.
A virtual machine in cPouta takes care of downloading, transforming, and re-uploading the images received in input.
Once it has transformed an image, the virtual machine also logs the event to a database hosted in Pukki.

For the sake of this tutorial, the transformed image simply corresponds to the input image whose colors are inverted.

## Step 1: creating buckets in Allas

We open a new terminal window, to which we will refer using the name `terminal_A`.
We use `terminal_A` for all the commands dealing with Allas.

To create buckets in Allas, we need to have a working command-line interface for it.
If we haven't set up such interface before on our workstation, we follow the [instructions on how to install and configure s3cmd](https://docs.csc.fi/data/Allas/using_allas/s3_client/#getting-started-with-s3cmd).

We can test the correct functioning of the command-line interface by simply listing all the buckets currently in our project.
An example of the command and itse expected output follows:
```
$ s3cmd ls
2021-07-14 15:14  s3://bucket1
2020-01-14 17:40  s3://bucket2
...
```
Please note that the list can also be empty, if we haven't created any bucket in our project before.

We create the input and the output buckets for our pipeline using the following commands:
```
$ s3cmd mb s3://input_bucket
Bucket 's3://input_bucket/' created
$ s3cmd mb s3://output_bucket
Bucket 's3://output_bucket/' created
```

!!! warning
    Bucket names must be unique.
    If another user has already selected the same name, bucket creation command will fail:
    ```
    $ s3cmd mb s3://input_bucket
    ERROR: Bucket 'input_bucket' already exists
    ERROR: S3 error: 409 (BucketAlreadyExists)
    ```
    In such case, we can just select a different name and retry the command.

In the rest of the tutorial, we assume:

* the name of the bucket used for uploading images to the pipeline is `input_bucket`
* the name of the bucket used by the pipeline to make available its outputs is `output_bucket`

## Step 2: creating database in Pukki

We open a second terminal window, to which we will refer using the name `terminal_B`.
We use `terminal_B` for all the commands dealing with Pukki.

Having a working command-line interface for Pukki is a prerequisite for continuing with the tutorial.
If we haven't set it up before, we follow the [instructions on how to install and configure Pukki command-line interface](https://docs.csc.fi/cloud/dbaas/cli/#getting-started).

We can test the correct functioning of the command-line interface by simply listing the available types of database.
An example of the command and its expected output follows:
```
$ openstack datastore list
+--------------------------------------+------------+
| ID                                   | Name       |
+--------------------------------------+------------+
| 71920375-6967-466e-b955-8ee8629312b7 | postgresql |
| 1a8efda2-7bb7-4c52-9eab-e251fd18323c | mariadb    |
+--------------------------------------+------------+
```

We now create the database that we use to log the actions of the pipeline by issuing the following command:
```
$ openstack database instance create pipeline_db_instance \
--flavor standard.small \
--databases pipeline_db \
--users db_admin:db_password \
--datastore postgresql \
--is-public \
--size 1
```

The output from the command should be similar to the following:
```
+--------------------------+--------------------------------------+
| Field                    | Value                                |
+--------------------------+--------------------------------------+
| allowed_cidrs            | []                                   |
| created                  | 2025-01-10T15:45:12                  |
| datastore                | postgresql                           |
| datastore_version        | 17.2                                 |
| datastore_version_number | 17.2                                 |
| flavor                   | d4a2cb9c-99da-4e0f-82d7-3313cca2b2c2 |
| id                       | dee965df-049e-4eca-bb86-d74dbd607a1f |
| name                     | pipeline_db_instance                 |
| operating_status         |                                      |
| public                   | True                                 |
| region                   | regionOne                            |
| service_status_updated   | 2025-01-10T15:45:12                  |
| status                   | BUILD                                |
| updated                  | 2025-01-10T15:45:12                  |
| volume                   | 1                                    |
+--------------------------+--------------------------------------+
```

In the rest of the tutorial, we assume that:

* the name of the database instance in Pukki is `pipeline_db_instance`
* the name of the postgresql database is `pipeline_db`
* the username for the admin of the postgresql database is `db_admin`
* the password for the admin of the postgresql database is `db_password`

## Step 3: creating virtual machine in cPouta

We open a third terminal window, to which we will refer using the name `terminal_C`.
We use `terminal_C` for all the commands dealing with cPouta.

In the same way as for Allas and Pukki, to continue the tutorial we need to have a working command-line interface for cPouta as well.
We follow the [instructions on how to install and configure cPouta command-line interface](https://docs.csc.fi/cloud/pouta/install-client/), if we haven't done it already.

We can test the correct functioning of the command-line interface by, for example, showing the properties of one of the flavors.
An example of the command and its expected output follows:
```
$ openstack flavor show standard.tiny
+----------------------------+--------------------------------------+
| Field                      | Value                                |
+----------------------------+--------------------------------------+
| OS-FLV-DISABLED:disabled   | False                                |
| OS-FLV-EXT-DATA:ephemeral  | 0                                    |
| access_project_ids         | None                                 |
| disk                       | 80                                   |
| id                         | 0143b0d1-4788-4d1f-aa04-4473e4a7c2a6 |
| name                       | standard.tiny                        |
| os-flavor-access:is_public | True                                 |
| properties                 | standard='true'                      |
| ram                        | 1000                                 |
| rxtx_factor                | 1.0                                  |
| swap                       |                                      |
| vcpus                      | 1                                    |
+----------------------------+--------------------------------------+
```

First, we create a keypair, which we will use to access the virtual machine once it is up and running.
To create a new keypair, we run the following command:
```
openstack keypair create mykeypair > mykeypair.pem
```

We check that the command has indeed created a file called `mykeypair.pem` in the current folder of our workstation.
```
$ ls mykeypair.pem
mykeypair.pem
```

We also restrict the permission of the just-created keypair file by issuing the following command:
```
$ chmod 600 mykeypair.pem
```

We now create the virtual machine that we will use for our pipeline.
The command we issue is the following:
```
$ openstack server create --flavor standard.tiny --image AlmaLinux-9 --key-name mykeypair pipeline_vm
```

The output from the command should be similar to the following:
```
+-----------------------------+------------------------------------------------------+
| Field                       | Value                                                |
+-----------------------------+------------------------------------------------------+
| OS-DCF:diskConfig           | MANUAL                                               |
| OS-EXT-AZ:availability_zone |                                                      |
| OS-EXT-STS:power_state      | NOSTATE                                              |
| OS-EXT-STS:task_state       | scheduling                                           |
| OS-EXT-STS:vm_state         | building                                             |
| OS-SRV-USG:launched_at      | None                                                 |
| OS-SRV-USG:terminated_at    | None                                                 |
| accessIPv4                  |                                                      |
| accessIPv6                  |                                                      |
| addresses                   |                                                      |
| adminPass                   | 3mNCv6E8y5rS                                         |
| config_drive                |                                                      |
| created                     | 2025-01-14T15:15:30Z                                 |
| flavor                      | standard.tiny (0143b0d1-4788-4d1f-aa04-4473e4a7c2a6) |
| hostId                      |                                                      |
| id                          | 27514aca-14f7-40dc-a47c-0a05a79281ed                 |
| image                       | AlmaLinux-9 (9e65c28a-5d4e-410c-bae3-96c6c6277377)   |
| key_name                    | mykeypair                                            |
| name                        | pipeline_vm                                          |
| progress                    | 0                                                    |
| project_id                  | ef20bcc4215d49ddbf33e5c5740d89fe                     |
| properties                  |                                                      |
| security_groups             | name='default'                                       |
| status                      | BUILD                                                |
| updated                     | 2025-01-14T15:15:30Z                                 |
| user_id                     | pozzamat                                             |
| volumes_attached            |                                                      |
+-----------------------------+------------------------------------------------------+
```

In the rest of the tutorial we assume that the name of the virtual machine in cPouta is `pipeline_vm`.

## Step 4: configuring the pipeline

Now that we have built all the components, we configure them to work as a pipeline.
First, we configure the virtual machine to allow us to access it from our workstation.
Then, we make sure that the virtual machine can work with the buckets in Allas, as well as that our database instance in Pukki accepts traffic coming from the virtual machine.
Finally, we install and configure in the virtual machine the tools required to get the pipeline working.

### Allowing traffic from workstation to virtual machine

Access to the virtual machine is regulated by means of _security groups_ and the rules they contain.
We thus create a new security group with a single rule, which allow access to the virtual machine, for example, from our workstation.

We go back to `terminal_C`.
We create a new security group issuing the following command:
```
$ openstack security group create pipeline_security_group
```

Output will look like the following:
```
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field           | Value                                                                                                                                                                      |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| created_at      | 2025-01-14T15:47:46Z                                                                                                                                                       |
| description     | pipeline_security_group                                                                                                                                                    |
| id              | 8c4acf2c-0884-42f7-b45b-d6197c9c9beb                                                                                                                                       |
| location        | cloud='', project.domain_id='default', project.domain_name=, project.id='ef20bcc4215d49ddbf33e5c5740d89fe', project.name='project_2003103', region_name='regionOne', zone= |
| name            | pipeline_security_group                                                                                                                                                    |
| project_id      | ef20bcc4215d49ddbf33e5c5740d89fe                                                                                                                                           |
| revision_number | 1                                                                                                                                                                          |
| rules           | created_at='2025-01-14T15:47:46Z', direction='egress', ethertype='IPv4', id='3c1f4d65-d1ea-4dfa-8107-268dd2d1a397', updated_at='2025-01-14T15:47:46Z'                      |
|                 | created_at='2025-01-14T15:47:46Z', direction='egress', ethertype='IPv6', id='7954977c-b555-48f1-886d-6555777591c3', updated_at='2025-01-14T15:47:46Z'                      |
| tags            | []                                                                                                                                                                         |
| updated_at      | 2025-01-14T15:47:46Z                                                                                                                                                       |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

We add the rule to allow access by issuing the following command:
```
$ openstack security group rule create --dst-port 22 --protocol tcp pipeline_security_group
```

The output will be similar to the following:
```
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field             | Value                                                                                                                                                                      |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| created_at        | 2025-01-14T15:51:32Z                                                                                                                                                       |
| description       |                                                                                                                                                                            |
| direction         | ingress                                                                                                                                                                    |
| ether_type        | IPv4                                                                                                                                                                       |
| id                | 6a78b15f-067b-44c0-abe6-58a152e19932                                                                                                                                       |
| location          | cloud='', project.domain_id='default', project.domain_name=, project.id='ef20bcc4215d49ddbf33e5c5740d89fe', project.name='project_2003103', region_name='regionOne', zone= |
| name              | None                                                                                                                                                                       |
| port_range_max    | 22                                                                                                                                                                         |
| port_range_min    | 22                                                                                                                                                                         |
| project_id        | ef20bcc4215d49ddbf33e5c5740d89fe                                                                                                                                           |
| protocol          | tcp                                                                                                                                                                        |
| remote_group_id   | None                                                                                                                                                                       |
| remote_ip_prefix  | 0.0.0.0/0                                                                                                                                                                  |
| revision_number   | 0                                                                                                                                                                          |
| security_group_id | 8c4acf2c-0884-42f7-b45b-d6197c9c9beb                                                                                                                                       |
| tags              | []                                                                                                                                                                         |
| updated_at        | 2025-01-14T15:51:32Z                                                                                                                                                       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

Now we apply the security group to the previously created virtual machine, so that this newly-created rule applies to its traffic.
```
$ openstack server add security group pipeline_vm pipeline_security_group
```
In case of success, the command will show no output.

### Connecting to the virtual machine

The virtual machine is now configured to allow traffic from our workstation but it is not reachable yet because it has no address assigned to it.

We go back to `terminal_C`.
We acquire a new address issuing the command:
```
$ openstack floating ip create public
```

The output will be similar to the following:
```
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field               | Value                                                                                                                                                                                                |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| created_at          | 2025-01-14T15:58:57Z                                                                                                                                                                                 |
| description         |                                                                                                                                                                                                      |
| dns_domain          | None                                                                                                                                                                                                 |
| dns_name            | None                                                                                                                                                                                                 |
| fixed_ip_address    | None                                                                                                                                                                                                 |
| floating_ip_address | 128.214.255.168                                                                                                                                                                                      |
| floating_network_id | 26f9344a-2e81-4ef5-a018-7d20cff891ee                                                                                                                                                                 |
| id                  | bea7b208-3111-4af4-9b75-15509a903036                                                                                                                                                                 |
| location            | Munch({'cloud': '', 'region_name': 'regionOne', 'zone': None, 'project': Munch({'id': 'ef20bcc4215d49ddbf33e5c5740d89fe', 'name': 'project_2003103', 'domain_id': 'default', 'domain_name': None})}) |
| name                | 128.214.255.168                                                                                                                                                                                      |
| port_details        | None                                                                                                                                                                                                 |
| port_id             | None                                                                                                                                                                                                 |
| project_id          | ef20bcc4215d49ddbf33e5c5740d89fe                                                                                                                                                                     |
| qos_policy_id       | None                                                                                                                                                                                                 |
| revision_number     | 0                                                                                                                                                                                                    |
| router_id           | None                                                                                                                                                                                                 |
| status              | DOWN                                                                                                                                                                                                 |
| subnet_id           | None                                                                                                                                                                                                 |
| tags                | []                                                                                                                                                                                                   |
| updated_at          | 2025-01-14T15:58:57Z                                                                                                                                                                                 |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
In particular, we note down the value returned for the field `floating_ip_address`, which in this case corresponds to `128.214.255.168`

We now associate the obtained address to our virtual machine by issuing the following command:
```
$ openstack server add floating ip pipeline_vm 128.214.255.168
```
In case of success, the command will show no output.

Everything is now ready.
We can test the connection to our virtual machine by issuing the command:
```
$ ssh -i mykeypair.pem almalinux@128.214.255.168
```

Most probably we will be asked the following question:
```
The authenticity of host '128.214.255.168 (128.214.255.168)' can't be established.
ED25519 key fingerprint is SHA256:D3+7xMloWirjr8z/19GcGR0RqRPvyDo6Ppd7KZJlkFA.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

We can safely answer `yes` and press enter, which will finally lead us to the virtual machine:
```
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '128.214.255.168' (ED25519) to the list of known hosts.
[almalinux@pipeline-vm ~]$
```

### Allowing traffic from virtual machine to database

## Step 5: testing the pipeline

## Conclusion
