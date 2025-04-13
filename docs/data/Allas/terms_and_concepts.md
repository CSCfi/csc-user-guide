# Termit ja käsitteet

[TOC]

### Käyttövaltuuslista {#access-control-list}

_Käyttövaltuuslista_ (Access Control List, ACL) -mekanismia voidaan käyttää hallitsemaan muiden Allas-käyttäjien pääsyä sinun bucket-teihisi.

### Laskutusyksikkö {#billing-unit}

_Laskutusyksiköt_ kuvaavat tietokone- ja tallennusresurssien käyttöä CSC-järjestelmissä. Allaksessa tallennettu datamäärä kuluttaa laskutusyksiköitä.

Katso [Laskutus ja kiintiöt](./introduction.md#billing-and-quotas)

### Ämpäri {#bucket}

_Ämpäri_ on objektille tarkoitettu säiliö, joka voi sisältää myös metatietoja, jotka kuvaavat ämpäriä.

### Tarkistussumma {#checksum}

_Tarkistussumma_ on laskettu merkkijono, jolla voidaan tarkistaa, onko objekti muuttunut (datan eheys). Voit näyttää tarkistussumman komennolla `md5sum`.

### Asiakasohjelma {#client}

_Asiakasohjelmaa_ käytetään objektitallennuspalvelun, kuten Allas, käyttämiseen. Asiakkaita on monenlaisia:

* **Verkkoselaimeen perustuva käyttö**:
    - [Allas-verkkokäyttöliittymä](./using_allas/allas-ui.md) – käyttäjäystävällinen graafinen käyttöliittymä ämpärien hallintaan, objektien lataamiseen ja jakamiseen.
    - [OpenStack Horizon -verkkokäyttöliittymä](./using_allas/web_client.md) – yksinkertainen verkkokäyttöliittymä pienten tiedostojen (≤5 GiB) hallintaan Allaksessa.

* **Komentoriviasiakkaat**, kuten:
    - [Swift](./using_allas/swift_client.md) ja [s3cmd](./using_allas/s3_client.md) – edistyneille käyttäjille, jotka tarvitsevat objektisäilytyksen tarkempaa hallintaa.

* **Ohjelmoitava rajapinta (API)** niille, jotka integroituvat Allakseen ohjelmistosovellusten kanssa.

### Metatiedot {#metadata}

_Metatiedot_ kuvaavat objektia tai ämpäriä ja niitä voidaan käyttää objektien hakemiseen. Näitä käytetään _avain-arvo_-pareina (esimerkiksi nimi: John).

### Objektin elinkaari {#object-lifecycle}

_Objektin elinkaari_ voidaan määrittää poistamaan objektit automaattisesti Allaksesta. Elinkaari määritetään ämpärin tasolla, jossa voidaan määrittää useita vanhenemisjaksoja. Elinkaari koskee ämpärin objekteja niiden vastaavien tunnisteiden ja/tai etuliitteiden perusteella. Katso esimerkki [s3-asiakasohjelman dokumentaatiosta](./using_allas/s3_client.md#setting-up-an-object-lifecycle).

### Objektitallennus {#object-storage}

_Objektitallennus_ viittaa tietokoneen tietotallennukseen, joka hallitsee dataa objekteina tiedostojen tai lohkojen sijasta. Tyypillisesti objekti koostuu itse datasta, metatiedoista ja yksilöllisestä tunnisteesta. Yleisesti ottaen data voi olla mitä tahansa, esim. kuva tai ääni.

### OpenStack {#openstack}

_OpenStack-pilvihallinnan middlewarea_ voidaan käyttää Allakseen pääsyyn. [OpenStack Horizon -verkkokäyttöliittymä](./using_allas/web_client.md) tarjoaa perustoimintoja datanhallintaan Allaksessa.

Katso lisätietoja [OpenStackista](https://www.openstack.org/).

### Pseudokansio {#pseudo-folder}

Ämpäreissä ei voi olla muita ämpäreitä. Voit kuitenkin käyttää niin kutsuttuja _pseudokansioita_.

Jos objektin nimi sisältää vinoviivan `/`, se tulkitaan kansion erottimeksi. Näitä näytetään kansiolistauksina, kun pääset dataan verkkokäyttöliittymän kautta. Nämä pseudokansiot lisätään automaattisesti, jos lataat kokonaisia kansioita komentoriviasiakkaalla.

Esimerkiksi, jos lisäät kaksi objektia
```bash
fishes/salmon.png
fishes/bass.png
```
ämpäriin, listatessasi ämpärin näet kansion nimeltä _fishes_ ja kaksi tiedostoa siinä.

## Kiintiö {#quota}

_Allaksen kiintiö_ määrittää suurimman sallitun datamäärän (kapasiteetin), jonka projekti saa tallentaa Allakseen.

Katso [Laskutus ja kiintiöt](./introduction.md#billing-and-quotas)