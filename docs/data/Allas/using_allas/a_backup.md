
# allas-backup: melkein itsepalveluvarmuuskopio {#allas-backup-nearly-a-self-service-backup}

CSC ei tarjoa varmuuskopiointipalvelua asiakkailleen ilmaisena palveluna. Tässä luvussa kuvaamme työkalun nimeltä _allas-backup_, jota voidaan käyttää varmuuskopiotiedostojen ja hakemistojen luomiseen, jotka sijaitsevat CSC:n supertietokoneilla tai käyttäjän omalla tietokoneella, Allasiin.

Tämä työkalu ei kuitenkaan tarjoa varsinaista varmuuskopiointipalvelua – data tallennetaan vain yhteen paikkaan ja yhteen buckettiin Allasissa. Tämän bucketin voi poistaa todennettu käyttäjä yhdellä komennolla, mikä poistaa kaikki varmuuskopiot peruuttamattomasti.

_allas-backup_-työkalu tarjoaa helppokäyttöisen komentoriviliittymän [restic](https://restic.readthedocs.io/)-varmuuskopiointityökalulle. _allas-backup_ luo automaattisesti projektilähtöisen varmuuskopiorepositorion CSC:n Allas-tallennuspalveluun ja käyttää sitä kumulatiivisiin varmuuskopioihin.

Toisin kuin datan lataustyökalut, kuten `a-put`, `s3cmd put` tai `rclone copy`, allas-backup (tai oikeastaan _restic_-ohjelma) tallentaa tuodun datan kokoelmatiivisteenä. Tämä ominaisuus mahdollistaa tehokkaan tallennuksen dataseteille, joihin sisältyy pieniä muutoksia. Näin datasetin eri versiot voidaan tallentaa niin, että uuden datasetin version tapauksessa vain edelliseen versioon verrattuna muuttuneet osat tarvitsevat tallentamista.

Käyttääksesi tätä työkalua, avaa ensin yhteys Allasiin:
```text
module load allas
allas-conf
```
Yhteys pysyy auki kahdeksan tuntia.

**VARMUUSKOPIOINNIN TOIMINNOT** {#backup-operations}

Toiminnot, joihin `allas-backup`-työkalua voidaan käyttää:

- `allas-backup <tiedosto_tai_hakemisto>` tai `allas-backup add <tiedosto_tai_hakemisto>`
  Lisää uuden varmuuskopioversion (snapshot) tiedostosta tai hakemistosta varmuuskopiorepositioon.

- `allas-backup list`
  Listaa varmuuskopiorepositioon tallennetut snapshotit. Optio _-last_ listaa vain snapshotien viimeisimmät versiot.

- `allas-backup files <snapshot_id>`
  Listaa snapshotin sisältämät tiedostot.

- `allas-backup find <kysely>`
  Etsii snapshotit, jotka sisältävät kyselytermille vastaavan tiedoston tai hakemiston.

- `allas-backup restore <snapshot_id>`
  Hakee snapshotin tiedot paikalliseen ympäristöön.
  Oletuksena tallennetut tiedot palautetaan paikalliseen hakemistoon. Muita sijainteja voidaan määritellä _-target_-optiolla.

- `allas-backup dump <snapshot_id> -f <tiedosto>`
  Palauttaa tiedoston sisällön snapshotista.

- `allas-backup delete <snapshot_id>`
  Poistaa snapshotin varmuuskopiorepositoriosta.

- `allas-backup unlock`
  Poistaa Restic-lukitustiedostot.

