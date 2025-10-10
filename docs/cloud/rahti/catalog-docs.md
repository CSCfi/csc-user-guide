# Rahti-luettelo { #rahti-catalog }

Rahti tarjoaa heti käyttövalmiina sovellusten ja sovelluskomponenttien (kuten tietokantojen) luettelon. Tämän lisäksi CSC lisää luetteloon valikoidun joukon sovelluksia. Nämä sovellukset toimitetaan ”sellaisinaan”. Seuraamme ylävirran toimittajan Redhatin julkaisemia päivityksiä. Emme pysty päivittämään niitä oma-aloitteisesti. Jos tarvitset apua sovelluksen uudemman version käyttöönotossa, ota yhteyttä Service Deskiin osoitteessa <servicedesk@csc.fi>. Jokainen pyyntö käsitellään tapauskohtaisesti.

Lisätietoja: virallinen GitHub-repositorio [oletusarvoisille OpenShift Helm -kaavioille](https://github.com/openshift-helm-charts/charts)

Mallipohjista löydät GitHub-repositorion täältä: [OpenShiftin oletusmallit](https://github.com/sclorg/)

Voit tutustua myös [Red Hat Ecosystem Catalogiin](https://catalog.redhat.com/). Tämä luettelo sisältää uusimmat konttikuvajulkaisut.  
Löydät ohjeet, kuinka tuoda kuvat omaan nimiavaruuteesi/Rahti-projektiisi.

## Miten luetteloon pääsee WebUI:n avulla { #how-to-access-the-catalog-using-the-webui }

!!! warning "Rahti Helm -kaaviot"

    Alkaen 29. syyskuuta 2025 Bitnami muuttaa katalogiaan koskevaa käytäntöä. Lue lisää [täältä](https://github.com/bitnami/containers/issues/83267)  
    - Nykyiset kuvat siirretään [Bitnami Legacy -repositorioon](https://hub.docker.com/u/bitnamilegacy) eikä niitä enää päivitetä.  
    - Jotkin kuvat ovat edelleen saatavilla [Bitnami Secure Images](https://hub.docker.com/u/bitnamisecure) -palvelussa, mutta vain `latest`-tunnisteella.  
    - Jos haluat jatkossakin saada kuvia uusimmilla päivityksillä ja käyttää eri tunnisteita, sinun on tilattava [Bitnami Secure Images](https://www.arrow.com/globalecs/uk/products/bitnami-secure-images/) -palvelun täysi versio  
        
    Jotkin Helm-kaavioistamme käyttivät `Bitnami`-kuvia. Helm-kaaviomme on nyt tarkoitettu testausta/kehitystä varten, koska ne käyttävät `bitnamilegacy`- ja/tai `bitnamisecure`-docker-repositorioita.  
        
    Bitnami-projekti julkaisee kuitenkin edelleen lähdekoodinsa osoitteessa [bitnami/containers](https://github.com/bitnami/containers) Apache 2 -lisenssillä. Voit rakentaa kuvan ja sitten lähettää (push) sen CSC-projektiisi.
    
    Lisätietoja kuvien lähettämisestä (push) löydät [täältä](./images/Using_Rahti_integrated_registry.md)

Voit selata luetteloa web-käyttöliittymästä, kun (1) kirjaudut Rahtiin ja sitten (2) vaihdat Developer-näkymään ja napsautat `+Add`.

![+Add](../img/rahti-catalog.png)


!!! Note "Rahti 1 -mallipohjat Rahtissa"
    Useimmat aiemmista mallipohjista on siirretty Helm-kaavioiksi Rahtia varten. Jos haluat käyttää Rahti 1 -mallipohjaa Rahtissa, löydät repositorion tästä [linkistä](https://github.com/CSCfi/rahti-1-templates).  
    CSC ei enää päivitä näitä vanhoja mallipohjia, ainoastaan Helm-kaavioita.