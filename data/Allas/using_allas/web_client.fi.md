# The web client – OpenStack Horizon Dashboard {#the-web-client-openstack-horizon-dashboard}

Tässä luvussa annetaan ohjeet Allas-palvelun käyttämiseen käyttäjäystävällisellä _OpenStack Horizon Dashboardilla_. 

OpenStackin dokumentaatio ämpärien hallintaan web-käyttöliittymän kautta: [https://docs.openstack.org/horizon/latest/user/manage-containers.html](https://docs.openstack.org/horizon/latest/user/manage-containers.html)

OpenStack-hallintapaneeli tarjoaa vain suppean osajoukon objektitallennustoimintoja. Saatavilla olevat toiminnot:

| Toiminto |
| :--- |
| _Luo_ uusi ämpäri |
| _Lataa_ objekti (max 5GB) |
| _Näytä_ objektit ja ämpärit |
| _Lataa_ objekti koneelle |
| _Poista_ objektit ja ämpärit |
| Aseta ämpärit _julkisiksi_ tai _yksityisiksi_ |


### **Alternative Web Interface – Allas Web UI** {#alternative-web-interface-allas-web-ui}
Käyttäjäystävällisemmän ja monipuolisemman web-käyttöliittymän saat käyttöösi myös **[Allas Web UI:n](./allas-ui.md)** avulla.  
Allas Web UI tarjoaa graafisen tavan hallita objektitallennusta, ämpärien luomista ja poistamista, objektien lataamista ja siirtämistä sekä jakamisoikeuksien asettamista – kaikki kätevästi yhdessä käyttöliittymässä.

## Create a bucket {#create-a-bucket}

1\. Siirry osoitteeseen [pouta.csc.fi](https://pouta.csc.fi/) ja kirjaudu sisään

2\. Valitse vasemman laidan valikosta **Projekti | Objektitallennus | Säiliöt**  
(Säiliö tarkoittaa tässä yhteydessä ämpäriä)

!["Creating a container"](img/allas_screenshot_create_container.png)  
**Kuva** Säiliön luominen

3\. Paina **+Säiliö**-painiketta ja nimeä ämpäri (katso [ämpärin nimeämisen tarkistuslista](../introduction.md#naming-buckets)). Jos päätät tehdä ämpäristä _julkisen_, sen sisältöä voidaan [tarkastella internetin kautta](#view-objects-via-the-internet).

## Upload an object {#upload-an-object}

Tässä käyttöliittymässä tietojen lataus toimii vain tiedostoille, jotka ovat alle 5 Gt:n kokoisia.

1\. Valitse haluttu ämpäri ja paina oikealla olevaa **lataussymbolia**.

!["Upload object"](img/Allas_screenshot_upload.png)  
**Kuva** Objektin lataaminen

2\. Valitse koneeltasi haluamasi objekti ja nimeä se. **Huom:** Älä <u>käytä</u> muita kuin ASCII-merkkejä (&auml;, &ouml; jne.).

3\. Lataa objekti. Se ilmestyy säiliöösi. Voit halutessasi luoda objekteille myös kansioita **+Kansio**-painikkeella lataussymbolin vieressä, esimerkiksi objektien järjestelyä varten.

## View objects via the internet {#view-objects-via-the-internet}

Jos objektit sisältävä ämpäri on asetettu _julkiseksi_, objektit voidaan katsella internetin kautta kenelle tahansa, jolla on oikea URL-osoite. Tätä asetusta voi muuttaa osoitteessa [pouta.csc.fi/dashboard/project/containers](https://pouta.csc.fi/dashboard/project/containers/) valitsemalla säiliön ja asettamalla **Public Access** -valinnan:

!["Making object public or private"](img/Allas_screenshot_public.png)  
**Kuva** Objektin asettaminen julkiseksi tai yksityiseksi

Esimerkiksi julkinen objekti nimeltään _my_fish_ ämpärissä _my_fishbucket_ on nähtävissä osoitteessa _a3s.fi/my_fishbucket/my_fish_.  
Huomaa, että tilanteissa, joissa suuri objekti tallennetaan Allakseen segmenteissä, on myös segmenttejä sisältävä ämpäri (esim. _my_fichbucket_segments_) asetettava _julkiseksi_.

## Download an object {#download-an-object}

Lataa objekti painamalla **Download**-painiketta objektin nimen oikealla puolella.

## Remove objects and buckets {#remove-objects-and-buckets}

Objektit voi poistaa avaamalla oikealla olevan pudotusvalikon _Download_-painikkeen vierestä ja valitsemalla **Delete**.

Ämpärin voi poistaa vain, jos se on tyhjä. Siksi kaikki ämpärin objektit tulee ensin poistaa tai siirtää muualle ennen ämpärin poistamista. Poista ämpäri painamalla **roskakorin symbolia** ämpärin nimen vierestä.

!["Removing object or container"](img/Allas_screenshot_delete.png)  
**Kuva** Objektin tai ämpärin poistaminen

Vaihtoehtoisesti – ja erityisesti jos haluat poistaa useita objekteja kerralla – voit valita haluamasi objektit klikkaamalla pienet valintaruudut objektien nimien vasemmalta puolelta ja valitsemalla sen jälkeen oikean yläkulman **roskakorin symbolin** punaisella taustalla.