# Luo virtuaalisia työpöytiä {#create-virtual-desktops}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/wb4TwsqNCRE" title="Create a virtual desktop in SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/KgdGueesSe4" title="Luo virtuaalinen työpöytä SD Desktop -palvelussa" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

SD Desktop -palvelun avulla voit luoda virtuaalisia tietokoneita arkaluonteisten aineistojen analysointiin. Virtuaalityöpöydälläsi voit analysoida herkkiä tutkimusaineistoja turvallisesti verkkoselaimen kautta. Lisäksi SD Desktop tarjoaa turvallisen työtilan yhteisiin tutkimusprojekteihin. Voit luoda yhteen CSC-projektiin enintään kolme virtuaalista työpöytää. Virtuaalityöpöydän luominen ei vaadi teknistä osaamista.

## Vaihe vaiheelta {#step-by-step}

### 1. Kirjaudu SD Desktopiin {#1-log-in-to-sd-desktop}

* Kirjaudu SD Desktopiin.
* Napsauta **Siirry SD Desktop -hallintaan**.

![Go to SD Desktop Management.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_GoToManagement.png)

### 2. Valitse {#2-select}

1. oikea CSC-projekti
2. käyttöjärjestelmä. Suosittelemme valitsemaan **Linux Ubuntu22**. Linux CentOS7:lle ei julkaista enää päivityksiä 30.6.2024 jälkeen.
3. työpöydällesi nimi. Kuvaava nimi on hyödyllinen etenkin silloin, kun työskentelet useissa projekteissa. Nimen tulee sisältää vain kirjaimia ja numeroita, erikoismerkkejä tai välilyöntejä ei tule käyttää.
4. valmiiksi rakennettu työpöytävaihtoehto tarpeidesi perusteella. [Katso vaihtoehdot alla](#virtual-desktop-options)

![Virtual desktop selections.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_SelectProject.png)

#### Virtuaalityöpöytävaihtoehdot {#virtual-desktop-options}

|  | Käyttö | Tekniset tiedot | Vastaava Pouta Flavor | Laskutusyksiköiden kulutus |
|-|-|-|-|-|
|  **Kevyt laskenta** | Ihanteellinen arkaluonteisen datan analysointiin toimisto-ohjelmistoilla (esim. yksinkertainen tilastoanalyysi Excelillä, videoiden katselu, äänitiedostojen kuuntelu sekä tekstityöskentely). Tätä voidaan verrata kannettavaasi. | Core 6; Muisti 15 GB; Juurilevy 80 GB; | standard.xlarge | 5,2 laskutusyksikköä/h|
|  **Keskiraskas laskenta**  | Soveltuu hyvin vaativampaan tilasto- tai genomianalyysiin (esim. komentorivillä erillisten skriptien ajamiseen). Tämä on verrattavissa organisaatiosi IT-yksikön tehokkaaseen kannettavaan. | Core 8; Muisti 30 GB; Juurilevy 80 GB | standard.xxlarge | 10,4 laskutusyksikköä/h |
| **Raskas laskenta**| Soveltuu hyvin ohjelmalliseen, ei-interaktiiviseen analyysiin (koneoppiminen), joka vaatii raskasta laskentaa. Älä valitse tätä vaihtoehtoa yksinkertaisiin analyyseihin, sillä se kuluttaa paljon resursseja. | Core 28; Muisti 176 GB; Juurilevy 80 GB  | hpc.6.28 core | 65 laskutusyksikköä/h |
| **Kevyt GPU-laskenta**| Tämä vaihtoehto on saatavilla vain pyynnöstä. Ota yhteyttä servicedesk@csc.fi (aihe 'SD Desktop') ennen luontia vahvistaaksesi saatavuuden ja saadaksesi lisätiedot |  |  |  |
| **Big Picture -projekti**| Tämä vaihtoehto on saatavilla vain pyynnöstä. Ota yhteyttä servicedesk@csc.fi  (aihe 'SD Desktop') ennen luontia vahvistaaksesi saatavuuden ja saadaksesi lisätiedot |  |  |  |

!!! note
    Kaikki virtuaaliset GPU-työpöydät, jotka on luotu **ilman ennakkohyväksyntää**, poistetaan resurssien optimaalisen käytön varmistamiseksi. Ota yhteyttä servicedesk@csc.fi (aihe "Sensitive Data") saadaksesi lisätietoja ja suunnittelutukea. Keskiraskas GPU-laskentavaihtoehto on poistettu käytöstä lokakuussa 2024.

### 3. Lisää ulkoinen levy (virtuaalinen ulkoinen kiintolevy) {#3-add-an-external-volume-virtual-external-hard-drive}

Lisää ulkoinen levy virtuaalityöpöydällesi, jolloin oletustallennustila (80 GB) kasvaa enintään 200 GB:hen.

1. Valitse koko, joka kattaa datasetisi ja työskentelytiedostojesi yhteenlasketun koon. Jos et ole varma, mitä levytilaa tarvitset, lähetä sähköposti osoitteeseen [CSC Service Desk](../../support/contact.md).

2. Nimeä levysi. Huomioi, ettei levyn nimessä tule olla erikoismerkkejä tai välilyöntejä.

* On suositeltavaa tallentaa tärkeimmät analyysit ja tiedostot levylle, joka toimii myös varmuuskopiona, jos virtuaalinen työpöytä muuttuu vastaamattomaksi. Huomaathan, että työpöydän käyttöönoton jälkeen levyä voi laajentaa vain, mikäli sille ei ole vielä tallennettu dataa tai tiedostoja. Laajennusta varten ota yhteyttä [CSC Service Desk](../../support/contact.md), *(aihe: SD Desktop)*.

* **Voit irrottaa ja liittää levyn virtuaalityöpöydältäsi** SD Desktop -hallintasivulla. Tätä voi verrata kiintolevyn liittämiseen/irrottamiseen kannettavaan tietokoneeseen. Ominaisuus on saatavilla vain työpöydillä, jotka on luotu helmikuun 2023 jälkeen. Lisätietoa löydät: [Levyjen ja työpöytien hallinta](./sd-desktop-manage.md).

![Add volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_Volume.png)

### 4. Luo virtuaalityöpöytä {#4-create-virtual-desktop}

Lopuksi napsauta *Luo työpöytä*. Prosessi on täysin automatisoitu ja voi kestää jopa 30 minuuttia. Jos yrität käyttää virtuaalityöpöytää tämän aikana, näytölle ilmestyy virheilmoitus, jossa pyydetään yrittämään myöhemmin uudelleen.

!!! Note
    "Luo"-painikkeen painamisen jälkeen huomioi, että vahvistusilmoituksessa voi kestää jopa 30 sekuntia. Jos olet epävarma, onko toimenpide onnistunut, ota yhteyttä palvelupisteeseemme. Pahoittelemme tästä mahdollisesti aiheutuvaa haittaa.

![Create desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_CreateButton.png)

## Tärkeitä huomioita {#important-considerations}

* Virtuaalityöpöytäsi on **kaikkien projektijäsenten käytettävissä heti luomisen jälkeen** ja **kuluttaa laskutusyksiköitä** CSC-projektiltasi, kunnes se [keskeytetään](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) tai [poistetaan](./sd-desktop-manage.md#deleting-a-virtual-desktop)

* Yksi CSC-projekti tukee enintään kolmea virtuaalista työpöytää, ja kymmeneen jäsentä voi olla yhteydessä kuhunkin työpöytään samanaikaisesti.

* Kaikilla työpöydillä on joukko valmiiksi asennettuja avoimen lähdekoodin ohjelmia, joiden hallinnasta vastaa CSC. Lisätietoa valmiista ohjelmistoista ja kustomoinnista löydät [delete](./sd-desktop-software.md).

* **Poista tai keskeytä käyttämättömät työpöydät**: Muista [poistaa](./sd-desktop-manage.md#deleting-a-virtual-desktop) tai [keskeyttää](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) työpöytäsi, kun se ei ole käytössä. Käyttämättömistä työpöydistä lähetetään sähköposti-ilmoitus 14 päivän käyttämättömyyden jälkeen.

!!! info "Tarvitsetko apua?"
    Jos olet epävarma, minkä työpöydän valitsisit tai tarvitset tukea tutkimukseesi, ota yhteyttä [CSC Service Desk](../../support/contact.md) otsikolla "Sensitive data".

## Seuraavat vaiheet tässä oppaassa {#your-next-steps-in-this-guide}

* [Levyjen ja virtuaalityöpöytien hallinta](./sd-desktop-manage.md)
* [Virtuaalityöpöydän käyttäminen](./sd-desktop-access-vm.md)
* [Työskentely työpöydälläsi: vinkkejä ja olennaisia asioita](./sd-desktop-working.md)
* [Kustomointi – ohjelmistot & työkalut](./sd-desktop-software.md)
* [Datan tuonti](./sd-desktop-access.md)
* [Datan vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Datan vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianetsintä](./sd-desktop-troubleshooting.md)