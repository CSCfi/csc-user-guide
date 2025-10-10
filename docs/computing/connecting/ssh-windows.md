# SSH-asiakasohjelma Windowsissa { #ssh-client-on-windows }

--8<-- "auth-update-ssh.md"

Windows-järjestelmässä on useita ohjelmia, joilla voi muodostaa etä-SSH‑yhteyden. Tällä sivulla on ohjeet kolmeen suosittuun vaihtoehtoon: [MobaXterm](#mobaxterm), [PuTTY](#putty) ja [PowerShell](#powershell).

## MobaXterm { #mobaxterm }

[MobaXterm](https://mobaxterm.mobatek.net/) on SSH-asiakas, jossa on sisäänrakennettu X-palvelin, joten sillä voidaan näyttää grafiikkaa.

### SSH-avainten luonti (MobaXterm) { #generating-ssh-keys-mobaxterm }

CSC:n supertietokoneisiin yhdistäminen SSH-asiakkaalla edellyttää SSH-avainten käyttöönottoa. Voit luoda SSH-avaimet MobaKeyGen-apuohjelmalla
([katso ohje](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html))
tai paikallisessa päätteessä komennolla:

```bash
ssh-keygen -a 100 -t ed25519
```

Tuetut avaintyypit ovat Ed25519 ja RSA 4096:sta 16384:ään. **Suosittelemme vahvasti Ed25519-avaimia**.

Jos haluat, että luodut avaimesi säilyvät MobaXtermin uudelleenkäynnistysten yli,
määritä MobaXtermille pysyvä kotihakemisto ohjelman asetuksissa
(`Settings --> Configuration --> General`). Huomaa, että tämä vaaditaan vain, jos
loit avaimesi päätteessä etkä MobaKeyGenillä.

Kun olet luonut SSH-avainparin, sinun on lisättävä **julkinen avain** MyCSC‑portaaliin.
[Lue ohjeet täältä](ssh-keys.md#adding-public-key-in-mycsc).

Voit halutessasi ottaa käyttöön
[todennusagentin](#authentication-agent-mobaxterm), jotta SSH-avainten käyttö olisi kätevämpää.

!!! note "SSH-avainten käyttö"
    Katso sivu [SSH-avainten käyttöönotto](ssh-keys.md) saadaksesi yleistä
    tietoa SSH-avainten käytöstä todennukseen. Huomaa, että julkisen avaimen
    lisääminen MyCSC:hen on pakollista – pelkkä avaimen kopioiminen CSC:n
    supertietokoneelle ei toimi!

### Peruskäyttö (MobaXterm) { #basic-usage-mobaxterm }

Kun olet ottanut SSH-avaimet käyttöön ja lisännyt julkisen avaimesi MyCSC:hen, voit muodostaa yhteyden CSC:n supertietokoneelle MobaXtermillä. Avaa
pääte ja suorita:

```bash
# Replace <username> with the name of your CSC user account and
# <host> with "puhti" or "mahti"

ssh <username>@<host>.csc.fi
```

Jos olet tallentanut SSH-avaintiedoston muulla kuin oletusnimellä tai
muualla kuin oletussijainnissa, sinun täytyy kertoa `ssh`-komennolle, mistä
avain löytyy. Käytä `-i`-valitsinta näin:

```bash
# Replace <username> with the name of your CSC user account,
# <host> with "puhti" or "mahti" and <path-to-private-key>
# with the path to your SSH private key

ssh <username>@<host>.csc.fi -i <path-to-private-key>
```

Vaihtoehtoisesti voit
[muodostaa yhteyden GUI:n kautta tämän ohjeen mukaan](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-puhti.html#connecting-from-windows).

### Graafinen yhteys (MobaXterm) { #graphical-connection-mobaxterm }

Grafiikan näyttämiseksi SSH:n yli käytä `-X`- (X11-edelleenlähetys) tai `-Y`-
(luotettu X11-edelleenlähetys) valitsinta yhteyttä luodessasi:

```bash
ssh -X <username>@<host>.csc.fi
```

### Todennusagentti (MobaXterm) { #authentication-agent-mobaxterm }

Välttääksesi salalauseen syöttämisen joka kerta, ota käyttöön
MobAgent-todennusagentti ohjelman asetuksissa (`Settings -->
Configuration --> SSH`).

## PuTTY { #putty }

[PuTTY SSH -asiakas](https://www.chiark.greenend.org.uk/~sgtatham/putty/) on vaihtoehto OpenSSH:n käytölle.

### SSH-avainten luonti (PuTTY) { #generating-ssh-keys-putty }

CSC:n supertietokoneisiin yhdistäminen SSH-asiakkaalla edellyttää SSH-avainten käyttöönottoa. Luo SSH-avaimet PuTTY-yhteyttä varten
[PuTTYgen-avaingeneraattorilla](https://www.puttygen.com/). PuTTYn dokumentaatiossa on
[ohjeet PuTTYgenin käyttöön](https://www.putty.be/0.76/htmldoc/Chapter8.html).

Tuetut avaintyypit ovat Ed25519 ja RSA 4096:sta 16384:ään. **Suosittelemme vahvasti Ed25519-avaimia**.

Kun olet luonut SSH-avainparin, sinun on lisättävä **julkinen avain** MyCSC‑portaaliin.
[Lue ohjeet täältä](ssh-keys.md#adding-public-key-in-mycsc).

Voit halutessasi ottaa käyttöön
[todennusagentin](#authentication-agent-putty), jotta SSH-avainten käyttö olisi kätevämpää.

!!! note "SSH-avainten käyttö"
    Katso sivu [SSH-avainten käyttöönotto](ssh-keys.md) saadaksesi yleistä
    tietoa SSH-avainten käytöstä todennukseen. Huomaa, että julkisen avaimen
    lisääminen MyCSC:hen on pakollista – pelkkä avaimen kopioiminen CSC:n
    supertietokoneelle ei toimi!

### Peruskäyttö (PuTTY) { #basic-usage-putty }

Kun olet ottanut SSH-avaimet käyttöön ja lisännyt julkisen avaimesi MyCSC:hen, voit muodostaa yhteyden CSC:n supertietokoneelle PuTTYlla. Kun käynnistät PuTTYn, sinua pyydetään määrittämään SSH‑istunto. Tee se alla olevan taulukon mukaan:

| Asetus | Arvo |
|-|-|
| **Isäntänimi** | `puhti.csc.fi` tai `mahti.csc.fi` |
| **Portti** | `22` |
| **Yhteyden tyyppi** | `SSH` |

Etäyhteyttä luodessasi valitse yksityisen avaimen tiedosto kohdasta `Connection --> SSH --> Auth --> Credentials`. Jos haluat, että yksityinen avain käytetään joka kerta yhdistettäessä, tallenna istunto, jotta valinta säilyy.
Lopuksi napsauta Open ja anna CSC‑käyttäjätunnuksesi sekä SSH‑avaimen salalause.

Jos yhdistät ensimmäistä kertaa, PuTTY kysyy, luotatko isäntään.
Napsauta Accept.

### Graafinen yhteys (PuTTY) { #graphical-connection-putty }

Jos haluat muodostaa yhteyden grafiikkatuella,
voit käyttää esimerkiksi
[Xming X -palvelinta](http://www.straightrunning.com/XmingNotes/). Ota etänä näytettävä grafiikka käyttöön valitsemalla `Enable X11 forwarding` PuTTYn ohjelman asetuksista
(`Connection --> SSH --> X11`).

### Todennusagentti (PuTTY) { #authentication-agent-putty }

Välttääksesi salalauseen syöttämisen joka kerta voit käyttää
[Pageant-todennusagenttia](https://www.putty.be/0.76/htmldoc/Chapter9.html)
yksityisten avainten säilyttämiseen muistissa.

## PowerShell { #powershell }

Voit käyttää
[Windows PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/ssh-remoting-in-powershell) ‑komentorivikuorta yhdistääksesi CSC:n supertietokoneelle
[Win32 OpenSSH -asiakkaan](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse) avulla.
Asentaaksesi OpenSSH:n Windows-laitteeseen, seuraa
[näitä asennusohjeita](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui#install-openssh-for-windows).

### SSH-avainten luonti (PowerShell) { #generating-ssh-keys-powershell }

CSC:n supertietokoneisiin yhdistäminen SSH-asiakkaalla edellyttää SSH-avainten käyttöönottoa. Kun OpenSSH on asennettu, voit luoda SSH-avaimet PowerShellissä suorittamalla:

```bash
ssh-keygen -a 100 -t ed25519
```

Tuetut avaintyypit ovat Ed25519 ja RSA 4096:sta 16384:ään. **Suosittelemme vahvasti Ed25519-avaimia**.

Kun olet luonut SSH-avainparin, sinun on lisättävä **julkinen avain** MyCSC‑portaaliin.
[Lue ohjeet täältä](ssh-keys.md#adding-public-key-in-mycsc).

Voit halutessasi ottaa käyttöön
[todennusagentin](#authentication-agent-powershell), jotta SSH-avainten käyttö olisi kätevämpää.

!!! note "SSH-avainten käyttö"
    Katso sivu [SSH-avainten käyttöönotto](ssh-keys.md) saadaksesi yleistä
    tietoa SSH-avainten käytöstä todennukseen. Huomaa, että julkisen avaimen
    lisääminen MyCSC:hen on pakollista – pelkkä avaimen kopioiminen CSC:n
    supertietokoneelle ei toimi!

### Peruskäyttö (PowerShell) { #basic-usage-powershell }

Kun olet ottanut SSH-avaimet käyttöön ja lisännyt julkisen avaimesi MyCSC:hen, voit muodostaa yhteyden CSC:n supertietokoneelle avaamalla PowerShellin ja suorittamalla:

```bash
# Replace <username> with the name of your CSC user account and
# <host> with "puhti" or "mahti"

ssh <username>@<host>.csc.fi
```

Jos olet tallentanut SSH-avaintiedoston muulla kuin oletusnimellä tai
muualla kuin oletussijainnissa, sinun täytyy kertoa `ssh`-komennolle, mistä
avain löytyy. Käytä `-i`-valitsinta näin:

```bash
# Replace <username> with the name of your CSC user account,
# <host> with "puhti" or "mahti" and <path-to-private-key>
# with the path to your SSH private key

ssh <username>@<host>.csc.fi -i <path-to-private-key>
```

### Graafinen yhteys (PowerShell) { #graphical-connection-powershell }

Jos haluat muodostaa yhteyden grafiikkatuella,
voit käyttää esimerkiksi
[Xming X -palvelinta](http://www.straightrunning.com/XmingNotes/). Ota etänä näytettävä grafiikka käyttöön suorittamalla:

```bash
$env:DISPLAY="localhost:0.0"
```

Käytä sitten `-X`- (X11-edelleenlähetys) tai `-Y`- (luotettu X11-edelleenlähetys) valitsinta yhteyttä luodessasi:

```bash
ssh -X <username>@<host>.csc.fi
```

### Todennusagentti (PowerShell) { #authentication-agent-powershell }

Välttääksesi salalauseen syöttämisen joka kerta,
voit
[konfiguroida Windowsin SSH-agentin](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement?source=recommendations#user-key-generation)
säilyttämään avaimesi muistissa paikallisen kirjautumisistuntosi ajan.

!!! warning "Corrupted MAC on input"
    Kun muodostat yhteyden Windowsin OpenSSH-asiakasohjelmalla, saatat
    kohdata virheilmoituksen "Corrupted MAC on input". Kyseessä on tunnettu
    ongelma, ja sen voi välttää valitsemalla erikseen eri MAC‑algoritmin.
    Lisätietoja on
    [aihetta käsittelevällä UKK-sivullamme](../../support/faq/i-cannot-login.md#why-is-my-ssh-client-saying-corrupted-mac-on-input).