# Poutan tietoturvaohjeet { #security-guidelines-for-pouta }

!!! warning "Tietoturvavastuu"

    Käyttäjät ovat vastuussa hallinnassaan olevien resurssien ja infrastruktuurin tietoturvasta. Tämä koskee muun muassa: **virtuaalikoneet**, **verkkomääritykset**, **käyttäjätilit**, ...

!!! info "Tietoturvailmoitukset"

    Jos olet löytänyt vakavan tietoturvahaavoittuvuuden tai epäilet, että koneesi on vaarantunut, ota meihin välittömästi yhteyttä osoitteessa <servicedesk@csc.fi>.

Tämä tietoturvaohjeiden luettelo ei kata kaikkia mahdollisia tapauksia ja tilanteita, vaan toimii lähtökohtana turvallisuuden varmistamiseksi. 

## Verkko { #network }

On erittäin tärkeää pitää verkkomääritykset mahdollisimman turvallisina, sillä niiden kautta tunkeutuja pyrkii järjestelmään. On melko helppoa ottaa käyttöön hyviä käytäntöjä, jotka tuovat lisäsuojakerroksen. Muutamia strategioita suositellaan. 

### Rajoittava palomuuri (sallittulistaus) { #restrictive-firewall-white-listing }

Virtuaalikoneidesi instanssit tulisi konfiguroida sallimaan vain sovelluksesi toiminnan kannalta välttämätön pääsy. Oletusarvoisesti virtuaalikoneilla ei ole ulkoista pääsyä, eli yhtäkään porttia ei ole oletuksena avattu julkiseen internetiin. Niihin yhdistäminen tai minkä tahansa palvelun tarjoaminen edellyttää pääsyn erikseen sallimista. On tärkeää avata vain ne portit, jotka on pakko avata, ja rajata avaukset mahdollisimman harvoihin IP-osoitteisiin.

Jokaisessa Poutassa toimivassa virtuaalikoneessa on kaksi palomuuria: itse virtuaalikoneen palomuuri (netfilter/iptables) ja Pouta Security groups. Keskitymme tässä Poutan security groupseihin, koska niiden avulla on helpointa soveltaa monimutkaisia palomuurisääntöjä joukkoon virtuaalikoneita. Tässä esimerkki security groupista, joka sallii pääsyn porttiin 22/SSH vain neljästä aliverkosta:

![Rajoitettu SSH](../../img/restricted-ssh-security-group.png)

Nämä neljä aliverkkoa voivat olla organisaatiosi toimistoverkossa käyttämät neljä julkista osoitealuetta.

Security groupsit on helppo määrittää ja niiden tilaa on helppo havainnollistaa. Tämä näkymä on virtuaalikoneen instanssisivulta:

![Rajoitettu API SSH](../../img/restricted-api-ssh.png)

näet, että jokainen avaus näkyy siellä. 

### Poista tarpeettomat palvelut käytöstä { #disable-unneeded-services }

Älä aja tarpeettomia palveluita virtuaalikoneella, vaikka niihin ei pääsisikään ulkopuolelta. Mitä enemmän palveluja ajat, sitä enemmän hyökkäyspinta-alaa tunkeutujilla on hyödynnettävänä. Esimerkiksi älä ota käyttöön omaa sähköpostipalvelinta. Jos sinun täytyy lähettää sähköpostia cPoudasta, käytä [Poutan SMTP-palvelinta](additional-services.md#sending-e-mail-from-cpouta). Jos tämä SMTP-palvelin ei kata käyttötapaustasi, ota yhteyttä <servicedesk@csc.fi>.

### Käytä suojattuja protokollia { #use-secure-protocols }

Käytä aina kun mahdollista salattuja ja turvallisia viestintäprotokollia man-in-the-middle-hyökkäysten välttämiseksi; tällöin joku pääsee väliin ja voi lukea liikennettä, kuten julkisessa WiFi-verkossa. Esimerkiksi: älä käytä HTTP:tä, vaan HTTPS:ää. Älä käytä tiedostonsiirtoon FTP:tä, vaan FTPS:ää, SFTP:tä tai S3:ta.

### Käytä tunkeutumisen havaitsemiseen tarkoitettuja ohjelmistoja { #use-intrusion-detection-software }

Työkalut kuten [denyhosts](https://github.com/denyhosts/denyhosts) ja [Fail2ban](https://en.wikipedia.org/wiki/Fail2ban) analysoivat lokitiedostoja ja estävät IP-osoitteita, jotka yrittävät murtautua palveluusi brute force -hyökkäyksillä. Ne ovat tehokkaita työkaluja, mutta niitä on käytettävä varoen, sillä ne voivat aiheuttaa vääriä positiivisia, eli estää IP-osoitteita, joita ei pitäisi estää. 

## Ohjelmistot { #software }

Turvallisten ohjelmistojen ajaminen on myös erittäin tärkeää. Täysin turvallisen ohjelmiston kehittäminen ei ole triviaalitehtävä, mutta on olemassa yksinkertaisia keinoja, jotka auttavat. 

### Asenna vain luotettavista lähteistä { #only-install-from-reputable-sources }

Ole tarkkana asentamiesi ohjelmistojen lähteiden kanssa. Asenna ohjelmistoja vain luotettavista lähteistä. Käytä mahdollisuuksien mukaan jakelun paketinhallintaa (`yum`, `dnf`, `apt`, ...). Paketinhallinta helpottaa ohjelmistojen asennusta, päivittämistä ja poistamista. Jos haluttua ohjelmistoa ei ole jakelun pakettivarastossa, käytä virallista lähdettä. Seuraa tarvitsemasi ohjelmiston virallisella sivustolla annettuja ohjeita. Jos tarjolla on useampi lähde, harkitse sellaista, joka tarjoaa helpomman elinkaaren (asennus/päivitys/poisto/...), kuten [snap](https://en.wikipedia.org/wiki/Snap_(software)) tai [flatpak](https://en.wikipedia.org/wiki/Flatpak).

### Automaattiset ohjelmistopäivitykset { #automatic-software-updates }

Kaikissa käyttöjärjestelmissä on mahdollisuus asentaa päivityksiä automaattisesti. Säännöllisesti päivittämällä altistut vähemmän tunnetuille tietoturvaongelmille. Usein korjaus on saatavilla jo ennen kuin haavoittuvuudesta julkaistaan tietoa.

Centos 8:ssa ja uudemmissa käytössä on `dnf-automatic`:

```yaml
sudo yum install dnf-automatic -y
systemctl enable --now dnf-automatic-install.timer
```

`yum-cron` Centos 7:lle (ja vanhemmille RedHat-sukuisille jakeluille):

```yaml
sudo yum install yum-cron -y
sudo systemctl enable yum-cron.service
sudo systemctl start yum-cron.service
```

`unattended-upgrades` Ubuntulle:

```yml
sudo apt install unattended-upgrades
```

Jokaisessa käyttöjärjestelmäversiossa tämän aktivointi tapahtuu omalla tavallaan.

!!! info "Ytimen päivitykset" 

    Jotkin päivitykset, kuten ytimen päivitykset, vaativat virtuaalikoneiden uudelleenkäynnistyksen. Huomioi tämä säännöllisessä ylläpidossa.

Jos käyttötapauksesi ei tue automaattisia päivityksiä, mikä on yleistä korkean käytettävyyden ympäristöissä, varmista että aikataulutat säännölliset huoltoikkunat, joiden aikana ohjelmistopäivitykset tehdään.

* **Tilaa käyttöjärjestelmäsi tietoturvatiedotteet**, jos käyttöjärjestelmässäsi ilmenee tietoturvaongelma, sinun on saatava siitä tieto mahdollisimman pian. Voit tilata sopivan postituslistan, RSS-syötteen, ... pysyäksesi ajan tasalla kiireellisistä toimenpiteistä.

### Kiinnitä huomiota virtuaalikoneen käyttäjätileihin { #be-mindful-about-the-user-accounts-in-the-vm }

Pidä silmällä järjestelmässäsi käytössä olevia käyttäjätilejä. Jotkin sovellukset luovat oletustilejä, jotka ovat tarpeettomia tai jopa suoraan turvattomia. Ihanne voisi olla kolme tiliä:

* `root`, jolla ssh on pois käytöstä eikä salasanaa. Tämä on oletus [Poutan VM-kuvissa](images.md).
* Järjestelmänvalvojan käyttäjätili, johon pääsee vain SSH-avaimilla ja jolla on sudo-oikeudet. Poutan VM-kuvissa tämä käyttäjä on esiasetettuna; käyttäjän nimi riippuu jakelusta (`cloud-user`, `centos` tai `ubuntu`), katso lisätietoja yllä olevasta dokumentaatiosta.
* sekä käyttäjätason tilit, jotka ajavat yksittäistä palvelua eikä niillä ole kirjautumismahdollisuutta, ei etänä eikä paikallisesti. 

Älä salli salasanoilla kirjautumista, **käytä SSH-avaimia** sen sijaan. Salasanat voidaan riittävällä ajalla ja laskentateholla arvata brute force -hyökkäyksillä. Keskimääräinen SSH-palvelin kohtaa tuhansia tällaisia yrityksiä joka viikko. Kun käytät SSH-avaimia, käytössä on haaste-vastaus-todennus. Tämä tarkoittaa, että joka kirjautumisella esitetään eri haaste ja oikea vastaus on eri. Yhtään salaista tietoa (salasanaa tai avainta) ei koskaan siirry verkon yli 

Suojaa SSH-avaimesi salasanalla ja varmista, ettei avaimesi koskaan poistu laitteesta, jolla se luotiin.

* Älä tallenna julkisia avaimia (saati yksityisiä) VM:n luomiseen käytettävään imageen. Poutan pilvet tarjoavat metatietopalvelun, jonka avulla voit ladata julkiset avaimet käynnistyksen yhteydessä. Tätä suositellaan, sillä jos avaimesi vaarantuu, kyseisen avaimen käyttöoikeus voidaan poistaa kaikista käynnissä olevista instansseista, eikä uusi instanssi koskaan saa tätä julkista avainta.

### Pidä sovellustesi lokit { #keep-logs-of-your-applications }

Käytä lokituksessa parhaita käytäntöjä:

- Varmista, että palvelut lokittavat turvalliseen, mahdollisimman väärentämisen kestävään sijaintiin.
- Säilytä lokit kohtuullisen pitkään.
- Harkitse lokien lähettämistä myös etäpalvelimelle.

*Uudelleenkäytetty ystävällisellä luvalla lähteestä <a
href="https://support.ehelp.edu.au/support/solutions"
class="external-link">NeCTAR</a>.*