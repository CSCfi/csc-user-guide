# SSH-asiakasohjelma macOSissa ja Linuxissa { #ssh-client-on-macos-and-linux }

--8<-- "auth-update-ssh.md"

Unix-tyyppisissä järjestelmissä, kuten macOSissa ja Linuxissa, suositellaan muodostamaan yhteys CSC:n supertietokoneisiin valmiiksi asennetun pääteohjelman avulla. OpenSSH-asiakas on tavallisesti esiasennettuna macOS- ja Linux-järjestelmissä.

## SSH-avainten luominen { #generating-ssh-keys }

Yhteyden muodostaminen CSC:n supertietokoneisiin SSH-asiakkaalla edellyttää SSH-avainten käyttöönottoa. macOSissa ja Linuxissa voit käyttää komentorivityökalua ssh-keygen SSH-avainten luomiseen:

```bash
ssh-keygen -a 100 -t ed25519
```

Sinua pyydetään syöttämään salasanalause. Valitse turvallinen salasanalause. Sen tulee olla vähintään 8 merkkiä pitkä ja sisältää numeroita, kirjaimia ja erikoismerkkejä. Älä koskaan jätä salasanalauseetta tyhjäksi!

Tuetut avaintyypit ovat Ed25519 ja RSA 4096–16384. Suosittelemme vahvasti Ed25519:tä.

Kun olet luonut SSH-avainparin, sinun on lisättävä julkinen avain MyCSC-portaaliin.
[Lue ohjeet täältä](ssh-keys.md#adding-public-key-in-mycsc).

Voit halutessasi ottaa käyttöön myös [todennusagentin](#authentication-agent), mikä helpottaa SSH-avainten käyttöä.

!!! note "SSH-avainten käyttö"
    Katso sivu [SSH-avainten käyttöönotosta](ssh-keys.md) yleistä tietoa varten SSH-avainten käytöstä todennuksessa. Huomaa, että julkisen avaimesi lisääminen MyCSC:hen on pakollista – sen kopioiminen suoraan CSC:n supertietokoneelle ei toimi!

## Peruskäyttö { #basic-usage }

Kun SSH-avaimet on otettu käyttöön ja julkinen avain lisätty MyCSC:hen, voit luoda etä-SSH-yhteyden avaamalla päätteen ja suorittamalla:

```bash
# Replace <username> with the name of your CSC user account and
# <host> with "puhti" or "mahti"

ssh <username>@<host>.csc.fi
```

Jos tallensit SSH-avaintiedoston muulla kuin oletusnimellä tai muuhun kuin oletussijaintiin, sinun on kerrottava `ssh`-komennolle, mistä avain löytyy. Käytä valitsinta `-i` seuraavasti:

```bash
# Replace <username> with the name of your CSC user account,
# <host> with "puhti" or "mahti" and <path-to-private-key>
# with the path to your SSH private key

ssh <username>@<host>.csc.fi -i <path-to-private-key>
```

## Graafinen yhteys { #graphical-connection }

Grafiikan, kuten käyttöliittymien ja kuvaajien, näyttäminen SSH-yhteyden yli edellyttää ikkunointijärjestelmää. Linux-järjestelmissä X-ikkunointijärjestelmän (X11) palvelinohjelma on asennettu oletuksena. macOSissa se täytyy asentaa erikseen, esimerkiksi [XQuartz](https://www.xquartz.org/).

Salli grafiikan näyttäminen SSH:n yli käyttämällä valitsinta `-X` (X11-välitys) tai `-Y` (luotettu X11-välitys), kun käynnistät SSH-asiakkaan:

```bash
ssh -X <username>@<host>.csc.fi
```

Lisätietoja X11-välityksen valitsimista saat ajamalla `man ssh` terminaalissa.

## Todennusagentti { #authentication-agent }

Välttääksesi salasanalauseen kirjoittamisen joka kerta, kun yhdistät CSC:n supertietokoneeseen, `ssh-agent`-apuohjelma voi pitää avaimesi muistissa. Ohjelman toiminta riippuu järjestelmästäsi:

- Linux-järjestelmissä `ssh-agent` on tyypillisesti asetettu ja käynnistyy automaattisesti kirjautumisen yhteydessä, eikä vaadi sinulta lisätoimia.
- macOS-järjestelmissä sinun kannattaa lisätä seuraavat rivit tiedostoon `~/.ssh/config` (luo tiedosto, jos sitä ei ole):

    ```text
    Host *
        UseKeychain no
        AddKeysToAgent yes
    ```

Jos SSH-yksityinen avaimesi on tallennettu polkuun `~/.ssh/id_ed25519`, lisää se todennusagenttiin ajamalla:

```bash
ssh-add ~/.ssh/id_ed25519
```

### SSH-agentin välitys { #ssh-agent-forwarding }

Agentin välitys on kätevä mekanismi, jossa SSH-asiakas on konfiguroitu sallimaan, että SSH-palvelin käyttää paikallista `ssh-agent`-ohjelmaasi palvelimella ikään kuin se olisi paikallinen siellä. Tämä tarkoittaa käytännössä, että voit esimerkiksi yhdistää Puhtista Mahtiin käyttäen paikalliskoneellesi Mahtia varten määritettyjä SSH-avaimia; toisin sanoen sinun ei tarvitse luoda uutta SSH-avainparia Puhtiin. Agentin välitys on myös erittäin kätevä, jos sinun tarvitsee tehdä push yksityiseen Git-repositorioon Puhtista tai Mahtista tai kopioida dataa Puhtin ja Mahtin välillä.

Ota agentin välitys käyttöön lisäämällä `-A`-lippu `ssh`-komentoosi:

```bash
ssh -A <username>@<host>.csc.fi
```

Lisätietoja ohjelmasta `ssh-agent` löytyy
[aiheeseen liittyvästä SSH Academy -oppaasta](https://www.ssh.com/academy/ssh/agent).