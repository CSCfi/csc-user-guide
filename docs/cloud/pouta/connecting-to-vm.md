# Yhteyden muodostaminen virtuaalikoneeseesi {#connecting-to-your-virtual-machine}

Tässä artikkelissa kuvataan useita tapoja muodostaa yhteys käynnissä olevaan virtuaalikoneeseen. Virtuaalikoneen luomiseksi tutustu artikkeliin [Creating a virtual machine in Pouta](launch-vm-from-web-gui.md).

!!! info "Salasanojensa käyttö on estetty"

    Pouta CSC:n tarjoamien oletuskuvien tileillä ei ole salasanaa kirjautuessa oletuksena edes käytössä. Vain SSH-avainparin käyttö on oletuksena mahdollista. Tämä on tehty parantamaan turvallisuutta.

## SSH-yhteys avainparin avulla {#keypair-based-ssh-connection}

Ensiksi sinun täytyy tarkistaa virtuaalikoneen tila Poutan verkkokäyttöliittymän **Laskenta > Instanssit** -näkymässä.

![VM-tilan tarkistus](../../img/pouta-instance-details.png)

**Kuva** cPoutan verkkokäyttöliittymän instanssit-näkymä.

Löydä kohta **Instanssin nimi**, ja valitse virtuaalikone, johon haluat muodostaa yhteyden.

* **Virrankäyttötila** (Power State) on `Running`

* Siihen on yhdistetty `Floating IP`, kirjoita se ylös.

!!! info
    ePouta-instanssille voit muodostaa yhteyden ssh-yhteyden avulla yksityisen IP:n avulla (ssh cloud-user@private-ip).

* Tarkista avaimen nimi kohdasta **Avainpari**. Tarvitset vastaavan SSH-salaisen avaimen asennettuna tietokoneellesi.

    !!! Info "Luo SSH-julkinen avain SSH-yksityisestä avaimesta"

        Jos sinulla on pääsy SSH-yksityiseen avaimeen, voit luoda vastaavan julkisen avaimen seuraavalla komennolla:

        `ssh-keygen -y -f ~/.ssh/id_rsa`

        Tämä on hyödyllistä varmistaaksesi, mikä yksityinen avain vastaa mitäkin julkista, joka on konfiguroitu Poutassa.

* Napsauta koneen nimeä ja tarkista, että olemassa on tietoturvaryhmä, joka sallii SSH-yhteydet nykyisestä IP-osoitteestasi. Katso artikkeli [tietoturvaryhmä](launch-vm-from-web-gui.md#firewalls-and-security-groups) lisätietoja, kuinka luoda SSH-tietoturvaryhmä.

* Nyt sinun on tiedettävä, mikä käyttäjänimi on konfiguroitu virtuaalikoneessa, jotta SSH-avainparisi voi kirjautua sisään. Eri jakeluilla/kuvilla on erilaisia käyttäjätunnuksia. Kolmannen osapuolen kuvat voivat käyttää mitä käyttäjätunnusta tahansa, tarkista kyseinen dokumentaatio. Pouta CSC:n tarjoamien oletuskuvien osalta katso [Kuvat](./images.md#images) -dokumentaatioartikkeli, jossa oleva tieto pidetään ajan tasalla kaikista lisäyksistä tai muutoksista.

!!! Info

    On yleinen käytäntö, että kuvat, kun yrität kirjautua sisään käyttäjänä `root`, antavat palautteena viestin, joka kertoo, mitä käyttäjätunnusta tulisi käyttää sen sijaan.

    ```sh
    $ ssh root@86.xxx.xxx.xxx
    Kirjaudu käyttäjänä "cloud-user" sen sijaan käyttäjänä "root".
    ```

Kun sinulla on kaikki tarvittava tieto, voit nyt yhdistää instanssiin.

### Linux, Mac ja PowerShell {#linux-mac-and-powershell}

Linuxilla, Macilla ja useimmilla moderneilla Windows-versioilla on mahdollista käyttää `ssh`-komentoa:

```sh
ssh <user_name>@<floating-ip> -i <secretkey>
```

#### ssh_config {#ssh-config}

Sen sijaan, että määrittäisit polun, IP:n ja käyttäjänimen joka kerta, kun haluat muodostaa yhteyden samaan virtuaalikoneeseen, voit kirjoittaa tämän tiedon ssh-konfiguraatiotiedostoosi. Muokkaa (tai luo, jos sitä ei ole siellä) `~/.ssh/config` -tiedosto, ja lisää tämä sisältö:

```ini
Host <machine_name>
Hostname <floating ip>
User <user_name>
IdentityFile <private_key_with_path>
```

* Kohdassa **Host** sinun tulisi kirjoittaa koneen nimi (jotta voit käyttää sitä myöhemmin yhdistääksesi `ssh machine_name` -komennolla).

* Kohdassa **Hostname** kirjoita virtuaalikoneen kelluva IP.

* Kohdassa **User** käyttäjänimi on ilmoitettava.

* Kohdassa **IdentityFile** koko polku yksityiseen avaimeen on kirjoitettava, esimerkiksi `IdentityFile ~/.ssh/id_rsa`.

Tarkista [ssh_config](https://linux.die.net/man/5/ssh_config) -manuaalisivulta lisätietoja.

!!! Info "Edustajansiirto"
    Voit ottaa käyttöön *agentin edustajan* siirtämisen, kun yhdistät SSH-yhteydellä virtuaalikoneeseen käyttämällä *-A* -merkintää.

        ssh -A cloud-user@public-ip

Aktivoimalla agentin edustajansiirron, sallit etävirtuaalikoneessa toimivan ssh-agentin käyttää paikallisessa työasemassasi ladattuja avaimia. Voit käyttää tätä ominaisuutta "Bastion host model" -mallin kanssa, jossa vain yhdellä ainoalla koneella, bastion host, klusterissa on kelluva IP ja ulkoinen pääsy, ja loput koneista saavutetaan bastionin kautta.

1. Määritä kelluva IP yhdelle instansseistasi
2. ssh instanssiin aktivoimalla agentin edustajansiirto
3. ssh tästä instanssista muihin verkon instansseihin käyttämättä heidän yksityistä IP:tään

Näitä askelia noudattamalla tarvitset vain yhden julkisen IP:n jokaisen instanssin julkisen IP:n sijaan.

    **Varoitus**: agentin edustajansiirrolla on joitakin [turvallisuusvaikutuksia](https://wizardsoftheweb.pro/ssh-agent-forwarding-vulnerability-and-alternative/#the-vulnerability)

### Putty {#putty}

Avaa Putty. Kun olet noudattanut ohjeita [windows-putty](./launch-vm-from-web-gui.md#windows-putty), sinulla pitäisi olla tallennettu istunto, jossa on tallennettu yksityinen avain.

* Lataa tallennettu istunto.

* Kohdassa **Host Name (or IP address)** kirjoita käyttäjänimi ja `@`-symboli ja instanssin kelluva IP kuten: `cloud@89.14.89.14`

* Kirjoita uusi nimi (koneen nimi) kohtaan **Saved Sessions** ja napsauta tallenna.

* Napsauta **Open**, uusi ikkuna instanssiin avautuu.

Seuraavan kerran kun sinun täytyy käyttää Puttya muodostaa yhteys tähän instanssiin, sinun tarvitsee vain ladata vastaava tallennettu istunto ja napsauttaa **Open**.

## `root`-hallintaoikeudet virtuaalikoneessa {#root-administrator-access-on-a-virtual-machine}

Jos käytät Poutan tarjoamaa kuvaa ja olet kirjautunut oletuskäyttäjätilillä, voit suorittaa komentoja root-oikeuksin `sudo`-komennolla ilman salasanaa. Jos muita tilejä luodaan, niillä ei ole root-hallintaoikeuksia oletuksena.

```sh
sudo <some command>
```

Voit myös avata interaktiivisen root-terminaalin:

```sh
sudo -i
```

## Yhteyden muodostaminen koneeseen Poutan virtuaalikonsolin avulla {#connect-to-a-machine-using-the-pouta-virtual-console}

Koneeseen on mahdollista saada yhteys Pouta-virtuaalikonsolin avulla. Tätä suositellaan vain **kun SSH-yhteyden muodostaminen on mahdotonta**, esimerkiksi kun virtuaalikoneen verkkoyhteys on poikki.

Jotta voit käyttää konsolia, **sinun täytyy ensin luoda salasanaan perustuva käyttäjätili**:

* Yhdistä virtuaalikoneeseesi SSH:n kautta
* Voit käyttää [useradd](https://linux.die.net/man/8/useradd) ja/ tai [passwd](https://linux.die.net/man/1/passwd) tilin luomiseen.
* Kuten turvallisuusohjeissamme on neuvottu [turvallisuusohjeet](security.md#be-mindful-about-the-user-accounts-in-the-vm), **älä salli etäkirjautumista** tälle **salasanaan perustuvalle tilille**, vaan käytä sitä vain jos tarvitset konsolia saavuttaaksesi instanssin.

Kun salasanaan perustuva tili on luotu, poissallitun etäkirjautumisen kera:

* Instanssisivulta kohdasta **Laskenta > Instanssit**, avaa konsoli-istunto napsauttamalla **Konsoli** instanssin avattavassa valikossa.

![Konsolin avaaminen verkkoliittymässä](../../img/console-button-horizon.png)

* Kirjoita tekstiä konsoliin napsauttamalla harmaata palkkia:

![Tekstin syöttäminen verkkokonsoliin](../../img/pouta-instances-terminal.png)

* Kirjaudu sisään luomasi käyttäjätilin ja salasanan avulla.

!!! warning "Ei ASCII-merkkien ongelmia"
    *Umlaut*-merkit, kuten *ä* tai *ö*, eivät toimi virtuaalikonsolissa useimmille näppäimistökartoille.

## Vianetsintä {#troubleshooting}

Jos sinulla on ongelmia yhteyden muodostamisessa uuteen Pouta-virtuaalikoneeseesi, katso artikkeli [Miksi en voi yhdistää virtuaalikoneeseeni Poutassa?](../../support/faq/why-cant-i-connect-to-my-vm-in-pouta.md)