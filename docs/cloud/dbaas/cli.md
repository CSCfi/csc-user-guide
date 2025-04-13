
# DBaaS:n käyttäminen komentoriviltä {#using-dbaas-with-cli}

DBaaS käyttää taustapuolella OpenStackia, mikä tarkoittaa, että voit käyttää OpenStackin komentorivityökaluja samalla tavalla kuin Poutassa. On tärkeää huomata, että vaikka Pouta käyttää samaa komentoriviä, se ei tarkoita, että olisit yhteydessä Poutaan. Tämä on erityisen tärkeää, jos automatisoit asioita sekä Poutassa että DBaaS:ssa, koska sinun on yhdistettävä eri Keystone-päätepisteisiin.

## Alkuun pääseminen {#getting-started}

1. Varmista ensin, että `python3` on asennettuna.
2. Asenna sitten komentorivityökalut:

   ```sh
   pip3 install python-openstackclient python-troveclient
   ```

3. Sinun on ladattava `openrc`-tiedostosi [Pukista](https://pukki.dbaas.csc.fi) ja valittava oikea projektinumero. Siirry sitten kohtaan `API Access` ja `Download OpenStack RC file` ja valitse `OpenStack RC file`.
4. Kun olet ladannut tiedoston, voit lähteä liikkeelle seuraavalla komennolla:

   ```sh
   source $FILENAME
   ```

5. Tämän jälkeen sinun pitäisi pystyä varmistamaan, että se toimii listaamalla käytettävissä olevat tietovarastot (saatavilla olevat tietokantatyypit):

   ```sh
   openstack datastore list
   ```

Muista, että voit käyttää apukomentoa `openstack help database` ja lippua `--help` saadaksesi lisätietoja eri komennoista.

## Tietokanta-instanssin luominen {#creating-a-database-instance}

1. Varmista, että olet käyttänyt lähdetettä openrc tiedostolle, jonka latasit [Pukista](https://pukki.dbaas.csc.fi).
2. Ennen tietokannan luomista on hyvä idea tietää, millaisia asetuksia haluat käyttää. Tässä ovat pääasiat, jotka haluat kerätä:
   - Uuden tietokanta-instancesi `name`. Tässä esimerkissä käytämme nimeä `my_database_instance`.
   - Mitä `databases` haluat luoda. Tässä esimerkissä käytämme `my_first_database`.
   - `IP addresses`, mistä haluaisit käyttää tietokantaasi. Voit yleensä selvittää IP-osoitteesi googlaamalla "mikä on IP-osoitteeni" tai käyttämällä tällaista sivustoa komentoriviltä:

     ```sh
     curl ifconfig.me
     ```

   - `Flavor`, esimerkiksi `standard.small`. Voit luetella käytettävissä olevat maut seuraavasti:

     ```sh
     openstack database flavor list
     ```

   - `Datastore`, ehdotus: `postgresql`. Voit löytää tietovarastoja seuraavasti:

     ```sh
     openstack datastore list
     ```

   - `datastore version`. Tämä valinnainen lippu riippuu valitusta tietovarastosta. Voit turvallisesti jättää sen pois, jos olet tyytyväinen oletustietovaraston versioon, joka on aina uusin saatavilla oleva. Voit selvittää käytettävissä olevat tietovarastoversiot seuraavasti:

     ```sh
     openstack datastore version list postgresql
     ```

   - Kuinka suuri `volume` GiB:ssä haluat käyttää tietokantasi tallentamiseen. Jos tämä on ensimmäinen kertasi testata DBaaS:ää, selviydyt yhdellä `1` GiB:llä.

   - Mitä `username` ja `password` haluat käyttää. Tässä esimerkissä käytämme `databaseuser` ja `myPassword568`.

3. Kun olet kerännyt tiedot, voit luoda tietokannan seuraavalla komennolla. Päivitä muuttujat tarpeesi mukaan, erityisesti `MY_IP`. Voit myös käyttää lippua `--allowed-cidr` useita kertoja lisätäksesi useita IP-osoitteita. Oletuksena luodut tietokanta-instanssit eivät sisällä yhtään `allowed-cidr`, mikä tarkoittaa, ettet voi yhdistää tietokantaasi.

   ```sh
   openstack database instance create my_database_instance \
   --flavor standard.small \
   --databases my_first_database \
   --users databaseuser:myPassword568 \
   --datastore postgresql \
   --datastore-version 17.0 \
   --is-public \
   --size 1 \
   --allowed-cidr ${MY_IP}/32
   ```

   Jos sinulla on ongelmia, älä epäröi käyttää komentoa `openstack database instance create --help`.

4. Nyt sinun on odotettava muutama minuutti, kunnes tietokanta-instanssit on luotu ja ne ovat saaneet julkisen IP:n. Kun instanssille on saatu `HEALTHY`-tila, julkinen IP pitäisi olla näkyvissä. Huomaa, että se näyttää sinulle yksityisen ja julkisen IP:n, olet kiinnostunut vain julkisesta IP:stä. Seuraava komento näyttää tietoja instanssista:

   ```sh
   openstack database instance show $INSTANCE_ID
   ```

5. Jos et ole tyytyväinen palomuureihin (`--allowed-cidr`), voit päivittää ne seuraavasti:

   ```sh
   openstack database instance update $INSTANCE_ID --allowed-cidr $NEW_IP_RANGE
   ```

On hyvä idea tarkistaa, mitä komentovaihtoehtoja on `openstack database instance update --help`.

Lisätietoja siitä, miten yhdistää tietokantoihin, löytyy navigaation vasemmalta puolelta kohdasta `Databases`.

### Palauttaminen varmuuskopioista {#restoring-from-backups}

Voit käyttää samaa komentoa kuin varmuuskopion luomisessa, mutta sinun on käytettävä lippua ja sitä varmuuskopiointitunnusta, jonka haluat käyttää palauttamiseen, `--backup $BACKUP_ID`.

### Lisähyödylliset komennot {#additional-useful-commands}

#### Luodaan ylimääräinen tietokanta tietokantainsanssiin {#create-additional-database-in-database-instance}

Tämä on samanlaista kuin `CREATE DATABASE db_name;`

```
openstack database db create $INSTANCE_ID $DB_NAME
```

#### Lisää käyttäjiä tietokantaan {#adding-users-to-a-database}

Listaa olemassa olevat käyttäjät tietokannassa:

```
openstack database user list $INSTANCE_ID
```

Luo uusi käyttäjä (`--databases` on valinnainen):

```
openstack database user create $INSTANCE_ID $USER_NAME $PASSWORD --databases $DATABASE_NAME
```

### Poistetaan käyttäjiä tietokannasta {#removing-users-from-a-database}

Käyttäjän poistaminen voidaan tehdä suorittamalla:

```
openstack database user delete $INSTANCE_ID $USER_NAME
```

#### Poista instanssi {#delete-instance}

Selvitä, mikä tietokantainstanssi haluat poistaa:

```
openstack database instance list
```

Poista instanssit:

```
openstack database instance delete $INSTANCE_ID
```

#### Tuetut toiminnot {#supported-functionality}

Nämä ovat käytettävissä olevat komennot tällä hetkellä:

| Openstack-komento | tila | Kommentit |
|--- |:---:|:---|
| openstack database backup create | Tuettu | Kaikkia lippuja ei ole testattu |
| openstack database backup delete | Tuettu | Saattaa poistua tulevaisuudessa |
| openstack database backup execution delete | Ei saatavilla | Ei tuettu DBaaS:ssä |
| openstack database backup list | Tuettu ||
| openstack database backup list instance | Tuettu ||
| openstack database backup show | Tuettu ||
| openstack database backup strategy create | Ei saatavilla | Vain ylläpitäjille käytettävissä |
| openstack database backup strategy delete | Ei saatavilla | Vain ylläpitäjille käytettävissä |
| openstack database backup strategy list | Ei saatavilla | Vain ylläpitäjille käytettävissä |
| openstack database cluster create | Ei saatavilla | Ei vielä tutkittu |
| openstack database cluster delete | Ei saatavilla | Ei vielä tutkittu |
| openstack database cluster force delete | Ei saatavilla | Ei vielä tutkittu |
| openstack database cluster grow | Ei saatavilla | Ei vielä tutkittu |
| openstack database cluster list | Ei saatavilla | Ei vielä tutkittu |
| openstack database cluster list instances | Ei saatavilla | Ei vielä tutkittu |
| openstack database cluster modules | Ei saatavilla | Ei vielä tutkittu |
| openstack database cluster reset status | Ei saatavilla | Ei vielä tutkittu |
| openstack database cluster show | Ei saatavilla | Ei vielä tutkittu |
| openstack database cluster shrink | Ei saatavilla | Ei vielä tutkittu |
| openstack database cluster upgrade | Ei saatavilla | Ei vielä tutkittu |
| openstack database configuration attach | Tuettu ||
| openstack database configuration create | Tuettu ||
| openstack database configuration default | Tuettu ||
| openstack database configuration delete | Tuettu ||
| openstack database configuration detach | Tuettu ||
| openstack database configuration instances | Tuettu ||
| openstack database configuration list | Tuettu ||
| openstack database configuration parameter list | Tuettu ||
| openstack database configuration parameter set | Tuettu ||
| openstack database configuration parameter show | Tuettu ||
| openstack database configuration set | Tuettu ||
| openstack database configuration show | Tuettu ||
| openstack database db create | Tuettu ||
| openstack database db delete | Tuettu ||
| openstack database db list | Tuettu ||
| openstack database flavor list | Tuettu ||
| openstack database flavor show | Tuettu ||
| openstack database instance create | Tuettu ||
| openstack database instance delete | Tuettu ||
| openstack database instance detach | Ei saatavilla ||
| openstack database instance eject | Ei saatavilla ||
| openstack database instance force delete | Vain ylläpitäjille ||
| openstack database instance list | Tuettu ||
| openstack database instance promote | Ei saatavilla ||
| openstack database instance reboot | Vain ylläpitäjille ||
| openstack database instance rebuild | Vain ylläpitäjille ||
| openstack database instance reset status | Vain ylläpitäjille ||
| openstack database instance resize flavor | Tuettu | Huomaa, että tämä aiheuttaa seisokkia |
| openstack database instance resize volume | Ei tuettu | Ei toimi ilman ylläpidon väliintuloa |
| openstack database instance restart | Tuettu | Uudelleenkäynnistää tietokantasäiliön - rajallinen hyöty |
| openstack database instance show | Tuettu ||
| openstack database instance update | Tuettu | Osa lipuista on tuettu. Tuetut liput ovat: --name , --allowed-cidr|
| openstack database instance upgrade | Tuettu | Päivittää tietokanta-instanssin. Tämä komento aiheuttaa seisokkia. |
| openstack database limit list | Tuettu ||
| openstack database log list | Tuettu | Mahdollistaa instanssilokien tarkastelun. Tämä API on epävakaa ja saattaa muuttua, se ei tee samaa kuin ylävirran |
| openstack database log save | Ei saatavilla ||
| openstack database log set | Ei saatavilla ||
| openstack database log show | Ei saatavilla ||
| openstack database log tail | Ei saatavilla ||
| openstack database quota show | Vain ylläpitäjille ||
| openstack database quota update | Vain ylläpitäjille ||
| openstack database root disable | Tuettu ||
| openstack database root enable | Tuettu | Useimmissa tapauksissa root enable ei ole tarpeen, mutta jos haluat tehdä kehittyneitä lupakonfiguraatioita, se on todennäköisesti tarpeen. |
| openstack database root show | Tuettu ||
| openstack database user create | Tuettu ||
| openstack database user delete | Tuettu ||
| openstack database user grant access | Tuettu ||
| openstack database user list | Tuettu ||
| openstack database user revoke access | Tuettu ||
| openstack database user show | Tuettu ||
| openstack database user show access | Tuettu ||
| openstack database user update attributes | Tuettu ||
| openstack datastore delete | Vain ylläpitäjille ||
| openstack datastore list | Tuettu ||
| openstack datastore show | Tuettu ||
| openstack datastore version create | Vain ylläpitäjille ||
| openstack datastore version delete | Vain ylläpitäjille ||
| openstack datastore version list | Tuettu ||
| openstack datastore version set | Vain ylläpitäjille ||
| openstack datastore version show | Tuettu ||

