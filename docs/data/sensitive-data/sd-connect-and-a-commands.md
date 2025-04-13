
# SD Connect -palvelun käyttäminen a-käskyjen kanssa {#using-sd-connect-service-with-a-commands}

SD Connect on osa CSC:n herkkien tietojen palveluita, jotka tarjoavat maksuttoman herkkien tietojen käsittely-ympäristön suomalaisissa yliopistoissa ja tutkimuslaitoksissa toteutettaville akateemisille tutkimusprojekteille. SD Connect lisää automaattisen salauskerroksen CSC:n Allas-objektien tallennusjärjestelmään, jotta sitä voidaan käyttää herkkien tietojen turvalliseen säilytykseen. SD Connect -palveluun tallennettua tietoa voidaan käyttää myös SD Desktop -turvallisiin virtuaalipöytiin.

Useimmissa tapauksissa SD Connect -palvelua käytetään [SD Connect -verkkoliittymän](https://sd-connect.csc.fi) kautta, mutta joissakin tapauksissa komentorivityökalut tarjoavat tehokkaamman tavan hallita tietoja SD Connectissa.

Tässä dokumentissa kuvaamme, kuinka voit käyttää [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils) -palvelun tarjoamia a-komentoja tietojen lataamiseen ja lataamiseen SD Connectista. Nämä työkalut ovat saatavilla CSC:n supertietokoneilla (Puhti, Mahti ja Lumi), ja ne voidaan asentaa myös paikallisiin Linux- ja Mac-koneisiin.

Huomaa, että itse Allas ei erottele SD Connectin kanssa tallennettuja tietoja muista Allasiin tallennetuista tiedoista. Tietokontit voivat sisältää sekoituksen SD Connect -tietoa, muuta salattua tietoa ja normaalia tietoa, ja käyttäjän vastuulla on tietää tietojen tyyppi. On kuitenkin todennäköisesti hyvä idea pitää SD Connect -tiedot konteissa ja kansioissa, jotka eivät sisällä muita tietotyyppejä.

## Yhteyden avaaminen SD Connectiin {#opening-connection-to-sd-connect}

SD Connect -yhteensopivan Allas-yhteyden avaamiseksi sinun on lisättävä vaihtoehto *--sdc* konfiguraatiokäskyyn. CSC:n supertietokoneilla yhteys avataan käskyillä:

```bash
module load allas
allas-conf --sdc
```
Paikallisissa asennuksissa yhteys avataan yleensä käskyillä, kuten

```bash
export PATH=/some-local-path/allas-cli-utils:$PATH
source /some-local-path/allas-cli-utils/allas_conf -u your-csc-account --sdc
```

Määrityksessä kysytään ensin CSC-salasanoja (Haka tai Virtu -salasanoja ei voi käyttää täällä). Sen jälkeen valitaan käytettävä CSC-projekti. Tämä on normaali sisäänkirjautumisprosessi Allasille. Kun SD Connect on käytössä, prosessi kysyy sinulta *SD Connect API -tunnuksen*. Tämä tunnus on haettava [SD Connect -verkkoliittymästä](https://sd-connect.csc.fi). Huomaa, että tunnukset ovat projektikohtaisia. Varmista, että olet valinnut saman SD Connect -projektin sekä komentorivillä että verkkoliittymässä.

Verkkoliittymässä tunnus voidaan luoda valitsemalla *Create API tokens* *Support*-valikosta avautuvasta valintaikkunasta.

Kopioi tunnus, liitä se komentoriville ja paina enter.

SD Connect -yhteensopiva Allas-yhteys on nyt voimassa seuraavat kahdeksan tuntia. Voit käyttää käskyjä kuten *a-list* ja *a-delete* hallitaksesi sekä normaaleja Allas-kohteita että SD Connect -kohteita.

## Datan lataaminen {#data-upload}

Dataa voidaan ladata SD Connect -palveluun käyttämällä käskyä *a-put* yhdessä vaihtoehdon *--sdc* kanssa.
Esimerkiksi ladattaessa tiedosto *my-secret-table.csv* sijaintiin *2000123-sens/dataset2* Allasissa käytä käskyä:

```bash
a-put --sdc my-secret-table.csv -b 2000123-sens/dataset2
```

Tämä tuottaa SD Connect -objektin: 2000123-sens/dataset2/my-secret-table.csv.c4gh

Kaikkia muita a-put-vaihtoehtoja ja ominaisuuksia voidaan käyttää myös. Esimerkiksi hakemistot
tallennetaan tar-tiedostoina, ellei --asis -vaihtoehtoa käytetä.

Käsky:

```bash
a-put --sdc my-secret-directory -b 2000123-sens/dataset2
```

Tuottaa SD connect -objektin: 2000123-sens/dataset2/my-secret-directory.tar.c4gh

Massiiviseen datalataukseen voit käyttää *allas-dir-to-bucket* yhdessä vaihtoehdon *--sdc* kanssa.

```bash
allas-dir-to-bucket --sdc my-secret-directory 2000123-new-sens
```

Yllä oleva käsky kopioi kaikki tiedostot hakemistosta my-secret-directory konttiin 2000123-new-sens SD Connect -yhteensopivassa muodossa.

## Datan lataaminen alas {#data-download}

Dataa voidaan ladata Alasista komennolla a-get. Jos SD Connect -yhteys on käytössä, a-get yrittää automaattisesti purkaa objektit, joiden pääte on *.c4gh*.

Joten esimerkiksi komento:

```bash
a-get 2000123-sens/dataset2/my-secret-table.csv.c4gh
```

Tuottaa paikallisen tiedoston: my-secret-table.csv

Ja vastaavasti komento:

```bash
a-get 2000123-sens/dataset2/my-secret-directory.tar.c4gh
```

Tuottaa paikallisen hakemiston: my-secret-directory

Huomaa, että tämä automaattinen purkaminen toimii vain tiedostoille, jotka on tallennettu uuden SD Connectin avulla, joka otettiin käyttöön lokakuussa 2024.

Vanhojen SD Connect -tiedostojen ja muiden Crypt4gh-salattujen tiedostojen kohdalla sinun on edelleen annettava vastaava salainen avain vaihtoehdolla *--sk*

```bash
a-get --sk my-key.sec 2000123-sens/old-date/sample1.txt.c4gh
```

Valitettavasti ei ole helppoa tapaa tietää, mitä salausmenetelmää on käytetty Alasiin tallennetun .c4gh-tiedoston kohdalla.

