# Kuinka kasvattaa levykiintiöitä { #how-to-increase-disk-quotas }

## Tallennuskapasiteetin kasvattaminen Puhtissa ja Mahtissa { #increasing-the-storage-capacity-in-puhti-and-mahti }

Puhti- ja Mahti-palvelimien [scratch](../computing/disk.md#scratch-directory)- ja [projappl](../computing/disk.md#projappl-directory) -hakemistojen kiintiöitä voidaan tarvittaessa kasvattaa.

Voit hallita näitä kiintiöitä MyCSC:ssä.

1. Kirjaudu [MyCSC](https://my.csc.fi):hen ja **valitse projekti**, jota haluat muokata.
1. Palvelut-listassa napsauta tarpeen mukaan **Puhti**- tai **Mahti**-palvelun Configuration-linkkiä. Tämä avaa sivun, jolla **projektipäällikkö** voi muokata kiintiöitä.

Voit tarkistaa scratch- ja projappl-alueiden oletusrajat alla olevasta taulukosta. Sulkeissa olevat arvot ilmaisevat automaattisesti hyväksyttävät rajat. Sitä suuremmista arvoista päätetään kolmen viikon välein pidettävissä resurssien kohdennuskokouksissa.
  
| Hakemisto | Oletuskoko | Enimmäiskoko | Tiedostomäärän oletusraja | Tiedostomäärän enimmäisraja |
|-----------|------------|--------------|---------------------------|-----------------------------|
| projappl&nbsp;(Puhti)  |   50 GiB     |  200&nbsp;GiB&nbsp;(<&nbsp;100&nbsp;GiB)    | 100 000                   | 2 000 000&nbsp;(<&nbsp;500&nbsp;000)                 |
| scratch&nbsp;(Puhti)   |   1 TiB      |  100&nbsp;TiB&nbsp;(<&nbsp;20&nbsp;TiB)    | 1 000 000                 | 10&nbsp;000&nbsp;000 (<&nbsp;5&nbsp;000&nbsp;000)               |
| projappl&nbsp;(Mahti)  |   50 GiB     |  200&nbsp;GiB&nbsp;(<&nbsp;100&nbsp;GiB)    | 100 000                   | 2 000 000 (<&nbsp;500&nbsp;000)                 |
| scratch&nbsp;(Mahti)   |   1 TiB      |  200&nbsp;TiB&nbsp;(<&nbsp;40&nbsp;TiB)    | 1 000 000                 | 20&nbsp;000&nbsp;000&nbsp;(<&nbsp;10&nbsp;000&nbsp;000)               |

Huomaa, että laajennettu kiintiö kuluttaa Storage Billing Units -yksiköitäsi riippumatta siitä, kuinka paljon dataa hakemistossa todellisuudessa on. [Katso laskutus](billing.md) lisätietoja varten. Lisäksi automaattinen siivousprosessi jatkaa jouten olevien tiedostojen poistamista scratch-hakemistosta myös kiintiön kasvattamisen jälkeen.

## Tallennuskapasiteetin kasvattaminen Allaksessa { #increasing-the-storage-capacity-in-allas }

Uuden projektin oletuskiintiö on 10 TB, mutta sitä voidaan tarvittaessa kasvattaa. Allas on ensisijainen tallennuspaikka suurille aineistoille CSC-ympäristössä, joten jos työskentelet suurten aineistojen parissa, voit huoletta pyytää Allakseen suurempaa kiintiötä.

Allas-kiintiön kasvattamiseksi lähetä pyyntö osoitteeseen: servicedesk@csc.fi 
Kerro pyynnössä, mitä Allas-projektia käytät, kuinka paljon tallennustilaa tarvitaan ja millaista dataa Allakseen tallennetaan. Jos sinulla on tietoaineiston hallintasuunnitelma, liitä se mukaan. 

Huomaa, että datan tallentaminen Allakseen kuluttaa Storage Billing Units -yksiköitä. Allaksessa laskutus perustuu tallennetun datan määrään. Hinta on 1 Storage BU/TiBh, eli Allakseen tallennettu 1 TB dataa kuluttaa 24 Storage Billing Units -yksikköä päivässä ja 8760 Storage Billing Units -yksikköä vuodessa. [Kuinka hakea Billing Units -yksiköitä](how-to-apply-for-billing-units.md)

## Tallennuskapasiteetin kasvattaminen IDAssa { #increasing-the-storage-capacity-in-ida }

[Projektikiintiön seuranta ja säätäminen IDA-käyttöoppaassa](https://www.fairdata.fi/en/user-guides/user-guide/#project-quota)