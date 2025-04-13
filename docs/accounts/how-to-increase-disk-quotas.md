
# Kuinka lisätä levykiintiöitä

## Tallennuskapasiteetin lisääminen Puhtissa ja Mahtissa {#increasing-the-storage-capacity-in-puhti-and-mahti}

Puhti ja Mahti palvelimien [scratch](../computing/disk.md#scratch-directory) ja [projappl](../computing/disk.md#projappl-directory) hakemistojen
kiintiöitä voidaan tarvittaessa lisätä.

Voit hallita näitä kiintiöitä käyttämällä MyCSC:tä.

1. Kirjaudu [MyCSC:hen](https://my.csc.fi) ja **valitse projekti,** jota haluat muokata.
2. Palvelut-listalta klikkaa Määritykset **Puhti** tai **Mahti** palvelulle tarpeen mukaan. Tämä avaa sivun, jossa projektipäällikkö voi muokata kiintiöitä.

Voit tarkastaa oletusrajat scratch ja projappl alueille alla olevasta taulukosta. Sulkeissa olevat arvot ovat automaattisesti hyväksyttyjä rajoja. Sovellukset, joilla on korkeammat arvot, päätetään seuraavassa resurssien allokointikokouksessa.

| Hakemisto | Oletuskoko | Enimmäiskoko | Oletustiedostojen määräraja | Enimmäistiedostojen määräraja |
|-----------|------------|--------------|-----------------------------|------------------------------|
| projappl  | 50 GiB     | 200&nbsp;GiB&nbsp;(<&nbsp;100&nbsp;GiB)    | 100 000                     | 2 000 000 (<&nbsp;500&nbsp;000)                 |
| scratch   | 1 TiB      | 100&nbsp;TiB&nbsp;(<&nbsp;20&nbsp;TiB)    | 1 000 000                   | 10 000 000 (<&nbsp;5&nbsp;000&nbsp;000)               |

Huomaa, että laajennettu kiintiö kuluttaa CSC:n laskutusyksiköitäsi riippumatta siitä, kuinka paljon dataa hakemistossasi on. [Katso laskutus](billing.md) saadaksesi lisätietoja. Lisäksi, vaikka kiintiötä on lisätty, automaattinen siivousprosessi jatkaa käyttämättömien tiedostojen poistamista scratch-hakemistosta.

## Tallennuskapasiteetin lisääminen Allasissa {#increasing-the-storage-capacity-in-allas}

Uuden projektin oletuskiintiö on 10 TB, mutta sitä voidaan tarvittaessa lisätä. Allas on suosittu tallennuspaikka suurille tietoaineistoille CSC:n ympäristössä, joten sinun ei tulisi epäröidä pyytää suurempaa kiintiötä Allasille, jos työskentelet suuremmilla tietoaineistoilla.

Lisätäksesi Allas-kiintiötäsi, lähetä pyyntö osoitteeseen: servicedesk@csc.fi
Pyynnössä määrittele, mitä Allas-projektia käytät, kuinka suurta tallennustilaa tarvitaan ja millaista dataa Allasiin tallennetaan.

Huomaa, että tiedon tallentaminen Allasiin kuluttaa laskutusyksiköitä. Allasiin perustuva laskutus pohjautuu tallennetun datan määrään. Hinta on 1 BU/TiBh, eli 1 TB dataa Allasissa kuluttaa 24 BU päivässä ja 8760 BU vuodessa. [Kuinka hakea laskutusyksiköitä](how-to-apply-for-billing-units.md)

## Tallennuskapasiteetin lisääminen IDAssa {#increasing-the-storage-capacity-in-ida}

[Projektikiintiön seurannasta ja säätämisestä IDA Käyttäjän oppaassa](https://www.fairdata.fi/en/user-guides/user-guide/#project-quota)


