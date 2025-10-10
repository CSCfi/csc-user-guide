[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# SD Connect -palvelun käyttö a-komennoilla { #using-sd-connect-service-with-a-commands }

SD Connect on osa CSC:n arkaluonteisten tietojen palveluita, jotka tarjoavat maksuttoman käsittely-ympäristön arkaluonteiselle datalle suomalaisissa yliopistoissa ja tutkimuslaitoksissa toteutettaville akateemisille tutkimusprojekteille. SD Connect lisää automaattisen salauskerroksen CSC:n Allas-objektivarastointijärjestelmään, jotta sitä voidaan käyttää arkaluonteisen datan turvalliseen säilyttämiseen. SD Connectiin tallennettuihin tietoihin pääsee käsiksi myös SD Desktop -turvattujen virtuaalityöpöytien kautta. 

Useimmissa tapauksissa SD Connectia käytetään [SD Connect -verkkokäyttöliittymän](https://sd-connect.csc.fi) kautta, mutta joissakin tilanteissa komentorivityökalut tarjoavat tehokkaamman tavan hallita SD Connectissa olevaa dataa.

Tässä dokumentissa kuvataan, miten voit käyttää [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils) -paketin a-komentoja datan lähettämiseen ja noutamiseen SD Connectista. Nämä työkalut ovat käytettävissä CSC:n supertietokoneissa (Puhti, Mahti ja Lumi), ja ne voidaan asentaa myös paikallisiin Linux- ja Mac-koneisiin. 

Huomaa, että Allas ei itsessään erota SD Connectilla tallennettua dataa muusta Allakseen tallennetusta datasta. Databucketeissa voi olla sekaisin SD Connect -dataa, muuta salattua dataa ja tavallista dataa, ja on käyttäjän vastuulla tietää, mitä tyyppiä data on. On kuitenkin todennäköisesti hyvä käytäntö pitää SD Connect -data bucketeissa ja kansioissa, jotka eivät sisällä muuntyyppistä dataa. 


## Yhteyden avaaminen SD Connectiin { #opening-connection-to-sd-connect }

SD Connect -yhteensopivan Allas-yhteyden avaamiseksi sinun on lisättävä valitsin *--sdc* määrityskomennolle. CSC:n supertietokoneissa yhteys avataan komennoilla:

```bash
module load allas
allas-conf --sdc
```
Paikallisissa asennuksissa yhteys avataan tyypillisesti esimerkiksi seuraavilla komennoilla

```bash
export PATH=/some-local-path/allas-cli-utils:$PATH
source /some-local-path/allas-cli-utils/allas_conf -u your-csc-account --sdc
```

Asennusprosessi kysyy ensin CSC-tunnuksesi salasanan (Haka- tai Virtu-salasanoja ei voi käyttää tässä).
Tämän jälkeen valitset käytettävän CSC-projektin. Tämä on Allaksen normaali kirjautumisprosessi.
Kun SD Connect on käytössä, prosessi pyytää lisäksi antamaan *SD Connect API -tunnisteen*. Tunniste haetaan [SD Connect -verkkokäyttöliittymästä](https://sd-connect.csc.fi). Huomaa, että tunnisteet ovat projektikohtaisia. Varmista, että olet valinnut saman SD Connect -projektin sekä komentorivillä että verkkokäyttöliittymässä.

Verkkokäyttöliittymässä tunniste luodaan valitsemalla *Create API tokens* valikosta *Support*, mikä avaa luonti-ikkunan.

Kopioi tunniste, liitä se komentoriville ja paina Enter.

SD Connect -yhteensopiva Allas-yhteys on nyt voimassa seuraavat kahdeksan tuntia. Voit käyttää komentoja kuten
*a-list* ja *a-delete* hallinnoidaksesi sekä tavallisia Allas-objekteja että SD Connect -objekteja.


## Datan lähetys { #data-upload }

Dataa voi lähettää SD Connectiin komennolla *a-put* ja valitsimella *--sdc*.
Esimerkiksi lähettääksesi tiedoston *my-secret-table.csv" sijaintiin *2000123-sens/dataset2* Allaksessa, käytä komentoa:

```bash
a-put --sdc my-secret-table.csv -b 2000123-sens/dataset2
```

Tämä tuottaa SD Connect -objektin: 2000123-sens/dataset2/my-secret-table.csv.c4gh

Kaikkia muitakin *a-put*-komennon valitsimia ja ominaisuuksia voi käyttää. Esimerkiksi hakemistot
tallennetaan tar-tiedostoiksi, ellei --asis-valitsinta käytetä.

Komento: 

```bash
a-put --sdc my-secret-directory -b 2000123-sens/dataset2
```

Tuottaa SD connect -objektin: 2000123-sens/dataset2/my-secret-directory.tar.c4gh

Suuria datamääriä lähettäessä voit käyttää komentoa *allas-dir-to-bucket* yhdessä valitsimen *--sdc* kanssa.

```bash
allas-dir-to-bucket --sdc my-secret-directory  2000123-new-sens
```

Yllä oleva komento kopioi kaikki tiedostot hakemistosta my-secret-directory buckettiin 2000123-new-sens SD Connect -yhteensopivassa muodossa.


## Datan nouto { #data-download }

Dataa voi ladata Allaksesta komennolla *a-get*. Jos SD Connect -yhteys on käytössä, *a-get* yrittää automaattisesti purkaa salauksen objekteista, joiden pääte on *.c4gh*.

Esimerkiksi komento: 

```bash
a-get 2000123-sens/dataset2/my-secret-table.csv.c4gh
```

Tuottaa paikallisen tiedoston: my-secret-table.csv

Ja vastaavasti komento:

```bash
a-get 2000123-sens/dataset2/my-secret-directory.tar.c4gh
```

Tuottaa paikallisen hakemiston: my-secret-directory 

Huomaa, että tämä automaattinen salauksen purku toimii vain niille tiedostoille, jotka on
tallennettu uuden SD Connectin avulla, joka otettiin käyttöön lokakuussa 2024.

Vanhempien SD Connect -tiedostojen ja muiden Crypt4gh-salattujen tiedostojen kohdalla sinun on edelleen
annettava vastaava salainen avain valitsimella *--sk*

```bash
a-get --sk my-key.sec  2000123-sens/old-date/sample1.txt.c4gh
```

Valitettavasti ei ole helppoa tapaa tietää, mitä salaustapaa on käytetty Allakseen tallennetussa .c4gh-tiedostossa.