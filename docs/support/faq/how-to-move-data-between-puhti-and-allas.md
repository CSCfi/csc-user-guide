
# Kuinka siirtää tietoja Puhtista Allakseen ja päinvastoin? {#how-to-move-data-from-puhti-to-allas-and-vice-versa}

Puhtin ja Allaksen välillä on useita vaihtoehtoja tietojen siirtämiseen. Tämä sivu tiivistää, miten tietoja voidaan siirtää käyttämällä _a-komentoja_, _Swiftiä_, _Rclonea_ ja _S3cmd_-asiakkaita.

Kaikki tarvittavat paketit ja ohjelmistot on jo asennettu Puhtille. Allaksen aktivoimiseksi ja projektiin kirjautumiseksi sinun tulee suorittaa komennot:

```bash
module load allas
allas-conf
```

## Siirrä tietoja a-komennoilla {#move-data-with-a-commands}

[a-komennot](../../data/Allas/using_allas/a_commands.md) ovat helppokäyttöisiä työkaluja Allaksen peruskäyttöön. Tärkeimmät komennot tietojen siirtämiseen Puhtin ja Allaksen välillä ovat:

* [`a-put`](../../data/Allas/using_allas/a_commands.md#a-put-uploads-data-to-allas):
  Siirrä tietoja Puhtista Allakseen
* [`a-get`](../../data/Allas/using_allas/a_commands.md#a-get-retrieves-stored-data):
  Siirrä tietoja Allaksesta Puhtiin 

## Siirrä tietoja Swiftillä {#move-data-with-swift}

Swift-asiakasohjelma tarjoaa vaihtoehdot `upload` ja `download` tietojen siirtämiseen:

```bash
swift upload <bucket name> <file name>
```

```bash
swift download <bucket name> <file name>
```

Lisätietoja löytyy
[Swift-asiakasohjelma](../../data/Allas/using_allas/swift_client.md):sta.

## Siirrä tietoja Rclonea käyttäen {#move-data-with-rclone}

Rclone on toinen asiakasohjelma, jolla voit siirtää tietoja Puhtin ja Allaksen välillä. Voit esimerkiksi luoda kauhan nimeltä `2000620-raw-data` Allakseen käyttämällä komentoa:

```bash
rclone mkdir allas:2000620-raw-data
```

Tiedoston nimeltä `file.dat` lataaminen tuohon kauhaan voidaan tehdä `rclone copy` -komennolla:

```bash
rclone copy file.dat allas:2000620-raw-data/
```

Tiedoston lataaminen takaisin Puhtiin tehdään samalla `rclone copy` -komennolla:

```bash
rclone copy allas:2000620-raw-data/file.dat .
```

!!! info "Huom"
    Toinen kohdehakemisto voidaan myös määrittää `rclone copy` -komennossa. Jos tätä hakemistoa ei ole olemassa, Rclone luo sen sinulle.

    ```bash
    rclone copy allas:2000620-raw-data/file.dat my-new-folder
    ```

Lisätietoja löytyy
[Allaksen käyttäminen Rclonella Puhtista](../../data/Allas/using_allas/rclone.md).

## Siirrä tietoja S3cmd:llä {#move-data-with-s3cmd}

Tietojen siirtämiseen Puhtin ja Allaksen välillä,
[S3cmd](../../data/Allas/using_allas/s3_client.md) tarjoaa seuraavat toiminnot:

* [`s3cmd put`](../../data/Allas/using_allas/s3_client.md#create-buckets-and-upload-objects):
  Siirrä tietoja Puhtista Allakseen

* [`s3cmd get`](../../data/Allas/using_allas/s3_client.md#download-objects-and-buckets):
  Siirrä tietoja Allaksesta Puhtiin

Lisätietoja löytyy
[S3-asiakasohjelma](../../data/Allas/using_allas/s3_client.md):sta.
