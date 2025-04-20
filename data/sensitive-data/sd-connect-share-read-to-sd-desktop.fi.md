# Kuinka antaa pääsy kansion sisältöön vain SD Desktopissa {#how-to-give-access-to-folder-content-only-in-sd-desktop}

## Käyttötapaus {#use-case}

Sinulla (Tiimi A) on dataa, johon toinen tiimi (Tiimi B) tarvitsee pääsyä. He haluavat tarkastella ja analysoida dataasi, mutta haluat rajoittaa heidän mahdollisuuttaan ladata kopion datasta suoraan.

## Ratkaisu {#solution}

Tässä tapauksessa voit jakaa datakansiosi Tiimi B:lle **Vain luku SD Desktopissa** -oikeudella. Näin Tiimi B:n jäsenet voivat tarkastella ja analysoida dataa SD Desktopin kautta, lataamatta alkuperäistä dataa.

Et myöskään halua, että Tiimi B vie alkuperäistä dataasi SD Desktopista. Siksi sinun tulee luoda projekti, jossa he (Tiimi B) ovat projektin jäseniä ja sinä olet projektipäällikkö – sillä vain projektipäällikkö voi viedä dataa SD Desktopista.

![Transfer Data Infograph](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ReadToDesktop.png)

!!! warning
    Huomaa, että sinun tulee olla molempien projektien projektipäällikkö. Ole hyvä ja [ota yhteyttä CSC Service Deskiin](../../support/contact.md) (aihe: *Sensitive data*) keskustellaksesi tästä jakovaihtoehdosta ennen jatkamista.

## Vaiheittainen ohje {#step-by-step-tutorial}

1. Kirjaudu sisään [MyCSC:hen](https://my.csc.fi/login){ target="_blank" }.
2. Luo kaksi uutta projektia: ***Projekti 1*** ja ***Projekti 2***.
3. Hallinnoi ***Projektia 1***: kytke SD Connect -palvelu käyttöön. Älä lisää projektijäseniä. [Katso ohjeet](./sd-access.md)
4. Hallinnoi ***Projektia 2***: kytke SD Connect ja SD Desktop -palvelut käyttöön. Lisää Tiimi B projektin jäseniksi. [Katso ohjeet](./sd-access.md)
5. Kirjaudu [SD Connectiin](./sd-connect-login.md).
6. Valitse ***Projekti 2*** ja kopioi **Share ID**.  
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareID2.png)
7. Valitse ***Projekti 1*** ja lataa datakansiosi sinne: [Katso latausohjeet](./sd-connect-upload.md).
8. Klikkaa “**Share**” juuri lataamasi kansion vieressä.
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareButton2.png)
9. Lisää Projektin 2 **Share ID** kenttään.
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_AddShareID2.png)
10. Valitse jako-oikeus: “**Vain luku SD Desktopissa**”. Klikkaa “**Share**”.
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_SelectPermission2.png)

Nyt kaikki kansion sisältö on näkyvissä Projektille 2 (Tiimi B) ja käytettävissä vain SD Desktopin kautta. Projektin 2 jäsenet voivat tarkastella ja analysoida jaettua kansion sisältöä SD Desktopin kautta. He eivät kuitenkaan voi viedä tai ladata tiedostoja, sillä kaikki dataviennit tekee suoraan projektipäällikkö – ja sinä olet molempien projektien projektipäällikkö.


## Ominaisuudet SD Connectissa {#features-in-sd-connect}

* [Lataus](./sd-connect-upload.md)
* [Jakaminen](./sd-connect-share.md)
* [Lataaminen](./sd-connect-download.md)
* [Poisto](./sd-connect-delete.md)