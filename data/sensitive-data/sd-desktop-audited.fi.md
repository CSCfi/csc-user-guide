# Sensitive Data Desktop for secondary use of health and social data {#sensitive-data-desktop-for-secondary-use-of-health-and-social-data}

Sensitive Data (SD) Desktop on rekisteröity ympäristö sosiaali- ja terveysalan tietojen toissijaiseen käyttöön (rekisteritiedot). Palvelun käyttö edellyttää tietosuojavastaavalta saatua lupaa, jonka myöntäjänä voi olla Findata tai yksittäinen rekisteri. SD Desktop on selainkäyttöinen käyttöliittymä, jonka kautta voit hallita (käynnistää, käyttää, poistaa) virtuaalityöpöytää (teknisesti määriteltynä virtuaalikone), suoraan selaimen kautta. Virtuaalityöpöydällä pääset käsiksi niihin aineistoihin, joihin olet saanut luvan. Pilvipalveluiden tai ohjelmoinnin osaamista ei vaadita palvelun käyttöön.

Sisältö:

 * [Keskeiset ominaisuudet](./sd-desktop-audited.md#key-features)

 * [Rajoitukset](./sd-desktop-audited.md#limitations)

 * [Ennen kuin aloitat](./sd-desktop-audited.md#before-you-start) 


## Keskeiset ominaisuudet {#key-features}

* Auditointi Findatan sääntelyn mukaisesti.

* Käytettävissä miltä tahansa käyttöjärjestelmältä (Mac, Linux tai Windows) web-selaimen (esim. Google Chrome, Firefox) kautta julkisesta internetistä (ei vaadi erillisen ohjelmiston asennusta tai VPN-yhteyden käyttöä).

* Vain saman CSC-projektin jäsenet voivat käyttää samaa virtuaalityöpöytää.

* Kirjauduttuaan SD Desktopiin käyttäjä voi käynnistää valmiiksi rakennetun laskentaympäristön (Linux Ubuntu -käyttöjärjestelmä) tarpeen mukaan; saatavilla olevat vaihtoehdot mahdollistavat yksinkertaisesta tilastollisesta analyysista koneoppimiseen.

* Sääntelyn noudattamiseksi toissijaisen käytön virtuaalityöpöydät on täysin eristetty internetistä ja muista palveluista: pääset vain niihin tietoihin, joihin olet saanut luvan tietosuojavastaavalta;

* SD Desktopia voi käyttää kaikenlaisen datan käsittelyyn: tekstitiedostot, kuvat, äänitiedostot, videot ja geneettiset aineistot. Virtuaalityöpöydällä on kuitenkin [rajoitettu valikoima valmiiksi asennettua ohjelmistoa](../../data/sensitive-data/sd-desktop-secondary-working.md#default-software-available-in-sd-desktop) (avoin lähdekoodi). Lisäohjelmistojen asentaminen virtuaalityöpöydälle on rajoitettua. Ota aina yhteyttä servicedesk@csc.fi, jos tarvitset ohjelmistoja ennen kuin aloitat datan kanssa työskentelyn.

## Rajoitukset {#limitations}

* Sääntelyn noudattamiseksi SD Desktop toissijaista käyttöä varten on **täysin eristetty internetistä ja muista palveluista**. Voit esimerkiksi avata Firefox-selaimen, mutta et pääse millekään verkkosivulle.

* **Datan ja ohjelmistojen tuonti SD Desktopiin on rajoitettua.** Et voi itse tuoda dataa tai ohjelmistoja turvallisuussyistä. Jos työskentelet aineiston kanssa, johon sinulla on lupa tietosuojavastaavalta, voit analysoida tietoja vain hyödyntämällä erityistä sovellusta nimeltä **Data Gateway**.

* **Myös datan vienti SD Desktopista on rajoitettua.** Vain *ei-arkaluonteisia* tuloksia voidaan viedä työtilasta, ja vain CSC-projektipäällikkö voi viedä tulokset. Ohjeet tulosten vientiin löydät seuraavasta kappaleesta.

* Lisäksi emme tällä hetkellä tarjoa virtuaalityöpöytää Windows-käyttöjärjestelmällä tai grafiikkakiihdyttimellä (GPU).

## Ennen kuin aloitat {#before-you-start}

* Sinulla on oltava Findatan tai yksittäisen rekisterin myöntämä käyttölupa, ennen kuin aloitat palvelun käyttöprosessin CSC:llä.

* Kaikki saman CSC-projektin jäsenet pääsevät käyttämään samaa virtuaalista laskentaympäristöä. Tällä hetkellä jokaiselle CSC-projektille voi avata 3 virtuaalista työpöytää (tai laskentaympäristöä). Jokaisella CSC-projektilla on oma työpöytänsä, ja jokainen työpöytä on eristetty muista projekteista ja CSC-tunnuksista.

* Auditointia läpikäynyt SD Desktopissa on muutamia tärkeitä rajoituksia: CSC-palvelupiste hallinnoi projektia ja datan siirto on rajoitettua (sisältäen käyttäjän omat skriptit ja ohjelmat).

* Kun käyttölupasi umpeutuu, et enää pääse käyttämään virtuaalityöpöytääsi. Jos haluat jatkaa samassa projektissa, sinun tulee lähettää muutoshakemus tietosuojavastaavalle. Muussa tapauksessa varmista, että pyydät kaikkien tulostesi viennin ennen kuin käyttölupasi voimassaoloaika päättyy. Vanhentunut projekti ja kaikki aineisto poistetaan 90 päivän jälkeen CSC:n tietojen säilytyskäytännön mukaisesti.

!!! Huom
    Suosittelemme olemaan **[yhteydessä CSC Service Deskiin](../../support/contact.md) hyvissä ajoin**, jo ennen käyttölupahakemuksen tekemistä, jos tarvitset **ohjelmistoa, joka ei kuulu Desktopin oletusvalikoimaan**.