
# Kuinka siirtää tietosi toiseen projektiin SD Connectilla {#how-to-transfer-your-data-to-another-project-with-sd-connect}

<iframe width="400" height="225" srcdoc="https://www.youtube.com/embed/YE5_THNJEsw" title="Introducing CSC Sensitive Data Services" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Käyttötapaus {#use-case}
Sinulla (tiimi A) on tietojoukkoja, joihin toinen tiimi (tiimi B) tarvitsee pääsyn. He haluavat tarkastella tietojasi ja analysoida niitä omassa ympäristössään. Olet valmis antamaan heille kopion tietojoukostasi.

## Ratkaisu {#solution}
Tässä tapauksessa voit jakaa data-kansiosi tiimille B **Transfer data** -luvalla. Tämä antaa tiimin B jäsenille mahdollisuuden katsella tietojasi, kopioida ne ja ladata kopion itselleen. Tiimi B voi pitää oman kopiollisen analysointia varten vaikuttamatta alkuperäiseen tietojoukkoosi.

![Transfer Data Infograph](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_TransferData.png)

## Opas vaihe vaiheelta {#step-by-step-tutorial}

Molemmilla tiimeillä tulisi olla oma CSC-projektinsa ja SD Connect aktivoituna. Jos sinulla ei vielä ole, noudata ohjeita kohdasta [Aloita täällä](sd-access.md) ja palaa tähän oppaaseen sen jälkeen, kun olet luonut CSC-projektin.

1. Pyydä tiimiltä B heidän projektiensa Share ID:tä. He löytävät sen SD Connectista 
![(screenshot)](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareID.png)
2. Kirjaudu [SD Connect](./sd-connect-login.md).
3. Lataa data-kansiosi SD Connectiin: [Katso latausohjeet](./sd-connect-upload.md).
4. Klikkaa “**Share**” haluamasi kansion vierestä.
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareButton.png)
5. Lisää Projektin B **Share ID** kenttään.
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_AddShareID.png)
6. Valitse jakolupa: “**Transfer data**”. Klikkaa “**Share**”.
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_SelectPermission.png)

Nyt kansion koko sisältö on näkyvissä Projektille B. Kaikki Projektin B jäsenet voivat kopioida, ladata ja purkaa kansion sisällön SD Connectin kautta. He voivat myös käyttää sitä SD Desktopin kautta analysointia varten. He eivät kuitenkaan voi muokata alkuperäistä kansiotasi.

## SD Connectin ominaisuudet {#features-in-sd-connect}

* [Lataa](./sd-connect-upload.md)
* [Jaa](./sd-connect-share.md)
* [Lataa](./sd-connect-download.md)
* [Poista](./sd-connect-delete.md)

