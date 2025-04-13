# QEMU:n virtuaalikuvat cPoutassa

[QEMU](https://www.qemu.org/docs/master/about/index.html) on vankka avoimen lähdekoodin koneemulaattori ja virtualisoija. Se mahdollistaa käyttöjärjestelmien ja sovellusten suorittamisen, jotka on tarkoitettu yhdelle koneelle, täysin eri alustalla. Tämä työkalu on keskeinen osa erilaisia virtualisointikehyksiä. Merkittävästi sitä käytetään OpenStack-pilvi-infrastruktuurissa.

## 1. Varmuuskopion tai tilannevedoksen lataaminen {#downloading-a-backup-or-snapshot}

Varmuuskopion tai tilannevedoksen kuvan lataaminen cPoutasta paikalliselle tietokoneellesi. Tämän saavuttamiseksi sinun tulee olla OpenStack-komentoriviasiakasohjelma (`openstack`). Aja openrc-käsikirjoitustiedostosi konfiguroidaksesi tarvittavat ympäristömuuttujat tunnistautumista varten. Jos sinulla ei ole tätä tiedostoa, voit ladata sen verkkokäyttöliittymästä [UI](https://pouta.csc.fi/). Lisätietoja saat kohdasta [Asenna asiakastyökalut pipin avulla](install-client.md) ja [Määritä terminaaliympäristösi OpenStackia varten](install-client.md).

Esimerkiksi Debian/Ubuntu-pohjaisessa järjestelmässä voit asentaa ne seuraavasti:

```bash
sudo apt-get install python3-openstackclient 
```
Aja openrc-käsikirjoitustiedosto:

```bash
source <project_name_here>-openrc.sh
```

Sinua pyydetään syöttämään salasanasi. Katso [Asenna OpenStack-asiakas](install-client.md) muille käyttöjärjestelmille.

Listaa kuvat/tilannevedokset mukaan lukien levyformaatti, jotka ovat saatavilla OpenStack-projektissasi:

```bash
openstack image list --long
```

Merkitse ylös kuvan ID, jonka haluat ladata.

Nyt, lataa kuva paikalliselle koneellesi:

```bash
openstack image save --file LOCAL_IMAGE_FILENAME.qcow2 IMAGE_ID
```

Korvaa `LOCAL_IMAGE_FILENAME.qcow2` haluamallasi paikallisella tiedostonimellä, levyformaatilla ja `IMAGE_ID` ID:llä.

## 2. Ladatun varmuuskopion tai tilannevedoksen tiedostomuotojen ymmärtäminen {#understanding-file-formats-of-the-downloaded-backup-or-snapshot}

Kun lataat virtuaalikoneesi (VM) varmuuskopion tai tilannevedoksen cPoutasta, ladatun kuvan tiedostomuoto voi olla joko raw tai qcow2. QEMU-emulaattori tukee useita levyformaatteja, mukaan lukien raw, vdi, ja qcow2. Katso [OpenStackin levyn ja kontin formaatit](https://docs.openstack.org/glance/stein/user/formats.html) saadaksesi lisää tietoa.

- **QCOW2 (QEMU Copy On Write)**: Tämä on yleisin ja oletusformaatti OpenStack-kuville, erityisesti kun QEMU:ta käytetään.
- **RAW**: Raaka levynkuvamuoto. Se on yleensä kooltaan suurempi kuin QCOW2-kuvat.
- **VDI (Virtual Disk Image)**: Tämä formaatti liittyy pääasiassa VirtualBoxiin, mutta sitä voidaan käyttää myös OpenStackin kanssa.

Seuraava komento kertoo sinulle kuvan formaatin, mikäli sinulla on `qemu-img` työkalu asennettuna. Katso [QEMU-asennus](https://www.qemu.org/download/#linux) saadaksesi lisää tietoa.

```bash
qemu-img info /path/to/your/image
```

## 3. VM-levykuvien muuntaminen QCOW2-muotoon QEMU:n avulla {#converting-vm-image-disk-formats-to-qcow2-with-qemu}

Jos sinulla ei ole QCOW2-kuvaa mutta sinulla on VM-levy toisessa formaatissa, voit muuntaa sen QCOW2-muotoon käyttämällä QEMU:n `qemu-img` työkalua. Seuraava komento muuntaa VM-levysi QCOW2-muotoon:

```bash
qemu-img convert -f [source_format] -O qcow2 [source_image] [destination_image.qcow2]
```

Missä:

- `[source_format]`: Lähdekuvan formaatti (esim., `raw`, `vdi`, `vmdk`, `vhdx`).
- `[source_image]`: Lähteen VM-levyn polku.
- `[destination_image.qcow2]`: Polku, johon haluat tallentaa muunnetun QCOW2-kuvan.

Esimerkiksi, muuntaaksesi `testCentOS.raw` ladatun kuvan QCOW2-muotoon QEMU:n avulla, hanki ensin kuvan tiedot ja muunna sitten seuraavasti:

```bash
qemu-img info testCentOS.raw

image: testCentOS.raw
file format: raw
virtual size: 2.97 GiB (3184721920 bytes)
disk size: 2.97 GiB
```

```bash
qemu-img convert -f raw -O qcow2 testCentOS.raw testCentOS.qcow2
```

Kun muuntaminen on valmis, voit tarkistaa muunnetun kuvan tiedot seuraavalla komennolla:

```bash
qemu-img info testCentOS.qcow2
```

## 4. Ladattujen varmuuskopio- tai tilannevedoskuvien suorittaminen paikallisesti QEMU:lla {#running-downloaded-backup-or-snapshot-images-locally-with-qemu}

Ladattu varmuuskopio tai tilannevedoskuva cPoutasta, joka on tyypillisesti `raw`-formaatissa. Ennen kuin suoritat sen QEMU:lla, on olennaista muuntaa tämä kuva `qcow2`-muotoon. Viittaa aiempaan osioon muodon muuntamisesta ja vahvistamisesta. Ennen kuin ajat virtuaalikoneen paikallisesti, varmista, että `cloud-utils` ja `qemu-kvm` paketit on asennettu. Vaiheittainen opas on seuraava:

!!! Varoitus  
    cPoutasta lataamasi kuva tarvitsee cloud-init-ohjelman ja vaatii muokkauksia toimiakseen kunnolla paikallisesti. Saattaa olla, että ladattu kuva vaatii kokoonpanomuutoksia paikallisessa verkkoasetuksessa.

- Asenna tarvittavat paketit.
    
    RHEL- tai CentOS 8 -järjestelmälle:

    ```bash
    sudo dnf install cloud-utils
    ```

    Debian/Ubuntu-pohjaiselle järjestelmälle:

    ```bash
    sudo apt-get install cloud-image-utils
    ```

- Valmistele cloud-init-kokoonpano.

    Luo tiedosto nimeltä `cloud-config.yaml` seuraavalla sisällöllä:

    ```yaml
    #cloud-config
    ssh_authorized_keys:
    - YOUR_SSH_PUBLIC_KEY
    ```

    Korvaa `YOUR_SSH_PUBLIC_KEY` SSH-julkisen avaimen sisältösi kanssa (`~/.ssh/id_rsa.pub`). Esimerkiksi:

    ```yaml
    #cloud-config
    ssh_authorized_keys:
    - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQ... your.email@example.com
    ```

- Generoi cloud-init ISO kokoonpanollasi

    Käyttämällä `cloud-localds`-työkalua, muuta YAML-tiedosto cloud-init ISO:ksi:

    ```bash
    cloud-localds user-data.iso cloud-config.yaml
    ```

-  Käynnistä virtuaalikone cloud-init ISO:n kanssa.
  
    Käyttäen QEMU:ta, käynnistä kuva seuraavasti:

    ```bash
    qemu-kvm  -enable-kvm -m 2048 -hda test100snapshot-v2.qcow2  -cdrom user-data.iso -net nic -net user,hostfwd=tcp::2222-:22
    ```

    Komento tulostaa `VNC server running on ::1:5900`.

    Tuloste `VNC server running on ::1:5900` ilmoittaa, että QEMU käynnisti virtuaalikoneen ja tarjoaa graafisen konsolin VNC-palvelimen kautta. Voit yhdistää tähän VNC-palvelimeen nähdäksesi virtuaalikoneen näytön ja olla vuorovaikutuksessa sen kanssa. Yritämme liittää siihen SSH:lla.

    Annettu QEMU-komento tekee muutamia asioita:

    1. `-enable-kvm`: Ottaa KVM:n käyttöön 
    2. `-m 2048`: Määrittää virtuaalikoneelle 2048MB (tai 2GB) RAM-muistia.
    3. `-hda test100snapshot-v2.qcow2`: Asettaa virtuaalikoneen primäärilevyn kuvan `test100snapshot-v2.qcow2`.
    4. `-cdrom user-data.iso`: Liittää `user-data.iso` CD-levyksi virtuaalikoneeseen.
    5. `-net nic`: Luo virtuaalisen verkkokortin (Network Interface Card) virtuaalikoneelle.
    6. `-net user,hostfwd=tcp::2222-:22`: Määrittää käyttäjätilassa toimivan verkon ja ohjaa isännän portin 2222 porttiin 22 virtuaalikoneessa. 

- Kun virtuaalikone on käynnistynyt ja valmis, voit yhdistää siihen SSH-yhteyden kautta paikallisesti (tässä esimerkkinä käytetty tilannevedos on Ubuntu 22.04):

    ```bash
    ssh -i ~/.ssh/id_rsa -p 2222 ubuntu@localhost
    ```

## 5. Virtuaalikonekuvan lataaminen cPoutaan {#uploading-a-vm-image-to-cpouta}

Virtuaalikonekuvan lataaminen cPoutaan voi tapahtua joko Horizon-verkkokäyttöliittymän (WEB UI) tai OpenStack CLI:n avulla. Katso lisää kohdasta [Kuvien lisääminen](adding-images.md).

- OpenStack CLI:tä käyttämällä, olettaen, että olet määritellyt OpenStack-tiedot yllä esitetyn mukaisesti.

    Käytä `openstack image create` komentoa kuvan lataamiseen seuraavasti:

    ```bash
    openstack image create "testCentOS" \
    --file  testCentOS.qcow2 \
    --disk-format qcow2 \
    --container-format bare \
    --private
    ```

    Tarkista, että luotu kuva on saatavilla olevien kuvien listassa OpenStack-projektissasi:

    ```bash
    openstack image list --long
    ```

- Käyttämällä Web UI:ta, kirjaudu ensin verkkopaneeliin tunnuksillasi.

    - **Siirry kuvanhallintaan**: `Project`-välilehdessä, mene kohtaan `Compute` -> `Images`.
    -  **Lataa kuva**: Klikkaa `+ Create Image` -painiketta ja täytä tiedot:
        - **Kuvan nimi**: Anna kuvalle nimi.
        - **Kuvan kuvaus**: (Valinnainen) Lisää lyhyt kuvaus.
        - **Kuvan lähde**: Valitse `File Browse` ja valitse QCOW2-kuvasi.
        - **Formaatti**: Valitse `QCOW2 - QEMU Emulator` tai `raw`.
        - **Arkkitehtuuri**: (Valinnainen) Määritä arkkitehtuuri (esim., x86_64).
        - **Kuvan jakaminen**: `Protected` `Yes`.
        - Klikkaa `Create Image`.
  
Kun komento suoritetaan tai web-sovelluslataus onnistuu, kuva on käytettävissä.