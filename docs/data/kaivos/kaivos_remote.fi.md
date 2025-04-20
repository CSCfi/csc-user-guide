# Käyttämällä kaivos.csc.fi-palvelinta suoraan omalta tietokoneeltasi {#using-kaivos-csc-fi-directly-from-your-local-computer}

MySQL-tietokantoihin `kaivos.csc.fi`:ssä voi normaalisti päästä suoraan vain CSC:n laskentapalvelimilta (Puhti ja Mahti). Voit kuitenkin tehdä tietokannan näkyväksi omalle tietokoneellesi käyttämällä CSC:n käyttäjätunnustasi ja _ssh-tunnelin_ kautta tapahtuvaa porttiohjausta.

!!! note "SSH-avaimet"
    Huomaa, että yhteys CSC:n laskentapalvelimiin SSH:lla vaatii SSH-avainten käyttöönottoa sekä julkisen avaimen lisäämistä MyCSC-portaaliin.
    [Lue ohjeet täältä](../../computing/connecting/ssh-keys.md).

Linux- ja MacOSX-koneissa ssh-tunnelin voi muodostaa omalta tietokoneelta `kaivos.csc.fi`:hin `puhti.csc.fi`:n kautta esimerkiksi seuraavalla komennolla:

```bash
ssh -l csc_username -L 3306:kaivos.csc.fi:3306 puhti.csc.fi -N
```

Yhteyskomennon lopussa oleva `-N`-valitsin estää komentotulkin käytön yhteyden muodostamisen jälkeen. Heti kun yhteys suljetaan, myös porttiohjaus lakkaa toimimasta. Huomaa, että yllä olevassa ssh-komennossa käytetään CSC:n käyttäjätunnusta, ei tietokannan käyttäjätunnusta.

Windows-koneissa voit käyttää esimerkiksi plink-ohjelmaa tunnelin avaamiseen. [Plink](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) toimii vain komentokehotteen kautta. Alla esimerkki plinkin käytöstä:

```bash
plink -L 3306:kaivos.csc.fi:3306 csc_username@puhti.csc.fi
```

Yllä olevissa tunnelointikomennoissa määritetään, että kaikki liikenne paikallisen koneesi porttiin 3306 (MySQL:n oletusportti) välitetään `kaivos.csc.fi`-palvelimen MySQL-porttiin CSC:n `puhti.csc.fi`-palvelimen kautta. Niin kauan kuin yhteys puhti.csc.fi:hin on aktiivinen, voit käyttää `kaivos.csc.fi`:n tietokantaa omalta tietokoneeltasi samoilla MySQL-komennoilla kuin Puhdilla (olettaen, että MySQL-asiakasohjelma on asennettuna paikalliselle koneellesi). Ainoa ero aikaisempiin komentoesimerkkeihin on, että nyt palvelinosa (`-h`) tulee osoittaa osoitteeseen `127.0.0.1`, joka viittaa paikalliseen koneeseesi, `kaivos.csc.fi`:n sijaan.

Esimerkiksi interaktiivisen MySQL-istunnon avaus komennolla:

```bash
mysql -u db_user_account -p -h 127.0.0.1 --local database_name
```

Ja `mysqlimport`-komennon syntaksi:

```bash
mysqlimport -h 127.0.0.1 -u db_user_account --local --compress --password database_name input_file.table
```

Samalla tavalla voit tehdä tietokannat näkyviksi omalle koneellesi myös paikallisesti asennettujen graafisten MySQL-ohjelmien, kuten [MySQL Workbenchin](https://www.mysql.com/products/workbench/), avulla. Ainoa merkittävä rajoite porttiohjauksessa on, että ssh-tunnelit eivät yleensä ole kovin vakaita. Saatat joutua avaamaan ssh-yhteyden uudelleen silloin tällöin, eikä ole syytä luottaa, että tunneli säilyy käytettävissä useiden tuntien ajan.

Tietoturvasyistä suosittelemme, että suljet ssh-yhteyden aina lopettaessasi tietokannan käytön.