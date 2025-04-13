
# Onko mahdollista tehdä Allas-tiedoista vain luku -tilaan?

## Projektin sisällä {#inside-a-project}

Projektin sisällä ei tällä hetkellä ole Allas-ympäristössä **vain luku** -tilaa. Jokaisella projektin jäsenellä on täysi pääsy tietoihin, mikä aiheuttaa riskin: mikä tahansa projektin jäsen voi vahingossa korvata tai poistaa tietoja.

## Projektien välillä {#between-projects}

Voit antaa toiselle projektille vain luku -pääsyn säiliöösi käyttämällä
[Swiftiä](../../data/Allas/using_allas/swift_client.md#giving-another-project-read-and-write-access-to-a-bucket)
tai
[S3cmd](../../data/Allas/using_allas/s3_client.md#giving-another-project-read-access-to-a-bucket).

## URL:n jakaminen {#sharing-url}

Lisäksi on mahdollista tehdä säiliö julkiseksi, jolloin sen sisältö on nähtävissä ("vain luku") URL-osoitteiden kautta. Julkisen säiliön objektin URL on muotoa `https://<bucket_name>.a3s.fi/<object_name>` tai `https://a3s.fi/swift/v1/AUTH_<project_id>/<bucket_name>/<object_name>`, missä `<project_id>` on laskentaprojektisi tunniste [UUID](../../data/Allas/using_allas/s3_client.md#giving-another-project-read-access-to-a-bucket) muodossa.

## Lisäohjeita säiliöiden julkiseksi tekemiseen {#additional-guidance-for-making-buckets-public}

* [Web client](../../data/Allas/using_allas/web_client.md#view-objects-via-the-internet)
* [Swift client](../../data/Allas/using_allas/swift_client.md#giving-another-project-read-and-write-access-to-a-bucket)
* [S3 client](../../data/Allas/using_allas/s3_client.md#s3cmd-and-public-objects)
* [a-komennot](../../data/Allas/using_allas/a_commands.md#a-publish)

