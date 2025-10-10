# Pouta-verkkokäyttöliittymä { #pouta-web-interface }

Tässä luvussa annetaan ohjeet Allaksen käyttämiseen Poutan verkkokäyttöliittymän (OpenStack-hallintapaneelin) kautta. 

OpenStack-hallintapaneeli tarjoaa vain rajatun joukon objektivaraston toimintoja. Käytettävissä olevat toiminnot:

| Toiminto |
| :--- |
| _Luo_ uusi bucket |
| _Lähetä_ objekti (enint. 5 Gt) |
| _Näytä_ objektit ja bucketit |
| _Lataa_ objekti |
| _Poista_ objekteja ja bucketteja |
| Aseta bucketit _public_- tai _private_-tilaan |

[OpenStackin ohjeet bucketien hallintaan verkkokäyttöliittymän kautta](https://docs.openstack.org/horizon/latest/user/manage-containers.html)


### **Vaihtoehtoinen verkkokäyttöliittymä – Allas Web UI** { #alternative-web-interface-allas-web-ui }
Käyttöystävällisemmän ja monipuolisemman verkkokäyttöliittymän saat käyttämällä myös **[Allas Web UI](./allas-ui.md)**.  
Allas Web UI tarjoaa graafisen tavan hallita objektivarastoa, luoda ja poistaa bucketteja, lähettää/ladata objekteja sekä asettaa jakamisoikeuksia yhdessä helppokäyttöisessä ympäristössä.

## Luo bucket { #create-a-bucket }

1\. Siirry osoitteeseen [pouta.csc.fi](https://pouta.csc.fi/) ja kirjaudu sisään

2\. Vasemman reunan valikosta: **Project | Object Store | Containers**  
(Container vastaa buckettia)

!["Containerin luominen"](img/allas_screenshot_create_container.png)  
**Kuva** Containerin luominen

3\. Paina **+Container**-painiketta ja nimeä bucket (katso [ohjeet buckettien nimeämiseen](../introduction.md#naming-buckets-and-objects)). Jos asetat bucketin _Public_-tilaan, sen sisältöjä voidaan [katsoa internetin kautta](#view-objects-via-the-internet).

## Lähetä objekti { #upload-an-object }

Tämän käyttöliittymän lähetys toimii vain alle 5 Gt:n tiedostoille.

1\. Valitse haluamasi bucket ja paina oikealla olevaa **lähetyskuvaketta**.

!["Objektin lähettäminen"](img/Allas_screenshot_upload.png)  
**Kuva** Objektin lähettäminen

2\. Valitse tietokoneeltasi objekti ja nimeä se. **Huom:** Älä <u>käytä</u> merkkejä, jotka eivät kuulu ASCII-merkistöön (&auml;, &ouml; jne.). 

3\. Lähetä objekti. Se ilmestyy containeriisi. Voit myös luoda objekteille näennäiskansioita lähetyskuvakkeen vieressä olevalla **+Folder**-painikkeella, esim. järjestääksesi objektit kansioihin.

## Näytä objektit internetin kautta { #view-objects-via-the-internet }

Jos objekteja sisältävä bucket on asetettu _public_-tilaan, kuka tahansa URL-osoitteen tietävä voi tarkastella sisältöä internetin kautta. Asetusta voidaan muuttaa osoitteessa [pouta.csc.fi/dashboard/project/containers](https://pouta.csc.fi/dashboard/project/containers/) valitsemalla container ja säätämällä **Public Access** -asetus:

!["Objektin asettaminen julkiseksi tai yksityiseksi"](img/Allas_screenshot_public.png)
**Kuva** Objektin asettaminen julkiseksi tai yksityiseksi

Esimerkiksi containerissa _my_fishbucket_ oleva julkinen objekti _my_fish_ on nähtävissä URL-osoitteesta _a3s.fi/my_fishbucket/my_fish_.  
Huomaa, että jos suuri objekti on tallennettu Allakseen segmentteinä, myös segmenttejä sisältävä bucket (esim. _my_fichbucket_segments_) on asetettava _public_-tilaan.

## Lataa objekti { #download-an-object }

Lataa objekti napsauttamalla objektin nimen oikealla puolella olevaa **Download**-painiketta.

## Poista objekteja ja bucketteja { #remove-objects-and-buckets }

Objekteja voi poistaa laajentamalla objektin nimen oikealla puolella olevaa pudotusvalikkoa _Download_-painikkeen vierestä ja valitsemalla **Delete**.

Bucketteja voi poistaa vain, jos ne ovat tyhjiä. Siksi kaikki bucketissa olevat objektit on poistettava tai siirrettävä muualle ennen bucketin poistamista. Poista bucket napsauttamalla bucketin nimen vieressä olevaa **roskakorisymbolia**. 

!["Objektin tai containerin poistaminen"](img/Allas_screenshot_delete.png)
**Kuva** Objektin tai containerin poistaminen

Vaihtoehtoisesti, ja erityisesti jos haluat poistaa useita objekteja kerralla, voit valita objektit merkitsemällä pienet ruudut objektien nimien vasemmalta puolelta ja valita oikean yläkulman punaisella taustalla olevan **roskakorisymbolin**.