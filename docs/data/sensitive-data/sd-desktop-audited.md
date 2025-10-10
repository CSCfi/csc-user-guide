[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Sensitive Data Desktop terveys- ja sosiaalidatan toissijaiseen käyttöön { #sensitive-data-desktop-for-secondary-use-of-health-and-social-data }

Sensitive Data (SD) Desktop on rekisteröity ympäristö terveys- ja sosiaalidatan (rekisteriaineistojen) toissijaiseen käyttöön. Pääsy palveluun edellyttää lupaa rekisterinpitäjältä, joka voi olla Findata tai yksittäinen rekisterinpitäjä. SD Desktop on selainkäyttöliittymä, jonka avulla voit hallita (käynnistää, käyttää, poistaa) virtuaalista työpöytää (teknisesti virtuaalikone) suoraan verkkoselaimestasi. Virtuaalityöpöydän kautta pääset käsiksi luvitettuihin aineistoihin. Palvelun käyttö ei edellytä aiempaa pilvilaskennan tuntemusta tai ohjelmointiosaamista.

Sisältö:

 * [Keskeiset ominaisuudet](./sd-desktop-audited.md#key-features)

 * [Rajoitukset](./sd-desktop-audited.md#limitations)

 * [Ennen kuin aloitat](./sd-desktop-audited.md#before-you-start) 

    
## Keskeiset ominaisuudet { #key-features }

* Auditoitu Findatan määräysten mukaisesti.

* Käytettävissä miltä tahansa käyttöjärjestelmältä (Mac, Linux tai Windows) web-selaimen (esim. Google Chrome, Firefox) kautta julkisesta internetistä (ilman erillistä asiakasohjelmaa tai VPN:ää).

* Vain saman CSC-projektin jäsenet voivat käyttää samaa virtuaalityöpöytää.

* Kirjautumisen jälkeen käyttäjä voi käynnistää valmiiksi rakennetun laskentaympäristön (Linux Ubuntu -käyttöjärjestelmä) tarpeen mukaan; tarjolla olevat vaihtoehdot mahdollistavat kaiken yksinkertaisesta tilastollisesta analyysistä koneoppimiseen.

* Sääntelyn noudattamiseksi toissijaisen käytön virtuaalityöpöydät on eristetty täysin internetistä ja muista palveluista: pääset käsiksi vain niihin aineistoihin, joita olet pyytänyt rekisterinpitäjältä;

* SD Desktopia voidaan käyttää kaiken tyyppisten aineistojen käsittelyyn: tekstitiedostot, kuvat, äänitiedostot, video ja geneettinen data. Virtuaalityöpöydällä on kuitenkin [rajoitettu valikoima valmiiksi asennettua ohjelmistoa](../../data/sensitive-data/sd-desktop-secondary-working.md#default-software-available-in-sd-desktop) (avoimen lähdekoodin). Lisäohjelmistojen asentaminen virtuaalityöpöydälle on rajoitettua. Ota aina yhteyttä servicedesk@csc.fi ohjelmistotarpeista ennen kuin aloitat aineistojen parissa työskentelyn.

## Rajoitukset { #limitations }

* Sääntelyn noudattamiseksi toissijaisen käytön SD Desktop on täysin eristetty internetistä ja muista palveluista. Voit esimerkiksi avata Firefox-selaimen, mutta et pääse millekään verkkosivulle.

* **Datan ja ohjelmistojen tuonti SD Desktopiin on rajoitettua**. Et voi turvallisuussyistä tuoda itse mitään dataa tai ohjelmistoja. Jos työskentelet aineiston kanssa, johon olet saanut luvan rekisterinpitäjältä, ainoa tapa päästä analysoitavan datan äärelle on käyttää erillistä sovellusta nimeltä **Data Gateway**. 

* **Datan vienti SD Desktopista on myös rajoitettua**. Vain ei-sensitiivisiä tuloksia voidaan viedä työtilasta, ja viennin voi tehdä ainoastaan CSC-projektin vastuuhenkilö. Ohjeet tulosten vientiin esitetään seuraavassa kappaleessa.


* Lopuksi: emme toistaiseksi tarjoa Windows-käyttöjärjestelmällä tai GPU:illa varustettua virtuaalityöpöytää. 

## Ennen kuin aloitat { #before-you-start }

* Sinulla tulee olla Findatan tai yksittäisen rekisterinpitäjän myöntämä tietolupa ennen kuin aloitat palveluun pääsyn hakemisen CSC:ssä.

* Kaikki tiettyyn CSC-projektiin kuuluvat jäsenet voivat käyttää samaa laskentaan tarkoitettua virtuaalityöpöytää. Tällä hetkellä kunkin CSC-projektin puitteissa on mahdollista käynnistää 3 virtuaalityöpöytää (tai laskentaympäristöä). Jokaisella CSC-projektilla on oma yksityinen työpöytänsä, ja kukin työpöytä on eristetty muista CSC-projekteista ja -tileistä.

* Auditoinnin läpäisseessä SD Desktopissa on joitakin tärkeitä rajoituksia: CSC-projektia hallinnoi Service Desk, ja tiedonsiirto on rajoitettua (mukaan lukien käyttäjien omat skriptit ja ohjelmat).

* Kun tietolupasi vanhenee, et enää pääse virtuaalityöpöydällesi. Jos haluat jatkaa työskentelyä saman projektin parissa, sinun on lähetettävä muutoshakemus rekisterinpitäjälle. Muussa tapauksessa pyydä kaikkien tulostesi vienti ennen tietolupasi voimassaolon päättymistä. Vanhentunut projekti ja kaikki data poistetaan 90 päivän kuluttua CSC:n tietojen säilytyspolitiikan mukaisesti.

!!! Note
    Suosittelemme, että **[otat yhteyttä CSC Service Deskiin](../../support/contact.md) hyvissä ajoin**, jopa ennen tietoluvan hakemista, jos tarvitset ohjelmistoa, jota ei ole oletuksena saatavilla työpöydällä.