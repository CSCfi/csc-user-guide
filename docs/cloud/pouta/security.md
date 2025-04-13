# Turvaohjeet Poutaa varten {#security-guidelines-for-pouta}

!!! warning "Turvavastuu"

    Käyttäjät ovat vastuussa hallinnassaan olevien resurssien ja infrastruktuurin turvallisuudesta. Tähän kuuluu, mutta ei rajoitu: **virtuaalikoneet**, **verkkokonfiguraatio**, **käyttäjätilit**, ...

!!! info "Tietoturvaraportit"

    Jos olet löytänyt kriittisen tietoturva-aukon tai epäilet, että koneesi on vaarantunut, ota meihin heti yhteyttä osoitteessa <servicedesk@csc.fi>.

Tämä lista turvaohjeista ei ole tarkoitettu kattamaan kaikkia mahdollisia tapauksia ja skenaarioita, vaan toimimaan lähtökohtana kaikkien turvallisuuden säilyttämiseksi.

## Verkkoyhteydet {#network}

On erittäin tärkeää pitää verkkokonfiguraatiosi mahdollisimman turvallisena, koska se on portti, jota mikä tahansa tunkeilija käyttää järjestelmääsi sisäänpääsemiseen. On suhteellisen helppoa soveltaa joitain hyviä käytäntöjä, jotka antavat ylimääräisen turvakerroksen. Muutamia strategioita on suositeltavaa.

### Rajoittava palomuuri (luettelointi) {#restrictive-firewall-white-listing}

Virtuaalikoneesi pitäisi olla konfiguroitu siten, että ne sallivat vain sovelluksesi vaatimat vähimmäiskäytöt. Oletusarvoisesti virtuaalikoneilla ei ole ulkoista pääsyä, eli yksikään portti ei ole avoinna oletusarvoisesti julkiselle Internetille. Jotta niihin voisi yhdistää tai tarjota minkäänlaista palvelua, pääsy on lisättävä nimenomaisesti. On tärkeää avata vain ne portit, jotka on avattava, ja avata ne vain mahdollisimman vähille IP-osoitteille.

Jokaisessa Poutassa toimivassa virtuaalikoneessa on kaksi palomuuria: virtuaalikoneen oma palomuuri (netfilter/iptables) ja Poutan turvaryhmät. Keskitymme vain Poutan turvaryhmiin, koska ne ovat helpoin tapa soveltaa joukko monimutkaisia palomuurisääntöjä joukkoon virtuaalisia koneita. Tässä on esimerkki turvaryhmästä, joka antaa pääsyn porttiin 22/SSH vain neljälle aliverkolle:

![Rajattu-SSH](../../img/restricted-ssh-security-group.png)

Nämä neljä aliverkkoa voisivat olla neljä julkista verkkoaluetta, joita organisaatiosi käyttää toimistoverkossaan.

Turvaryhmät ovat helppoja konfiguroida ja helppoja visualisoida. Tämä on näkymä virtuaalikoneen yksikkösivulta:

![Rajattu API SSH](../../img/restricted-api-ssh.png)

näet, että jokainen avaus on siellä näytetty.

### Tarpeettomien palveluiden poistaminen käytöstä {#disable-unneeded-services}

Älä aja tarpeettomia palveluita virtuaalikoneellasi, vaikka ne eivät olekaan ulkopuolelle saavutettavissa. Mitä enemmän palveluita ajat, sitä suurempi on hyökkäyspinta, jota tunkeilijat voivat hyödyntää. Älä esimerkiksi ota käyttöön omaa sähköpostipalvelinta. Jos sinun tarvitsee lähettää sähköpostia cPoutasta, käytä [Poutan SMTP-palvelinta](additional-services.md#sending-e-mail-from-cpouta). Jos tämä SMTP-palvelin ei kata käyttötapaustasi, ota yhteyttä osoitteeseen <servicedesk@csc.fi>.

### Käytä turvallisia protokollia {#use-secure-protocols}

Käytä aina, kun mahdollista, salattuja ja turvallisia viestintäprotokollia välttääksesi man-in-the-middle -hyökkäykset; nämä ovat tapauksia, joissa joku saa pääsyn viestintääsi ja voi lukea menevät tiedot, kuten julkisessa WIFI:ssä. Esimerkiksi: älä käytä HTTP:tä, käytä sen sijaan HTTPS:ää. Älä käytä FTP:tä tiedostojen siirtoon, käytä sen sijaan FTPS:ää, SFTP:tä tai S3:a.

### Käytä tunkeutumisen havaitsemisohjelmistoja {#use-intrusion-detection-software}

Työkalut kuten [denyhosts](https://github.com/denyhosts/denyhosts) tai [Fail2ban](https://en.wikipedia.org/wiki/Fail2ban) analysoivat lokitiedostoja ja estävät IP-osoitteet, jotka yrittävät tehdä bruteforce-hyökkäyksiä sovellukseesi. Ne ovat erittäin tehokkaita työkaluja, mutta niitä on käytettävä huolellisesti, sillä ne voivat johtaa vääriin positiivisiin, eli estää IP-osoitteet, joita ei pitäisi estää.

## Ohjelmisto {#software}

Turvallisen ohjelmiston ajaminen on myös erittäin tärkeää. Täysin turvallisten ohjelmistojen kehittäminen ei ole triviaalitehtävä, mutta on olemassa yksinkertaisia strategioita, jotka auttavat tässä tehtävässä.

### Asenna vain tunnetuista lähteistä {#only-install-from-reputable-sources}

Ole tarkkana ohjelmiston asennuslähteiden suhteen. Asenna vain ohjelmistoa tunnetuista lähteistä. Jos mahdollista, käytä jakelun pakettienhallintaa (`yum`, `dnf`, `apt`, ...). Pakettienhallinta tekee ohjelmistojen asennuksen, päivittämisen ja poistamisen helpoksi. Jos haluttua ohjelmistoa ei ole saatavilla jakelun pakettienhallinnan varastossa, on käytettävä virallista lähdettä. Seuraa tarvitsemasi ohjelmiston virallisella verkkosivulla annettuja ohjeita. Jos tarjolla on useampi lähde, harkitse sellaista, joka tarjoaa helpomman elinkaaren (asukas/päivitys/poisto/...), kuten [snap](https://en.wikipedia.org/wiki/Snap_(software)) tai [flatpak](https://en.wikipedia.org/wiki/Flatpak).

### Automaattiset ohjelmistopäivitykset {#automatic-software-updates}

Kaikissa käyttöjärjestelmissä on mahdollisuus tehdä päivityksiä automaattisesti. Jos suoritat säännöllisiä päivityksiä, altistut vähemmän tunnetuille tietoturvaongelmille. On yleistä, että korjaus on saatavilla ennen tietoturvaongelman julkistamista.

Centos 8:ssa ja uudemmissa käytössä on `dnf-automatic`:

```yaml
sudo yum install dnf-automatic -y
systemctl enable --now dnf-automatic-install.timer
```

`yum-cron` Centos 7:lle:

```yaml
sudo yum install yum-cron -y
sudo systemctl enable yum-cron.service
sudo systemctl start yum-cron.service
```

`unattended-upgrades` Ubuntulle:

```yaml
sudo apt install unattended-upgrades
```

Jokaisella käyttöjärjestelmäversiona on oma tapa aktivoida tämä.

!!! info "Ydinpäivitykset" {#kernel-updates}

    Jotkut päivitykset, kuten ydinpäivitykset, vaativat virtuaalikoneiden uudelleenkäynnistämisen. Suunnittele tämä osaksi säännöllistä ylläpitoa.

Jos käyttötapauksesi ei tue automaattisia päivityksiä, mikä on yleistä erittäin saatavilla olevissa kokoonpanoissa, varmista, että aikataulutat säännöllisesti kunnossapitot aikoja, joissa ohjelmistopäivitys on aikataulutettu.

* **Tilaa käyttöjärjestelmäsi tietoturvailmoitukset**, jos käyttöjärjestelmässäsi ilmenee tietoturvaongelma, sinun on saatava selville se mahdollisimman pian. Voit tilata asiaankuuluvan postituslistan, RSS-syötteen, ... seurata kaikkea, mikä vaatii kiireellisiä toimenpiteitä.

### Ole tarkkana virtuaalikoneen käyttäjätilien suhteen {#be-mindful-about-the-user-accounts-in-the-vm}

Pidä silmällä järjestelmäsi käytössä olevia käyttäjätilejä. Jotkin sovellukset luovat oletustilejä, jotka ovat tarpeettomia tai jopa suoraan turvattomia. Ihannetapauksessa tilejä voisi olla kolme:

* `root`, jolla on ssh pois käytöstä ja ei salasanaa. Tämä on oletus [Pouta VM -kuvissa](images.md).
* Käyttäjätili, jolla on sysadminin pääsyoikeus, johon voi päästä vain ssh-avainten kautta ja jolla on sudo-oikeudet. Pouta VM -kuvat tarjoavat tämän käyttäjän esikonfiguroituna, käyttäjän nimi riippuu jakelusta (`cloud-user`, `centos` tai `ubuntu`), katso yllä olevaa dokumentaatiota lisätietojen saamiseksi.
* ja lisää palvelutasoiset tilit, jotka suorittavat vain yhden palvelun eikä niillä ole kirjautumismahdollisuutta, ei etä- eikä paikalliskäyttö.

Älä aktivoi salasanalla kirjautumista, **käytä SSH-avaimia** sen sijaan. Salasanat voidaan, riittävällä ajalla ja laskentateholla, arvata brutaalivoimatoimien avulla. Keskimääräinen SSH-palvelin käsittelee tuhansia tällaisia hyökkäyksiä joka viikko. Kun käytät SSH-avaimia, käytetään haaste-vastaus-autentikointia. Tämä tarkoittaa sitä, että jokaisessa kirjautumisessa kysytään erilainen haaste ja oikea vastaus on erilainen. Mitään salaisuutta (salasanaa tai avainta) ei koskaan matkusteta verkon ylitse.

Suoja salasanalla SSH-avaimesi ja varmista, ettei avaimesi koskaan poistu laitteesta, jossa se luotiin.

* Älä tallenna julkisia avaimia (saati yksityisiä) kuvassa, jota käytetään VM:n luomiseen. Pouta clouds tarjoaa metatietopalvelun, jotta voit ladata julkisia avaimia käynnistyksen yhteydessä. Tämä on suositeltavaa, koska se varmistaa, että jos avaimesi vaarantuu, pääsy kyseisestä avaimesta voidaan poistaa kaikista käynnissä olevista instansseista eikä yhdelläkään uudella instanssilla ole koskaan tätä julkista avainta.

### Pidä kirjaa sovellustesi lokitiedostoista {#keep-logs-of-your-applications}

Käytä kirjauskäytännön parhaita käytäntöjä:

- Varmista, että palvelut kirjaavat turvalliseen sijaintiin, joka on mahdollisimman väärinkäytönkestävä.
- Säilytä lokit kohtuullisen pitkän aikaa.
- Harkitse myös kirjautumista etäpalvelimelle.

*Toistettu ystävällisellä luvalla <a
href="https://support.ehelp.edu.au/support/solutions"
class="external-link">NeCTAR</a>.*