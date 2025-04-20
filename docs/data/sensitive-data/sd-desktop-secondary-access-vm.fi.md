# Virtuaalityöpöydän käyttäminen {#access-virtual-desktop}

* [Siirry virtuaalityöpöydälle](#access-virtual-desktop)
* [Kirjaudu ulos virtuaalityöpöydältä](#log-out-from-virtual-desktop)
* [Yhdistä uudelleen analyysisessioon](#reconnecting-to-an-analysis-session)

## Siirry virtuaalityöpöydälle {#access-virtual-desktop}

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. Kaikki virtuaalityöpöytäsi löytyvät kotisivun **Kaikki yhteydet** -kohdasta.

2. Valitse projekti (esim. `project_NNNNN`) ja napsauta **plus-kuvaketta**.

3. Nyt voit nähdä kaikki työpöydät, jotka kuuluvat tähän projektiin (`desktopname-NNNNNNNNNN`). Siirry virtuaalityöpöydälle napsauttamalla nimeä.

Kun avaat yhteyden, selain avaa virtuaalisen laskentaympäristön. Jos käytät virtuaalityöpöytää ensimmäistä kertaa, näet aloituspaneelin, josta voit esimerkiksi säätää näytön tarkkuutta.

![All connections](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_AllConnections.png)

## Kirjaudu ulos virtuaalityöpöydältä {#log-out-from-virtual-desktop}

1. Napsauta **virta-kuvaketta** työpöydän oikeassa yläkulmassa.
2. Valitse **Sammuta / kirjaudu ulos**, ja valitse sitten **Kirjaudu ulos**.
3. Valitse uudessa ikkunassa **Kirjaudu ulos**.
4. Valitse **Koti** palataksesi SD Desktopin kotisivulle.

Tämä sulkee kaikki sovellukset ja katkaisee työistunnon. Voit käyttää samaa työpöytää milloin tahansa kirjautumalla uudelleen palveluun.

![Log out from desktop](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LogOut1.png)

![Return to main view](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LogOut2.png)

## Yhdistä uudelleen analyysisessioon {#reconnecting-to-an-analysis-session}

* **Selaimen ikkunan sulkeminen:** Jos olet käynnistänyt analyysin ohjelmallisesti (esim. suorittamalla skriptin), voit turvallisesti sulkea selainikkunan ilman, että käynnissä olevat prosessit keskeytyvät. Työkalut ja käyttöliittymät pysyvät auki, kun yhdistät uudelleen työpöytääsi ja voit jatkaa työskentelyä.
* **Yhdistäminen vanhaan istuntoon:** Voit yhdistää uudelleen aiempaan istuntoon vain, jos selainikkunan koko on täsmälleen sama kuin alkuperäisen istunnon aikana. Tämä on tyypillisesti mahdollista vain, jos käytät SD Desktopia koko näytön tilassa samalla laitteella. Jos ikkunan koko on muuttunut, et todennäköisesti pysty yhdistämään vanhaan istuntoon.

!!! Note
    Yhteysrajoitus: jokainen virtuaalityöpöytä sallii korkeintaan 10 samanaikaista yhteyttä. Tämä tarkoittaa, että enintään 10 CSC-projektin jäsentä voi olla kirjautuneena ja käyttämässä järjestelmää yhtä aikaa. Jos yli 10 CSC-projektin jäsentä yrittää yhdistää samaan virtuaalityöpöytään, ylimääräiset käyttäjät eivät pääse palveluun, ennen kuin joku aktiivista istunnoista katkaisee yhteytensä.
    Jos yhteys pysyy passiivisena kaksi peräkkäistä päivää, järjestelmä kirjaa käyttäjän automaattisesti ulos vapauttaakseen resursseja. Muista siis kirjautua ulos käsin, kun lopetat työskentelyn, jotta vältät tämän.

## Seuraavat askeleesi tässä oppaassa {#your-next-steps-in-this-guide}

* [Työpöydän käyttö: vinkkejä ja perusasiat](./sd-desktop-working.md)
* [Muokkaus – ohjelmat ja työkalut](./sd-desktop-software.md)
* [Datan tuonti](./sd-desktop-access.md)
* [Datan vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Datan vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianetsintä](./sd-desktop-troubleshooting.md)