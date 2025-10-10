# Paikkatietotiedostojen käyttäminen suoraan julkisista arkistoista ja S3-tallennuspalveluista, ml. Allas { #using-geospatial-files-directly-from-public-repositories-and-s3-storage-services-inc-allas }

[GDAL](https://gdal.org/) on keskeinen avoimen lähdekoodin kirjasto paikkatiedon lukuun ja kirjoitukseen, ja monet kehittyneet työkalut, kuten QGIS, ArcGIS, Python, R jne., tukeutuvat siihen. GDALissa on useita virtuaalisia [verkkopohjaisia tiedostojärjestelmiä](https://gdal.org/user/virtual_file_systems.html#network-based-file-systems), jotka on tarkoitettu erilaisille API-rajapinnoille ja käyttötapauksille. GDAL ja useimmat siihen perustuvat työkalut osaavat lukea suoraan julkisesta URL-osoitteesta tai S3-tallennuspalveluista. Tämä poistaa tarpeen ladata tiedostoja manuaalisesti ennen analyysiä. GDAL osaa myös kirjoittaa tiedostoja S3-palveluihin, mutta vain osa GDALiin tukeutuvista työkaluista tukee tätä.

Datan lukeminen suoraan ulkoisesta palvelusta on yleensä hitaampaa kuin paikalliselta levyltä lukeminen, mutta monissa tapauksissa nämä sekunnit ovat vähäisiä koko analyysin kestoon nähden. Hyvä Internet-yhteys on kuitenkin tärkeä.

S3-palvelut ovat hyvin yleisiä suurten datamäärien tallentamiseen, esimerkiksi:

* CSC [Allas](../../../data/Allas/index.md),
* EuroHPC [LUMI-O](https://docs.lumi-supercomputer.eu/storage/lumio/),
* ESA [Copernicus Data Space Ecosystem S3](https://documentation.dataspace.copernicus.eu/APIs/S3.html),
* Amazon [S3](https://aws.amazon.com/pm/serv-s3/),
* Google [Cloud Storage](https://cloud.google.com/storage),
* Microsoft [Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs/) jne.

Alla on lisätietoja GDALin käytöstä julkisille URL-tiedostoille (VSICURL) ja yksityisille S3-tiedostoille (VSIS3). Erityishuomio on CSC:n Allas-objektivarastossa ja supertietokoneissa. Supertietokoneella GDALia käytettäessä on aktivoitava moduuli, joka sisältää [GDAL](../../../apps/gdal.md).

## Julkisten tiedostojen lukeminen URL-osoitteesta { #reading-public-files-from-url }

[VSICURL](https://gdal.org/user/virtual_file_systems.html#vsicurl) soveltuu URL-osoitteen kautta saatavilla olevien tiedostojen lukemiseen. S3-tallennuksen julkisilla objekteilla on yleensä myös URL, joten tämä toimii myös S3:n julkisille tiedostoille. VSICURL tukee tiedostojen osittaista lukua, joten se toimii hyvin pilvioptimoitujen tiedostomuotojen kanssa. VSICURL tukee myös perusautentikointia.

```
# A public file
gdalinfo /vsicurl/URL

# For example, from Paituli
gdalinfo /vsicurl/https://www.nic.funet.fi/index/geodata/mml/orto/normal_color_3067/mara_v_25000_50/2023/N33/02m/1/N3324F.jp2

# CSC Allas
gdalinfo /vsicurl/https://a3s.fi/bucket_name/object_name
# OR alternatively
gdalinfo /vsicurl/https://bucket_name.a3s.fi/object_name

# Amazon S3 (us-west-2)
gdalinfo /vsicurl/https://s3.us-west-2.amazonaws.com/bucket_name/object_name

#Depending on GDAL installation settings VSICURL may sometimes work also without the `/vsicurl/` before the URL.
gdalinfo URL
```

## Tiedostojen luku ja kirjoitus S3-palveluista/palveluihin { #reading-and-writing-files-fromto-s3-services }

GDALin [VSIS3](https://gdal.org/user/virtual_file_systems.html#vsis3-aws-s3-files) on tarkoitettu työskentelyyn S3-palveluiden kanssa.

### S3-yhteyden määritykset { #s3-connection-details }

Jotta S3-palveluista voi käyttää dataa, yhteysasetukset on ensin määritettävä oikein. Yleensä tarvitaan seuraavat tiedot:

* endpoint-URL
* alue (region)
* käyttöavain (access key) ja salainen avain (secret key)

Kunkin palvelun käyttöohjeissa määritellään endpoint ja alue sekä kerrotaan, miten avaimet löytyvät. Suositeltavaa on tallentaa avaimet ja alueen nimi `credentials`-tiedostoon, joka sijaitsee Windowsissa `C:\Users\username\.aws\credentials` ja Macissa tai Linuxissa `~/.aws/credentials`. Esimerkiksi Allasta varten credentials-tiedosto voi näyttää tältä:

```
[allas_project1]
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=yyy
AWS_DEFAULT_REGION=regionOne
```

Endpoint-URL:ia ei tarvita Amazon S3:lle, mutta muille palveluille se tarvitaan. Valitettavasti sitä ei voi antaa asetustiedostojen kautta, vaan se pitää asettaa ympäristömuuttujaksi GDALia varten jokaisessa istunnossa, kun S3:ea käytetään.
Esimerkiksi Allaksen endpointin asettaminen:

* Windowsin komentotulkki: `set AWS_S3_ENDPOINT=a3s.fi`
* Linux/Mac: `export AWS_S3_ENDPOINT=a3s.fi`

#### S3-yhteyden määritys Allakselle { #s3-connection-set-up-for-allas }

Helpoin tapa määrittää `GDAL`:in S3-asetukset on
[määrittää S3-yhteys CSC:n supertietokoneella](../../../data/Allas/using_allas/allas-conf.md#s3-connection).

GDAL edellyttää lisäksi, että Allaksen endpoint annetaan AWS_S3_ENDPOINT-ympäristömuuttujana, katso yllä olevat komennot.

#### S3-yhteyden määritys Copernicus Data Space Ecosystemille (CDSE) { #s3-connection-set-up-for-copernicus-data-space-ecosystem-cdse }

ESA:n data, ml. Sentinel-aineistot, on saatavilla [CDSE S3:n](https://dataspace.copernicus.eu/) kautta. Hanki [CDSE S3 -tunnisteet](https://documentation.dataspace.copernicus.eu/APIs/S3.html) ja tallenna ne `credentials`-tiedostoon edellä kuvatulla tavalla. CDSE:tä käytettäessä `AWS_VIRTUAL_HOSTING` tulee asettaa arvoksi False:
```
export AWS_S3_ENDPOINT=eodata.dataspace.copernicus.eu
export AWS_VIRTUAL_HOSTING=FALSE
```

#### Useita yhteysprofiileja { #several-connection-profiles }
Kun työskentelet useiden CSC-projektien tai eri S3-tallennusten kanssa, `credentials`-tiedostoon voi määritellä useita profiileja:

```
[allas_project1]
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=yyy
AWS_DEFAULT_REGION = regionOne

[esa_cdse]
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=yyy
```

Ennen GDALin käyttöä kulloinkin käytössä oleva profiili on asetettava ympäristömuuttujaan: `export AWS_PROFILE=allas_project1`

### S3:n käyttäminen { #using-s3 }

```
# Reading data
gdalinfo /vsis3/<name_of_your_bucket>/<name_of_your_file>

# Writing data
export CPL_VSIL_USE_TEMP_FILE_FOR_RANDOM_WRITE=YES
gdal_translate /vsis3/<name_of_your_bucket>/<name_of_your_input_file> /vsis3/<name_of_your_bucket>/<name_of_your_output_file> -of COG
```

## GDAL-pohjaiset työkalut { #gdal-based-tools }

 * [ArcGIS Pro, yhteys pilvitallennukseen](https://pro.arcgis.com/en/pro-app/latest/help/projects/connect-to-cloud-stores.htm). Vain rastereille ja lukuun.
	* ArcGIS Pro kysyy kaikki yhteystiedot pilvitallennusyhteyttä luotaessa, joten `credentials`-tiedostoa tai ympäristömuuttujia ei tarvita.
 * QGIS:
 	* Sekä rasteri- että vektoritasojen [lisäysikkunoissa](https://docs.qgis.org/3.28/en/docs/user_manual/managing_data_source/opening_data.html#loading-a-layer-from-a-file) on vaihtoehdot lisätä dataa URL-osoitteesta (HTTPS) tai S3:sta. Vain luku.
	* Lisää S3-avaimet `credentials`-tiedostoon yllä kuvatulla tavalla tai käytä ympäristömuuttujia.
	* QGIS yhdistää oletuksena Amazon S3:een; yhdistääksesi johonkin muuhun palveluun lisää Asetukset -> Options -> Variables -kohtaan uusi muuttuja nimeltä AWS_S3_ENDPOINT; Allakselle arvo on `a3s.fi`.
 	* QGIS tukee myös pistepilviä URL-osoitteesta.
 * [Esimerkkikoodi Pythonilla Allaksen kanssa, rasterio, geopandas ja boto3](https://github.com/csc-training/geocomputing/blob/master/python/allas).
 * [Esimerkkikoodi R:llä Allaksen kanssa, terra, sf ja aws.s3](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R).