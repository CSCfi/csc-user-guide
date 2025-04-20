# Varmuuskopiopalvelin SD Desktopille {#backup-server-for-sd-desktop}

Turvallisuussyistä vain projektipäällikkö voi viedä tietoja SD Desktopista. Tämän vuoksi tavalliset SD Desktopin käyttäjät eivät voi tehdä varmuuskopioita SD Desktopissa olevista tiedoistaan. Tämä ohje esittelee `backup_server.sh`-prosessin ja `sd-backup`-komennon käytön, jotka mahdollistavat SD-käyttäjille datan varmuuskopioinnin SD Connectiin.

## Asennus {#installation}

Varmuuskopioprosessin työkalut eivät ole oletuksena asennettuna SD Desktop -virtuaalikoneisiin. Ensimmäinen vaihe on siis, että projektipäällikkö asentaa **SD Backup tool** -paketin käyttämällä [SD Software installeria](../../sensitive-data/sd-desktop-software.md#customisation-via-sd-software-installer).

Kirjaudu SD Desktopiin ja avaa **Data Gateway**. Jos ohjelmiston asennusaputyökalut ovat käytössä projektissasi, niin kansio `tools-for-sd-desktop` löytyy hakemistosta, jonka Data Gateway loi (polussa `Projects/SD-Connect/your-project-name`). Jos et löydä `tools-for-sd-desktop`-hakemistoa Data Gatewayn kautta, **lähetä pyyntö [CSC Service Deskille](../../../support/contact.md)**. Pyynnössä mainitse, että haluat SD Desktopin ohjelmiston asennusaputyökalut saataville projektiisi. Muista liittää pyyntöön myös projektisi **Project identifier string**.
Voit tarkistaa tämän satunnaisen tunnisteen esimerkiksi [SD Connect palvelusta](https://sd-connect.csc.fi). Sieltä löydät projektitunnisteen **User information** -näkymästä.

Avaa `tools-for-sd-desktop`-kansio ja vedä/kopioi sieltä tiedosto `sd-installer.desktop` työpöydällesi.

[![Installing-sd-installer](../images/desktop/sd-installer1.png)](../images/desktop/sd-installer1.png)

**Kuva 1.** `sd-installer.desktop`-tiedoston kopiointi SD Desktopille.
 
Kaksoisnapsauta kopioitua `sd-installer.desktop`-tiedostoa käynnistääksesi ohjelmistoasennustyökalun. Käytä tätä työkalua _SD Backup_ -työkalun asentamiseen SD Desktopin virtuaalikoneelle, mikäli et ole sitä vielä asentanut.

## Projektipäällikkö käynnistää varmuuskopiopalvelimen {#project-mangers-starts-backup-server}

Kun SD Backup -työkalu on asennettu, projektipäällikön tulee avata uusi pääteistunto ja käynnistää siellä virtuaalipääteistunto komennolla:

```text
screen
```

Käynnistä sitten varmuuskopiointiprosessi komennolla:

```text
sd-backup-server.sh
```

Kun `sd-backup-server.sh` käynnistetään, ohjelma kysyy projektipäällikön CSC-salasanaa.

Tämän jälkeen projektipäällikkö voi jättää virtuaali-istunnon taustalle painamalla:
`Ctrl+a+d`.

Näin `sd-backup-server.sh`-komento pysyy aktiivisena virtuaalipääteistunnossa, vaikka yhteys SD Desktopiin suljetaan.

Varsinainen palvelinprosessi on hyvin yksinkertainen. Se tarkistaa varmuuskopiohakemiston sisällön kerran minuutissa ja siirtää tämän hakemiston sisällön SD Connectissa olevaan buckettiin. Data salataan CSC:n julkisella avaimella siten, että varmuuskopioita voidaan käyttää vain SD Desktop -ympäristössä.
Oletuksena varmuuskopiohakemisto on `/shared-data/auto-backup` ja kohde-bucket SD Connectissa on `sdd-backup-<virtual-machine-name>`.

Huomaa, että palvelin ei pysty tarkistamaan, oliko annettu salasana oikea. Jos salasana on väärin, varmuuskopiointipyynnöt epäonnistuvat.
Siksi voi olla hyvä testata varmuuskopiointiprosessin toimivuus, kun palvelin on käynnissä.

## Varmuuskopioinnin tekeminen {#doing-backups}

Kun varmuuskopiopalvelin on käynnissä, kaikki virtuaalikoneen käyttäjät voivat käyttää komentoa `sd-backup` varmuuskopioidakseen tietoaineiston SD Connectiin.
Komennon `sd-backup` syntaksi on:

```text
sd-backup file.csv
```

tai

```text
sd-backup directory
```

Komento kopioi annetun tiedoston tai hakemiston varmuuskopiohakemistoon, josta palvelinprosessi siirtää sen SD Connectiin.
SD Connectissa tiedostonimeen lisätään aikaleima, jotta tiedostonimi on yksilöllinen. Lisäksi luodaan metadata-tiedosto.
Tämä tiedosto sisältää tietoa siitä käyttäjästä, joka on tehnyt varmuuskopion, alkuperäisestä koneesta ja tiedoston sijainnista. Jos varmuuskopio tehdään hakemistosta, hakemiston sisältö tallennetaan yhdeksi tar-arkistoksi, ja metadata-tiedosto sisältää listan varmuuskopioiduista tiedostoista.
 
Esimerkiksi tiedostolle `my_data.csv`, joka sijaitsee SD Desktop -virtuaalikoneessa nimeltä `secserver-1683868755`, seuraava varmuuskopiokomento:

```text
sd-backup  my_data.csv
```

Luo varmuuskopiotiedoston, joka on saatavilla Data Gatewayn kautta seuraavassa polussa:

```text
Projects/SD-Connect/project_number/sdd-backup-secserver-1683868755/my_data.csv-2023-05-15-07:41
```

Huomaa, että sinun täytyy päivittää Data Gateway -yhteys nähdäksesi muutokset SD Connectissa.