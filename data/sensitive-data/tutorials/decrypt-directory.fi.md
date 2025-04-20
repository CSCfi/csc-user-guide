# Kaikkien tiedostojen salauksen purku hakemistossa {#decrypting-all-files-in-a-directory}

Graafinen Crypt4gh-käyttöliittymä tarjoaa helpon tavan salata ja purkaa
yksittäisiä tiedostoja. Kuitenkin salatut aineistot voivat sisältää suuren määrän
tiedostoja, jolloin tiedostokohtaisten salausten tai purkujen tekeminen
yksi kerrallaan voi olla liian työlästä.

Tämä ohje sisältää yksinkertaisia skriptausesimerkkejä, joiden avulla
salauksen purkuprosessin voi automatisoida.
Käytännössä automatisoitu purkuprosessi vaatii kaksi
toiminnallisuutta:

  1. Silmukan rakentaminen, joka löytää salatut tiedostot
  ja ajaa salauksen purkukomennon.

  2. Menetelmän, joka syöttää salauksen purkuun tarvittavan salasanan
  purkukomentoon automaattisesti.

Alla olevissa esimerkeissä oletamme, että meillä on hakemisto,
jonka nimi on _data1_. Hakemistossa on satoja tiedostoja,
joista salatut tiedostot tunnistaa _.c4gh_-päätteestä. Salaus
on tehty siten, että salauksen purku onnistuu salaisella avaimella _my-key.sec_,
joka on suojattu salasanalla: _badpasswd_.


## Salauksen purku bash-skriptillä Macissa ja Linuxissa {#decryption-using-bash-script-in-mac-and-linux}

Linux- ja Mac-koneissa `crypt4gh`-komentorivityökalu osaa
lukea yksityisen avaimen salasanan ympäristömuuttujasta
C4GH_PASSPHRASE. Ensimmäinen vaihe on siis tämän muuttujan asettaminen. Bash-kuoressa
tämä voidaan tässä tapauksessa tehdä komennoilla:

```bash
read C4GH_PASSPHRASE
export C4GH_PASSPHRASE
```

Find-komento voidaan käyttää kaikkien _.c4gh_-loppuisten tiedostojen listaamiseen
annetuissa hakemistossa (_data1_) ja sen alihakemistoissa.
Tätä listaa voidaan käyttää _for-silmukan_ syötteenä.

```bash
find data1 -name *.c4gh
```

Silmukan sisällä meidän täytyy määritellä nimi salauksen puretulle tiedostolle. Tässä tapauksessa
käytämme komentoputkea _rev | cut -c6- | rev_ leikataksemme viisi viimeistä
merkkiä pois salatun tiedoston nimestä (eli .c4gh), jolloin saadaan nimi
puretulle tiedostolle.

Varsinainen purku tehdään komennolla:

```bash
crypt4gh decrypt --sk my-key.sec < encrypted-file > decrypted-file
```

Näillä vaiheilla kokonainen skripti voisi näyttää tältä:

```bash
#!/bin/bash

echo "Anna my-key.sec-tiedoston salasana"
read C4GH_PASSPHRASE
export C4GH_PASSPHRASE

for f_encrypted in $(find data1 -name *.c4gh)
do
  echo "Puretaan $f_encrypted"
  #määrittele nimi puretulle tiedostolle
  f_decrypted=$(echo $f_encrypted | rev | cut -c6- | rev)
  crypt4gh decrypt --sk my-key.sec < "$f_encrypted" > $f_decrypted
done
```

Skripti voidaan suorittaa komennoilla:

```bash
  chmod u+x decryption_script
  ./chmod u+x decryption_script
```


## Salauksen purku Windows PowerShellilla {#decryption-using-windows-powershell}

Cryp4gh on saatavilla myös Windows-koneille, mutta Windows-versio
ei pysty lukemaan salaisen avaimen salasanaa ympäristömuuttujasta.
Tämän vuoksi on käytettävä _sda-cli.exe_-komentoa sen sijaan.
Tässä tapauksessa salasana voidaan tallentaa muuttujaan C4GH_PASSWORD.

Sda-cli.exe:n voi ladata täältä:
[https://github.com/NBISweden/sda-cli/releases](https://github.com/NBISweden/sda-cli/releases)

Kun komento on käytettävissä, salauksen purku voidaan tehdä seuraavilla
PowerShell-komennoilla. Tässä oletetaan, että purettavat aineistot ovat
hakemistossa _E:\data1_.

```powershell
$env:C4GH_PASSWORD = "badpasswd"
$files = (Get-ChildItem -Path 'E:\data1\'*.c4gh -Recurse).fullname

foreach ($f in $files) {
.\sda-cli decrypt -key .\my-key.sec $f  }
```