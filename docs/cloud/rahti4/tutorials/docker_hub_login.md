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
    * You will need a TOKEN, go to <https://hub.docker.com/settings/security> and create a token. You will be able to see when the token was last used. Also you can create several tokens, and use them in different projects, increasing security.

* Secondly, navigate to the Web UI and select developer view. On the left navigation, select **Secrets**.

* On upper right, click "Create" menu, and select "Image pull secret". Set the following values:
    * Secret name = give it a clear name, this will be used later
    * Authentication type = "Image Registry Credentials"
    * Registry server address = "docker.io"
    * Username = your docker user name
    * Password = your docker **token**
    * Email = your docker email

![create secret](/cloud/rahti4/img/create_docker_hub_secret.png)

* Verify values are correct and select "Create".

* Next we'll go to command line. Log in and use following commands to link credentials to service accounts:

```sh
$ oc -n <project-name> secrets link builder <secret-name> --for=pull
$ oc -n <project-name> secrets link deployer <secret-name> --for=pull
$ oc -n <project-name> secrets link default <secret-name> --for=pull
```

**Note**: Substitute <project-name> place holder with actual project name (without <>) and <secret-name> with actual secret-name.

## Troubleshooting

If the error persists, you may check two things:

1. From <https://hub.docker.com/settings/security> you will be able to see when the token was last used. Please check that if the time there matches the last time it should have been used.

1. Check that the links between the secret and the service accounts are there:

```sh
$ oc -n <project-name> describe sa builder
$ oc -n <project-name> describe sa deployer
$ oc -n <project-name> describe sa default
```

**Note**: Substitute <project-name> place holder with actual project name (without <>).
