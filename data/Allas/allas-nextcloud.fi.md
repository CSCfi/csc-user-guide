# Nextcloudin käyttäminen Allas-tallennusjärjestelmän käyttöliittymänä {#using-nextcloud-as-front-end-for-allas-storage-system}

Motivaatio: Allas on yleiskäyttöinen tutkimusdatan tallennusjärjestelmä. 
Sitä voidaan käyttää Swift- ja S3-protokolliin pohjautuvilla työkaluilla. Kuitenkin monissa tapauksissa 
Allaksen suora käyttö S3:n tai Swiftin kautta on rajallista käyttäjähallinnan yksinkertaisen rakenteen vuoksi 
sekä siksi, että pääsy perustuu henkilökohtaisiin CSC-käyttäjätunnuksiin.

Nextcloud-palvelimen käyttäminen käyttöliittymänä mahdollistaa oman käyttäjäkunnan luomisen ja hallinnan 
Allas-tallennusalueellesi ja pääsyn hallinnan eri tietoaineistoihin ja tallennusalueisiin. 
Lisäksi Nextcloud tarjoaa useita käyttöliittymiä (mukaan lukien WWW-käyttöliittymä ja mobiilisovellus), 
jotka ovat usein helppokäyttöisempiä ja joustavampia kuin Swift- tai S3-sovellukset.

Tässä dokumentissa esitetään yksinkertainen käyttötapaus seuraavilla vaiheilla:

   1. Käynnistä uusi Ubuntu18-virtuaalikone
   2. Asenna Nextcloud-palvelin uuteen VM:ään
   3. Linkitä Nextcloud-palvelin Allaksen tietosäiliöön
   4. Luo uusi Nextcloud-käyttäjätunnus ulkoiselle käyttäjälle

## 1. Käynnistä uusi Ubuntu-virtuaalikone {#1-launch-a-new-ubuntu-virtual-machine}

Käynnistä ensin uusi Ubuntu-pohjainen palvelin cPouta-palvelussa. Tämä ohje on testattu **Ubuntu18**- ja **Ubuntu24**-järjestelmissä.  
Katso ohjeet [cPouta-dokumentaatiosta](../../cloud/pouta/index.md) sekä
[tutoriaalivideosta](https://www.youtube.com/watch?v=CvoN4pv0RJQ).

Useimmissa tapauksissa “standard small” -kokoluokan ja **Ubuntu18** tai **Ubuntu24** -kuvan yhdistelmä riittää.

Kun luot VM:lle tietoturvaryhmän, yllä oleva ohje kertoo, miten 
portti 22 avataan ssh-yhteyttä varten. Tässä tapauksessa käytä samaa menettelyä avataksesi 
myös portti 443 (https), sillä sitä tarvitaan Nextcloud-palvelimen käyttöön.

## 2. Nextcloud-palvelimen asentaminen virtuaalikoneeseen {#2-setting-up-a-next-cloud-sever-in-the-vm}

Avaa terminaaliyhteys palvelimelle (ssh tai Putty) Nextcloud-palvelimen asennusta varten.
Ensiksi Ubuntu-järjestelmä kannattaa päivittää:

```bash
sudo apt-get update
```
Tässä esimerkissä käytämme _snap_:ia, joka tarjoaa helpon tavan asentaa Nextcloudin.
Voit tehdä asennukset vain muutamalla komennolla.

Tee ensin nextcloudin asennus komennolla:
```bash
sudo snap install nextcloud
```
Tämän jälkeen luodaan Nextcloudin ylläpitotunnus. Alla olevassa komennossa tilinimeksi 
asetetaan _ncadmin_ ja salasanaksi _1Hu9kgFsN_.
```bash
sudo nextcloud.manual-install ncadmin 1Hu9kgFsN
```
Seuraavaksi tulee ottaa käyttöön https itse allekirjoitetulla varmenteella. Itse allekirjoitetut varmenteet riittävät testaukseen, mutta 
tuotantokäyttöä varten kannattaa käyttää oikeita varmenteita (esim. lets-encrypt itse allekirjoitetun sijasta).
```bash
sudo nextcloud.enable-https self-signed
```

Viimeisenä vaiheena lisää Nextcloud-palvelimesi IP-osoite hyväksyttyjen domainien listaan. IP-osoite on VM:lle määritetty kelluva IP, 
jota käytit myös terminaaliyhteyden avaamiseen. 
Esimerkiksi jos IP on 86.50.252.77, määrityskomento on:
```bash
sudo nextcloud.occ config:system:set trusted_domains 1 --value=86.50.252.77
```

Nyt sinun pitäisi pystyä yhdistämään Nextcloud-palvelimeesi osoitteessa _https://ip-of-your-VM_

Eli tässä esimerkissä: _https://86.50.252.77_

Jos selainyhteys ei toimi, tarkista että:

*   käytät oikeaa protokollaa ja IP-osoitetta
*   portti 443 ja oma (paikallinen) IP-osoitteesi (ei palvelimen IP) on määritelty cPoutan tietoturvaryhmään ja että ryhmä on käytössä
*   selain hyväksyy itse allekirjoitetut varmenteet
 

Nextcloud-ohjelmisto on modulaarinen ja sitä voidaan laajentaa Nextcloud-sovelluksilla (Apps). Kun 
Nextcloud on asennettu ja käynnissä, on hyvä tarkistaa mitkä sovellukset ovat päällä ja miten 
erilaiset ominaisuudet on määritelty. Voit tehdä tämän Nextcloudin käyttöliittymässä admin-tunnuksella kirjautuneena. 
Halutessasi voit myös ajaa CSC:n tarjoaman skriptin, joka poistaa joitain sekä määrittelee sovelluksia, 
jotta Nextcloud ei tulisi ylikuormitetuksi ominaisuuksista tässä Allas-käyttötapauksessa. Skriptin voi ladata ja ajaa näin:

```bash
curl https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/nextcloud_snap/clean_nextcloud_snap >clean_nextcloud_snap
chmod +x clean_nextcloud_snap
./clean_nextcloud_snap
```

## 3. Nextcloudin liittäminen Allas-säiliöön {#3-link-nextcloud-to-a-bucket-in-allas}

Jotta voit liittää Allaksen Nextcloud-palvelimeen, sinulla täytyy olla voimassa oleva S3-avaipari ja valmiiksi luotu tietosäiliö (bucket) Allaksessa. Säiliö voi olla tyhjä tai se voi sisältää dataobjekteja.

Nämä toimet voit tehdä esimerkiksi puhti.csc.fi-palvelussa seuraavilla komennoilla:

### a. Yhteyden määrittely:

```bash
module load allas
allas-conf --mode s3cmd
```

### b. Uuden tyhjän säiliön luonti

```bash
s3cmd mb s3://your-proj-num-nextcloud
```
Tässä esimerkissä käytämme projektia 2001234, joten 
säiliön nimi voisi olla:

```text
2001234-nextcloud
```

### c. Avainten tulostaminen

```bash
grep key $HOME/.s3cfg
```
!!! note "S3 Allas -tunnukset"
    Voit myös hakea Allaksen S3-tunnukset tämän [ohjeen](../../support/faq/how-to-get-Allas-s3-credentials.md) avulla.

Siirry nyt Nextcloudin WWW-käyttöliittymään ja kirjaudu admin-käyttäjänä. 
Klikkaa sinistä valikkorivin oikeasta reunasta ympyräsymbolia ja valitse _+Apps_ avautuvasta valikosta.

Siirry kohtaan _Omat sovellukset_ ja ota käyttöön listalta _External storage support_.

Klikkaa sitten uudelleen ympyräkuvaketta ja avaa _Administration settings_.

Asetuspaneelista vasemmalta selaa kohtaan Administration ja valitse: _External storage_.

Avaa _Add storage_ -valikko ja valitse: _Amazon S3_

Aukeavaan määrityslomakkeeseen täytä seuraavat tiedot: 

*   Kansion nimi: Näyttönimi Allas-säiliölle (2001234-nextcloud)
*   Tunnistautuminen: Valitse _Access key_
*   Bucket: Äsken luomasi (tai joku aiempi) säiliö.
*   Hostname: a3s.fi
*   Portti: 443
*   Alue: US
*   Enable SSL
*   Access key: yllä olevan grep-komennon tulos
*   Secret key: yllä olevan grep-komennon tulos

Siirry tämän jälkeen _External storage_ -kohtaan henkilökohtaisissa asetuksissa ja klikkaa juuri luodun ulkoisen kansion riviä varmistaaksesi, että tallennus toimii.

Jos nyt siirryt _Files_-työkaluun päävalikossa (sininen yläpalkki), 
sinun pitäisi nähdä uusi ulkoinen tallennuskansio nimellä, jonka annoit edellä.

Nyt voit klikata kansiota ja alkaa ladata dataa Allas-säiliöön ja sieltä 
Nextcloud-käyttöliittymän kautta.

## 4. Uuden Nextcloud-käyttäjätunnuksen luonti ulkoiselle käyttäjälle {#4-create-new-nextcloud-user-account-for-an-external-user}

Nextcloudin ylläpitotunnuksella voidaan luoda uusia käyttäjiä ja käyttäjäryhmiä palvelimelle. 
Klikkaa sinisen valikkorivin oikeasta reunasta ympyräsymbolia ja valitse _Users_ avautuvasta valikosta.

Luo ensin uusi käyttäjäryhmä klikkaamalla _+_-merkkiä _Groups_-kohdan vieressä. Tässä annamme ryhmän nimeksi “users” 
ja vahvistamme luonnin kirjoittamalla Nextcloudin adminin salasanan.

Sen jälkeen luodaan uusi käyttäjä klikkaamalla _New account_.
Käyttäjänimi ja salasana määritetään ja uusi tili lisätään _Users_-ryhmään.

Lopuksi tulee sallia uudelle käyttäjälle pääsy _External storage_:en (Allaksen säiliö). 
Tee tämä palaamalla asetuksiin ja avaamalla _External storage_ -asetukset hallintatyökaluista.

Nyt “Available for” -sarakkeesta klikkaa määrityskenttää. Tämä näyttää käyttäjät ja käyttäjäryhmät. 
Valitse käyttäjä tai käyttäjäryhmä, jolle haluat sallia pääsyn Allas-säiliöön. Voit määritellä sekä luku- että kirjoitusoikeudet 
tai antaa vain lukuoikeuden käyttäjälle tai ryhmälle. Nämä vaihtoehdot löytyvät kolmen pisteen valikosta määrityskentän vierestä.

## 5. Nextcloudin käyttäminen {#5-using-nextcloud}

Kun uusi Nextcloud-tili on luotu, voit lähettää tilin tiedot uudelle käyttäjälle ja hän 
voi käyttää Nextcloudia tiedostojen lähettämiseen ja lataamiseen siihen säiliöön, 
joka liitettiin Nextcloud-palvelimeen. Huomaa, että tämän käyttäjän ei tarvitse omistaa CSC-tunnusta, 
Nextcloud-tili riittää. Selainkäyttöliittymien lisäksi Nextcloudia voi käyttää myös [työpöytäohjelmilla](https://nextcloud.com/install/) ja [puhelinsovelluksilla](https://apps.nextcloud.com/). 

Komentorivityöskentely on myös mahdollista. Tämä on hyödyllistä esimerkiksi silloin, kun datan lataus tai lähetys täytyy automatisoida. Alla on esimerkki datan lähettämisestä ja lataamisesta `curl`-komennolla ja _sovellussalasanalla_. Tässä tapauksessa Nextcloudin ylläpitäjä on luonut käyttäjän _ncuser1_ tätä varten. Käyttäjä _ncuser1_ kirjautuu ensin nextcloud-palvelimelle. Käyttäjä avaa *Settings*-valikon ja siirtyy *Security*-asetuksiin.

Turvallisuusosiossa *Devices & Sessions* luodaan sovellukselle salasana painamalla *Create a new app password* -painiketta. Huomaa, että sinun täytyy kopioida ja tallentaa luotu salasana heti, sillä sitä ei enää näytetä myöhemmin.

Käyttäjätunnuksen ja sovellussalasanan lisäksi käyttäjän täytyy tietää palvelimen IP-osoite tai nimi, jotta palveluun voidaan yhdistää. 
Tällä tiedolla dataa voidaan ladata Nextcloudista curl-komennolla näin:
```bash
curl -k -u username:app-password "https://server-ip/remote.php/webdav/nextcloudirectiory/file-name"
```

Ja lataaminen palveluun onnistuu näin:
```bash
curl -k -u username:app-password -T file-to-upload "https://server-ip/remote.php/webdav/nextcloudirectory/file-name"
```

Yllä olevissa komennoissa `-k`-optio tarvitaan, kun Nextcloud käyttää itse allekirjoitettuja varmenteita.

Tässä esimerkissä käyttäjän _ncuser1_ generoima sovellussalasana on: _Q34EN-Ni7pH-9oSes-ZQsF7-NdkYi_
ja Nextcloud-palvelimen IP-osoite on 123.456.768.910. Aiemmin Nextcloudin ylläpitäjä liitti Allaksen säiliön _2001234-nextcloud_ 
palveluun.

Nyt _ncuser1_ voi ladata tiedoston _image1.jpg_ Allaksen säiliöön _2001234-nextcloud_ komennolla:

```bash
curl -k -u ncuser1:Q34EN-Ni7pH-9oSes-ZQsF7-NdkYi -T ./image1.jpg "https://123.456.768.910/remote.php/webdav/2001234-nextcloud/image1.jpg"
```

Saman tiedoston voi ladata takaisin komennolla:

```bash
curl -k -u ncuser1:Q34EN-Ni7pH-9oSes-ZQsF7-NdkYi "https://123.456.768.910/remote.php/webdav/2001234-nextcloud/image1.jpg" > image1.jpg
```