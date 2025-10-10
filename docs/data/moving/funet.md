# Tiedostojen jakaminen ja siirtäminen Funet FileSenderin avulla { #sharing-and-transporting-files-using-funet-filesender }

Funet FileSender on selainpohjainen palvelu suurten tiedostojen lähettämiseen
kollegoille. Se on vaihtoehto sähköpostin liitetiedostoille, mutta sitä voidaan
käyttää myös tiedostojen siirtämiseen CSC-ympäristöön. Palvelun avulla voit
lähettää jopa 300 Gt:n kokoisia tiedostoja. Palvelu ei ole tarkoitettu
pitkäaikaiseen säilytykseen, sillä tiedostot poistetaan automaattisesti, kun
säilytysaika ylittyy. Suurin sallittu säilytysaika on 21 päivää.

Funet FileSender on käytettävissä kaikille Haka-yhteentoimivuuden
mahdollistaville organisaatioille ilman lisätoimia. Esimerkiksi
CSC-käyttäjätiliä ei tarvita palvelun käyttöön. Sekä lähetys että vastaanotto
onnistuvat ilman lisäohjelmien asennusta.

Voit jakaa Funet FileSenderilla tiedostosi kenelle tahansa. Vastaanottaja ei
tarvitse tunnistautumista ladatakseen tiedoston FileSenderista. Jos et kuulu
Haka-järjestelmään, tarvitset kollegan, joka voi lähettää sinulle
_upload voucherin_. Voucher on kertaluonteinen lupa käyttää palvelua
tiedoston lähettämiseen.

## Tietojen lähettäminen FileSenderiin { #uploading-data-to-filesender }

Ensin [kirjaudu palveluun selaimellasi](https://filesender.funet.fi).
Kirjaudu järjestelmään Haka-tunnuksillasi; valitse ensin kotiorganisaatiosi ja
kirjaudu sisään organisaatiosi käyttäjätunnuksella ja salasanalla (ei CSC:n
käyttäjätunnuksella ja salasanalla).

Tämän jälkeen voit määrittää vastaanottajan sähköpostiosoitteen tai
vaihtoehtoisesti hankkia jaettavan linkin. Käytä painiketta _Select files_
valitaksesi lähetettävät tiedostot. Kun väliaikainen säilytysaika on määritetty
(_Expiry date:_) ja käyttöehdot on hyväksytty, paina _Send_-painiketta
siirtääksesi tiedostot. Kun tiedostot on lähetetty, vastaanottaja saa
sähköposti-ilmoituksen.

Voit hallinnoida tiedostojasi niiden odottaessa noutoa. Napsauta tätä varten
painiketta _My Transfers_.

![Funet FileSenderin lähetyssivu](/img/funet_upload.png 'Funet FileSenderin lähetyssivu')

!!! Note
    Koska dataa siirretään Funet FileSenderiin verkkoselaimen kautta, CSC:n
    supertietokoneilla sijaitsevan datan käyttäminen voi olla hankalaa. Tällöin
    voit vaihtoehtoisesti käyttää
    [Allas-komentoja](../Allas/using_allas/a_commands.md) `a-flip` tai
    `a-publish` datan jakamiseen. Vielä yksi vaihtoehto on
    [käyttää FileSenderin komentorivityökalua](#using-filesender-from-the-command-line).

## Tietojen lataaminen FileSenderista { #download-data-from-filesender }

Vastaanottaja saa sähköpostin, joka sisältää URL-osoitteen lähetettyjen
tiedostojen lataussivulle. Jaettava linkki osoittaa myös lataussivulle. Voit
aloittaa latauksen painamalla _Download_-painiketta.

![Funet FileSenderin lataussivu](/img/funet_download.png)

Voit myös napsauttaa _Download_-painiketta hiiren oikealla ja valita
_Copy Link_ saadaksesi tiedoston lataus-URL-osoitteen. URL-osoitetta voidaan
sen jälkeen käyttää tiedoston lataamiseen toisella työkalulla, esimerkiksi
[`wget`](wget.md):

```bash
wget "https://filesender.funet.fi/download.php?token=4da0-b98e-3290c6471469&files_ids=36805" -O data_from_FS
```

!!! note "Huom."
    1. Kun lataat dataa Funet FileSenderista komennolla `wget`, sinun on
       ympäröitävä latauslinkki lainausmerkeillä ja käytettävä valintaa `-O`
       määritelläksesi tiedostonimen, jota käytetään ladattavalle datalle.
    2. `wget`-menetelmä toimii vain yksittäisiä tiedostoja ladattaessa.
       _Download as single (.zip/.tar) file_ -painikkeen URL-osoitteen
       kopioiminen ja käyttäminen useiden tiedostojen lataamiseen kerralla
       arkistona ei valitettavasti toimi.

## FileSenderin käyttäminen komentoriviltä { #using-filesender-from-the-command-line }

FileSenderia voidaan käyttää myös komentoriviltä Python 3
-apuohjelmaskriptillä.

Oletetaan, että olet Linux-palvelimella (esim. Puhti tai Mahti):

1. Lataa `filesender.py`-Python-työkalu:

    ```bash
    wget https://raw.githubusercontent.com/filesender/filesender/refs/heads/development/scripts/client/filesender.py
    ```

2. Luo kotihakemistoosi uusi kansio `~/.filesender`:

    ```bash
    mkdir -p ~/.filesender
    ```

3. Luo `~/.filesender/filesender.py.ini`-asiakaskonfiguraatiotiedosto
   seuraavasti (pienennä säilytysaikaa tarpeen mukaan):

    ```ini
    [system]
    base_url = https://filesender.funet.fi/rest.php
    default_transfer_days_valid = 7

    [user]
    username = <your username>
    apikey = <api secret>
    ```

    Käyttäjätunnuksesi (_Identifiant_) ja API-avain (_Secret_) löytyvät/voidaan
    luoda sivulta _My profile_ [Funet FileSenderin verkkosivustolla](https://filesender.funet.fi/)
    (vaatii kirjautumisen ensin). Kohtele API-avainta kuten mitä tahansa
    salasanaa – pidä se salassa! Huomaa, että käyttäjätunnus tässä tapauksessa
    **ei** ole sama kuin CSC-tilisi käyttäjätunnus.

4. Nyt voit lähettää tiedoston (esim. `data.tgz`) vastaanottajalle (esim.
   `recipient@example.com`) komennolla:

    ```bash
    python3 filesender.py -r recipient@example.com ./data.tar.gz
    ```