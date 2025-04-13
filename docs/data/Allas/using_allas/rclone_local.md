
# Paikallinen Rclone-konfiguraatio Allasta varten {#local-rclone-configuration-for-allas}

Rclone voidaan asentaa mihin tahansa käyttöjärjestelmään ja siten se tarjoaa tehokkaan tavan käyttää Allasta mistä tahansa tietokoneesta. Voit ladata kopion Rclonesta omalle tietokoneellesi alla olevasta linkistä.

* [Rclone-lataussivusto](https://rclone.org/downloads/)

Kun olet asentanut Rclonen, sinun on vielä konfiguroitava yhteys Allakseen. Rclone on komentorivisovellus, joten sekä konfigurointi että varsinainen käyttö tapahtuvat normaalisti komentorivillä: _Terminal_ Macissa ja Linuxissa, _Komentokehote_ tai _Powershell_ Windowsissa.

## Allas-yhteyden konfigurointi Macissa ja Linuxissa (Swift ja S3) {#configuring-allas-connection-in-mac-and-linux-swift-and-s3}

Jos käytät Rcloneta paikallisessa **Linux**- tai **Mac-koneessa**, voit ladata `allas_conf`-sovelluksen asettaaksesi yhteyden Allas-projektiisi.

```bash
wget https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/allas_conf
source allas_conf -u your-csc-username -p your-csc-project-name
```

Huomaa, että sinun tulee käyttää `-u`-vaihtoehtoa määrittääksesi CSC-käyttäjänimesi ja `-p` määrittääksesi CSC-projektin, jota haluat käyttää. Esimerkiksi:

```bash
source allas_conf -u kkayttaj -p project_2001234
```

Yllä oleva komento määrittää yhteyden, joka käyttää Swift-protokollaa ja on voimassa nykyisessä
terminaalisessiossa 8 tuntia. Rclone _remote_-sivuston nimi on tässä tapauksessa _allas_. Konfiguroinnin jälkeen voit esimerkiksi listata ämpärisi Allaksessa komennolla:

```bash
rclone lsd allas:
```

Jos haluat käyttää S3-protokollaa Swifin sijasta, lisää konfigurointikomennolle vaihtoehto `-m S3`.

```bash
source allas_conf -u kkayttaj -p project_2001234 -m S3
```

Huomaa, että yllä olevan komennon suorittamiseen sinulla on oltava _OpenStack_-asiakas asennettuna paikalliseen koneeseesi. Kun olet konfiguroinut S3-yhteyden Allakseen, voit käyttää sitä Rclone-remotea nimeltä _s3allas:_ kautta. Esimerkiksi:

```bash
rclone lsd s3allas:
```

S3-yhteys on aktiivinen, kunnes poistat sen nimenomaisesti komennolla:

```bash
source allas_conf -u csc-user-name -p csc-project-name --s3remove
```

!!! Huomio
    Muista olla varovainen ja tietoturvatietoinen konfiguroidessasi S3-yhteyttä Allakseen. S3-avaimet tallennetaan luettavassa muodossa kotihakemistoosi, ja kuka tahansa, joka voi lukea avaimesi, voi käyttää Allasta, kunnes avaimet on nimenomaisesti peruutettu Allaksesta. Avainten poistaminen omalta tietokoneeltasi ei riitä deaktivoimaan niitä.

## Allas-yhteyden konfigurointi Windowsissa {#configuring-allas-connection-in-windows}

Windows-koneissa et voi käyttää `allas_conf`-sovellusta. Joten Windowsissa tietyt yhteyskohtaiset muuttujat on tarkistettava rinnakkain Linux-/Mac-koneesta, joka tukee `allas_conf`-sovellusta. Helpoin voisi olla Puhti, jos käytät sitä muuten. Yksi vaihtoehto on myös käyttää Windowsin Linux-alijärjestelmää, ja sitten voit seurata yllä olevia ohjeita.

Konfiguroi Allas-yhteys komennolla:

```bash
rclone config
```

Voit käyttää tätä komentoa myös muissa koneissa, joissa `allas_conf` ei ole saatavilla.
Yllä oleva komento käynnistää konfiguraatioprosessin, jota voit käyttää uuden Rclone-
yhteyden määrittämiseen. Rclonessa näitä määriteltyjä yhteyksiä kutsutaan nimellä _remotes_.

Alla kuvaamme, miten luodaan Swift- ja S3-yhteyksiä Allakseen.

#### Swift-yhteyden konfigurointi Windowsissa {#configuring-swift-connection-in-windows}

Aloita prosessi avaamalla PowerShell ja suorittamalla komento:

```bash
.\rclone.exe config
```

Interaktiivisessa konfiguraatioprosessissa tee seuraavat valinnat:

1. Valitse **n** luodaksesi _New remote_
2. Nimeä remote:ksi **allas**
3. Valitse tallennusprotokollaluettelosta numero, joka määrittelee:
_OpenStack Swift (Rackspace Cloud Files, Memset Memstore, OVH)_
4. Valitse todennusvaihtoehto **2**: _Get swift credentials from environment vars._
5. Valitse sen jälkeen oletus _tyhjä_ asetus kaikille jäljellä oleville asetuksille, kunnes olet takaisin konfiguraatioprosessin aloitusvalikossa.
6. Lopuksi valitse **q** lopettaaksesi konfiguraatioprosessi.

Swiftin tapauksessa tämä konfiguraatio tarvitsee tehdä vain kerran. Konfiguraatiossa
on nyt määritelty, että _allasta_ varten kaikki yhteyden tiedot luetaan ympäristömuuttujista.

Jos sinulla on pääsy Puhti-palveluun, helpoin tapa tarkistaa tarvittavien muuttujien arvot on avata siihen terminaaliyhteys ja aktivoida siellä yhteys haluamaasi Allas-projektiin. Toinen vaihtoehto on käyttää apuohjelmaa [allas-get-swift-token-win.zip](https://github.com/CSCfi/allas-get-swift-token/releases/download/v1.0.0/allas-get-swift-token-win.zip). Jos valitset apuohjelman käytön, sinun (tai paikallisen IT-tukesi) saattaa joutua konfiguroimaan virustorjunta- jne. ohjelmistosi sallimaan sen suorittamisen.

Jos käytät Puhtia Swift-pääsyoikeus muuttujien asettamiseen, aktivoi Allas-ympäristö Puhtissa komennoilla:

```bash
module load allas
allas-conf --show-powershell
```

Kun konfiguraatioprosessi Puhtissa on valmis, kopioi neljä viimeistä riviä, jotka alkavat `$Env:`, paikalliseen PowerShelliin ja suorita ne. Testaa sitten Rclone-yhteyttä komennolla:

```bash
  .\rclone.exe lsd allas:
```

Huomaa, että myös tässä tapauksessa yhteys toimii vain seuraavat 8 tuntia.

#### S3-yhteyden konfigurointi Windowsissa {#configuring-s3-connection-in-windows}

!!! Huomio
    Muista, että sinun on oltava varovainen ja tietoturvatietoinen konfiguroidessasi S3-yhteyttä Allakseen. S3-avaimet tallennetaan luettavassa muodossa kotihakemistoosi, ja kuka tahansa, joka voi lukea avaimesi, voi päästä Allakseen, kunnes avaimet on nimenomaisesti peruutettu Allaksesta. Avainten poistaminen omalta tietokoneeltasi ei riitä deaktivoimaan niitä.

Tarkistaaksesi S3-avaimesi, avaa yhteys Puhtiin (tai johonkin muuhun koneeseen, joka voi ajaa `allas_conf`-työkalua). Jos sinulla ei vielä ole S3-yhteyttä Allas-projektiin aktivoituna, avaa se komennoilla:

```
module load allas
allas-conf -m S3
```

Tämä luo paikallisen konfiguraatiotiedoston, jota käytämme myöhemmin tiettyjen arvojen tarkistamiseen.

Siirry sitten Windowsin _Komentokehoteen_ ja aloita Rclone-konfiguraatioprosessi suorittamalla komento:

```bash
rclone config
```

Ja tee seuraavat valinnat:

1. Valitse **n** luodaksesi _New remote_
2. Nimeä remote:ksi **s3allas**
3. Valitse tallennusprotokollaluettelosta numero, joka määrittelee: _Amazon S3 Compliant Storage Providers including AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, and Tencent COS_
4. Seuraavaksi sinua pyydetään valitsemaan S3-palveluntarjoajasi. Valitse vaihtoehto, joka tarjoaa _Any other S3 compatible provider_
5. Valitse sitten, että _Enter AWS credentials in the next step_
6. Anna _AWS access key_. Voit tarkistaa tämän Puhtissa komennolla:
`grep access_key $HOME/.s3cfg | cut -d " " -f3`
7. Anna _AWS secret access key_. Voit tarkistaa tämän Puhtissa komennolla:
`grep secret_key $HOME/.s3cfg | cut -d " " -f3`
8. Region: **1**
9. Endpoint: **a3s.fi**
10. Sijaintovakio: (tyhjä, paina vain Enteriä)
11. ACL: **1**
12. Advanced config: **n**
13. Remote config: **y** (kyllä, tämä on ok)
14. **q**, lopeta konfigurointi

Tämän jälkeen voit käyttää Allas-projektiasi Rclone remoten _s3allas_ avulla. Esimerkiksi:

```bash
rclone.exe lsd s3allas:
```

Tämä yhteys pysyy aktiivisena kannettavassasi, kunnes poistat sen.
