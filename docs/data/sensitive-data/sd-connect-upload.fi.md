# Datan lataaminen ja salaus {#uploading-and-encrypting-data}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SMnEkcS_HJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Tietosi salataan automaattisesti, kun lataat dataa SD Connectiin. Tämä sopii kaikille tiedostotyypeille ja -muodoille, mutta sitä tuetaan vain tiedostoille, jotka ovat enintään 100 GB, ja kansioille, jotka ovat pienempiä kuin 1 TB. Suuremmat tiedostot tai kansiot voi ladata [ohjelmallisesti](./sd-connect-command-line-interface.md).

!!! Note
    Jos käytät palvelua ensimmäistä kertaa, selaimeesi voi ilmestyä ponnahdusikkuna, joka pyytää hyväksymään evästeet. Klikkaa Hyväksy, jotta tiedostojen ja kansioiden lataaminen voidaan sallia.

## Lataa ja salaa tiedostoja uuteen kansioon {#upload-and-encrypt-files-to-a-new-folder}

1. Kirjaudu sisään SD Connectiin.
2. Valitse oikea CSC-projekti vasemmasta yläkulmasta.
3. Klikkaa **Lataa** oikeasta yläkulmasta.
4. Uudessa ikkunassa nimeä kohdekansio tiedostoillesi.
5. Klikkaa **Valitse tiedostot** avataksesi selainikkunan ja valitse lataettavat tiedostot. Jos haluat ladata kansioita, raahaa ja pudota ne ikkunaan. Klikkaa **Lataa** käynnistääksesi automaattisen salauksen ja latauksen.
6. Ilmoitus latauksen tilasta tulee näkyviin ja pysyy näkyvillä, kunnes lataus on valmis. Ilmoituksessa on myös linkki kohdekansioon.
7. Kun lataus on päättynyt, salatut tiedostot ovat käytettävissä latausta ja jakamista varten SD Connectin kautta tai analysointiin, muokkaukseen tai annotointiin SD Desktopin kautta.

!!! info "Kansion nimet"

    - Kansion nimien tulee olla yksilöllisiä kaikissa olemassa olevissa kansioissa kaikissa projekteissa SD Connectissa ja Allaksessa (pilvitallennusratkaisu, johon SD Connect perustuu). Jos et voi luoda uutta kansiota, valitsemasi nimi saattaa olla jo toisen projektin käytössä. Tämän välttämiseksi kannattaa lisätä projektiin liittyvä tunniste (esim. projekti-ID tai lyhenne) kansion nimeen.
    - Vältä välilyöntejä ja erikoismerkkejä; käytä latinalaisia aakkosia (a-z), numeroita (0-9), tavuviivaa (-), alaviivaa (_) ja pistettä (.). Muista, kaikki kansionimet ovat julkisia; älä siis sisällytä niihin luottamuksellisia tietoja.
    - Kansion nimeä ei voi muuttaa jälkikäteen.

## Lataa ja salaa tiedostoja olemassa olevaan kansioon {#upload-and-encrypt-files-to-an-existing-folder}

1. Valitse oikea kansio (kaksoisklikkaamalla).
2. Klikkaa **Lataa** oikeasta yläkulmasta ja noudata yllä olevan kappaleen kohtia 4–6.

!!! warning "Varoitus"

    Saman CSC-projektin jäsenet voivat ladata ja purkaa tietoja SD Connectista. Tätä voi rajoittaa jakamalla tiedostoja **Read to SD Desktop** -oikeudella. [Lue käyttötapaus](./sd-connect-share-read-to-sd-desktop.md)

!!! Note "Lisähuomiot"

    - Suurten tiedostojen (> 100 GB) lataaminen voi kestää useita tunteja, ja lataukset keskeytyvät 8 tunnin kuluttua.
    - Käyttöliittymä voi hidastua, jos kansiossa on yli 2500 tiedostoa. Tässä tapauksessa käytä [komentorivityökaluja lataukseen ja automaattiseen avainhallintaan](./sd-connect-command-line-interface.md).
    - Tiedostoja ei voi muokata SD Connectissa; lataa ne muokattavaksi tai käytä SD Desktopia.
    - Tiedostojen lataaminen alikansioihin ei toistaiseksi ole tuettu.
    - SD Connect näyttää salatut tiedostosi virtuaalikansioina. Suunnittele kansion rakenne huolellisesti—järjestele tiedostot projektien, teemojen tai loogisten rakenteiden mukaan parantaaksesi saavutettavuutta ja työnkulkuja. Tämä helpottaa myös käyttöoikeuksien jakamista muille. Lisäapua saat CSC:n Service Deskistä (aihe: Arkaluontoiset tiedot).

## SD Connectin ominaisuudet {#features-in-sd-connect}

* [Lataaminen](./sd-connect-upload.md)
* [Jakaminen](./sd-connect-share.md)
* [Lataaminen koneelle](./sd-connect-download.md)
* [Tiedostojen poisto](./sd-connect-delete.md)
* [Komentorivikäyttöliittymä](./sd-connect-command-line-interface.md)
* [Vianmääritys](./sd-connect-troubleshooting.md)