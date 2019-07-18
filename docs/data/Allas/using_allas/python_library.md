------------------

## Python library

Some details about setting up the client with **keystone authentication**: [https://docs.openstack.org/python-swiftclient/newton/client-api.html](https://docs.openstack.org/python-swiftclient/newton/client-api.html){:target="_blank"} 
 
Some usage examples in **CEPH RadosGW Swift** documentation: [http://docs.ceph.com/docs/jewel/radosgw/swift/python/](http://docs.ceph.com/docs/jewel/radosgw/swift/python/){:target="_blank"}
 
CSC Instructions for how to use the **CLI**: [https://research.csc.fi/pouta-install-client](https://research.csc.fi/pouta-install-client){:target="_blank"}
 
The **python pip libraries** needed for the example below are: _python-keystoneclient_ and _python-swiftclient_.
 
Then create this script:
```bash
salmon << EOF > list_swift.py
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

resp_headers, containers = conn.get_account()

for container in containers:
   print container
EOF
```
Use it to list objects:
```bash
$ python list_swift.py
{u'count': 1, u'bytes': 1099122, u'name': u'fishes'}
{u'count': 0, u'bytes': 0, u'name': u'salmon.jpg'}
```
