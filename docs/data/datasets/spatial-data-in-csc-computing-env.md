
# Paikkatiedot CSC:n laskentaympäristössä
## Paikkatiedot Puhtissa {#spatial-data-in-puhti}

Puhtissa on seuraavat aineistot:

*   **Paituli-aineistot**. Paituli kattaa aineistoja Väestörekisterikeskukselta, Ruokavirastolta, Ilmatieteen laitokselta, Väylävirastolta, Kotimaisten kielten keskukselta, Karelia-ammattikorkeakoululta, Maanmittauslaitokselta, Luonnonvarakeskukselta, Tilastokeskukselta ja Helsingin yliopistolta. Viikoittaiset päivitykset.
    -   [Lista kaikista Paituli-aineistoista](https://paituli.csc.fi/metadata.html)
    -   Kaikilla Paituli-aineistoilla on readme-tiedosto, joka sisältää linkin Etsin-aineistokuvauksiin ja käyttöehtoihin.
    -   Jos on vaikeuksia löytää jotain tiedostoa, voit käyttää Paitulin lataussivua apuna. Voit nähdä aineiston polun linkin alla (rajata alusta) tai ladata tiedostojen listan "Download list of files" -linkistä, jos aineistolla on paljon karttalehtiä.
    -   Maanmittauslaitoksen normaalit värilliset orto-kuvat eivät ole saatavilla Puhtissa, mutta infrapunakuvat ovat.
    - Lisäykset Maanmittauslaitoksen aineistoihin:
        +   2m ja 10m DEM ja infrapuna-ortokuvat ovat saatavilla virtuaalirastereina, katso alla Puhti-virtuaalirastereista.
        +   Stereoluokiteltu lidar-data on hieman muokattu. Alkuperäisessä Maanmittauslaitoksen datassa oli virheitä otsikoissa, jotka on korjattu. Lisäksi lax-indeksitiedostot on lisätty.
        + Automaattisesti luokiteltu lidar-data, vain vuoden 2019 data
    - Helpoin tapa löytää Paitulin rasteridataa on [Paituli STAC](https://paituli.csc.fi/stac.html), joka sisältää myös linkit Puhtin paikallisiin tiedostoihin.
*   **LUKE, monilähteinen metsien inventointi**, 2013, 2015, 2017, 2019 ja 2021. LUKEn lisenssi muuttui elokuussa 2019, lisenssiksi tuli CC BY 4.0.
*   **SYKE, kaikki avoimet paikkatietoaineistot** saatavilla [SYKEn avointen tietojen palvelusta](https://www.syke.fi/fi-FI/Avoin_tieto/Paikkatietoaineistot/Ladattavat_paikkatietoaineistot). Viikoittaiset päivitykset.
*   **Verkkojen yhteys, CC BY 4.0 -lisenssi,** päivitetty 8/2023
    * [Lehtikorkeusmalli](https://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/0e7ad446-2999-4c94-ad0d-095991d8f80a)
    * [Ruutusolut](http://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/3fa1beeb-ea6b-42b1-8e76-eb2bc8ac6d24)
    * [Metsämaski](https://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/df99fbd3-44b3-4ffc-b84a-9459f318d545)
    * [Metsäresurssitontit](http://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/332e5abf-63c2-4723-9c2d-4a926bbe587a)
*   **SYKEn ja FMI:n tuottamat Landsat-mosaiikit** Paikkatietoalusta-hankkeessa
    -   [Historialliset Landsat-satelliittikuvamosaiikit](https://ckan.ymparisto.fi/dataset/historical-landsat-satellite-image-mosaics-href-historialliset-landsat-kuvamosaiikit-href): 1985, 1990, 1995
    -   [Historialliset Landsat NDVI -mosaiikit](https://ckan.ymparisto.fi/dataset/historical-landsat-image-index-mosaics-hind-historialliset-landsat-kuvaindeksimosaiikit-hind): 1984-2011

Maanmittauslaitoksen 2m DEM, lidar, infrapuna-ortokuvat ja kaikki SYKE-aineistot päivitetään Puhtissa automaattisesti joka maanantai.

Avoimet paikkatiedot tallennetaan Puhtissa: **/appl/data/geo**

Pääsy tietoihin Puhtissa vaatii CSC-käyttäjätilin ja projektin, jossa on Puhti-palvelu aktivoitu. Kaikilla Puhti-käyttäjillä on **luku**-oikeus näihin aineistoihin. Tiedostoja ei tarvitse siirtää: niitä voidaan käyttää suoraan, ellei niitä tarvitse muokata, mikä vaatii oman kopion luomisen. Puhtin avoimet paikkatiedot ylläpitää CSC:n henkilökunta. Jos huomaat ongelmia tiedoissa tai haluat uuden aineiston, ota yhteyttä CSC Servicedeskiin.

!!! warning "SYKEn ja FMI:n Paikkatietoalusta-hankkeessa tuottamat Sentinel-satelliittimosaiikit poistettiin Puhtista 21.11.2023"

    Poistetut aineistot olivat: [Sentinel1 SAR -mosaiikit](https://ckan.ymparisto.fi/dataset/sentinel-1-sar-image-mosaic-s1sar-sentinel-1-sar-kuvamosaiikki-s1sar), [Sentinel2 -indeksimosaiikit](https://ckan.ymparisto.fi/dataset/sentinel-2-image-index-mosaics-s2ind-sentinel-2-kuvamosaiikit-s2ind). Ne ovat saatavilla FMI:n omasta objektivarastosta, jossa on enemmän dataa kuin mitä oli tallennettu Puhtin paikallislevyille. Helpoin tapa löytää PTA Sentinel -mosaiikit FMI:stä on [Paituli STAC](https://paituli.csc.fi/stac.html). Paituli STAC -sivustoon sisältyy myös esimerkkejä käytöstä R:llä ja Pythonilla.

## Paikkatiedot Allaksessa {#spatial-data-in-allas}

CSC:n laskentapalveluiden käyttäjät ovat tervetulleita jakamaan paikkatietoa [Allas](../Allas/index.md)-palvelussa muiden käyttäjien kanssa, jos datan lisenssiehdot sallivat sen. Tämä on yhteisöpalvelu, mikä tarkoittaa, että mikä tahansa CSC:n käyttäjä saa vapaasti osallistua ja lisätä tietoa Allakseen. Allaksen datakoreja omistavat datayhteistyökumppanit. Jos haluat jakaa Allaksessa olevaa aineistoasi, ja haluat sen lisättävän tälle sivulle, ota yhteyttä CSC Servicedeskiin.

Tällä hetkellä saatavissa:

1.  **[Sentinel2 2A-tason kuvat](https://a3s.fi/sentinel-readme/README.txt)**. Maria Yli-Heikkilä (LUKE) ja Arttu Kivimäki (NLS/FGI) ovat ladanneet suomalaisia tietoja kasvukaudelta (n. 10.5.-1.9.) vuodesta 2016 alkaen. Helpoin tapa löytää Allakseen tallennettu Sentinel-data on [Paituli STAC](https://paituli.csc.fi/stac.html). Nämä tiedostot ovat julkisia, joten kuka tahansa voi ladata ne omalta tietokoneelta tai muista palveluista.

Allaksen datan käyttöön, katso [CSC-webinaari Allaksesta ja paikkatiedoista](https://youtu.be/mnFXe2-dJ_g) ja [Pilvitiedostojen suora käyttö, mukaan lukien Allas-opetus](../../support/tutorials/gis/gdal_cloud.md). 

## Puhti-virtuaalirasterit {#puhti-virtual-rasters}

Virtuaalirasterit ovat erittäin käytännöllinen konsepti isompien rasteriaineistojen käsittelyssä, katso CSC:n [Virtuaalirasterit](../../support/tutorials/gis/virtual-rasters.md) -sivu pidempään selitykseen ja kuinka luoda omia virtuaalirastereita, mukaan lukien STAC-haun tuloksista.

### Maanmittauslaitoksen DEM ja ortokuvat valmiit virtuaalirasterit
CSC on lisännyt Maanmittauslaitoksen 2m ja 10m korkeusmallit ja infrapuna-ortokuvat Puhtiin. Korkeusmalleille on kaksi erilaista virtuaalirasteriversiota:

1.  **Suorat** virtuaalirasterit sisältävät suoraan lähdetif-kvat ilman hierarkkista rakennetta, yleistyksiä tai ennalta laskettuja tilastoja. Suora virtuaalirasteri on tarkoitettu käytettäväksi **vain skripteissä**. Sitä ei pitäisi avata QGIS-ohjelmassa, ellei suoraan zoomata sisään ja tarvitse avata vain muutamia tiedostoja jne:
    *   2m DEM: `/appl/data/geo/mml/dem2m/dem2m_direct.vrt`
    *   10m DEM: `/appl/data/geo/mml/dem10m/dem10m_direct.vrt`
    *   infrapuna-ortokuvat: `/appl/data/geo/mml/orto/infrared_3067/infrared_euref_direct.vrt`

2.  **Hierarkkinen** virtuaalirasteri on ensisijaisesti **katselutarkoituksiin** esimerkiksi QGIS-ohjelmalla. Siinä on hierarkkinen rakenne, jossa jokaisessa kansiossa oleva virtuaalirasteri sisältää kyseiseen kansioon ja sen alikansioihin tallennetut tiedot. Hierarkkinen tiedostorakenne sisältää myös tilastotiedot (min, max, mean, stddev) ja tiivistelmät jokaiselle vrt-tiedostolle, mikä mahdollistaa varsin responsiivisen koko DEM-aineiston katselun esimerkiksi QGIS-ohjelmassa. Näin koko aineisto voidaan helposti nähdä eri zoomaustasoilla. Voit käyttää alinta tason virtuaalirasteria (esim. M41 2m DEM:ssä) myös skripteissä, mutta korkeamman tason virtuaalirasterit voivat aiheuttaa laskentavirheitä.

    *   2m DEM: `/appl/data/geo/mml/dem2m/dem2m_hierarchical.vrt`

### Puhti: luo virtuaalirasterit DEM:stä valitulle alueelle {#puhti-create-virtual-rasters-of-dem-for-custom-area}

Joissakin tapauksissa voi olla hyödyllistä luoda virtuaalirastereita, jotka kattavat vain oman tutkimusalueesi tai sen osan. CSC on tehnyt Python-skriptin virtuaalirasterien luomiseksi valitulle alueelle Maanmittauslaitoksen 2m ja 10m DEM-aineistoista Puhtissa. Sitä käytetään seuraavasti:

```
module load geoconda
python /appl/soft/geo/vrt/vrt_creator.py dataset polygon_file output_directory
```

Tuetut _dataset_-arvot ovat: dem2m, dem10m ja demCombined. Viimeinen vaihtoehto valitsee 2m DEM:in milloin se on saatavilla ja interpoloimalla loput alueet 2m-resoluutiolle 10m DEM:stä käyttämällä bicubic-interpolointia.

Valinnaiset argumentit:

*   -i: luo yksittäinen vrt jokaiselle polygonille, oletuskäytös on luoda yksi vrt, joka kattaa kaikki polygoneja.
*   -o: luo yleistykset
*   -p: tuloksen nimen etuliite

## Lisenssi ja tunnustukset {#license-and-acknowledgement}

Yleisesti ottaen kaikilla aineistoilla on avoin lisenssi, mutta tarkat ehdot vaihtelevat hieman, useimmiten käytössä on CC-BY-4.0-lisenssit. Katso lisätietoa readme-tiedostoista.

Ole hyvä ja tunnusta datan tuottaja lisenssiehtojen mukaisesti, sekä CSC että Geoportti julkaisuissasi, se on tärkeää projektin jatkumiselle ja rahoitusraporteille. Jos käytät Allakseen tarjottua dataa, ole hyvä ja tunnusta myös henkilö, joka jakaa dataa.
Esimerkiksi, voit kirjoittaa "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for data provision".
