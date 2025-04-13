
# SSH-asiakasohjelma Windowsissa {#ssh-client-on-windows}

--8<-- "auth-update-ssh.md"

Windows-järjestelmässä on useita ohjelmia etä-SSH-yhteyden luomiseen. Tämä sivu tarjoaa ohjeet kolmelle suositulle vaihtoehdolle: [PowerShell](#powershell), [PuTTY](#putty) ja [MobaXterm](#mobaxterm).

## PowerShell {#powershell}

Voit käyttää [Windows PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/ssh-remoting-in-powershell) komentoriviä yhdistääksesi CSC:n supertietokoneeseen käyttäen [Win32 OpenSSH -asiakasohjelmaa](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse).
Asentaaksesi OpenSSH:n Windows-laitteeseen seuraa [näitä asennusohjeita](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui#install-openssh-for-windows).

### SSH-avaimien luominen (PowerShell) {#generating-ssh-keys-powershell}

SSH-asiakasohjelman käyttö CSC:n supertietokoneilla edellyttää SSH-avainten asettamista. Kun olet asentanut OpenSSH:n, voit luoda SSH-avaimia PowerShellillä suorittamalla:

```bash
ssh-keygen -a 100 -t ed25519
```

Tuetut avaintyypit ovat Ed25519 ja RSA 2048–16384. **Suosittelemme vahvasti Ed25519-avaimia**. Jos valitset RSA:n, käytä vähintään 4096 bittiä.

Kun olet luonut SSH-avainparin, sinun on lisättävä **julkinen avain** MyCSC-portaaliin.
[Lue ohjeet täältä](ssh-keys.md#adding-public-key-in-mycsc).

Saatat myös haluta konfiguroida [autentikointipääte](#authentication-agent-powershell) tekemään SSH-avaimien käytöstä kätevämpää.

!!! note "SSH-avainten käyttö"
    Katso sivu [SSH-avainten asettaminen](ssh-keys.md) saadaksesi yleistä tietoa SSH-avainten käytöstä autentikointiin. Huomioi, että sinun on pakko lisätä julkinen avain MyCSC:hen – sen kopioiminen suoraan CSC supertietokoneeseen ei toimi!

### Peruskäyttö (PowerShell) {#basic-usage-powershell}

Kun olet asentanut SSH-avaimet ja lisännyt julkisen avaimesi MyCSC:hen, voit yhdistää CSC:n supertietokoneeseen avaamalla PowerShellin ja suorittamalla:

```bash
# Korvaa <username> CSC-käyttäjätilisi nimellä ja <host> "puhti" tai "mahti"

ssh <username>@<host>.csc.fi
```

### Graafinen yhteys (PowerShell) {#graphical-connection-powershell}

Jos haluat luoda yhteyden graafisella tuella, voit käyttää esimerkiksi [Xming X -palvelinta](http://www.straightrunning.com/XmingNotes/). Etänä näytettävien grafiikoiden mahdollistamiseksi suorita:

```bash
$env:DISPLAY="localhost:0.0"
```

Käytä sitten `-X` (X11-välitys) tai `-Y` (luotettu X11-välitys) -vaihtoehtoa luodessasi yhteyttä:

```bash
ssh -X <username>@<host>.csc.fi
```

### Autentikointipääte (PowerShell) {#authentication-agent-powershell}

Välttääksesi salasanasi kirjoittamisen joka kerta yhdistäessäsi, voit
[konfiguroida Windowsin SSH-päätteen](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement?source=recommendations#user-key-generation)
säilyttämään avaimiasi muistissa paikallisen kirjautumissession ajan.

!!! warning "Syöte virheellinen MAC"
    Kun yhdistät OpenSSH-asiakasohjelmalla Windowsissa, saatat kohdata virheen "Syöte virheellinen MAC". Tämä on tunnettu ongelma, ja sen voi välttää valitsemalla nimenomaisesti toisen MAC-algoritmin. Katso yksityiskohdat [meidän FAQ-sivulta aiheesta](../../support/faq/i-cannot-login.md#why-is-my-ssh-client-saying-corrupted-mac-on-input).

## PuTTY {#putty}

[PuTTY SSH -asiakasohjelma](https://putty.org/) on vaihtoehto OpenSSH:n käytölle.

### SSH-avainten luominen (PuTTY) {#generating-ssh-keys-putty}

SSH-asiakasohjelman käyttö CSC:n supertietokoneilla vaatii SSH-avainten asettamista. Luodaksesi SSH-avaimia PuTTY:lle käytä [PuTTYgen-avaingeneraattoria](https://www.puttygen.com/). PuTTY-dokumentaatio tarjoaa [ohjeet PuTTYgenin käyttöön](https://www.putty.be/0.76/htmldoc/Chapter8.html).

Tuetut avaintyypit ovat Ed25519 ja RSA 2048–16384. **Suosittelemme vahvasti Ed25519-avaimia**. Jos valitset RSA:n, käytä vähintään 4096 bittiä.

Kun olet luonut SSH-avainparin, sinun on lisättävä **julkinen avain** MyCSC-portaaliin.
[Lue ohjeet täältä](ssh-keys.md#adding-public-key-in-mycsc).

Saatat myös haluta konfiguroida [autentikointipääte](#authentication-agent-putty) tekemään SSH-avaimien käytöstä kätevämpää.

!!! note "SSH-avainten käyttö"
    Katso sivu [SSH-avainten asettaminen](ssh-keys.md) saadaksesi yleistä tietoa SSH-avainten käytöstä autentikointiin. Huomioi, että sinun on pakko lisätä julkinen avain MyCSC:hen – sen kopioiminen suoraan CSC supertietokoneeseen ei toimi!

### Peruskäyttö (PuTTY) {#basic-usage-putty}

Kun olet asentanut SSH-avaimet ja lisännyt julkisen avaimesi MyCSC:hen, voit yhdistää CSC:n supertietokoneeseen käyttäen PuTTY:a. Kun avaat PuTTY:n, sinua pyydetään konfiguroimaan SSH-istuntosi. Tee se alla olevan taulukon mukaisesti:

| Asetus | Arvo |
|-|-|
| **Kohdekoneen nimi** | `puhti.csc.fi` tai `mahti.csc.fi` |
| **Portti** | `22` |
| **Yhteyden tyyppi** | `SSH` |

Kun luot etäyhteyttä PuTTY:llä, valitse yksityisavain tiedosto kohdasta `Connection --> SSH --> Auth`. Jos haluat, että yksityisavain käytetään joka kerta yhdistäessäsi, tallenna istuntosi tallentaaksesi valintasi. Lopuksi, napsauta `Open`.

### Graafinen yhteys (PuTTY) {#graphical-connection-putty}

Jos haluat luoda yhteyden graafisella tuella, voit käyttää esim. [Xming X -palvelinta](http://www.straightrunning.com/XmingNotes/). Käyttääksesi graafista näyttöä etänä, valitse `Enable X11 forwarding` PuTTY:n ohjelma-asetuksista (`Connection --> SSH --> X11`).

### Autentikointipääte (PuTTY) {#authentication-agent-putty}

Välttääksesi salasanasi kirjoittamisen joka kerta yhdistäessäsi, voit käyttää [Pageant-autentikointipäätettä](https://www.putty.be/0.76/htmldoc/Chapter9.html) säilyttääksesi yksityisavaimet muistissa.

## MobaXterm {#mobaxterm}

[MobaXterm](https://mobaxterm.mobatek.net/) on SSH-asiakasohjelma, jossa on sisäänrakennettu X-palvelin, mikä tarkoittaa, että sitä voidaan käyttää grafiikoiden näyttöön.

### SSH-avainten luominen (MobaXterm) {#generating-ssh-keys-mobaxterm}

SSH-asiakasohjelman käyttö CSC:n supertietokoneilla vaatii SSH-avainten asettamista. Voit luoda SSH-avaimia MobaXtermillä suorittamalla:

```bash
ssh-keygen -a 100 -t ed25519
```

Tuetut avaintyypit ovat Ed25519 ja RSA 2048–16384. **Suosittelemme vahvasti Ed25519-avaimia**. Jos valitset RSA:n, käytä vähintään 4096 bittiä.

Jos haluat, että luodut avaimet säilyvät MobaXtermin uudelleenkäynnistysten läpi, määritä pysyvä kotihakemisto MobaXtermille ohjelman asetuksissa (`Settings --> Configuration --> General`).

Kun olet luonut SSH-avainparin, sinun on lisättävä **julkinen avain** MyCSC-portaaliin.
[Lue ohjeet täältä](ssh-keys.md#adding-public-key-in-mycsc).

Saatat myös haluta konfiguroida [autentikointipääte](#authentication-agent-mobaxterm) tekemään SSH-avaimien käytöstä kätevämpää.

!!! note "SSH-avainten käyttö"
    Katso sivu [SSH-avainten asettaminen](ssh-keys.md) saadaksesi yleistä tietoa SSH-avainten käytöstä autentikointiin. Huomioi, että sinun on pakko lisätä julkinen avain MyCSC:hen – sen kopioiminen suoraan CSC supertietokoneeseen ei toimi!

### Peruskäyttö (MobaXterm) {#basic-usage-mobaxterm}

Kun olet asentanut SSH-avaimet ja lisännyt julkisen avaimesi MyCSC:hen, voit yhdistää CSC:n supertietokoneeseen käyttäen MobaXtermia. Yhdistyäksesi MobaXtermilla, avaa terminaali ja suorita:

```bash
# Korvaa <username> CSC-käyttäjätilisi nimellä ja <host> "puhti" tai "mahti"

ssh <username>@<host>.csc.fi
```

### Graafinen yhteys (MobaXterm) {#graphical-connection-mobaxterm}

Mahdollistaaksesi grafiikoiden näyttämisen SSH:n yli, käytä `-X` (X11 forwarding) tai `-Y` (trusted X11 forwarding) -vaihtoehtoa yhteyttä luodessasi:

```bash
ssh -X <username>@<host>.csc.fi
```

### Autentikointipääte (MobaXterm) {#authentication-agent-mobaxterm}

Välttääksesi salasanasi kirjoittamisen joka kerta yhdistäessäsi, ota käyttöön MobAgent-autentikointipääte ohjelman asetuksista (`Settings --> Configuration --> SSH`).

