# Paikallinen Rclone-kokoonpano Allasta varten { #local-rclone-configuration-for-allas }

Rclone voidaan asentaa kaikkiin käyttöjärjestelmiin, joten sen avulla Allasta voi käyttää miltä tahansa tietokoneelta. Voit ladata Rclonen omalle koneellesi alla olevasta linkistä.

* [Rclonen lataussivusto](https://rclone.org/downloads/)

Kun Rclone on asennettu, Allas-yhteys täytyy vielä määrittää. Rclone on komentorivityökalu, joten sekä määritys että varsinainen käyttö tehdään tavallisesti komentoriviltä: _Terminal_ Macissa ja Linuxissa, _Command prompt_ tai _Powershell_ Windowsissa.

## Allas-yhteyden määrittäminen Macissa ja Linuxissa (Swift ja S3) { #configuring-allas-connection-in-mac-and-linux-swift-and-s3 }

Ensin [asenna `allas-conf` paikallisesti](allas-conf.md#allas-conf-installation) ja määritä yhteytesi.

```bash
# Swift
source allas_conf -u your-csc-username -p your-csc-project-name
# S3
source allas_conf -u kkayttaj -p project_2001234 -m S3
```

Rclone-komennoissa tähän Swift-pohjaiseen yhteyteen viitataan etänimellä `allas:` ja S3-yhteyteen nimellä `s3allas:`. 

## Allas-yhteyden määrittäminen Windowsissa { #configuring-allas-connection-in-windows }

Windows-koneissa et voi käyttää `allas_conf`-skriptiä. Siksi Windowsissa osa yhteyskohtaisista muuttujista täytyy tarkistaa rinnakkain Linux/Mac-ympäristöstä, jossa `allas_conf` toimii. Helpoin vaihtoehto on Puhti, jos käytät sitä muutenkin. Vaihtoehtoisesti voit käyttää Windows Subsystem for Linuxia, jolloin yllä olevia ohjeita voidaan noudattaa.

Määritä Allas-yhteys komennolla:

```bash
rclone config
```

Voit käyttää tätä komentoa myös muilla koneilla, joissa `allas_conf` ei ole käytettävissä. Yllä oleva komento käynnistää määritysprosessin, jonka avulla voit luoda uuden Rclone-yhteyden. Rclonessa näitä yhteyksiä kutsutaan nimellä remotes.

Alla kuvataan, kuinka luodaan Swift- ja S3-yhteydet Allakseen.

#### Swift-yhteyden määrittäminen Windowsissa { #configuring-swift-connection-in-windows }

Aloita avaamalla PowerShell ja suorita komento:

```bash
.\rclone.exe config
```

Tee vuorovaikutteisessa määritysprosessissa seuraavat valinnat:

1. Valitse **n** luodaksesi _New remote_
2. Nimeä etäkohde: **allas**
3. Tallennusprotokollien luettelosta valitse numero, joka vastaa:
_OpenStack Swift (Rackspace Cloud Files, Memset Memstore, OVH)_
4. Valitse todennusvaihtoehto **2**: _Get swift credentials from environment vars._
5. Tämän jälkeen hyväksy oletus (tyhjä) kaikissa jäljellä olevissa asetuksissa, kunnes palaat määritysprosessin aloitusvalikkoon. 
6. Lopuksi valitse **q** lopettaaksesi määrityksen.
 
Swiftin tapauksessa tämä määritys tarvitsee tehdä vain kerran. Määrityksessä on nyt määritelty, että _allas_-etäkohteen yhteystiedot luetaan ympäristömuuttujista.

Jos sinulla on pääsy Puhtiin, helpoin tapa tarkistaa tarvittavien muuttujien arvot on avata siihen terminaaliyhteys ja aktivoida siellä haluamasi Allas-projekti. Toinen vaihtoehto on käyttää apuohjelmaa [allas-get-swift-token-win.zip](https://github.com/CSCfi/allas-get-swift-token/releases/download/v1.0.0/allas-get-swift-token-win.zip). Jos valitset apuohjelman käytön, sinun (tai organisaatiosi IT-tuen) voi olla tarpeen säätää virustorjuntaa ym. ohjelmistoja sallimaan sen suoritus.

Jos käytät Puhtia Swift-käyttöoikeusmuuttujien asettamiseen, aktivoi Allas-ympäristö Puhtissa komennoilla:

```bash
module load allas
allas-conf --show-powershell
```

Kun määritys Puhtissa on valmis, kopioi tulosteen lopusta paikalliseen PowerShelliin rivit, jotka alkavat merkkijonolla `$Env:`, ja suorita ne. Kokeile sen jälkeen Rclone-yhteyttä komennolla:

```bash
  .\rclone.exe lsd allas:
```

Huomaa, että tässäkin tapauksessa yhteys toimii vain seuraavat 8 tuntia.

#### S3-yhteyden määrittäminen Windowsissa { #configuring-s3-connection-in-windows }

!!! Note
    Muista olla huolellinen ja turvallisuustietoinen määrittäessäsi S3-yhteyttä Allakseen. S3-avaimet tallennetaan luettavassa muodossa kotihakemistoosi, ja kuka tahansa, joka voi lukea avaimesi, pääsee Allakseen, kunnes avaimet perutaan nimenomaisesti Allaksesta. Pelkkä avainten poistaminen omalta koneeltasi ei riitä niiden mitätöimiseen.

Tarkista S3-avaimesi avaamalla yhteys Puhtiin (tai muuhun koneeseen, jossa `allas_conf` toimii). Jos S3-yhteys Allas-projektiisi ei ole vielä aktivoitu, aktivoi se komennoilla:

```
module load allas
allas-conf -m S3
```

Tämä luo paikallisen asetustiedoston, josta tarkistamme myöhemmin joitakin arvoja.

Vaihda sitten Windowsin _Command Promptiin_ ja käynnistä Rclonen määritysprosessi komennolla:

```bash
rclone config
```

Tee seuraavat valinnat:

   1. Valitse **n** luodaksesi _New remote_
   2. Nimeä etäkohde: **s3allas**
   3. Valitse tallennusprotokollien listasta numero, joka vastaa: _Amazon S3 Compliant Storage Providers including AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, and Tencent COS_
   4. Seuraavaksi sinulta kysytään S3-palveluntarjoaja. Valitse vaihtoehto _Any other S3 compatible provider_
   5. Valitse, että _Enter AWS credentials in the next step_ 
   6. Anna _AWS access key_. Voit tarkistaa tämän Puhtissa komennolla: 
   `grep access_key $HOME/.s3cfg  | cut -d " " -f3`
   7. Anna _AWS secret access key_. Voit tarkistaa tämän Puhtissa komennolla: 
   `grep secret_key $HOME/.s3cfg  | cut -d " " -f3`
   8. Region: **1**
   9. Endpoint: **a3s.fi**
   10. Location constant: (tyhjä, paina vain Enter)
   11. acl: **1**
   12. Edit advanced config: **n**
   13. Remote config: **y** (kyllä, tämä on ok)
   14. **q**, poistu määrityksestä
 
Tämän jälkeen pääset Allas-projektiisi Rclonen etäkohteella _s3allas_. Esimerkiksi:

```bash
rclone.exe lsd s3allas:
```

Tämä yhteys pysyy aktiivisena kannettavallasi, kunnes poistat sen.