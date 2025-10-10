# Virtuaalikoneiden levykuvien luominen, muuntaminen, lataaminen ja jakaminen { #creating-converting-uploading-and-sharing-virtual-machine-images }

Tässä artikkelissa kerrotaan, miten levykuvia hallitaan Poutassa.

[TOC]

## Levykuvien luominen { #creating-images }

Uusia virtuaalikoneiden levykuvia voi luoda kahdella tavalla: luomalla kuvan tyhjästä tai käynnistämällä virtuaalikoneen olemassa olevan kuvan perusteella, tekemällä muutokset käynnissä olevaan koneeseen ja tallentamalla muutokset uutena kuvana luomalla tilannevedos (snapshot).

### Levykuvan luominen olemassa olevan kuvan pohjalta { #creating-an-image-based-on-an-existing-image }

Käynnistä virtuaalikone käyttämällä jotakin saatavilla olevista kuvista joko Horizon-verkkokäyttöliittymän kautta tai komentoriviltä.

Instanssin käynnistys komentoriviltä:

```bash
openstack server create --flavor <flavor> \
--image <image uuid> \
--key-name <key name> \
--nic net-id=<name of network> \
--security-group default \
--security-group <additional security group> <name of server>
```

Kirjaudu sisään ja tee tarvittavat muutokset. Johdonmukaisten tilannevedosten varmistamiseksi tilannevedokset tulisi luoda vain sammutetuista instansseista. Sammuta ensin virtuaalikoneesi:

```bash
openstack server stop <name of vm>
```

Luo sitten tilannevedos koneen nykyisestä tilasta:

```bash
openstack server image create --name <name of snapshot to create> <name of vm>
```

Tilannevedoksen luominen kestää hetken. Kun se on valmis, se näkyy uutena kuvana. Jos tarvitset alkuperäistä instanssia, voit käynnistää sen, kun tilannevedos on luotu.

```bash
openstack server start <name of vm>
```

Verkkokäyttöliittymässä kohdassa **Compute | Instances** instanssikohtaiset Create Snapshot -valinnat tekevät saman kuin yllä oleva CLI-komento. Luodut tilannevedokset ilmestyvät osioon **Compute | Images**.

![Tilannevedos-valikko](/img/horizon-snapshot-menu.png)

### Levykuvan luominen tyhjästä { #creating-an-image-from-scratch }

Levykuvien luomiseen tyhjästä on useita työkaluja. Ne voidaan jakaa kahteen ryhmään: työkaluihin, joissa ajetaan käyttöjärjestelmää virtuaalikoneessa kuvan asennusta ja konfigurointia varten, sekä työkaluihin, jotka ottavat peruskuvan ja tekevät siihen muutoksia ilman virtuaalikoneen ajamista. Kutsumme näitä nimillä ”asennuspohjaiset työkalut” ja ”peruskuvapohjaiset työkalut”.

<table> <colgroup> <col style="width: 33%" /> <col style="width: 33%"
/> <col style="width: 33%" /> </colgroup> <thead> <tr class="header">
<th> </th> <th>Asennuspohjaiset työkalut</th> <th>Peruskuvapohjaiset työkalut</th>
</tr> </thead> <tbody> <tr class="odd"> <td>Edut</td> <td><ul>
<li>Helppo käyttää ja ymmärtää</li> <li>Tuttu työnkulku kaikille, jotka tuntevat manuaalisen OS-asennuksen</li> </ul></td> <td><ul>
<li>Nopea</li> <li>Mahdollista automatisoida</li> <li>Tuottaa pieniä kuvia</li> <li>Tuottaa pilviympäristöihin sopivia kuvia ilman lisämuokkauksia</li> </ul></td> </tr> <tr class="even"> <td>Haitat</td>
<td><ul> <li>Hidas</li> <li>Päivitykset hankalia</li> <li>Kuva on tehtävä pilvivalmiiksi alkuasennuksen jälkeen</li>
<li>Tuotetut kuvat voivat olla melko suuria</li> </ul></td> <td><ul>
<li>Kuvien räätälöinti voi olla vaikeaa</li> </ul></td> </tr> <tr
class="odd"> <td>Esimerkkejä</td> <td><a
href="http://linux.die.net/man/1/virt-install">virt-install</a>, <a
href="https://virt-manager.org/">virt-manager</a>, <a
href="https://www.virtualbox.org/">VirtualBox</a></td> <td><a
 href="https://github.com/openstack/diskimage-builder">diskimage-builder</a>,
<a href="http://libguestfs.org/virt-builder.1.html">virt-builder</a></td>
</tr> </tbody> </table>

Yleinen työnkulku asennuspohjaisia työkaluja käytettäessä:

1. Hanki asennusmedia tai verkkoasennuslinkki.
2. Käynnistä virtuaalikone ja ohjaa se asennusmedialle tai verkkoasennuslinkkiin.
3. Suorita asennusohjelma.
      - Tämän vaiheen voi halutessa automatisoida esim. työkalulla [Kickstart].
4. Kun asennus on valmis, sammuta VM ja tee lisämuokkaukset, jotta kuva on valmis pilvikäyttöön.

Yleinen työnkulku peruskuvapohjaisia työkaluja käytettäessä:

1. Räätälöi tarvittaessa konfiguraatiotiedostot, joita käytetään lopullisen kuvan luontiin.
2. Määritä sopivat räätälöintiparametrit.
3. Suorita komento lopullisen kuvan tuottamiseksi.

Lisätietoa levykuvien luonnista löytyy perusteellisesta oppaasta [OpenStack virtual machine image guide]. Katso erityisesti luvut [creating images manually] ja [tool support for creating images].

#### Huomioitavaa levykuvien luonnissa tyhjästä { #caveats-to-keep-in-mind-when-creating-images-from-scratch }

Nämä huomiot koskevat yleensä vain asennuspohjaisia menetelmiä. Peruskuvia käyttävät työkalut on yleensä suunniteltu nimenomaan pilvikuvien luontiin, joten ne hoitavat nämä puolestasi. Jos päätät käyttää asennuspohjaista menetelmää, tutustu erinomaiseen työkaluun [virt-sysprep], joka tekee suurimman osan pilvikäyttöä varten tarvittavista muokkauksista yhdellä komennolla. Tässä luvussa listataan joitakin asioita, jotka on käsiteltävä ennen kuin kuva on valmis pilviympäristöihin.

#### cloud-init { #cloud-init }

Työkalu nimeltä [cloud-init] on asennettava kaikkiin kuviin, joita käytetään Pouta-pilvissä. Sitä käytetään tiettyihin tehtäviin, jotka ajetaan virtuaalikoneen ensimmäisellä käynnistyskerralla, kuten SSH-isäntäavainten luontiin ja käyttäjän julkisten SSH-avainten lisäämiseen.

#### Käyttäjätilit (voi tehdä työkalulla [virt-sysprep]) { #user-accounts-can-be-done-with-virt-sysprep }

Pilvikuvissa tulisi olla vain minimaalinen määrä käyttäjätilejä. Useimmiten niissä tulisi olla vain yksi tavallinen geneerinen käyttäjätili (esim. ”cloud-user” CSC:n oletuskuvissa) ja root-käyttäjä.

#### SSH-isäntäavaimet (voi tehdä työkalulla [virt-sysprep]) { #ssh-host-keys-can-be-done-with-virt-sysprep }

Pilvessä käytettävissä kuvissa ei saa olla valmiiksi SSH-isäntäavaimia, koska niiden mukanaolo tarkoittaisi, että jokaisella kuvasta käynnistetyllä palvelimella olisi SSH:n näkökulmasta sama identiteetti. Tämä on myös tietoturvariski, sillä kuka tahansa kuvatiedostoon käsiksi pääsevä voisi esiintyä miltä tahansa kyseisellä kuvatiedostolla käynnistetyltä palvelimelta. Uudet SSH-isäntäavaimet tulee generoida _cloud-initin_ toimesta (ks. yllä) virtuaalikoneen ensimmäisellä käynnistyskerralla.

#### Verkkoliittymien järjestys (voi tehdä työkalulla [virt-sysprep]) { #network-interface-ordering-can-be-done-with-virt-sysprep }

Linux-ytimen _udev_-laitehallinta kiinnittää tietyn verkkoliittymän nimen tiettyyn MAC-osoitteeseen. Tämä ei ole hyvä, jos samasta kuvasta luodaan useita virtuaalikoneita, koska kaikilla on eri MAC-osoite. Se on huono myös silloin, jos luot tilannevedoksen virtuaalikoneesta ja yrität käyttää sitä uuden koneen käynnistämiseen: tällöin se muistaa vanhan virtuaalikoneen MAC-osoitteen. Paras tapa hoitaa tämä on käyttää _virt-sysprep_-työkalua.

#### Osiointi { #partitioning }

Kun osioit Linux-kuvaa, varmista että juuriosio on ensimmäinen ja ainoa osio. Virtuaalikoneen käynnistysprosessin aikana OpenStack lisää SSH-avaimet ensimmäiselle osiolle hakemiston /root/.ssh alle, mikä tarkoittaa, että tämän osion on oltava juuriosio, ei esim. /boot. Kirjautuminen ei onnistu ilman root-salasanaa, ellei avaimia lisätä oikein.

#### ACPI-daemon { #acpi-daemon }

ACPI-daemonia käytetään vastaanottamaan virtuaalikoneen virranhallintaan liittyviä komentoja. Asenna ACPI-daemon konekuviin, jotta sammutus/uudelleenkäynnistys toimii oikein pilvikäyttöliittymästä.

#### Hotplug { #hotplug }

Jotta voit käyttää levyjä (volumes), sinun on oltava *ACPI hotplug* käytössä. Tämä on oletuksena päällä CentOS 6:ssa ja uudemmissa, mutta Ubuntussa sinun on lisättävä rivi ”*acpiphp*” tiedostoon */etc/modules*. Muissa distroissa tarkista jakelun dokumentaatiosta, miten *acpiphp* ladataan käynnistyksessä.

## Levykuvien muuntaminen { #converting-images }

Kun virtuaalikoneesta otetaan tilannevedos, OpenStack luo kuvan _raw_-muodossa. Nämä kuvat vievät tyypillisesti yhtä monta gigatavua kuin virtuaalikoneen juurilevyn kapasiteetti, riippumatta asiakkaan datan todellisesta määrästä. Seurauksena tilannevedokset voivat nopeasti kuluttaa levykuville varatun tilan.

Ratkaisu tähän on muuntaa tilannevedoksesta saatu kuva kompaktimpaan muotoon, kuten _qcow2_:een, joka tallentaa vain asiakasdatan. Tätä varten ladataan raw-kuva, muunnetaan se qcow2-muotoon ja ladataan uusi kuva takaisin OpenStackiin. Koska raw-kuvat voivat olla hyvin suuria, emme suosittele tämän tekemistä henkilökohtaisella tietokoneella, vaan apuna käytettävässä virtuaalikoneessa Poutassa. Alla esitellään menettely käyttäen väliaikaista virtuaalikonetta.

1. Oletetaan, että olemme juuri ottaneet virtuaalikoneesta tilannevedoksen ja saaneet kuvan _myVmSnapshot_. Ensimmäinen vaihe on luoda väliaikainen virtuaalikone, jota käytämme myVmSnapshotin muuntamiseen. Virtuaalikoneessa on oltava riittävästi tilaa sekä myVmSnapshotille että sen kompaktimmalle versiolle yhtä aikaa. Koska kompakti versio on pienempi tai yhtä suuri kuin myVmSnapshot, varma valinta on ottaa flavor, joka kykenee tallettamaan vähintään kaksinkertaisesti myVmSnapshotin koon. Jos myVmSnapshot on esimerkiksi kooltaan 80 GB, sopiva flavor apuvirtuaalikoneelle on io.160GB, koska siinä on 160 GB efemeeristä tallennustilaa. Käyttöjärjestelmä voi olla esimerkiksi `AlmaLinux-9`.
   ```bash
   openstack server create --flavor <flavor> \
   --image <image uuid> \
   --key-name <key name> \
   --nic net-id=<name of network> \
   --security-group default \
   --security-group <additional security group> snapshotConverter
   ```
   Ainoa lisävaatimus virtuaalikoneen käyttöönotolle on i) julkisen kelluvan IP-osoitteen liittäminen ja ii) SSH:n salliminen, jotta voimme kirjautua koneelle.

2. Kun virtuaalikone on käynnissä, kopioi OpenStack RC File v3 -tiedosto cPouta/ePouta-käyttöä varten virtuaalikoneeseen. Jos sinulla ei vielä ole tätä tiedostoa, katso ohjeet:
   [this guide](install-client.md#configure-your-terminal-environment-for-openstack)
   tiedoston hankkimiseksi.
   ```bash
   scp <project_name_here>-openrc.sh cloud-user@<floating_ip>:/home/cloud-user/
   ```
   Kirjaudu virtuaalikoneelle ja lataa tunnistetietosi tiedostosta.
   ```bash
   source <project_name_here>-openrc.sh
   ```

3. Jotta voimme tallettaa tilannevedoksesta saadun kuvan, efemeerinen tallennustila on alustettava oikein. Katso ohjeet:
   [our guide](ephemeral-storage.md). Tämän vaiheen jälkeen oletamme, että efemeerinen levy on liitetty hakemistoon _/mnt_.
4. Seuraavaksi asennamme tarvittavat perustyökalut.
   ```bash
   sudo yum install python3 python3-virtualenv screen qemu-img
   ```
   Luomme Python 3 -virtuaaliympäristön, jota käytämme cPouta/ePouta-yhteyksiin, ja aktivoimme sen.
   ```bash
   virtualenv-3 env
   source env/bin/activate
   ```
   Asennamme nyt työkalut, joilla keskustelemme cPouta/ePoutan kanssa.
   ```bash
   pip install python-openstackclient==3.11.0 openstacksdk==0.9.17 os-client-config==1.27.0 osc-lib==1.6.0
   ```
5. Seuraavaksi ladataan tilannevedoksesta saatu kuva. Siirry efemeerisen tallennustilan hakemistoon.
   ```bash
   cd /mnt
   ```
   Vaikka se ei ole pakollista, suosittelemme tässä vaiheessa avaamaan _screen_-session, jonka avulla prosessi voi jatkua taustalla ilman, että terminaalia täytyy pitää auki prosessin valmistumiseen asti.
   ```bash
   screen -S converter
   ```
   Annetaan komento tilannevedoksesta saadun kuvan lataamiseksi.
   ```bash
   openstack image save --file myVmSnapshotRaw.raw <id_of_myVmSnapshot>
   ```
   Kuvan koon vuoksi prosessi kestää muutamia minuutteja. Voit poistua screen-sessiosta painamalla CTRL+A ja sen jälkeen CTRL+D. Voit palata sessioon milloin tahansa komennolla:
   ```bash
   screen -r converter
   ```
6. Kun edellinen komento on valmistunut, on aika muuntaa kuva.
   ```bash
   qemu-img convert -f raw -O qcow2 myVmSnapshotRaw.raw myVmSnapshotQcow2.qcow2
   ```
   Kuten aiemmin mainittiin, qcow2-muoto tallentaa vain varsinaisen asiakasdatan sen sijaan, että se kopioisi juurilevyn 1:1. Jos asiakasdatan määrä on huomattavasti pienempi kuin juurilevyn kokonaiskapasiteetti, myös qcow2-kuva on huomattavasti pienempi kuin raw-kuva.

7. Kun muunnos on valmis, uusi kuva voidaan ladata OpenStackiin.
   ```bash
   openstack image create --disk-format qcow2 --file myVmSnapshotQcow2.qcow2 myVmSnapshotCompact 
   ```
   Jos toimenpide onnistuu, raw-muotoinen kuva voidaan poistaa OpenStackista.
   ```bash
   openstack image delete <id_of_myVmSnapshot>
   ```
   Voit säilyttää apuvirtuaalikoneen tulevia muunnoksia varten tai poistaa sen heti käytön jälkeen.
   ```bash
   openstack server delete <id_of_snapshotConverter>
   ```

## Levykuvien lataaminen { #uploading-images }

Levykuvia voi ladata joko verkkokäyttöliittymästä tai _openstack_-komentorivityökalulla.

Ennen lataamista sinun on tiedettävä, missä muodossa ladattava kuva on. Todennäköisimmät vaihtoehdot ovat _qcow2_ ja _raw_. Voit selvittää tyypin _file_-komennolla. Tältä _qcow2_-kuva näyttää:

```bash
$ file images/Ubuntu-15.10-Phoronix.qcow2
images/Ubuntu-15.10-Phoronix.qcow2: Qemu Image, Format: Qcow (v3), 10737418240 bytes
```

Ja tältä _raw_-kuva näyttää:

```bash
$ file images/Ubuntu-14.04-old.raw
images/Ubuntu-14.04-old.raw: x86 boot sector; partition 1: ID=0x83, active, starthead 0, startsector 16065, 20948760 sectors, code offset 0x63
```

Lataus komentoriviltä:

```bash
openstack image create --disk-format <disk format> --private --file <image file to upload> <name of image to create>
```

Tämä lataa kuvan. Ennen kuin kuva on käyttökelpoinen, kestää hetken.

Jos haluat käyttää verkkokäyttöliittymää, voit ladata kuvia kohdassa **Compute | Images** painamalla **Create Image** -painiketta:

![Kuvan lataus](/img/horizon-image-upload2.png)

Näet seuraavan valintaikkunan:

![Kuvan latauksen valintaikkuna](/img/horizon-image-upload-dialog.png)

Tässä esimerkissä luomme kuvan nimeltä _Alpine-linux_. Voit halutessasi lisätä kuvalle **Image Description** -kenttään kuvauksen omaa käyttöä varten. Tietoturvasyistä tuemme kuvien lataamista vain omalta työasemaltasi, eikä julkisten URL-osoitteiden kautta lataaminen ole mahdollista. Tässä esimerkissä olemme siis valinneet paikallisen kuvatiedoston **Browse**-painikkeella. Koska kuvamme on ISO-tyyppinen, olemme valinneet sen **Format**-pudotusvalikosta. Kaikki muut kentät paitsi **Image Sharing | Visibility** voivat jäädä oletusarvoihinsa. **Image Sharing | Visibility** -kohdassa varmista, että asetat kuvan näkyvyydeksi _Private_. Tavalliset käyttäjät eivät voi luoda julkisia kuvia tietoturvasyistä. Jos yrität ladata kuvan ja asettaa näkyvyydeksi _Public_, saat virheilmoituksen. Kun asetat näkyvyydeksi _Private_, ladattu kuva on yksityinen OpenStack-projektillesi, ja vain projektisi jäsenet voivat käyttää sitä.

## Levykuvien jakaminen Pouta-projektien välillä { #sharing-images-between-pouta-projects }

Voit jakaa kuvia eri Pouta-projektien välillä komentorivityökaluilla. Kuvien jakaminen projektien välillä ei tällä hetkellä ole mahdollista Poutan verkkokäyttöliittymässä. Kun kuva on jaettu, se näkyy molemmissa projekteissa eli sekä luovuttajalla että vastaanottajalla.

Huomaa, että jakaminen toimii saman pilviympäristön sisällä: voit jakaa kuvia cPouta-projektista toiseen, mutta et cPouta- ja ePouta-projektien välillä.

1. Hanki ensin jaettavan kuvan UUID (`<your-image-UUID>`). Listaa nykyisen projektin kaikki kuvat komennolla:

    ```sh
    openstack image list
    ```

1. Seuraavaksi tarvitset kohdeprojektin UUID:n (`<destination-project-UUID>`). Voit listata käytettävissä olevat projektisi komennolla:

    ```sh
    openstack project list
    ```

1. Kun sinulla on molemmat UUID:t, varmista ensin, että kuva on **shared**-varianttia, jos se ei sitä jo ole:

    ```bash
    openstack image set --shared <your-image-UUID>
    ```

1. Käynnistä sitten jako suorittamalla seuraava _openstack_-komento lähtöprojektissa:

    ```bash
    openstack image add project <your-image-UUID> <destination-project-UUID>
    ```

1. Lopuksi kohdeprojektin on hyväksyttävä jäsenyys. Tätä varten sinun tai kollegasi tulee suorittaa seuraava glance-komento vastaanottavassa projektissa:

    ```bash
    openstack image set --accept <your-image-UUID>
    ```

[GitHub page]: https://github.com/CSC-IT-Center-for-Science/diskimage-builder-csc-automation
[Kickstart]: https://github.com/rhinstaller/pykickstart/blob/master/docs/kickstart-docs.rst
[OpenStack virtual machine image guide]: http://docs.openstack.org/image-guide/index.html
[creating images manually]: http://docs.openstack.org/image-guide/create-images-manually.html
[tool support for creating images]: http://docs.openstack.org/image-guide/create-images-automatically.html
[virt-sysprep]: http://libguestfs.org/virt-sysprep.1.html
[cloud-init]: https://cloudinit.readthedocs.org/en/latest/
[glance]: https://research.csc.fi/pouta-install-client