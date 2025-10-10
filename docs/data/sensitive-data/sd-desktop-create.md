[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Luo virtuaalityöpöytiä { #create-virtual-desktops }

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/wb4TwsqNCRE" title="Create a virtual desktop in SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/KgdGueesSe4" title="Luo virtuaalinen työpöytä SD Desktop -palvelussa" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

SD Desktop -palvelulla voit luoda virtuaalisia tietokoneita arkaluonteisen datan analysointiin. Virtuaalityöpöydälläsi voit analysoida arkaluonteisia tutkimusaineistoja turvallisesti suoraan verkkoselaimella. Lisäksi SD Desktop tarjoaa turvallisen työtilan yhteisiin tutkimusprojekteihin. Voit luoda yhteen CSC-projektiin enintään kolme virtuaalityöpöytää. Virtuaalityöpöydän luominen ei vaadi teknistä osaamista.

## Vaihe vaiheelta { #step-by-step }

### 1. Kirjaudu SD Desktop -palveluun { #1-log-in-to-sd-desktop }

* Kirjaudu SD Desktop -palveluun.
* Napsauta **Go to SD Desktop Management**.

![Siirry SD Desktop Managementiin.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_GoToManagement.png)

### 2. Valitse { #2-select }

1. oikea CSC-projekti
2. käyttöjärjestelmä. Suosittelemme valitsemaan **Linux Ubuntu22**:n, sillä Linux CentOS7:lle ei julkaista päivityksiä 30.6.2024 jälkeen.
3. työpöydällesi nimi. Kuvaava nimi on hyödyllinen, erityisesti jos työskentelet useissa projekteissa. Huomaa, että nimen tulee sisältää vain kirjaimia tai numeroita; älä käytä erikoismerkkejä tai välilyöntejä.
4. valmiiksi määritetty työpöytävaihtoehto tarpeidesi mukaan. [Katso vaihtoehdot alta](#virtual-desktop-options)

![Virtuaalityöpöydän valinnat.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_SelectProject.png)

#### Virtuaalityöpöytävaihtoehdot { #virtual-desktop-options }

|  | Käyttötarkoitus  | Tekniset tiedot | Vastaava Pouta Flavor | Cloud Billing Units -kulutus |
|-|-|-|-|-|
|  **Pieni laskenta** | Ihanteellinen arkaluonteisen datan analysointiin toimisto-ohjelmilla (esim. yksinkertainen tilastollinen analyysi Excelillä, videoiden katselu, äänitiedostojen kuuntelu ja tekstitiedostojen käsittely). Voit verrata tätä työpöytää omaan kannettavaasi. | Ytimiä 6; Muisti 15 GB; Juurilevy 80 GB; | standard.xlarge | 5.2 Cloud Billing Units/h|
|  **Keskisuuri laskenta**  | Sopii monimutkaisten tilastollisten tai genomi-analyysien ajamiseen (esim. komentorivillä tiettyjen skriptien suoritus). Vastaa organisaatiosi IT-yksikön tarjoamaa tehokasta kannettavaa. | Ytimiä 8; Muisti 30 GB; Juurilevy 80 GB | standard.xxlarge | 10.4 Cloud Billing Units/h |
| **Raskas laskenta**| Sopii raskaasti laskevaa ei-interaktiivista ohjelmallista analyysiä (koneoppiminen) varten. Älä valitse tätä vaihtoehtoa yksinkertaisiin analyyseihin, sillä se kuluttaa runsaasti resursseja. | Ytimiä 28; Muisti 176 GB; Juurilevy 80 GB  | hpc.6.28 core | 65 Cloud Billing Units/h |
| **Pieni GPU-laskenta**| Tämä vaihtoehto on saatavilla vain pyynnöstä. Ota yhteyttä osoitteeseen servicedesk@csc.fi (aihe 'SD Desktop') ennen luontia vahvistaaksesi saatavuuden ja saadaksesi lisätietoja. |  |  |  |
| **Big Picture -projekti**| Tämä vaihtoehto on saatavilla vain pyynnöstä. Ota yhteyttä osoitteeseen servicedesk@csc.fi (aihe 'SD Desktop') ennen luontia vahvistaaksesi saatavuuden ja saadaksesi lisätietoja. |  |  |  |

!!! note
    Kaikki ilman ennakkohyväksyntää luodut virtuaaliset GPU-työpöydät poistetaan, jotta rajallisia resursseja voidaan käyttää optimaalisesti. Ota yhteyttä osoitteeseen servicedesk@csc.fi (aihe "Sensitive Data") saadaksesi lisätietoja ja suunnitteluapua. Keskisuuri GPU -laskentavaihtoehto poistettiin käytöstä lokakuussa 2024. 

### 3. Lisää ulkoinen taltio (virtuaalinen ulkoinen kiintolevy) { #3-add-an-external-volume-virtual-external-hard-drive }

Lisää virtuaalityöpöydällesi ulkoinen taltio, jolloin oletustallennustila (80 GB) laajenee jopa 200 gigatavuun.

1. Valitse koko, joka kattaa aineistosi ja työtiedostojesi yhteiskoon. Jos et ole varma, minkä kokoisen taltion tarvitset, lähetä sähköpostia [CSC Service Deskille](../../support/contact.md).

2. Nimeä taltio. Huomaa, että taltion nimessä ei tule käyttää erikoismerkkejä tai välilyöntejä.

* On suositeltavaa tallentaa kriittiset analyysit tai tiedostot taltiolle, joka voi toimia varmuutena, jos virtuaalityöpöytä lakkaa vastaamasta. Huomaa, että virtuaalityöpöydän käyttöönoton jälkeen taltiota voidaan laajentaa lisätilalla vain, jos sille ei ole tallennettu dataa tai tiedostoja. Laajennusta varten ota yhteyttä [CSC Service Deskiin](../../support/contact.md), *(aihe: SD Desktop)*.

* **Voit irrottaa ja liittää taltion virtuaalityöpöydästäsi** SD Desktop Management -sivulla. Tämä vastaa kiintolevyn kytkemistä/irrottamista kannettavasta. Ominaisuus on käytettävissä vain työpöydissä, jotka on luotu helmikuun 2023 jälkeen. Lisätietoja: [Taltion ja työpöytien hallinta](./sd-desktop-manage.md).

![Lisää taltio.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_Volume.png)

### 4. Luo virtuaalityöpöytä { #4-create-virtual-desktop }

Lopuksi napsauta *Create desktop*. Toiminto on täysin automatisoitu ja voi kestää jopa 30 minuuttia. Jos yrität käyttää virtuaalityöpöytää prosessin aikana, näyttöön tulee virheilmoitus, jossa pyydetään palaamaan myöhemmin.

!!! Note
    Kun olet klikannut "Create", huomaa, että vahvistusilmoituksen ilmestyminen voi kestää jopa 30 sekuntia. Jos et ole varma, onnistuiko toiminto, ota yhteyttä Service Deskiin. Pahoittelemme tästä mahdollisesti aiheutuvaa vaivaa.

![Luo työpöytä.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_CreateButton.png)

## Tärkeitä huomioita { #important-considerations }

* Virtuaalityöpöytäsi on **kaikkien projektin jäsenten käytettävissä heti luomisen jälkeen** ja **kuluttaa CSC-projektisi Cloud Billing Units -yksiköitä**, kunnes se [keskeytetään](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) tai [poistetaan](./sd-desktop-manage.md#deleting-a-virtual-desktop).

* Jokaisessa CSC-projektissa voi olla enintään 6 virtuaalityöpöytää, ja jopa 10 projektin jäsentä voi olla samanaikaisesti yhteydessä kuhunkin työpöytään.

* Kaikkiin työpöytiin on esiasennettu joukko avoimen lähdekoodin ohjelmistoja, joita CSC hallinnoi. Lisätietoja esiasennetuista ohjelmistoista ja mukauttamisesta on saatavilla [delete](./sd-desktop-software.md).

* **Poista tai keskeytä käyttämättömät työpöydät**: Muista [poistaa](./sd-desktop-manage.md#deleting-a-virtual-desktop) tai [keskeyttää](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) työpöytäsi, kun et käytä sitä. Käyttämättömistä työpöydistä lähetetään sähköposti-ilmoituksia 14 päivän toimettomuuden jälkeen.
  

!!! info "Tarvitsetko apua?"
    Jos et ole varma, minkä työpöydän valitsisit, tai tarvitset tukea tutkimukseesi, ota yhteyttä [CSC Service Deskiin](../../support/contact.md) aiherivillä "Sensitive data".

## Seuraavat vaiheet tässä oppaassa { #your-next-steps-in-this-guide }

* [Taltion ja virtuaalityöpöytien hallinta](./sd-desktop-manage.md)
* [Virtuaalityöpöydälle kirjautuminen](./sd-desktop-access-vm.md)
* [Työskentely työpöydälläsi: vinkit ja perusasiat](./sd-desktop-working.md)
* [Mukauttaminen – ohjelmistot ja työkalut](./sd-desktop-software.md)
* [Datan tuonti](./sd-desktop-access.md)
* [Datan vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Datan vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)