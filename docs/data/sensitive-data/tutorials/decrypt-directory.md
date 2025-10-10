# Kaikkien tiedostojen salauksen purkaminen hakemistossa { #decrypting-all-files-in-a-directory }

Graafinen Crypt4gh-käyttöliittymä tarjoaa helpon tavan salata ja purkaa
yksittäisiä tiedostoja. Salatut aineistot voivat kuitenkin sisältää suuren määrän
tiedostoja, jolloin tiedosto kerrallaan salaaminen tai salauksen purku
voi olla liian työlästä.

Tässä dokumentissa esitetään yksinkertaisia skriptausesimerkkejä
havainnollistamaan, miten salauksen purku voidaan automatisoida.
Käytännössä automatisoitu salauksen purkuprosessi vaatii kaksi
toiminnallisuutta:

  1. Silmukan rakentaminen, joka etsii salatut tiedostot
  ja suorittaa purkukomennon.

  2. Menetelmä, joka syöttää purkukomennoille salasanan
  automaattisesti.

Alla olevissa esimerkeissä oletetaan, että käytössä on hakemisto
nimeltä _data1_. Hakemistossa on satoja tiedostoja,
joista salatuilla on pääte _.c4gh_. Salaus on tehty siten, että
purku onnistuu salaisella avaimella _my-key.sec_,
joka on suojattu salasanalla: _badpasswd_.


## Salauksen purku bash-skriptillä Macissa ja Linuxissa { #decryption-using-bash-script-in-mac-and-linux }

Linux- ja Mac-koneissa komentorivityökalu `crypt4gh` osaa
lukea yksityisen avaimen salasanan ympäristömuuttujasta
C4GH_PASSPHRASE. Siksi ensimmäinen vaihe on asettaa tämä muuttuja. Bash-kuoressa
tämä voidaan tässä tapauksessa tehdä komennoilla:

```bash
read C4GH_PASSPHRASE
export C4GH_PASSPHRASE
```

find-komennolla voidaan listata kaikki _.c4gh_-päätteiset tiedostot
annetussa hakemistossa (_data1_) ja sen alihakemistoissa.
Tätä listaa voidaan käyttää syötteenä _for-silmukalle_.

```bash
find data1 -name *.c4gh
```

Silmukan sisällä meidän on määritettävä puretun tiedoston nimi. Tässä tapauksessa
käytämme komentoputkea _rev | cut -c6- | rev_ poistamaan salatun tiedostonimen viisi viimeistä
merkkiä (eli .c4gh), jotta saamme puretun datan tiedostonimen.

Varsinainen purku tehdään komennolla:

```bash
crypt4gh decrypt --sk my-key.sec < encrypted-file > decrypted-file
```

Näillä vaiheilla koko skripti voisi näyttää seuraavalta:

```bash
#!/bin/bash

echo "Give the password of my-key.sec"
read C4GH_PASSPHRASE
export C4GH_PASSPHRASE

for f_encrypted in $(find data1 -name *.c4gh)
do
  echo "Decrypting $f_encrypted"
  #define the file name for the decrypted data
  f_decrypted=$(echo $f_encrypted | rev | cut -c6- | rev)
  crypt4gh decrypt --sk my-key.sec < "$f_encrypted" > $f_decrypted
done
```

Skriptin voi suorittaa komennoilla:

```bash
  chmod u+x decryption_script
  ./decryption_script
```


## Salauksen purku Windows PowerShellilla { #decryption-using-windows-powershell }

Crypt4gh on saatavilla myös Windows-koneille, mutta Windows-versio
ei pysty lukemaan salaisen avaimen salasanaa ympäristömuuttujasta.
Siksi meidän täytyy käyttää sen sijaan komentoa _sda-cli.exe_.
Tässä tapauksessa salasana voidaan tallentaa muuttujaan C4GH_PASSWORD.

Sda-cli.exe-komennon voi ladata osoitteesta:
[https://github.com/NBISweden/sda-cli/releases](https://github.com/NBISweden/sda-cli/releases)

Kun komento on käytettävissä, salauksen purku voidaan tehdä seuraavilla
PowerShell-komennoilla. Tässä oletetaan, että purettava data on
hakemistossa _E:\data1_.

```powershell
$env:C4GH_PASSWORD = "badpasswd"
$files = (Get-ChildItem -Path 'E:\data1\'*.c4gh -Recurse).fullname

foreach ($f in $files) {
.\sda-cli decrypt -key .\my-key.sec $f  }
```