[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Kansioiden jakaminen { #sharing-folders }

!!! info "Share ID"

    SD Connectin avulla voit jakaa kansioita eri CSC-projektien välillä. Tämä tehdään käyttämällä Share ID -tunnusta, joka on yksilöllinen 32-numeroinen koodi, joka liittyy CSC-projektiin. Voit jakaa kansion useille CSC-projekteille ja käyttää erilaisia käyttöoikeustasoja. 

SD Connect tarjoaa useita tapoja jakaa tiedostojasi. Lue käyttöoikeuksista ja esimerkkikäyttötapauksista, jotka havainnollistavat, miten eri käyttöoikeudet toimivat:

* [Siirrä dataa](#transfer-data)
* [Yhteistyö](#collaborate)
* [Luku SD Desktopissa](#read-to-sd-desktop)


## Jaa kansio toiseen projektiin { #share-folder-to-another-project }


1. Pyydä vastaanottajalta hänen projektinsa Share ID. Se löytyy heidän SD Connectistaan. Vastaanottajan tulee valita vasemmasta yläkulmasta oikea CSC-projekti, sitten klikata projektinumeron vieressä olevaa **Copy Share ID** -painiketta ja toimittaa se sinulle sähköpostitse. 
![(kuvakaappaus)](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareID.png)
2. Napsauta “**Share**” sen kansion vierestä, jonka haluat jakaa.
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareButton.png)
3. Lisää vastaanottajaprojektin **Share ID** kenttään.
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_AddShareID.png)
4. Valitse sopiva jakamisoikeus. Napsauta “**Share**”.
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_SelectPermission.png)

### Muuta jakamisoikeutta { #change-share-permission }

1. Napsauta “**Share**” sen kansion vierestä, jonka haluat jakaa.
2. Vieritä alas ja valitse "This project is shared to" -otsikon alta oikea Share ID, ja muuta sitten oikeutta "Permissions"-pudotusvalikosta. 
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ChangePermissions.png)

## Käyttöoikeudet ja esimerkkikäyttötapaukset { #permission-rights-and-example-use-cases }

 Lue käyttöoikeuksista ja esimerkkikäyttötapauksista, jotka havainnollistavat, miten eri käyttöoikeuksia voidaan soveltaa yhteistyötarpeiden ja tiedonjakotarpeiden mukaan.

### Siirrä dataa { #transfer-data }

Vastaanottajaprojektin jäsenet voivat kopioida kansion SD Connectissa ja ladata tiedostot salauksen purettuina. Tiedostot ovat myös käytettävissä SD Desktopin kautta. Käytä tätä, kun haluat siirtää datasi toiseen projektiin.

[Lue käyttötapauksesta: Siirrä datasi toiseen projektiin](./sd-connect-share-tranfer-data.md)


### Yhteistyö { #collaborate }

Siirrä dataa -oikeuden lisäksi vastaanottajaprojektin jäsenet voivat lisätä uusia tiedostoja tai poistaa olemassa olevia tiedostoja kansiostasi SD Connectissa. Käytä tätä, kun haluat kansiosta yhteisen työtilan.

[Lue käyttötapauksesta: Käytä kansiota yhteisenä työtilana](./sd-connect-share-workspace.md)



### Luku SD Desktopissa { #read-to-sd-desktop }

Vastaanottajaprojektin jäsenet voivat käyttää kansion sisältöä ainoastaan SD Desktopissa. Käytä tätä, kun tarvitset mahdollisimman suuren varmuuden siitä, ettei tiedostojasi jaeta eteenpäin.

!!! warning
    Huomaa, että sinun on myös oltava vastaanottajaprojektin projektipäällikkö. [Ota yhteyttä CSC Service Deskiin](../../support/contact.md) keskustellaksesi tästä vaihtoehdosta ennen etenemistä.

[Lue käyttötapauksesta: Anna pääsy kansion sisältöön vain SD Desktopissa](./sd-connect-share-read-to-sd-desktop.md)

## SD Connectin ominaisuudet { #features-in-sd-connect }

* [Lähetys](./sd-connect-upload.md)
* [Jakaminen](./sd-connect-share.md)
* [Lataus](./sd-connect-download.md)
* [Poistaminen](./sd-connect-delete.md)
* [Komentorivikäyttöliittymä](./sd-connect-command-line-interface.md)
* [Vianmääritys](./sd-connect-troubleshooting.md)