# Paikkatieto CSC:n laskentaympäristössä { #spatial-data-in-csc-computing-environment }
## Paikkatieto Puhtissa { #spatial-data-in-puhti }

Puhtissa on seuraavat aineistot:

*   **Paituli-aineistot**. Paituli sisältää aineistoja Digi- ja väestötietovirastosta, Ruokavirastosta, Ilmatieteen laitokselta, Väylävirastosta, Kotimaisten kielten keskuksesta, Karelia-ammattikorkeakoulusta, Maanmittauslaitokselta, Luonnonvarakeskukselta, Tilastokeskukselta ja Helsingin yliopistolta.
    -   [Paituli-aineistojen täydellinen luettelo](https://paituli.csc.fi/metadata.html)
    -   Kaikissa Paituli-aineistoissa on readme-tiedosto, jossa on linkki Etsimen aineistokuvauksiin ja käyttöehtoihin.
    -   Jos jonkin tiedoston löytäminen on hankalaa, voit käyttää apuna myös Paitulin lataussivua. Näet aineiston polun linkkien alla (leikkaa alusta tarpeeton osa), tai voit ladata tiedostolistan valinnalla ”Download list of files”, jos aineistossa on paljon karttalehtiä.
    -   MML:n normaaliväriset ortokuvat eivät ole saatavilla Puhtissa, mutta infrapunaiset ovat.
    -   MML:n 2 m DEM, lidar ja infrapunaortokuvat päivittyvät Puhtissa automaattisesti joka maanantai.
    -   Lisäykset MML:n aineistoihin:
        + 2 m ja 10 m DEM sekä infrapunaortokuvat on varustettu virtuaalirastereilla; katso alempana Puhti-virtuaalirasterit.
        + Stereoluokiteltua lidar-aineistoa on hieman muokattu. Alkuperäisessä MML-aineistossa oli virheitä otsakkeissa; nämä on korjattu. Lisäksi lax-indeksitiedostot on lisätty.
        + [Automaattisesti luokiteltu lidar](https://www.maanmittauslaitos.fi/kartat-ja-paikkatieto/aineistot-ja-rajapinnat/tuotekuvaukset/laserkeilausaineisto-05-p), 2008–2024. Sisältää indeksikartan juurihakemistossa. Viimeisin päivitys 5/2025.
    -   Helpoin tapa löytää Paitulin rasteriaineistoja on [Paituli STAC](https://paituli.csc.fi/stac.html); siellä on myös linkit Puhtin paikallisiin tiedostoihin.
*   **SYKE, kaikki avoimet paikkatietoaineistot** saatavilla [SYKEn avoimen datan palvelusta](https://www.syke.fi/fi-FI/Avoin_tieto/Paikkatietoaineistot/Ladattavat_paikkatietoaineistot). Viimeisin päivitys 1/2025.
*   **Suomen metsäkeskus**, CC BY 4.0 -lisenssi, viimeisin päivitys 8/2023
    * [Latvusmalli](https://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/0e7ad446-2999-4c94-ad0d-095991d8f80a)
    * [Ruutuaineisto](http://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/3fa1beeb-ea6b-42b1-8e76-eb2bc8ac6d24)
    * [Metsämaski](https://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/df99fbd3-44b3-4ffc-b84a-9459f318d545)
    * [Metsävarakoealat](http://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/332e5abf-63c2-4723-9c2d-4a926bbe587a)
*   **SYKEn ja Ilmatieteen laitoksen tuottamat Landsat-mosaiikit** Paikkatietoalusta-hankkeessa
    -   [Historialliset Landsat-satelliittikuvamosaiikit](https://ckan.ymparisto.fi/dataset/historical-landsat-satellite-image-mosaics-href-historialliset-landsat-kuvamosaiikit-href): 1985, 1990, 1995

Avoin paikkatieto on tallennettu Puhtissa: **/appl/data/geo**

Aineistojen käyttö Puhtissa edellyttää CSC-käyttäjätiliä ja projektia, jossa Puhti-palvelu on käytössä. Kaikilla Puhti-käyttäjillä on näihin aineistoihin **luku**oikeus. Tiedostoja ei tarvitse siirtää: niitä voi käyttää suoraan, ellei niitä tarvitse muokata – muokkaus edellyttää oman kopion tekemistä. Puhtin avointa paikkatietoa ylläpitää CSC:n henkilökunta. Jos havaitset aineistoissa ongelmia tai toivot uusia aineistoja, ota yhteyttä CSC Servicedeskiin.

!!! note "Paikkatietoalusta-hankkeessa SYKEn ja Ilmatieteen laitoksen tuottamat satelliittimosaiikit poistettiin Puhtista 21.11.2023"

    Poistetut aineistot olivat: [Sentinel1 SAR -mosaiikit](https://ckan.ymparisto.fi/dataset/sentinel-1-sar-image-mosaic-s1sar-sentinel-1-sar-kuvamosaiikki-s1sar), [Sentinel2-indeksimosaiikit](https://ckan.ymparisto.fi/dataset/sentinel-2-image-index-mosaics-s2ind-sentinel-2-kuvamosaiikit-s2ind) ja Landsat-indeksimosaiikit. Ne ovat saatavilla Ilmatieteen laitoksen (FMI) omasta objektitallennuksesta, jossa on enemmän dataa kuin mitä Puhtin paikallisille levyille oli tallennettu. Helpoin tapa löytää FMI:n PTA-mosaiikkeja on [Paituli STAC](https://paituli.csc.fi/stac.html). Paituli STAC -sivulla on myös käyttöesimerkkejä R:lle ja Pythonille.

## Paikkatieto Allaksessa { #spatial-data-in-allas }

CSC:n laskentapalveluiden käyttäjät voivat lisenssiehtojen salliessa jakaa paikkatietoa [Allaksessa](../Allas/index.md) muiden käyttäjien kanssa. Tämä on yhteisöpalvelu, eli kuka tahansa CSC:n käyttäjä voi osallistua ja lisätä dataa Allakseen. Allaksen datasankkojen omistajina toimivat datan jakajat. Jos haluaisit jakaa Allaksessa olevaa dataasi ja toivot aineiston lisättävän tälle sivulle, ota yhteyttä CSC Servicedeskiin.

Tällä hetkellä saatavilla:

1.  **[Sentinel2 tason 2A -kuvat](https://a3s.fi/sentinel-readme/README.txt)**. Maria Yli-Heikkilä (LUKE) ja Arttu Kivimäki (MML/FGI) ovat ladanneet suomalaisia aineistoja kasvukaudelta (noin 10.5.–1.9.) vuodesta 2016 alkaen. Helpoin tapa löytää Allakseen tallennettuja Sentinel-aineistoja on [Paituli STAC](https://paituli.csc.fi/stac.html). Nämä tiedostot ovat julkisia, joten kuka tahansa voi ladata ne, myös omalta tietokoneelta tai muista palveluista.

Allaksen datan käyttöön liittyen katso [CSC:n webinaari Allaksesta ja paikkatiedosta](https://youtu.be/mnFXe2-dJ_g) sekä [Paikkatietotiedostojen käyttö suoraan pilvestä, ml. Allas-ohje](../../support/tutorials/gis/gdal_cloud.md).

## Puhti-virtuaalirasterit { #puhti-virtual-rasters }

Virtuaalirasterit ovat erittäin kätevä tapa työskennellä suurten rasteriaineistojen kanssa. Katso CSC:n sivu [Virtual rasters](../../support/tutorials/gis/virtual-rasters.md) saadaksesi laajemman selityksen ja ohjeet omien virtuaalirasterien luomiseen, myös STAC-hakutuloksista.

### MML:n DEM- ja ortokuvat: valmiit virtuaalirasterit { #nls-dem-and-orthophotos-ready-made-virtual-rasters }
CSC on lisännyt Puhtiin MML:n 2 m ja 10 m korkeusmallien sekä infrapunaortokuvien virtuaalirasterit. Korkeusmalleille on kaksi virtuaalirasterivaihtoehtoa:

1.  **Suorat** virtuaalirasterit sisältävät suoraan lähteenä olevat tif-kuvat ilman hierarkkista rakennetta, yleiskatsauksia (overviews) tai valmiiksi laskettuja tilastoja. Suora virtuaalirasteri on tarkoitettu käytettäväksi **vain skripteissä**. Sitä **ei** tule avata QGIS:ssä, ellei ole zoomattu sisään ja tarve ole avata vain muutamia tiedostoja tms.:
    *   2 m DEM: `/appl/data/geo/mml/dem2m/dem2m_direct.vrt`
    *   10 m DEM: `/appl/data/geo/mml/dem10m/dem10m_direct.vrt`
    *   infrapunaortokuvat: `/appl/data/geo/mml/orto/infrared_3067/infrared_euref_direct.vrt`

2.  **Hierarkkinen** virtuaalirasteri on tarkoitettu pääasiassa **katseluun**, esimerkiksi QGIS:llä. Siinä on hierarkkinen rakenne, jossa kunkin kansion virtuaalirasteri sisältää kaiken kyseiseen kansioon ja sen alikansioihin tallennetun datan. Hierarkkinen tiedostorakenne sisältää myös tilastot (min, max, mean, stddev) ja yleiskatsaukset (overviews) jokaiselle vrt-tiedostolle, mikä mahdollistaa varsin sujuvan koko DEM-aineiston katselun esimerkiksi QGIS:ssä. Näin koko aineistoa on helppo tarkastella eri mittakaavoissa. Voit käyttää myös alinta hierarkiatasoa (esim. M41 2 m DEM:ssä) skripteissä; ylemmät tasot voivat aiheuttaa laskentavirheitä.

    *   2 m DEM: `/appl/data/geo/mml/dem2m/dem2m_hierarchical.vrt`

### Puhti: luo DEM:n virtuaalirasterit omalle alueelle { #puhti-create-virtual-rasters-of-dem-for-custom-area }

Joissakin tapauksissa voi olla hyödyllistä luoda virtuaalirastereita, jotka kattavat vain tutkimusalueesi tai sen osan. CSC on tehnyt Python-skriptin, jolla voi luoda Puhtissa MML:n 2 m ja 10 m DEM -aineistoista virtuaalirasterit omalle alueelle. Sitä käytetään seuraavasti:

```
module load geoconda
python /appl/soft/geo/vrt/vrt_creator.py dataset polygon_file output_directory
```

Tuetut _dataset_-arvot ovat: dem2m, dem10m ja demCombined. Viimeksi mainittu vaihtoehto käyttää ensisijaisesti 2 m DEM:iä aina kun sitä on saatavilla ja interpoloidaan loput alueet 2 m resoluutioon 10 m DEM:stä käyttäen bikubista interpolointia.

Valinnaiset argumentit:

*   -i: luo erillinen vrt jokaiselle polygonille; oletuksena luodaan yksi kaikki polygonit kattava vrt.
*   -o: luo yleiskatsaukset (overviews)
*   -p: tulostiedoston nimen etuliite

## Lisenssi ja kiitokset { #license-and-acknowledgement }

Yleisesti ottaen kaikilla aineistoilla on avoin lisenssi, mutta tarkat ehdot vaihtelevat hieman; useimmiten käytössä on CC BY 4.0. Katso lisätietoja readme-tiedostoista.

Mainitse julkaisuissasi lisenssiehtojen mukaisesti sekä aineiston tuottaja että CSC ja Geoportti; tämä on tärkeää hankkeen jatkumisen ja rahoitusraportoinnin kannalta. Jos käytät Allaksessa jaettua dataa, kiitä myös datan jakajaa.
Esimerkiksi: ”Tekijät kiittävät CSC:tä – Tieteen tietotekniikan keskusta, Suomi (urn:nbn:fi:research-infras-2016072531) ja avointa paikkatiedon tutkimusinfrastruktuuria Geoporttia (urn:nbn:fi:research-infras-2016072513) datan tarjoamisesta.”