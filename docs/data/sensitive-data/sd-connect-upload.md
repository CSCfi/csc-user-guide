[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Datan lataaminen ja salaaminen { #uploading-and-encrypting-data }

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SMnEkcS_HJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Datasi salataan automaattisesti, kun lataat aineistoa SD Connectiin. Tämä sopii kaikille tiedostotyypeille ja -muodoille, mutta sitä tuetaan vain enintään 100 Gt:n tiedostoille ja alle 1 Tt:n kansioille. Suuremmat tiedostot tai kansiot voidaan ladata [ohjelmallisesti](./sd-connect-command-line-interface.md).

!!! Note
    Jos käytät palvelua ensimmäistä kertaa, selaimeesi saattaa ilmestyä ponnahdusikkuna, jossa pyydetään hyväksymään evästeet. Napsauta "Accept" ottaaksesi tiedostojen ja kansioiden lataamisen käyttöön.

## Lataa ja salaa tiedostot uuteen kansioon { #upload-and-encrypt-files-to-a-new-folder }

1. Kirjaudu SD Connectiin.
2. Valitse oikea CSC-projekti vasemmasta yläkulmasta.
3. Napsauta oikeassa yläkulmassa **Upload**.
4. Nimeä uudessa ikkunassa tiedostoillesi kohdekansio.
5. Napsauta **Select Files** avataksesi selausikkunan ja valitse ladattavat tiedostot. Jos haluat ladata kansioita, vedä ja pudota ne ikkunaan. Napsauta **Upload** käynnistääksesi automaattisen salauksen ja latauksen.
6. Ilmoitus latauksen tilasta tulee näkyviin ja pysyy näkyvissä, kunnes lataus on valmis. Ilmoituksessa on myös linkki kohdekansioon.
7. Kun lataus on valmis, salatuissa tiedostoissa on .c4gh-pääte, mikä tarkoittaa, että salaus on onnistunut.
8. Nyt tiedostot ovat ladattavissa ja jaettavissa SD Connectissa tai analysoitavissa, muokattavissa tai annotoitavissa SD Desktopin kautta.

!!! info "Kansion nimet"

    * Kansion nimen tulee alkaa pienellä kirjaimella tai numerolla.
    * Kansion nimen tulee olla 3–63 merkkiä pitkä.
    * Käytä latinalaisia aakkosia (a–z), numeroita (0–9) ja väliviivaa (-).
    * Suuria kirjaimia, alaviivaa (_) sekä diakriittisiä tai erityismerkeillä varustettuja kirjaimia (åäöe') ei sallita.
    * Kansionimien on oltava yksilöllisiä kaikissa SD Connectin ja Allaksen projekteissa. Jos et voi luoda uutta kansiota, jokin toinen projekti saattaa jo käyttää valitsemaasi nimeä. Tämän välttämiseksi on hyvä käytäntö sisällyttää kansionimeen projektikohtaisia tunnisteita (esim. projektin ID-numero tai lyhenne).
    * Muista, että kaikki kansionimet ovat julkisia; älä sisällytä niihin luottamuksellista tietoa.
    * Kansionimiä ei voi muuttaa jälkikäteen.



![SD Connect – lataus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_Upload.png)


## Lataa ja salaa tiedostot olemassa olevaan kansioon { #upload-and-encrypt-files-to-an-existing-folder }

1. Valitse oikea kansio (kaksoisnapsauttamalla).
2. Napsauta oikeassa yläkulmassa **Upload** ja seuraa yllä olevan kappaleen vaiheita 4–6.

## Luo kansio { #create-a-folder }

Voit luoda kansion ja ladata tiedostot siihen myöhemmin.

1. Napsauta **Create folder**.
2. Nimeä kansiosi.
3. Napsauta **Save**.

![SD Connect – Luo kansio](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_CreateFolder.png)

!!! warning "Varoitus"

    Samassa CSC-projektissa olevat jäsenet voivat ladata ja purkaa salauksen SD Connectista. Tätä voidaan rajoittaa jakamalla tiedostoja käyttöoikeudella **Read to SD Desktop**. [Lue käyttötapauksesta](./sd-connect-share-read-to-sd-desktop.md)

!!! Note "Lisähuomioita"

    - Suuret tiedostot (> 100 Gt) voivat viedä tunteja latautua, ja lataukset keskeytyvät 8 tunnin jälkeen.
    - Käyttöliittymä voi hidastua, kun yhdessä kansiossa on yli 2500 tiedostoa. Tällöin käytä [komentorivityökaluja lataukseen ja avainten automatisoituun hallintaan](./sd-connect-command-line-interface.md).
    - Tiedostoja ei voi muokata SD Connectissa; lataa ne muokattavaksi tai käytä niitä SD Desktopin kautta.
    - Tiedostojen lataaminen alikansioihin ei toistaiseksi ole tuettua.
    - SD Connect näyttää salatut tiedostosi virtuaalisina kansioina. Suunnittele kansionrakenne huolellisesti—järjestä tiedostot projektien, teemojen tai loogisten kokonaisuuksien mukaan parantaaksesi löydettävyyttä ja työnkulkua. Tämä helpottaa myös käyttöoikeuksien jakamista muille. Tarvittaessa ota yhteyttä CSC Service Deskiin (aihe: Sensitive data).

## SD Connectin ominaisuudet { #features-in-sd-connect }

* [Lähetys](./sd-connect-upload.md)
* [Jakaminen](./sd-connect-share.md)
* [Lataus](./sd-connect-download.md)
* [Poistaminen](./sd-connect-delete.md)
* [Komentorivikäyttöliittymä](./sd-connect-command-line-interface.md)
* [Vianmääritys](./sd-connect-troubleshooting.md)