
# Python library

This chapter gives guidance for using Allas with **Python**. The instructions includes some commonly used basic operations but feel free to discover more.

CSC instructions for how to install Python and the required libraries can be found from:  
[https://research.csc.fi/pouta-install-client](https://research.csc.fi/pouta-install-client){:target="_blank"}.

Download the **OpenStack RC File v3** as guided in the last chapter *3.4.1.3 Configure your terminal environment for OpenStack*.

The **Python pip libraries** needed for the examples below are:  
 *python-keystoneclient* and *python-swiftclient*.

This page includes Python scripts for the following operations:

| Function |
| :--- |
| Create a connection to server |
| Create a bucket |
| Upload an object |
| List buckets and objects |
| Download an object |
| Remove buckets and objects |

&nbsp; 

## Create a connection

This Python script creates a connection to the server:

```bash
from keystoneauth1 import session
from keystoneauth1.identity import v3
import swiftclient
import os

_authurl = os.environ['OS_AUTH_URL']
_auth_version = os.environ['OS_IDENTITY_API_VERSION']
_user = os.environ['OS_USERNAME']
_key = os.environ['OS_PASSWORD']
_os_options = {
    'user_domain_name': os.environ['OS_USER_DOMAIN_NAME'],
    'project_domain_name': os.environ['OS_USER_DOMAIN_NAME'],
    'project_name': os.environ['OS_PROJECT_NAME']
}

conn = swiftclient.Connection(
    authurl=_authurl,
    user=_user,
    key=_key,
    os_options=_os_options,
    auth_version=_auth_version
)
```

Alternatively, you can write the information directly to the script from the downloaded RC file:

```bash
import swiftclient

_authurl = 'https://pouta.csc.fi:5001/v3'
_auth_version = '3'
_user = 'John'
_key = 'John1234'
_os_options = {
    'user_domain_name': 'Default',
    'project_domain_name': 'Default',
    'project_name': 'project_123456'
}

conn = swiftclient.Connection(
    authurl=_authurl,
    user=_user,
    key=_key,
    os_options=_os_options,
    auth_version=_auth_version
)
```

  
In the example above:

| | | |
|-|-|-|
| OS_AUTH_URL | = _authurl | = *https://pouta.csc.fi:5001/v3*  |
| OS_IDENTITY_API_VERSION | = _auth_version | = *3*  |
| OS_USERNAME | = _user | = *John*  |
| OS_PASSWORD | = _key | = *John1234* |  
| OS_PROJECT_NAME | = project_name | = *project_123456* |

For further information of *Keystone authentication*, see:  
[https://docs.openstack.org/python-swiftclient/newton/client-api.html](https://docs.openstack.org/python-swiftclient/newton/client-api.html){:target="_blank"} 


&nbsp; 

## Create a bucket

You can create a new bucket with script:

```bash
bucket_name='snakebucket'
conn.put_container(bucket_name)
```

&nbsp; 



## Upload an object

Uploading an object called "my_snake.txt" to bucket "snakebucket" can be done with script:

```bash
object_name='my_snake.txt'
with open(object_name, 'r') as f:
    conn.put_object(bucket_name, object_name,
                    contents=f.read(),
                    content_type='text/plain')
```

&nbsp; 


## List buckets and objects

You can list all the buckets belonging to the project with the following script:

```bash
resp_headers, containers = conn.get_account()

for container in containers:
   print(container)
```

And all the objects belonging to a bucket:

```bash
for info in conn.get_container('snakebucket')[1]:
    print('{0}\t{1}\t{2}'.format(info['name'], info['bytes'], info['last_modified']))
```

&nbsp; 


## Download an object

Yoy can download an object with script:

```bash
my_obj = conn.get_object(bucket_name, object_name)[1]
with open('new_name_for_file.txt', 'w') as f:
    f.write(my_obj)
```

**Please note:** If you get error:
```bash
TypeError: write() argument must be str, not bytes
```
add condition:
```bash
if type(my_obj)==bytes:
    my_obj = my_obj.decode('utf-8')
```
before opening the file.

&nbsp; 


## Remove buckets and objects

Deleting a bucket can be done with script:
```bash
conn.delete_container(bucket_name)
```
**Note:** Only empty buckets can be removed.

You can remove an object with script:
```bash
conn.delete_object(bucket_name, 'my_snake.txt')
```