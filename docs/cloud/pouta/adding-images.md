# Virtuaalisten konekuvien luominen, muuntaminen, lataaminen ja jakaminen {#creating-converting-uploading-and-sharing-virtual-machine-images}

Tässä artikkelissa kerrotaan, miten hallitset kuvia Poutassa.

[TOC]

## Kuvien luominen {#creating-images}

Uusien virtuaalisten konekuvien luomiseen on kaksi erilaista vaihtoehtoa: kuvan luominen alusta tai virtuaalikoneen käynnistäminen olemassa olevan kuvan pohjalta, käynnissä olevan koneen muutosten tekeminen ja muutosten tallentaminen uutena kuvana luomalla tilannevedos.

### Kuvan luominen olemassa olevan kuvan pohjalta {#creating-an-image-based-on-an-existing-image}

Käynnistä virtuaalikone jollakin saatavilla olevista kuvista joko Horizonin verkkokäyttöliittymän kautta tai komennorivikäyttöliittymän avulla.

Instanssin käynnistäminen komentoriviltä:

```bash
openstack server create --flavor <flavor> \
--image <image uuid> \
--key-name <key name> \
--nic net-id=<name of network> \
--security-group default \
--security-group <additional security group> <name of server>
```

Kirjaudu sisään ja tee tarvittavat muutokset. Varmistaaksesi yhtenäiset tilannevedokset, ne tulisi luoda vain sammutetuista instansseista. Sammuta ensin instanssisi:

```bash
openstack server stop <name of vm>
```

Luo sitten tilannevedos koneen nykyisestä tilasta:

```bash
openstack server image create --name <name of snapshot to create> <name of vm>
```

Tilannevedoksen luomisessa kestää jonkin aikaa. Kun se on valmis, se näkyy uutena kuvana. Jos tarvitset alkuperäisen instanssin, voit käynnistää sen tilannevedoksen luomisen jälkeen.

```bash
openstack server start <name of vm>
```

Verkkokäyttöliittymässä kohdassa **Compute | Instances**, instanssikohtaiset Create Snapshot -valikot toimivat samalla tavalla kuin yllä oleva CLI-komento. Luodut tilannevedokset näkyvät kohdassa **Compute | Images**.

![Snapshot menu](/img/horizon-snapshot-menu.png)

### Kuvan luominen alusta {#creating-an-image-from-scratch}

On olemassa useita työkaluja kuvien luomiseen alusta. Nämä työkalut voidaan jakaa työkaluihin, jotka liittyvät käyttöjärjestelmän ajamiseen virtuaalikoneessa kuvan asentamiseksi, ja työkaluihin, jotka tekevät muutoksia peruskuvaan ilman virtuaalikoneen ajamista. Kutsumme näitä "asennuspohjaisiksi työkaluiksi" ja "peruskuvatyökaluiksi".

<table> <colgroup> <col style="width: 33%" /> <col style="width: 33%"
/> <col style="width: 33%" /> </colgroup> <thead> <tr class="header">
<th> </th> <th>Asennuspohjaiset työkalut</th> <th>Peruskuvatyökalut</th>
</tr> </thead> <tbody> <tr class="odd"> <td>Edut</td> <td><ul>
<li>Helppo käyttää ja ymmärtää</li> <li>Tuttu työnkulku kaikille, jotka tuntevat manuaalisen käyttöjärjestelmän asennuksen</li> </ul></td> <td><ul>
<li>Nopea</li> <li>Mahdollisuus automatisoida</li> <li>Tuottaa pieniä kuvia</li> <li>Tuottaa pilville sopivia kuvia ilman muutoksia</li> </ul></td> </tr> <tr class="even"> <td>Haitat</td>
<td><ul> <li>Hidas</li> <li>Päivitykset ovat hankalia</li> <li>On huolehdittava, että kuvat ovat pilvi-kelpoisia alustavan asennuksen jälkeen</li>
<li>Tuotetut kuvat voivat olla melko suuria</li> </ul></td> <td><ul>
<li>Voi olla vaikea mukauttaa kuvia</li> </ul></td> </tr> <tr
class="odd"> <td>Esimerkkejä</td> <td><a
href="http://linux.die.net/man/1/virt-install">virt-install</a>, <a
href="https://virt-manager.org/">virt-manager</a>, <a
href="https://www.virtualbox.org/">VirtualBox</a></td> <td><a
 href="https://github.com/openstack/diskimage-builder">diskimage-builder</a>,
<a href="http://libguestfs.org/virt-builder.1.html">virt-builder</a></td>
</tr> </tbody> </table>

Yleinen työnkulku asennuspohjaisia työkaluja käytettäessä:

1. Hanki asennusmedia tai verkkoinstallaatiolinkki.
2. Käynnistä virtuaalikone ja osoita se asennusmediaan tai verkkoinstallaatiolinkkiin.
3. Käy läpi asennusohjelma.
      - Tämä vaihe voidaan tarvittaessa automatisoida esimerkiksi [Kickstart]-työkaluilla.
4. Kun asennus on valmis, sammuta virtuaalikone ja käytä lisätyökaluja kuvan valmisteluun pilvikäyttöön.

Yleinen työnkulku peruskuvatyökaluja käytettäessä:

1. Mukauta tarvittaessa asetustiedostoja, joita käytetään lopullisen kuvan luomiseen.
2. Määritä sopivat mukautusparametrit.
3. Suorita komento lopullisen kuvan tuottamiseksi.

Saat lisätietoa kuvien luomisesta erittäin kattavasta [OpenStackin virtuaalikonekuvien oppaasta]. Erityisesti katso luvut [kuvien luominen manuaalisesti] ja [työkalujen tuki kuvien luomiselle].

#### Huomioitavaa alusta alkaen kuvia luotaessa {#caveats-to-keep-in-mind-when-creating-images-from-scratch}

Nämä varoitukset on yleensä otettava huomioon vain käytettäessä asennuspohjaisia kuvanluontimenetelmiä. Peruskuvia käyttävät työkalut on yleensä erityisesti suunniteltu luomaan pilvikuvia, joten ne huolehtivat näistä varoituksista puolestasi. Jos päätät käyttää asennuspohjaista menetelmää kuvan luontiin, sinun kannattaa harkita [virt-sysprep]-työkalua, joka huolehtii useimmista pilvikäyttöä varten tarvittavista muutoksista yhdellä komentorivikomennolla. Tässä luvussa luetellaan joitakin varoituksia, jotka on käsiteltävä ennen kuvan valmiutta pilville.

#### cloud-init {#cloud-init}

On olemassa [cloud-init]-niminen työkalu, joka on asennettava kaikkiin kuviin, joita käytetään Pouta-pilvissä. Tätä työkalua käytetään tiettyihin tehtäviin, jotka on suoritettava, kun virtuaalikone käynnistyy ensimmäisen kerran, kuten **SSH-isäntäavainten luominen ja käyttäjän SSH-julkisten avainten lisääminen.**

#### Käyttäjätilit (voidaan tehdä [virt-sysprep]) {#user-accounts}

Pilvikuvissa pitäisi olla vain minimaalinen joukko käyttäjätilejä. Todennäköisesti niissä pitäisi olla vain yksi tavallinen geneerinen käyttäjätili (esim. "cloud-user" CSC:n tarjoamilla oletuskuvilla) ja pääkäyttäjän tili.

#### SSH-isäntäavaimet (voidaan tehdä [virt-sysprep]) {#ssh-host-keys}

Pilvissä käytettävissä kuvissa ei saa olla SSH-isäntäavaimia, sillä niiden olemassaolo kuvassa tarkoittaisi, että jokaisella kuvan avulla luodulla palvelimella olisi sama identiteetti SSH:n näkökulmasta. Tämä on myös turvallisuusriski, sillä kuka tahansa, jolla on pääsy kuvafileeseen, voisi esittää mitä tahansa kuvan avulla käynnistettyä palvelinta. Uudet SSH-isäntäavaimet on luotava _cloud-init_:n avulla (katso yllä) heti, kun virtuaalikone käynnistetään ensimmäisen kerran.

#### Verkkoliitännän tila (voidaan tehdä [virt-sysprep]) {#network-interface-ordering}

Linux-ytimen _udev_-laitteenhallinnalla on toiminto, joka kiinnittää tietyn verkkoliitännän nimen tiettyyn MAC-osoitteeseen. Tämä ei ole hyvä, jos samassa verkossa halutaan luoda useita virtuaalikoneita kuvan perusteella, sillä kaikilla virtuaalikoneilla on eri MAC-osoitteet. Tämä ei myöskään ole hyvä idea, jos luot tilannevedoksen virtuaalikoneesta ja yrität käyttää tilannevedosta uuden virtuaalikoneen käynnistämiseen, sillä tilannevedos muistaa vanhan virtuaalikoneen MAC-osoitteen, jota käytettiin tilannevedoksen luomiseen. Paras tapa tehdä tämä on käyttää _virt-sysprep_-työkalua.

#### Partitiointi {#partitioning}

Kun partitoit Linux-kuvaa, sinun pitäisi varmistaa, että juuripartitio on ensimmäinen ja ainoa partitiokansio. Virtuaalikoneen käynnistysprosessin aikana OpenStack lisää SSH-avaimet ensimmäiseen partitiokansioon /root/.ssh-hakemistoon, mikä tarkoittaa, että tämän partitiokansio on oltava juuripartitio eikä esimerkiksi /boot. Kirjautuminen ei ole mahdollista ilman pääkäyttäjän salasanaa, ellei avaimia ole asetettu oikein.

#### ACPI-daemon {#acpi-daemon}

ACPI-daemonilla vastaanotetaan virtuaalikoneen virtajärjestelmän hallintaan liittyviä komentoja. Sinun pitäisi asentaa ACPI-daemon konekuville, jotta ne voidaan sammuttaa/käynnistää uudelleen oikein pilviliittymästä.

#### Hotplug {#hotplug}

Jotta tilavuuksia voitaisiin käyttää, sinun pitäisi käyttää *ACPI hotplug* -ominaisuutta. Tämä on oletusarvoisesti kytketty päälle CentOS 6:ssa ja uudemmissa versioissa, mutta Ubuntussa sinun on lisättävä rivi "*acpiphp*" tiedostoon */etc/modules*. Muiden jakelujen osalta tarkista, miten ladata *acpiphp* käynnistyksen aikana jakelun asiakirjoista.

## Kuvien muuntaminen {#converting-images}

Kun teet tilannevedoksen virtuaalikoneesta, OpenStack luo kuvan _raw_-muodossa. Nämä kuvat vievät yleensä niin monta gigatavua kuin virtuaalikoneen juurilevyllä on kapasiteettia riippumatta siitä, kuinka monta gigatavua asiakas tosiasiallisesti käyttää. Tämän seurauksena tilannevedosten ottaminen voi nopeasti tyhjentää kuva-alueelle käytettävissä olevan tilan.

Ratkaisu tähän ongelmaan on muuntaa tilannevedoksesta saatu kuva tiiviimpiin muotoihin, kuten _qcow2_, joka tallentaa vain asiakkaan tiedot. Tätä varten ladataan raakakuva, muutetaan se qcow2-muotoon ja ladataan vastasaadut kuvat OpenStackiin. Koska raakakuvat voivat viedä monia gigatavuja, emme suosittele suorittamaan tätä toimintoa henkilökohtaisella tietokoneella, vaan käytämme sen sijaan apuna olevaa virtuaalikonetta Poutassa. Seuraavassa esitetään menettelytapa väliaikaisen virtuaalikoneen avulla.

1. Oletamme, että olemme juuri tehneet tilannevedoksen virtuaalikoneesta ja olemme näin ollen saaneet kuvan _myVmSnapshot_. Ensimmäinen vaihe on luoda väliaikainen virtuaalikone, jota käytämme myVmSnapshotin muuntamiseen. Virtuaalikoneella pitäisi olla tarpeeksi tilaa isännöidä myVmSnapshotia ja sen tiivistettyä versiota samanaikaisesti. Koska tiivistetty versio on pienempi tai yhtä suuri kuin myVmSnapshot, varma valinta on valita maku, joka pystyy hallitsemaan kahdesti myVmSnapshotin koon. Esimerkiksi, jos myVmSnapshotilla on koko 80GB, sopiva virtuaalikoneen maku on io.160GB, koska siinä on 160 GB tilapäistä tallennustilaa. Käyttöjärjestelmä voi olla esimerkiksi CentOS-7.
   ```bash
   openstack server create --flavor <flavor> \
   --image <image uuid> \
   --key-name <key name> \
   --nic net-id=<name of network> \
   --security-group default \
   --security-group <additional security group> snapshotConverter
   ```
   Virtuaalikoneen perustamiseen liittyvät lisävaatimukset ovat i) julkisen kelluvan IP-osoitteen ja ii) SSH-yhteyden mahdollistaminen, jotta voimme tosiasiallisesti kirjautua virtuaalikoneeseen.

2. Kun virtuaalikone on käynnissä, kopioimme OpenStack RC File v3-tiedoston cPouta/ePouta-laitteeseen virtuaalikoneeseen. Jos sinulla ei ole vielä tällaista tiedostoa, katso
   [tämä opas](install-client.md#configure-your-terminal-environment-for-openstack) saadaksesi kopion.
   ```bash
   scp <project_name_here>-openrc.sh cloud-user@<floating_ip>:/home/cloud-user/
   ```
   Kirjaudu virtuaalikoneeseen ja käytä tiedostoa tunnistetietojesi lataamiseksi.
   ```bash
   source <project_name_here>-openrc.sh
   ```

3. Jotta vois ⚙️ thesaurus_register{DEFINITION}   no translation.

a
  
  The modification of option in v1.09 is not just about the output, the default will use the same output_pc but the FPU with a same epsilon goes parallel kro.

  We general set up the path on disk images on the RPI guide, but the biggest advantage it has (unsurprisingly), will be due out of ebcdic .   char rewrite(spokorris) as goth moederene.
   
 tää koskee   nice size mutex
metainokju LTD

>$$ 

+9 

&R

>successfully delete the test image 

--

http://fileos.csc.fi/

socket_path=$KAKL

NAT features the operative g.down# is deadspacekr
ZEN-ALTOS 

>sin (version 5 or 9.8)
     <$APT gitosstract    

> IP!!
-1 > o ny$$nché=print wot+wi,

addtoreal$$$$@FUS ##clone <> sop und
    shows        
        @aws-03-w-glide>20279-^^@wl-break~
          $web-p



          
            .

             cob>          (scrollssffeet)
           
orne /run/kif coded
reset.define({
                                                
                                    apis: [["cp-set-open", 1, 2]]
                                                
                                           }

