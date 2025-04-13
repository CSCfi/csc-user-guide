
# Nextcloudin käyttö Allas-tallennusjärjestelmän edustana {#using-nextcloud-as-front-end-for-allas-storage-system}

Motivaatio: Allas on yleiskäyttöinen tallennusjärjestelmä tutkimusdatalle. 
Sitä voidaan käyttää workenteilla perustuen Swift- ja S3-protokolliin. Monissa tapauksissa suora Allas-käyttö S3- tai Swift-protokollia käyttäen on 
kuitenkin rajoitettua käyttäjähallinnan yksinkertaisen rakenteen ja sen vuoksi, että pääsy perustuu henkilökohtaisiin CSC-käyttäjätileihin.

Nextcloud-palvelimen käyttäminen edustana mahdollistaa oman käyttäjäkannan luomisen ja hallinnan Allas-tietovarastoalueellesi 
sekä pääsyn hallinnan eri datakokonaisuuksiin ja tallennusalueisiin. Lisäksi Nextcloud tarjoaa useita käyttöliittymiä 
(mukaan lukien WWW-käyttöliittymä ja matkapuhelinsovellus), jotka ovat usein helpompia ja joustavampia käyttää kuin alkuperäiset Swift- tai S3-sovellukset.

Tässä dokumentissa näytämme yksinkertaisen käyttötilanteen seuraavin vaihein:

1. Käynnistä uusi Ubuntu18 Virtuaalikone
2. Asenna Nextcloud-palvelin uuteen VM:ään
3. Yhdistä Nextcloud-palvelin Allas-data-ämpäriin
4. Luo uusi Nextcloud-käyttäjätili ulkopuoliselle käyttäjälle

## 1. Käynnistä uusi Ubuntu Virtuaalikone {#launch-a-new-ubuntu-virtual-machine}

Ensiksi, käynnistä uusi Ubuntu-pohjainen palvelin cPouta-palvelussa. Tämä opetusohjelma on testattu **Ubuntu18** ja **Ubuntu24** käyttöjärjestelmillä.  
Katso ohjeet [cPouta-dokumentaatiosta](../../cloud/pouta/index.md) ja
[tutustustumisvideosta](https://www.youtube.com/watch?v=CvoN4pv0RJQ).

Useimmissa tapauksissa "standard small" flavor- ja **Ubuntu18** tai **Ubuntu24** -kuvakombinaatio on riittävä.

Kun luot VM:lle suojausryhmää, yllä olevat ohjeet näyttävät, kuinka portti 22 avataan ssh-yhteydelle. Tässä tapauksessa, käytä samaa menettelyä 
avataaksesi myös portti 443 (https), sillä sitä käytetään Nextcloud-palvelimen käyttämiseen.

## 2. Next Cloud -palvelimen asentaminen virtuaalikoneeseen {#setting-up-a-next-cloud-sever-in-the-vm}

Avaa päätelaitteen yhteys palvelimeesi (ssh tai Putty) Nextcloud-palvelimen asentamiseksi.
Ensiksi, on hyvä päivittää Ubuntu-järjestelmä:

```bash
sudo apt-get update
```

Tässä esimerkissä käytämme _snap_:ia, sillä se tarjoaa helpon tavan asentaa Nextcloud.
Voit suorittaa asennukset vain muutamalla komennolla.

Suorita ensin next-cloud-asennus komennolla:
```bash
sudo snap install nextcloud
```

Sitten Nextcloud-hallintotili luodaan. Alla olevassa komennossa tilin nimeksi
on määritetty _ncadmin_ ja salasana _1Hu9kgFsN_.
```bash
sudo nextcloud.manual-install ncadmin 1Hu9kgFsN
```

Seuraavaksi sinun on otettava käyttöön https itse allekirjoitetulla varmenteella. Itse allekirjoitetut varmenteet riittävät
testaukseen, mutta tuotantoon sinun tulisi käyttää oikeita varmenteita (esim. lets-encrypt itse allekirjoitetun sijaan).
```bash
sudo nextcloud.enable-https self-signed
```

Lisäksi lisää Nextcloud-palvelimesi IP-osoite luotettujen verkkotunnusten listaan. IP-osoite on Kelluva IP 
osoite, jonka annoit VM:lle ja jota käytit avaamaan päätelaitteen yhteyden.
Esimerkiksi IP:86.50.252.77 tapauksessa määrittely olisi mahdollista komennolla:
```bash
sudo nextcloud.occ config:system:set trusted_domains 1 --value=86.50.252.77
```

Nyt sinun pitäisi pystyä liittymään Nextcloud-palvelimeeseesi, joka toimii _https://ip-of-your-VM_

Tässä esimerkissä: _https://86.50.252.77_

Jos yhteyden verkkoliittymä epäonnistuu, tarkista että:

* käytät oikeaa protokollaa ja ip-osoitetta
* portti 443 ja paikallinen IP-osoitteesi (ei palvelimen IP) on määritelty cPouta-suojausryhmässä ja että tämä suojausryhmä on käytössä
* selaimesi hyväksyy itse allekirjoitetut varmenteet

Nextcloud-ohjelmisto on modulaarinen, sitä voidaan laajentaa Nextcloud-sovelluksilla. Kun olet saanut
Nextcloudin toimimaan, on hyvä käytäntö tarkastaa, mitkä sovellukset ovat käytössä ja miten
erilaisia ominaisuuksia on määritelty toimimaan. Tämä voidaan tehdä Nextcloudin käyttäjäliittymässä
kirjautumalla sisään adminina. Voit halutessasi myös aloittaa tämän suorittamalla CSC:n
tarjoaman skriptin, joka poistaa käytöstä joitain ja konfiguroi joitain sovelluksia, jotta 
Nextcloud-vähemmän kuormittunut testeissä Allas-edustana. Skripti voidaan 
ladata ja suorittaa näin:

```bash
curl https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/nextcloud_snap/clean_nextcloud_snap >clean_nextcloud_snap
chmod +x clean_nextcloud_snap
./clean_nextcloud_snap
```

## 3. Yhdistä Nextcloud ämpäriin Allasissa {#link-nextcloud-to-a-bucket-in-allas}

Jotta voit yhdistää Allas Nextcloud-palvelimeen, sinulla on oltava voimassa oleva S3-avainpari ja valmiiksi tehty data-ämpäri Allasissa. Ämpäri voi olla tyhjä tai se voi jo sisältää joitain dataobjekteja.

Voit tehdä tämän esimerkiksi puhti.csc.fi komentoilla:

### a. Yhteyden muodostaminen:

```bash
module load allas
allas-conf --mode s3cmd
```

### b. Uuden tyhjän ämpärin luominen

```bash
s3cmd mb s3://your-proj-num-nextcloud
```

Tässä esimerkissä käytämme projektia 2001234, joten
ämpärin nimi voisi olla:

```text
2001234-nextcloud
```

### c. Avainten tulostaminen

```bash
grep key $HOME/.s3cfg
```
!!! note "S3 Allas Credentiaalit"
    Voit myös luoda Allas S3 -tunnisteita seuraamalla tätä [ohjetta](../../support/faq/how-to-get-Allas-s3-credentials.md)

Palaa nyt Nextcloud WWW-käyttöliittymään ja kirjaudu sisään adminina. 
Klikkaa pyöreää symbolia sinisen valikkopalkin oikeassa päässä ja valitse 
_+Sovellukset_ avattavasta valikosta.

Siirry kohtaan _Sovelluksesi_ ja sieltä ilmestyvästä sovelluslistasta aktivoi _Ulkoinen tallennustuki_. 

Klikkaa sitten jälleen pyöreää symbolia ja avaa _Hallinta-asetukset_.

Asetuspaneelin vasemmalla puolella, vieritä Hallinta-osioon ja valitse: _Ulkoinen tallennus_.

Avaa _Lisää tallennustila_ valikko ja valitse: _Amazon S3_

Tämä avaa määrittelyvalikon, jossa sinun täytyy täyttää seuraavat parametrit:

*   Kansion nimi: näytettävä nimi allas-ämpärille (2001234-nextcloud)
*   Tunnistautuminen: Valitse _Pääsyavain_
*   Ämpäri: Ämpäri jonka juuri loit tai jokin vanhempi ämpäri.
*   Isäntänimi:a3s.fi
*   Portti: 443
*   Alue: US
*   Ota SSL käyttöön
*   Access-avain: grep-komennon tulosteesta yllä
*   Salainen avain: grep-komennon tulosteesta yllä

Mene sitten _Ulkoinen tallennus_ omissa _Henkilökohtaisissa_ asetuksissasi ja klikkaa juuri luodun ulkoisen kansion nimeä varmistaaksesi, että tallennus toimii.

Jos siirryt nyt _Tiedostot_ työkaluun päävalikossa (sininen palkki ylhäällä), sinun pitäisi nähdä uusi ulkoinen tallennuskansio nimettynä edellä määritellyllä tavalla.

Nyt voit klikata tätä kansiota ja aloittaa datan lataamisen ja purkamisen tästä Allas-ämpäristä ja siihen Nextcloud-käyttöliittymällä.

## 4. Uuden Nextcloud-käyttäjätilin luominen ulkopuoliselle käyttäjälle {#create-new-nextcloud-user-account-for-an-external-user}

Nextcloud-admintili voi luoda uusia käyttäjiä ja käyttäjäryhmiä Nextcloud-palvelimeen. 
Klikkaa pyöreää symbolia sinisen valikkopalkin oikeassa päässä ja valitse _Käyttäjät_ avattavasta valikosta.

Ensiksi luomme uuden käyttäjäryhmän klikkaamalla _+_ merkkiä _Ryhmät_ vieressä. 
Tässä nimetämme ryhmän "users" ja vahvistamme luontipyynnön syöttämällä Nextcloud-adminin salasanan.

Sitten uusi käyttäjä luodaan klikkaamalla _Uusi tili_ 
Käyttäjän nimi ja salasana on määritettävä ja uusi tili lisätään ryhmään _Käyttäjät_.

Lopuksi meidän on sallittava tämän uuden käyttäjän pääsy _Ulkoinen tallennus_ (Allas-ämpäriin). 
Siirry siihen takaisin Asetusnäkymään ja toista _Ulkoinen tallennus_ asetusten avaaminen 
Hallinta-työkaluista. 

Nyt “Käytettävissä” sarakkeessa, klikkaa määrittelykenttää. Tämä listaa käyttäjät ja käyttäjäryhmät. 
Valitse joko käyttäjä tai käyttäjäryhmä salliaksesi uuden käyttäjän pääsyn Allas-ämpäriin. 
Voit määrittää sekä luku- että kirjoitusluvat tai voit antaa vain 
lukua-oikeuden käyttäjälle tai käyttäjäryhmälle. Nämä asetukset tehdään kentän vieressä olevien kolmen pisteen avautuvasta valikosta.

## 5. Nextcloudin käyttö {#using-nextcloud}

Kun uusi nextcloud-tili on luotu, voit lähettää tilitiedot uudelle käyttäjälle ja hän voi käyttää Nextcloudia 
datan lataamiseen ja purkamiseen Nextcloud-palvelimeen liitetystä data-ämpäristä. Huomaa, että tämä 
käyttäjä ei tarvitse CSC-tiliä, Nextcloud-tili riittää. Lisäksi web-käyttöliittymiä, Nextcloudia voi käyttää [pöytäkoneohjelmilla](https://nextcloud.com/install/) ja [puhelinsovelluksilla](https://apps.nextcloud.com/).

Komentorivikäyttö on myös mahdollista. Tätä voidaan hyödyntää esimerkiksi, kun datan lataus tai purkaminen tarvitsee automatisoida. Alla on esimerkki, jossa dataa ladataan ja puretaan `curl`-komennolla ja 
_sovellussalasana_:lla. Tässä tapauksessa Nextcloud-admin on luonut käyttäjän nimeltä _ncuser1_ 
tätä tarkoitusta varten. Ensin _ncuser1_ kirjautuu nextcloud-palvelimeen. Käyttäjä avaa *Asetukset* valikon ja siirtyy siellä *Turvallisuus* asetuksiin.

Turvallisuusosiossa *Laitteet & Istunnot*, sovellussalasana luodaan klikkaamalla painiketta: *Luo uusi sovellussalasana*. Huomaa, että sinun on kopioitava ja tallennettava juuri luotu sovellussalasana, koska et voi tarkastella sitä myöhemmin.

Käyttäjänimen ja sovellussalasanan lisäksi käyttäjän on tiedettävä IP-osoite tai palvelimen nimi päästäkseen palveluun. 
Näillä tiedoilla data voidaan ladata Nextcloudista curl-komennon syntaksilla:
```bash
curl -k -u username:app-password "https://server-ip/remote.php/webdav/nextcloudirectory/file-name"
```

Ja lataus voidaan tehdä syntaksilla:
```bash
curl -k -u username:app-password -T file-to-upload "https://server-ip/remote.php/webdav/nextcloudirectory/file-name"
```

Komennossa yllä oleva `-k` vaihtoehto tarvitaan, kun Nextcloud-palvelin käyttää itse allekirjoitettuja varmenteita.

Tässä esimerkissä sovellussalasana, jonka käyttäjä _ncuser1_  loi, on: _Q34EN-Ni7pH-9oSes-ZQsF7-NdkYi_
ja Nextcloud-palvelimen IP-osoite on 123.456.768.910. Aiemmin Nextcloud-admin oli linkittänyt Allas-ämpärin _2001234-nextcloud_
Nextcloud-palveluun.

Nyt _ncuser1_ pystyy lataamaan tiedoston _image1.jpg_ Allas-ämpäriin _2001234-nextcloud_ komennolla:

```bash
curl -k -u ncuser1:Q34EN-Ni7pH-9oSes-ZQsF7-NdkYi -T ./image1.jpg "https://123.456.768.910/remote.php/webdav/2001234-nextcloud/image1.jpg"
```

Sama tiedosto voidaan ladata komennolla:

```bash
curl -k -u ncuser1:Q34EN-Ni7pH-9oSes-ZQsF7-NdkYi "https://123.456.768.910/remote.php/webdav/2001234-nextcloud/image1.jpg" > image1.jpg
```
