# Virtuaalisen työpöydän käyttäminen {#accessing-virtual-desktop}

* [Virtuaalisen työpöydän käyttöönotto](#access-virtual-desktop)
* [Kirjaudu ulos virtuaalisesta työpöydästä](#log-out-from-virtual-desktop)
* [Yhteyden muodostaminen uudelleen analyysisessioon](#reconnecting-to-an-analysis-session)

## Virtuaalisen työpöydän käyttöönotto {#access-virtual-desktop}

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. Kaikki virtuaaliset työpöytäsi on esitetty etusivulla kohdan **Kaikki yhteydet** alla.

2. Valitse projekti (esim. `project_NNNNN`) ja napsauta **plus-ikonia**.
  
3. Nyt voit nähdä kaikki tähän projektiin kuuluvat työpöydät (`desktopname-NNNNNNNNNN`). Käytä virtuaalista työpöytää napsauttamalla nimeä.

Kun avaat yhteyden, virtuaalinen laskentaympäristö avautuu selaimeesi. Jos käytät virtuaalista työpöytää ensimmäistä kertaa, näet aloituspaneelin, josta voit esimerkiksi säätää näytön tarkkuutta.

![Kaikki yhteydet](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_AllConnections.png)

## Kirjaudu ulos virtuaalisesta työpöydästä {#log-out-from-virtual-desktop}

1. Napsauta **virta-ikonia** työpöydän oikeassa yläkulmassa.
2. Valitse **Virta pois/pieni** ja sitten **Kirjaudu ulos**.
3. Valitse **Kirjaudu ulos** uudessa ikkunassa.
4. Valitse **Koti** palataksesi SD Desktopin etusivulle.

Tämä sulkee kaikki sovellukset ja katkaisee istunnon. Voit käyttää samaa työpöytää milloin tahansa kirjautumalla palveluun uudelleen.

![Kirjaudu ulos työpöydältä](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LogOut1.png)

![Palaa päänäkymään](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LogOut2.png)

## Yhteyden muodostaminen uudelleen analyysisessioon {#reconnecting-to-an-analysis-session}

* **Selaimen ikkunan sulkeminen:** Jos aloitit analyysin ohjelmallisesti (esim. suorittamalla skriptin), voit sulkea selainikkunan keskeyttämättä meneillään olevia prosesseja. Työkalut ja käyttöliittymät pysyvät avoinna, kun muodostat yhteyden työpöytääsi uudelleen, jolloin voit jatkaa työskentelyä.
* **Yhteyden muodostaminen vanhaan istuntoon:** Voit muodostaa yhteyden aiempaan istuntoon vain, jos selainikkuna on täsmälleen saman kokoinen kuin silloin, kun alkuperäinen istunto oli käytössä. Tämä on yleensä mahdollista vain, jos käytät SD Desktopia koko näytön tilassa samalla koneella. Jos ikkunan koko on muuttunut, et todennäköisesti voi muodostaa yhteyttä vanhaan istuntoon.

!!! Huom
    Yhteysrajoitus: jokainen virtuaalinen työpöytä sallii enintään 10 samanaikaista yhteyttä. Tämä tarkoittaa, että enintään 10 CSC-projektin jäsentä voi olla kirjautuneena ja käyttää järjestelmää samaan aikaan. Jos yli 10 CSC-projektin jäsentä yrittää muodostaa yhteyttä samaan virtuaaliseen työpöytään, muut käyttäjät eivät voi käyttää järjestelmää ennen kuin jokin aktiivisista istunnoista katkaistaan.
    Jos yhteys pysyy epäaktiivisena kaksi peräkkäistä päivää, järjestelmä kirjautuu automaattisesti ulos käyttäjästä vapauttaakseen resursseja. Varmista, että kirjaudut ulos manuaalisesti, kun olet valmis, jotta tämä ei tapahdu.

## Seuraavat vaiheet tässä oppaassa {#your-next-steps-in-this-guide}

* [Työpöydän käyttäminen: vinkit ja perusteet](./sd-desktop-working.md)
* [Mukauttaminen - ohjelmisto ja työkalut](./sd-desktop-software.md)
* [Tietojen tuonti](./sd-desktop-access.md)
* [Tietojen vieminen käyttöliittymän kautta](./sd-desktop-export.md)
* [Tietojen vieminen ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)