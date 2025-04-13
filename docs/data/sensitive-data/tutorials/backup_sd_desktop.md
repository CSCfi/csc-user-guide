# Varmuuskopiointipalvelin SD-Desktopille

Turvallisuussyistä vain projektipäällikkö voi viedä tietoja SD-Desktopilta. Siksi tavalliset SD-Desktopin käyttäjät eivät voi tehdä varmuuskopioita tiedoista, joita heillä on SD-Desktopilla. Tämä opas esittelee `backup_server.sh`-prosessin ja `sd-backup`-komennon käytön, jotka tarjoavat tavan SD-käyttäjille varmuuskopioida tietonsa SD Connectiin.

## Asennus {#installation}

SD Desktop -virtuaalikoneisiin ei oletuksena ole asennettu varmuuskopiointityökaluja. Siksi ensimmäinen askel on, että päällikkö asentaa **SD Backup tool** -paketin [SD-ohjelmistoasentajalla](../../sensitive-data/sd-desktop-software.md#customisation-via-sd-software-installer).

Kirjaudu SD-Desktopillesi ja avaa **Data Gateway**. Jos ohjelmistoasennuksen apuvälineet ovat käytössä projektissasi, sinulla pitäisi olla kansio `tools-for-sd-desktop` mukana hakemistossa, jonka Data Gateway on luonut (sijainnissa `Projects/SD-Connect/your-project-name`). Jos et löydä `tools-for-sd-desktop` -hakemistoa Data Gatewayn kautta, **lähetä pyyntö [CSC Service Deskille](../../../support/contact.md)**. Pyynnössä kerro, että haluat, että SD-Desktopin ohjelmistoasennuksen apuvälineet saataisiin projektiisi. Sinun tulee myös sisällyttää viestiin projektisi **projektin tunnusmerkkijono**. Voit tarkistaa tämän satunnaisen merkkijonon esimerkiksi [SD Connect -palvelusta](https://sd-connect.csc.fi). Siellä löydät projektin tunnusmerkinnän **Käyttäjätiedot** -näkymästä.

Avaa `tools-for-sd-desktop` -kansio ja sieltä vedä/kopioi tiedosto `sd-installer.desktop` työpöydällesi.

[![Installing-sd-installer](../images/desktop/sd-installer1.png)](../images/desktop/sd-installer1.png)

**Kuva 1.** Kopioidaan `sd-installer.desktop` -tiedosto SD-Desktopille.

Tuplaklikkaa kopiota `sd-installer.desktop`-tiedostosta käynnistääksesi ohjelmistoasennustyökalun. Käytä tätä työkalua asentaaksesi _SD Backup_ -työkalun SD-Desktopin virtuaalikoneeseen, jos et ole vielä tehnyt niin.

## Projektipäällikkö käynnistää varmuuskopiointipalvelimen {#project-managers-starts-backup-server}

Kun SD-Backup-työkalu on asennettu, projektipäällikön tulee käynnistää uusi pääteistunto ja siellä aloittaa virtuaalipääteistunto komennolla:

```text
screen
```

ja sitten käynnistää varmuuskopiointiprosessi komennolla:

```text
sd-backup-server.sh
```

Kun `sd-backup-server.sh` on käynnistetty, se kysyy projektipäällikön CSC-salasanaa.

Tämän jälkeen projektipäällikkö voi jättää virtuaalisen istunnon taustalle painamalla:
`Ctrl+a+d`.

Tällä tavoin `sd-backup-server.sh`-komento pysyy aktiivisena virtuaalipääteistunnossa, vaikka yhteys SD-Desktopille sulkeutuisikin.

Varsinainen palvelinprosessi on hyvin yksinkertainen. Se tarkistaa varmuuskopiohakemiston sisällön kerran minuutissa ja siirtää tämän hakemiston sisällön SD Connectin säiliöön. Tietoja salataan CSC:n julkisella avaimella niin, että varmuuskopioita voidaan käyttää vain SD Desktop -ympäristössä.
Oletusvarmuuskopiohakemisto on `/shared-data/auto-backup` ja kohdesäiliö SD Connectissa on `sdd-backup-<virtual-machine-name>`.

Huomaa, että palvelin ei pysty tarkistamaan, oliko annettu salasana oikein. Jos annettiin väärä salasana, varmuuskopiointipyynnöt epäonnistuvat. Siksi voi olla hyvä testata varmuuskopiointia, kun palvelin on käynnissä.

## Varmuuskopioiden teko {#doing-backups}

Kun varmuuskopiointipalvelin on käynnissä, kaikki virtuaalikoneen käyttäjät voivat käyttää `sd-backup`-komentoa tehdäkseen varmuuskopion tietoaineistosta SD Connectiin.
`Sd-backup`-komennon syntaksi on:

```text
sd-backup file.csv
```

tai

```text
sd-backup directory
```

Komento kopioi annetun tiedoston tai hakemiston varmuuskopiohakemistoon, mistä palvelinprosessi voi siirtää sen SD Connectiin.
SD Connectissa tiedoston nimeen lisätään aikaleima, jotta tiedoston nimi olisi yksilöllinen. Lisäksi luodaan metatietotiedosto. Tämä tiedosto sisältää tietoa käyttäjästä, joka pyysi varmuuskopiota, alkuperäisestä isännästä ja tiedoston sijainnista. Jos varmuuskopio tehdään hakemistosta, hakemiston sisältö tallennetaan yhdeksi tar-arkistotiedostoksi ja metatietotiedosto sisältää luettelon varmuuskopioiduista tiedostoista.

Esimerkiksi tiedostolle nimeltä `my_data.csv`, joka sijaitsee SD Desktop -virtuaalikoneessa nimeltä `secserver-1683868755`, varmuuskopiointikomennolla:

```text
sd-backup  my_data.csv
```

Luodaan varmuuskopiotiedosto, joka on saatavilla Data Gatewayn kautta polussa:

```text
Projects/SD-Connect/project_number/sdd-backup-secserver-1683868755/my_data.csv-2023-05-15-07:41
```

Huomaa, että sinun on päivitettävä Data Gateway -yhteys nähdäksesi muutokset SD Connectissa.