# Tiedostojen jakaminen ja siirtäminen Funet FileSenderilla {#sharing-and-transporting-files-using-funet-filesender}

Funet FileSender on selaimella käytettävä palvelu, jonka avulla voit lähettää suuria tiedostoja kollegoillesi. Sitä tarjotaan vaihtoehtona sähköpostin liitetiedostoille, mutta sitä voidaan myös käyttää tiedostojen siirtämiseen CSC-ympäristöön. Palvelun avulla voit ladata ja lähettää tiedostoja, joiden koko on enintään 300 GB. Palvelu **ei** ole tarkoitettu pitkäaikaiseen säilytykseen, sillä tiedostot poistetaan automaattisesti säilytysajan umpeuduttua. Suurin säilytysaika on 21 päivää.

Funet FileSender on käytettävissä kaikille Haka-tunnistetuille organisaatioille ilman lisätoimia. Esimerkiksi CSC:n käyttäjätunnusta ei tarvita palvelun käyttöön. Sekä lähettäminen että vastaanottaminen onnistuvat ilman lisäohjelmien asentamista.

Voit käyttää Funet FileSenderia jakamaan tiedostojasi kenelle tahansa. Vastaanottajan ei tarvitse tunnistautua ladatakseen tiedoston FileSenderistä. Jos et kuulu Hakaan, tarvitset kollegan, joka voi lähettää sinulle _lähetysluvan_ (upload voucher). Lähetyslupa on kertaluonteinen oikeus käyttää palvelua tiedoston lähettämiseen.

## Tietojen lataaminen FileSenderiin {#uploading-data-to-filesender}

Kirjaudu ensin [palveluun selaimellasi](https://filesender.funet.fi). Sinun tulee kirjautua järjestelmään Haka-tunnuksillasi; valitse ensin kotiorganisaatiosi ja käytä oppilaitoksesi käyttäjätunnusta ja salasanaa (ei CSC:n käyttäjätunnusta ja salasanaa).

Tämän jälkeen voit määrittää vastaanottajan sähköpostiosoitteen, tai vaihtoehtoisesti saat jaettavan linkin. Valitse lähetettävät tiedostot _Valitse tiedostot_ (Select files) -painikkeella. Kun tilapäinen säilytysaika on määritelty (_Vanhenee_: Expiry date:) ja käyttöehdot on hyväksytty, paina _Lähetä_ (Send) -painiketta siirtääksesi tiedostot. Kun tiedostot on ladattu, vastaanottaja saa sähköposti-ilmoituksen.

Voit hallinnoida tiedostojasi niiden odottaessa noutoa. Tee tämä napsauttamalla _Omat siirrot_ (My Transfers) -painiketta.

![Funet FileSenderin lähetyssivu](/img/funet_upload.png 'Funet FileSender upload page')

!!! Huomio
    Koska tietoja ladataan Funet FileSenderiin verkkoselaimella, sen käyttö voi olla haastavaa CSC:n supertietokoneilla sijaitseviin aineistoihin. Tällöin voit käyttää vaihtoehtoisesti
    [Allasin komentoja](../Allas/using_allas/a_commands.md) `a-flip` tai
    `a-publish` tietojen jakamiseen. Yksi vaihtoehto on myös
    [käyttää FileSenderin komentoriviasiakasta](#using-filesender-from-the-command-line).

## Tietojen lataaminen FileSenderistä {#download-data-from-filesender}

Vastaanottaja saa sähköpostin, joka sisältää lataussivun URL-osoitteen lähetyille tiedostoille. Jaettava linkki osoittaa myös lataussivulle. Voit aloittaa latauksen painamalla _Lataa_ (Download) -painiketta.

![Funet FileSenderin lataussivu](/img/funet_download.png)

Voit myös napsauttaa oikealla latauspainiketta ja valita _Kopioi linkki_ (Copy Link) saadaksesi tiedoston lataus-URL:n. Tämän jälkeen URL:ia voi käyttää tiedoston lataamiseen toisella työkalulla, esimerkiksi [`wget`](wget.md):

```bash
wget "https://filesender.funet.fi/download.php?token=4da0-b98e-3290c6471469&files_ids=36805" -O data_from_FS
```

!!! note "Huomio"
    Kun lataat tietoja Funet FileSenderistä `wget`-ohjelmalla, sinun tulee ympäröidä latauslinkki lainausmerkeillä ja käyttää `-O`-valitsinta määritelläksesi nimi ladattavalle tiedostolle.

## FileSenderin käyttäminen komentoriviltä {#using-filesender-from-the-command-line}

FileSenderia voi käyttää myös komentoriviltä Python 3 -aputyökalun avulla.

Oletetaan, että olet Linux-palvelimella (esim. Puhti tai Mahti):

1. Lataa `filesender.py` Python-työkalu:

    ```bash
    wget https://raw.githubusercontent.com/filesender/filesender/refs/heads/development/scripts/client/filesender.py
    ```

2. Luo uusi kansio `~/.filesender` kotihakemistoosi:

    ```bash
    mkdir -p ~/.filesender
    ```

3. Luo `~/.filesender/filesender.py.ini` -asiakaskonfiguraatiotiedosto seuraavasti (voit lyhentää säilytysaikaa tarvittaessa):

    ```ini
    [system]
    base_url = https://filesender.funet.fi/rest.php
    default_transfer_days_valid = 7

    [user]
    username = <your username>
    apikey = <api secret>
    ```

    Käyttäjätunnuksesi (_Identifiant_) ja API-avaimesi (_Secret_) löytyvät/generoidaan
    _Oma profiili_ (My profile) -sivulla
    [Funet FileSender -verkkosivustolla](https://filesender.funet.fi/) (vaatii ensin sisäänkirjautumisen). Käsittele API-avainta kuten salasanaa – pidä se salassa! Huomaa, että tässä tapauksessa käyttäjätunnus **ei** ole sama kuin CSC-tunnuksesi.

4. Nyt voit lähettää tiedoston (esim. `data.tgz`) vastaanottajalle (esim.
   `recipient@example.com`) seuraavalla tavalla:

    ```bash
    python3 filesender.py -r recipient@example.com ./data.tar.gz
    ```