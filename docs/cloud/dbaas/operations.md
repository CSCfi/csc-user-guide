# Tietokantaoperaatiot

## Pienten versioiden tietokantapäivitykset {#minor-version-database-upgrades}

Pukki DBaaS tarjoaa työkaluja, joiden avulla voit itse päivittää tietokantasi. Ennen päivitystä sinun on oltava tietoinen riskeistä ja vaikutuksista. Tietokannan päivittäminen aiheuttaa lyhyen käyttökatkon, jonka pituus riippuu käytetyistä tietokantaversioista ja tietokannan koosta. On suositeltavaa luoda uusi tietokantaesiintymä viimeaikaisesta varmuuskopiosta testataksesi päivitystä ensin.

Kun teet pienen tietokantapäivityksen,

1. Tietokantaesiintymäsi hakee uuden tietokantaversion.
2. Tietokantaesiintymäsi pysäyttää tietokantasi.
3. Tietokantaesiintymäsi käynnistää uuden tietokantaversion.

Käytettävät komennot:

1. Selvitä, mikä tietokanta haluat päivittää, ja ota huomioon `Datastore` ja `Datastore Version`:

    ```
    openstack database instance list
    ```

2. Varmista suosikkityökalullasi, että tietokantasi toimii odotetusti. Ota huomioon, mitä komentoa käytit, jotta voit käyttää samaa komentoa/prosessia varmistaaksesi, että kaikki toimii päivityksen jälkeen.
3. Selvitä, mitkä tietokantaversiot ovat saatavilla:

    ```
    openstack datastore version list $Datastore
    ```

4. Todennäköisesti haluat valita uusimman version:

    ```
    openstack database instance upgrade $Instance $Datastore_version
    ```

5. Varmista suosikkityökalullasi, että tietokantasi toimii odotetusti.

## Suuret tietokantapäivitykset {#major-database-upgrades}

Suuret version päivitykset eivät eroaa käyttäjän näkökulmasta, mutta taustalla tapahtuu enemmän, mikä voi aiheuttaa enemmän virhemahdollisuuksia.

Tietoja, jotka sinun tulee ottaa huomioon, kun teet suuren tietokantaversion päivityksen:
1. Sinulla on riittävän uusi varmuuskopio, jota voit käyttää, jos päivitys epäonnistuu.
2. Olet testannut päivityksen tekemistä varmuuskopiosta palautetulla tietokantaesiintymällä.
3. Olet varannut runsaasti aikaa päivitykselle.
4. Olet harkinnut, olisiko hyötyä käyttää suurempaa esiintymäversiota päivityksen aikana.
5. Olet tarkistanut, että tietokantaesiintymälläsi on riittävästi vapaata levytilaa ennen päivityksen aloittamista - suosittelemme, että tilaa on noin kaksinkertaisesti enemmän kuin käytössä.

Suosittelemme luomaan uuden tietokantaesiintymän viimeaikaisesta varmuuskopiosta ja päivittämään kyseisen esiintymän haluttuun tietokantaversioon, koska voit sitten siirtyä käyttämään uutta tietokantaesiintymää uudella tietokantaversiolla omalla aikataulullasi sen jälkeen, kun olet varmistunut ongelmien puuttumisesta. Haittoihin kuuluu se, että sinun on vaihdettava uuteen IP-osoitteeseen tietokantaan yhdistämiseksi, ja kaikki alkuperäiseen tietokantaan tehdyt muutokset varmuuskopion ottamisen jälkeen menetetään.

## Tietokannan poistaminen tietokantaesiintymästäsi {#deleting-a-database-in-your-database-instance}

Oletuksena tietokantakäyttäjätunnuksellasi ei ole oikeuksia poistaa tietokantoja. Jos haluat poistaa tietokannan tietokantaesiintymästäsi, sinun on käytettävä web-käyttöliittymää tai OpenStack CLI:ta:

```
openstack database db delete $INSTANCE_UUID $DATABASE_NAME
```

## Pääkäyttäjän käyttöönottaminen {#enable-root}

Joihinkin muutoksiin, kuten laajennusten käyttöönotto tai edistyneempien käyttäjäoikeuksien muokkaaminen, ei päästä web-käyttöliittymän tai OpenStack-komentorivityökalujen kautta. Kannattaa pitää mielessä, että pääkäyttäjätunnuksella aktiivisena voit tehdä tietokantaan muutoksia, jotka voivat rikkoa sen toimintaa. On suositeltavaa käyttää pääkäyttäjää vain silloin, kun se on todellisuudessa tarpeellista.

### Kuinka ottaa pääkäyttäjä käyttöön web-käyttöliittymässä {#how-to-enable-root-from-the-web-interface}

1. Kirjaudu sisään web-käyttöliittymään, jossa näet kaikki olemassa olevat esiintymäsi.
2. Etsi 'Toiminnot'-valikko oikeimmasta sarakkeesta ja valitse `Hallitse pääkäyttäjän käyttöoikeuksia`. ![Hallitse pääkäyttäjän käyttöoikeuksia](../../img/dbaas-enable-root.png)
3. Hallitse pääkäyttäjän käyttöoikeuksia -sivulla paina oikeimman sarakkeen `Ota pääkäyttäjä käyttöön` -painiketta esiintymätaulukosta.
4. Pääkäyttäjän salasana on nyt näkyvissä samalla Hallitse pääkäyttäjän käyttöoikeuksia -sivulla. Voit käyttää tietokantaa näytetyllä salasanalla ja `root`-tunnuksella.
5. Kun et enää tarvitse pääkäyttäjän käyttöoikeuksia, paina `Poista pääkäyttäjä` hallitse pääkäyttäjän käyttöoikeuksia -sivulla.

### Kuinka ottaa pääkäyttäjä käyttöön komentorivillä {#how-to-enable-root-from-the-cli}

1. Ota pääkäyttäjä käyttöön
    ```
    openstack database root enable $INSTANCE_ID
    ```

2. Käytä salasanana pääkäyttäjän käyttöoikeuksia, ja käytä käyttäjätunnuksena `root` päästäksesi tietokantaan.

3. Kun et enää tarvitse pääkäyttäjän käyttöoikeuksia, suorita seuraava komento poistaaksesi sen:

    ```
    openstack database root disable $INSTANCE_ID
    