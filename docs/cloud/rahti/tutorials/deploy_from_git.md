!!! success "Perustaso"
    Tämä on yksinkertainen opas, jossa näytetään, miten web‑palvelin otetaan käyttöön Rahtin [verkkokäyttöliittymän](../usage/getting_started.md) avulla käyttäen Git-repositoriota lähteenä

# Käyttöönotto Gitistä { #deploy-from-git }

Näin perustat staattisen verkkopalvelimen Rahtiin Git-repositoriosta.

1. Luo projekti. [Ohjeet](../usage/projects_and_quota.md)

1. OpenShiftin verkkokonsolissa vaihda Developer-näkymään. Valitse navigointipaneelista _Add_. Sovelluksen luomiseksi valitse Developer Catalog -luettelosta _Import from Git_. 

    ![click_git](../../../img/click_git.png)

1. Syötä Git-repositorion URL-osoite. OpenShift käyttää tätä osoitetta repositorion kloonaamiseen.  

    ![import_from_git](../../../img/import_from_git_1.png)

    Valinta `Advanced Git Options` mahdollistaa "reference" (Branch, tag tai commit) tai context dir -arvon muuttamisen. Lisäksi voit lisätä secretin, jolla saat pääsyn repositorioon (käyttäjätunnus ja salasana tai SSH-avaimet).

1. URL-osoitteen syöttämisen jälkeen OpenShift validoi ja analysoi repositorion. 

    ![import_from_git](../../../img/import_from_git_2.png)

1. Jos analyysi onnistui, viimeinen vaihe on napsauttaa `Create`. Muutaman minuutin kuluttua sivusto on käytettävissä.

Tämän oppaan jälkeen voit tutustua [Webhooks](webhooks.md) -artikkeliin. Webhookien avulla voit ottaa tämän sivuston automaattisesti uudelleen käyttöön aina, kun master-päähaaraan tehdään muutos.