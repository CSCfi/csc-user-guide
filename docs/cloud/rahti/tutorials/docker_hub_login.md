# How to add docker hub credentials to a project

Since 2nd November 2020, docker hub has imposed a rate limit for image pulls. For Rahti this means a
limit of 200 pulls every 6 hours. This limit can be easily reached and it prevents new applications to be deployed if the image is in docker hub.

The error looks like this:

```
Pulling image "docker.io/centos/python-38-centos7@sha256:da83741689a8d7fe1548fefe7e001c45bcc56a08bc03fd3b29a5636163ca0353" ...
pulling image error : toomanyrequests: You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limit
```

The solution involves using both the Web UI and the client:

* First, you need a docker hub account. It can be a free account. In this case you will still have rate limits, but only the pulls you have done using your credential will be taken into account for the rate limit. Paid accounts have no limit.

* Secondly, navigate to the Web UI and open your project. On the left navigation, select **Resources -> Secrets**.

* On upper right, select "Create Secret" button, and on the secret creation dialog, set:
  * Secret Type = "Image Secret"
  * Secret Name = give it a clear name, this will be used later
  * Authentication Type = "Image Registry Credentials"
  * Image Registry Server Address = "docker.io"
  * Username = your docker username
  * Password = your docker password
  * Email = your docker email

**Note**: Leave "Link secret to a service account." empty, we'll do this on command line.

![create secret](/cloud/rahti/img/create_docker_hub_secret.png)

* Verify values are correct and select "Create".

* Next we'll go to command line. Log in and use following commands to link credentials to service accounts:

```sh
$ oc -n <project-name> secrets link builder <secret-name> --for=pull
$ oc -n <project-name> secrets link deployer <secret-name> --for=pull
$ oc -n <project-name> secrets link default <secret-name> --for=pull
```

**Note**: Substitute <project-name> placeholder with actual project name (without <>) and <secret-name> with actual secret-name.

