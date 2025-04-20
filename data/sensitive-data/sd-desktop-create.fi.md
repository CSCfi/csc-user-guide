# Luo virtuaalityöpöytiä {#create-virtual-desktops}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/wb4TwsqNCRE" title="Create a virtual desktop in SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/KgdGueesSe4" title="Luo virtuaalinen työpöytä SD Desktop -palvelussa" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

SD Desktop -palvelussa voit luoda virtuaalitietokoneita arkaluonteisten tietojen analysointiin. Virtuaalityöpöydälläsi voit analysoida arkaluontoista tutkimusdataa turvallisesti suoraan verkkoselaimen kautta. SD Desktop tarjoaa myös suojatun työtilan yhteistyöhankkeisiin. Voit luoda yhdelle CSC-projektille enintään kolme virtuaalityöpöytää. Virtuaalityöpöydän luominen ei vaadi teknistä osaamista.

## Vaihe vaiheelta {#step-by-step}

### 1. Kirjaudu SD Desktopiin {#1-log-in-to-sd-desktop}

* Kirjaudu SD Desktopiin.
* Napsauta **Siirry SD Desktopin hallintaan**.

![Go to SD Desktop Management.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_GoToManagement.png)

### 2. Valitse {#2-select}

1. oikea CSC-projekti
2. käyttöjärjestelmä. Suosittelemme valitsemaan **Linux Ubuntu22** -version, sillä Linux CentOS7:lle ei julkaista enää päivityksiä 30.6.2024 jälkeen.
3. työpöydän nimi. Kuvaava nimi on hyödyllinen erityisesti, jos työskentelet useissa projekteissa. Huomaa, että nimen tulee sisältää vain kirjaimia ja numeroita, eikä erikoismerkkejä tai välilyöntejä saa käyttää.
4. sopiva valmiiksi rakennettu työpöytä vaihtoehto tarpeesi mukaan. [Katso vaihtoehdot alempana](#virtual-desktop-options)

![Virtual desktop selections.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_SelectProject.png)

#### Virtuaalityöpöytä vaihtoehdot {#virtual-desktop-options}

|  | Käyttötarkoitus  | Tekniset tiedot | Vastaava Pouta Flavor | Laskutusyksikät |
|-|-|-|-|-|
|  **Pieni laskenta** | Sopii arkaluontoisen datan analysointiin toimisto-ohjelmilla (esim. yksinkertainen tilastoanalyysi Excelissä, videoiden katselu, äänitiedostojen kuuntelu, tekstin käsittely). Tätä voi verrata kannettavaan tietokoneeseen. | Core 6; Muisti 15 GB; Juurilevy 80 GB; | standard.xlarge | 5.2 laskutusyksikköä/h |
|  **Keskitasoinen laskenta**  | Sopii monimutkaisen tilastollisen tai genomianalyysin suorittamiseen (esim. komentoriviscriptien ajamiseen). Tätä voi verrata tehokkaaseen kannettavaan, jonka organisaatiosi IT-yksikkö on toimittanut. | Core 8; Muisti 30 GB; Juurilevy 80 GB | standard.xxlarge | 10.4 laskutusyksikköä/h |
| **Raskas laskenta**| Sopii ei-interaktiivisiin ohjelmallisiin analyyseihin (koneoppiminen), jotka vaativat paljon laskentatehoa. Älä valitse tätä vaihtoehtoa yksinkertaisiin analyyseihin, koska se kuluttaa paljon resursseja. | Core 28; Muisti 176 GB; Juurilevy 80 GB  | hpc.6.28 core | 65 laskutusyksikköä/h |
| **Pieni GPU-laskenta**| Saatavilla vain pyynnöstä. Ota yhteyttä servicedesk@csc.fi (aihe 'SD Desktop') ennen luontia, jotta saat lisätietoja ja vahvistuksen saatavuudesta. |  |  |  |
| **Big Picture -projekti**| Saatavilla vain pyynnöstä. Ota yhteyttä servicedesk@csc.fi (aihe 'SD Desktop') ennen luontia, jotta saat lisätietoja ja vahvistuksen saatavuudesta. |  |  |  |

!!! note
    Kaikki virtuaaliset GPU-työpöydät, jotka **luodaan ilman ennakkohyväksyntää**, poistetaan resurssien optimaalisen käytön varmistamiseksi. Ota yhteyttä servicedesk@csc.fi (aihe "Sensitive Data") saadaksesi lisätietoja ja apua suunnitteluun. Keskikokoisen GPU-laskennan vaihtoehto poistui käytöstä lokakuussa 2024.

### 3. Lisää ulkoinen levy (virtuaalinen ulkoinen kiintolevy) {#3-add-an-external-volume-virtual-external-hard-drive}

Lisää ulkoinen levy virtuaalityöpöydällesi laajentaaksesi oletustallennustilan (80 GB) jopa 200 GB:iin.

1. Valitse koko, joka kattaa aineistosi ja työtiedostojen yhteiskoon. Jos et ole varma sopivasta levyn koosta, lähetä sähköpostia [CSC Service Deskille](../../support/contact.md).

2. Anna levylle nimi. Huomaa, että levy nimenä ei saa käyttää erikoismerkkejä tai välilyöntejä.

* On suositeltavaa tallentaa kriittiset analyysit tai tiedostot levylle, joka voi toimia myös varmuuskopiona, jos virtuaalityöpöytä muuttuu toimimattomaksi. Huomaa, että kun työpöytä on luotu, levyä voidaan laajentaa lisätallennuksella ainoastaan, jos levylle ei ole vielä tallennettu tietoja. Laajennuspyyntöihin ota yhteyttä [CSC Service Deskiin](../../support/contact.md), *(aihe: SD Desktop)*.

* **Voit irrottaa ja liittää levyn virtuaalityöpöytääsi** SD Desktopin hallintasivulla. Tätä voi verrata kiintolevyn liittämiseen/irrottamiseen kannettavasta tietokoneesta. Tämä ominaisuus on käytettävissä vain työpöydissä, jotka on luotu helmikuun 2023 jälkeen. Lisätietoja: [Levyjen ja työpöytien hallinta](./sd-desktop-manage.md).

![Add volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_Volume.png)

### 4. Luo virtuaalityöpöytä {#4-create-virtual-desktop}

Lopuksi napsauta *Luo työpöytä*. Prosessi on täysin automatisoitu ja voi kestää jopa 30 minuuttia. Jos yrität käyttää virtuaalityöpöytää prosessin aikana, saat virheilmoituksen, jossa kehotetaan palaamaan myöhemmin.

!!! note
    Napsautuksen "Luo" jälkeen vahvistusilmoituksen saaminen voi kestää jopa 30 sekuntia. Jos olet epävarma siitä, onnistuiko toiminto, ota yhteyttä palvelupisteeseemme. Pahoittelemme mahdollista vaivaa.

![Create desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_CreateButton.png)

## Tärkeitä huomioita {#important-considerations}

* Virtuaalityöpöytäsi **on kaikkien projektin jäsenien käytettävissä luomisen jälkeen** ja **kuluttaa laskutusyksiköitä** CSC-projektistasi, kunnes se [keskeytetään](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) tai [poistetaan](./sd-desktop-manage.md#deleting-a-virtual-desktop).

* Yhdellä CSC-projektilla voi olla enintään 3 virtuaalityöpöytää, ja kullekin työpöydälle voi yhtäaikaisesti liittyä 10 projektijäsentä.

* Kaikissa työpöydissä on valmiiksi asennettu joukko avoimen lähdekoodin ohjelmistoja, joiden hallinnasta vastaa CSC. Lisätietoja asennetuista ohjelmistoista ja mukauttamisesta on saatavilla [tästä](./sd-desktop-software.md).

* **Poista tai keskeytä käyttämättömät työpöydät**: Muista [poistaa](./sd-desktop-manage.md#deleting-a-virtual-desktop) tai [keskeyttää](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) työpöytäsi, kun et enää käytä sitä. Käyttämättömistä työpöydistä lähetetään sähköposti-ilmoitukset 14 päivän käyttämättömyyden jälkeen.

!!! info "Tarvitsetko apua?"
    Jos olet epävarma sopivasta työpöydästä tai tarvitset tukea tutkimukseesi, ota yhteyttä [CSC Service Deskiin](../../support/contact.md) (aihe "Sensitive data").

## Seuraavat askeleet tässä oppaassa {#your-next-steps-in-this-guide}

* [Levyjen ja virtuaalityöpöytien hallinta](./sd-desktop-manage.md)
* [Virtuaalityöpöydän käyttö](./sd-desktop-access-vm.md)
* [Työskenteleminen työpöydällä: vinkit ja keskeiset asiat](./sd-desktop-working.md)
* [Mukauttaminen – ohjelmistot ja työkalut](./sd-desktop-software.md)
* [Aineiston tuonti](./sd-desktop-access.md)
* [Aineiston vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Aineiston vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)