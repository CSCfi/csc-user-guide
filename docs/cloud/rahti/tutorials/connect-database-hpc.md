
!!! error "Kehittynyt taso"
    Tämä opas käyttää OpenShiftin CLI työkalua [oc](../usage/cli.md).
    Sinun tulee ymmärtää, että OpenShift [Reitit](../concepts.md#route) altistavat internetille vain HTTP/HTTPS-portteja

# Tietokantojen käyttö Rahdilla CSC:n supertietokoneilla {#accessing-databases-on-rahti-from-csc-supercomputers}

!!! warning "Uusi Rahti LoadBalancer saatavilla"
    Rahdilla on nyt mahdollista ottaa käyttöön [LoadBalancer](../networking.md#using-loadbalancer-service-type-with-dedicated-ips).
    Toisin kuin [Reitit](../networking.md#routes), LoadBalancer-palvelu mahdollistaa palveluiden altistamisen internetille ilman, että se rajoittuu HTTP/HTTPS:ään.
    Tutustu yllä linkitettyyn dokumentaatioon saadaksesi lisätietoja.

    Seuraava dokumentaatio on edelleen saatavilla, jos haluat käyttää Reittejä ja Websocat-ohjelmaa.

Monet HPC-työprosessit vaativat tietokannan. Näiden suorittaminen kirjautumissolmussa aiheuttaa useita ongelmia, ja suorittaminen Poutassa tuo hallinnollista kuormitusta. Rahti on hyvä vaihtoehto, mutta yksi este on, että Rahti ei tue HTTP:stä poikkeavaa liikennettä ulkoisista lähteistä.

Tämän ongelman kiertämiseksi voidaan luoda HTTP-yhteensopiva WebSocket-yhteys TCP-tunneloinnin avulla. Tämä voidaan saavuttaa käyttämällä komentoriviasiakasohjelmaa nimeltä [WebSocat](https://github.com/vi/websocat), jolla voi muodostaa yhteyksiä ja palvella WebSocateja. Tässä tapauksessa Rahdin sisällä toimiva WebSocat-instance muuntaa työprosessista tulevan tietokantakyselyn HTTP-yhteensopivaksi WebSocket-protokollaksi. Kun liikenne saapuu Rahdille, käytämme toista Rahdin sisällä toimivaa WebSocat-instanssia muuntaaksemme WebSocket-yhteyden takaisin TCP-yhteydeksi alkuperäiselle portille, jolle tietokanta on määritetty vastaanottamaan liikennettä. Prosessin piirros on esitetty alla.

![Kuva, joka kuvaa WebSocket-yhteyttä CSC:n HPC-ympäristön ja Rahdilla olevan tietokantapalvelun välillä](../../../img/websocat-diagram-4.drawio.png)

Tämä opas kuvaa vaiheet tämän saavuttamiseksi käyttäen MariaDB:tä esimerkkitietokantana.

!!! info

    Alla käytetty OpenShift-malli WebSocatin konfiguroimiseen Rahdilla on tuettu beta-versio!

!!! info

    Tämä ratkaisu soveltuu laskennallisesti kevyisiin käyttötapauksiin. Järkevä mittakaava voidaan olettaa noin 100 prosessille, jotka samanaikaisesti käyttävät tietokantaa Rahdilla. Tämän rajan ylittäminen ei ole suositeltavaa ja saattaa heikentää suorituskykyä.

## Vaihe 1: MariaDB:n ja WebSocatin asennus Rahdilla {#step-1-setting-up-mariadb-and-websocat-on-rahti}

MariaDB:n ja WebSocatin konfigurointi Rahdilla voidaan tehdä joko verkkokäyttöliittymän kautta tai käyttämällä `oc` komentorivityökalua. Huomaa, että CSC-projektillasi on oltava pääsy Rahdin palveluun. Katso [kuinka lisätä palvelun käyttöoikeus projektille](../../../accounts/how-to-add-service-access-for-project.md).

!!! info

    Kiinnitä huomiota eroon [pysyvän](../storage/index.md#persistent-storage) ja [ohimenevän tallennustilan](../storage/index.md#ephemeral-storage) välillä, kun luot uutta tietokantaa Rahdille. Ohimenevä tietokanta on tarkoitettu tilapäiseen tallennukseen eikä pitäisi pitää luotettavana. Jos [Pod](../networking.md#pods), jossa tietokantasi toimii, poistetaan tai käynnistetään uudelleen, menetät kaikki tietosi! Tämän välttämiseksi luo tietokanta pysyvällä levyllä ja varmista, että suoritat säännöllisesti varmuuskopioita esimerkiksi [Allas](../../../data/Allas/index.md)-palveluun.

### Vaihtoehto 1: Rahdin verkkokäyttöliittymän käyttö {#option-1-using-the-rahti-web-interface}

- Kirjaudu [Rahdin verkkokäyttöliittymään](https://rahti.csc.fi/). Katso [Pääsyn hankkiminen](../access.md) ohjeet.
- Ota käyttöön MariaDB "Sovelluskehittäjien katalogista". Löydät kehittäjäkatalogin `Kehittäjä`-valikon **+Lisää**-osiosta.
- Määritä tietokanta. Sinun on valittava tai luotava vähintään Rahdin projekti, johon haluat lisätä tietokannan. Jos luot uuden projektin, varmista, että projektin kuvauksessa on CSC-projektin numero muodossa `csc_project: 2001234`
- Luo tietokanta ja muista nämä
    - Yhteyskäyttäjänimi
    - Yhteyssalasana
    - Juuren salasana
    - Tietokannan nimi (`sampledb` oletuksena)
    - Tietokantapalvelun nimi (`mariadb` oletuksena)
- Tarkista luomisen jälkeen verkkoasetukset ja muista ne:
    - Kohdeportti (3306 oletuksena)
    - Isännän osoite (muodossa `<palvelunimi>.<projektinimi>.svc`)
- WebSocatin konfiguroimiseen Rahdilla tarvitaan [OpenShift-malli](https://github.com/CSCfi/websocat-template/blob/main/websocat-template.yaml). Lataa tai kopioi tämä YAML-tiedosto leikepöydällesi. **Huom:** tämä on _tuettu_ beta-malli
- Klikkaa `+` merkkiä verkkokäyttöliittymän oikeassa yläkulmassa ja liitä malli. Klikkaa luo.
- Palaa "Sovelluskehittäjien katalogiin" ja ota käyttöön Websocat-malli. Sinun on annettava "Tietokantapalvelun nimi" (`mariadb` oletuksena) ja "Tietokantaportti" (`3306` oletuksena).
- `Kehittäjä`-valikossa, siirry **Project -> Route** ja kopioi Location URL. Käytät tätä URL:ää yhdistymiseen Rahdista ulkopuolelta.

### Vaihtoehto 2: `oc` komentorivityökalun käyttö {#option-2-using-the-oc-command-line-tool}

- Katso [Komentorivityökalun käyttö](../usage/cli.md) perusohjeet
- Kirjautuminen CSC:n käyttäjänimellä ja salasanalla

```bash
oc login https://api.2.rahti.csc.fi:6443 -u <username> -p <password>
```

- Luo uusi projekti (namespace) tai siirry olemassa olevaan. Jos luot uuden projektin, varmista, että projektin kuvauksessa on CSC-projektin numero muodossa `csc_project: 2001234`

```bash
oc new-project <project name> --display-name='Uusi projektini'\
   --description='csc_project: <project number>'
```

tai

```bash
oc project <project name>
```

- Lisää MariaDB käynnistämällä `mariadb-persistent` mallin. Muista käyttäjänimi, salasana, tietokannan nimi ja tietokantapalvelun nimi. Käytä `-p` lippua muokataksesi oletusparametreja

```bash
oc new-app --template=mariadb-persistent
```

- Lisää WebSocat käynnistämällä [OpenShift-malli](https://github.com/CSCfi/websocat-template/blob/main/websocat-template.yaml). Voit tarkistaa kohdeportin komennolla `oc describe services <service name>`. Palvelun nimi ja kohdeportin oletusparametrit ovat `mariadb` ja 3306

```bash
oc new-app --file=/path/to/websocat-template.yaml\
  --param=DATABASE_SERVICE=<service name>.<project name>.svc\
  --param=DATABASE_PORT=<port>
```

- Muista reitti isäntänimi muodossa `websocat-<project name>.2.rahtiapp.fi`. Voit tarkistaa tämän myöhemmin komennolla `oc get route websocat`

Jos vierailet reitillä selaimesi kautta, sinun pitäisi nähdä seuraava viesti:

```
Vain WebSocket-yhteydet ovat tervetulleita tänne
```

## Vaihe 2: WebSocatin suorittaminen CSC:n supertietokoneilla {#step-2-running-websocat-on-csc-supercomputers}

MariaDB ja WebSocat ovat nyt asetettu Rahdilla, ja sinulla pitäisi olla seuraavat tiedot: MariaDB-käyttäjänimi, salasana, tietokannan nimi ja WebSocat-reitin isäntänimi. Näitä tarvitaan yhdettäessä tietokantaan. Ensin meidän on kuitenkin suoritettava `websocat`-binaari Puhti/Mahti-palvelimilla vaaditun TCP-tunnelin avaamiseksi.

- [Lataa `websocat` GitHubista](https://github.com/vi/websocat/releases) ja lisää se `PATH`-polkuusi. Esimerkiksi:

```bash
wget https://github.com/vi/websocat/releases/download/v1.8.0/websocat_amd64-linux-static \
  -O websocat
chmod +x websocat
export PATH=$PATH:$PWD
```

- Emme halua suorittaa WebSocatia kirjautumissolmussa, joten avaa interaktiivinen istunto komennolla `sinteractive -i` ja käynnistä `websocat`. Antamalla kohdeportiksi 0, WebSocat saa käyttöönsä vapaan portin, jonka voimme selvittää `lsof`-komennolla (alla olevat komennot on kätevästi laitettu skriptiin). Muista, että `<project name>`-paikkamerkintä reitin isäntänimessä, joka annetaan `websocat`-ohjelmaan, viittaa Rahti-projektisi nimeen

```bash
websocat -b tcp-l:127.0.0.1:0 wss://websocat-<project name>.2.rahtiapp.fi -E &
ws_pid=$!  # $! sisältää viimeksi suoritetun taustakomennon prosessitunnuksen
mkdir -p /tmp/$USER
lsof -i -p $ws_pid 2>/dev/null | grep TCP | grep -oE "localhost:[0-9]*" | \
  cut -d ":" -f2 > /tmp/$USER/${SLURM_JOB_ID}_rahtidb_port
echo "Saavutettu kohdeportti $(cat /tmp/$USER/${SLURM_JOB_ID}_rahtidb_port)"
```

!!! info

    Jos haluat käyttää tietokantaasi erässä, suorita `websocat` eräskriptisi sisällä. Voit käyttää samaa saatua kohdeporttia, jos olet lähettämässä työtäsi interaktiivisesta istunnosta, jossa `websocat` on jo käynnissä; käy komennolla `websocat -b tcp-l:127.0.0.1:<port> wss://websocat-<project name>.2.rahtiapp.fi -E &`. Muussa tapauksessa anna kohdeportiksi 0 ja tarkista, mikä portti WebSocatille lopulta myönnetään `lsof`-komennolla.

- Nyt `websocat` toimii interaktiivisessa istunnossa/erätyössä ja voit yhdistää Rahdilla olevaan MariaDB-tietokantaan käyttäen saatua kohdeporttia. Voit tarkistaa yhteyden esimerkiksi Pythonilla. Huomaa, että alla olevassa esimerkissä käytetyt käyttäjänimi ja salasana viittaavat luotuun tietokantapalveluun, eivät CSC-tietoihisi

!!! info

    Jotta tämä esimerkki toimisi, sinun tulee asentaa mariadb python-moduuli. Kirjoitushetkellä käytettävä komento on:
    `pip3 install mariadb=1.0.11`
    Tämä johtuu siitä, että moduulin uusin versio on rikki alustoille, joilla testasimme tätä. Katso alkuperäisestä dokumentaatiosta lisätietoa: <https://mariadb-corporation.github.io/mariadb-connector-python/install.html>

```python
# Moduulin tuonnit
import mariadb
import sys

# Yhdistä MariaDB-alustaan
try:
    conn = mariadb.connect(
        user="<username>",
        password="<password>",
        host="127.0.0.1",
        port=<port>,
        database="<database name>"

    )
except mariadb.Error as e:
    print(f"Virhe MariaDB-alustaan yhdistettäessä: {e}")
    sys.exit(1)

# Hanki kursori
cur = conn.cursor()
```

**Huom:** Websocat-asiakasohjelma kuuntelee vain IPv4:llä. Joillakin järjestelmillä on sen vuoksi välttämätöntä käyttää isäntänä `127.0.0.1`, muuten käytetään IPv6:ta eikä se yhdistä.
