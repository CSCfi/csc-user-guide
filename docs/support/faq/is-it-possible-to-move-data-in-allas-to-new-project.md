
# Onko mahdollista siirtää dataa Allas-palvelussa uuteen projektiin? {#is-it-possible-to-move-data-in-allas-to-new-project}

Allas-palvelussa datan siirto projektien välillä voidaan tehdä antamalla vastaanottavalle projektille luku- tai kirjoitusoikeus dataa sisältävään ämpäriin. Toinen projekti voi sitten joko lukea dataa suoraan jaetusta ämpäristä tai kopioida datan omaan ämpäriinsä.

Voit antaa lukuoikeuden ämpäriin toiselle projektille
[S3cmd](../../data/Allas/using_allas/s3_client.md#giving-another-project-read-access-to-a-bucket)-
komennolla tai luku- ja kirjoitusoikeuden komennolla
[Swift](../../data/Allas/using_allas/swift_client.md#giving-another-project-read-and-write-access-to-a-bucket).

Toinen tapa siirtää dataa projektien välillä voisi olla datan lataaminen alkuperäisestä projektista ja sitten sen lataaminen uuteen projektiin. Katso
[ohjeet datan siirtämiseksi Puhtin ja Allaksen välillä](how-to-move-data-between-puhti-and-allas.md).
Puhtin sijasta voit myös käyttää toista supertietokonetta, pilviympäristöä, virtuaalikonetta tai paikallista tietokonettasi välivaiheena. Katso
[Allas-palvelun käyttäminen](../../data/Allas/accessing_allas.md).
