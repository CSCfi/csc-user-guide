# How to backup a Postgres DB into Allas

In this tutorial we are going to show how to backup a PostgreSQL DB running in Rahti into Allas. The general idea is to use a `CronJob` that will create a dump file of the database and upload it to Allas.

This is a simple example, the backup SQL file is not compressed, the checksums are not verified, there is no encryption, ... it just shows the basic idea of creating a backup and putting it in object storage.

## Prerequisites

* A postgres DB. You need to have read access to it. To deploy a new DB in Rahti, you can use the Postgres template provided in the catalog. It is also possible to backup an external DB, but all instructions assume the DB is running in Rahti in the same namespace as the backup process will be run.


* A secret called `postgresql` with the following keys: `database-user`, `database-password`, and `database-name`. This secret is created by Postgres's template, but will need to be created manually if Postgres is running outside Rahti.

* The `ACCESS_KEY` and `SECRET_KEY` to access Allas. You may get them by doing:

```bash
pip install python-openstackclient
```

Then go to [Access & Security](https://pouta.csc.fi/dashboard/project/api_access/), download the OpenStack RC File v3.0, source it, and input your password when prompted:

```bash
$ source ~/Downloads/project_XXXXXXX-openrc.sh
Please enter your OpenStack Password for project project_XXXXXXX as user <USER>:

```

Finally you can create the credentials:

```bash
openstack ec2 credentials create
```

Or if you already have created the credentials, you may show them by doing:

```bash
openstack ec2 credentials list -f yaml
```

* An Allas bucket/container. You may create it from the web interface, or using `rclone`.

## Add the CronJob

First you need to clone the repository with the template and add it to the Rahti namespace where Postgres is running:

```sh
git clone https://github.com/lvarin/rclone-template.git -b psql
cd rclone-template
oc create -f rclone.yaml
```

Once the template is added to your namespace, you just need to deploy it:

```sh
$ oc process rclone \
    ACCESS_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \
    SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \
    BUCKET_DIR=existing_bucket/existing/path \
    SCHEDULE="0 4 * * *" | oc create -f -
```

This will run the backup process every day at 4:00 am. You may change the schedule, see <https://en.wikipedia.org/wiki/Cron> for reference.

