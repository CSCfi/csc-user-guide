
# SSH-asiakasohjelma macOS:ssä ja Linuxissa {#ssh-client-on-macos-and-linux}

--8<-- "auth-update-ssh.md"

Unix-pohjaisissa järjestelmissä, kuten macOS:ssä ja Linuxissa, on suositeltavaa yhdistää CSC:n supertietokoneisiin käyttämällä esiasennettua pääteohjelmaa. OpenSSH-asiakasohjelma on yleensä esiasennettuna macOS- ja Linux-järjestelmissä.

## SSH-avainten luominen {#generating-ssh-keys}

Yhteyden muodostaminen CSC:n supertietokoneisiin SSH-asiakkaan avulla edellyttää SSH-avainten asettamista. macOS:ssä ja Linuxissa voit käyttää `ssh-keygen`-komentorivityökalua SSH-avainten luomiseen:

```bash
ssh-keygen -a 100 -t ed25519
```

Sinua pyydetään antamaan salalause. Valitse turvallinen salalause. Sen tulisi olla vähintään 8 merkkiä pitkä ja sisältää numeroita, kirjaimia ja erikoismerkkejä. Älä koskaan jätä salalausetta tyhjäksi!

Tuetut avaintyypit ovat Ed25519 ja RSA 2048:sta 16384:ään. **Suosittelemme voimakkaasti Ed25519:**tä. Jos valitset RSA:n, käytä vähintään 4096 bittiä.

Kun olet luonut SSH-avainparin, sinun on lisättävä **julkinen avain** MyCSC-portaaliin.
[Lue ohjeet tästä](ssh-keys.md#adding-public-key-in-mycsc).

Saatat haluta myös määrittää [todennusagentin](#authentication-agent) tekemään SSH-avainten käytöstä helpompaa.

!!! note "SSH-avainten käyttö"
    Katso sivu [SSH-avainten asettaminen](ssh-keys.md) yleistä tietoa varten SSH-avainten käytöstä todennukseen. Huomaa, että julkisen avaimen lisääminen MyCSC:hen on pakollista – suoraan CSC:n supertietokoneelle kopioiminen ei toimi!

## Peruskäyttö {#basic-usage}

Kun olet asettanut SSH-avaimet ja lisännyt julkisen avaimen MyCSC:hen, voit luoda etä-SSH-yhteyden avaamalla pääte ja suorittamalla:

```bash
# Korvaa <käyttäjänimi> CSC-käyttäjätunnuksellasi ja
# <isäntä> "puhti":lla tai "mahti":lla

ssh <käyttäjänimi>@<isäntä>.csc.fi
```

Jos olet tallentanut SSH-avain tiedostosi muuta kuin oletusnimellä tai muuhun kuin oletuspaikkaan, sinun on kerrottava `ssh`-komennolle, mistä etsiä avainta. Käytä -i-vaihtoehtoa seuraavasti:

```bash
# Korvaa <käyttäjänimi> CSC-käyttäjätunnuksellasi ja
# <isäntä> "puhti":lla tai "mahti":lla

ssh <käyttäjänimi>@<isäntä>.csc.fi -i /polku/avaintiedostoon
```

## Graafinen yhteys {#graphical-connection}

Grafiikan, kuten käyttöliittymien ja kuvaajien, näyttäminen SSH-yhteyden kautta vaatii ikkunointijärjestelmän. Useimmissa macOS- ja Linux-järjestelmissä on oletuksena X-ikkunointijärjestelmän (X11) palvelinohjelma asennettuna.

Ota käyttöön grafiikan näyttäminen SSH:n kautta käyttämällä -X (X11-välitys) tai -Y (luotettu X11-välitys) vaihtoehtoa, kun käynnistät SSH-asiakkaan:

```bash
ssh -X <käyttäjänimi>@<isäntä>.csc.fi
```

Lisätietoja X11-välitysvaihtoehdoista saat suorittamalla `man ssh` pääteohjelmassa.

## Todennusagentti {#authentication-agent}

Välttääksesi salalauseen syöttämisen joka kerta, kun yhdistät CSC:n supertietokoneeseen, voi `ssh-agent`-työkalu pitää avaimiasi muistissa. Ohjelman toiminta riippuu järjestelmästäsi:

- Linux-järjestelmissä `ssh-agent` on tyypillisesti määritetty ja suoritetaan automaattisesti kirjautumisen yhteydessä, eikä se vaadi lisätoimenpiteitä.
- macOS-järjestelmissä sinun pitäisi lisätä seuraavat rivit `~/.ssh/config`-tiedostoon (luo tiedosto, jos se ei ole olemassa):

    ```text
    Host *
        UseKeychain no
        AddKeysToAgent yes
    ```

Olettamalla, että SSH-yksityinen avain on tallennettu `~/.ssh/id_ed25519`, lisää se todennusagenttiin suorittamalla:

```bash
ssh-add ~/.ssh/id_ed25519
```

### SSH-agentin välitys {#ssh-agent-forwarding}

Agentin välitys on hyödyllinen mekanismi, jossa SSH-asiakas on määritetty sallimaan SSH-palvelimen käyttää paikallista `ssh-agent`:ia palvelimella kuten se olisi paikallinen siellä. Tämä tarkoittaa käytännössä sitä, että voit esimerkiksi yhdistää Puhtista Mahtiin käyttämällä paikallisessa koneessasi asetettuja Mahtin SSH-avaimia eli sinun ei tarvitse luoda uutta avainsarjaa Puhtissa. Agentin välitys on myös hyvin kätevä, jos sinun täytyy työntää yksityiseen Git-repositorioon Puhtista tai Mahtista.

Jos haluat ottaa agentin välityksen käyttöön, lisää rivi `ForwardAgent yes` paikalliseen `~/.ssh/config`-tiedostoon:

```text
Host *
    ForwardAgent yes
```

Toinen vaihtoehto on yksinkertaisesti sisällyttää -A-lippu `ssh`-komentoosi:

```bash
ssh -A <käyttäjänimi>@<isäntä>.csc.fi
```

Lisätietoja `ssh-agent`:sta saat [asianmukaisesta SSH Academy -oppaasta](https://www.ssh.com/academy/ssh/agent).
