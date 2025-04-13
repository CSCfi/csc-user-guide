# The web client – OpenStack Horizon Dashboard {#the-web-client-openstack-horizon-dashboard}

Tämä luku tarjoaa ohjeita Allaksen käyttöön käyttäjäystävällisellä _OpenStack Horizon Dashboardilla_.

OpenStack-dokumentaatio ämpärien hallintaan verkkokäyttöliittymän kautta: [https://docs.openstack.org/horizon/latest/user/manage-containers.html](https://docs.openstack.org/horizon/latest/user/manage-containers.html)

OpenStack-hallintapaneeli tarjoaa pienen osajoukon objektien tallennustoiminnallisuuksia. Saatavilla olevat toiminnot:

| Toiminto |
| :--- |
| _Luo_ uusi ämpäri |
| _Lataa_ objekti (maks. 5 GB) |
| _Näytä_ objektit ja ämpärit |
| _Lataa_ objekti |
| _Poista_ objektit ja ämpärit |
| Tee ämpärit _julkisiksi_ tai _yksityisiksi_ |

### **Vaihtoehtoinen verkkoliittymä – Allas Web UI** {#alternative-web-interface-allas-web-ui}
Käyttäjäystävällisemmän ja ominaisuusrikkaamman verkkoliittymän saatavuutta varten voit käyttää myös **[Allas Web UI:tä](./allas-ui.md)**.  
Allas Web UI tarjoaa graafisen tavan hallita objektien tallennusta, luoda ja poistaa ämpäreitä, ladata objekteja ja asettaa jakoluvat, kaikki käyttäjäystävällisessä ympäristössä.

## Luo ämpäri {#create-a-bucket}

1\. Siirry osoitteeseen [pouta.csc.fi](https://pouta.csc.fi/) ja kirjaudu sisään

2\. Valikossa vasemmalla, navigoi kohtaan **Project | Object Store | Containers**  
(Kontti vastaa ämpäriä)

!["Käytä kontoa"](img/allas_screenshot_create_container.png)  
**Kuva** Kontin luominen

3\. Paina **+Container**-painiketta ja nimeä ämpäri (katso [ämpärin nimeämisen tarkistuslista](../introduction.md#naming-buckets)). Jos päätät tehdä ämpärin _julkiseksi_, sen sisältöä voi [katsoa internetin kautta](#view-objects-via-the-internet).

## Lataa objekti {#upload-an-object}

Tämän käyttöliittymän tiedostojen lataustoiminto toimii vain alle 5 GB tiedostoille.

1\. Valitse haluamasi ämpäri ja paina oikealla olevaa **lataussymbolia**.

!["Lataa objekti"](img/Allas_screenshot_upload.png)  
**Kuva** Objekti lataaminen

2\. Valitse objektit tietokoneeltasi ja nimeä se. **Huom:** Älä <u>käytä</u> ei-ASCII-merkkejä (&auml;, &ouml; jne.).

3\. Lataa objekti. Se ilmestyy konttiisi. Voit myös luoda pseudo-kansioita objekteille painamalla **+Folder**-painiketta lataussymbolin vieressä, esim. objektien järjestämiseksi kansioihin.

## Katso objekteja internetin kautta {#view-objects-via-the-internet}

Jos objektit sisältävä ämpäri on asetettu _julkiseksi_, kaikkien, jotka tietävät URL-osoitteen, voi katsella internetin kautta. Tämä asetus voidaan muuttaa osoitteessa [pouta.csc.fi/dashboard/project/containers](https://pouta.csc.fi/dashboard/project/containers/) valitsemalla kontti ja valitsemalla **Public Access** -asetus:

!["Tee objekti julkiseksi tai yksityiseksi"](img/Allas_screenshot_public.png)
**Kuva** Objekti julkiseksi tai yksityiseksi tekeminen

Esimerkiksi, julkinen objekti nimeltä _my_fish_ kontissa _my_fishbucket_ voi katsella URL-osoitteella _a3s.fi/my_fishbucket/my_fish_. Huomaa, että tapauksissa, joissa suuri objekti tallennetaan Allakseen segmentteinä, täytyy myös segmenttejä sisältävä ämpäri (esim. _my_fichbucket_segments_) asettaa _julkiseksi_.

## Lataa objekti {#download-an-object}

Lataa objekti napsauttamalla objektin nimen oikealla puolella olevaa **Lataa**-painiketta.

## Poista objekteja ja ämpäreitä {#remove-objects-and-buckets}

Objekteja voi poistaa laajentamalla oikealla olevasta pudotusvalikosta _Lataa_-painikkeen vierestä ja valitsemalla **Poista**.

Ämpärit voidaan poistaa vain, kun ne ovat tyhjiä. Siksi kaikki objektit ämpärissä on poistettava tai siirrettävä pois ennen kuin ämpäri voidaan poistaa. Poista ämpäri napsauttamalla ämpärin nimen vieressä olevaa **roskakorisymbolia**.

!["Poista objekti tai kontti"](img/Allas_screenshot_delete.png)
**Kuva** Objektin tai ämpärin poistaminen

Vaihtoehtoisesti, ja erityisesti jos haluat poistaa useita objekteja kerralla, voit valita objektit valitsemalla pientä ruutua objektin nimen vasemmalla puolella ja valitsemalla punaisen taustan oikeassa yläkulmassa olevan **roskakorin symbolin**.