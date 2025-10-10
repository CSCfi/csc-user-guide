[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Virtuaalityöpöydän käyttäminen { #accessing-virtual-desktop }


* [Siirry virtuaalityöpöydälle](#access-virtual-desktop)
* [Kirjaudu ulos virtuaalityöpöydältä](#log-out-from-virtual-desktop)
* [Uudelleenyhdistäminen analyysisessioon](#reconnecting-to-an-analysis-session)


## Siirry virtuaalityöpöydälle { #access-virtual-desktop }

1. [Kirjaudu](./sd-desktop-login.md) SD Desktopiin. Kaikki virtuaalityöpöytäsi on listattu etusivulla kohdassa **All connections**.

2. Valitse projekti (esim. `project_NNNNN`) ja napsauta **plus-kuvaketta**.
  
3. Näet nyt kaikki tähän projektiin kuuluvat työpöydät (`desktopname-NNNNNNNNNN`). Avaa virtuaalityöpöytä napsauttamalla nimeä.

Kun avaat yhteyden, virtuaalinen laskentaympäristö avautuu selaimeesi. Jos käytät virtuaalityöpöytää ensimmäistä kertaa, näet aloituspaneelin, josta voit esimerkiksi säätää näytön resoluutiota.

![Kaikki yhteydet](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_AllConnections.png)


## Kirjaudu ulos virtuaalityöpöydältä { #log-out-from-virtual-desktop }

1. Napsauta työpöydän oikeassa yläkulmassa olevaa **Power-kuvaketta**. 
2. Valitse **Power Off/Log out**, sitten **Log Ou**t.
3. Valitse uudessa ikkunassa **Log Out**.
4. Valitse **Home** palataksesi SD Desktopin etusivulle. 

Tämä sulkee kaikki sovellukset ja katkaisee työistunnon. Pääset samalle työpöydälle milloin tahansa uudelleen kirjauduttuasi palveluihin.

![Kirjaudu ulos työpöydältä](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LogOut1.png)

![Palaa päänäkymään](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LogOut2.png)

## Uudelleenyhdistäminen analyysisessioon { #reconnecting-to-an-analysis-session }

* **Selaimen ikkunan sulkeminen:** Jos käynnistit analyysin ohjelmallisesti (esim. ajamalla skriptin), voit sulkea selainikkunan keskeyttämättä käynnissä olevia prosesseja. Työkalut ja käyttöliittymät pysyvät avoinna, kun yhdistät työpöydällesi uudelleen, jolloin voit jatkaa työskentelyä.
* **Yhdistäminen vanhaan istuntoon:** Voit yhdistää aiempaan istuntoon vain, jos selainikkuna on täsmälleen saman kokoinen kuin alkuperäistä istuntoa käytettäessä. Tämä on tyypillisesti mahdollista vain, jos käytät SD Desktopia koko näytön tilassa samalla laitteella. Jos ikkunan koko on muuttunut, et todennäköisesti voi yhdistää vanhaan istuntoon.

!!! Note
    Yhteysrajoitus: kukin virtuaalityöpöytä sallii enintään 10 samanaikaista yhteyttä. Tämä tarkoittaa, että enintään 10 CSC-projektin jäsentä voi olla yhtä aikaa kirjautuneena ja käyttämässä järjestelmää. Jos yli 10 CSC-projektin jäsentä yrittää yhdistää samaan virtuaalityöpöytään, ylimääräiset käyttäjät eivät pääse järjestelmään ennen kuin jokin aktiivisista istunnoista katkaistaan.
    Jos yhteys pysyy passiivisena kahtena peräkkäisenä päivänä, järjestelmä kirjaa käyttäjän automaattisesti ulos resurssien vapauttamiseksi. Varmistathan, että kirjaudut ulos manuaalisesti, kun olet valmis, jotta tämä vältetään.

## Seuraavat vaiheet tässä oppaassa { #your-next-steps-in-this-guide }

* [Työskentely työpöydällä: vinkit ja perusasiat](./sd-desktop-working.md)
* [Mukauttaminen – ohjelmistot ja työkalut](./sd-desktop-software.md)
* [Tietojen tuonti ](./sd-desktop-access.md)
* [Datan vienti  käyttöliittymän kautta](./sd-desktop-export.md)
* [Datan vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)