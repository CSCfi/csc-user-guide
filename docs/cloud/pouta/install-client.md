# OpenStack-komentorivityökalujen asennus pakettienhallintatyökaluilla { #openstack-command-line-tool-installation-using-package-manager-tools }

Tässä artikkelissa kuvataan, miten OpenStackin komentorivityökalut asennetaan
Ubuntu-, Red Hat- ja OS X -pohjaisiin järjestelmiin
OpenStackin eri ominaisuuksien tehokkaaseen hallintaan.
Asennusohjeet perustuvat Pythonin _pip_-pakettiin. Kun pip on
paikallaan, vaiheet ovat samat kaikissa järjestelmissä.

!!! info

    Jos sinulla ei ole root-/ylläpitäjäoikeuksia
    siihen järjestelmään, jossa haluat ajaa komentoriviasiakkaita,
    katso ohjeet [virtuaaliympäristöistä](#optional-installation-in-a-python-virtual-environment).

Windowsiin asentaminen on myös mahdollista, mutta se ei kuulu tämän
oppaan piiriin. Rackspace ylläpitää opasta [python-novaclientin asentamiseen Windowsissa](https://docs.rackspace.com/support/how-to/install-python-novaclient-on-windows/).

Suosittelemme ensin tutustumaan [Pouta-verkkokäyttöliittymään](launch-vm-from-web-gui.md) ja keskeisiin käsitteisiin.

## OpenStackin komentorivityökalujen yleiskuvaus { #overview-of-the-openstack-command-line-tools }

On olemassa yleiskäyttöinen komentorivityökalu nimeltä "openstack",
jolla voidaan hallita suurinta osaa OpenStackin toiminnoista. Lisäksi on
erillisiä työkaluja tiettyjen OpenStack-toiminnallisuuksien hallintaan, kuten
"neutron" verkkojen hallintaan ja "glance" virtuaalikonekuvien
hallintaan. Useimmissa tapauksissa tulisi käyttää yleistä openstack-
työkalua. Muut työkalut ovat OpenStack-projektissa vanhentuneita
(deprecated) ja niitä tarvitaan yleensä vain, jos sinulla on niistä riippuvia skriptejä
tai jos sinun on ajettava tiettyjä hallinnollisia
komentoja.

| Työkalun nimi | Paketin nimi | Käyttötarkoitus |
|-----------|------------------------|------------------------------------------------------------------------------------------------|
| openstack | python-openstackclient | Koko OpenStackin hallinta |
| nova      | python-novaclient      | Virtuaalikoneiden hallinta sekä rajattu toiminnallisuus esim. volyymien ja kuvien hallintaan. |
| neutron   | python-neutronclient   | Virtuaaliverkkojen ja reitittimien hallinta. |
| glance    | python-glanceclient    | Virtuaalikonekuvien hallinta. |
| cinder    | python-cinderclient    | Virtuaalikoneisiin liitettävien volyymien hallinta. |
| swift     | python-swiftclient     | Objektien hallinta Swift API:n avulla |

### Valmistelut { #preparation }

Varsinaisten komentorivityökalujen asennusta varten asennetaan pip ja Pythonin kehityspaketit.

!!! info

    Oletamme tässä, että sinulla on Python jo asennettuna. Tämä on
    todennäköistä, jos käytät jotakin käyttöjärjestelmää,
    jolle tässä annamme ohjeita.

Selvitä, onko Python asennettu ja mikä versio on käytössä:

~~~~
python --version
~~~~

Tarvitset Python 3:n tai uudemman, jotta voit asentaa komentorivi-
asiakastyökalut. Jos käytät edes suhteellisen tuoretta käyttöjärjestelmäversiota,
tämän ei pitäisi olla ongelma. Jos sinulla kuitenkin on Red Hat -pohjainen
järjestelmä, joka on vanhempi kuin versio 7, et voi asentaa Python 3:a
tavanomaisella tavalla. Emme tue RHEL/CentOS 7:ää vanhempia versioita.

Jos sinulla ei jostain syystä ole Pythonia asennettuna, ole hyvä ja [install it first].

#### Valmistelut: Ubuntu-pohjaiset järjestelmät { #preparation-ubuntu-based-systems }

Jos käytössä on Ubuntu 16.04 tai uudempi:

~~~~
sudo apt install python3-pip python3-dev
~~~~

Versioille, jotka ovat vanhempia kuin 16.04:

    sudo apt-get install python3-pip python3-dev

#### Valmistelut: Red Hat -pohjaiset järjestelmät { #preparation-red-hat-based-systems }

Jos käytössä on versio 7 tai uudempi:

    sudo yum install python3-pip python3-devel

#### Valmistelut: OS X -järjestelmät { #preparation-os-x-systems }

Lataa uusin [Python setuptools](https://pypi.python.org/pypi/setuptools)"

Asenna työkalut ja pip:

    sudo python ez_setup.py
    sudo /usr/local/bin/easy_install pip

### Openstack-työkalun asennus (kaikki käyttöjärjestelmät) { #installing-the-openstack-tool-all-operating-systems }

Tästä eteenpäin asennusohjeet ovat samat kaikille käyttöjärjestelmille.

#### Valinnainen: asennus Pythonin virtuaaliympäristöön { #optional-installation-in-a-python-virtual-environment }

Jos käytät OpenStackin komentorivityökalujen lisäksi muita Python-
ohjelmia tietokoneellasi, suosittelemme Pythonin virtuaaliympäristöjen käyttöä.
Pythonin virtuaaliympäristöt mahdollistavat eristetyn Python-pakettijoukon,
joka on käytettävissä vain kyseisessä virtuaaliympäristössä. Ne ovat kätevä tapa
pitää Python-asennuksesi siistinä ja hallittavana. Tarvitset niitä myös, jos
haluat asentaa komentoriviasiakkaat tietokoneeseen, johon sinulla ei ole
pääkäyttäjäoikeuksia. Tällöin järjestelmänvalvojan tulee asentaa puolestasi
Python, pip ja virtualenv-Python-paketti. Lisätietoja virtuaaliympäristöistä:
[The Hitchhiker's Guide to Python].

Tässä annamme perusohjeet yksinkertaisen virtuaaliympäristön
luomiseksi asiakastyökalujen asennusta varten. Jos et halua käyttää
virtuaaliympäristöjä, voit ohittaa nämä vaiheet ja siirtyä suoraan
pip-asennusohjeisiin.

Asenna ensin python3-venv-paketti. Ubuntussa:

    sudo apt install python3-venv

Huomaa, että Red Hat -pohjaisissa järjestelmissä erillistä pakettia ei tarvitse asentaa.

Luo hakemisto virtuaaliympäristöillesi. Annamme sille tässä tietyn nimen, mutta voit käyttää myös muuta nimeä:

    mkdir python_virtualenvs

Siirry hakemistoon ja luo uusi virtuaaliympäristö:

    cd python_virtualenvs
    python3 -m venv osclient

Tämä luo uuden "osclient"-nimisen hakemiston
"python_virtualenvs"-hakemistoon. Tämä hakemisto sisältää
kaiken, mitä asennat virtuaaliympäristöön. Se sisältää myös ympäristön
aktivointiskriptin, joka täytyy ajaa seuraavaksi:

    source osclient/bin/activate

Aktivoinnin jälkeen kaikki Python- tai
pip-komennot suoritetaan virtuaaliympäristön kontekstissa. Jos
jatkat nyt alla olevien asennusohjeiden mukaan, kaikki paketit
asennetaan juuri luomaasi virtuaaliympäristöön. Tiedät, että
"osclient"-virtuaaliympäristö on aktivoitu, kun näet
kuoren kehotteessa tekstin "(osclient)". Jos asennat komentoriviasiakkaat
virtuaaliympäristöön, ne ovat käytettävissä vain kyseisessä virtuaaliympäristössä.

Asennuksen jälkeen, jos haluat poistaa virtuaaliympäristön käytöstä,
voit yksinkertaisesti kirjoittaa:

    deactivate

Huomaa, että tämän tekeminen tarkoittaa myös sitä, että mitkään asentamasi
komentorivityökalut eivät ole käytettävissä ennen kuin aktivoit
virtuaaliympäristön uudelleen.

#### Asiakastyökalujen asennus pipillä { #installing-the-client-tools-using-pip }

OpenStack tarjoaa joukon Python-työkaluja toimintojensa eri osa-alueiden
hallintaan. Jokaisella OpenStackin osakomponentilla on oma työkalunsa. Lisäksi
on yhteinen jaettu työkalu
*python-openstackclient*. Helpoin tapa asentaa suurin osa
komentorivityökaluista on asentaa python-openstackclient. Sen pitäisi
tuoda useita muita asiakkaita riippuvuuksina. Jos jokin tarvitsemasi työkalu
puuttuu vielä python-openstackclientin asentamisen jälkeen, katso
tämän sivun alussa olevaa taulukkoa asennettavista paketeista.

!!! info

    Jos seurasit virtuaaliympäristön luonnin ohjeita, poista "sudo"
    alla olevien komentojen alusta. Koska asennat omaan virtuaaliympäristöösi, et
    halua ajaa komentoja pääkäyttäjänä.

Asenna python-openstackclient pipillä:

    sudo pip install python-openstackclient

Jos haluat lisäksi asentaa kaikki sivun alussa luetellut palvelukohtaiset työkalut:

    sudo pip install python-keystoneclient python-novaclient python-glanceclient python-neutronclient

Riippuen tietokoneesi kokoonpanosta jotkin riippuvuudet saattavat olla
hukassa. Virheilmoitus `ImportError: No module named
<module>` korjaantuu yleensä asentamalla puuttuva moduuli
pipillä ja toistamalla edellinen, epäonnistunut komento. Joissakin
asennusvirheissä setuptoolsin tai pipin päivittäminen voi auttaa.
Päivitä paketti:

    sudo pip install -U python_module_to_be_upgraded

### Määritä päätteen ympäristö OpenStackia varten { #configure-your-terminal-environment-for-openstack }

Ympäristömuuttujat on asetettava ennen kuin voit käyttää
asiakasta. Voit asettaa ne OpenStackin web-käyttöliittymän
tarjoamalla skriptillä. Voit ladata tämän skriptin seuraavasta URL-osoitteesta
kirjautumisen jälkeen:

> <a
> href="https://pouta.csc.fi/dashboard/project/api_access/"
> class="external-link">https://pouta.csc.fi/dashboard/project/api_access/</a>

Lataa skripti web-käyttöliittymässä siirtymällä
kohtaan *API Access* ja painamalla *Download OpenStack RC File v3.*

![RC-tiedoston esimerkki](../../img/pouta-openrc.png)

Kun sinulla on web-käyttöliittymästä ladattu openrc-skripti, voit lisätä
ympäristömuuttujat:

    source <project_name_here>-openrc.sh

Sinua pyydetään syöttämään salasana. *Käytä CSC-tunnuksesi salasanaa*, koska komentorivikäyttöliittymä ei vielä tue
linkitettyjen tunnusten, kuten Haka tai Virtu, käyttöä. Tämän jälkeen
nykyisessä pääteistunnossa on oikeat ympäristömuuttujat komentorivityökalujen käyttöä
varten. Sinun on tehtävä tämä uudelleen, jos avaat uuden päätteen.

  [install it first]: http://docs.python-guide.org/en/latest/starting/installation/
  [SoftwareCollections.org]: https://www.softwarecollections.org/en/
  [The Hitchhiker's Guide to Python]: http://docs.python-guide.org/en/latest/dev/virtualenvs/