# Kuvaputken asettaminen

## Tavoitteet {#objectives}

* Tutustua siihen, miten useita pilvipalveluja voidaan käyttää yhdessä.
* Tutustua siihen, miten pilvipalveluja voidaan käyttää niiden komentorajapintojen avulla.

Opetus keskittyy seuraaviin palveluihin:

* [Allas](../../../data/Allas/introduction.md), meidän objektitallennuspalvelumme
* [cPouta](../index.md), meidän julkinen pilvipalvelumme
* [Pukki](../../dbaas/what-is-dbaas.md), meidän tilauspohjainen tietokantapalvelumme

## Johdanto {#introduction}

Haluamme asettaa yksinkertaisen putken, joka muuttaa sille annetut kuvat.

![kuvasputki-kaavio](../../img/picture-pipeline-diagram.png)

Ensiksi lataamme kuvat työasemaltamme Allasilla olevaan säiliöön.
cPoutassa oleva virtuaalikone ottaa kuvat säiliöstä ja lataa ne paikallisesti.
Virtuaalikone muuntaa kuvat ja kirjaa suoritetun toiminnon Pukissa isännöityyn tietokantaan.
Lopulta virtuaalikone lataa muutetut kuvat toiseen säiliöön Allasissa.
Voimme sitten ladata muutetut kuvat työasemallemme säiliöstä.

Tämän opetusmateriaalin tarkoituksessa muokattu kuva vastaa yksinkertaisesti syötekuvaa, jonka värit on käännetty, toisinaan kutsutaan "käännetyksi".

## Vaihe 1: säiliöiden luominen Allasissa {#step-1-creating-buckets-in-allas}

Avaamme uuden pääteikkunan, johon viittaamme käyttämällä nimeä `terminal_allas`.
Käytämme `terminal_allas`-päätettä kaikille Allasiin liittyville komennoille.

Jotta voimme luoda säiliöitä Allasissa, meillä on oltava toimiva komentorajapinta sitä varten.
Jos emme ole aiemmin asentaneet tällaista rajapintaa työasemallemme, noudatamme [s3cmd:n asentamista ja konfigurointia koskevia ohjeita](../../../data/Allas/using_allas/s3_client.md#getting-started-with-s3cmd).

Voimme testata komentorajapinnan oikeaa toimintaa yksinkertaisesti listaamalla kaikki projektissamme tällä hetkellä olevat säiliöt.
Esimerkki komennosta ja sen odotetusta tulosteesta:
```
$ s3cmd ls
2021-07-14 15:14  s3://bucket1
2020-01-14 17:40  s3://bucket2
...
```
Huomaa, että lista voi olla myös tyhjä, jos emme ole aiemmin luoneet säiliötä projektissamme.

Nyt luomme syöttö- ja tulossaavad putkillemme säiliöt.
Ensiksi määrittelemme säiliöiden nimet ympäristömuuttujiin:
```
$ export INPUT_BUCKET="input_bucket"
$ export OUTPUT_BUCKET="output_bucket"
```

Käytämme sitten seuraavia komentoja säiliöiden luomiseen:
```
$ s3cmd mb s3://$INPUT_BUCKET
Bucket 's3://input_bucket/' created
$ s3cmd mb s3://$OUTPUT_BUCKET
Bucket 's3://output_bucket/' created
```

!!! huom
    Säiliöiden nimet täytyy olla uniikkeja. 
    Jos toinen käyttäjä on jo valinnut saman nimen, säiliön luomiskomento epäonnistuu:
    ```
    $ s3cmd mb s3://$INPUT_BUCKET
    ERROR: Bucket 'input_bucket' already exists
    ERROR: S3 error: 409 (BucketAlreadyExists)
    ```
    Tässä tapauksessa voimme yksinkertaisesti yrittää komentoa eri nimellä.

## Vaihe 2: tietokannan luominen Pukkiin {#step-2-creating-a-database-in-pukki}

Avaamme toisen pääteikkunan, johon viittaamme käyttämällä nimeä `terminal_pukki`.
Käytämme `terminal_pukki`-päätettä kaikille Pukkiin liittyville komennoille.

Toimivan komentorajapinnan olemassaolo Pukkille on edellytys oppimateriaalin jatkamiselle.
Jos emme ole sitä aikaisemmin asentaneet, noudatamme [Pukki-komentorajapinnan asentamista ja konfigurointia koskevia ohjeita](../../dbaas/cli.md#getting-started).

Voimme testata komentorajapinnan oikeaa toimintaa yksinkertaisesti listaamalla käytettävissä olevat tietokantatyypit.
Esimerkki komennosta ja sen odotetusta tulosteesta:
```
$ openstack datastore list
+--------------------------------------+------------+
| ID                                   | Name       |
+--------------------------------------+------------+
| 71920375-6967-466e-b955-8ee8629312b7 | postgresql |
| 1a8efda2-7bb7-4c52-9eab-e251fd18323c | mariadb    |
+--------------------------------------+------------+
```

Nyt luomme tietokannan, jota käytämme putkiston toimintojen kirjaamiseen.
Ensin määrittelemme muutamia ympäristömuuttujia, joita käytämme myöhemmin:
```
$ export DB_INSTANCE_NAME="pipeline_db_instance" # tietokanta-instanssin nimi Pukissa
$ export DB_NAME="pipeline_db" # tietokannan nimi
$ export DB_USERNAME="db_admin" # tietokantaan konfiguroitavan käyttäjän nimi
$ export DB_PASSWORD="xxxxxx" # laita tähän tietokantaan konfiguroitavan käyttäjän salasana
```

Luomme sitten varsinaisen tietokanta-instanssin antamalla seuraavan komennon:
```
$ openstack database instance create $DB_INSTANCE_NAME \
--flavor standard.small \
--databases $DB_NAME \
--users $DB_USERNAME:$DB_PASSWORD \
--datastore postgresql \
--is-public \
--size 1
```
Komennon parametrit ovat seuraavat:

* **flavor** määrittää tietokanta-instanssille osoitettujen resurssien (CPU, muisti) määrän, lisätietoja katso [DBaaS-makrot ja hinnat](../../dbaas/flavors.md).
* **databases** on lista tietokanta-instanssiin luotavista tietokanoista, tässä tapauksessa tilanne yhden tietokannan kanssa.
* **users** on lista tunnisteista muodossa *käyttäjänimi:salasana*, tietokantojen käyttäjien konfigurointia varten, tässä tapauksessa tilanne yhden credentials-parin kanssa.
* **datastore** määrittää käytettävän tietokannan tyypin, esim., postgresql tai mariadb.
* **is-public** määrittää, että tietokanta-instanssin tulisi olla julkisesti saavutettavissa.
* **size** on tietokannan koko gigatavuina.

Komennon tuloste pitäisi olla seuraavanlainen:
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

## Vaihe 3: virtuaalikoneen luominen cPoutaan {#step-3-creating-virtual-machine-in-cpouta}

Avaamme kolmannen pääteikkunan, johon viittaamme käyttämällä nimeä `terminal_pouta`.
Käytämme `terminal_pouta`-päätettä kaikille cPoutaan liittyville komennoille.

Samoin kuin Allasin ja Pukin osalta, oppimateriaalin jatkaminen vaatii myös toimivan komentorajapinnan olemassaolon cPoutaan.
Seuraamme [cPouta-komentorajapinnan asentamista ja konfigurointia koskevia ohjeita](../install-client.md), jos emme ole jo tehneet sitä.

!!! huom
    Vaikkakin Pukki ja cPouta ovat monilla tavoilla samanlaisia, niiden komentorajapinnat ovat erilaisia, eikä niitä saa käyttää keskenään.
    Esimerkiksi, Pukki-komentojen suorittaminen cPoutan konfiguroidussa päätelaitteessa johtaa seuraavaan virheeseen:
    ```
    julkista päätepistettä tietokantapalvelulle regionOne-alueella ei löydy
    ```
    Jotta vältetään tämän kaltaisia ongelmia, tulee käyttää kahta eri päätettä niiden kanssa työskentelyyn.
    
    Jos haluat tarkistaa, mille palvelulle nykyinen päätelaitteesi on konfiguroitu, voit kirjoittaa seuraavan komennon:
    ```
    $ printenv | grep OS_AUTH_URL
    OS_AUTH_URL=https://pukki.dbaas.csc.fi:5000/v3 # saatatelaitteemme on konfiguroitu Pukkille
    
    $ printenv | grep OS_AUTH_URL
    OS_AUTH_URL=https://pouta.csc.fi:5001/v3 # päätelaitteemme on konfiguroitu cPoutalle
    ```

Voit testata komentorajapinnan oikeaa toimintaa näyttämällä esimerkiksi jonkin muodon ominaisuuksia.
Esimerkki komennosta ja sen odotetusta tulosteesta:
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

Nyt kun työskentelemme cPoutan kanssa, ensimmäisenä askeleena luomme avainparin, jota käytämme pääsemään virtuaalikoneelle, kun se on käynnissä.
Luodaksemme uuden avainparin, määrittelemme ensin sen nimen ympäristömuuttujan avulla ja suorita sitten erikoiskomento:
```
$ export POUTA_KEYPAIR="mykeypair"
$ ssh-keygen -t rsa -b 2048 -f $POUTA_KEYPAIR -N ''
```

Varmistamme, että komento on luonut kaksi tiedostoa nykyiseen kansioon työasemaltamme.
```
$ ls $POUTA_KEYPAIR*
mykeypair mykeypair.pub
```
Ensimmäinen tiedosto, ilman `.pub`-päätettä, vastaa yksityistä avainta, kun taas `.pub` päätteinen tiedosto vastaa julkista avainta.
Yksityinen avain ei saisi koskaan poistua työasemaltasi, eli sitä ei pitäisi kopioida minnekään muualle.
Sen sijaan julkinen avain voidaan vapaasti kopioida ja jakaa paikkoihin, joissa haluat käyttää juuri luotua avainparia.
Tätä varten lataamme julkisen avaimen cPoutaan antamalla seuraavan komennon:
```
$ openstack keypair create $POUTA_KEYPAIR \
--public-key $POUTA_KEYPAIR.pub 
```
Komennon **public-key**-parametri määrittää polun julkisen avaindin tiedostoon.

Komennon tuloste on seuraavanlainen:
```
+-------------+-------------------------------------------------+
| Field       | Value                                           |
+-------------+-------------------------------------------------+
| fingerprint | 0e:60:39:df:83:83:fb:18:91:87:67:25:a9:67:27:fd |
| name        | mykeypair                                       |
| user_id     | xxxxxxxx                                        |
+-------------+-------------------------------------------------+
```

Luomme nyt virtuaalikoneen, jota käytämme putkemme runkoon.
Ensin määrittelemme virtuaalikoneen nimen ympäristömuuttujana:
```
$ export POUTA_INSTANCE_NAME="pipeline_vm"
```

Komento, jolla luomme virtuaalikoneen, on seuraava:
```
$ openstack server create $POUTA_INSTANCE_NAME \
--flavor standard.tiny \
--image Ubuntu-24.04 \
--key-name $POUTA_KEYPAIR
```
Komennon parametrit ovat seuraavat:

* **flavor** määrittää virtuaalikoneelle osoitettujen resurssien (CPU, muisti) määrän, lisätietoja katso [Virtuaalikoneen muodot ja laskutusyksikön hinnat](../vm-flavors-and-billing.md).
* **image** määrittää käyttöjärjestelmän kuvauksen, jota käytetään virtuaalikoneen rakentamiseen, katso [Perustiedot kuvista](../images.md) vaihtoehtoisten kuvien lista.
* **key-name** määrittää virtuaalikoneeseen konfiguroitavan julkisen avaimen.

Komennon tuloste on seuraavanlainen:
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

## Vaihe 4: putken konfigurointi {#step-4-configuring-the-pipeline}

Nyt kun olemme rakentaneet kaikki komponentit, konfiguroimme ne toimimaan putkena.
Ensiksi konfiguroimme virtuaalikoneen siten, että voimme käyttää sitä työasemaltamme.
Sitten varmistamme, että virtuaalikone voi toimia Allasinsa sisältämien säiliöiden kanssa.
Määrittelemme myös tietokanta-instanssimme Pukissa hyväksymään liikenteen virtuaalikoneelta.
Lopulta asennamme ja konfiguroimme työkalut, jotka mahdollistavat putken toiminnan virtuaalikoneessa.

### Liikenteen salliminen työasemalta virtuaalikoneelle {#allowing-traffic-from-workstation-to-virtual-machine}

Oletuksena virtuaalikone ei salli saapuvaa liikennettä Internetistä estääkseen luvattomat pääsyyritykset.
Pääsy virtuaalikoneelle säädellään _turvallisuusryhmien_ ja niiden sisältämien sääntöjen avulla.
Näin ollen luomme uuden turvallisuusryhmän yhdellä säännöllä, joka sallii pääsyn virtuaalikoneelle työasemaltamme.

Palaamme `terminal_pouta`-laitteeseen.

Ensiksi selvitämme, mikä on työasemamme julkisesti käytetty ip-osoite ja tallennamme sen ympäristömuuttujaan antamalla seuraavan komennon:
```
$ export WORKSTATION_IP=$(curl -4 ifconfig.me)

```

Luomme uuden turvallisuusryhmän määrittelemällä ensin sen nimen ympäristömuuttujaan ja antamalla sitten erikoiskomennon:
```
$ export POUTA_SEC_GROUP_NAME="pipeline_security_group"
$ openstack security group create $POUTA_SEC_GROUP_NAME
```

Tuloste näyttää seuraavanlaiselta:
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

Lisäämme säännön, joka sallii pääsyn suorittamalla seuraavan komennon:
```
$ openstack security group rule create $POUTA_SEC_GROUP_NAME \
--remote-ip $WORKSTATION_IP/32 \
--dst-port 22 \
--protocol tcp
```
Komennon parametrit ovat seuraavat:

* **remote-ip** määrittää ip-osoitteiden joukon, jolle sääntö on määritelty. Etäpäätepisteet vastaavat liikenteen lähteitä.
* **dst-port** määrittää, mille kohteen portille sääntö on määritelty. Kohdeportti vastaa liikenteen kohdetta.
* **protocol** määrittää protokollan, johon sääntö on määritelty. Tässä tapauksessa sääntö huomioi vain TCP-liikenteen.

Tuloste on seuraavanlainen:
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

Nyt sovellamme turvallisuusryhmän aiemmin luotuun virtuaalikoneeseen niin, että tämä juuri luotu sääntö koskee sen liikennettä.
```
$ openstack server add security group $POUTA_INSTANCE_NAME $POUTA_SEC_GROUP_NAME
```
Jos komento onnistuu, se ei näytä tulostetta.

### Yhteyden muodostaminen virtuaalikoneelle {#connecting-to-the-virtual-machine}

Virtuaalikone on nyt konfiguroitu sallimaan liikenteen työasemaltamme, mutta se ei ole vielä saavutettavissa.
Virtuaalikoneelle annetaan yksityinen IP-osoite käynnistyksen yhteydessä, mutta sille ei määritetä automaattisesti julkista IP:tä, joka vaaditaan yhteyden muodostamiseen virtuaalikoneeseen Internetistä.

Palaamme `terminal_pouta`-laitteeseen.
Hankimme uuden osoitteen antamalla seuraavan komennon:
```
$ openstack floating ip create public
```

Tuloste on seuraavanlainen:
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
Erityisesti merkitsemme ylös kentän `floating_ip_address` arvon ympäristömuuttujaan:
```
$ export POUTA_FLOATING_IP="xxx.xxx.xxx.xxx" # laita tähän kelluvan IP-osoitteen arvo
```

Yhdistämme nyt saadun osoitteen virtuaalikoneeseemme antamalla seuraavan komennon:
```
$ openstack server add floating ip $POUTA_INSTANCE_NAME $POUTA_FLOATING_IP
```
Jos komento onnistuu, se ei näytä tulostetta.

Kaikki on nyt valmista.
Voimme testata yhteyden muodostamista virtuaalikoneeseemme antamalla seuraavan komennon:
```
$ ssh -i $POUTA_KEYPAIR ubuntu@$POUTA_FLOATING_IP
```

Mahdollisesti meille esitetään seuraava kysymys:
```
Virheellistä laitetta 'xxx.xxx.xxx.xxx (xxx.xxx.xxx.xxx)' ei voi todentaa. 
ED25519 avain on sormenjälki SHA256:waKe82wIU0HYSGpRFCBOx0n6GOvH108nkJ+koosOF80.
Tätä avainta ei tunneta millään muilla nimillä
Haluatko varmasti jatkaa yhteyden muodostamista (yes/no/[fingerprint])?
```

Voimme turvallisesti vastata `yes` ja painaa Enter-näppäintä, mikä lopulta johtaa meidät virtuaalikoneelle:
```
Haluatko varmasti jatkaa yhteyden muodostamista (yes/no/[fingerprint])? yes
Varoitus: Lisätty 'xxx.xxx.xxx.xxx' (ED25519) pysyvästi tiedostoon known hosts.
Tervetuloa Ubuntu 24.04.1 LTS (GNU/Linux 6.8.0-51-generic x86_64)

...

Ylläpitäjänä (käyttäjänä "root") voit suorittaa komennon "sudo <komento>".
Ks. "man sudo_root" lisätietoa varten.

ubuntu@pipeline-vm:~$
```

Lähdemme hetkeksi `terminal_pouta`, palaamme kun on aika asentaa ja konfiguroida työkalut sen sisällä.

### Liikenteen salliminen virtuaalikoneelta tietokantaan {#allowing-traffic-from-virtual-machine-to-database}

Oletuksena tietokanta-instanssimme Pukkissa ei salli mitään saapuvaa liikennettä.
Haluamme konfiguroida sen niin, että se hyväksyy liikenteen virtuaalikoneeltamme cPoutassa.

Siirrymme `terminal_pukki`-laitteeseen.
Ennen kuin aloitamme toiminnan tietokanta-instanssin kanssa, on huomattava, että yhdessä päätelaitteessa määritellyt ympäristömuuttujat eivät leviä automaattisesti muihin päätelaitteisiin.
Tämän vuoksi meidän on määritettävä kelluva IP-osoite, joka on annettu virtuaalikoneelle cPoutassa, ympäristömuuttujaksi myös tässä päätelaitteessa.
```
$ export POUTA_FLOATING_IP="xxx.xxx.xxx.xxx" # laita tähän sama arvo, joka on annettu samaan muuttujaan terminal_pouta-laitteessa
```

Annamme sitten seuraavan komennon:
```
$ openstack database instance update $DB_INSTANCE_NAME \
--allowed-cidr $POUTA_FLOATING_IP/32
```
Komennon **allowed-cidr**-parametri määrittää ip-osoitteiden joukon, joille liikenne tietokanta-instanssille on sallittua.

Jos komento onnistuu, se ei näytä tulostetta.
Voimme kuitenkin tarkistaa onnistuneen toiminnan katsomalla tietokanta-instanssimme tietoja:
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
| naam                     | pipeline_db_instance                                                                                      |
| operating_status         | HEALTHY                                                                                                   |
| julkinen                 | False                                                                                                     |
| region                   | regionOne                                                                                                 |
| service_status_updated   | 2025-02-04T13:16:10                                                                                       |
| status                   | ACTIVE                                                                                                    |
| päivitetty               | 2025-02-04T13:16:52                                                                                       |
| volume                   | 1                                                                                                         |
| volume_used              | 0.08                                                                                                      |
+--------------------------+-----------------------------------------------------------------------------------------------------------+
```
Näemme, että virtuaalikoneen kelluva IP-osoite on nyt listattu kohdassa `allowed_cidrs`.

Näyttämissä tiedoissa huomaa myös tietokanta-instanssimme julkisen IP-osoitteen, jota tarvitsemme seuraavissa vaiheissa.
Kentän `addresses` rivi sisältää kaksi osaa: osoitteen, joka on merkitty `private`, ja toisen, joka on merkitty `public`.
Palaamme `terminal_pouta`-laitteeseen, missä olemme vielä kirjautuneina virtuaalikoneeseemme cPoutassa, ja määrittelemme ympäristömuuttujaksi tietokannan julkisen osoitteen, koska tarvitsemme sitä myöhemmin konfiguroinnissa.
```
$ export DB_PUBLIC_IP="xxx.xxx.xxx.xxx" # laita tähän tietokanta-instanssin julkinen ip-osoite Pukissa
```

### Virtuaalikoneen pääsyn konfigurointi Allasiin {#configuring-access-from-virtual-machine-to-allas}

Työasemamme tavoin myös virtuaalikone on konfiguroitava pääsemään Allasissa isännöityihin säiliöihin.

`terminal_pouta`-päätteessä seuraamme [ohjeita s3cmd:n asennuksesta ja konfiguroinnista](../../../data/Allas/using_allas/s3_client.md#getting-started-with-s3cmd) virtuaalikoneen sisältä.
Kun s3cmd on konfiguroitu, testaamme, että kaikki toimii oikein listaamalla Allasin säiliömme:
```
$ s3cmd ls
2025-01-16 14:59  s3://input_bucket
2025-01-16 14:59  s3://output_bucket
```
Huomaamme, että voimme nähdä kaksi säiliötä, jotka olemme luoneet aikaisemmin opetusmateriaalissa.
Näin ollen olemme varmistaneet, että virtuaalikone pääsee nyt kunnolla Allasissa oleviin säiliöihin.

### Virtuaalikoneen pääsyn konfigurointi tietokantaan {#configuring-access-from-virtual-machine-to-database}

Tässä vaiheessa opetusmateriaalia liikenne virtuaalikoneelta voi saavuttaa Pukin tietokannan.
Tällä hetkellä virtuaalikoneella ei kuitenkaan ole tietoa siitä, missä tietokanta löytyy, eli sen julkista IP-osoitetta, eikä myöskään niitä tunnuksia, joita käytetään tietokantaan pääsemiseen.
Siksi konfiguroimme seuraavaksi tietokantayhteyden virtuaalikoneessa.

Pysymme `terminal_pouta`-päätteellä.
Aluksi asennamme työkalun, jota tarvitsemme puhuaksemme tietokannan kanssa:
```
$ sudo apt update ; sudo apt install postgresql-client
```

Määrittelemme sitten kaikki ympäristömuuttujat, joita tarvitsemme yhdistääksemme ja päästäksemme Pukin tietokantaan.
```
$ export DB_NAME="pipeline_db" # tietokannan nimi
$ export DB_USERNAME="db_admin" # tietokannan käyttäjä
$ export DB_PASSWORD="xxxxxx" # laita tähän tietokannan käyttäjän salasana
```

Määrittelemme myös postgresql-salasanatiedoston, jota voidaan sitten käyttää helposti tietokantaan yhdistämiseen komentoriviltä.
```
$ echo "$DB_PUBLIC_IP:5432:$DB_NAME:$DB_USERNAME:$DB_PASSWORD" >> ~/.pgpass
$ chmod 0600 ~/.pgpass
```
Lisätietoja postgresql-salasanatiedostosta löytyy sen omalta [kelvisivulta](https://www.postgresql.org/docs/current/libpq-pgpass.html).

Testataan nyt tietokantaan pääsyä.
`terminal_pouta`-päätteessä suorita seuraava komento:
```
$ psql -h "$DB_PUBLIC_IP" -d "$DB_NAME" -U "$DB_USERNAME"
```
Saat seuraavan kehotteen, joka osoittaa onnistuneen yhteyden tietokantaan:
```
psql (16.6 (Ubuntu 16.6-0ubuntu0.24.04.1), palvelin 17.2 (Debian 17.2-1.pgdg110+1))
VAROITUS: psql:n suuri versio 16, palvelimen suuri versio 17.
         Joitakin psql-ominaisuuksia ei ehkä toimi.
SSL-yhteys (protokolla: TLSv1.3, salaus: TLS_AES_256_GCM_SHA384, pakkaus: off)
Kirjoita "help" saadaksesi apua.

pipeline_db=>
```
Mennäksesi takaisin virtuaalikoneelle kirjoita vain `exit` ja paina `Enter`.

Kun olemme yhteydessä tietokantaamme, valmistelemme sen isännöimään tietoa, jota lähetämme siihen käsitellessämme kuvia.
Suoritamme seuraavan komennon luodaksemme taulukon, joka isännöi tietoa kuvista:
```
$ psql \
-h "$DB_PUBLIC_IP" \
-d "$DB_NAME" \
-U "$DB_USERNAME" \
-c "CREATE TABLE IF NOT EXISTS log_records (timestamp varchar(25) primary key, negated_picture_name text, negated_picture_hash text)"
```
Komennon parametrit ovat seuraavat:

* **h** on isäntänimi, eli ip-osoite, jossa tietokanta on löydettävissä.
* **d** on tietokannan nimi.
* **U** on käyttäjänimi, jota käytetään tietokantaan autentikoitumiseen.
* **c** on komento, joka annetaan tietokantaan itsessään. Komento on kirjoitettu tietokannan käyttämällä syntaksilla.

Jos komento onnistui, pääte vastaa yksinkertaisesti merkkijonolla `CREATE TABLE`.
Tietokanta on nyt konfiguroitu putkellemme.

### Kuvanmuuntoskriptin asentaminen {#installing-picture-transforming-script}

Viimeisenä osana konfigurointifaasia asennamme skriptin, joka huolehtii Allasista ja Pukista keskustelemisesta, sekä syötteen muuntamisesta.
Tätä varten asennamme ensin työkalun kuvien muuntamiseen.
`terminal_pouta`-päätteessä suorita:
```
$ sudo apt install imagemagick
```

Kun työkalu on asennettu kaikilla sen riippuvuuksilla, suoritamme:
```
$ nano pipeline_script.sh
```
Näemme vilkkuvan kursorin ikkunan vasemmassa yläkulmassa, mikä osoittaa, että voimme nyt kirjoittaa uuteen `pipeline_script.sh`-nimiseen tiedostoomme.
Kopioimme ja liitämme seuraavan sisällön.
Muistathan vaihtaa skriptin alussa määritellyt ympäristömuutt