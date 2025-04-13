
# Kuinka käyttää hakemistoja Puhtissa ja Mahtissa cPoudasta? {#how-to-access-directories-in-puhti-and-mahti-from-cpouta}

CSC:n laskentapalvelimien (Puhti ja Mahti) tallennusympäristöt eivät ole
suoraan käytettävissä cPoudasta, koska HPC-järjestelmien verkko on eristetty
cPoudasta turvallisuus- ja suorituskykysyistä.

Normaalisti suositeltu tapa siirtää tietoa cPoudan ja CSC:n laskentapalvelimien
välillä on käyttää Allasta. Jos kuitenkin tarvitset suorapääsyn tietoihisi
HPC-palvelimilla, voit käyttää `sshfs`:ää luomaan väliaikaisia etäasennuksia
henkilökohtaisille hakemistoillesi Puhtissa tai Mahtissa.

Esimerkiksi, jos käyttäjä `kkayttaj` haluaisi liittää oman pikakansion
(`/scratch/project_2012345`) Puhtista Ubuntu-pohjaiseen virtuaalikoneeseen
cPoudassa, hänen täytyy ensin asentaa `sshfs` virtuaalikoneeseen:

```bash
sudo apt install sshfs
```

CentOS-koneissa vastaava komento on:

```text
sudo yum install sshfs
```

Tämän jälkeen luodaan tyhjä kansio, jota käytetään liitoskohteena:

```bash
mkdir puhti_scratch
```

Jotta voit muodostaa yhteyden Puhtiin ja Mahtiin SSH-asiakkaan avulla, sinun
on määritettävä SSH-avaimet paikalliselle työasemallesi ja rekisteröitävä
julkinen avaimi MyCSC:ssä. Lisäksi, jotta paikalliset SSH-avaimet ovat
saatavilla myös cPoudassa olevassa virtuaalikoneessasi, sinun täytyy ottaa
käyttöön SSH-agentin edelleenlähetys paikallisella koneellasi. Lue ohjeet:

* [Kuinka määrittää SSH-avaimet](../../computing/connecting/ssh-keys.md)
* [Kuinka ottaa käyttöön SSH-agentin edelleenlähetys](../../computing/connecting/ssh-unix.md#authentication-agent)

Kun SSH-avaimet ovat määritetty, julkinen avain rekisteröity MyCSC:ssä ja
SSH-agentin edelleenlähetys on konfiguroitu paikalliselle työasemalle, etäkohteen
hakemiston liittäminen Puhtissa voidaan suorittaa cPoudan virtuaalikoneessa
komennolla:

```bash
sshfs kkayttaj@puhti.csc.fi:/scratch/project_2012345 ./puhti_scratch
```

Tässä sinun tulisi korvata `/scratch/project_2012345`
oman projektisi pikahakemistolla.

Tämän jälkeen `puhti_scratch`-hakemisto näyttää Puhtin pikakansiosi sisällön
ja sitä voidaan käyttää kuin mitä tahansa liitettyä hakemistoa. Kuitenkin, etäasennettujen
hakemistojen I/O-suorituskyky ei ole yhtä hyvä kuin paikallisesti
liitettyjen hakemistojen. Tämän vuoksi, I/O-vaativissa tehtävissä saattaa olla
järkevämpää kopioida data virtuaalikoneen paikallisille levyille. Työkalut kuten
[`scp`](../../data/moving/scp.md) ja
[`rsync`](../../data/moving/rsync.md) voidaan käyttää tähän.

Poistaaksesi _**liitännän**_; tiedostojärjestelmästä, anna komento:

```bash
fusermount -u mountpoint
```

Esimerkiksi yllä luotu etäliitäntä poistettaisiin komennolla:

```bash
fusermount -u puhti_scratch
```

Katso myös [Etälevyjen liitännät](../../data/moving/disk_mount.md).
