# Application credentials.

You will need to use application credentials if you are planning on using the service API or using
the [OpenStack command line tools](cli.md). If you are not planning on using the API or command
line tools then you probably won't need any application credentials.

Application credentials are also very useful to create credentials with limited permissions. You can
create credentials that are only allowed to get data about your project. You can also create
credentials that can only modify a specific instance or create new instances. It is also possible
to create credentials that can do everything that you can.

One thing that is important to remember is that the application credentials are personal, this
means that the application credentials are owned by a user-account, and all operations that the
credentials does is on behalf of the user that created the credentials. This means that if a user
is removed from the project the users credentials will stop working.


## Creating application credentials

1. Go to the web-interface.
2. Choose witch project you want to use.
3. Go to `Identitiy` -> `Application Credentials`
4. Press `Create Applicaiton Credential`
5. It is a good idea to choose a descriptive name an description. Otherwise you might get confused
in the future why the application credentials exists. It might be a good idea to name your first 
credentials `Testing application credentials $TODAYS_DATE`.
6. Secret should be a long random string that you should keep secret.
7. It is a good idea to put an expiration date especially if you are testing the credentials only
for today.
<!-- 8. Choosing a role, you should choose `member`. The `reader` role does not work as one would expect
at the point of writing there is no difference between reader and member role when it comes to
managing your databases at the moment. In the future the reader role might become a read-only user
role. -->
8. There are two roles `reader` and `member`. Usually you want to use the `member` role you can find
out more in the [Using roles sections](#Using-roles).
9. Access rules this is useful when you want to make credentials with fine grained permissions
this is super useful if you want to build a lot of automation around your databases. For example
you can make a script that is only allowed to modify the users of a specific database or a
credentials that is only allowed to create new instances. You probably want to start using these
when you start to build automation around your databases. You can find more information about the
options in [Using access rules sections](#Using-access-rules).
<!--- TODO Add section
 -->

10. The `Unrestricted (dangerous)` check-box. This will allow your application credentials to
create new application credentials, this might be useful if you are a power-user of the CLI but you
should probably not give an application or automation credentials that have this permission.
11. Once you have created the application credentials you can either download the credentials as 
file that you can source or .yaml file or alternatively add the secret to your secret manager. The
secret key will not be possible to read once you have completed the credential created process.

12. If you download the application credentials you will get a file that contains something like this:

```
#!/usr/bin/env bash

export OS_AUTH_TYPE=v3applicationcredential
export OS_AUTH_URL=https://pukki.dbaas.csc.fi:5000/v3
export OS_IDENTITY_API_VERSION=3
export OS_REGION_NAME="pukki_dbaas"
export OS_INTERFACE=public
export OS_APPLICATION_CREDENTIAL_ID=xxxxxxxxxxxxxxxxxxxxxx
export OS_APPLICATION_CREDENTIAL_SECRET=xxxxxxxxxxxxxxxxxxx
```

13. If you source the file you can use it together with with [OpenStack command line tools](cli.md)
.
14. It is a good idea to test that the application credentials is allowed to do what you expect it
to be able to do. It is also a good idea to verify that it is NOT allowed to do what you expect it
not be allowed to do.

## Using roles
There are two roles available `reader` and `member`. The reader roles is a read-only role while the
member role is allowed to make changes to your project.

    * `reader` role can only collect data
from your project but not make any changes, this is good if you want to create a script that check
the state of your services. Sometimes it is nice to have a default reader account that you user for
day-to-day operation, when you collect information so that you can be sure that you can't do any
destructive commands.
    * `member` role is the normal user role it can do everything that the `reader` role but it can
also make changes to the system. When you log into the web-interface you have the `member` role
enabled.

## Using access rules 

It is possible to create application credentials that are limited to only do a selected API-calls.
To find out which API-calls are available you can take a look at this:
[OpenStack Database API](https://docs.openstack.org/api-ref/database/).

For example if you want to create an application credential that only have permission to list
your instances you can add the permission:

```
- service: database
  method: GET
  path: /v1.0/*/instances
```

(note: that the wildcard `*` can if you like be changed to your project-id)


With this permission you are only allowed to do `openstack database instance list`. If you would
also would like to do both. An application credential can how as many permissions as you like.
So if you would like to be able to "create", "list", "show" and "delete" database instances you
would need to do an application credential like this:

```
# Create instance
- service: database
  method: POST
  path: /v1.0/*/instances
# List instance
- service: database
  method: GET
  path: /v1.0/*/instances
# Show instances
- service: database
  method: GET
  path: /v1.0/*/instances/*
# Delete instances
- service: database
  method: DELETE
  path: /v1.0/*/instances/*
```

There are a lot of other permissions that might be interesting to you:
[OpenStack Database API](https://docs.openstack.org/api-ref/database/).













<!--
## Using the reader and member roles

NOTE: The reader role does not work as expected. ATM the services does not differiate between
reader and member you should 



When your create the applicaiton credentials you

TODO reader role does not work in Trove! The trove/policies/base.py probably needs to be updated
and all polices that uses `admin_or_owner` We probably want to use something like: `project_reader_or_admin`
and `project_member_api` as in nova/policies/base.py
-->


