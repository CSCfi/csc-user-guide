# Paikkatiedot CSC:n laskentaympäristössä {#spatial-data-in-csc-computing-environment}

## Paikkatiedot Puhtissa {#spatial-data-in-puhti}

Puhtissa on seuraavat aineistot:

*   **Paituli-aineistot**. Paituli sisältää aineistoja seuraavilta tahoilta: Digi- ja väestötietovirasto, Ruokavirasto, Ilmatieteen laitos, Väylävirasto, Kotimaisten kielten keskus, Karelia-AMK, Maanmittauslaitos, Luonnonvarakeskus, Tilastokeskus ja Helsingin yliopisto. Viikoittaiset päivitykset. 
    -   [Täydellinen lista Paituli-aineistoista](https://paituli.csc.fi/metadata.html)
    -   Kaikissa Paituli-aineistoissa on readme-tiedosto, jossa on linkki Etsimessä oleviin aineistokuvauksiin ja käyttöehtoihin.
    -   Jos et löydä jotakin tiedostoa, voit käyttää apuna Paitulin lataussivua. Näet aineiston polun linkeistä (leikkaa alku pois) tai tarvittaessa voit ladata tiedostolistauksen "Download list of files" -toiminnolla, jos aineistossa on paljon lehtikarttoja.
    -   MML:n normaalivärisiä ortokuvia ei ole Puhtissa, mutta infrapunaiset ovat saatavilla.
    - Lisäykset MML:n aineistoihin:
        +   2m ja 10m DEM sekä infrapunaiset ortokuvat sisältävät virtuaalirasterit, ks. alla kohta Puhtin virtuaalirasterit.
        +   Stereoluokitellussa laserkeilausaineistossa on tehty pieniä korjauksia. Alkuperäisessä MML:n datassa oli virheitä otsikkotiedoissa, nämä on korjattu. Lisäksi on lisätty lax-indeksitiedostot.
        +   Automaattisesti luokiteltu laserkeilausaineisto, vain vuoden 2019 data.
    - Helpoin tapa löytää Paitulin rasteriaineistot on käyttää [Paituli STACia](https://paituli.csc.fi/stac.html), jossa on myös linkit Puhtin paikallisiin tiedostoihin.
*   **LUKE, monilähteinen valtakunnan metsien inventointi**, 2013, 2015, 2017, 2019 ja 2021. Luken lisenssi vaihtui elokuussa 2019 CC BY 4.0:aan.
*   **SYKE, kaikki avoimet paikkatietoaineistot** saatavilla [SYKEn avoimen datan palvelusta](https://www.syke.fi/fi-FI/Avoin_tieto/Paikkatietoaineistot/Ladattavat_paikkatietoaineistot).  Viikoittaiset päivitykset.
*   **Suomen metsäkeskus**, CC BY 4.0 -lisenssi, **päivitetty 8/2023**
    * [Latvusmalli](https://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/0e7ad446-2999-4c94-ad0d-095991d8f80a)
    * [Ruuturuudukot](http://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/3fa1beeb-ea6b-42b1-8e76-eb2bc8ac6d24)
    * [Metsämaski](https://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/df99fbd3-44b3-4ffc-b84a-9459f318d545)
    * [Metsävarantoruudut](http://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/332e5abf-63c2-4723-9c2d-4a926bbe587a)
*   **Landsat-mosaiikit SYKE:n ja FMI:n tuottamana** Paikkatietoalusta-hankkeessa
    -   [Historialliset Landsat-satelliittikuvamosaiikit](https://ckan.ymparisto.fi/dataset/historical-landsat-satellite-image-mosaics-href-historialliset-landsat-kuvamosaiikit-href): 1985, 1990, 1995
    -   [Historialliset Landsat NDVI -mosaiikit](https://ckan.ymparisto.fi/dataset/historical-landsat-image-index-mosaics-hind-historialliset-landsat-kuvaindeksimosaiikit-hind): 1984-2011

MML:n 2m DEM, laserkeilaus, infrapunaiset ortokuvat ja kaikki SYKEn aineistot päivittyvät Puhtissa automaattisesti joka maanantai.

Avoimet paikkatietoaineistot löytyvät Puhtista: **/appl/data/geo**

Aineiston käyttö Puhtissa vaatii CSC:n käyttäjätunnuksen ja projektin, jossa Puhti-palvelu on käytössä. Kaikilla Puhti-käyttäjillä on **lukuoikeus** näihin aineistoihin. Tiedostoja ei tarvitse siirtää: niitä voi käyttää suoraan, ellei niitä tarvitse muokata, mikä edellyttää oman kopion tekemistä. Avoimista paikkatiedoista Puhtissa vastaa CSC:n henkilöstö. Jos huomaat dataongelman tai toivot uutta aineistoa, ota yhteyttä CSC Servicedeskiin.

!!! warning "SYKEn ja FMI:n tuottamat Sentinel-satelliittimosaiikit Paikkatietoalusta-hankkeesta poistettiin Puhtista 21.11.2023" {#sentinel-satellite-mosaics-produced-by-syke-and-fmi-in-paikkatietoalusta-project-were-removed-from-puhti-on-21-11-2023}

    Poistetut aineistot olivat: [Sentinel1 SAR -mosaiikit](https://ckan.ymparisto.fi/dataset/sentinel-1-sar-image-mosaic-s1sar-sentinel-1-sar-kuvamosaiikki-s1sar), [Sentinel2 indeksimosaiikit](https://ckan.ymparisto.fi/dataset/sentinel-2-image-index-mosaics-s2ind-sentinel-2-kuvamosaiikit-s2ind). Ne ovat saatavilla FMI:n omasta objektitallennuksesta, jossa on enemmän dataa kuin Puhtissa. Helpoiten PTA Sentinel -mosaiikit FMI:n tallennuksesta löytää [Paituli STACin](https://paituli.csc.fi/stac.html) avulla. Paituli STAC -sivu sisältää myös käyttöesimerkkejä R- ja Python-kielillä.

## Paikkatietoaineistot Allaksessa {#spatial-data-in-allas}

CSC:n laskentapalveluiden käyttäjillä on mahdollisuus jakaa paikkatietoaineistoja [Allaksessa](../Allas/index.md) muille käyttäjille, mikäli aineiston lisenssiehdot sen sallivat. Tämä on yhteisöpalvelu, eli kuka tahansa CSC:n käyttäjä voi osallistua ja lisätä aineistoja Allakseen. Allaksen datakaukalot (bucketit) ovat tietoa tuottavien käyttäjien hallinnassa. Jos haluat jakaa jotakin Allaksessa olevaa dataasi muille ja toivoisit aineiston päätyvän tälle sivulle, ota yhteyttä CSC Servicedeskiin.

Tällä hetkellä saatavilla:

1.  **[Sentinel2 2A tason kuvat](https://a3s.fi/sentinel-readme/README.txt)**. Maria Yli-Heikkilä (LUKE) ja Arttu Kivimäki (MML/FMI) ovat ladanneet suomalaista dataa kasvukaudelta (noin 10.5.-1.9.) vuodesta 2016 eteenpäin. Helpoiten Allakseen tallennetun Sentinel-datan löytää [Paituli STACilla](https://paituli.csc.fi/stac.html). Tiedostot ovat julkisia, joten kuka tahansa voi ladata niitä myös omalta koneelta tai muista palveluista.

Ohjeita Allaksen paikkatiedon käyttöön löydät [CSC:n webinaarista Allaksesta ja paikkatiedoista](https://youtu.be/mnFXe2-dJ_g) sekä [Oppaasta: Paikkatietotiedostojen suora käyttö pilvestä, mukaan lukien Allas](../../support/tutorials/gis/gdal_cloud.md). 

## Puhtin virtuaalirasterit {#puhti-virtual-rasters}

Virtuaalirasterit on erittäin käytännöllinen konsepti suurten rasteriaineistojen kanssa työskentelyyn. Katso CSC:n [Virtuaalirasterit](../../support/tutorials/gis/virtual-rasters.md) -sivulta tarkempi selitys ja ohjeet virtuaalirasterien tekemiseen myös STAC-haun tuloksista.

### MML DEM- ja ortokuvien valmiit virtuaalirasterit {#nls-dem-and-orthophotos-ready-made-virtual-rasters}

CSC on liittänyt MML:n 2m ja 10m korkeusmalliaineistoihin sekä infrapunaisiin ortokuviin Puhtissa valmiita virtuaalirastereita. Korkeusmalleissa on kaksi virtuaalirasterin versiota:

1.  **Suora** virtuaalirasteri sisältää suoraan lähde-tif-tiedostot ilman hierarkkista rakennetta, yleiskatsauksia tai valmiiksi laskettuja tilastotietoja. Suorat virtuaalirasterit on tarkoitettu **vain skripteissä käytettäväksi**. Sitä **ei** tulisi avata QGIS-ohjelmassa, ellei tarkoituksena ole zoomata lähelle ja avata vain muutamia tiedostoja kerrallaan:
    *   2m DEM: `/appl/data/geo/mml/dem2m/dem2m_direct.vrt`
    *   10m DEM: `/appl/data/geo/mml/dem10m/dem10m_direct.vrt`
    *   infrapunaiset ortokuvat: `/appl/data/geo/mml/orto/infrared_3067/infrared_euref_direct.vrt`

2.  **Hierarkkinen** virtuaalirasteri on tarkoitettu pääasiassa **katseluun**, kuten esimerkiksi QGIS-ohjelmalla. Siinä on hakemistorakenteen mukainen hierarkia, jossa jokaisen kansion virtuaalirasteri sisältää kaiken siinä ja sen alakansioissa olevan datan. Hierarkkisessa tiedostorakenteessa on myös tilastotiedot (min, max, keskiarvo, hajonta) ja yleiskatsaukset (overview) jokaiselle vrt-tiedostolle. Tämän ansiosta koko DEM-aineistoa voi katsella varsin sujuvasti esimerkiksi QGIS-ohjelmassa eri zoomaustasoilla. Voit käyttää alimman tason virtuaalirasteria (esimerkiksi M41 2m DEM:ssä) myös skripteissä. Korkeammat tasot voivat aiheuttaa laskennallisia virheitä.

    *   2m DEM: `/appl/data/geo/mml/dem2m/dem2m_hierarchical.vrt`

### Puhti: luo DEM-virtuaalirasteri omalle alueelle {#puhti-create-virtual-rasters-of-dem-for-custom-area}

Joissakin tapauksissa voi olla hyödyllistä luoda virtuaalirasteri, joka kattaa vain oman tutkimusalueen tai osan siitä. CSC on tehnyt Python-skriptin, jolla voi rakentaa MML:n 2m ja 10m DEM-aineistojen perusteella virtuaalirasterin rajatulle alueelle Puhtissa. Skriptiä käytetään seuraavasti:

```
module load geoconda
python /appl/soft/geo/vrt/vrt_creator.py dataset polygon_file output_directory
```

Tuetut _dataset_-arvot ovat: dem2m, dem10m ja demCombined. Viimeinen vaihtoehto valitsee ensisijaisesti 2m DEM:n ja interpoloidaan loput alueet 2m-tarkkuuteen 10m DEM:n pohjalta bikubisen interpolaation avulla.

Valinnaiset argumentit:

*   -i: luo yksittäinen vrt jokaiselle polygonille; oletuksena tehdään yksi vrt koko polygonialueelle.
*   -o: luo yleiskatsaukset (overview)
*   -p: tulostiedoston etuliite


## Lisenssit ja aineiston maininta {#license-and-acknowledgement}

Yleisesti ottaen kaikilla aineistoilla on avoin lisenssi, mutta tarkemmat ehdot voivat vaihdella, useimmiten käytössä on CC-BY-4.0 -lisenssi. Tarkista lue lisää tiedostoista kunkin aineiston lisenssistä.

Muista mainita aineiston tuottaja lisenssiehtojen mukaisesti sekä CSC että Geoportti julkaisuissasi, sillä maininnat ovat tärkeitä hankkeiden jatkuvuuden ja rahoituksen raportoinnin kannalta. Jos käytät Allaksessa tarjottua dataa, mainitse myös datan jakanut henkilö.
Esimerkiksi voit kirjoittaa: "Kirjoittajat haluavat kiittää CSC:tä – Tieteen tietotekniikkakeskusta, Finland (urn:nbn:fi:research-infras-2016072531) ja Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) aineistojen saatavuudesta."