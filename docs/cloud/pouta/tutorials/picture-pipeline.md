# Kuvien käsittelyputken käyttöönotto { #setting-up-a-pipeline-for-images }

## Tavoitteet { #objectives }

* Harjoittele, miten useita pilvipalveluja käytetään yhdessä.
* Harjoittele pilvipalvelujen käyttöä niiden komentorivityökaluilla.

Tässä ohjeessa keskitytään seuraaviin palveluihin:

* [Allas](../../../data/Allas/introduction.md), objektivarastopalvelumme
* [cPouta](../index.md), julkinen pilvipalvelumme
* [Pukki](../../dbaas/what-is-dbaas.md), tilauspohjainen tietokantapalvelumme

## Johdanto { #introduction }

Haluamme pystyttää yksinkertaisen putken, joka muuntaa sille syötteenä annetut kuvat.

![picture-pipeline-diagram](../../img/picture-pipeline-diagram.png)

Ensin lähetämme kuvat työasemaltamme Allaksen bucketiin.
cPoutassa ajettava virtuaalikone noutaa kuvat bucketista ja lataa ne paikallisesti.
Virtuaalikone muuntaa kuvat ja kirjaa tehdyn toimen tietokantaan, joka on Pukissa.
Lopuksi virtuaalikone lataa muunnetut kuvat toiseen Allaksen bucketiin.
Tämän jälkeen voimme ladata muunnetut kuvat bucketista takaisin työasemallemme.

Tämän ohjeen yksinkertaisuuden vuoksi muunnettu kuva on alkuperäinen kuva, jonka värit on invertoitu, joskus kutsutaan myös “käännetyksi”.

## Vaihe 1: bucketien luominen Allakseen { #step-1-creating-buckets-in-allas }

Avaamme uuden pääteikkunan, johon viittaamme nimellä `terminal_allas`.
Käytämme `terminal_allas`-päätettä kaikkiin Allakseen liittyviin komentoihin.

Luodaksemme bucketteja Allakseen tarvitsemme toimivan komentorivikäyttöliittymän.
Ellei sellaista ole aiemmin työasemalle asennettu, seuraamme ohjetta [s3cmd:n asentaminen ja määrittäminen](../../../data/Allas/using_allas/s3_client.md#getting-started-with-s3cmd).

Voimme testata komentorivityökalun toiminnan listaamalla projektimme nykyiset bucketit.
Esimerkki komennosta ja odotetusta tulosteesta:
```
$ s3cmd ls
2021-07-14 15:14  s3://bucket1
2020-01-14 17:40  s3://bucket2
...
```
Huomaa, että lista voi olla myös tyhjä, jos emme ole aiemmin luoneet bucketteja projektiimme.

Luomme nyt putkeamme varten syöte- ja tulosbucketit.
Määritellään ensin bucketien nimet ympäristömuuttujiin:
```
$ export INPUT_BUCKET="input_bucket"
$ export OUTPUT_BUCKET="output_bucket"
```

Luodaan bucketit seuraavilla komennoilla:
```
$ s3cmd mb s3://$INPUT_BUCKET
Bucket 's3://input_bucket/' created
$ s3cmd mb s3://$OUTPUT_BUCKET
Bucket 's3://output_bucket/' created
```

!!! warning
    Bucketien nimien on oltava yksilöllisiä.
    Jos toinen käyttäjä on jo valinnut saman nimen, luonti epäonnistuu:
    ```
    $ s3cmd mb s3://$INPUT_BUCKET
    ERROR: Bucket 'input_bucket' already exists
    ERROR: S3 error: 409 (BucketAlreadyExists)
    ```
    Tällöin voit vain yrittää uudelleen eri nimellä.

## Vaihe 2: tietokannan luominen Pukkiin { #step-2-creating-a-database-in-pukki }

Avaamme toisen pääteikkunan, johon viittaamme nimellä `terminal_pukki`.
Käytämme `terminal_pukki`-päätettä kaikkiin Pukkiin liittyviin komentoihin.

Pukin komentorivityökalun toimivuus on edellytys ohjeen jatkamiselle.
Ellei sitä ole aiemmin määritetty, seuraamme ohjetta [Pukin komentorivityökalun asentaminen ja määrittäminen](../../dbaas/cli.md#getting-started).

Voimme testata työkalun toiminnan listaamalla saatavilla olevat tietokantatyypit.
Esimerkki komennosta ja odotetusta tulosteesta:
```
$ openstack datastore list
+--------------------------------------+------------+
| ID                                   | Name       |
+--------------------------------------+------------+
| 71920375-6967-466e-b955-8ee8629312b7 | postgresql |
| 1a8efda2-7bb7-4c52-9eab-e251fd18323c | mariadb    |
+--------------------------------------+------------+
```

Luomme nyt tietokannan, jota käytämme putken toimien lokittamiseen.
Määritellään ensin muutama ympäristömuuttuja myöhempää käyttöä varten:
```
$ export DB_INSTANCE_NAME="pipeline_db_instance" # name of the database instance in Pukki
$ export DB_NAME="pipeline_db" # name of the database
$ export DB_USERNAME="db_admin" # name of the user to be configured in the database
$ export DB_PASSWORD="xxxxxx" # put here the password for the user to be configured in the database 
```

Luodaan varsinainen tietokanta-ajuri seuraavalla komennolla:
```
$ openstack database instance create $DB_INSTANCE_NAME \
--flavor standard.small \
--databases $DB_NAME \
--users $DB_USERNAME:$DB_PASSWORD \
--datastore postgresql \
--is-public \
--size 1
```
Komennon parametrit:

* **flavor** määrittää tietokanta-instanssille varattujen resurssien (CPU, muisti) määrän; katso lisätiedot kohdasta [DBaaS-flavorit ja hinnat](../../dbaas/flavors.md).
* **databases** on lista instanssiin luotavista tietokannoista; tässä yksi tietokanta.
* **users** on lista tunnuksista muodossa *käyttäjä:salasana*; tässä yksi tunnuspari.
* **datastore** määrittää käytettävän tietokantatyypin, esim. postgresql tai mariadb.
* **is-public** tekee instanssista julkisesti saavutettavan.
* **size** on tietokannan koko gigatavuina.

Komennon tuloste on samankaltainen kuin alla:
```
+--------------------------+--------------------------------------+
| Field                    | Value                                |
+--------------------------+--------------------------------------+
| allowed_cidrs            | []                                   |
| created                  | 2025-02-04T13:08:51                  |
| datastore                | postgresql                           |
| datastore_version        | 17.2                                 |
| datastore_version_number | 17.2                                 |
| flavor                   | d4a2cb9c-99da-4e0f-82d7-3313cca2b2c2 |
| id                       | 2f347948-9460-4ac0-a588-32187c8b6ab1 |
| name                     | pipeline_db_instance                 |
| operating_status         |                                      |
| public                   | True                                 |
| region                   | regionOne                            |
| service_status_updated   | 2025-02-04T13:08:51                  |
| status                   | BUILD                                |
| updated                  | 2025-02-04T13:08:51                  |
| volume                   | 1                                    |
+--------------------------+--------------------------------------+
```

## Vaihe 3: virtuaalikoneen luominen cPoutassa { #step-3-creating-virtual-machine-in-cpouta }

Avaamme kolmannen pääteikkunan, johon viittaamme nimellä `terminal_pouta`.
Käytämme `terminal_pouta`-päätettä kaikkiin cPoutaan liittyviin komentoihin.

Samoin kuin Allaksen ja Pukin kanssa, tarvitsemme toimivan komentorivityökalun myös cPoutaan.
Seuraamme ohjetta [cPoutan komentorivityökalun asentaminen ja määrittäminen](../install-client.md), ellei sitä ole vielä tehty.

!!! warning
    Vaikka Pukin ja cPoutan komentorivityökalut ovat monin tavoin samankaltaisia, ne ovat eri työkalut eikä niitä voi käyttää ristiin.
    Esimerkiksi Pukin komentojen ajaminen cPoutaan määritetyssä päätteessä johtaa seuraavaan virheeseen:
    ```
    public endpoint for database service in regionOne region not found
    ```
    Käytä kahta eri päätettä, yksi kummallekin palvelulle, välttääksesi tällaiset ongelmat.
    
    Jos haluat tarkistaa, mille palvelulle nykyinen pääte on määritetty, voit antaa seuraavat komennot:
    ```
    $ printenv | grep OS_AUTH_URL
    OS_AUTH_URL=https://pukki.dbaas.csc.fi:5000/v3 # our terminal is configured for Pukki
    
    $ printenv | grep OS_AUTH_URL
    OS_AUTH_URL=https://pouta.csc.fi:5001/v3 # our terminal is configured for cPouta
    ```

Voimme testata komentorivikäyttöliittymän toiminnan esimerkiksi tarkastelemalla yhden flavorin ominaisuuksia.
Esimerkki komennosta ja sen tulosteesta:
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

Koska nyt toimimme cPoutassa, ensimmäiseksi luomme avainparin, jolla kirjaudumme virtuaalikoneelle sen käynnistyttyä.
Määritellään avainparin nimi ympäristömuuttujaan ja luodaan se:
```
$ export POUTA_KEYPAIR="mykeypair"
$ ssh-keygen -t rsa -b 2048 -f $POUTA_KEYPAIR -N ''
```

Tarkistetaan, että komento loi kaksi tiedostoa työasemamme nykyiseen kansioon.
```
$ ls $POUTA_KEYPAIR*
mykeypair mykeypair.pub
```
Ensimmäinen tiedosto ilman `.pub`-päätettä on yksityinen avain ja `.pub`-päätteinen on julkinen avain.
Yksityisen avaimen ei tule koskaan poistua työasemaltasi, eli sitä ei tarvitse kopioida minnekään muualle.
Sen sijaan julkisen avaimen voi kopioida ja jakaa vapaasti niihin kohteisiin, joihin haluat päästä juuri luodulla avainparilla.
Lähetetään julkinen avain cPoutaan komennolla:
```
$ openstack keypair create $POUTA_KEYPAIR \
--public-key $POUTA_KEYPAIR.pub 
```
Parametri **public-key** määrittää polun julkisen avaimen tiedostoon.

Komennon tuloste on samankaltainen kuin alla:
```
+-------------+-------------------------------------------------+
| Field       | Value                                           |
+-------------+-------------------------------------------------+
| fingerprint | 0e:60:39:df:83:83:fb:18:91:87:67:25:a9:67:27:fd |
| name        | mykeypair                                       |
| user_id     | xxxxxxxx                                        |
+-------------+-------------------------------------------------+
```

Luodaan nyt virtuaalikone, jota käytämme putkessamme.
Määritellään ensin virtuaalikoneen nimi ympäristömuuttujaan:
```
$ export POUTA_INSTANCE_NAME="pipeline_vm"
```

Luodaan virtuaalikone komennolla:
```
$ openstack server create $POUTA_INSTANCE_NAME \
--flavor standard.tiny \
--image Ubuntu-24.04 \
--key-name $POUTA_KEYPAIR
```
Komennon parametrit:

* **flavor** määrittää virtuaalikoneelle varatut resurssit (CPU, muisti); katso lisätiedot kohdasta [Virtuaalikoneiden flavorit ja Billing Unit -hinnat](../vm-flavors-and-billing.md).
* **image** määrittää käyttöjärjestelmäkuvan, josta virtuaalikone rakennetaan; katso vaihtoehdot kohdasta [Perustietoa levykuvista](../images.md).
* **key-name** määrittää virtuaalikoneeseen asennettavan julkisen avaimen.

Komennon tuloste on samankaltainen kuin alla:
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
| adminPass                   | xxxxxxxxxxxx                                         |
| config_drive                |                                                      |
| created                     | 2025-02-04T13:10:43Z                                 |
| flavor                      | standard.tiny (0143b0d1-4788-4d1f-aa04-4473e4a7c2a6) |
| hostId                      |                                                      |
| id                          | ae9f924b-f6c5-488c-b617-36809008e37e                 |
| image                       | Ubuntu-24.04 (bc68d79a-6dcc-446f-a8cd-c8313b885718)  |
| key_name                    | mykeypair                                            |
| name                        | pipeline_vm                                          |
| progress                    | 0                                                    |
| project_id                  | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                     |
| properties                  |                                                      |
| security_groups             | name='default'                                       |
| status                      | BUILD                                                |
| updated                     | 2025-02-04T13:10:43Z                                 |
| user_id                     | timo                                                 |
| volumes_attached            |                                                      |
+-----------------------------+------------------------------------------------------+
```

## Vaihe 4: putken määrittäminen { #step-4-configuring-the-pipeline }

Nyt kun kaikki osat on luotu, määritämme ne toimimaan putkena.
Ensin määritämme virtuaalikoneen sallimaan pääsyn työasemaltamme.
Seuraavaksi varmistamme, että virtuaalikone pystyy käsittelemään Allaksen bucketteja.
Määritämme myös Pukin tietokanta-instanssin hyväksymään liikenteen virtuaalikoneelta.
Lopuksi asennamme ja konfiguroimme virtuaalikoneeseen työkalut, joita putki tarvitsee toimiakseen.

### Työaseman liikenteen salliminen virtuaalikoneelle { #allowing-traffic-from-workstation-to-virtual-machine }

Oletuksena virtuaalikone ei salli saapuvaa liikennettä internetistä luvattomien pääsyyritysten estämiseksi.
Pääsyä virtuaalikoneelle säädellään suojausryhmillä (security groups) ja niiden säännöillä.
Luomme siis uuden suojausryhmän yhdellä säännöllä, joka sallii pääsyn virtuaalikoneelle työasemaltamme.

Palataan `terminal_pouta`-päätteeseen.

Selvitämme ensin työasemamme julkisen IP-osoitteen ja talletamme sen ympäristömuuttujaan:
```
$ export WORKSTATION_IP=$(curl -4 ifconfig.me)

```

Luomme uuden suojausryhmän määrittelemällä ensin sen nimen ympäristömuuttujaan ja ajamalla komennon:
```
$ export POUTA_SEC_GROUP_NAME="pipeline_security_group"
$ openstack security group create $POUTA_SEC_GROUP_NAME
```

Tuloste näyttää tältä:
```
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field           | Value                                                                                                                                                                      |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| created_at      | 2025-02-04T13:12:43Z                                                                                                                                                       |
| description     | pipeline_security_group                                                                                                                                                    |
| id              | a8630776-db3d-408a-ba8e-8c52b5f2a8c9                                                                                                                                       |
| location        | cloud='', project.domain_id='default', project.domain_name=, project.id='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', project.name='project_xxxxxxx', region_name='regionOne', zone= |
| name            | pipeline_security_group                                                                                                                                                    |
| project_id      | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                                                                                                                                           |
| revision_number | 1                                                                                                                                                                          |
| rules           | created_at='2025-02-04T13:12:44Z', direction='egress', ethertype='IPv6', id='8e0cba6e-814d-4e70-92de-61389f9b6ca7', updated_at='2025-02-04T13:12:44Z'                      |
|                 | created_at='2025-02-04T13:12:43Z', direction='egress', ethertype='IPv4', id='cdf6527c-ca5a-4247-8e47-40213b601ee0', updated_at='2025-02-04T13:12:43Z'                      |
| tags            | []                                                                                                                                                                         |
| updated_at      | 2025-02-04T13:12:43Z                                                                                                                                                       |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

Lisätään sääntö, joka sallii pääsyn:
```
$ openstack security group rule create $POUTA_SEC_GROUP_NAME \
--remote-ip $WORKSTATION_IP/32 \
--dst-port 22 \
--protocol tcp
```
Komennon parametrit:

* **remote-ip** määrittää IP-osoitteet, joihin sääntö kohdistuu. Nämä ovat liikenteen lähdeosoitteita.
* **dst-port** määrittää kohteen portin, johon sääntö kohdistuu. Tämä on liikenteen kohdeportti.
* **protocol** määrittää protokollan. Tässä säännössä huomioidaan vain TCP-liikenne.

Tuloste on samankaltainen kuin alla:
```
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field             | Value                                                                                                                                                                      |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| created_at        | 2025-02-04T13:13:04Z                                                                                                                                                       |
| description       |                                                                                                                                                                            |
| direction         | ingress                                                                                                                                                                    |
| ether_type        | IPv4                                                                                                                                                                       |
| id                | 29ebe032-f09c-4cb5-9e49-bc75e6d1880c                                                                                                                                       |
| location          | cloud='', project.domain_id='default', project.domain_name=, project.id='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', project.name='project_xxxxxxx', region_name='regionOne', zone= |
| name              | None                                                                                                                                                                       |
| port_range_max    | 22                                                                                                                                                                         |
| port_range_min    | 22                                                                                                                                                                         |
| project_id        | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                                                                                                                                           |
| protocol          | tcp                                                                                                                                                                        |
| remote_group_id   | None                                                                                                                                                                       |
| remote_ip_prefix  | xxx.xxx.xxx.xxx/32                                                                                                                                                         |
| revision_number   | 0                                                                                                                                                                          |
| security_group_id | a8630776-db3d-408a-ba8e-8c52b5f2a8c9                                                                                                                                       |
| tags              | []                                                                                                                                                                         |
| updated_at        | 2025-02-04T13:13:04Z                                                                                                                                                       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

Lisätään suojausryhmä aiemmin luotuun virtuaalikoneeseen, jotta uusi sääntö vaikuttaa sen liikenteeseen.
```
$ openstack server add security group $POUTA_INSTANCE_NAME $POUTA_SEC_GROUP_NAME
```
Onnistuneessa tapauksessa komento ei näytä tulostetta.

### Yhteyden muodostaminen virtuaalikoneeseen { #connecting-to-the-virtual-machine }

Virtuaalikone on nyt määritetty sallimaan liikenne työasemaltamme, mutta siihen ei vielä pääse käsiksi.
Virtuaalikoneelle annetaan käynnistyksessä yksityinen IP-osoite, mutta sille ei automaattisesti tule julkista IP-osoitetta, jota tarvitaan internetin yli yhdistämiseen.

Palataan `terminal_pouta`-päätteeseen.
Hankitaan uusi osoite komennolla:
```
$ openstack floating ip create public
```

Tuloste on samankaltainen kuin alla:
```
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field               | Value                                                                                                                                                                                                |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| created_at          | 2025-02-04T13:13:38Z                                                                                                                                                                                 |
| description         |                                                                                                                                                                                                      |
| dns_domain          | None                                                                                                                                                                                                 |
| dns_name            | None                                                                                                                                                                                                 |
| fixed_ip_address    | None                                                                                                                                                                                                 |
| floating_ip_address | xxx.xxx.xxx.xxx                                                                                                                                                                                      |
| floating_network_id | 26f9344a-2e81-4ef5-a018-7d20cff891ee                                                                                                                                                                 |
| id                  | 1a38ae4f-1354-4958-b2be-72502b53c492                                                                                                                                                                 |
| location            | Munch({'cloud': '', 'region_name': 'regionOne', 'zone': None, 'project': Munch({'id': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'name': 'project_xxxxxxx', 'domain_id': 'default', 'domain_name': None})}) |
| name                | xxx.xxx.xxx.xxx                                                                                                                                                                                      |
| port_details        | None                                                                                                                                                                                                 |
| port_id             | None                                                                                                                                                                                                 |
| project_id          | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                                                                                                                                                                     |
| qos_policy_id       | None                                                                                                                                                                                                 |
| revision_number     | 0                                                                                                                                                                                                    |
| router_id           | None                                                                                                                                                                                                 |
| status              | DOWN                                                                                                                                                                                                 |
| subnet_id           | None                                                                                                                                                                                                 |
| tags                | []                                                                                                                                                                                                   |
| updated_at          | 2025-02-04T13:13:38Z                                                                                                                                                                                 |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Kirjataan erityisesti talteen `floating_ip_address`-kentän arvo ympäristömuuttujaan:
```
$ export POUTA_FLOATING_IP="xxx.xxx.xxx.xxx" # put here the value returned for floating_ip_address
```

Liitetään saatu osoite virtuaalikoneeseemme:
```
$ openstack server add floating ip $POUTA_INSTANCE_NAME $POUTA_FLOATING_IP
```
Onnistuneessa tapauksessa komento ei näytä tulostetta.

Kaikki on nyt valmista.
Voimme testata yhteyttä virtuaalikoneeseen komennolla:
```
$ ssh -i $POUTA_KEYPAIR ubuntu@$POUTA_FLOATING_IP
```

Todennäköisesti meiltä kysytään seuraavaa:
```
The authenticity of host 'xxx.xxx.xxx.xxx (xxx.xxx.xxx.xxx)' can't be established.
ED25519 key fingerprint is SHA256:waKe82wIU0HYSGpRFCBOx0n6GOvH108nkJ+koosOF80.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Voimme vastata turvallisesti `yes` ja painaa Enter, minkä jälkeen päädymme virtuaalikoneelle:
```
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'xxx.xxx.xxx.xxx' (ED25519) to the list of known hosts.
Welcome to Ubuntu 24.04.1 LTS (GNU/Linux 6.8.0-51-generic x86_64)

...

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@pipeline-vm:~$
```

Jätämme `terminal_pouta`-päätteen hetkeksi ja palaamme siihen, kun on aika asentaa ja määrittää työkalut virtuaalikoneessa.

### Liikenteen salliminen virtuaalikoneelta tietokantaan { #allowing-traffic-from-virtual-machine-to-database }

Oletuksena Pukin tietokanta-instanssi ei hyväksy saapuvaa liikennettä.
Haluamme määrittää sen niin, että se hyväksyy liikenteen cPoutan virtuaalikoneeltamme.

Siirrytään `terminal_pukki`-päätteeseen.
Ennen kuin jatkamme tietokanta-instanssin parissa, huomaa että yhdessä päätteessä määritetyt ympäristömuuttujat eivät siirry automaattisesti toiseen.
Siksi meidän on määritettävä cPoutan virtuaalikoneelle annettu floating IP myös tässä päätteessä ympäristömuuttujaan.
```
$ export POUTA_FLOATING_IP="xxx.xxx.xxx.xxx" # put here the same value assigned to the same variable in terminal_pouta
```

Ajetaan sitten seuraava komento:
```
$ openstack database instance update $DB_INSTANCE_NAME \
--allowed-cidr $POUTA_FLOATING_IP/32
```
Parametri **allowed-cidr** määrittää IP-osoitejoukon, josta liikenne tietokanta-instanssiin sallitaan.

Onnistuneessa tapauksessa komento ei näytä tulostetta.
Voimme kuitenkin tarkistaa, että muutos meni perille, katsomalla instanssin tiedot:
```
$ openstack database instance show $DB_INSTANCE_NAME
+--------------------------+-----------------------------------------------------------------------------------------------------------+
| Field                    | Value                                                                                                     |
+--------------------------+-----------------------------------------------------------------------------------------------------------+
| addresses                | [{'address': '192.168.215.98', 'type': 'private', 'network': 'a89ef792-74ec-434f-8e20-7d33b5b6d633'},     |
|                          | {'address': 'xxx.xxx.xxx.xxx', 'type': 'public'}]                                                         |
| allowed_cidrs            | ['xxx.xxx.xxx.xxx/32']                                                                                    |
| created                  | 2025-02-04T13:08:51                                                                                       |
| datastore                | postgresql                                                                                                |
| datastore_version        | 17.2                                                                                                      |
| datastore_version_number | 17.2                                                                                                      |
| flavor                   | d4a2cb9c-99da-4e0f-82d7-3313cca2b2c2                                                                      |
| id                       | 2f347948-9460-4ac0-a588-32187c8b6ab1                                                                      |
| ip                       | 192.168.215.98, xxx.xxx.xxx.xxx                                                                           |
| name                     | pipeline_db_instance                                                                                      |
| operating_status         | HEALTHY                                                                                                   |
| public                   | False                                                                                                     |
| region                   | regionOne                                                                                                 |
| service_status_updated   | 2025-02-04T13:16:10                                                                                       |
| status                   | ACTIVE                                                                                                    |
| updated                  | 2025-02-04T13:16:52                                                                                       |
| volume                   | 1                                                                                                         |
| volume_used              | 0.08                                                                                                      |
+--------------------------+-----------------------------------------------------------------------------------------------------------+
```
Näemme, että virtuaalikoneemme floating IP on nyt listattuna `allowed_cidrs`-kentässä.

Edellisen komennon tulosteesta poimimme myös tietokanta-instanssin julkisen IP-osoitteen, jota tarvitsemme myöhemmin.
`addresses`-rivi sisältää kaksi osaa: yksityisen osoitteen (private) ja julkisen osoitteen (public).
Palataan `terminal_pouta`-päätteeseen, jossa olemme edelleen kirjautuneena cPoutan virtuaalikoneelle, ja tallennetaan tietokannan julkinen osoite ympäristömuuttujaan myöhempää käyttöä varten.
```
$ export DB_PUBLIC_IP="xxx.xxx.xxx.xxx" # put here the public ip address of the database instance in Pukki
```

### Pääsyn määrittäminen virtuaalikoneelta Allakseen { #configuring-access-from-virtual-machine-to-allas }

Samoin kuin työasemalla, myös virtuaalikone on määritettävä siten, että se pääsee käsiksi Allaksen bucketteihin.

`terminal_pouta`-päätteessä seuraamme virtuaalikoneessa ohjetta [s3cmd:n asentaminen ja määrittäminen](../../../data/Allas/using_allas/s3_client.md#getting-started-with-s3cmd).
Kun s3cmd on konfiguroitu, testaamme toiminnan listaamalla Allaksen bucketit:
```
$ s3cmd ls
2025-01-16 14:59  s3://input_bucket
2025-01-16 14:59  s3://output_bucket
```
Huomaamme, että näemme kaksi aiemmin luomaamme buckettia.
Olemme siis varmistaneet, että virtuaalikone pääsee käsiksi Allaksen bucketteihin.

### Pääsyn määrittäminen virtuaalikoneelta tietokantaan { #configuring-access-from-virtual-machine-to-database }

Tässä vaiheessa virtuaalikoneelta lähtevä liikenne pääsee Pukin tietokantaan.
Virtuaalikoneella ei kuitenkaan vielä ole tietoa siitä, missä tietokanta sijaitsee (julkinen IP-osoite) tai mitä tunnuksia käytetään.
Määritetään siis yhteys tietokantaan virtuaalikoneelta.

Pysytään `terminal_pouta`-päätteessä.
Asennetaan ensin työkalu, jolla voimme keskustella tietokannan kanssa:
```
$ sudo apt update ; sudo apt install postgresql-client
```

Määritetään sitten kaikki tarvittavat ympäristömuuttujat tietokantaan yhdistämistä varten:
```
$ export DB_NAME="pipeline_db" # name of the database
$ export DB_USERNAME="db_admin" # name of the user configured for the database
$ export DB_PASSWORD="xxxxxx" # put here the password of the user configured for the database
```

Määritellään myös PostgreSQL:n salasanatiedosto, jonka avulla komentorivityökalulla on helppo yhdistää tietokantaan:
```
$ echo "$DB_PUBLIC_IP:5432:$DB_NAME:$DB_USERNAME:$DB_PASSWORD" >> ~/.pgpass
$ chmod 0600 ~/.pgpass
```
Lisätietoja PostgreSQL:n salasanatiedostosta löytyy sen [viitesivulta](https://www.postgresql.org/docs/current/libpq-pgpass.html).

Testataan nyt yhteyttä tietokantaan.
Aja `terminal_pouta`-päätteessä:
```
$ psql -h "$DB_PUBLIC_IP" -d "$DB_NAME" -U "$DB_USERNAME"
```
Saat seuraavan kehotteen, mikä kertoo, että yhteys tietokantaan onnistui:
```
psql (16.6 (Ubuntu 16.6-0ubuntu0.24.04.1), server 17.2 (Debian 17.2-1.pgdg110+1))
WARNING: psql major version 16, server major version 17.
         Some psql features might not work.
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
Type "help" for help.

pipeline_db=>
```
Palaa virtuaalikoneen komentoriville kirjoittamalla `exit` ja painamalla Enter.

Kun yhteys tietokantaan toimii, valmistellaan se vastaanottamaan käsittelyä koskevat tiedot.
Luodaan taulu, johon tallennetaan kuvien käsittelyä koskevat tiedot:
```
$ psql \
-h "$DB_PUBLIC_IP" \
-d "$DB_NAME" \
-U "$DB_USERNAME" \
-c "CREATE TABLE IF NOT EXISTS log_records (timestamp varchar(25) primary key, negated_picture_name text, negated_picture_hash text)"
```
Komennon parametrit:

* **h** on isäntänimi, eli tietokannan IP-osoite.
* **d** on tietokannan nimi.
* **U** on käyttäjätunnus, jolla tunnistaudutaan tietokantaan.
* **c** on tietokannassa suoritettava komento. Komento kirjoitetaan tietokannan syntaksilla.

Onnistuneessa tapauksessa terminaali vastaa `CREATE TABLE`.
Tietokanta on nyt konfiguroitu putkeamme varten.

### Kuvien muunnosskriptin asentaminen { #installing-picture-transforming-script }

Konfiguroinnin viimeinen osa on skriptin asentaminen. Skripti huolehtii Allaksen ja Pukin kanssa kommunikoinnista sekä kuvan muuntamisesta.
Asennetaan ensin kuvien muunnostyökalu.
Aja `terminal_pouta`-päätteessä:
```
$ sudo apt install imagemagick
```

Kun työkalu on asennettu riippuvuuksineen, suoritetaan:
```
$ nano pipeline_script.sh
```
Näet vilkkuvan kohdistimen ikkunan vasemmassa yläkulmassa, mikä kertoo, että voit nyt kirjoittaa uuteen tiedostoon `pipeline_script.sh`.
Kopioi ja liitä alla oleva sisältö.
Muista vaihtaa skriptin alussa määritetyt ympäristömuuttujat omaan ympäristöösi sopiviksi.
```
#!/bin/bash

### NB! Change the value of these environment variables to match your setup
export INPUT_BUCKET="input_bucket"
export OUTPUT_BUCKET="output_bucket"
export DB_PUBLIC_IP="xxx.xxx.xxx.xxx"
export DB_NAME="pipeline_db"
export DB_USERNAME="db_admin"
###



export NEGATED_PREFIX="negated_"

(
# perform the task if the lock is free, otherwise exit
flock -n 200 || exit 1
# iterate over the pictures in the bucket
for PICTURE_URL in $(s3cmd ls s3://$INPUT_BUCKET | awk '{ print $4 }')
do
        # get the current timestamp
        TIMESTAMP=$(date +%FT%T)
        # get the picture
        PICTURE_NAME=$(echo "$PICTURE_URL" | awk -F '/' '{ print $NF }')
        s3cmd get "$PICTURE_URL" "$PICTURE_NAME"
        # compute the negated
        NEGATED_PICTURE_NAME="$NEGATED_PREFIX$PICTURE_NAME"
        convert -negate "$PICTURE_NAME" "$NEGATED_PICTURE_NAME"
        # compute hash of the result
        NEGATED_PICTURE_HASH=$(sha256sum "$NEGATED_PICTURE_NAME" | awk '{ print $1 }')
        # log to the db that this was done
        psql -h "$DB_PUBLIC_IP" -d "$DB_NAME" -U "$DB_USERNAME" -c "INSERT INTO log_records (timestamp, negated_picture_name, negated_picture_hash) VALUES ('$TIMESTAMP', '$NEGATED_PICTURE_NAME', '$NEGATED_PICTURE_HASH')"
        # push the negated picture to the output bucket
        s3cmd put "$NEGATED_PICTURE_NAME" s3://$OUTPUT_BUCKET
        # delete the local copies of the pictures
        rm "$PICTURE_NAME" "$NEGATED_PICTURE_NAME"
        # delete the picture from the input bucket
        s3cmd del "$PICTURE_URL"
        # sleep 1 sec
        sleep 1
done
) 200>/var/lock/pipeline_script_lock
```
Kun olet valmis, paina näppäinyhdistelmää `CTRL + X`.
Terminaali kysyy, tallennetaanko muutokset; vastaa painamalla `y`.
Saat vielä mahdollisuuden muuttaa tiedoston nimen.
Nykyinen nimi kelpaa, joten paina Enter ja palaat takaisin terminaalinäkymään.

Skriptissä on nyt putken logiikka, mutta se ei vielä käynnisty automaattisesti.
Aja `terminal_pouta`-päätteessä seuraavat komennot:
```
$ chmod +x /home/ubuntu/pipeline_script.sh
$ crontab -l > crontab_list
$ echo "* * * * * /home/ubuntu/pipeline_script.sh" >> crontab_list
$ crontab crontab_list
```

Nyt skripti on ajastettu ajettavaksi minuutin välein.
Olemme valmiita testaamaan putken toimintaa.

## Vaihe 5: putken testaaminen { #step-5-testing-the-pipeline }

Valitse haluamasi kuva ja kopioi se työasemasi kotihakemistoon.
Esimerkkinä tässä kuvamme polussa `~/cat1.jpg`:

![picture-cat](../../img/cat1.jpg)

Lähetetään kuva putken läpi.
`terminal_allas`-päätteessä siirry ensin kotihakemistoon ja lataa kuva Allakseen:
```
$ cd ~
$ s3cmd put cat1.jpg s3://$INPUT_BUCKET
upload: 'cat1.jpg' -> 's3://input_bucket/cat1.jpg'  [1 of 1]
 133275 of 133275   100% in    0s     2.47 MB/s  done
```

Odotetaan noin minuutti, tarkistetaan bucketin sisältö ja huomataan, että se on tyhjä.
```
$ s3cmd ls s3://$INPUT_BUCKET
$
```
Putki on siis ottanut kuvan bucketista ja käsitellyt sen.

Tarkistetaan, löytyykö tietokannasta merkintä kuvan muunnoksesta.
Aja `terminal_pouta`-päätteessä:
```
$ psql \
-h "$DB_PUBLIC_IP" \
-d "$DB_NAME" \
-U "$DB_USERNAME" \
-c "select * from log_records where negated_picture_name like '%cat1%'"
```
Saat samankaltaisen tulosteen kuin alla:
```
      timestamp      | negated_picture_name |                        negated_picture_hash                        
---------------------+--------------------+------------------------------------------------------------------
 2025-02-04T12:01:01 | negated_cat1.jpg   | 50cc363c1528371cf9526d1fddead5f37f3004f11e9f24b72ea210db58dee095
(1 row)
```
Tuloste kertoo, että putki on käsitellyt alkuperäisen `cat1.jpg`-kuvan ja tuottanut tulokseksi `negated_cat1.jpg`-kuvan.

Katsotaan muunnettua kuvaa.
`terminal_allas`-päätteessä varmistetaan ensin, että kuva löytyy toisesta bucketista.
Ladataan se sitten kotihakemistoon:
```
$ s3cmd ls s3://$OUTPUT_BUCKET
2025-02-04 12:01       140798  s3://output_bucket/negated_cat1.jpg
$ s3cmd get s3://$OUTPUT_BUCKET/negated_cat1.jpg .
download: 's3://output_bucket/negated_cat1.jpg' -> './negated_cat1.jpg'  [1 of 1]
 140798 of 140798   100% in    0s     2.12 MB/s  done
```

Voimme vihdoin ihailla aherruksemme tulosta!

![picture-negated-cat](../../img/negated_cat1.jpg)

## Yhteenveto { #conclusion }

Rakensimme automatisoidun työnkulun kuvien muuntamiseksi käyttäen kolmea eri pilvipalvelua.
Tässä ohjeessa työnkulku on vain yksinkertainen menettely kuvan kääntämiseksi invertoituun versioon, mutta sen päälle voi rakentaa konkreettisempiakin käyttötapauksia.
Muutama keskeinen oppi:

* Kun käytät useita pilvipalveluja yhtä aikaa, voi olla hyödyllistä käyttää yhtä pääteikkunaa per palvelu. Vaikka se ei ole välttämätöntä, se helpottaa eri palveluiden tunnusten järjestyksessä pitämistä, esim. jos käytät Allasta projektista `X` ja cPoutaa projektista `Y`.
* Oletuksena cPoutassa ja Pukissa ajettavat instanssit eivät hyväksy saapuvaa liikennettä. Pääsy tällaisiin instansseihin on aina määriteltävä erikseen suojausryhmillä ja sallitulla CIDR-listauksella.