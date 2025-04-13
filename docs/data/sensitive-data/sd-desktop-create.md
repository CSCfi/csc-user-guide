
# Luo virtuaalisia työpöytiä {#create-virtual-desktops}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/wb4TwsqNCRE" title="Create a virtual desktop in SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/KgdGueesSe4" title="Luo virtuaalinen työpöytä SD Desktop -palvelussa" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

SD Desktop -palvelun avulla voit luoda virtuaalisia tietokoneita arkaluonteisten tietojen analysointia varten. Virtuaalisella työpöydälläsi voit analysoida arkaluonteisia tutkimustietoja turvallisesti verkkoselaimen kautta. Lisäksi SD Desktop tarjoaa turvallisen työympäristön yhteistyöhön perustuville tutkimusprojekteille. Voit luoda enintään kolme virtuaalista työpöytää yhdessä CSC-projektissa. Virtuaalisen työpöydän luominen ei vaadi teknisiä taitoja.

## Vaihe vaiheelta {#step-by-step}

### 1. Kirjaudu SD Desktopiin {#1-log-in-to-sd-desktop}

* Kirjaudu SD Desktopiin.
* Klikkaa **Siirry SD Desktopin hallintaan**.

![Siirry SD Desktopin hallintaan.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_GoToManagement.png)

### 2. Valitse {#2-select}

1. oikea CSC-projekti
2. käyttöjärjestelmä. Suosittelemme valitsemaan **Linux Ubuntu22**, koska Linux CentOS7:lle ei julkaista päivityksiä 30. kesäkuuta 2024 jälkeen.
3. nimi työpöydällesi. Kuvaava nimi on hyödyllinen, erityisesti jos työskentelet useissa projekteissa. Huomaa, että nimen tulisi sisältää vain kirjaimia tai numeroita, eikä erikoismerkkejä tai välilyöntejä saa käyttää nimessä.
4. esirakennettu työpöytävalinta tarpeidesi mukaan. [Katso vaihtoehdot alta](#virtual-desktop-options)

![Virtuaaliset työpöytävalinnat.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_SelectProject.png)

#### Virtuaalisen työpöydän vaihtoehdot {#virtual-desktop-options}

|  | Käyttötarkoitus | Tekninen erittely | Pouta-vastaavuus | Laskutusyksiköiden kulutus |
|-|-|-|-|-|
| **Pieni laskenta** | Ihanteellinen arkaluonteisten tietojen analysointiin toimisto-ohjelmilla (esim. yksinkertainen tilastollinen analyysi Excelillä, videoiden katseleminen, äänitiedostojen kuuntelu ja tekstinkäsittely). Voit verrata tätä työpöytää omaan kannettavaasi. | Ydin 6; Muisti 15 GB; Juurilevy 80 GB; | standard.xlarge | 5.2 laskutusyksikköä/h |
| **Keskikokoinen laskenta** | Ihanteellinen monimutkaisen tilastollisen tai genomianalyysin suorittamiseen (esim. komentorivin käyttö skriptien suorittamiseen). Voit verrata tätä työpöytää organisaatiosi IT-osaston tarjoamaan tehokkaaseen kannettavaan. | Ydin 8; Muisti 30 GB; Juurilevy 80 GB | standard.xxlarge | 10.4 laskutusyksikköä/h |
| **Raskaampi laskenta** | Ihanteellinen ei-interaktiivisen ohjelmallisen analyysin (koneoppimisen) suorittamiseen, joka vaatii raskasta laskentatehoa. Ole hyvä äläkä valitse tätä vaihtoehtoa yksinkertaiseen analyysiin, koska se kuluttaa merkittävästi resursseja. | Ydin 28; Muisti 176 GB; Juurilevy 80 GB  | hpc.6.28 core | 65 laskutusyksikköä/h |
| **Pieni GPU-laskenta** | Tämä vaihtoehto on saatavilla vain pyynnöstä. Ole hyvä ja ota yhteyttä servicedesk@csc.fi (aihe 'SD Desktop') ennen luontia varmistaaksesi saatavuuden ja saadaksesi lisätietoja |  |  |  |
| **Suuri kuvaprojekti** | Tämä vaihtoehto on saatavilla vain pyynnöstä. Ole hyvä ja ota yhteyttä servicedesk@csc.fi (aihe 'SD Desktop') ennen luontia varmistaaksesi saatavuuden ja saadaksesi lisätietoja |  |  |  |

!!! huom
    Kaikki virtuaalipohjaiset GPU-työpöydät, joita on luotu **ilman ennakkohyväksyntää**, poistetaan, jotta resurssien käyttö on optimaalista. Ole hyvä ja ota yhteyttä servicedesk@csc.fi (aihe "Arkaluonteiset tiedot") saadaksesi lisätietoja ja suunnitellaksesi. Keskikokoisen GPU-laskennan vaihtoehto on lopetettu lokakuussa 2024.


### 3. Lisää ulkoinen levy (virtuaalinen ulkoinen kiintolevy) {#3-add-an-external-volume-virtual-external-hard-drive}

Lisää ulkoinen levy virtuaaliseen työpöytääsi, laajentaen oletustallennuksen (80 GB) jopa 200 GB:iin.

1. Valitse koko, joka kattaa datasetin ja työtiedostojen yhdistetyn koon. Jos et ole varma, minkä levykoon sinun tulisi valita, lähetä sähköpostia [CSC Service Deskiin](../../support/contact.md).

2. Nimeä volyymi. Huomaa, että volyymin nimi ei saa sisältää erikoismerkkejä tai välilyöntejä.

* On suositeltavaa tallentaa kriittiset analyysit tai tiedostot volyymille, joka voi toimia myös varmuuskopiona, jos virtuaalinen työpöytä lakkaa vastaamasta. Huomaa, että virtuaalisen työpöydän asennuksen jälkeen volyymi voidaan laajentaa lisäämällä tallennustilaa vain, jos sille ei ole tallennettu tietoja tai tiedostoja. Pyydä laajennusta ottamalla yhteyttä [CSC Service Deskiin](../../support/contact.md), *(aihe: SD Desktop)*.

* **Voit irrottaa ja liittää volyymin virtuaalisesta työpöydästäsi** SD Desktopin hallintasivulla. Tätä voidaan verrata kiintolevyn liittämiseen/irrottamiseen kannettavaasi. Tämä ominaisuus on saatavilla vain helmikuun 2023 jälkeen luoduilla työpöydillä. Lisätietoja: [Volyymin ja työpöytien hallinta](./sd-desktop-manage.md).

![Lisää volyymi.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_Volume.png)

### 4. Luo virtuaalinen työpöytä {#4-create-virtual-desktop}

Lopuksi, klikkaa *Luo työpöytä*. Toimenpide on täysin automatisoitu ja voi kestää jopa 30 minuuttia. Jos yrität päästä virtuaaliseen työpöytään tämän prosessin aikana, näkyviin tulee virheilmoitus, joka pyytää sinua palaamaan myöhemmin.

!!! Huomaa
    Kun olet klikannut "Luo", ole tietoinen, että vahvistusilmoitus voi kestää jopa 30 sekuntia ilmestyä. Jos et ole varma, oliko toiminto onnistunut, ole hyvä ja ota meihin yhteyttä palvelupisteeseen. Pahoittelemme mahdollisista epämukavuuksista.

![Luo työpöytä.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_CreateButton.png)

## Tärkeitä huomioita {#important-considerations}

* Virtuaalinen työpöytäsi on **saatavilla kaikille projektin jäsenille luomisen jälkeen** ja **kuluttaa laskutusyksiköitä** CSC-projektistasi kunnes [keskeytetty](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) tai [poistettu](./sd-desktop-manage.md#deleting-a-virtual-desktop)

* Jokainen CSC-projekti tukee enintään 3 virtuaalista työpöytää, ja 10 projektin jäsenellä on mahdollisuus yhdistää samanaikaisesti kuhunkin työpöytään.

* Kaikki työpöydät sisältävät valikoituja ennaltainstalletuja avoimen lähdekoodin ohjelmistoja, joita hallinnoi CSC. Lisää tietoa esiasennetuista ohjelmistoista ja mukauttamisesta on saatavilla [poista](./sd-desktop-software.md).

* **Poista tai keskeytä käyttämättömät työpöydät**: Varmista, että [poistat](./sd-desktop-manage.md#deleting-a-virtual-desktop) tai [keskeytät](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) työpöytäsi, kun et käytä sitä. Käyttämättömät työpöydät laukaisevat sähköposti-ilmoituksia 14 päivän käyttämättömyyden jälkeen.


!!! info "Tarvitsetko apua?"
    Jos olet epävarma siitä, minkä työpöydän valita tai tarvitset tukea tutkimuksellesi, ota yhteyttä [CSC Service Deskiin](../../support/contact.md), aihe "Arkaluonteiset tiedot".

## Seuraavat askeleet tässä oppaassa {#your-next-steps-in-this-guide}

* [Volyymien ja virtuaalisten työpöytien hallinta](./sd-desktop-manage.md)
* [Virtuaalisen työpöydän käyttäminen](./sd-desktop-access-vm.md)
* [Työskentely työpöydälläsi: vinkit ja välttämättömyydet](./sd-desktop-working.md)
* [Mukauttaminen - ohjelmistot ja työkalut](./sd-desktop-software.md)
* [Tiedon tuonti ](./sd-desktop-access.md)
* [Tietojen vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Vie tietoja ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)

