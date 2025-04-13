
# Hakemisto-objektivirhe {#directory-object-error}

Allaksessa ei ole varsinaisia hakemistoja. Jotkin asiakasohjelmistot saattavat virheellisesti luoda nollakokoisia objekteja ja metatietoja tai lisätä kauttaviivan nimen loppuun.
```bash
Content Type: application/directory
Content Type: application/x-directory
Content Type: binary/octet-stream
```
**Se ei tee siitä hakemistoa.**

Tällaisia ohjelmistoja ovat esim. Cyberduck, Nextcloud ja s3fuse. Tämä on järkevää vain, jos kaikki dataa käyttävät käyttäjät käyttävät samanlaisia työkaluja ja erityisesti eivät käytä _s3cmd_:tä.

Esimerkiksi Cyberduckin lataama hakemistorakenne
```
data4.dat
mydata
├── data1.dat
├── data2.dat
└── subdir
    └── data3.dat
```
listattuna s3cmd:llä:

```bash
$ s3cmd ls -r s3://idev1clitest/
ls -r s3://idev1clitest/
2019-08-20 07:25   1048576   s3://idev1clitest/data4.dat
2019-08-20 07:22         0   s3://idev1clitest/mydata
2019-08-20 07:22      1024   s3://idev1clitest/mydata/data1.dat
2019-08-20 07:22    102400   s3://idev1clitest/mydata/data2.dat
2019-08-20 07:22         0   s3://idev1clitest/mydata/subdir
2019-08-20 07:22     10240   s3://idev1clitest/mydata/subdir/data3.dat
```

On olemassa nollakokoisia objekteja kuten mydata ja _mydata/subdir_. Ongelma, jonka tämäntyyppiset ylimääräiset objektit aiheuttavat, on se, että kun yritetään ladata rakennetta s3cmd:llä, nollakokoinen objekti ladataan tiedostoksi, mikä estää samannimisen hakemiston luonnin ja siten estää myös hakemiston sisällä olevien tiedostojen lataamisen:

```bash
$ s3cmd get -r s3://idev1clitest/
get -r s3://idev1clitest/
download: 's3://idev1clitest/data4.dat' -> './data4.dat'  [1 of 6]
 1048576 of 1048576   100% in    0s     9.79 MB/s  done
download: 's3://idev1clitest/mydata' -> './mydata'  [2 of 6]
 0 of 0     0% in    0s     0.00 B/s  done
ERROR: Skipping ./mydata/data1.dat: Not a directory
ERROR: Skipping ./mydata/data2.dat: Not a directory
ERROR: Skipping ./mydata/subdir: Not a directory
ERROR: Skipping ./mydata/subdir/data3.dat: Not a directory
$
```

Tällaisen hierarkian voi ladata _s3_:lla luomalla ensin jokaisen paikallisen hakemiston ja lataamalla sitten tiedostot hakemistotasolla.
