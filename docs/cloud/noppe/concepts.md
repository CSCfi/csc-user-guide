# Konseptit

Tämä asiakirja määrittelee terminologian Noppe-palvelussa.

Noppe on CSC:n pilvipalvelu interaktiivisille verkkopohjaisille sovelluksille

## Sovelluspohja {#application-template}

- Luo ylläpitäjä
- Määrittää sovelluskonteinerikuvan ja konfiguraation
- Määrittää resurssirajat (kuten muisti)
- Katso [kuvien lähdekoodi](https://github.com/CSCfi/noppe-public-images/tree/master/builds){target="_blank"} teknisiä yksityiskohtia varten

## Sovellus {#application}

- Esimääritelty sisältö yhdelle oppimistuokiolle
- Perustuu Docker-konttiin - joko JupyterLab tai RStudio
- Työpajapäällikön luoma sovelluspohjan perusteella

## Sovellussessio eli Sessio {#application-session-aka-session}

- Yksi käynnissä oleva kopio sovelluksesta
- Käyttäjä käynnistää ja hallitsee
- Sovellus määrittää eliniän

## Työtila {#workspace}

- Kontti sovelluksille ja käyttäjille
- Sidottu klusteriin
- Omistajalla
- Voi olla yhteisomistajia
- On elinikä
- Voi sisältää pysyviä kansioita (Työtilan `shared`, käyttäjien `my-work`). Katso [Tietojen pysyvyys Noppessa](data_persistence.md)
- Enimmäismäärä sovelluksia (oletusarvoisesti 10)
- Muistin kokonaismääräraja yhtäaikaisille sessioille

## Oma työkansio {#my-work-folder}

- Yksityinen hakemisto käyttäjää kohden työtilassa, joka tallentaa tietoja sovellussession käynnistysten välillä
- Käytettävissä sovellussessiossa (jos omistaja sen sallii) nimellä `$HOME/my-work`
- Sidottu työtilaan
- Elinikä sidottu työtilaan

## Työtilan jaettu kansio {#workspace-shared-folder}

- Jaettu hakemisto, joka on saatavilla kaikille työtilan käyttäjille
- Kirjoitusoikeus vain työpajapäälliköllä
- Sidottu työtilaan
- Elinikä sidottu työtilaan
- Huomaa, että muistikirjatiedostoja ei tulisi suorittaa "shared"-kansiossa vaan siirtää "my-work"-kansioon

## Liittymiskoodi {#join-code}

- Yksilöllinen koodi, joka luodaan jokaiselle työtilalle
- Työtilan omistaja jakaa tämän koodin, jotta käyttäjät voivat liittyä työtilaan

## Loppukäyttäjä {#end-user}

- Työtilan jäsen tai julkisten sovellusten käyttäjä
- Todennettu
- Voi käynnistää sovellussessioita
- Pääsy julkisiin sovelluksiin
- Voi kuulua työtiloihin
- Pääsy työtilan sovelluksiin jäsenyyden kautta

## Työtilan omistaja {#workspace-owner}

- Käyttäjä, joka omistaa työtilat tai jolle on annettu kiintiö työtilojen luomiseen
- Työtilan johtaja
- Luo työtilan ja sisällön työtilan jäsenille
- Voi kutsua käyttäjiä jäseniksi jakamalla liittymiskoodin
- Voi ylentää jäseniä yhteisomistajiksi
- Voi alentaa yhteisomistajia jäseniksi
- Voi lisätä sovelluksia sovelluspohjien perusteella

## Työtilan yhteisomistaja {#workspace-co-owner}

- Voi luoda sisältöä työtilassa
- Voi ylentää jäseniä yhteisomistajiksi
- Voi alentaa yhteisomistajia jäseniksi
- Voi kutsua käyttäjiä jäseniksi jakamalla liittymiskoodin
- Voi lisätä sovelluksia sovelluspohjien perusteella

## Ylläpitäjä {#admin}

- Järjestelmänvalvoja CSC:ssä
- Täydet oikeudet järjestelmässä

## Klusteri {#cluster}

- Resurssi sovellussessioiden suorittamiseen
- Käytännössä: jonkinlainen Kubernetes-klusteri CSC:n pilvessä
- Ylläpitäjän konfiguroima