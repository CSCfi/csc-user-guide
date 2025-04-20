# Termit ja käsitteet {#terms-and-concepts}

[TOC]

### Käyttöoikeuslista {#access-control-list}

_Käyttöoikeuslista_ (Access Control List, ACL) -mekanismia voidaan käyttää muiden Allas-käyttäjien pääsyn hallintaan omiin bucketeihin.

### Laskutusyksikkö {#billing-unit}

_Laskutusyksiköt_ kuvaavat CSC:n järjestelmien laskenta- ja tallennusresurssien kulutusta. Allaksessa talletetun datan määrä kuluttaa laskutusyksiköitä.

Katso [Laskutus ja kiintiöt](./introduction.md#billing-and-quotas)

### Bucket {#bucket}

_Bucket_ on säiliö objekteille, joka voi sisältää myös buckettia kuvaavaa metatietoa.

### Tarkistussumma {#checksum}

_Tarkistussumma_ on objektista laskettu hajautettu merkkijono, jonka avulla voidaan havaita, onko objekti muuttunut (tietojen eheys).
Voit näyttää tarkistussumman komennolla `md5sum`.

### Asiakasohjelma {#client}

_Asiakasohjelmaa_ käytetään objektitallennuspalveluun, kuten Allakseen, pääsyyn. Asiakasohjelmia on eri tyyppejä:

* **Web-selaimeen perustuva käyttö** esimerkiksi:
    - [Allas Web UI](./using_allas/allas-ui.md) – käyttäjäystävällinen graafinen käyttöliittymä bucketien hallintaan, tiedostojen lataamiseen ja siirtämiseen sekä datan jakamiseen.
    - [OpenStack Horizon -web-käyttöliittymä](./using_allas/web_client.md) – yksinkertainen web-käyttöliittymä pienten tiedostojen (≤5 GiB) hallintaan Allaksessa.

* **Komentoriviasiakasohjelmat** kuten:
    - [Swift](./using_allas/swift_client.md) ja [s3cmd](./using_allas/s3_client.md) – edistyneille käyttäjille, jotka tarvitsevat tarkempaa kontrollia objektitallennukseen.

* **Ohjelmoitava rajapinta (API)** niille, jotka integroivat Allaksen muihin ohjelmistoihin.

### Metatieto {#metadata}

_Metatieto_ kuvaa objektia tai buckettia. Sitä voidaan käyttää objektien hakemiseen.
Metatietoa käytetään _avain-arvo_ -pareina (esimerkiksi nimi: John).

### Objektin elinkaari {#object-lifecycle}

_Objektin elinkaari_ voidaan määritellä poistamaan objektit automaattisesti Allaksesta. Elinkaari määritetään bucket-tasolla, jossa voidaan asettaa useita vanhentumisaikoja. Elinkaari koskee bucketin objekteja niiden täsmäävien tagien ja/tai etuliitteiden perusteella. Katso esimerkki [s3-asiakasohjelman dokumentaatiossa](./using_allas/s3_client.md#setting-up-an-object-lifecycle)

### Objektitallennus {#object-storage}

_Objektitallennus_ tarkoittaa tietojen tallentamista, jossa data hallitaan objekteina tiedostojen tai lohkojen sijaan. Tyypillisesti objekti sisältää itse datan, metatietoa sekä yksilöllisen tunnisteen. Data voi olla esimerkiksi kuva tai ääni.

### OpenStack {#openstack}

_OpenStack-pilvihallintaohjelmistoa_ voidaan käyttää Allakseen pääsyyn.
[OpenStack Horizon -web-käyttöliittymä](./using_allas/web_client.md) tarjoaa perustoimintoja Allaksen datanhallintaan.

Katso lisätietoa [OpenStackin](https://www.openstack.org/) sivuilta.

### Pseudokansio {#pseudo-folder}

Bucketit eivät voi sisältää muita bucketteja. Voit kuitenkin käyttää niin sanottuja _pseudokansioita_.

Jos objektin nimessä on kauttaviiva `/`, sitä tulkitaan kansioerottimena. Näitä näytetään kansioina dataa web-käyttöliittymässä tarkasteltaessa. Pseudokansiot luodaan automaattisesti, jos siirrät kokonaisia kansioita komentoriviohjelmalla.

Esimerkiksi jos lisäät kaksi objektia
```bash
fishes/salmon.png
fishes/bass.png
```
bucketiin, bucketin listauksessa näkyy kansio _fishes_ ja sen sisällä kaksi tiedostoa.

## Kiintiö {#quota}

_Allaksen kiintiö_ määrittää, kuinka paljon dataa (kapasiteettia) projekti saa tallettaa Allakseen.

Katso [Laskutus ja kiintiöt](./introduction.md#billing-and-quotas)