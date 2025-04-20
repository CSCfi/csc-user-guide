# Virtuaalityöpöydän käyttäminen {#access-virtual-desktop}

* [Virtuaalityöpöydän käyttäminen](#access-virtual-desktop)
* [Kirjaudu ulos virtuaalityöpöydältä](#log-out-from-virtual-desktop)
* [Yhdistäminen analyysikertaan uudelleen](#reconnecting-to-an-analysis-session)

## Virtuaalityöpöydän käyttäminen {#access-virtual-desktop}

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktop -palveluun. Kaikki virtuaalityöpöytäsi näkyvät etusivulla kohdassa **Kaikki yhteydet**.

2. Valitse projekti (esim. `project_NNNNN`) ja napsauta **plus-kuvaketta**.

3. Nyt näet kaikki tähän projektiin kuuluvat työpöydät (`desktopname-NNNNNNNNNN`). Käytä virtuaalityöpöytää napsauttamalla sen nimeä.

Kun avaat yhteyden, selaimeen avautuu virtuaalinen laskentaympäristö. Jos käytät virtuaalityöpöytää ensimmäistä kertaa, näet aloituspaneelin, josta voit esimerkiksi säätää näytön tarkkuutta.

![Kaikki yhteydet](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_AllConnections.png)

## Kirjaudu ulos virtuaalityöpöydältä {#log-out-from-virtual-desktop}

1. Napsauta **virta-kuvaketta** työpöydän oikeassa yläkulmassa.
2. Valitse **Sammuta/Kirjaudu ulos** ja sen jälkeen **Kirjaudu ulos**.
3. Valitse uudessa ikkunassa **Kirjaudu ulos**.
4. Valitse **Etusivu** palataksesi SD Desktopin etusivulle.

Tämä sulkee kaikki sovellukset ja katkaisee työskentelyistunnon. Voit käyttää samaa työpöytää halutessasi myöhemmin, kun olet kirjautunut palveluun uudelleen.

![Kirjaudu ulos työpöydältä](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LogOut1.png)

![Palaa päänäkymään](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LogOut2.png)

## Yhdistäminen analyysikertaan uudelleen {#reconnecting-to-an-analysis-session}

* **Selaimen ikkunan sulkeminen:** Jos aloitit analyysin ohjelmallisesti (esim. ajamalla skriptin), voit turvallisesti sulkea selainikkunan ilman, että käynnissä olevat prosessit keskeytyvät. Työkalusi sekä käyttöliittymät pysyvät auki, kun yhdistät uudelleen työpöytääsi ja voit jatkaa työskentelyäsi.
* **Uudelleen yhdistäminen vanhaan istuntoon:** Voit yhdistää aiempaan istuntoon vain, jos selainikkunan koko on täsmälleen sama kuin käytettäessä alkuperäistä istuntoa. Tämä onnistuu tyypillisesti vain silloin, kun käytät SD Desktopia kokoruututilassa samalla koneella. Jos ikkunan koko on muuttunut, et todennäköisesti voi yhdistää vanhaan istuntoon.

!!! Huom
    Yhteysrajoitus: jokaiselle virtuaalityöpöydälle sallitaan enintään 10 samanaikaista yhteyttä. Tämä tarkoittaa, että korkeintaan 10 CSC-projektin jäsentä voi olla kirjautuneena ja käyttää järjestelmää samaan aikaan. Jos yli 10 CSC-projektin jäsentä yrittää yhdistää samaan virtuaalityöpöytään, ylimääräiset käyttäjät eivät pääse palveluun, ennen kuin yksi aktiivisista istunnoista lopettaa.
    Jos yhteys pysyy käyttämättömänä kaksi vuorokautta peräkkäin, järjestelmä kirjaa käyttäjän automaattisesti ulos vapauttaakseen resursseja. Muista kirjautua ulos käsin työskentelyn päätyttyä välttääksesi tämän.

## Seuraavat askeleesi tässä oppaassa {#your-next-steps-in-this-guide}

* [Työskentely työpöydällä: vinkit ja oleelliset asiat](./sd-desktop-working.md)
* [Mukauttaminen – ohjelmistot & työkalut](./sd-desktop-software.md)
* [Datan tuonti](./sd-desktop-access.md)
* [Datan vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Datan vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)