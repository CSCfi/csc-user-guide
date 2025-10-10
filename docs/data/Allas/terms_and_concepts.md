# Termit ja käsitteet { #terms-and-concepts }

[TOC]

### Käyttöoikeusluettelo { #access-control-list }

_Menetelmää Käyttöoikeusluettelo_ (ACL) voidaan käyttää hallitsemaan muiden Allas-käyttäjien pääsyä säiliöihisi.

### Laskutusyksikkö { #billing-unit }

_Laskutusyksiköt_ (BU) kuvaavat laskennan (CPU BU, GPU BU, Cloud BU) ja tallennusresurssien (Storage BU) kulutusta CSC:n järjestelmissä. Allaksessa tallennettu datamäärä kuluttaa tallennuksen laskutusyksiköitä (Storage BU).

Katso [Laskutus ja kiintiöt](./introduction.md#billing-and-quotas)

### Säiliö { #bucket }

_Säiliö_ on objektien säilytysastia, joka voi sisältää myös säiliötä kuvaavia metatietoja.

### Tarkistussumma { #checksum }

_Tarkistussumma_ on objektista laskettu hajautearvo, jonka avulla voidaan havaita, onko objekti muuttunut (tiedon eheys).
Voit näyttää tarkistussumman komennolla `md5sum`.

### Asiakasohjelma { #client }

_Asiakasohjelmaa_ käytetään objektitallennuspalveluun, kuten Allakseen, pääsyyn. Allakseen voi ottaa yhteyden useilla eri [asiakasohjelmilla](accessing_allas.md).

### Metatiedot { #metadata }

_Metatiedot_ kuvaavat objektia tai säiliötä. Niiden avulla voidaan hakea objekteja.
Niitä käytetään _avain–arvo_ -pareina (esimerkiksi, nimi: John).

### Objektin elinkaari { #object-lifecycle }

_Objektin elinkaari_ voidaan määrittää poistamaan objektit Allaksesta automaattisesti. Elinkaari määritetään säiliötasolla, jossa voidaan määritellä useita vanhenemisaikoja. Elinkaari kohdistetaan säiliön objekteihin niiden täsmäävien tunnisteiden (tags) ja/tai etuliitteiden (prefixes) perusteella. Katso esimerkki [s3-asiakasohjelman dokumentaatiosta](./using_allas/s3_client.md#setting-up-an-object-lifecycle)

### Objektitallennus { #object-storage }

_Objektitallennus_ tarkoittaa tietojen tallennusta, jossa dataa hallitaan objekteina tiedostojen tai lohkojen sijaan. Tyypillisesti objekti koostuu itse datasta, metatiedoista ja yksilöllisestä tunnisteesta. Yleisesti data voi olla mitä tahansa, esim. kuva tai ääni.

### OpenStack { #openstack }

[OpenStack](https://www.openstack.org/)-pilvihallinnan middleware_ voidaan käyttää Allakseen pääsyyn.


### Näennäiskansio { #pseudo-folder }

Säiliöt eivät voi sisältää toisia säiliöitä. Voit kuitenkin käyttää niin sanottuja _näennäiskansioita_.

Jos objektin nimessä on kauttaviiva `/`, sitä tulkitaan kansioerottimena. Nämä näytetään kansiolistoina, kun dataa käytetään joillakin asiakkailla, esimerkiksi verkkokäyttöliittymissä. Nämä näennäiskansiot lisätään automaattisesti, jos lataat kokonaisia kansioita komentoriviasiakkaalla.

Esimerkiksi, jos lisäät kaksi objektia
```bash
fishes/salmon.png
fishes/bass.png
```
säiliöön, säiliön listaus näyttää kansion nimeltä _fishes_ ja kaksi sen sisällä olevaa tiedostoa.

## Kiintiö { #quota }

_Allas-kiintiö_ määrittää suurimman datamäärän (kapasiteetin), jonka projekti saa tallentaa Allakseen.

Katso [Laskutus ja kiintiöt](./introduction.md#billing-and-quotas)