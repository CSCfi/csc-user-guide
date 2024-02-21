# Using Allas with Python and SWIFT protocol

CSC's instructions for [Installing OpenStack and other required Python libraries](../../../cloud/pouta/install-client.md).

Download the **OpenStack RC File v3** as instructed in the last section [*Configure your terminal environment for OpenStack*](../../../cloud/pouta/install-client.md#configure-your-terminal-environment-for-openstack).

The **Python pip libraries** required in the examples:  
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

## Create a connection

This Python script creates a connection to the server:
```python
from keystoneauth1 import session
from keystoneauth1.identity import v3
import os
import swiftclient
from swiftclient.multithreading import OutputManager
from swiftclient.service import SwiftError, SwiftService, SwiftUploadObject


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

Alternatively, you can enter the information directly in the script from the downloaded RC file:

```python
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
  
In the above example:

| | | |
|-|-|-|
| OS_AUTH_URL | = _authurl | = *https://pouta.csc.fi:5001/v3*  |
| OS_IDENTITY_API_VERSION | = _auth_version | = *3*  |
| OS_USERNAME | = _user | = *John*  |
| OS_PASSWORD | = _key | = *John1234* |  
| OS_PROJECT_NAME | = project_name | = *project_123456* |

Further information of the _Keystone authentication_:  
[https://docs.openstack.org/python-swiftclient/newton/client-api.html](https://docs.openstack.org/python-swiftclient/newton/client-api.html) 

## Create a bucket

Create a new bucket using the following script:

```python
bucket_name='snakebucket'
conn.put_container(bucket_name)
```

## Upload an object

Upload a small file called `my_snake.txt` to the bucket `snakebucket`:

```python
object_name='my_snake.txt'
with open(object_name, 'r') as f:
    conn.put_object(bucket_name, object_name,
                    contents=f.read(),
                    content_type='text/plain')
```
The upload process above works only for files that are smaller than 5 GB. 
In the case of larger files, you should use _SwiftService_.

```python
object_list = [ 'my_snake.txt' ]
# limit upload threads to 4
opts = {'object_uu_threads': 4}

with SwiftService(options=opts) as swift:
    try:
        for r in swift.upload(bucket_name, object_list, { 'segment_size': 5000000000, }):
            if r['success']:
                if 'object' in r:
                    print(r['object'])
                elif 'for_object' in r:
                    print(
                        '%s segment %s' % (r['for_object'],
                            r['segment_index'])
                         )
            else:
                print(r)

    except SwiftError as e:
        print(e.value)
```



## List buckets and objects

List all buckets belonging to a project:
```python
resp_headers, containers = conn.get_account()

for container in containers:
   print(container)
```

And all objects belonging to a bucket:
```python
for info in conn.get_container('snakebucket')[1]:
    print('{0}\t{1}\t{2}'.format(info['name'], info['bytes'], info['last_modified']))
```

## Download an object

Download an object:
```python
my_obj = conn.get_object(bucket_name, object_name)[1]
with open('new_name_for_file.txt', 'w') as f:
    f.write(my_obj)
```

**Please note:** If you get the error
```python
TypeError: write() argument must be str, not bytes
```
open the file in the binary mode
```python
with open('new_name_for_file.txt', 'bw') as f:
    f.write(my_obj)
```
instead of the text mode.


## Remove buckets and objects

Delete a bucket:
```python
conn.delete_container(bucket_name)
```

**Note:** Only empty buckets can be removed.

Remove an object:
```python
conn.delete_object(bucket_name, 'my_snake.txt')
```
