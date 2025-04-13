# CSC:n suurkoneympäristön Allas-objektitallennuspalvelun käyttö {#using-allas-object-storage-service-from-csc-supercomputing-environment}

CSC:n suurkoneiden, Puhtin ja Mahtin, levytilaympäristöjä ei ole tarkoitettu tutkimusdatan pitkäaikaiseen säilytykseen, mikäli dataa ei aktiivisesti käytetä laskentaan. Pidemmäksi ajaksi kuin muutamaksi viikoksi säilytettävä data tulisi kopioida Allas-objektitallennuspalveluun.

Allas tarjoaa alustan, jossa voit säilyttää dataasi niin kauan kuin CSC-projektisi on aktiivinen. Tietojen säilytyksen lisäksi Allas voi toimia tietojen kuljetusalustana eri palvelimien välillä ja tietojen jakamisessa muiden käyttäjien kanssa.

## Allaksen käyttöoikeuden hankkiminen {#getting-access-to-allas}

Oletusarvoisesti CSC-laskentaprojekteilla ei ole pääsyä Allakseen. Ensimmäinen askel on varmistaa, että projektillasi on pääsy Allakseen. Tämä voidaan tehdä [MyCSC-palvelussa](https://my.csc.fi). Huomaa, että vain projektipäällikkö voi lisätä uusia palveluita projektille. Kun Allas-käyttöoikeus on aktivoitu, kaikkien projekti jäsenten tulee käydä MyCSC:ssä hyväksymässä Allaksen käyttöehdot ennen kuin he voivat käyttää Allas-tilaa.

Allekirjoitettu tallennuskiintiö Allaksessa on 10 TB. Koska tämä tila on jaettu kaikkien projektin jäsenten kesken, tila ei välttämättä riitä. Tässä tapauksessa sinun tulisi arvioida tarvittava tila ja pyytää lisää tilaa. Pyyntö tulisi lähettää osoitteeseen servicedesk@csc.fi.

## Yhteys Allakseen {#connecting-allas}

Voidaksesi käyttää Allasta Puhtissa tai Mahtissa, lataa ensin _allas_-moduuli:
```text
module load allas
```
Allas-käyttöoikeuden tietylle projektille voi aktivoida komennolla:
```text
allas-conf
```
tai 
```text
allas-conf project_name
```
Komento _allas-conf_ kysyy CSC-salasanaasi. Se listaa Allas-projektisi ja pyytää määrittelemään projektin (jos sitä ei vielä ole annettu argumenttina). Tämän jälkeen _allas-conf_ luo konfiguraatiotiedostot useille Allas-asiakasohjelmille ja todentaa yhteyden Allakseen valitulle projektille.

Oletuksena _allas-conf_ aktivoi työkalut, jotka käyttävät Allasta **swift-protokollan** kautta. Voit vaihtoehtoisesti käyttää myös S3-protokollaa, mutta tässä dokumentissa käsitellään vain _swift_-pohjaista Allas-käyttöä.

Autentikointi on istuntokohtainen ja voimassa kahdeksan tuntia kerrallaan. Voit olla yhteydessä vain yhteen Allas-projektiin kerrallaan yhdessä istunnossa. Eri istunnot voivat kuitenkin käyttää eri Allas-projekteja. Käytettävän Allas-projektin ei tarvitse vastata Puhtissa tai Mahtissa käytettävää projektia. Voit päivittää autentikoinnin tai vaihtaa projektia milloin tahansa suorittamalla _allas-conf_ uudelleen.

**Allas-asiakkaan ohjelmistovaihtoehdot Puhtille, Mahtille ja muille Linux-palvelimille** {#allas-client-software-options-for-puhti-and-mahti-and-other-linux-servers}

_moduuli allas_ tarjoaa useita työkaluja, joilla voit siirtää dataa Allaksen ja laskentapalvelimen välillä. Voit käyttää ristiin Allas-asiakasohjelmia, kunhan käytät Allasta samalla protokollalla (swift tai S3). Alla on luettelo Allas-asiakasohjelmista, joita käytetään yleisimmin Puhtissa ja Mahtissa:

* **a-komennot:** (Swift, valinnaisesti S3) [Helppo ja turvallinen: a-komennot](../data/Allas/using_allas/a_commands.md)
* **rclone:** (Swift, valinnaisesti S3) [Edistynyt työkalu: rclone](../data/Allas/using_allas/rclone.md)
* **swift python -asiakasohjelma:** (Swift) [Natiivi Swift-asiakasohjelma](../data/Allas/using_allas/swift_client.md)
* **s3cmd:** (S3) [S3-asiakasohjelma](../data/Allas/using_allas/s3_client.md#configuring-s3-connection-in-supercomputers)

Lisätietoja Allaksen käytöstä löytyy Allas-dokumentaatiosta:

* [Allas](../data/Allas/index.md)

Allas-dokumentaatio sisältää kaksi tutoriaalia, jotka on erityisesti suunniteltu Puhtin ja Mahtin käyttäjille:

* [Esimerkkejä Allaksen käytöstä CSC:n suurkoneilla](../data/Allas/allas-examples.md)

* [Allaksen käyttö eräajotehtävissä](../data/Allas/allas_batchjobs.md)