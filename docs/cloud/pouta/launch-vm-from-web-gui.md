# Virtuaalikoneen luominen Poutaan {#creating-a-virtual-machine-in-pouta}

!!! Warning

    Sinun tulisi tutustua Poutan turvallisuusohjeisiin ja
    laskutussääntöihin ennen ensimmäisen virtuaalikoneesi käynnistämistä.

Tässä dokumentissa esitellään yksinkertainen tapa käynnistää virtuaalikone
Poutan palvelussa. Kuka tahansa CSC:n käyttäjä, jolla on laskentaprojekti,
voi pyytää palveluun pääsyä kuten kuvailtu [Hakeminen Poutan käyttöoikeuteen].
Käyttääksesi Poutaa, sinun tulee ensin hakea käyttöoikeutta projektiisi.
Varmista ensin, että olet tutustunut [käsitteisiin](../index.md) ja
[turvallisuusasioihin](security.md). Saatat myös haluta katsoa
[verkkolähetyksen](https://www.youtube.com/watch?v=CIO8KRbgDoI).

[TOC]


<!--TOC luo sisällysluettelon -->

Pouta-pilvien verkkokäyttöliittymät ovat saatavilla seuraavissa osoitteissa:

| URL           | Palvelun nimi           | Pääsy |
| :------------- |:-------------| :-----|
| [https://pouta.csc.fi](https://pouta.csc.fi)       | cPouta-verkkoliittymä | Pääsy internetissä |
| [https://epouta.csc.fi](https://epouta.csc.fi)     | ePouta-verkkoliittymä      | Pääsy vain IP-osoitteista, jotka on tarkoitettu ePoutan hallintaliittymien käytölle |

Tämä _OpenStack Horizon_ -pohjainen käyttöliittymä mahdollistaa perus pilvilaskentatoimintojen hallinnan, kuten uuden virtuaalikoneen käynnistämisen ja turvallisuusasetusten hallinnan. Tämän palvelun käyttöön tarvitaan CSC:n käyttäjätili ja cPouta/ePouta-projekti CSC:ssä.

Voit kirjautua cPoutaan useilla tileillä. CSC:n käyttäjätilisi (CSC:n käyttäjätunnus ja salasana) lisäksi voit käyttää Haka-, VIRTU- ja Life Science AAI -tilejä. Haka-, VIRTU- ja Life Science AAI -tilit toimivat vain, jos ne on linkitetty CSC-tunnukseesi. Tilit voidaan linkittää [MyCSC](https://my.csc.fi/).

Voit kirjautua ePoutaan vain CSC-tililläsi.

## Valmistelevat vaiheet {#preparatory-steps}

Ennen virtuaalikoneen luomista sinun täytyy suorittaa seuraavat 3 vaihetta:

1. Valitse oikea **CSC-projekti**.

1. Luo ja asenna **SSH-avaimien pari**.

1. Aseta **turvallisuusryhmä** hallitsemaan palomuuria.

Ennen ensimmäisen virtuaalikoneen käynnistämistä cPoutassa/ePoutassa, sinun on ensin luotava SSH-avaimien pari ja muokattava turvallisuusasetuksia, jotta voit yhdistää virtuaalikoneeseesi.

### Valitse CSC-projekti {#selecting-the-csc-project}

![Pouta-projektin valinta](../../img/pouta_project_selection.png){ align=left }

Sinulla voi olla useampi kuin yksi CSC-projekti, jolla on pääsy Poutaan. Voit tarkistaa tämän [my.csc.fi](https://my.csc.fi){:target="_blank"}, jossa näet kaikki projektit, joihin sinulla on pääsy ja joihin cPouta (tai ePouta) on aktivoitu palveluna.

Poutan käyttöliittymässä varmista, että valitset oikean projektin. Tässä on kaksi huomioon otettavaa seikkaa:

* Projekti on hiekkalaatikko, joka sisältää resursseja kuten virtuaalikoneita ja verkkoja, ja kuka tahansa projektissa voi nähdä ja hallita kaikkia näitä resursseja. He eivät välttämättä voi päästä virtuaalikoneeseen, koska tämä määritetään koneeseen konfiguroiduilla SSH-avaimilla, mutta he voivat **poistaa**, **käynnistää uudelleen**, ... jne.
* Projektit määrittävät laskutuksen. Varmista, että kustannukset menevät oikealle laskutusprojektille.

### SSH-avaimien asettaminen {#setting-up-ssh-keys}

Avaa yhteys virtuaalikoneisiisi cPoutassa/ePoutassa, sinun on ensin todistettava identiteettisi virtuaalikoneelle, ja tätä varten tarvitset SSH-avaimia. Tämä on oletustapa (ja turvallisin) päästä virtuaalikoneisiin. Sinun tarvitsee asettaa SSH-avaimesi vain kerran per projekti.

!!! info "Public avainten tuonti"
    Jos olet jo perehtynyt SSH-avaimiin, voit käyttää olemassa olevia SSH-avaimiasi päästäksesi virtuaalikoneisiin. Verkkokäyttöliittymässä mene **Compute > Key Pairs** -osioon ja valitse **Import Public Key**. Sinun täytyy nimetä avain, muista, että sinun täytyy käyttää tätä nimeä, kun luot virtuaalikoneita, joten suositus on pitää se lyhyenä ja informatiivisena aiotun käytön suhteen. Toiseksi liitä julkinen avaimellesi, sen täytyy olla yhdessä rivissä ja olla muodossa `key-type hash comment`, esimerkiksi RSA-avain `henkilö@domain.nimi`:

    `ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAQQCo9+BpMRYQ/dL3DS2CyJxRF+j6ctbT3/Qp84+KeFhnii7NT7fELilKUSnxS30WAvQCCo2yU1orfgqr41mM70MB henkilö@domain.nimi`

Jos et ole aikaisemmin käyttänyt SSH-avaimia, sinun täytyy luoda sellainen. Verkkokäyttöliittymä voi hoitaa tämän puolestasi:

1. Mene **Compute > Key Pairs** -osioon ja valitse **Create Key Pair**.

    ![Käyttöliittymän Access & Security -alivälilehti cPoutassa](../../img/pouta-user-guide-keypairs.png 'ssh key pairs')

    **Kuva** _Access & Security_ -alivälilehti cPoutan verkkokäyttöliittymässä

1. Anna avaimellesi nimi ja napsauta **Create Key Pair**. Saat "_keyname.pem_" tallentaaksesi. Tallenna se kotihakemistoosi. Tämä on viimeinen kerta, kun voit ladata tämän **yksityisen avaimen**, Pouta ei pidä kopiota palvelimillaan.

    ![Luo avain](../../img/pouta-create-key.png)

    **Kuva** Create Key Pair -dialogi

#### Linux ja Mac {#linux-and-mac}

Asentaaksesi avaimen, jonka latasit edellisessä vaiheessa (_keyname.pem_ tai _keyname.cer_), sinun täytyy ajaa nämä komennot:

!!! info "MacOS:lle"
    Jos käytät Chrome-selainta Mac OS X Monterey -käyttöjärjestelmässä, saat avainname.cer sijasta avainname.pem. Seuraava menettely pysyy samana.

```bash
mkdir -p ~/.ssh
chmod 700 .ssh
mv keyname.pem ~/.ssh
chmod 400 ~/.ssh/keyname.pem
```

!!! info "400 = Vain omistaja voi lukea"
    Kun tiedostolla Unixissa on 400 käyttöoikeudet, se tarkoittaa:
    `r-- --- ---`

    mikä tarkoittaa, että vain omistaja voi lukea tiedostoa. Tämä on suositeltu arvo SSH-avaimille, mutta jos sinun tarvitsee ylikirjoittaa tiedosto, sinun täytyy myös antaa kirjoitusoikeudet: `chmod 600 ~/.ssh/keyname.pem`.

Ennen kuin käytät juuri luotua avainta, sinun tulisi suojata se salasanalla:

```bash
chmod 600 ~/.ssh/keyname.pem
ssh-keygen -p -f .ssh/keyname.pem
chmod 400 ~/.ssh/keyname.pem
```

#### Windows (PowerShell) {#windows-powershell}

**Windows**-ympäristöissä suositellaan käytettävän PowerShelliä. Prosessi on hyvin samankaltainen

```PowerShell
mkdir ~/.ssh
mv yourkey.pem ~/.ssh/
```

Ennen kuin käytät juuri luotua avainta, sinun tulisi suojata se salasanalla:

```PowerShell
ssh-keygen.exe -p -f yourkey.pem
```

Sitten, edelleen PowerShellistä, voit käyttää `ssh` komentoa yhdistääksesi koneeseen, samalla tavalla kuin se tehdään Linuxista tai Macista.

#### Windows (Putty) {#windows-putty}

Jos Windowsissasi ei ole _ssh_-komentoa asennettuna, on myös mahdollista käyttää Puttya.

Tämä tehdään käyttämällä _puttygen_-työkalua, ladata yksityinen avain (.pem) ja tallentaa se (salasanalla suojattuna) .ppk-muodossa, jota Putty voi käyttää.

1. Lataa _Putty_ ja _puttygen_, jotka ovat saatavilla osoitteessa <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>.

1. Aja _puttygen_ ja lataa avain, jonka latasit (sen pitäisi olla Lataukset-sivulla).

    ![Putty Gen](../../img/putty-load.png)

1. Aseta avaimelle salasana. Tämä ei ole pakollista, mutta suositeltua.

1. Tallenna avain _ppk_-muodossa, tämä on oletusmuoto Puttylle.

    ![Tallennettu](../../img/putty-saved-ppk.png)

Nyt voimme käyttää tätä uutta Puttya yhdistäksemme virtuaalikoneeseen.

1. Aja _putty_ ja lataa ssh-avain. Mene **Connection > SSH > Auth > Credentials** ja **Private key file for authentication**-kohdassa käytä **Browse...**-painiketta valitaksesi oikea .ppk-tiedosto.

    ![Yksityinen avaintiedosto todennukseen](../../img/putty-key-file-authentication.png)

1. Kun avain on ladattu, tallenna istunto. Mene **Session**-osioon ja **Saved Sessions**-kohdassa kirjoita uuden istunnon nimi ja napsauta tallenna.

### Palomuurit ja suojausryhmät {#firewalls-and-security-groups}

Suojausryhmät ovat joukko palomuurisääntöjä, jotka rajoittavat pääsyä koneisiisi. Virtuaalikone voi käyttää yhtä tai useampaa suojausryhmää. Nämä palomuurisäännöt tehdään _OpenStack_-kerroksessa, ja sinulla voi olla lisäpalomuurisääntöjä virtuaalikoneessasi. Yhteysongelmien sattuessa sinun tulisi varmistaa, että sekä suojausryhmä että virtuaalikoneen sisäinen palomuuri on oikein konfiguroitu. "Oletus"-suojausryhmässä on säännöt, jotka sallivat sisäisen kommunikaation virtuaalikoneiden välillä, jotka kuuluvat suojausryhmään.

Suojausryhmää voidaan muokata tai luoda missä tahansa virtuaalikoneen elinkaaren vaiheessa. Kaikki suojausryhmään tehdyt muutokset sovelletaan heti virtuaalikoneeseen.

!!! warning "Älä muokkaa oletussuojausryhmää"
    Hyväksi käytännöksi ei suositella "Oletus"-suojausryhmän muokkaamista. Suosittelemme sen sijaan luomaan erityisiä suojausryhmiä erityisiin tarkoituksiin ja nimeämään ne vastaavasti. Esimerkiksi luo suojausryhmä nimeltä "SSH-VPN", jotta VPN-koneiden on mahdollista tehdä SSH/22-kutsuja suojausryhmän koneisiin.

Uuden suojausryhmän luomiseksi:

1. Siirry **Network > Security Groups** -osioon ja napsauta **Create Security Group**, anna nimi ja lisää kuvaus.

1. Napsauta **Manage Rules** ja esiin tulevassa näkymässä napsauta **Add Rule**.

    ![Lisää sääntö](../../img/pouta-add-rules-secgroup.png)

    Saatavilla on runsaasti mukautusvaihtoehtoja, mutta tässä tapauksessa suositellaan käytettäväksi `SSH`-sääntöä, joka vaatii vain yhden parametrin: `CIDR`. **Classless Inter-Domain Routing** tai **CIDR** antaa sinun määrittää aliverkon (`88.44.55.0/24`) tai tietyn IP:n (`88.44.55.77/32`).

1. Löytääksesi IP:si voit käyttää palveluja kuten <https://apps.csc.fi/myip>.

!!! warning
    Verkko-ongelmasi voivat olla monimutkaisempia. Saatat olla proxy-palvelimen takana. Jos näin on, kysy neuvoa verkko-tukihenkilöltäsi.

!!! error
    Voit myös avata portit kaikille mahdollisille IP-osoitteille käyttämällä `0.0.0.0/0` CIDR-arvona, mutta tämä on huono tietoturvakäytäntö.

!!! Tip
    **Huomaa:**

    *   **Oletussäännöt poistaminen ulospäin (salli mikä tahansa protokolla 0.0.0.0/0 ja ::/0) cPoutassa aiheuttaa häiriöitä metatietopalvelussa, joka vastaa SSH-avainasettelusta. Jos haluat rajoittaa ulospäin suuntautuvaa liikennettä, sinun pitäisi ainakin sallia lähtevä liikenne IP-osoitteeseen 169.254.169.254, TCP-porttiin 80, jotta SSH-avainten asettaminen toimii.**
    *   **Vaikka ePoutan virtuaalikoneet ovat vain asiakkaan verkon käytettävissä, niidenkin tulee olla konfiguroitu suojausryhmillä. Muutoin niihin ei pääse.**
    *   **On mahdollista lisätä ja poistaa suojausryhmiä käynnissä olevasta instanssista. Tämä tehdään instanssisivulta.**

### Palveluryhmät {#server-groups}

Jos haluat politiikan, joka sallii instanssisi toimia (tai ei toimia) samalla isännällä, voit asettaa palveluryhmät.

![Palveluryhmät](../../img/pouta-server-groups.png)

!!! Warning  
    Voit lisätä instanssin palveluryhmään vain instanssia luodessasi. Ei myöhemmin!

Klikattuasi **Create Server Group**, ikkuna avautuu:  

![Luo palveluryhmä](../../img/pouta-create-server-group.png)

Anna palveluryhmällesi nimi ja valitse politiikka. Valittavana on **Affinity**, **Anti Affinity**, **Soft Affinity** ja **Soft Anti Affinity**.  

- **Affinity**: Instanssit, jotka sijaitsevat palveluryhmässä, jossa on affinity-politiikka, ajoittavat ajamiseen samalla isännällä aina kun mahdollista. Affinity-politiikan tavoitteena on pitää instanssit yhdessä samalla fyysisellä palvelimella, mikä voi olla hyödyllistä sovelluksille tai palveluille, jotka vaativat alhaisen viiveen kommunikaatiota instanssien välillä.

- **Anti Affinity**: Instanssit, jotka sijaitsevat palveluryhmässä, jossa on anti-affinity-politiikka, ajoittavat ajamiseen eri isännillä aina kun mahdollista. Anti-affinity-politiikka parantaa vikasietoisuutta ja saatavuutta levittämällä instanssit useille fyysisille palvelimille. Tämä auttaa minimoimaan laitteistovikojen vaikutuksia yhdelle palvelimelle.

- **Soft Affinity**: Soft affinity on variaatio affinity-politiikasta. Palveluryhmässä, jossa on soft affinity -politiikka, ajurlintia yrittää pitää instanssit samalla isännällä, mutta se ei ole tiukka vaatimus. Jos rajoitteet estävät instanssien sijoittumisen samalla isännällä, aikatauluttaja voi silti sijoittaa ne eri isännälle. Soft affinity tarjoaa joustavamman lähestymistavan verrattuna tiukkaan affinity-politiikkaan.

- **Soft Anti-Affinity:** Soft anti-affinity on variaatio anti-affinity-politiikasta. Palveluryhmässä, jossa on soft anti-affinity -politiikka, ajurlintia yrittää sijoittaa instanssit eri isännille, mutta se ei ole tiukka vaatimus. Jos rajoitteet estävät instanssien levittämisen eri isännille, ajurlintia voi silti sijoittaa ne samalle isännälle. Soft anti-affinity tarjoaa joustavamman lähestymistavan verrattuna tiukkaan anti-affinity-politiikkaan.  

Tarkistaaksesi, ovatko instanssisi samalla (tai eri) isännällä, voit käyttää tätä komentoa:
```sh
openstack server show [INSTANCE_NAME | INSTANCE_ID] | grep HostId
```

!!! Note  
    "Pehmeät" variantit sallivat enemmän joustavuutta instanssien sijoituksessa.  
    Affinity- tai anti-affinity-politiikoita ei aina ole mahdollista toteuttaa resurssirajoitteiden tai muiden aikatauluttamisrajoitusten vuoksi.

## Virtuaalisen koneen käynnistäminen {#launching-a-virtual-machine}

Kun SSH-avaimet ja suojausryhmät on asetettu, voit käynnistää uuden virtuaalikoneen Poutan verkkokäyttöliittymien kautta:

!!! info
    * [https://pouta.csc.fi](https://pouta.csc.fi) (cPoutaa varten)
    * tai [https://epouta.csc.fi](https://epouta.csc.fi) (ePoutaa varten)

1. Poutan verkkokäyttöliittymän pääsivulla avaa **Compute > Instances** -näkymä.
1. Klikkaa **Launch Instance** oikealla yläkulmassa. Tämä avaa _launch instance_-näytön, jossa määritellään uuden virtuaalikoneen ominaisuudet.

    ![Käynnistä instanssinäkymä](../../img/pouta-launch-instance.png 'Launch cPouta instance')

    **Kuva** Käynnistä instanssinäkymä

1. _Launch instance_-näkymän **Details**-välilehdellä kirjoita ensin **Instance Name**.

1. Valitse **Flavour**, joka on luomasi virtuaalikoneen "koko". Katso [Virtuaalikoneen maustet ja laskutusyksikkön korot](vm-flavors-and-billing.md) täydelliselle listalle ja kuvauksille.

1. **Instance Count**-kohdassa voit määrittää luotavien virtuaalikoneiden määrän. Jos olet epävarma, jätä se arvoon `1`.

1. **Instance Boot Source**. Valitse avattavasta valikosta "Boot from image".

    !!! Info "Cloud-native"

        Jos haluat olla enemmän cloud-native, voit valita "Boot from image (creates a new volume)" -vaihtoehdon. Tämä vaihtoehto luo uuden pysyvän levyn instanssillesi. Jos poistat epähuomiossa instanssisi tai se menee palautumattomaan tilaan, instanssisi tiedostojärjestelmä tallentuu tähän levyyn. Myöhemmin voit käyttää tätä levyä käynnistääksesi uuden instanssin samalla tiedostojärjestelmän tilalla kuin edellinen instanssi.

    !!! Warning "Huomaa"

        Lähestymistapa "Boot from image (creates a new volume)" luo lisälevyn, josta laskutetaan normaalisti kuten [hinnoittelusivullamme](https://research.csc.fi/billing-units) mainitaan.


1. **Image Name**, tämä päättää, mitä Linux-jakelua käytetään. Voit valita kuvan, joka sopii paremmin käyttötapaukseesi. Poutan oletuksena tarjoamat kuvat ovat säännöllisesti ajan tasalla.

1. **Access & Security**-välilehdellä sinun täytyy määrittää kaksi vaihtoehtoa. Ensiksi sinun täytyy valita *Key Pair* -nimi, jonka olet luonut [**Valmisteluvaiheissa**](#setting-up-ssh-keys). Toiseksi sinun täytyy valita [**Suojausryhmät**](#firewalls-and-security-groups)-kohdassa aikaisemmin luotu suojausryhmä.

    !!! Warning "Avaimia ei voida lisätä luomisen jälkeen"
        Julkinen avain lisätään VM:lle vain, jos se on määritelty tässä vaiheessa. Kun napsautat **Launch**, VM luodaan, eikä konfiguroituja avainnippoja voi muuttaa. Jos avainnippua ei ole konfiguroitu, suositeltu ratkaisu on poistaa VM ja aloittaa alusta.

    ![Launch the instance access view](../img/launch_instance_access_security.png 'Launch cPouta instance network')

    !!! Warning
        Jos napsautat "+"-painiketta, ikkuna sulkeutuu odottamatta ja pieni ponnahdusikkuna ilmestyy:

        ![Error plus button](../img/danger_keypairs.png 'Danger key pairs')

        Tämä on tunnettu bugi. Katso edellinen [jakso](#setting-up-ssh-keys) luodaksesi SSH-avaimesi.

1. **Networking**-välilehdellä varmista, että oma verkko (projektisi nimi) on valittuna.

    ![Launch the instance network view](../img/launch_instance_network.png 'Launch cPouta instance network')

1. Lopuksi, **Advanced Options**-välilehti mahdollistaa [**Palveluryhmän**](#server-groups) valinnan

Voit napsauttaa **Launch** aloittaaksesi virtuaalikoneen luomisen.

## Jälkimmäinen luominen askel {#post-creation-step}

Kun virtuaalikone käynnistetään, se saa vain **yksityinen IP** (`192.168.XXX.XXX`). Tämä tarkoittaa, että kone voi päästä internettiin ja muihin virtuaalikoneisiin samassa projektissa, mutta siihen ei pääse projektin ulkopuolelta. Jotta voit päästä virtuaalikoneeseesi, sinun täytyy liittää **julkinen IP-osoite** siihen.  

!!! info
    Kelluvan IP:n yhdistäminen on käytettävissä vain cPouta-instansseissa.

1. Mene **Compute > Instances**, sinun pitäisi nähdä virtuaalikoneesi listauksessa.

1. Oikealla uuden koneesi kohdalla **Actions**, napsauta pudotusvalikkoa ja valitse **Associate Floating IP**.

    ![Floating IP -yhdistämisvaihtoehdot](../../img/associate-floating-ip-menu.png 'Associate floating IP menu')

    **Kuva** Floating IP -yhdistämisvaihtoehdot

1. Valitse **IP Address**-kohdassa IP-osoite. Jos "No floating IP addresses allocated" näkyy, napsauta plus-symbolia allokoidaksesi uuden IP:n projektiisi, sinun täytyy lisätä kuvaus.

1. **Port to be associated**-kohdassa valitse virtuaalikone.

1. Napsauta **Associate**.

![Floating IP -yhdistämisdialogi](../../img/pouta-assign-ip.png 'Assign IP')

**Kuva** Floating IP -yhdistämisdialogi

!!! warning "IP-laskutus"

    Allokoidut kelluvat IP-osoitteet laskutetaan 0,2 BU/tunti nopeudella. Voit lisäksi lukea [blogipostauksemme](http://cloud.blog.csc.fi/2017/12/floating-ip-management.html) kelluvien IP-osoitteiden hallinnasta cPouta-projektissa.

Nyt voimme siirtyä [Yhdistää virtuaalikoneeseesi](connecting-to-vm.md)-osioon ja kirjautua vastikään luotuun virtuaalikoneeseen.

