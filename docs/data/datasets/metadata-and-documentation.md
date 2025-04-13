
# Metadata ja datadokumentaatio

## Yleiskatsaus

Metadata ja datadokumentaatio ovat tietojen kontekstuaalisia tietoja ja niiden alkuperä, jotka ovat tarpeellisia tietojen ymmärtämiseksi. Tarjoamalla kattavaa metadataa ja dokumentoimalla datan elinkaaren tieteenalasi käytäntöjen mukaisesti teet datastasi ymmärrettävää, löydettävää ja uudelleenkäytettävää.

**Metadata**, eli dataa koskeva data, voi tarkoittaa useita asioita, ja yllä kuvatut dokumentit, jotka selittävät, miten data tulisi tulkita, voidaan myös kutsua metadataksi. Näillä sivuilla käytämme termiä metadata viittaamaan **löytymetadadaan**, datasi 'etikettiin', joka on tarpeen, kun data julkaistaan ja jaetaan.

**Datadokumentaatio** tarkoittaa tiedon luomista, jonka avulla data voidaan tulkita oikein ja itsenäisesti. Se koostuu tiedostoista, jotka selittävät, miten data on luotu tai digitoitu, miten data tulisi tulkita, sen rakenne, ja miten dataa on muokattu. Tätä tietoa voidaan kutsua myös *datan tasoiseksi* dokumentaatioksi tai jopa metadataksi, koska se on tietoa datasta. Datan dokumentoimista tulisi pitää parhaana käytäntönä datanhallinnassa, ja se on myös oleellista datan säilytykselle. Aina kun dataa käytetään, tarvitaan riittävästi kontekstuaalista tietoa datan tulkitsemiseksi oikein ja itsenäisesti.

## Metadatan tyypit

Metadata on dataa koskevaa tietoa, esimerkiksi missä, milloin, miksi ja miten data kerättiin, käsiteltiin ja tulkittiin. Metadata voi myös sisältää tietoja kokeista, analyyttisistä menetelmistä ja tutkimusympäristöistä.

![Löytymetadata. Datadokumentaatio. Data.](../../img/levels-of-openness_v1.png "Löytymetadata. Datadokumentaatio. Data.")

Lisenssi: CC BY 4.0

### Löytymetadata

Löytymetadataa voi olla kolmessa eri tyypissä: Kuvaileva, Hallinnollinen ja Rakenteellinen.

***Kuvaileva metadata***

Datasettin kuvaileva metadata voidaan jakaa kahteen alaluokkaan:

**1) ydinmetadata** *tai tutkimustason metadata* (löytämiseen ja tunnistamiseen - haut ja viittaukset), johon sisältyy:

  * pysyvä tunniste, jota käytetään datasetin siteerauksessa tai uudelleenkäytön raportoinnissa
  * yleistä tietoa datasetistä (otsikko, tieteenala, avainsanat, sisällön kattavuus, muuttujat)
  * tietoa toimijoista (tekijät, avustajat, kustantaja, jakelija)
  * pääsytietoa (latauslinkki tai pääsytiedot ja käyttöoikeuslausunnot)
  * tiedot elinkaaritapahtumista ja niihin liittyvistä entiteeteistä (provenienssi)
  * teknistä tietoa kuten tarkistussumma, koko, tiedostomuoto, mediatyyppi

**2) datadokumentaatio (kutsutaan myös *yksityiskohtaiseksi kuvailevaksi metadataksi* tai datatason metadataksi)** (muuttujien kokoonpanot, työnkulut, käsittelykoodi jne. - arvioinnin ja uudelleenkäytön mahdollistamiseksi). Lisää yksityiskohtaisesta kuvailevasta metadatasta kohdassa [Datadokumentaatio](#data-documentation-also-called-detailed-descriptive-metadata-or-data-level-metadata).

***Hallinnollinen metadata***

Hallinnollinen metadata sisältää tietoa datasetin oikeuksista. Tämä tarkoittaa tietoa lisenssistä, rajoitustyypistä ja sen syistä (eettiset, oikeudelliset jne.), embargo-aikaa, oikeuksien omistajaa, uudelleenkäyttöyhteyttä sekä siitä, miten sovellusta käyttöluvan ja pääsyn saamiseksi.

Muita hallinnollisen metadatan luokkia ovat tekninen metadata (tiedostotyypit jne., tiedot, joita tarvitaan tiedostojen luomiseksi) ja säilytysmetadata.

***Rakenteellinen metadata***

Rakenteellinen metadata kuvaa, miten datasetti on järjestetty sisäisesti ja miten se liittyy muihin datasetteihin (versionhallinta jne.). Joillakin aloilla data julkaistaan ja jaetaan yhteisön hyväksymillä standardeilla ja kaavoilla, jotka ovat muodollisia ja koneellisesti toimintakelpoisia tapoja ilmentää rakenteellista metadataa. Kaavat ilmaisevat tieteellisen alueen, rakenteen, suhteet, kenttämerkit ja parametrien tason standardit datasetin kokonaisuudelle. Kaava mahdollistaa datan jakamisen, yhdistämisen tai siirtämisen tietojärjestelmien välillä merkityksen tai rakenteen menettämättä (ts. data on yhteentoimivaa). Teknisten standardien ja kaavojen toteuttamisen lisäksi yhteentoimivuuden turvaaminen eri datan välillä vaatii julkaistujen semanttisten artefaktien käyttämistä ja niihin viittaamista.

!!! note "Huomautus"

    Voit käyttää [Qvain - Tutkimusdatasetin Metadatatyökalua](https://www.fairdata.fi/en/qvain/) luomaan ydin-, hallinnollisia ja rakenteellisia metatietoja datajoukkoosi.

    Se julkaistaan [Etsin - Tutkimusdatan Löytäjässä](https://www.fairdata.fi/en/services/etsin/).

### Datadokumentaatio (kutsutaan myös *yksityiskohtaiseksi kuvailevaksi metadataksi* tai datatason metadataksi) {#data-documentation-also-called-detailed-descriptive-metadata-or-data-level-metadata}

Jos sinulla on lisämetadataa, joka ei sovi datakatalogiin, lisämetadataa ja **dokumentaatiota** kuten koodikirjoja tai konfiguraatiotiedostoja voi lisätä datasettiin erillisinä tiedostoina. Tämä metadata voi myös olla mukana datatiedostoissa. Muista kuitenkin, että tämä voi tehdä datasta vaikeammin löydettävää. Jos lisäät ylimääräistä metadataa:

1. Käytä metadatastandardeja, jos mahdollista: Varannot vaativat usein tietyn metadatastandardin käyttöä; *strukturoidut muodot, jotka käyttävät tiettyjä sanastoja tai ontologioita kuvatessaan dataa*. Tarkista, onko olemassa tieteenala/yhteisö- tai varantopohjaista metadatakaavaa tai -standardia (eli mieluiten metatietoelementtien joukkoa), joka voidaan ottaa käyttöön. Tieteenalakohtaiset standardit löytyvät [Digital Curation Centre -sivustolta](http://www.dcc.ac.uk/resources/metadata-standards).
    - Jotkut tutkimuslaitteet luovat vakiomuotoisia metadatamuotoja automaattisesti. Valitse standardi, joka on yhteensopiva muiden ohjelmistojen kanssa, jos mahdollista.
2. Käytä erillisiä metatietotiedostoja tai dataan sisältyviä metatietoja, konfiguraatiotiedostoja, lisenssiasiakirjoja, koodikirjoja ja muuta tietoa, joka on tärkeää datan toistamiselle ja uudelleenkäytölle.
    - Readme-tiedosto(t) tarjoavat tietoa datatiedostoista oikean tulkinnan varmistamiseksi
    - Datadictionary / Koodikirja selittävät datan muuttujat ja kerätyt koodit datasarjassa.

Mieti myös tiedostonimikorvauskäytäntöjäsi, hakemistorakennetta ja **versionhallintaa**. Lisää siitä kohdassa [Datan järjestäminen](#data-organization).

!!! note "Datadokumentaatio voidaan tehdä käyttämällä:"
    - (alakohtaisia) metatieto- ja datastandardeja
    - sähköisiä laboratorion muistikirjoja
    - sanastoja ja sanakirjoja
    - readme-tiedostoja 
    
    ja ne kaikki osallistuvat projektidatan ja sen merkityksen selittämiseen.

## Semanttinen yhteentoimivuus ja koneellisesti luettavuus

**Kontrolloidut sanastot, tesaurukset, ja ontologiat** ovat kaikki niin sanottuja semanttisia artefakteja, jotka ovat koneellisesti luettavia tietomalleja. Kun datastandardi ja -kaava ilmaisevat datan rakenteen (elementtien väliset suhteet datassa), semanttiset artefaktit tekevät sisällön merkityksestä yksiselitteistä ja koneelle 'ymmärrettävää' (koneellisesti toimintakelpoista). Esimerkiksi kun keräät tietoa kasveista, voi olla muille ihmislukijoille selvää, että data koskee eläviä organismeja eikä voimalaitoksia ja muita tehtaita, mutta tietokone ei pysty erottamaan eroavaisuutta tulkitsemalla merkitystä kontekstista ihmisten tavoin. Tästä syystä data tulisi toimittaa tai siihen viitata julkisesti saatavilla olevalla sanastolla, joka kertoo koneelle, miten data tulkitaan kontekstissa ja mitä muuttujien arvot tarkoittavat (esimerkiksi ovatko numerot "Asteet"-sarakkeessa Fahrenheit- vai Celsius-asteita). On myös tärkeää kertoa koneelle, tarkoittaako tyhjä kenttä, NULL tai nolla nolla-arvoa vai onko data yksinkertaisesti puuttuvaa. Tämä voi olla ratkaisevaa analyyseille ja tuloksille, jos dataa tulkitaan (väärin) eri tavoin, kun datasetteja uudelleen käytetään tai yhdistetään.

!!! note "Linkit kontrolloituihin sanastoihin, tesauruksiin ja ontologioihin"
    - [Suomalainen Tesaurus- ja Ontologiapalvelu (Finto.fi)](https://finto.fi/en/)
    - [Suomen lajitietokeskus (Laji.fi)](https://laji.fi/en/taxon)
    - [Perusrekisteri tesauruksista, ontologioista & luokituksista (BARTOC)](https://bartoc.org/)
    - [CESSDA-vokabulaaripalvelu](https://vocabularies.cessda.eu/)
    - [Linked Open Vocabularies (LOV)](https://lov.linkeddata.es/dataset/lov)
    - [The Open Biological and Biomedical Ontology (OBO) Foundry](https://obofoundry.org/)
    - [Biolääketieteellisten ontologioiden varasto (BioPortal)](https://bioportal.bioontology.org/)
    - [NERC Sanastopalvelin (NVS)](https://vocab.nerc.ac.uk/)
    - [Research Vocabulary Australia](https://vocabs.ardc.edu.au/)
    - [Merenkulun Metadatan Yhteensopivuus Ontologiavarasto ja -rekisteri (MMI ORR)](https://mmisw.org/)
    - [Industriell Ontologies Foundry (IOF)](https://www.industrialontologies.org/)

<iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="315" srcdoc="https://www.youtube.com/embed/f9m4montnF0" title="FAIRin osatekijät - Yhteentoimivuus" width="560"></iframe>

## Datan järjestäminen {#data-organization}

Hyvässä datanhallinnassa on tärkeää myös huolehtia datan järjestämisestä. Tämä sisältää esimerkiksi harkitut tiedostonimitykset, selkeän kansiorakenteen, helposti saatavilla olevat tiedostomuodot ja selkeä versionhallinta.

On hyvä käytäntö luoda selkeä **tiedostonimitysjärjestelmä** jo projektisi alusta alkaen ja käyttää esimerkiksi samaa järjestelmää tutkimusryhmäsi kanssa. Tämä auttaa sinua sekä kollegoitasi ymmärtämään, mitä tiedostot sisältävät nimestä. Lue vinkkejä siitä, miten järjestät dataasi ja nimeät tiedostoja ja kansioita alla tai [RDMKit järjestämissivulta](https://rdmkit.elixir-europe.org/data_organisation.html).

Tutkimusalallasi voi myös olla ohjeita ja suosituksia datan järjestämiseksi. Aivotutkimusyhteisö, esimerkiksi, on luonut Brain Imaging Data Structure (BIDS), joka määrittelee tiedostomuodot, tiedostojen nimeämissäännöt ja säännöt datan järjestämiseksi hakemistoihin.

### Versionhallinta

Jotta data pysyy hyvin organisoituna, sinun tulisi käyttää **versionhallintajärjestelmää**. Tämä voidaan tehdä joko käsin, jossa lisäät juoksevan numeron tiedostonimen loppuun _(_v03)_, tai automaattisesti, mikä on suositeltavin tapa. Automaattinen versionhallinta voidaan tehdä ohjelmistoilla kuten [Git](https://git-scm.com/), [GitHub](https://github.com/) tai [GitLab](https://gitlab.com/gitlab-org/gitlab) (organisaatiosi saattaa tarjota integroidun ratkaisun) tai käyttää pilvitallennusratkaisuja, jotka yleensä tarjoavat automaattisen tiedostojen versionhallinnan. Lisää vinkkejä datan järjestämiseen löydät [ELIXIRin Tutkimusdatan hallintaoppaasta (RDMkit)](https://rdmkit.elixir-europe.org/).

Kun teet uusia versioita datatiedostoista, on tärkeää **säilyttää kopio alkuperäisistä raakadatoista**. Dataa tulisi säilyttää raaka muodossaan aina kun mahdollista läpinäkyvyyden mahdollistamiseksi ja uudelleenanalyysin helpottamiseksi. Se helpottaa myös useiden tietolähteiden yhdistämistä ja datan uudelleen käytön kohdistamista. Lisäksi, kun jaat datan, voi olla hyödyllistä tarjota sekä käsittelemättömiä että käsiteltyjä versioita datastasi, joko koodin tai selitysten kanssa, miten jälkimmäinen on johdettu. Joissakin tapauksissa voi olla mahdollista jopa julkaista data käsittely- ja analyysikoodin kanssa "suoritettavana paperina" todistamaan, että tieteellinen prosessi on toistettavissa. Toisin sanoen suoritettavat paperit ovat dynaamisia ohjelmistoja, jotka yhdistävät tekstiä, raakadatan ja analyysissa käytetyn koodin, jotka lukija voi olla vuorovaikutuksessa.

!!! note "Lisätietoa toistettavuudesta ja suoritettavista tutkimusartikkeleista:"
    - [Mikä on suoritettava paperi?](https://sozmethode.hypotheses.org/1045)

### Tiedostot ja tiedostomuodot

Kaikki digitaalinen tieto on rakenteellista dataa. **Tiedostomuoto** on standardoitu tapa, jolla tieto koodataan tietokonetiedostoon säilyttämistä varten. **Avoin muoto** on tiedostomuoto digitaalisen datan säilyttämistä varten, määritetty julkistetussa spesifikaatiossa, jota yleensä ylläpitää standardointiorganisaatio, ja jota **kuka tahansa voi käyttää ja toteuttaa**. Toisin kuin avoimet muodot, **suljetut muodot** katsotaan liikesalaisuuksiksi. Esimerkiksi suuri osa kaupallisesta laitteistosta tai ohjelmistoista tuottaa dataa, jota ei voi lukea tai tulkita ilman muita saman toimittajan työkaluja. Organisoitaessa, tallennettaessa ja julkaistaessa tutkimusdataa on tärkeää luoda yhtenäisiä, ymmärrettäviä ja läpinäkyviä kokonaisuuksia, jotka ovat helposti saatavilla ja uudelleenkäytettävissä. Tämä on mahdollista avomuotojen avulla, jotka ovat avoimia ja joita voidaan käyttää myös laajalti käytetyillä avoilla työkaluilla.

**Datan järjestäminen**

- Lajittele ja luokittele tietosi
    - Esimerkiksi, älä sekoita eri tyyppistä tietoa excel-sarakeisiin: on yleensä helpompaa yhdistää datasarjat kuin selvittää huonosti strukturoidun datan jälkeenpäin
- Ajattele granulaatiota (tiedoston kokoa) ja metadataa
- Päätä muodoista, yksiköistä, koodeista jne. ja ole johdonmukainen
    - Käytä yleisiä tiedostomuotoja, mieluiten avoimia
    - Löydät suositeltujen tiedostomuotojen listan digitaalisesta säilytyksestä kertovalta verkkosivustolta. Jos käytät muita muotoja, sinun on mietittävä teknisen dokumentaation liittämistä tiedostomuotoon.
- Kirjoita koodikirja, dokumentti. Lue minut -tiedostoja tarvitaan usein.
- Ajattele ymmärrettävyyttä
- Ole varovainen dataa uudelleenjärjestäessä, uudelleenmuotoillessa, lajitellessa tai kopioitaessa-liittyessä
- Vältä väliaikaisten tai piilotettujen järjestelmä tiedostojen sisällyttämistä yhdessä varsinaisten datatiedostojen kanssa
- Käytä prosesseja datan laadun ja täydellisyyden tarkistamiseksi
- Ole tarkka master-kopioiden ja muiden kopioiden suhteen
- Ole varovainen ja suunnittele hyvin herkkien tietojen ja anonymisoinnin osalta
- Mieti turvallisuutta ja pääsyoikeuksia
- Suunnittele ja sopi, mitkä datasetin versiot arkistoidaan ja/julkaistaan
- Mieti toistettavuutta ja datan siteeraamista

**Tiedostot ja kansiot: jäsentäminen ja nimeäminen**

On tärkeää käyttää aikaa tiedostojen ja kansioiden rakenteiden suunnitteluun ja nimeämiseen.

- Luo ja sopi järjestelmä tiedostojen ja kansioiden nimeämiselle ja ole johdonmukainen
- Yritä organisoida tiedostoja loogisesti kansion ja alakansioiden avulla sen sijaan, että sisällyttäisit kaikki tiedostot yhteen kansioon
    - Vältä erittäin syviä kansiorakenteita, koska niitä voi olla vaikea käsitellä
- Jos datasolu on aikaherkkä ja järjestettu loogisesti ajanjaksojen mukaan, voi olla hyödyllistä järjestää tiedostot aikakohtaisiin kansioihin, kuten VVVV-KK-PP
- Käytä merkityksellisiä, ainutlaatuisia tiedosto- ja kansiomäärittäjiä
- Pidä tiedosto- ja kansiotimääritykset mahdollisimman lyhyinä mutta asiaankuuluvina. 25 merkkiä pidetään yleensä enimmäisrajana.
- Päivämäärät muodossa VVVV-KK-PP mahdollistavat tiedostoselauksen ja haun tekemisen
- Vältä erityismerkkien kuten % & / \ : ; * . ? < > ^! " () ja skandinaavisia kirjaimia
- Käytä kolmea numeroa (tai neljää, jos sinulla on suuri määrä tiedostoja) ts. 001, 002…….201, 202 (ei 1, 2, 21).
- Käytä alaviivoja (_) välilyöntien sijasta
- Jos käytät henkilökohtaista nimeä nimessä, anna sukunimi ensin seurattuna etunimestä
    - Ole hyvin varovainen henkilökohtaisten tietojen kanssa nimeämällä tiedostoja ja kansioita
- Merkitse versionumero käyttämällä 'V' tai 'version'-termiä ja numeroa (ja alipainoksia enemmän numeroita, jos on pieniä muutoksia)

!!! note "Lisälukemista"
    - [The UK Data Service: Muotoile tietosi](https://www.ukdataservice.ac.uk/manage-data/format)
    - [RDMkit: Datan organisaatio](https://rdmkit.elixir-europe.org/data_organisation.html#what-is-the-best-way-to-name-a-file)

<iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="315" srcdoc="https://www.youtube.com/embed/Xkqkg1oiUOQ" title="Hallitse hyvin ja säily - 6. Hallitse tiedostoja ja tiedostojen nimeämistä" width="560"></iframe>

