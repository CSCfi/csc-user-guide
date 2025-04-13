# Kuinka antaa pääsy kansioihin vain SD Desktopissa {#how-to-give-access-to-folder-content-only-in-sd-desktop}

## Käyttötapaus {#use-case}

Teillä (Tiimi A) on dataa, johon toinen tiimi (Tiimi B) tarvitsee pääsyn. He haluavat tarkastella ja analysoida dataanne, mutta te haluatte rajoittaa heidän mahdollisuuksiaan ladata kopion datasta suoraan.

## Ratkaisu {#solution}

Tässä tapauksessa voitte jakaa datakansionne Tiimille B **Read to SD Desktop** -luvalla. Näin Tiimi B:n jäsenet voivat tarkastella ja analysoida dataa SD Desktopin kautta ilman, että he lataavat kopion alkuperäisestä datasta.

Ette myöskään halua, että Tiimi B vie alkuperäistä dataanne SD Desktopista. Siksi teidän tulee luoda projekti, jossa he (Tiimi B) ovat projektin jäseniä ja te olette projektipäällikkö - koska vain projektipäällikkö voi viedä dataa SD Desktopista.

![Transfer Data Infograph](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ReadToDesktop.png)

!!! warning
    Huomioikaa, että teidän tulee olla projektipäällikkö kummassakin projektissa. Olkaa hyvä ja [ottakaa yhteyttä CSC Service Deskiin](../../support/contact.md) (aihe: *Sensitive data*) keskustellaksenne tästä jakovaihtoehdosta ennen etenemistä.

## Vaiheittainen opetusohjelma {#step-by-step-tutorial}

1. Kirjaudu [MyCSC:hen](https://my.csc.fi/login){ target="_blank" }.
2. Luo kaksi uutta projektia: ***Projekti 1*** ja ***Projekti 2***.
3. Hallinnoi ***Projektia 1***: ota palvelupääsy käyttöön SD Connectille. Älä lisää yhtään projektin jäsentä. [Katso ohjeet](./sd-access.md)
4. Hallinnoi ***Projektia 2***: ota palvelupääsy käyttöön SD Connectille ja SD Desktopille. Lisää Tiimi B **projektin jäseniksi.** [Katso ohjeet](./sd-access.md)
5. Kirjaudu sisään [SD Connectiin](./sd-connect-login.md).
6. Valitse ***Projekti 2*** ja kopioi **Share ID**.
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareID2.png)
7. Valitse ***Projekti 1*** ja lataa datakansio sinne: [Katso latausohjeet](./sd-connect-upload.md).
8. Klikkaa "**Share**" juuri lataamasi kansion vieressä.
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareButton2.png)
9. Lisää Projektin 2 **Share ID** kenttään.
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_AddShareID2.png)
10. Valitse jakolupa: "**Read to SD Desktop**". Klikkaa "**Share**".
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_SelectPermission2.png)

Nyt kaikki kansion sisältö on näkyvissä Projekti 2:ssa (Tiimi B) ja käytettävissä vain SD Desktopin kautta. Projekti 2:n jäsenet voivat käyttää ja analysoida jaettua kansion sisältöä SD Desktopin kautta. He eivät kuitenkaan voi viedä tai ladata tiedostoja, sillä kaikki datan vientiä hallinnoi suoraan projektipäällikkö - ja sinä olet kummankin projektin projektipäällikkö.

## Toiminnot SD Connectissa {#features-in-sd-connect}

* [Lataa](./sd-connect-upload.md)
* [Jaa](./sd-connect-share.md)
* [Lataa alas](./sd-connect-download.md)
* [Poista](./sd-connect-delete.md)