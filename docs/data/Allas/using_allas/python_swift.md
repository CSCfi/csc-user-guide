
# Allaksen käyttö Pythonin ja SWIFT-protokollan kanssa {#using-allas-with-python-and-swift-protocol}

CSC:n ohjeet [OpenStackin ja muiden tarvittavien Python-kirjastojen asentamiseen](../../../cloud/pouta/install-client.md).

Lataa **OpenStack RC File v3** viimeisessä osiossa annettujen ohjeiden mukaan [*Configure your terminal environment for OpenStack*](../../../cloud/pouta/install-client.md#configure-your-terminal-environment-for-openstack).

Esimerkeissä tarvittavat **Python pip -kirjastot**:  
*python-keystoneclient* ja *python-swiftclient*.

Tämä sivu sisältää Python-skriptit seuraaville toiminnoille:

| Toiminto |
| :--- |
| Luo yhteys palvelimeen |
| Luo bucket |
| Lataa objekti |
| Listaa bucketit ja objektit |
| Lataa objekti palvelimelta |
| Poista bucketit ja objektit |

## Luo yhteys {#create-a-connection}

Tämä Python-skripti luo yhteyden palvelimeen:
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

Vaihtoehtoisesti voit syöttää tiedot suoraan skriptiin ladatusta RC-tiedostosta:

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

Ylläolevassa esimerkissä:

| | | |
|-|-|-|
| OS_AUTH_URL | = _authurl | = *https://pouta.csc.fi:5001/v3*  |
| OS_IDENTITY_API_VERSION | = _auth_version | = *3*  |
| OS_USERNAME | = _user | = *John*  |
| OS_PASSWORD | = _key | = *John1234* |  
| OS_PROJECT_NAME | = project_name | = *project_123456* |

Lisätietoa _Keystone autentikoinnista_:  
[https://docs.openstack.org/python-swiftclient/newton/client-api.html](https://docs.openstack.org/python-swiftclient/newton/client-api.html) 

## Luo bucket {#create-a-bucket}

Luo uusi bucket seuraavalla skriptillä:

```python
bucket_name='snakebucket'
conn.put_container(bucket_name)
```

## Lataa objekti {#upload-an-object}

Lataa pieni tiedosto nimeltä `my_snake.txt` bucketiin `snakebucket`:

```python
object_name='my_snake.txt'
with open(object_name, 'r') as f:
    conn.put_object(bucket_name, object_name,
                    contents=f.read(),
                    content_type='text/plain')
```
Ylläoleva latausprosessi toimii vain tiedostoille, jotka ovat pienempiä kuin 5 GB. 
Suurempien tiedostojen tapauksessa sinun pitäisi käyttää _SwiftService_-palvelua.

```python
object_list = [ 'my_snake.txt' ]
# rajaa lataus säikeitä neljään
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


## Listaa bucketit ja objektit {#list-buckets-and-objects}

Listaa kaikki projektiin kuuluvat bucketit:
```python
resp_headers, containers = conn.get_account()

for container in containers:
   print(container)
```

Ja kaikki buckettiin kuuluvat objektit:
```python
for info in conn.get_container('snakebucket')[1]:
    print('{0}\t{1}\t{2}'.format(info['name'], info['bytes'], info['last_modified']))
```

## Lataa objekti palvelimelta {#download-an-object}

Lataa objekti:
```python
my_obj = conn.get_object(bucket_name, object_name)[1]
with open('new_name_for_file.txt', 'w') as f:
    f.write(my_obj)
```

**Huomaa:** Jos saat virheen
```python
TypeError: write() argument must be str, not bytes
```
avaa tiedosto binääritilassa
```python
with open('new_name_for_file.txt', 'bw') as f:
    f.write(my_obj)
```
sen sijaan, että käyttäisit tekstitilaa.

## Poista bucketit ja objektit {#remove-buckets-and-objects}

Poista bucket:
```python
conn.delete_container(bucket_name)
```

**Huom:** Vain tyhjät bucketit voidaan poistaa.

Poista objekti:
```python
conn.delete_object(bucket_name, 'my_snake.txt')
```
