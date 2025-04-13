
# Suorayhteyden käyttö kaivos.csc.fi:tä tietokoneeltasi {#using-kaivos-csc-fi-directly-from-your-local-computer}

MySQL-tietokantoihin `kaivos.csc.fi`:ssä voidaan suoraan päästä ainoastaan CSC:n laskentapalvelimilta (Puhti ja Mahti). Voit kuitenkin tehdä tietokannan näkyväksi omalle tietokoneellesi käyttämällä CSC:n käyttäjätiliäsi ja porttiohjausta _ssh tunnelin_ kautta.

!!! note "SSH-avaimet"
    Huomaa, että CSC:n laskentapalvelimille SSH-yhteyden ottaminen edellyttää SSH-avainten luomista ja julkisen avaimen lisäämistä MyCSC-portaaliin.
    [Lue ohjeet täältä](../../computing/connecting/ssh-keys.md).

Linux- ja MacOSX-koneilla ssh-tunnelin luominen omalta tietokoneeltasi `kaivos.csc.fi`:hin `puhti.csc.fi`:n kautta voidaan tehdä esimerkiksi komennolla:

```bash
ssh -l csc_käyttäjänimi -L 3306:kaivos.csc.fi:3306 puhti.csc.fi -N
```

Yhteyden komennon lopussa oleva `-N`-vaihtoehto estää komentorivin käytön yhteyden avaamisen jälkeen. Kun yhteys suljetaan, myös porttiohjaus lakkaa toimimasta. Huomaa, että yllä olevassa ssh-komennossa käytetään CSC-käyttäjätilisi nimeä, ei tietokannan käyttäjätiliä.

Windows-koneilla voit käyttää esimerkiksi plink-ohjelmaa tunnelin avaamiseen. [Plink](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) voidaan käyttää vain komentokehotteen kautta. Alla on esimerkki plink-komennosta:

```bash
plink -L 3306:kaivos.csc.fi:3306 csc_käyttäjänimi@puhti.csc.fi
```

Yllä olevat tunnelointikomennot määrittävät, että viestintä porttiin 3306 (MySQL:n oletusportti) omassa tietokoneessasi siirretään `kaivos.csc.fi`:n MySQL-porttiin `puhti.csc.fi`-palvelimen kautta. Niin kauan kuin yhteys puhti.csc.fi:hin on aktiivinen, `kaivos.csc.fi`:n tietokantaan pääsee käsiksi omalta tietokoneeltasi käyttämällä samoja MySQL-komentoja kuin yllä on kuvattu Puhtille (olettaen, että MySQL-asiakasohjelma on asennettu omalle koneellesi). Ainoa ero aikaisempiin komentoesimerkkeihin verrattuna on, että isäntäosio (`-h`) tulisi nyt osoittaa isäntään `127.0.0.1`, joka viittaa paikalliseen isäntään, `kaivos.csc.fi`:n sijaan.

Esimerkiksi MySQL:n interaktiivisen istunnon avaamisen syntaksi olisi nyt:

```bash
mysql -u db_käyttäjätili -p -h 127.0.0.1 --local tietokannan_nimi
```

Ja `mysqlimport`-syntaksi:

```bash
mysqlimport -h 127.0.0.1 -u db_käyttäjätili --local --compress --password tietokannan_nimi syötetiedosto.tiedosto
```

Samalla tavoin voit tehdä tietokantojesi näkyviksi paikallisella tietokoneellasi käyttämällä paikallisesti asennettuja graafisia MySQL-rajapintoja, kuten [MySQL Workbench](https://www.mysql.com/products/workbench/). Ainoa merkittävä rajoitus porttiohjauksella on, että normaalisti ssh-tunnelit eivät ole kovin vakaita. Saatat joutua avaamaan ssh-yhteyden uudelleen silloin tällöin, eikä tule luottaa siihen, että tunneli pysyy käytettävissä useita tunteja.

Tietoturvasyistä suosittelemme, että suljet ssh-yhteyden aina, kun lopetat tietokannan käytön.