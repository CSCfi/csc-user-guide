# SD Connect -palvelun käyttäminen a-komentojen kanssa {#using-sd-connect-service-with-a-commands}

SD Connect on osa CSC:n arkaluonteisen datan palveluita, jotka tarjoavat maksuttoman ympäristön arkaluonteisen datan käsittelyyn suomalaisissa yliopistoissa ja tutkimuslaitoksissa toteutettavia tieteellisiä projekteja varten. SD Connect lisää automaattisen salauskerroksen CSC:n Allas-objektitallennusjärjestelmään, jotta sitä voidaan käyttää arkaluonteisen datan turvalliseen tallennukseen. SD Connectiin tallennettua dataa voidaan käyttää myös SD Desktopin turvattujen virtuaalityöpöytien kautta.

Useimmissa tapauksissa SD Connectia käytetään [SD Connect Web -käyttöliittymän](https://sd-connect.csc.fi) kautta, mutta joissakin tilanteissa komentorivityökalut tarjoavat tehokkaamman tavan hallita dataa SD Connectissa.

Tässä ohjeessa kuvaamme, miten voit käyttää [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils) -paketin tarjoamia a-komentoja tiedon siirtämiseen SD Connectiin ja sieltä takaisin. Nämä työkalut ovat saatavilla CSC:n supertietokoneilla (Puhti, Mahti ja Lumi) ja ne voidaan asentaa myös paikallisille Linux- ja Mac-koneille.

Huomaa, että Allas itsessään ei erottele SD Connectilla tallennettua dataa muusta Allakseen tallennetusta datasta. Datakaukalot voivat sisältää sekaisin SD Connect -dataa, muuta salattua dataa ja tavallista dataa, ja käyttäjän vastuulla on tietää, minkä tyyppistä dataa kyseessä on. On kuitenkin luultavasti hyvä käytäntö pitää SD Connect -data omissa kansioissaan ja kaukaloissaan ilman muita datatyyppejä.

## Yhteyden avaaminen SD Connectiin {#opening-connection-to-sd-connect}

Jotta voisit avata SD Connect -yhteensopivan Allas-yhteyden, sinun tulee lisätä *--sdc* -valitsin konfigurointikomentoon. CSC:n supertietokoneilla yhteys avataan komennoilla:

```bash
module load allas
allas-conf --sdc
```

Paikallisissa asennuksissa yhteys avataan tyypillisesti kommentoilla, kuten

```bash
export PATH=/some-local-path/allas-cli-utils:$PATH
source /some-local-path/allas-cli-utils/allas_conf -u your-csc-account --sdc
```

Asetusprosessi pyytää ensin CSC-tunnusten salasanan (Haka- tai Virtu-tunnuksia ei voi käyttää tässä). Tämän jälkeen valitaan käytettävä CSC-projekti. Tämä on tavallinen Allas-kirjautumisprosessi. Mutta kun SD Connect on käytössä, prosessi pyytää syöttämään *SD Connect API -tunnisteen* (token). Tunniste täytyy hakea [SD Connectin web-käyttöliittymästä](https://sd-connect.csc.fi). Huomaa, että tunnisteet ovat projektikohtaisia. Tarkista, että olet valinnut saman SD Connect -projektin sekä komentorivillä että web-käyttöliittymässä.

Web-käyttöliittymässä tunnisteen voi luoda valitsemalla *Create API tokens* valikosta *Support*.

Kopioi tunniste, liitä se komentoriville ja paina enter.

SD Connect -yhteensopiva Allas-yhteys on nyt voimassa seuraavat kahdeksan tuntia. Voit käyttää esimerkiksi *a-list*- ja *a-delete*-komentoja hallitaksesi sekä tavallisia Allas-objekteja että SD Connect -objekteja.

## Datan lataaminen palveluun {#data-upload}

Dataa voidaan lähettää SD Connectiin käyttäen komentoa *a-put* yhdessä *--sdc*-valinnan kanssa.
Esimerkiksi ladataksesi tiedoston *my-secret-table.csv* paikkaan *2000123-sens/dataset2* Allakseen, käytä komentoa:

```bash
a-put --sdc my-secret-table.csv -b 2000123-sens/dataset2
```

Tämä luo SD Connect -objektin: 2000123-sens/dataset2/my-secret-table.csv.c4gh

Kaikkia muitakin a-put valintoja ja ominaisuuksia voi käyttää normaalisti. Esimerkiksi hakemistot tallennetaan tar-tiedostoina, ellei --asis-valintaa käytetä.

Komento:

```bash
a-put --sdc my-secret-directory -b 2000123-sens/dataset2
```

Luo SD Connect -objektin: 2000123-sens/dataset2/my-secret-directory.tar.c4gh

Suurien datamäärien siirtoon voit käyttää *allas-dir-to-bucket* -komentoa yhdessä *--sdc*-valinnan kanssa.

```bash
allas-dir-to-bucket --sdc my-secret-directory  2000123-new-sens
```

Yllä oleva komento kopioi kaikki tiedostot hakemistosta my-secret-directory kaukaloon 2000123-new-sens SD Connect -yhteensopivassa muodossa.

## Datan lataaminen palvelusta {#data-download}

Dataa voidaan ladata Allaksesta komennolla a-get. Jos SD Connect -yhteys on käytössä, a-get pyrkii automaattisesti purkamaan salauksen niistä objekteista, joiden pääte on *.c4gh*.

Esimerkiksi komento:

```bash
a-get 2000123-sens/dataset2/my-secret-table.csv.c4gh
```

Tuottaa paikallisen tiedoston: my-secret-table.csv

Vastaavasti komento:

```bash
a-get 2000123-sens/dataset2/my-secret-directory.tar.c4gh
```

Tuottaa paikallisen hakemiston: my-secret-directory

Huomaa, että tämä automaattinen purku toimii vain niille tiedostoille, jotka on tallennettu uudella SD Connectilla, joka otettiin käyttöön lokakuussa 2024.

Vanhempien SD Connect -tiedostojen ja muiden Crypt4gh-salattujen tiedostojen kanssa on yhä annettava oikea salausavain valitsimella *--sk*

```bash
a-get --sk my-key.sec  2000123-sens/old-date/sample1.txt.c4gh
```

Valitettavasti ei ole yksinkertaista tapaa selvittää, mitä salaustapaa .c4gh-tiedoston tallentamisessa Allakseen on käytetty.