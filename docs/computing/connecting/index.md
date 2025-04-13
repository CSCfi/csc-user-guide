# Yhdistäminen CSC:n supertietokoneisiin {#connecting-to-csc-supercomputers}

--8<-- "auth-update-ssh.md"

CSC:n supertietokoneisiin voi yhdistää kahdella pääasiallisella tavalla.

1. Perinteinen tapa yhdistää supertietokoneeseen on
   [käyttämällä SSH-asiakasohjelmaa](#using-an-ssh-client).
2. Tarjoamme myös [verkkokäyttöliittymän](#using-the-web-interface) järjestelmiimme,
   joka mahdollistaa sekä graafisten sovellusten ajamisen että komentorivishelmeiden käytön.

Ohjeet yhdistämisestä LUMI-supertietokoneeseen löytyvät
[LUMIn käyttäjän oppaan get started -sivulta](https://docs.lumi-supercomputer.eu/firststeps/getstarted/).

!!! note "Kirjautumissolmun käyttöpolitiikka"
    Kun yhdistät supertietokoneeseen SSH-asiakasohjelmalla tai 
    [*Kirjautumissolmun shell*](../webinterface/shell.md) -sovelluksella, ohjataan sinut
    kirjautumissolmuun. Kirjautumissolmut **eivät ole tarkoitettu pitkiin tai raskaisiin prosessointeihin**.
    Hyväksytyt käyttötavat kirjautumissolmuihin on määritelty meidän
    [kirjautumissolmujen käyttöpolitiikassa](../usage-policy.md#login-nodes).

## Verkkokäyttöliittymän käyttäminen {#using-the-web-interface}

[Verkkokäyttöliittymä](../webinterface/index.md) on hyvä alusta
graafisten sovellusten käyttämiseen Puhti- ja Mahti-supertietokoneilla.
Se isännöi
[vuorovaikutteisia sovelluksia valikoiduille ohjelmille](../webinterface/apps.md),
kuten Jupyter ja RStudio, ja muihin GUI-sovelluksiin voit käyttää
[etätyöpöytä](../webinterface/desktop.md) -käyttöliittymää.

On myös mahdollista [avata shell-ohjelma](../webinterface/shell.md)
kirjautumissolmulla tai laskentasolmulla. Laskentasolmun shell on pysyvä, mikä tarkoittaa, että se jatkaa toimimista, vaikka sulkisit selaimen tai menettäisit internet-yhteyden. Shell-sovellukset ovat erityisen käteviä käyttäjille, joiden työasema toimii Windows-käyttöjärjestelmällä, koska Windowsissa ei yleensä ole esiasennettua SSH-asiakasohjelmaa. Katso ohjeet [yhdistämiselle Puhtin ja Mahtin verkkokäyttöliittymiin](../webinterface/connecting.md).

## SSH-asiakasohjelman käyttäminen {#using-an-ssh-client}

Kirjautuminen Puhtiin ja Mahtiin SSH-asiakasohjelmalla edellyttää, että olet
[määrittänyt SSH-avaimet](ssh-keys.md) ja
[lisännyt julkisen avaimesi MyCSCi:iin](ssh-keys.md#adding-public-key-in-mycsc).
Perinteinen salasanapohjainen tunnistautuminen ja henkilökohtaiseen
`~/.ssh/authorized_keys` -tiedostoosi tallennetut julkiset avaimet eivät **toimi**.

Unix-pohjaisissa järjestelmissä, kuten macOS ja Linux, on yleensä esiasennettu
päätelmäohjelma nimeltä yksinkertaisesti *Terminal*. Ohjeet [SSH-asiakasohjelman käyttämiseen macOS- ja Linux-järjestelmissä](ssh-unix.md) näyttävät, kuinka yhdistää CSC:n supertietokoneeseen käyttämällä päätelmäohjelmaa.

Windows-järjestelmissä ei ole vastaavaa esiasennettua ratkaisua SSH-yhteyttä varten, mutta on olemassa useita ohjelmia, joita voi käyttää tähän tarkoitukseen. Ohjeet [SSH-asiakasohjelman käyttämiseen Windowsissa](ssh-windows.md) listaavat muutamia suosittuja vaihtoehtoja.

Kun olet määrittänyt SSH-avaimet ja lisännyt julkisen avaimen MyCSCi:iin, käytä alla olevaa komentoa yhdistääksesi SSH:n kautta:

```bash
# Korvaa <username> CSC:n käyttäjätilisi nimellä ja
# <host> "puhti" tai "mahti"

ssh <username>@<host>.csc.fi
```

!!! note
    Uuden avaimen aktivoituminen voi kestää jopa tunnin sen jälkeen, kun se on lisätty MyCSCi:iin.

Kun SSH-yhteys supertietokoneeseen on auki, voit olla vuorovaikutuksessa sen kanssa antamalla Linux-komentoja Bash shell -ohjelman avulla. Johdanto työskentelyyn Linux-komentorivillä löytyy oppaastamme
[Linuxin perusteet CSC:lle](../../support/tutorials/env-guide/index.md).
Voit pitää useita CSC supertietokoneen yhteyksiä auki samanaikaisesti.

### Ensimmäinen yhteys {#first-connection}

Kun muodostat yhteyden tiettyyn supertietokoneeseen ensimmäistä kertaa, SSH-asiakasohjelma saattaa ilmoittaa, että isäntä on tuntematon, ja pyytää sinua vahvistamaan yhteyden. OpenSSH-asiakasohjelmassa viesti näyttää tältä:

```text
The authenticity of host 'puhti.csc.fi' can't be established.
ECDSA key fingerprint is SHA256:kk0Tar9opQ+6Gq0GWJdWVVvFEMeI6kW1DW1VOYveT5c.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Jatkaaksesi sinun tulee varmistaa, että näytetty avaimen sormenjälki löytyy [alla olevasta taulukosta](#host-key-fingerprints), ja sitten syöttää `yes`. Sinulta ei kysytä tätä uudelleen, ellei palvelimen avain muutu, jolloin sinun tulee jälleen varmistaa uusi avain CSC:n tarjoamista sormenjäljistä.

#### Isäntäavaimen sormenjäljet {#host-key-fingerprints}

=== "Puhti"
    | SHA256-tarkistussumma                       | Avain                              |
    |---------------------------------------------|------------------------------------|
    | kk0Tar9opQ+6Gq0GWJdWVVvFEMeI6kW1DW1VOYveT5c | ssh_host_ecdsa_key.pub (ECDSA)     |
    | Q2lpykI43ffs4PrRODZ/qncjUo3eyrRHc5T9yjJEwWY | ssh_host_ed25519_key.pub (ED25519) |
    | WH1Ag2OQtMPZb+hj3YeH9uVMMetXpCvyNUbsdk0Qcpk | ssh_host_rsa_key.pub (RSA)         |

=== "Mahti"
    | SHA256-tarkistussumma                       | Avain                              |
    |---------------------------------------------|------------------------------------|
    | WC9Lb5tmKDzUJqsQjaZLvp9T7LTs3aMUYSIy2OCdtgg | ssh_host_ecdsa_key.pub (ECDSA)     |
    | tE+1jA4Et1enbbat1V3dMRWlLtJgA8t7ZrkyIkU4ooo | ssh_host_ed25519_key.pub (ED25519) |
    | 0CxM3ECpD2LhAnMfHnm3YaXresvHrhW4cevvcPb+HNw | ssh_host_rsa_key.pub (RSA)         |

### Graafinen yhteys {#graphical-connection}

Suosittelemme verkkokäyttöliittymien käyttöä sovellusten ajamiseen graafisilla käyttöliittymillä. Vaihtoehtoisesti grafiikkaa voidaan myös näyttää SSH-yhteyden kautta käyttämällä X11-siirtoa. Katso käyttöjärjestelmäkohtaiset ohjeet:

* [X11-siirto Linux- ja macOS-järjestelmissä](ssh-unix.md#graphical-connection)
* X11-siirto Windowsissa:
    * [PowerShell](ssh-windows.md#graphical-connection-powershell)
    * [PuTTY](ssh-windows.md#graphical-connection-putty)
    * [MobaXterm](ssh-windows.md#graphical-connection-mobaxterm)

### Kehittyneempi käyttö {#advanced-usage}

#### Yhteyden muodostaminen tiettyyn solmuun {#connecting-to-a-specific-node}

Kun muodostat yhteyden supertietokoneeseen, sinut ohjataan automaattisesti johonkin järjestelmän kirjautumissolmuista. Voit kuitenkin käyttää SSH-asiakasohjelmaasi myös yhdistääksesi tiettyyn kirjautumissolmuun:

```bash
ssh <username>@<host>-login<id>.csc.fi  # esim. 'puhti-login11.csc.fi'
```

Saatavilla olevat kirjautumissolmut ovat:

| Puhti | Mahti |
|-|-|
| `puhti-login11` | `mahti-login11` |
| `puhti-login12` | `mahti-login12` |
| `puhti-login14` | `mahti-login14` |
| `puhti-login15` | `mahti-login15` |

Tämä pätee myös laskentasolmuihin, tosin vain niihin, joissa sinulla on ajossa oleva tehtävä. Käytä `squeue`-komentoa nähdäksesi, millä solmuilla tehtäväsi on ajossa, ja yhdistä solmuun käyttämällä `ssh`-komentoa.

```bash
# Solmut, joilla tehtävä on ajossa,
# näkyvät sarakkeessa "NODELIST(REASON)".

[username@puhti-login11 ~]$ squeue --me
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          12345678      test     test username  R       0:01      1 r07c01
[username@puhti-login11 ~]$ ssh r07c01
[username@r07c01 ~]$ hostname
r07c01.bullx
```

Jos yrität yhdistää solmuun, jossa sinulla ei ole aktiivista tehtävää, saat seuraavan virheilmoituksen: `Access denied by pam_slurm_adopt: you have no active jobs on this node`.

#### SSH-asiakasohjelman konfigurointi {#configuring-ssh-client}

Voit säästää aikaa lisäämällä isäntäkohtaisia asetuksia CSC:n supertietokoneille [SSH config -tiedostoon](https://www.ssh.com/academy/ssh/config) (esim. `~/.ssh/config`).

```bash
Host <host>  # esim. "puhti"
    HostName <host>.csc.fi
    User <csc-username>
```

Nyt voit yhdistää isäntään yksinkertaisesti ajamalla:

```bash
ssh <host>
```

#### Etäkehitys {#remote-development}

Joitakin editoreita, kuten Visual Studio Code ja Notepad++, voidaan käyttää
[työskentelemään tiedostojen kanssa etänä](../../support/tutorials/remote-dev.md)
sopivan liitännäisen avulla. **Tätä ei kuitenkaan suositella.**