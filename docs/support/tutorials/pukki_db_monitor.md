!!! error "Advanced level"
    You need to have Docker and Python knowledge.  
    Regarding Rahti, we will privilege the use of OpenShift CLI tool [oc](../../cloud/rahti/usage/cli.md)

# Monitor Pukki DBaaS instance sizes from a Rahti CronJob using application credentials

This tutorial shows how to run a **Rahti CronJob** that uses **Pukki application credentials** to query OpenStack DBaaS instances and send an email alert if any database instance volume exceeds a configured threshold (default: **90%**).

Application credentials are the recommended way to authenticate automated tools and scripts without exposing your personal username and password.


# Overview

The example workflow:

1. Create an application credential in Pukki
2. Store credentials as a Secret in Rahti
3. Build a container image with a monitoring script
4. Push the image to the Rahti internal registry
5. Deploy a CronJob
6. Run periodic checks and send email alerts

The script uses:

```bash
openstack database instance list -f json
openstack database instance show <instance_name> -f json
```

The example files can be found in [CSC github](https://github.com/CSCfi/pukki-dbaas-monitor)

# 1. Create application credentials in Pukki

1. Log in to Pukki

2. Select your project

3. Navigate to `Identity → Application Credentials`

4. Click **Create Application Credential**

5. Use Role: `reader`

6. Create the credential and download the file

!!! note
    Application credentials are linked to the user account that created them. If the user leaves the project or their access is revoked, the credentials will become invalid

Read more about [Application credentials here](../../cloud/dbaas/application-credentials.md)

# 2. Clone the example repository

Clone the example repository:

```sh
git clone https://github.com/CSCfi/rahti-openstack-dbaas-monitor.git
```

# 3. Configure Credentials in Rahti

Edit the file `db-monitor-openstack-secret.yaml`

Replace all placeholder values:

```
OS_AUTH_URL: "<replace me>"
OS_REGION_NAME: "<replace me>"
OS_APPLICATION_CREDENTIAL_ID: "<replace me>"
OS_APPLICATION_CREDENTIAL_SECRET: "<replace me>"
```

Then apply the Secret:

```sh
oc apply -f db-monitor-openstack-secret.yaml
```

# 4. Build and push the container image

Login to the Rahti registry:

```sh
sudo docker login -u unused -p $(oc whoami -t) image-registry.apps.2.rahti.csc.fi
```

Build the [image](https://github.com/CSCfi/pukki-dbaas-monitor/blob/main/Dockerfile) (uses [`requirements.txt`](https://github.com/CSCfi/pukki-dbaas-monitor/blob/main/requirements.txt), [`monitor_dbaas.py`](https://github.com/CSCfi/pukki-dbaas-monitor/blob/main/monitor_dbaas.py) ):

```sh
sudo docker build -t image-registry.apps.2.rahti.csc.fi/<replace me>/db-monitor:latest .
```

Push the image:

```sh
sudo docker push image-registry.apps.2.rahti.csc.fi/<replace me>/db-monitor:latest
```

For more info about Rahti registry [read here](../../cloud/rahti/images/Using_Rahti_integrated_registry.md)

# 5. Configure the CronJob

Open `db-monitor-cronjob.yaml` and update

image path:
```
image-registry.apps.2.rahti.csc.fi/<replace me>/db-monitor:latest
```
email settings:
```
MAIL_FROM: "<replace me>"
MAIL_TO: "<replace me>"
```
optional threshold:
```
THRESHOLD_PERCENT: "90"
```
Apply the configuration:

```sh
oc apply -f db-monitor-cronjob.yaml
```

# 6. Run a manual test

Before waiting for the scheduled run, test manually:

```sh
oc create job --from=cronjob/openstack-db-monitor db-monitor-test
oc logs -f job/db-monitor-test
```

You should see something like:

```
Starting OpenStack DBaaS volume usage check
Found 3 instance(s): db-a, db-b, db-c
db-a: 12.50%
db-b: 93.00%
Alert email sent for 1 instance(s)
```

# Conclusion

In this tutorial, you used Pukki application credentials to securely authenticate a Rahti-based automation workflow that monitors DBaaS instance storage.

Application credentials provide a safe and practical way to grant scripts and services access to OpenStack APIs without exposing personal user credentials. By storing them in Rahti Secrets and using them in a CronJob, you can build automated workflows that are both secure and maintainable.

When using application credentials, it is important to remember that they are tied to the user who created them. For long-running or shared services, you should plan how credentials are managed, rotated, and owned within the project to avoid unexpected disruptions.
