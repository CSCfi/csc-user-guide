# Kaikkien tiedostojen purkaminen kansiossa {#decrypting-all-files-in-a-directory}

Graafinen Crypt4gh-käyttöliittymä tarjoaa helpon tavan salata ja purkaa yksittäisiä tiedostoja. Kuitenkin, salatut tietoaineistot saattavat sisältää suuria määriä tiedostoja, ja näissä tapauksissa tiedostokohtainen salaus tai purku voi olla liian työlästä.

Tämä asiakirja tarjoaa yksinkertaisia skriptausesimerkkejä, jotka havainnollistavat, kuinka purkuprosessi voidaan automatisoida. Käytännössä automatisoitu purkuprosessi vaatii kahta toimintoa:

1. Silmukan rakentaminen, joka löytää salatut tiedostot ja suorittaa purkukomennon.

2. Menetelmän, joka tarjoaa automaattisesti purkulausekkeen purkukomennolle.

Alla olevissa esimerkeissä oletamme, että meillä on hakemisto nimeltä _data1_. Hakemisto sisältää satoja tiedostoja, joista salatut tiedostot ovat _.c4gh_-päätteisiä. Salaus on tehty niin, että purkaminen voidaan suorittaa salaisella avaimella _my-key.sec_, joka on suojattu salasanalla: _badpasswd_.

## Purku bash-skriptillä Macissa ja Linuxissa {#decryption-using-bash-script-in-mac-and-linux}

Linux- ja Mac-koneissa `crypt4gh`-komentorivityökalu pystyy lukemaan yksityisavaimen salasanan ympäristömuuttujasta C4GH_PASSPHRASE. Siksi ensimmäinen askel on asettaa tämä muuttuja. Bash-kuoressa tämä voidaan tehdä seuraavilla komennoilla:

```bash
read C4GH_PASSPHRASE
export C4GH_PASSPHRASE
```

Find-komentoa voidaan käyttää listaamaan kaikki tiedostot, jotka päättyvät _.c4gh_ annetussa hakemistossa (_data1_) ja sen alihakemistoissa. Tätä listaa voidaan käyttää syötteenä _for-silmukalle_.

```bash
find data1 -name *.c4gh
```

Silmukan sisällä meidän täytyy määritellä nimi puretulle tiedostolle. Tässä tapauksessa käytämme komentoputkea _rev | cut -c6- | rev_ leikkaamaan pois salatun tiedostonimen viimeiset viisi merkkiä (eli .c4gh), jotta määritämme puretun datan tiedostonimen.

Varsinainen purku suoritetaan komennolla:

```bash
crypt4gh decrypt --sk my-key.sec < encrypted-file > decrypted-file
```

Näillä askelilla koko skripti voisi näyttää seuraavalta:

```bash
#!/bin/bash

echo "Anna salasanan my-key.sec:lle"
read C4GH_PASSPHRASE
export C4GH_PASSPHRASE

for f_encrypted in $(find data1 -name *.c4gh)
do
  echo "Purkaa $f_encrypted"
  # määrittele tiedoston nimi puretulle datalle
  f_decrypted=$(echo $f_encrypted | rev | cut -c6- | rev)
  crypt4gh decrypt --sk my-key.sec < "$f_encrypted" > $f_decrypted
done
```

Skripti voitaisiin suorittaa komentoina:

```bash
  chmod u+x decryption_script
  ./chmod u+x decryption_script
```

## Purku Windows PowerShellin avulla {#decryption-using-windows-powershell}

Cryp4gh on saatavilla myös Windows-koneille, mutta Windows-versio ei pysty lukemaan salaisen avaimen salasanaa ympäristömuuttujasta. Tämän vuoksi meidän täytyy käyttää _sda-cli.exe_-komentoa sen sijaan. Tässä tapauksessa salasana voidaan tallentaa muuttujaan C4GH_PASSWORD.

Sda-cli.exe-komennon voi ladata osoitteesta:
[https://github.com/NBISweden/sda-cli/releases](https://github.com/NBISweden/sda-cli/releases)

Kun komento on saatavilla, purku voidaan suorittaa seuraavilla PowerShell-komennoilla. Tässä oletamme, että purettavat tiedot ovat hakemistossa _E:\data1_.

```powershell
$env:C4GH_PASSWORD = "badpasswd"
$files = (Get-ChildItem -Path 'E:\data1\'*.c4gh -Recurse).fullname

foreach ($f in $files) {
.\sda-cli decrypt -key .\my-key.sec $f  }
