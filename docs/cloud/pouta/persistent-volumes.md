# Pysyvät volyymit { #persistent-volumes }

Tässä artikkelissa kuvataan yksi tapa tallentaa dataa Poudassa siten, että se säilyy myös virtuaalikoneen sammuttamisen jälkeen.

Pysyvät volyymit nimensä mukaisesti säilyvät, vaikka instanssit poistetaan. Niitä voidaan liittää virtuaalikoneisiin tai irrottaa niistä niiden käydessä.

Pysyvät volyymit käyttävät CEPH-klusteria. Jos I/O-suorituskyky on kriittinen, tätä volyymityyppiä ei kannata käyttää – dataan päästään käsiksi verkon kautta, mikä aiheuttaa väistämättä viivettä.

## Volyymin luominen ja liittäminen Poutan web-käyttöliittymässä { #creating-and-attaching-a-volume-in-the-pouta-web-interface }

Pysyviä volyymeja voidaan luoda joko web-käyttöliittymässä tai komentorivillä.

Web-käyttöliittymässä käytä *Volumes*-sivulla painiketta **Create volume** uuden volyymin luomiseksi. Voit antaa volyymille nimen ja koon (vähintään 1 Gt). Ainoa pakollinen parametri on volyymin koko.

![Luo pysyvä volyymi](../../img/create-volume-horizon.png)

!!! Warning "Vältä ei-ASCII-merkkejä nimessä tai kuvauksessa"
    Tämä on tunnettu virhe volyymijärjestelmässä. Volyymin luonti epäonnistuu, jos sen nimessä tai kuvauksessa on muita kuin ASCII-merkkejä (esim. ä, ö, å, é, à, ñ, [CJK characters](https://en.wikipedia.org/wiki/CJK_characters), ...):

    ![Volyymin luonti epäonnistui](../img/Unable-to-create-volume.png)

    Ja volyymi jumittuu tilaan "Creating":

    ![Luodaan](../img/Creating.png)

    Ainoa tapa poistaa volyymi, joka on luotu ei-ASCII-merkillä, on käyttää komentoriviä (katso alla).

Kun volyymi on luotu, se voidaan liittää käynnissä olevaan virtuaalikoneeseen. Yksi volyymi voidaan liittää vain yhteen virtuaalikoneeseen kerrallaan.

Volyymin liittämiseksi valitse ensin Poutan web-käyttöliittymässä näkymä *Volumes*. Napsauta nuolikuviota sen volyymin **Edit Volume** -painikkeen vieressä, jonka haluat liittää, ja valitse **Manage attachments**. Valitse instanssi (eli virtuaalikone), johon haluat liittää volyymin, **Attach to Instance** -valitsimesta.

![Liitä pysyvä volyymi](../../img/volume-attach-horizon2.png)

## Volyymin luominen ja liittäminen komentorivillä { #creating-and-attaching-a-volume-with-command-line-interface }

Pysyviä volyymeja voidaan myös luoda ja liittää komentoriviltä:

```
openstack volume create --description "<description>" --size <size> <name>
```

!!! Warning "Vältä ei-ASCII-merkkejä nimessä tai kuvauksessa"
    Tämä on tunnettu virhe volyymijärjestelmässä. Volyymin luonti epäonnistuu, jos sen nimessä tai kuvauksessa on ei-ASCII-merkkejä; tähän kuuluvat ääkköset ja muut erikoismerkit.

    ```sh
    $ openstack volume create --description='Déjà vu' --size 1 matrice
    Error decoding your request. Either the URL or the request body contained characters that could not be decoded by Cinder. (HTTP 400) (Request-ID: req-7dc59e6f-eb29-4a5f-9cdc-4a44b177e3f2)
    ```

    Ainoa tapa poistaa volyymi, joka on luotu ei-ASCII-merkillä, on käyttää komentoriviä (katso alla).

Listaa olemassa olevat volyymit:

```
openstack volume list
```

Listaa olemassa olevat virtuaalikoneet löytääksesi sen, johon haluat liittää volyymin:

```
openstack server list
```

Kun volyymin tila on "available", voit liittää sen virtuaalikoneeseen (voit viitata sekä virtuaalikoneeseen että volyymiin nimellä tai ID:llä):

```
openstack server add volume <virtual machine> <volume>
```

!!! info

    Useimmat volyymityypit voidaan liittää vain yhteen virtuaalikoneeseen kerrallaan.

## Liitettyjen volyymien käyttö { #using-attached-volumes }

Liitetty volyymi pitää alustaa ensimmäisellä käyttökerralla. Tämä tulee tehdä vain ensimmäisellä käyttökerralla, muuten ylikirjoitat kaiken datan volyymilla. Selvitä ensin, mikä laite vastaa volyymiasi.

Alla on yksinkertainen esimerkki tiedostojärjestelmän luomisesta volyymille ja sen liittämisestä automaattisesti uudelleenkäynnistyksen jälkeen. Huomaa, että tämä on yksinkertainen esimerkki ja tiedostojärjestelmiä voi hallita monin muinkin tavoin.

Kirjauduttuasi virtuaalikoneeseen voit listata levyt:

    sudo parted -l

Volyymin pitäisi olla tunnistettavissa koon perusteella. Tässä esimerkissä oletetaan, että se on `/dev/vdb`. Luodaan ensin sille tiedostojärjestelmä. Käytämme *xfs*:ää, koska se toimii hyvin Poudassa:

    sudo mkfs.xfs /dev/vdb

Nyt voit alkaa käyttää volyymiä. Jos haluat liittää sen hakemistoon `/media/volume`, varmista ensin, että polku on olemassa:

    sudo mkdir -p /media/volume

Sitten voit liittää sen:

    sudo mount /dev/vdb /media/volume

Lopuksi sinun pitää muuttaa omistajuus, jotta voit lukea ja kirjoittaa siihen. Alla oletetaan käyttäjänimeksi cloud-user.

    sudo chown cloud-user:cloud-user /media/volume

Tämän jälkeen volyymiä voi käyttää normaalisti. Jos haluat, että volyymi on käytettävissä myös virtuaalikoneen uudelleenkäynnistyksen jälkeen, lisää se `/etc/fstab`-määritystiedostoon. Voit käyttää aiemmin osiolle luomaasi tunnistetta:

    sudo sh -c 'echo "/dev/vdb     /media/volume    xfs    defaults,nofail    0    2" >> /etc/fstab'

## Volyymin irrottaminen web-käyttöliittymässä { #detaching-the-volume-using-web-interface }

Kun olet valmis ja haluat irrottaa volyymin, muista ensin irrottaa tiedostojärjestelmä ennen volyymin irrottamista!

    sudo umount /dev/vdb

## Volyymin irrottaminen komentorivillä { #detaching-the-volume-using-cli }

Kun et enää tarvitse volyymiä liitettynä, voit irrottaa sen. Ennen irrottamista muista irrottaa volyymin tiedostojärjestelmä virtuaalikoneessa, jotta vältät tietojen menetyksen!

```
openstack server remove volume <server> <volume>
```

- Kun instanssi, johon volyymi on liitetty, laitetaan [shelved](vm-lifecycle.md#shelved)-tilaan, volyymin tila muuttuu muotoon **Reserved**. Instanssin palauttaminen (unshelving) muuttaa tilan takaisin **In-use**, ja instanssin poistaminen asettaa tilaksi **Available**.
- Kun kyseessä on **multiattach volume**, tila muuttuu **Reserved**-tilaan, kun kaikki liitetyt instanssit shelvataan. Tämä estää volyymiä tulemasta liitetyksi toiseen instanssiin. Tila palautuu **In-use** heti, kun vähintään yksi liitetyistä instansseista on **unshelved**.

Jos haluat poistaa volyymin ja sillä olevan datan, suorita:

```
openstack volume delete <volume> # Name or ID of volume
```

Data poistetaan pysyvästi, eikä sitä voi palauttaa.

## Volyymien siirtäminen kahden Pouta-projektin välillä web-käyttöliittymällä { #transferring-volumes-between-two-pouta-projects-using-web-interface }

Joskus saatat tarvita pysyvien volyymien siirtämistä kahden Pouta-projektin välillä. Esimerkiksi suurten aineistojen tai käynnistettävien volyymien siirtäminen kollegoille toiseen Pouta-projektiin. Tämä voidaan tehdä volyymisiirroilla. Poutassa projektien välinen volyymisiirto on nopeaa, välttää datan monistamisen ja tarpeettomat verkkosiirrot. Volyymin siirtäminen toiseen projektiin tarkoittaa, että alkuperäisellä projektillasi ei ole enää siihen pääsyä. Huomaa, että Poudan volyymisiirrot toimivat saman pilviympäristön sisällä; voit siis siirtää volyymin cPouta-projektista toiseen cPouta-projektiin, mutta et cPouta- ja ePouta-projektien välillä.

Siirtääksesi volyymin varmista ensin, että sen tila on **Available**. Voit tehdä tämän irrottamalla sen instanssista, johon se alun perin oli liitetty. Kun volyymin tila on available, voit aloittaa siirron joko Poudan web-käyttöliittymässä tai komentorivillä.

Poudan web-käyttöliittymässä siirry näkymään *Volumes* ja napsauta siirrettävän volyymin **Edit Volume** -painikkeen vieressä olevaa nuolikuviota ja valitse **Create Transfer.** Nimeä siirtopyyntö ja napsauta **Create Volume Transfer.** Saat tämän jälkeen siirtotunnisteet (transfer ID ja authorization key).

![Siirrä volyymi toiseen projektiin](../../img/pouta-volume-transfer-creation.png)

Sinun on annettava nämä tunnisteet kollegalle, jolle haluat siirtää volyymin.

Kollegasi voi hyväksyä volyymin siirron omassa projektissaan siirtymällä web-käyttöliittymän *Volumes*-näkymään ja napsauttamalla **Accept Transfer** -painiketta. Hänen tulee syöttää edellisessä vaiheessa saamasi siirtotunnisteet ja valita **Accept Volume Transfer.** Tämän jälkeen volyymi siirtyy kollegasi projektille.

![Hyväksy volyymin siirto](../../img/pouta-accept-volume-transfer.png)

## Volyymien siirtäminen kahden Pouta-projektin välillä komentorivillä { #transferring-volumes-between-two-pouta-projects-using-cli }

Volyymisiirrot voi tehdä myös komentorivillä:

    openstack volume transfer request create <name or UUID of volume to transfer>

Tämän komennon tuloste sisältää siirtotunnisteet (transfer ID ja authorization key). Tallenna ne ja toimita kollegalle, jolle haluat siirtää volyymin.

Kollegasi voi hyväksyä tämän volyymin siirtopyynnön:

    openstack volume transfer request accept <transferID> <authKey>

## Liitetyn volyymin koon kasvattaminen Poutan web-käyttöliittymässä { #expanding-size-of-the-attached-volume-in-the-pouta-web-interface }

Olet aiemmin luonut ja liittänyt volyymin. Tässä osassa kasvatat instanssiin liitetyn volyymin kokoa. Ennen kuin kasvatat volyymin kokoa, sinun on irrotettava se instanssista; muista irrottaa tiedostojärjestelmä ennen volyymin irrottamista!

    sudo umount /dev/vdb

Volyymin laajentamiseksi valitse ensin web-käyttöliittymässä näkymä *Volumes*. Napsauta **Edit Volume** -painikkeen vieressä olevaa nuolikuviota sen volyymin kohdalla, jota haluat suurentaa, ja valitse **Extend Volume**. Syötä haluamasi volyymin määrä "GiB"-yksiköissä kenttään **New Size (GiB)**. Napsauta lopuksi **Extend Volume** -painiketta.
Laajennetun volyymin liittäminen tapahtuu kuten aiemmin: valitse *Volumes*-näkymä, napsauta laajennetun volyymin **Edit Volume** -painikkeen vieressä olevaa nuolikuviota ja valitse **Manage attachments**. Valitse instanssi (eli virtuaalikone), johon haluat volyymin liittää, **Attach to Instance** -valitsimesta.

![Laajenna pysyvää volyymiä](../../img/volume-expand-horizon1.png)

Kirjauduttuasi virtuaalikoneeseen voit listata levyt:

    sudo parted -l

Kuten aiemmin, voit tunnistaa volyymin sen koon perusteella. Liitä volyymi ensin tavanomaiseen polkuun:

    sudo mount /dev/vdb /media/volume

Lopuksi tiedostojärjestelmä täytyy kasvattaa, jotta lisätila tulee käyttöön. Jos volyymin tiedostojärjestelmä on xfs, sen voi kasvattaa komennolla:

    sudo xfs_growfs /dev/vdb
    
Voit varmistaa, että tiedostojärjestelmän koko on odotettu, seuraavalla komennolla:

    sudo xfs_info /dev/vdb

Kertomalla lohkokoon (_bs_) tiedostojärjestelmän lohkojen määrällä (_blocks_) saat tiedostojärjestelmän koon tavuina.

## Liitetyn volyymin koon kasvattaminen komentorivillä { #expanding-size-of-the-attached-volume-using-cli }

Kasvattaaksesi volyymin kokoa irrota se ensin palvelimesta komennolla:

```
openstack server remove volume <server-id> <volume-id>
```
Tarkista sitten, että volyymi on vapaana laajennusta varten, listaamalla volyymit:
```
openstack volume list
```
Voit nyt kasvattaa volyymin kokoa antamalla volyymin ID:n ja uuden koon:
```
openstack volume set <volume-id> --size <volume-size>
```