
## OpenStack-komentorivityökalut Poutalle {#openstack-command-line-client-tools-for-pouta}

Tässä artikkelissa kuvataan Poutan käyttö komentorivillä. Jos et ole
vielä tehnyt sitä, aloita [OpenStack-työkalujen asentaminen](install-client.md).

Voit suorittaa suurimman osan tarvitsemistasi toiminnoista OpenStackin (Horizon)
verkkokäyttöliittymässä cPoutassa ja ePoutassa. Kuitenkin joskus on kätevämpää
tai jopa välttämätöntä käyttää komentorivityökaluja. OpenStack on jaettu
osakokonaisuuksiin, jotka kukin hoitavat tiettyjä tehtäviä kuten virtuaalikoneiden,
volumien tai kuvien hallintaa. Jokaisella osakokonaisuudella on oma API, jota voidaan 
käyttää joko ohjelmallisesti tai terminaalissa käyttämällä tässä luvussa 
esiteltyjä komentorivityökaluja.

Komentorivityökaluja käytetään palvelun hallintaan, joten ne tulisi asentaa
paikalliselle kannettavalle/pöytäkoneelle tai toiselle palvelimelle, jota
käytät palvelun hallintaan.

# Poutan käyttäminen komentoriviltä {#using-pouta-from-the-command-line}

Tämä artikkeli sisältää joitakin peruskomentoja, joita tarvitaan
tavallisimmissa OpenStack-toiminnoissa. Jokaiselle toimenpiteelle esitetään
komento, joka käyttää yleistä OpenStack-komentorivityökalua.

##### Näiden suositeltujen OpenStack-komentojen versioiden pitäisi toimia nykyisten ePouta- ja cPouta-versioiden (Ussuri) kanssa. {#these-recommended-versions-of-the-openstack-commands-should-work-with-the-current-version-of-epouta-and-cpouta-ussuri}

- [python-openstackclient](https://docs.openstack.org/releasenotes/python-openstackclient/)==5.2.2
- [python-cinderclient](https://docs.openstack.org/releasenotes/python-cinderclient/)==7.0.2
- [python-glanceclient](https://docs.openstack.org/releasenotes/python-glanceclient/)==3.1.2
- [python-heatclient](https://docs.openstack.org/releasenotes/python-heatclient/)==2.1.0
- [python-keystoneclient](https://docs.openstack.org/releasenotes/python-keystoneclient/)==4.0.0
- [python-neutronclient](https://docs.openstack.org/releasenotes/python-neutronclient/)==7.1.1
- [python-novaclient](https://docs.openstack.org/releasenotes/python-novaclient/)==17.0.1
- [python-swiftclient](https://docs.openstack.org/releasenotes/python-swiftclient/)==3.9.1

Lisätietoja: [OpenStackClient pip -moduuli](https://pypi.org/project/python-openstackclient/)

!!! info

    Voit asentaa OpenStackClient pip -moduulin uusimmat versiot, koska ne ovat taaksepäin yhteensopivia.

##### Openstack-komennot ja ohje {#openstack-commands-and-help}

    openstack -h

Voit saada listan saatavilla olevista OpenStack-alakomennosta lisäämällä "-h"
`openstack`-komennon jälkeen. Jos haluat nähdä tietyn alakomennon vaihtoehdot,
lisää komennon nimi sanan "help" jälkeen. Esimerkiksi:

    openstack help server create

##### Avaintapparin lisääminen {#adding-a-keypair}

    openstack keypair create --public-key <file> <name>

**Ensimmäinen asia, jonka sinun tulisi tehdä,** on
avainparin luominen. Sitä käytetään virtuaalikoneiden käyttöön
pääsyyn. Voit myös valinnaisesti määritellä aiemmin luodun julkisen avaimen,
jolloin yksityinen avain on se, jonka loit, kun
julkinen avain luotiin.

Luo avain nimeltä "test" yksityisellä avaimella, joka on tallennettu "test.pem":

    openstack keypair create test > test.pem

##### Saatavilla olevien kuvien listaaminen {#list-available-images}

    openstack image list

Tämä komento listaa käyttäjän käytettävissä olevat kuvat. Tämä
sisältää julkiset kuvat ja käyttäjän lisäämät kuvat.

##### Saatavilla olevien flavorien listaaminen {#list-the-available-flavors}

    openstack flavor list

Virtuaalikoneen flavor määrittelee sen virtuaalisen laitteiston: kuinka monta
ydintä, kuinka paljon muistia jne.

##### Virtuaalikoneen käynnistäminen {#launch-a-virtual-machine}

    openstack server create --flavor <flavor> --image <image id> --key-name <key name> <name for machine>

Tässä komennossa on minimimäärä tietoa, joka tarvitaan
toimivan virtuaalikoneen käynnistämiseksi.

!!! info

    Komennon "openstack server create" tuloste näyttää myös
    salasanan nimeltä adminPass. Sinun ei tarvitse säilyttää tätä salasanaa, sillä
    sitä ei käytetä virtuaalikoneeseen yhdistämiseen. Virtuaalikone sallii
    pääsyn käyttäjille vain, jos he käyttävät SSH-avaimia.

##### Virtuaalikoneen kustomointi ennen käynnistämistä {#customize-the-virtual-machine-before-launch}

    openstack server create --flavor <flavor> --image <image id> --key-name <key name> --user-data user-data.sh <name for machine>

`user-data.sh`-tiedostossa voi olla ylimääräisiä komentoja, jotka suoritetaan automaattisesti, kun instanssi on käynnistetty.

Alla on esimerkki skriptitiedostosta, joka lisää räätälöidyn käyttäjän flavoriin ja antaa sille `sudo`-oikeudet:

```bash
#!/bin/sh

# Lisää uusi käyttäjä nimeltään boss
useradd -m boss

# Lisää käyttäjä sudoers-tiedostoon. Sudo-käskyn käyttöön ei tarvita salasanaa.
echo 'boss ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/boss
```

Skriptitiedosto voi sisältää minkä tahansa mielivaltaisen komennon, joten varovaisuus on suositeltavaa.

!!! Note
    Huomaa, että esimerkissä ei ole käyttäjän tunnistamista (julkinen SSH-avain.)

##### Instanssien listaaminen {#list-instances}

    openstack server list

Tämä antaa käyttäjän instanssien ja niihin liittyvien tietojen listauksen.

##### Instanssien lopettaminen {#terminate-instances}

    openstack server delete <server>

Tämä komento sammuttaa ja poistaa koneen. Käynnissä oleva virtuaalikone
poistetaan, eikä sitä voida palauttaa.

##### Julkisen osoitteen liittäminen {#associate-public-address}

    openstack floating ip create public

Julkinen osoite on ensin varattava osoitepoolista. Tässä
vaiheessa IP-osoitetta ei ole liitetty mihinkään isäntään.

    openstack server add floating ip <server> <address>

Tämä komento liittää juuri varatun osoitteen virtuaalikoneeseen.

Kun et enää tarvitse julkista osoitetta, voit vapauttaa sen
julkiseen pooliin poistamalla sen.

    openstack floating ip delete <address>

Näin voit säästää laskutusyksiköitä ja ylläpitää julkisten IP-osoitteiden tehokasta käyttöä.

##### Valtuutus virtuaalikoneisiin yhdistämiseksi {#authorization-to-connect-to-virtual-machines}

Luo uusi turvaryhmä:

    openstack security group create <security group name>

Lisää sääntö tähän uuteen ryhmään, joka sallii pingiämisen määritellyltä
lähdeverkostolta:

    openstack security group rule create --proto icmp --remote-ip <source network> --dst-port 0 <security group name>

Lisää sääntö, joka sallii SSH-yhteydet määritellyltä lähdeverkostolta:

    openstack security group rule create --proto tcp --remote-ip <source network> --dst-port 22 <security group name>

Liitä juuri luotu turvaryhmä virtuaalipalvelimeesi:

    openstack server add security group <server> <security group name>

Oletuksena kaikki yhteydet virtuaalikoneisiin on estetty. Tämä komento
sallii ping- ja SSH-yhteydet.

##### Palvelinryhmät ja affinity {#server-groups-and-affinity}

OpenStackilla on mahdollisuus luoda niin sanottuja palvelinryhmiä
tietyillä affinity- ja anti-affinity-säännöillä. Voit määrittää, haluatko
käyttää tiettyä ryhmää, kun käynnistät palvelimen.

Palvelinryhmä, jossa on affinity-sääntö, takaa, että kaikki ryhmään kuuluvat
virtuaalikoneet käynnistetään samalla fyysisellä palvelimella. Palvelinryhmä,
jossa on anti-affinity-sääntö, takaa, että ryhmän kaikki palvelimet käynnistetään
eri fyysisillä palvelimilla. Jos sopivaa fyysistä palvelinta ei löydy,
virtuaalikonetta ei luoda.

    openstack server group create --policy <affinity or anti-affinity> <server group name>

Tämän jälkeen voit käynnistää virtuaalikoneita ryhmässä määrittämällä ryhmän ID:n
vinkkiparametriin.

    openstack server create --flavor <flavor> --image <image id> --key-name <key name> --hint group=<server group id> <name for machine>

Tarkista, mitkä virtuaalikoneet kuuluvat palvelinryhmään:

    openstack server group show <server group id>

### Ulkoinen dokumentaatio {#external-documentation}

[Yksityiskohtaisempi OpenStack CLI -viite](https://docs.openstack.org/python-openstackclient/latest/).

