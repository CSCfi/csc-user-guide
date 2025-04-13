
# Tietojen lataaminen ja salaaminen {#uploading-and-encrypting-data}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SMnEkcS_HJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Tietosi salataan automaattisesti, kun lataat tietoja SD Connectiin. Tämä sopii kaikille tiedostotyypeille ja -muodoille, mutta on tuettu vain tiedostoille, joiden koko on enintään 100 GB, ja kansioille, jotka ovat pienempiä kuin 1 TB. Suurempia tiedostoja tai kansioita voidaan ladata [ohjelmallisesti](./sd-connect-command-line-interface.md).

!!! Huomautus
    Jos käytät palvelua ensimmäistä kertaa, selaimessasi saattaa ilmestyä ponnahdusikkuna, joka pyytää sinua hyväksymään evästeet. Ole hyvä ja klikkaa Hyväksy, jotta tiedostojen ja kansioiden lataaminen mahdollistuu.

## Lataaminen ja tiedostojen salaaminen uuteen kansioon {#upload-and-encrypt-files-to-a-new-folder}

1. Kirjaudu SD Connectiin.
2. Valitse oikea CSC-projekti vasemmasta yläkulmasta.
3. Napsauta **Lataa** oikeassa yläkulmassa.
4. Uudessa ikkunassa nimeä tiedostojesi kohdekansio.
5. Napsauta **Valitse tiedostot** avataksesi selainikkunan ja valitse tiedostot ladattavaksi. Jos haluat ladata kansioita, vedä ja pudota ne ikkunaan. Napsauta **Lataa**, jotta automaattinen salaus ja lataus alkaa.
6. Ilmoitus latauksen tilasta ilmestyy ja on näkyvissä, kunnes lataus on valmis. Ilmoitus sisältää myös linkin kohdekansioon.
7. Kun lataus on valmis, salatut tiedostot ovat saatavilla ladattavaksi ja jaettavaksi SD Connectin kautta tai analysointia, muokkausta tai merkintöjen lisäämistä varten SD Desktopin kautta.

!!! Info "Kansioiden nimet"

    - Kansion nimien on oltava yksilöllisiä kaikissa olemassa olevissa kansioissa kaikissa projekteissa SD Connectissä ja Allaksessa (pilvitallennusratkaisu, jonka pohjalta SD Connect on kehitetty). Jos et voi luoda uutta kansiota, joku toinen projekti saattaa jo käyttää valitsemaasi nimeä. Tämän tilanteen välttämiseksi on hyvä käyttää projektikohtaisia tunnisteita (esimerkiksi projektin ID-numero tai lyhenne) kansion nimessä.
    - Vältä välilyöntejä ja erikoismerkkejä; käytä latinalaisia aakkosia (a-z), numeroita (0-9), väliviivaa (-), alaviivaa (_) ja pistettä (.). Muista, että kaikki kansion nimet ovat julkisia; älä sisällytä mitään luottamuksellisia tietoja.
    - Kansion nimiä ei voi muokata jälkeenpäin.

## Lataaminen ja tiedostojen salaaminen olemassa olevaan kansioon {#upload-and-encrypt-files-to-an-existing-folder}

1. Valitse oikea kansio (tuplaklikkaamalla).
2. Napsauta **Lataa** oikeassa yläkulmassa ja noudata yllä olevan kappaleen vaiheita 4–6.

!!! Varoitus "Varoitus"

    Samassa CSC-projektissa olevat jäsenet voivat ladata ja purkaa tietoja SD Connectista. Tämä voidaan rajoittaa jakamalla tiedostoja **Vain luku SD Desktopiin** -oikeudella. [Lisätietoa käyttöesimerkistä](./sd-connect-share-read-to-sd-desktop.md)

!!! Huomautus "Lisähuomioita"

    - Suurten tiedostojen (> 100 GB) lataaminen voi kestää tunteja, ja lataus keskeytyy 8 tunnin jälkeen.
    - Käyttöliittymä voi hidastua, kun kussakin kansiossa on yli 2500 tiedostoa. Tässä tapauksessa käytä [komentorivityökaluja lataamiseen ja automaattiseen avainten hallintaan](./sd-connect-command-line-interface.md). 
    - Tiedostoja ei voi muokata SD Connectissä; lataa ne muokattaviksi tai käytä niitä SD Desktopin kautta.
    - Tiedostojen lataaminen alikansioihin ei ole tällä hetkellä tuettua.
    - SD Connect näyttää salatut tiedostosi virtuaalisina kansioina. Suunnittele kansiorakenteesi huolellisesti — järjestele tiedostoja projektien, teemojen tai loogisten rakenteiden mukaan parantaaksesi saavutettavuutta ja työnkulkua. Tämä auttaa myös, kun jaat käyttöoikeuksia muille. Lisäapua saa CSC:n asiakaspalvelusta (aihe: Arkaluontoiset tiedot).

## Ominaisuudet SD Connectissä {#features-in-sd-connect}

* [Lataaminen](./sd-connect-upload.md)
* [Jakaminen](./sd-connect-share.md)
* [Lataaminen alas](./sd-connect-download.md)
* [Poistaminen](./sd-connect-delete.md)
* [Komentorivikäyttöliittymä](./sd-connect-command-line-interface.md)
* [Vianmääritys](./sd-connect-troubleshooting.md)
