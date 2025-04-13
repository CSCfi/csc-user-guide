# Tiedostojen jakaminen ja siirtäminen Funet FileSenderilla {#sharing-and-transporting-files-using-funet-filesender}

Funet FileSender on selainpohjainen palvelu, jolla voi lähettää suuria tiedostoja kollegoille. Se tarjoaa vaihtoehdon sähköpostiliitteille, mutta sitä voi myös käyttää tiedostojen siirtämiseen CSC-ympäristöön. Palvelun avulla voit ladata ja lähettää tiedostoja, joiden koko on enintään 300 GB. Palvelua ei ole tarkoitettu pitkäaikaiseen säilytykseen, koska tiedostot poistetaan automaattisesti säilytysajan ylittyessä. Suurin sallittu säilytysaika on 21 päivää.

Funet FileSender on käytettävissä kaikille Haka-verkkoon kuuluville organisaatioille ilman lisätoimenpiteitä. Esimerkiksi CSC-käyttäjätiliä ei tarvita palvelun käyttöön. Sekä lähettäminen että vastaanottaminen on mahdollista ilman lisäohjelmien asennusta.

Voit käyttää Funet FileSenderia tiedostojesi jakamiseen kenelle tahansa. Vastaanottaja ei tarvitse tunnistautumista FileSenderista tiedoston lataamiseen. Jos et kuulu Haka-verkon piiriin, tarvitset kollegan, joka voi lähettää sinulle _upload voucherin_. Voucher on kertalupa palvelun käyttämiseen tiedoston lähettämiseksi.

## Tiedostojen lataaminen FileSenderiin {#uploading-data-to-filesender}

[Kirjaudu ensin sisään palveluun selaimellasi](https://filesender.funet.fi). Sinun tulee kirjautua järjestelmään Haka-tunnuksillasi; valitse ensin kotiorganisaatiosi ja käytä laitoksesi käyttäjätunnusta ja salasanaa (ei CSC:n käyttäjätunnusta ja salasanaa).

Tämän jälkeen voit määrittää vastaanottajan sähköpostiosoitteen tai vaihtoehtoisesti saada jaettavan linkin. Käytä _Select files_ -painiketta valitaksesi tiedostot, jotka haluat lähettää. Kun tilapäisen säilytysajan päivämäärä on asetettu (_Expiry date:_) ja käyttöehdot hyväksytty, paina _Send_ -painiketta ladataksesi tiedostot. Kun tiedostot on ladattu, vastaanottaja saa sähköposti-ilmoituksen.

On mahdollista hallita tiedostojasi niiden odottaessa noutoa. Klikkaa _My Transfers_ -painiketta tehdäksesi tämän.

![Funet FileSender lataussivu](/img/funet_upload.png 'Funet FileSender lataussivu')

!!! Huomio
    Koska data ladataan Funet FileSenderiin verkkoselaimen kautta, voi olla vaikeaa käyttää sitä CSC:n supertietokoneilla sijaitsevan datan siirtämiseen. Tässä tapauksessa voit vaihtoehtoisesti käyttää [Allas-käskyjä](../Allas/using_allas/a_commands.md) `a-flip` tai `a-publish` datan jakamiseen. Toinen vaihtoehto on [käyttää FileSender komentoriviltä](#using-filesender-from-the-command-line).

## Tiedostojen lataaminen FileSenderista {#download-data-from-filesender}

Vastaanottaja saa sähköpostin, joka sisältää URL-osoitteen ladattavien tiedostojen sivulle. Jaettava linkki ohjaa myös lataussivulle. Voit aloittaa lataamisen painamalla _Download_ -painiketta.

![Funet FileSender lataussivu](/img/funet_download.png)

Voit myös klikata hiiren oikealla painikkeella latauspainiketta ja valita _Copy Link_ saadaksesi lataus-URL:n tiedostoon. URL:ä voidaan sitten käyttää tiedoston lataamiseen toisella välineellä, esimerkiksi [`wget`](wget.md):

```bash
wget "https://filesender.funet.fi/download.php?token=4da0-b98e-3290c6471469&files_ids=36805" -O data_from_FS
```

!!! huomio "Huomio"
    Kun lataat tietoja Funet FileSenderista `wget`-komennolla, sinun täytyy sulkea latauslinkki lainausmerkkeihin ja käyttää `-O`-valitsinta määrittääksesi tiedostonimen, jota käytetään ladatun datan tallentamiseen.

## FileSenderin käyttäminen komentoriviltä {#using-filesender-from-the-command-line}

FileSenderia voi käyttää myös komentoriviltä Python 3 -apuohjelman avulla.

Oletetaan, että olet Linux-palvelimella (esim. Puhti tai Mahti):

1. Lataa `filesender.py` Python-työkalu:

    ```bash
    wget https://raw.githubusercontent.com/filesender/filesender/refs/heads/development/scripts/client/filesender.py
    ```

2. Luo uusi kansio `~/.filesender` kotihakemistoosi:

    ```bash
    mkdir -p ~/.filesender
    ```

3. Luo `~/.filesender/filesender.py.ini` asiakaskonfiguraatiotiedosto seuraavasti (pienennä säilytysaikaa tarvittaessa):

    ```ini
    [system]
    base_url = https://filesender.funet.fi/rest.php
    default_transfer_days_valid = 7

    [user]
    username = <your username>
    apikey = <api secret>
    ```

    Käyttäjätunnuksesi (_Identifiant_) ja API-avain (_Secret_) löytyvät/voidaan luoda [Funet FileSender -verkkosivun](https://filesender.funet.fi/) _My profile_ -sivulta (ensin täytyy kirjautua sisään). Käsittele API-avainta kuin mitä tahansa salasanaa – pidä se salassa! Huomaa, että käyttäjätunnus tässä tapauksessa ei ole samanhankintainen CSC:n käyttäjätunnuksen kanssa.

4. Nyt voit lähettää tiedoston (esim. `data.tgz`) vastaanottajalle (esim. `recipient@example.com`) seuraavasti:

    ```bash
    python3 filesender.py -r recipient@example.com ./data.tar.gz
    
