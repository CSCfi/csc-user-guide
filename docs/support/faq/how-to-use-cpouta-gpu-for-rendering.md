# Kuinka käyttää cPouta GPU:ta renderöintiin? {#how-to-use-cpouta-gpu-for-rendering}

Jos sinulle on myönnetty GPU-muotoiluja, voit käyttää GPU:ta renderöintiin. Seuraavat ohjeet osoittavat, kuinka voit perustaa cPouta-etägrafiikkaympäristön. Jos et tarvitse GPU-kiihdytettyä ympäristöä etätyöpöydälle, tässä on ohjeet cPoutan [etätyöpöytäympäristön](how-to-use-cpouta-for-remote-desktop.md) määrittämiseksi. GPU-käyttöön sinun on asennettava X, VNC ja VirtualGL-palvelimet. Kun asennukset on suoritettu, palvelimet pysyvät käynnissä myös silloin, kun poistut SSH-istunnostasi. Palataksesi cPouta-etägrafiikan käyttöön, avaa vain yksi turvallinen SSH-yhteys. Yleinen menettely selitetään, ja annamme joitakin esimerkkejä. Osa tiedoista on saatavilla myös [video-oppaana](https://youtu.be/An1e9ryS3nY).

Ohjeet ovat pääasiassa cPoutan Ubuntu 18 -kuvalle, mutta periaatteet pätevät muihin Linux-jakeluihin. Ubuntu on hyvä valinta, jos uusimpia ominaisuuksia tarvitaan. Lyhyet CentOS-ohjeet ovat myös mukana lopussa. Nämä asennukset ovat minimaalisia. Joidenkin sovellusten asianmukainen toiminta edellyttää lisäpakettien asennusta. Vaikka cPouta CUDA-kuvat voidaan mukauttaa renderöintiin, on suositeltavaa tehdä asennus alusta alkaen.

[TOC]

## Ubuntu-asennus {#ubuntu-installation}

Kun olet käynnistänyt cPouta Ubuntu -kuvan, päivitä pakettien listat, asenna X-palvelin ja Openbox-ikkunahallinta

```
sudo apt-get update
sudo apt-get install xorg openbox
```

_(Ohita seuraava ajurin asennus, jos käytät CUDA-kuvaa.)_ Asenna ensin Linux-ytimeen liittyviä lähteitä, joita tarvitaan NVIDIA-ajurin käännöksen toimimiseksi. Lataa sitten tarpeisiisi parhaiten sopiva NVIDIA-ajuri. Tässä esimerkissä käytetään viimeisintä ajuria 450.51.06. Katso NVIDIA:n verkkosivuilta saatavilla olevat Linux-ajurit (cPoutalla on Tesla P100 -kortteja).

```
sudo apt install build-essential libglvnd-dev pkg-config
sudo wget http://uk.download.nvidia.com/tesla/450.51.06/NVIDIA-Linux-x86_64-450.51.06.run
```

Kun ajat NVIDIA:n asennusskriptin, saat varoituksen siitä, että 32-bittisiä yhteensopivia kirjastoja ei asenneta, mikä on useimmissa tapauksissa ok. Jos kuitenkin tarvitset 32-bittistä tukea, suorita ensin `sudo apt-get install gcc-multilib`

```
sudo sh NVIDIA-Linux-x86_64-450.51.06.run
```

_(Jatka tästä, jos käytät CUDA-kuvaa.)_ Määritä X NVIDIA-ajurille **nvidia-xconfig**-työkalulla. Se selvittää kortin BusID-osoitteen (esimerkissä PCI:0:5:0, vaihda kyselytuloksesi mukaan), jota käytetään X:n konfiguraatiotiedoston luomiseen. Ohita konfiguraatiotiedostoon liittyvä varoitus.

```
nvidia-xconfig --query-gpu-info
sudo nvidia-xconfig --busid=PCI:0:5:0
```

VirtualGL-välikerros tarvitaan graafisen ohjauksen ohjaamiseksi NVIDIA-kortille, ja VNC-palvelin suoratoistaa renderöidyn grafiikan paikalliseen VNC-asiakkaaseesi. Lataa ja asenna VirtualGL ja TurboVNC-palvelimet. (Tarvitset myös VNC-asiakasohjelman paikalliselle tietokoneellesi, katso alta.)

```
wget https://netix.dl.sourceforge.net/project/virtualgl/2.6.4/virtualgl_2.6.4_amd64.deb
wget https://kumisystems.dl.sourceforge.net/project/turbovnc/2.2.5/turbovnc_2.2.5_amd64.deb
sudo dpkg -i virtualgl_*.deb turbovnc_*.deb
```

Määritä VirtualGL-palvelin. Jos olet virtuaalikoneen ainoa käyttäjä, vastaa **Ei** kaikkiin kysymyksiin (valitse: 1,n,n,n,x). Lisätietoja löytyy [virtualgl.org/Documentation/](https://virtualgl.org/Documentation/)

```
sudo vglserver_config
```
Käynnistä cPouta-virtuaalikoneesi uudelleen tässä vaiheessa ennen jatkamista.

Uudelleenkäynnistyksen jälkeen käynnistä VNC-palvelin. Määritä virtuaalisen työpöytäikkunan koko _geometry_-parametrilla. Jos jätät parametrin pois, oletuskoko on 1240x900. Ensimmäisellä kerralla, kun VNC-palvelin käynnistyy, se pyytää luomaan salasanan. Kun sinua pyydetään, kirjoita (enintään) 8 merkin salasana (kahdesti), ja vastaa sitten **Ei** katselu-only-salasanalle. Tarvitset tätä TurboVNC-salasanaa myöhemmin, kun muodostat yhteyden paikallisen tietokoneesi VNC-katseluohjelman kautta. Katso **Käyttö** alla. Lisätietoja on saatavilla osoitteessa [turbovnc.org/Documentation/](https://turbovnc.org/Documentation/)

```
/opt/TurboVNC/bin/vncserver -geometry 1920x1080
```

Käynnistä X-palvelin (sinun on painettava _enter_ kahdesti), ja aseta näyttönumeroksi 0.

```
sudo /usr/bin/X :0 &
export DISPLAY=:0
```

Nyt GPU on valmis käytettäväksi paikallisen VNC-katseluohjelmasi kautta, kuten alla on kuvattu. Sinun on avattava yksi turvallinen SSH-tunneli VNC-yhteydelle. Palvelimet jatkavat käyntiään, kun poistut SSH:sta. Jos käynnistät virtuaalikoneesi uudelleen, aja yllä olevat kolme viimeistä komentoa palvelinten käynnistämiseksi uudelleen.

  
## Käyttö - kuinka käyttää cPouta-etägrafiikkaa {#usage---how-to-use-cpouta-remote-graphics}

Asenna TurboVNC 2.2.5 katseluohjelma paikalliselle työpöytätietokoneellesi [sourceforge.net/projects/turbovnc/files/](https://sourceforge.net/projects/turbovnc/files/)

Avaa salattu SSH-tunneli VNC-yhteydelle tietokoneesi ja virtuaalikoneen (VM) välillä. TurboVNC-palvelimen käyttämä portti näkyy, kun TurboVNC käynnistyy: _TurboVNC started on display **name-of-VM:1**_ (name-of-VM on virtuaalikoneellesi antamasi instanssinimi, ja TurboVNC-palvelin käyttää ensimmäistä vapaata porttia). Paikalliselle tietokoneellesi valitse portti, joka ei ole jo käytössä, esimerkiksi 5911. Kun SSH-tunneli on muodostettu, käynnistä paikallinen TurboVNC-näkymäsi paikallisessa portissa. Katso alla olevat esimerkit (huomaa, että muut jakelut käyttävät *cloud-user*ia oletusnimimerkkinä *ubuntun* sijasta).

**Linux/Mac:**  
täytä _vncviewer_-polku, virtuaalikoneesi ip-numero ja nimi sekä avainparitiedoston sijainti ja nimi. Kirjoita TurboVNC-salasanasi, kun sinua pyydetään.

```
path/vncviewer -via ubuntu@ip-number-of-VM name-of-VM:1 -i path/private-key-file.pem
```

  
**Windows PC, komentokehotteessa:**  
täytä PuTTY-polku (PuTTY tulee TurboVNC:n mukana, ja oletustietuna polku on esitetty esimerkissä), täytä virtuaalikoneesi nimi, sen ip-numero sekä avainparitiedoston sijainti ja nimi

```
"c:\\program files\\turbovnc\\putty.exe" -L 5911:name-of-VM:5901 ubuntu@ip-number-of-VM -i path\\private-key-file.ppk
```

**Windows-tietokoneella käyttäen PuTTY:n graafista käyttöliittymää:**  
kirjoita avainparitiedoston sijainti _Private key file for authentication_ -ruutuun PuTTY-konfigurointiruudun _Auth_-paneelissa. Täytä myös lähde- ja kohdesatamat kategoriassa _Connection_\-_SSH_\-_Tunnels_, _Source port:_ 5911, _Destination:_ name-of-VM:5901 (muista napsauttaa _Add_-painiketta). Tallenna istunto profiili myöhempää käyttöä varten.

Kun SSH-tunneli on muodostettu, avaa TurboVNC-katseluohjelmasi. Kun _New TurboVNC Connection_ -ikkuna avautuu, täytä localhost:11, napsauta _Connect_ ja kirjoita TurboVNC-salasanasi, kun kysytään.

  
**Kaikilla alustoilla:**  
Kun TurboVNC-salasana hyväksytään, tyhjä VNC-ikkuna avautuu. Napsauta hiiren kakkospainikkeella avataksesi terminaalin. Muista **käynnistää sovelluksesi vglrun-komennolla**. Esimerkiksi suorittaaksesi OpenGL-testisovelluksen glxspheres64, kirjoita

```
vglrun /opt/VirtualGL/bin/glxspheres64
```

Kun olet valmis, sulje VNC-ikkuna napsauttamalla _X_ -painiketta joko valikkopalkissa (_Disconnect_) tai oikeassa yläkulmassa olevassa ikkunassa. Älä napsauta hiiren kakkospainikkeella työpöytää ja valitse _exit_, koska tämä sulkee Openbox-ikkunahallinnan (katso **Tunnetut ongelmat** alla).

  
## Hyödyllisiä komentoja {#useful-commands}

Selvitä TurboVNC-palvelimen näyttönumero ja prosessitunnus

```
/opt/TurboVNC/bin/vncserver -list
```

Sulje TurboVNC-palvelin, joka toimii näytöllä 1

```
/opt/TurboVNC/bin/vncserver -kill :1
```

Tarkista, onko X-palvelin käynnissä

```
ps auxw | grep X
```

Pysäytä X-palvelin

```
sudo killall X (CentOS)
sudo killall Xorg (Ubuntu)
```

Selvitä glibc, NVIDIA-ajuriversiot

```
ldd --version
nvidia-smi
```

Poista NVIDIA-ajuri (esimerkiksi 450.51.06)

```
sudo sh NVIDIA-Linux-x86_64-450.51.06.run --uninstall
```

NVIDIA:n ohjetiedosto sijaitsee _/usr/share/doc/NVIDIA_GLX-1.0/README.txt_

## Tunnetut ongelmat {#known-issues}

Jos poistut TurboVNC-katseluohjelman ikkunasta napsauttamalla hiiren kakkospainiketta ja valitset _exit_, Openbox-ikkunahallinta sulkeutuu. Käynnistä Openbox, sulje ja käynnistä TurboVNC-palvelin uudelleen yllä olevan ohjeen mukaisesti.

Jotkin sovellukset vaativat lisäpakettien asennusta toimiakseen oikein. Esimerkiksi Ubuntu-asennuksessa ParaView vaatii ylimääräisen paketin

```
sudo apt-get install libxcb-keysyms1
```

ja CentOS:ssa

```
sudo yum install xcb-util-keysyms
```

## CentOS-asennus {#centos-installation}
----------------------

Kun olet käynnistänyt CentOS-7-kuvan, päivitä pakettien listat, asenna X-palvelin, fontit ja Openbox-ikkunahallinta

```
yum check-update
sudo yum install xorg-x11-xauth xorg-x11-server-Xorg dejavu-sans-fonts xterm openbox
```

Asenna Linux-kernelin lähteet, joita tarvitaan NVIDIA-ajurin käännöksen toimimiseksi

```
sudo yum install kernel-devel-$(uname -r) gcc
```

Lataa NVIDIA-ajurin (esimerkiksi version 450.51.06) asennusskripti

```
sudo wget http://uk.download.nvidia.com/tesla/450.51.06/NVIDIA-Linux-x86_64-450.51.06.run
```

Suorita skripti. Suositellut vastaukset: **Ei** _rekisteröi ytimen moduulin lähteet DKMS:ssä_, ja **Ei** _asentaa NVIDIA:n 32-bittiset yhteensopivat kirjastot_. Ohita varoitukset.

```
sudo sh NVIDIA-Linux-x86_64-450.51.06.run
```

Määritä X NVIDIA-ajurille **nvidia-xconfig**-työkalulla. Se selvittää kortin BusID-osoitteen (esimerkissä PCI:0:5:0, vaihda kyselytuloksesi mukaan), jota käytetään X:n konfiguraatiotiedoston luomiseen (ohita vastaava varoitus).

```
nvidia-xconfig --query-gpu-info
sudo nvidia-xconfig --busid=PCI:0:5:0
```

Lataa VirtualGL ja TurboVNC-repot, ja asenna palvelimet

```
sudo wget --directory-prefix=/etc/yum.repos.d https://virtualgl.org/pmwiki/uploads/Downloads/VirtualGL.repo
sudo wget --directory-prefix=/etc/yum.repos.d https://turbovnc.org/pmwiki/uploads/Downloads/TurboVNC.repo
sudo yum install VirtualGL
sudo yum install turbovnc
```

Määritä VirtualGL-palvelin (suositellut vastaukset: 1,n,n,n,x)

```
sudo /opt/VirtualGL/bin/vglserver_config
```

Käynnistä TurboVNC-palvelin. Se pyytää sinua luomaan salasanan. Kun sinua pyydetään, kirjoita: 8 merkkiä pitkä salasana (kahdesti), vastaa sitten **Ei** _katselu-only-salasanalle_

```
/opt/TurboVNC/bin/vncserver -geometry 1920x1080
```

Muokkaa _.vnc/xstartup.turbovnc_-tiedostoa suosikkieditorillasi. Tiedostossa tulisi olla vain seuraavat kaksi riviä, poista kaikki muut

```
#!/bin/sh
exec openbox-session
```

Sinun täytyy käynnistää TurboVNC-palvelin uudelleen, jotta muutokset astuvat voimaan. Joko käynnistä VM uudelleen tai tapa ja käynnistä TurboVNC uudelleen

```
/opt/TurboVNC/bin/vncserver -kill :1
/opt/TurboVNC/bin/vncserver -geometry 1920x1080
```

Käynnistä X-palvelin näytöllä 0, ja cPouta-etägrafiikka-asennus on valmis.

```
sudo /usr/bin/X :0 &
export DISPLAY=:0
