
# Kuinka tehdä ämpäristä julkinen? {#how-to-make-a-bucket-public}

Oletuksena Allas-ämpärit ovat vain todennuksen kautta käytettävissä (ks. [Allaksen käyttäminen](../../data/Allas/accessing_allas.md)), mutta on mahdollista tehdä ämpäristä julkinen. Tekemällä ämpäristä julkisen, kaikki tiedostot ja hakemistot ämpärissä ovat käytettävissä ilman minkäänlaista todennusta mistä tahansa internetistä HTTPS-protokollan kautta.

!!! Info "Allas-käyttöliittymä ei vielä tue julkisia ämpäreitä"
    Tällä hetkellä ämpäreitä ei voi tehdä julkisiksi osoitteesta <allas.csc.fi>. Tavoitteena on lisätä tämä ominaisuus tulevaisuudessa.

Tämän tekemiseksi meidän täytyy mennä [Poudan web-käyttöliittymään](https://pouta.csc.fi) ja:

1. Siirry kohtaan **Object Store** > **Containers**. Tämä avaa "Containers"-sivun, jossa on luettelo kaikista valitun CSC-projektin ämpäreistä.
2. Klikkaa ämpärin nimeä, jolloin ämpärin tiedot tulevat näkyviin:

    ![Ämpäritiedot](../../img/bucket_information.png)

3. Klikkaa "Public Access" -ruutua.
4. Tarkista, onko olemassa "segments"-ämpäri, ja niin ollen sen nimi on sama kuin "pää"-ämpäri, mutta `_segments`-päätteellä, esimerkiksi:

  * Jos nimi on `musel-photos`, segmenttiämpäri on `musel-photos_segments`

5. Jos on olemassa "segments"-ämpäri, klikkaa myös sen "Public Access" -ruutua.

Nyt ämpäri on julkinen ja sen sisältö on saatavilla URL:n kautta: `https://$BUCKETNAME.a3s.fi/`. Missä `$BUCKETNAME` on ämpärin nimi (joten ämpäri nimeltä `musel-photos` on saatavilla osoitteessa `https://musel-photos.a3s.fi/`).

