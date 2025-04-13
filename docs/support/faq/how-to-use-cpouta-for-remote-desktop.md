# Kuinka käyttää cPoutaa Etätyöpöytänä

Tässä artikkelissa käydään läpi, kuinka etätyöpöytä asetetaan noVNC:llä ja ssh-tunnelilla c- ja ePoutassa ilman GPU:ta. Käytämme noVNC:ä, koska se mahdollistaa työpöydän käyttämisen selaimen kautta, eli paikallisia asennuksia ei tarvita. Jos tarvitset ohjeita GPU-instanssin käyttämisestä renderöintiin, katso [täältä](how-to-use-cpouta-gpu-for-rendering.md): [Kuinka käyttää cPouta GPU:ta renderöintiin](how-to-use-cpouta-gpu-for-rendering.md)

Ensiksi, näytämme, kuinka tarvittavat ohjelmistot asennetaan manuaalisesti. Artikkelin lopussa näytämme, kuinka tämä tehdään automaattisesti luotaessa instanssi (post install skriptit). Jos haluat siirtyä suoraan post install skriptiin, klikkaa [tästä](#jälkiasennusskriptit).

## Valmistelut {#preparations}

Käytämme seuraavia teknologioita asentaaksemme etätyöpöydän:

  - Vakio-maku, esimerkiksi _standard.medium_ 
  - Almalinux-9 kuva (Poudassa heillä on jo epel-repository asennettuna)
  - noVNC, koska se mahdollistaa selaimen käytön perinteisen VNC-asiakasohjelman sijaan työpöydän katseluun
  - tigervnc-server VNC-palvelimena
  - Xfce työpöytäympäristönä
  - ssh-tunnel, jotta VNC-palvelin ei ole avoinna internetille. Tämä on erittäin tärkeää.

### Luo ja käytä instanssiasi etätyöpöydälle {#create-and-access-your-instance-for-remote-desktop}

!!! Varoitus  
    Älä käytä `standard.tiny` makua. Koska tässä maussa on vain 1 Gt RAM-muistia, ei voida asentaa noVNC:tä

1. Käynnistä vakio-maku instanssi Alamlinux-9 kuvalla.
2. Liitä kelluva IP instanssiin.
3. Salli SSH-tulo tietoturvasäännöissä (portti 22).
4. SSH:ssaudu instanssiin tällä komennolla ja luo SSH-tunneli.

```shell
ssh -L2001:localhost:6081 almalinux@SINUN-KELLUVA-IP
```

Tämä toimii ainakin Windows Powershellissä. Jos sinulla ei ole käynnissä SSH-agenttia, sinun pitää myös määrittää SSH-avain:

```shell
ssh -i C:\käyttäjät\paikallinenkäyttäjänimi\.ssh\sinunavain.pem -L2001:localhost:6081 almalinux@SINUN-KELLUVA-IP
```

Huomaa, että portti 2001 on se, jota käytät selaimella myöhemmin.

`-L2001:localhost:6081` tarkoittaa, että pääsemme porttiin 6081 palvelimella tietokoneemme paikallisesta portista 2001. Pidä terminaali auki. SSH-komento on ainoa askel, joka tarvitaan paikallisella tietokoneella.

### Asenna tarvittavat ohjelmistot virtuaalikoneelle {#install-the-required-software-on-the-vm}

Tässä esimerkissä käytämme Xfce:tä Työpöytäympäristönä. Jos haluat käyttää jotain toista työpöytäympäristöä, sinun pitää todennäköisesti muokata vncserver-config-defaults konfiguraatiotiedostoa.

```shell
sudo dnf update
sudo dnf install -y epel-release
sudo dnf groupinstall -y "Xfce" "base-x"
sudo systemctl set-default graphical
sudo reboot
```

Asenna noVNC ja tigervnc vncserverille

```shell
sudo dnf install -y novnc tigervnc-server
```

### Määritä ohjelmistot {#configure-the-software}

Luo uusi käyttäjä nimeltä `vncuser` esimerkiksi.

```shell
sudo adduser vncuser
sudo passwd vncuser
sudo su - vncuser
```

Luo peruskonfiguraatio käyttäjälle `vncuser` etätyöpöydän käyttämiseksi.

```shell
vncpasswd

Password:
Verify:
Would you like to enter a view-only password (y/n)? n
```

Poistu `vncuser` shellistä

```shell
exit
```

Määritä haluamasi resoluutio. 1440x900 on yleinen resoluutio, mutta tätä on testattu toimivan resoluutiolla niin suurella kuin 3840x2160. Tämä voidaan konfiguroida kaikille käyttäjille globaalisti.

```shell
sudo sed -i -e 's/=gnome/=xfce/g' /etc/tigervnc/vncserver-config-defaults
sudo sh -c "cat >> /etc/tigervnc/vncserver-config-defaults" <<EOF
## CONFIGURATION FOR ALL USERS ##
geometry=1440x900
depth=24
localhost=no
EOF
```

Tai jokainen käyttäjä voi omistaa oman konfiguraationsa. Tässä, `vncuser` kanssa

```shell
sudo su - vncuser
cat >> ~/.config/tigervnc/config <<EOF
geometry=1440x900
depth=24
session=xfce
localhost=no
EOF
```

### Käynnistä etätyöpöytäsi {#starting-your-remote-desktop}

Huomaa, että tämän dokumentaation kanssa NoVNC-istunto toimii vain ':1'.

Hyvä käytäntö on käyttää `systemd` palvelua `vncserver` käynnistämiseen. Malli löytyy `/lib/systemd/system` nimeltään `vncserver@.service`. Kopioi se hakemistoon `/etc/systemd/system/vncserver@:1.service`.

```shell
sudo cp /lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@:1.service
```

Määritä `vncuser` näyttöön :1

```shell
sudo sh -c "cat >> /etc/tigervnc/vncserver.users" <<EOF
:1=vncuser
EOF
```

Ota käyttöön ja käynnistä `vncserver` palvelu

```shell
sudo systemctl enable vncserver@:1.service && sudo systemctl start vncserver@:1.service
```

Voit tarkistaa palvelun tilan

```shell
sudo systemctl status vncserver@:1.service
```

Ja se kuuntelee portissa `5901` ja `0.0.0.0` (ei pelkästään localhost `127.0.0.1`)

```shell
ss -tulpn | egrep -i 'vnc|590'
```

Voit aloittaa noVNC-asiakkaan ajamalla

```shell
novnc_server --listen 6081 --vnc localhost:5901
```

Sovelluksen sijainti saattaa vaihdella käyttämäsi Linux-jakelun mukaan. `--listen 6081` tarkoittaa, millä portilla palvelu on saatavilla. `--vnc localhost:5901` tarkoittaa, millä portilla se odottaa vncserverin saavutettavuutta. Voit poistua noVNC-istunnosta painamalla `ctrl+c`.

Sinun pitäisi nyt pystyä kirjautumaan noVNC-istuntoon selaimellasi osoitteessa `http://127.0.0.1:2001/vnc.html`. Huomaa, että porttinumero on sama, jota käytit ssh-komennolla.

## Tärkeää tietoa, jos et halua käyttää ssh-tunnelia {#important-information-if-you-dont-want-to-use-the-ssh-tunnel}

On tietenkin mahdollista käyttää noVNC- tai VNC:tä suoraan internetin kautta, mutta suosittelemme tätä voimakkaasti välttämään. VNC on yksi helpoimmista palveluista käyttää väärin internetissä, ja kysymys ei ole, jos palvelimesi hakkeroidaan, vaan milloin. Jos päätät silti sivuuttaa suosituksemme, varmista vähintään, että lisäät hyvän tietoturvasäännön palvelimeesi, jotta saat palvelimen käyttöön vain IP-osoitteestasi.

## Ota Guacamole käyttöön {#deploy-guacamole}

Guacamole on asiakasvapaaton etätyöpöytäväylä. Se tukee standardiprotokollia, kuten VNC, RDP ja SSH.
Lisätietoa [virallisella sivustolla](https://guacamole.apache.org/)

Voit helposti ottaa guacamolen käyttöön tällä [ansible-skriptillä](https://github.com/trispera/ansible-openstack-guacamole).

Aiemmin otimme käyttöön uuden graafisen palvelimen. `templates/user-mapping.xml.j2` tiedostossa sinun on määritettävä nimi, palvelimen paikallinen osoite ja portti.

Asennuksen jälkeen guacamole on käytettävissä `https://<YOUR_FLOATING_IP>:8080/guacamole`

Se mahdollistaa pääsyn eri koneille `vncserver` yhdestä paikasta.

## Jos haluat käyttää Ubuntua {#if-you-want-to-use-ubuntu}

Kirjoitettaessa `ubuntu-desktop` ja `tigervnc-server` toimivat `Ubuntu-22`:n kanssa. Jos haluat käyttää `Ubuntu-24`:ää, käytä `Xfce` graafiympäristönä.

Seuraavat ovat vaiheet `tigervnc-server`:n asennukseen Ubuntu-22:lle. Vaiheet ovat varsin samanlaiset kuin aiemmin nähty `Almalinux-9`, muutamien paketinnimien ollessa erilaisia.

1. Käynnistä vakio-maku instanssi Ubuntu-22.04 kuvalla.
2. Liitä kelluva IP instanssiin.
3. Salli SSH-tulo tietoturvasäännöissä (portti 22).
4. SSH:ssaudu instanssiin tällä komennolla ja luo SSH-tunneli.

```shell
ssh -L2001:localhost:6081 ubuntu@SINUN-KELLUVA-IP
```

Tämä toimii ainakin Windows Powershellissä. Jos sinulla ei ole käynnissä SSH-agenttia, sinun pitää myös määrittää SSH-avain:

```shell
ssh -i C:\käyttäjät\paikallinenkäyttäjänimi\.ssh\sinunavain.pem -L2001:localhost:6081 ubuntu@SINUN-KELLUVA-IP
```

Huomaa, että portti 2001 on se, jota käytät selaimella myöhemmin.

`-L2001:localhost:6081` tarkoittaa, että pääsemme porttiin 6081 palvelimella tietokoneemme paikallisesta portista 2001. Pidä terminaali auki. SSH-komento on ainoa askel, joka tarvitaan paikallisella tietokoneella.

Tässä esimerkissä käytämme Ubuntu-työpöytää Työpöytäympäristönä. Jos haluat käyttää jotain toista työpöytäympäristöä, sinun pitää todennäköisesti muokata vncserver-config-defaults konfiguraatiotiedostoa.

```shell
sudo apt update && sudo apt upgrade
sudo apt install ubuntu-desktop -y
sudo systemctl set-default graphical
sudo reboot
```

Asenna noVNC ja tigervnc vncserverille

```shell
sudo snap install novnc
sudo apt install -y tigervnc-standalone-server
```

### Määritä ohjelmistot {#configure-the-software}

Luo uusi käyttäjä nimeltä `vncuser` esimerkiksi.

```shell
sudo adduser vncuser
sudo su - vncuser
```

Luo peruskonfiguraatio käyttäjälle `vncuser` etätyöpöydän käyttämiseksi.

```shell
vncpasswd

Password:
Verify:
Would you like to enter a view-only password (y/n)? n
```

Poistu `vncuser` shellistä

```shell
exit
```

Määritä haluamasi resoluutio. 1440x900 on yleinen resoluutio, mutta tätä on testattu toimivan resoluutiolla niin suurella kuin 3840x2160. Tämä voidaan konfiguroida kaikille käyttäjille globaalisti.

```shell
sudo sh -c "cat >> /etc/tigervnc/vncserver-config-defaults" <<EOF
## CONFIGURATION FOR ALL USERS ##
$geometry = "1440x900";
$depth = "24";
$session = "ubuntu";
$localhost = "no";
EOF
```

Tai jokainen käyttäjä voi omistaa oman konfiguraationsa. Tässä, `vncuser` kanssa

```shell
sudo su - vncuser
cat >> ~/.vnc/config <<EOF
$geometry = "1440x900";
$depth = "24";
$session = "ubuntu";
$localhost = "no";
EOF
```

### Käynnistä etätyöpöytäsi {#starting-your-remote-desktop}

Huomaa, että tämän dokumentaation kanssa NoVNC-istunto toimii vain ':1'.

Hyvä käytäntö on käyttää `systemd` palvelua `vncserver` käynnistämiseen. Malli löytyy `/lib/systemd/system` nimeltään `tigervncserver@.service`. Kopioi se hakemistoon `/etc/systemd/system/tigervncserver@:1.service`.

```shell
sudo cp /lib/systemd/system/tigervncserver@.service /etc/systemd/system/tigervncserver@:1.service
```

Määritä `vncuser` näyttöön :1

```shell
sudo sh -c "cat >> /etc/tigervnc/vncserver.users" <<EOF
:1=vncuser
EOF
```

Ota käyttöön ja käynnistä `vncserver` palvelu

```shell
sudo systemctl enable tigervncserver@:1.service && sudo systemctl start tigervncserver@:1.service
```

Voit tarkistaa palvelun tilan

```shell
sudo systemctl status tigervncserver@:1.service
```

Ja se kuuntelee portissa `5901` ja `0.0.0.0` (ei pelkästään localhost `127.0.0.1`)

```shell
ss -tulpn | egrep -i 'vnc|590'
```

Voit aloittaa noVNC-asiakkaan ajamalla

```shell
novnc --listen 6081 --vnc localhost:5901
```

Sovelluksen sijainti saattaa vaihdella käyttämäsi Linux-jakelun mukaan. `--listen 6081` tarkoittaa, millä portilla palvelu on saatavilla. `--vnc localhost:5901` tarkoittaa, millä portilla se odottaa vncserverin saavutettavuutta. Voit poistua noVNC-istunnosta painamalla `ctrl+c`.

Sinun pitäisi nyt pystyä kirjautumaan noVNC-istuntoon selaimellasi osoitteessa `http://127.0.0.1:2001/vnc.html`. Huomaa, että porttinumero on sama, jota käytit ssh-komennolla.

## Jälkiasennusskriptit {#post-install-scripts}

Kun luot instanssin cPoutassa, on mahdollista lisätä `Jälkikäsittely` vaihe.

Se mahdollistaa automaattisten tehtävien suorittamisen ohjelmistojen asentamiseen ja/tai päivitysten suorittamiseen.

![laite jälkikäsittely](img/post-creation-pouta.png)

Sinulla on valittavana `Suora Syöttö`, mikä tarkoittaa, että sinun tulee kirjoittaa komennot tai `Tiedosto`, mikä tarkoittaa, että voit ladata bash-skriptin tai [cloud-init](https://docs.cloud-init.io/en/latest/index.html) skriptin.

Täältä löydät kaksi skriptiä käyttäen `cloud-init`:ia. Yksi `AlmaLinux`:ille ja yksi `Ubuntu`:lle:

`init_vnc_almalinux.yaml`:

```yaml
#cloud-config
#
# Edellä oleva ensimmäinen rivi osoittaa, että tiedosto on Cloud-Init konfiguraatiotiedosto. Älä poista sitä

# Päivitä pakettien luettelo
package_update: true

# Päivitä kaikki asennetut paketit uusimpiin versioihin
package_upgrade: true

# Asennettavien pakettien luettelo
packages:
  - epel-release

runcmd:
  - dnf install -y tigervnc-server novnc
  - dnf groupinstall -y "Xfce" "base-x"
  - systemctl set-default graphical
  - cp /lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@:1.service
  - systemctl enable vncserver@:1.service

users:
  - default
  - vncuser

write_files:
  - content: |
      ## CONFIGURATION FOR ALL USERS ##
      geometry=1440x900
      depth=24
      session=xfce
      localhost=no
    path: /etc/tigervnc/vncserver-config-defaults
    append: true
  - content: |
      :1=vncuser
    path: /etc/tigervnc/vncserver.users
    append: true

final_message: |
  init_vnc_almalinux has finished
  version: $version
  timestamp: $timestamp
  datasource: $datasource
  uptime: $uptime

power_state:
  mode: reboot
  message: rebooting machine
```

`init_vnc_ubuntu.yaml`:

```yaml
#cloud-config
#
# Edellä oleva ensimmäinen rivi osoittaa, että tiedosto on Cloud-Init konfiguraatiotiedosto. Älä poista sitä

# Päivitä pakettien luettelo
package_update: true

# Päivitä kaikki asennetut paketit uusimpiin versioihin
package_upgrade: true

# Asennettavien pakettien luettelo
packages:
  - ubuntu-desktop
  - tigervnc-standalone-server
  - snap:
    - novnc

users:
  - default
  - vncuser

write_files:
  - content: |
      ## CONFIGURATION FOR ALL USERS ##
      $geometry = "1440x900";
      $depth = "24";
      $session = "ubuntu";
      $localhost = "no";
    path: /etc/tigervnc/vncserver-config-defaults
    append: true
  - content: |
      :1=vncuser
    path: /etc/tigervnc/vncserver.users
    append: true

runcmd:
  - systemctl set-default graphical
  - cp /lib/systemd/system/tigervncserver@.service /etc/systemd/system/tigervncserver@:1.service
  - systemctl enable tigervncserver@:1.service

final_message: |
  init_vnc_ubuntu has finished
  version: $version
  timestamp: $timestamp
  datasource: $datasource
  uptime: $uptime

power_state:
  mode: reboot
  message: rebooting machine
```

Suosittelemme tallentamaan nämä skriptit yaml-tiedostoon ja käyttämään **Tiedosto** Jälkikäsittely-valikosta.

Koneen asennuksen jälkeen sinun on yhä luotava vnc-salasana. Yhdistä koneeseesi SSH:n kautta 
(`ssh -L2001:localhost:6081 {ubuntu | almalinux}@{YOUR-FLOATING-IP}`) ja suorita seuraavat komennot:

AlmaLinuxille:

```sh
$ sudo su - vncuser
$ vncpasswd

Password:
Verify:
Would you like to enter a view-only password (y/n)? n

$ exit
$ sudo systemctl start vncserver@:1.service
```

Ubuntulle:

```sh
$ sudo su - vncuser
$ vncpasswd

Password:
Verify:
Would you like to enter a view-only password (y/n)? n

$ exit
$ sudo systemctl start tigervncserver@:1.service
```

Kun palvelu on käynnissä, voit ajaa `novnc`:

Almalinuxille:

```sh
novnc_server --listen 6081 --vnc localhost:5901
```

Ubuntulle:

```sh
novnc --listen 6081 --vnc localhost:5901
```

ja kirjautua noVNC-istuntoon osoitteessa `http://127.0.0.1:2001/vnc.html` käyttämällä aiemmin määrittämääsi `vncpasswd`-salaa.