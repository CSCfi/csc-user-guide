
# Varaukset {#backups}

Kaikki tietokannat DBaaS:ssa varmuuskopioidaan automaattisesti noin 24 tunnin välein. Käyttäjät voivat myös manuaalisesti ottaa varmuuskopion omista instansseistaan, mutta tällöin seuraava automaattinen varmuuskopio otetaan noin 24 tuntia edellisen jälkeen. Kaikki varmuuskopiot säilytetään 90 päivää, jonka jälkeen ne poistetaan automaattisesti, käyttäjä ei voi poistaa varmuuskopioita manuaalisesti.

Varmuuskopiot tallennetaan salattuina Allas-järjestelmään.
<!-- TODO Haluaisin dokumentaatiomme mainitsevan, miten varmuuskopio toimiii taustalla esim. -->

Web-käyttöliittymä näyttää tällä hetkellä vain viimeiset 20 varmuuskopiota. Jos haluat nähdä kaikki varmuuskopiosi, sinun on käytettävä CLI-työkalua.

## Riskit {#risks}

Ole tietoinen siitä, että varmuuskopiointitoiminto on vielä kehitysvaiheessa, eikä sitä pitäisi käyttää mihinkään arkaluonteiseen tai tärkeään.

* Varmuuskopiot tallennetaan salattuina Allas-järjestelmään. Tämä on hyvä pitää mielessä, jos haluat ottaa oman varmuuskopioinnin (sinun kannattaa luultavasti tallentaa ne muualle kuin Allas tai cPouta).
* Kun "palautat" varmuuskopion, se luo uuden instanssin uudella IP:llä. Ole siis tietoinen siitä, että saatat joutua päivittämään palvelusi poistuvat palomuurit.
* Jos sinulla on huolenaiheita, älä epäröi ottaa yhteyttä [CSC Service Desk](../../support/contact.md).
* Kaikki tietokantasi tiedot ja varmuuskopiot tallennetaan CSC:n Kajaanin datakeskuksessa. Jos datakeskukseen kohdistuu katastrofaalinen tietojen menetys, voit menettää kaikki tietosi.
* Jos käytät DBaaS-palvelua todella tärkeisiin projekteihin/tietoihin, kannattaa harkita myös omien varmuuskopioiden ottamista, jotka tallennetaan muualla kuin CSC:ssä mahdollisen katastrofin varalta.

## Manuaaliset varmuuskopiot {#manual-backups}

Varmuuskopioita voidaan tehdä manuaalisesti.

1. Varmuuskopion luominen:

    ```
    openstack database backup create --instance $INSTANCE_ID $USER_FRIENDLY_NAME_OF_BACKUP
       # Sopiva nimi voisi olla instanssin nimi
    ```

2. Nyt voit listata kaikki varmuuskopiosi:

    ```
    openstack database backup list
    ```

3. Voit myös näyttää lisätietoja varmuuskopiosta:

    ```
    openstack database backup show $BACKUP_ID
    ```

## Varmuuskopion palautus ja/tai tarkistus {#restoring-and-or-verifying-backup}

Varmuuskopion palauttaminen on samanlainen prosessi kuin uuden instanssin luominen. Tämän voi tehdä [web-käyttöliittymästä](web-interface.md) sekä [CLI:stä](cli.md).
