# allas-backup: melkein omatoiminen varmuuskopiointi {#allas-backup-nearly-a-self-service-backup}

CSC ei tarjoa varmuuskopiointipalvelua ilmaiseksi asiakkailleen. Tässä luvussa kuvataan _allas-backup_-niminen työkalu, jota voidaan käyttää tiedostojen ja hakemistojen varmuuskopiointiin, joko CSC:n supertietokoneilta tai käyttäjän omalta tietokoneelta Allakseen.

Kuitenkin tämä työkalu ei tarjoa varsinaista varmuuskopiointipalvelua – data tallennetaan vain yhteen sijaintiin ja yhteen bucketiin Allaksessa. Tämän bucketin voi vahvistettu käyttäjä poistaa yhdellä komennolla, mikä poistaa kaikki varmuuskopiot peruuttamattomasti.

_allas-backup_-työkalu tarjoaa helppokäyttöisen komentoriviliittymän [restic](https://restic.readthedocs.io/) -varmuuskopiointityökalulle. _allas-backup_ luo automaattisesti projektikohtaisen varmuuskopiointivaraston CSC:n Allas-tallennuspalveluun ja käyttää sitä kumulatiivisiin varmuuskopioihin.

Toisin kuin tiedostonlähetystyökalut, kuten `a-put`, `s3cmd put` tai `rclone copy`, allas-backup (tai oikeastaan _restic_-ohjelma) tallentaa tuodun datan kokoelmahajana (hashinä). Tämä ominaisuus mahdollistaa tehokkaan tallennuksen aineistoille, joissa tapahtuu pieniä muutoksia. Näin ollen eri versiot aineistosta voidaan tallentaa siten, että uuden version tapauksessa tallennetaan vain muutokset edelliseen versioon nähden.

Tämän työkalun käyttöä varten yhdistä ensin Allakseen:
```text
module load allas
allas-conf
```
Yhteys pysyy auki kahdeksan tunnin ajan.

**VARMUUSKOPIOINTITOIMINNOT** {#backup-operations}

Toiminnot, joita `allas-backup`-työkalulla voi tehdä:

 - `allas-backup <file_or_directory>`  tai `allas-backup add <file_or_directory>`   
 	Lisää uuden varmuuskopiointiversion (snapshot) tiedostosta tai hakemistosta varastoon.

 - `allas-backup list`   
 	Listaa varastoon tallennetut snapshotit. Vaihtoehto _-last_ listaa vain viimeisimmät snapshotien versiot.
 
 - `allas-backup files <snapshot_id>`   
 	Listaa snapshotin sisältämät tiedostot.

 - `allas-backup find <query>`          
 	Etsii snapshotteja, jotka sisältävät haun määrittelyn mukaisen tiedoston tai hakemiston.

 - `allas-backup restore <snapshot_id>`  
 	Noutaa snapshotin datan paikalliseen ympäristöön. 
	Oletusarvoisesti tallennettu data palautetaan paikalliseen hakemistoon. Muita sijainteja voi määritellä _-target_-valitsimella.

 - `allas-backup dump <snapshot_id> -f <file>`  
    Noutaa tiedoston sisällön snapshotista.

 - `allas-backup delete <snapshot_id>`  
 	Poistaa snapshotin varmuuskopiointivarastosta.

 -	`allas-backup unlock`                
    Poistaa Resticin lukitustiedostot.