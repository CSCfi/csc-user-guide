## OpenStackin komentoriviasiakastyökalut Poutaa varten { #openstack-command-line-client-tools-for-pouta }

Tämä artikkeli kuvaa Poutan käyttöä komentoriviltä. Jos et ole vielä tehnyt sitä, aloita [asentamalla OpenStack-työkalut](install-client.md).

Suurimman osan tarvitsemistasi asioista voit tehdä OpenStackin (Horizon)
verkkokäyttöliittymässä cPoutassa ja ePoutassa. Joskus on kuitenkin kätevämpää
tai jopa välttämätöntä käyttää komentorivityökaluja. OpenStack on jaettu
alijärjestelmiin, joista kukin hoitaa tiettyjä tehtäviä, kuten virtuaalikoneiden,
levyjen tai levykuvien hallintaa. Jokaisella alijärjestelmällä on oma API, jota
voi käyttää joko ohjelmallisesti tai päätteen kautta hyödyntäen tässä
luvussa esiteltyjä komentorivityökaluja.

Komentorivityökaluilla hallitaan palvelun käyttöäsi, joten ne kannattaa
asentaa joko paikalliselle kannettavalle/työpöydälle tai toiselle palvelimelle,
jolta hallinnoit palvelua.

# Poutan käyttäminen komentoriviltä { #using-pouta-from-the-command-line }

Tässä artikkelissa luetellaan peruskomentoja OpenStackin yleisimpiin
toimenpiteisiin. Jokaisesta toimenpiteestä näytämme komennon, joka käyttää
yhteistä OpenStackin komentorivityökalua.

##### Seuraavien OpenStack-komentojen suositellut versiot toimivat nykyisen ePoutan ja cPoutan (Wallaby) kanssa. { #these-recommended-versions-of-the-openstack-commands-should-work-with-the-current-version-of-epouta-and-cpouta-wallaby }

- [python-openstackclient](https://docs.openstack.org/releasenotes/python-openstackclient/)==5.5.0
- [python-cinderclient](https://docs.openstack.org/releasenotes/python-cinderclient/)==7.4.1
- [python-glanceclient](https://docs.openstack.org/releasenotes/python-glanceclient/)==3.3.0
- [python-heatclient](https://docs.openstack.org/releasenotes/python-heatclient/)==2.3.0
- [python-keystoneclient](https://docs.openstack.org/releasenotes/python-keystoneclient/)==4.2.0
- [python-neutronclient](https://docs.openstack.org/releasenotes/python-neutronclient/)==7.3.0
- [python-novaclient](https://docs.openstack.org/releasenotes/python-novaclient/)==17.4.0
- [python-swiftclient](https://docs.openstack.org/releasenotes/python-swiftclient/)==3.11.0

Lisätietoja: [OpenStackClient pip -moduuli](https://pypi.org/project/python-openstackclient/)  

!!! info

    Voit asentaa OpenStackClient-pip-moduulin uusimmat versiot, sillä ne ovat taaksepäin yhteensopivia.

##### OpenStack-komennot ja ohje { #openstack-commands-and-help }

    openstack -h

Saat listan käytettävissä olevista OpenStackin alakomennoista lisäämällä "-h"
`openstack`-komennon perään. Jos haluat nähdä tietyn alakäskyn valinnat,
lisää komennon nimi "help"-sanan jälkeen. Esimerkiksi:

    openstack help server create

##### Avainparin lisääminen { #adding-a-keypair }

    openstack keypair create --public-key <file> <name>

**Ensimmäinen asia, joka kannattaa tehdä**, on
luoda avainpari. Sitä käytetään virtuaalikoneisiin kirjautumiseen. Voit myös
halutessasi antaa aiemmin luodun julkisen avaimen, jolloin yksityinen avain
on se, jonka loit kyseistä julkista avainta luotaessa.

Luo "test"-niminen avainpari ja tallenna yksityinen avain tiedostoon "test.pem":

    openstack keypair create test > test.pem

##### Luettele saatavilla olevat levykuvat { #list-available-images }

    openstack image list

Tämä komento listaa käyttäjälle saatavilla olevat levykuvat.
Mukana ovat julkiset kuvat ja käyttäjän itse lisäämät kuvat.

##### Luettele saatavilla olevat flavorit { #list-the-available-flavors }

    openstack flavor list

Virtuaalikoneen flavor määrittää sen virtuaalisen laitteiston: kuinka monta
ydintä, kuinka paljon muistia jne.

##### Käynnistä virtuaalikone { #launch-a-virtual-machine }

    openstack server create --flavor <flavor> --image <image id> --key-name <key name> <name for machine>

Tässä komennossa on vähimmäistiedot toimivan virtuaalikoneen käynnistämiseksi.

!!! info

    Komennon "openstack server create" tulosteessa näkyy myös
    adminPass-niminen salasana. Sinun ei tarvitse tallettaa tätä salasanaa,
    koska sitä ei käytetä virtuaalikoneeseen yhdistettäessä. Virtuaalikone
    sallii pääsyn vain käyttäjälle, joka käyttää SSH-avaimia.

##### Mukauta virtuaalikonetta ennen käynnistystä { #customize-the-virtual-machine-before-launch }

    openstack server create --flavor <flavor> --image <image id> --key-name <key name> --user-data user-data.sh <name for machine>

Tiedosto `user-data.sh` voi sisältää lisäkomentoja, jotka ajetaan automaattisesti instanssin käynnistyksen jälkeen.

Alla on esimerkki skriptitiedoston sisällöstä, joka lisää oman käyttäjän ja antaa sille `sudo`-oikeudet:

``` bash
#!/bin/sh

# Add a new user called boss
useradd -m boss

# Add the user to sudoers. No password is needed for sudo.
echo 'boss ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/boss
```

Skripti voi sisältää mitä tahansa komentoja, joten varovaisuutta suositellaan.

!!! Note
    Huomaathan, että esimerkki ei lisää käyttäjän todennusta (julkista SSH-avainta).

##### Luettele instanssit { #list-instances }

    openstack server list

Tämä antaa listan käyttäjän instansseista ja niihin liittyvistä tiedoista.

##### Poista instanssit { #terminate-instances }

    openstack server delete <server>

Tämä komento sammuttaa ja poistaa koneen. Käynnissä ollut virtuaalikone
poistetaan eikä sitä voi palauttaa.

##### Liitä julkinen osoite { #associate-public-address }

    openstack floating ip create public

Julkinen osoite pitää ensin varata osoitepoolista. Tässä vaiheessa
IP-osoitetta ei ole vielä liitetty mihinkään koneeseen.

    openstack server add floating ip <server> <address>

Tämä komento liittää juuri varatun osoitteen virtuaalikoneeseen.

Kun et enää tarvitse julkista osoitetta, voit vapauttaa sen julkiseen
pooliin poistamalla sen.

    openstack floating ip delete <address>

Näin säästät Cloud Billing Unit -yksiköitä ja pidät julkisten IP-osoitteiden
käytön tehokkaana.

##### Yhteyksien salliminen virtuaalikoneisiin { #authorization-to-connect-to-virtual-machines }

Luo uusi security group:

    openstack security group create <security group name>

Lisää tähän uuteen ryhmään sääntö, joka sallii pingin tietystä
lähdeverkosta:

    openstack security group rule create --proto icmp --remote-ip <source network> --dst-port 0 <security group name>

Lisää sääntö, joka sallii SSH-yhteydet tietystä lähdeverkosta:

    openstack security group rule create --proto tcp --remote-ip <source network> --dst-port 22 <security group name>

Liitä luotu security group virtuaalipalvelimeesi:

    openstack server add security group <server> <security group name>

Oletuksena kaikki yhteydet virtuaalikoneisiin on estetty. Näillä komennoilla
sallitaan ping ja SSH.

##### Palvelinryhmät ja affiniteetti { #server-groups-and-affinity }

OpenStackissa voidaan luoda niin sanottuja palvelinryhmiä (server groups),
joille määritellään affiniteetti- tai anti-affiniteettisääntöjä. Määrität
palvelinta käynnistäessäsi, haluatko käyttää tiettyä ryhmää.

Affiniteettisäännöllä varustettu palvelinryhmä takaa, että kaikki ryhmään
käynnistetyt virtuaalikoneet käynnistetään samalle fyysiselle palvelimelle.
Anti-affiniteettisäännöllä varustettu ryhmä takaa, että kaikki ryhmän
palvelimet käynnistetään eri fyysisille palvelimille. Jos sopivaa
fyysistä palvelinta ei löydy, virtuaalikonetta ei luoda.

    openstack server group create --policy <affinity or anti-affinity> <server group name>

Tämän jälkeen voit käynnistää virtuaalikoneita ryhmään
antamalla ryhmän tunnisteen hint-parametrissa.

    openstack server create --flavor <flavor> --image <image id> --key-name <key name> --hint group=<server group id> <name for machine>

Tarkista, mitkä virtuaalikoneet kuuluvat palvelinryhmään:

    openstack server group show <server group id>

### Ulkoinen dokumentaatio { #external-documentation }

[Laajempi OpenStack CLI -viite](https://docs.openstack.org/python-openstackclient/latest/).