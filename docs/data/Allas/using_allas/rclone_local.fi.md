# Paikallinen Rclone-konfiguraatio Allasta varten {#local-rclone-configuration-for-allas}

Rclonen voi asentaa mihin tahansa käyttöjärjestelmään, joten se tarjoaa tehokkaan tavan käyttää Allasta miltä tahansa tietokoneelta. Voit ladata Rclonen oman koneesi seuraavasta linkistä.

* [Rclone lataussivu](https://rclone.org/downloads/)

Kun olet asentanut Rclonen, sinun täytyy vielä konfiguroida yhteys Allakseen. Rclone on komentorivityökalu, joten sekä konfigurointi että varsinainen käyttö tehdään normaalisti komentorivillä: _Terminal_ Macilla ja Linuxilla, _Komentokehote_ tai _Powershell_ Windowsissa.

## Allas-yhteyden konfigurointi Macilla ja Linuxilla (Swift ja S3) {#configuring-allas-connection-in-mac-and-linux-swift-and-s3}

Jos käytät Rclonea paikallisella **Linux**- tai **Mac**-koneella, voit ladata `allas_conf`-skriptin määrittääksesi yhteyden Allas-projektiisi.

```bash
wget https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/allas_conf
source allas_conf -u your-csc-username -p your-csc-project-name
```

Huomaa, että sinun tulee käyttää `-u`-optiota määrittääksesi CSC-käyttäjätunnuksesi ja `-p` määrittääksesi käytettävän CSC-projektin. Esimerkiksi:

```bash
source allas_conf -u kkayttaj -p project_2001234
```

Yllä oleva komento määrittää yhteyden, joka käyttää Swift-protokollaa ja on voimassa nykyisessä
terminaalisessiossa 8 tuntia. Rclonen _remote_-paikan nimi on tässä tapauksessa _allas_. Konfiguroinnin jälkeen voit esimerkiksi listata Allaksessa olevat bucketit komennolla:

```bash
rclone lsd allas:
```

Jos haluat käyttää Swiftin sijasta S3-protokollaa, lisää konfiguraatiokomennolle optio `-m S3`.

```bash
source allas_conf -u kkayttaj -p project_2001234 -m S3
```

Huomaa, että yllä olevan komennon suorittamista varten sinun täytyy olla _OpenStack_-asiakasohjelma asennettuna paikalliselle koneellesi. Kun S3-yhteys on määritetty Allakseen, voit käyttää sitä Rclonen _remote_-sivuston nimellä _s3allas:_. Esimerkiksi:

```bash
rclone lsd s3allas:
```

S3-yhteys on aktiivinen, kunnes poistat sen erikseen komennolla:

```bash
source allas_conf -u csc-user-name -p csc-project-name --s3remove
```

!!! Huom
    Muista olla tarkkana ja tietoturvatietoinen, kun konfiguroit S3-yhteyttä Allakseen. S3-avaimet tallentuvat kotihakemistoon luettavassa muodossa, ja jokainen joka pääsee lukemaan avaimiasi, voi käyttää Allasta kunnes avaimet poistetaan erikseen Allaksesta. Avainten poistaminen omalta koneeltasi ei riitä niiden käytöstä poistamiseen.

## Allas-yhteyden konfigurointi Windowsissa {#configuring-allas-connection-in-windows}

Windows-koneilla et voi käyttää `allas_conf`-skriptiä. Näin ollen Windowsissa jotkin yhteyskohtaiset muuttujat tulee tarkistaa rinnakkain Linux/Mac-järjestelmästä, joka tukee `allas_conf`-skriptiä. Helpoin vaihtoehto voi olla Puhti, jos muuten käytät sitä. Yksi vaihtoehto on myös käyttää Windowsin Linux-alijärjestelmää, jolloin voit noudattaa ylempiä ohjeita.

Määritä Allas-yhteys komennolla:

```bash
rclone config
```

Voit käyttää tätä komentoa myös muissa koneissa, joissa `allas_conf` ei ole saatavilla.
Yllä oleva komento käynnistää konfigurointiprosessin, jolla voit määrittää uuden Rclone-yhteyden. Rclonessa näistä määritetyistä yhteyksistä käytetään nimitystä _remote_.

Alla kerromme, kuinka luoda Swift- ja S3-yhteydet Allakseen.

#### Swift-yhteyden konfigurointi Windowsissa {#configuring-swift-connection-in-windows}

Aloita prosessi avaamalla PowerShell ja suorittamalla komento:

```bash
.\rclone.exe config
```

Vuorovaikutteisessa konfigurointiprosessissa tee seuraavat valinnat:

1. Valitse **n** luodaksesi _Uusi remote_
2. Anna remote-nimeksi: **allas**
3. Protokollalistasta valitse numero, joka määrittää kohteen:
_OpenStack Swift (Rackspace Cloud Files, Memset Memstore, OVH)_
4. Valitse todennustavaksi **2**: _Get swift credentials from environment vars._
5. Tämän jälkeen valitse oletusarvoinen _tyhjä_ asetus kaikille jäljellä oleville kentille kunnes palaat konfiguraatioprosessin aloitusvalikkoon.
6. Lopuksi valitse **q**, jotta lopetat konfiguraatioprosessin.

Swiftin tapauksessa tämä konfigurointi tarvitsee suorittaa vain kerran. Konfiguraatiossa on nyt määritetty, että _allas_-yhteyden tapauksessa kaikki yhteyden tiedot luetaan ympäristömuuttujista.

Jos sinulla on pääsy Puhtiin, helpoin tapa tarkistaa tarvittavat muuttujat on avata siihen terminaaliyhteys ja aktivoida haluamasi Allas-projekti. Toinen vaihtoehto on käyttää apuohjelmaa [allas-get-swift-token-win.zip](https://github.com/CSCfi/allas-get-swift-token/releases/download/v1.0.0/allas-get-swift-token-win.zip). Jos käytät apuohjelmaa, sinun (tai paikallisen IT-tukesi) voi joutua määrittämään virustorjunta tms. sallimaan sen suorittaminen.

Jos käytät Puhtia Swift-muuttujien asettamiseen, aktivoi Allas-ympäristö Puhtissa komennoilla:

```bash
module load allas
allas-conf --show-powershell
```

Kun konfiguraatioprosessi Puhtissa on valmis, kopioi viimeiset neljä riviä, jotka alkavat `$Env:`, paikalliseen PowerShelliin ja suorita ne. Testaa sitten Rclone-yhteyttä komennolla:

```bash
  .\rclone.exe lsd allas:
```

Huomaa, että myös tässä tapauksessa yhteys toimii vain seuraavat 8 tuntia.

#### S3-yhteyden konfigurointi Windowsissa {#configuring-s3-connection-in-windows}

!!! Huom
    Muista, että sinun tulee olla tarkkana ja tietoturvatietoinen, kun konfiguroit S3-yhteyden Allakseen. S3-avaimet tallennetaan kotihakemistoosi luettavassa muodossa, ja jokainen joka voi lukea avaimia, voi käyttää Allasta kunnes avaimet poistetaan erikseen Allaksesta. Avainten poistaminen omalta koneeltasi ei riitä niiden käytöstä poistamiseen.

Tarkistaaksesi S3-avaimet, avaa yhteys Puhtiin (tai toiseen koneeseen, jossa voi ajaa `allas_conf`-työkalua). Jos S3-yhteyttä ei ole vielä aktivoitu Allas-projektiin, avaa se komennoilla:

```
module load allas
allas-conf -m S3
```

Tämä luo paikallisen konfiguraatiotiedoston, jota käytämme myöhemmin tiettyjen arvojen tarkistamiseen.

Vaihda sitten Windowsin _Komentokehoteen_ ja käynnistä Rclonen konfigurointiprosessi komennolla:

```bash
rclone config
```

Tee seuraavat valinnat:

   1. Valitse **n** luodaksesi _Uusi remote_
   2. Anna remote-nimeksi: **s3allas**
   3. Protokollalistasta valitse numero, joka määrittää kohteen: _Amazon S3 Compliant Storage Providers including AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, and Tencent COS_
   4. Seuraavaksi sinulta kysytään _Choose your S3 provider_. Valitse vaihtoehto, joka tarjoaa _Any other S3 compatible provider_
   5. Valitse, että annat _AWS credentials in the next step_
   6. Anna _AWS access key._ Tarkista tämä Puhtissa komennolla: 
   `grep access_key $HOME/.s3cfg  | cut -d " " -f3`
   7. Anna _AWS secret access key._ Tarkista tämä Puhtissa komennolla:
   `grep secret_key $HOME/.s3cfg  | cut -d " " -f3`
   8. Region: **1**
   9. Endpoint: **a3s.fi**
   10. Location constant: (tyhjä, paina vain Enter)
   11. acl: **1**
   12. Edit advanced config: **n**
   13. Remote config: **y** (kyllä, tämä ok)
   14. **q**, lopeta konfiguraatio

Tämän jälkeen voit käyttää Allas-projektiasi Rclonen _s3allas_-remoten kautta. Esimerkiksi:

```bash
rclone.exe lsd s3allas:
```

Yhteys pysyy aktiivisena läppärissäsi kunnes poistat sen.