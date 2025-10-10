[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# FEGA-datan uudelleenkäytön mahdollistaminen { #enabling-reuse-of-fega-data }

CSC:lle tallennettuihin ja kontrolloidun käyttöoikeuden piirissä julkaistuihin datoihin pääsyn hallinnoi SD Apply -palvelussa rekisterinpitäjä tai hänen edustajansa. Jotta Suomen Federated EGA:ssa (FEGA) säilytettyjen aineistojen uudelleenkäyttö olisi mahdollista, sinun on lisättävä organisaatiosi tarjoamat aineistot SD Applyn luetteloon. Huomaa, että kun käytät SD Applyta FEGA:ssa säilytettävien aineistojen käyttöoikeuksien hallintaan, organisaatiollasi on oltava CSC:n kanssa voimassa oleva palvelusopimus. Lue lisää [FEGA:n oikeudellisista sopimuksista](./fega-submission.md#step-1-legal-agreements-data-access-committee-and-policies).

Rekisterinpitäjänä SD Applyssa vastaat seuraavista:

* Aineistojen lisääminen SD Applyn luetteloon yhdessä hakemuslomakkeen ja käytäntöjen kanssa.
* Edustajien (Data Access Committee, DAC) nimeäminen käsittelemään organisaatiosi aineistoihin kohdistuvia käyttöoikeuspyyntöjä.
* Datan käyttöoikeuskäytäntöjen määrittely uudelleenkäyttöä varten.

## Data Access Committee (DAC) -toimikunnan perustaminen { #forming-a-data-access-committee-dac }

Ennen kuin alat lisätä tietoja SD Applyhin, suosittelemme keskustelemaan organisaatiosi sisällä yleisen Data Access Committee (DAC) -toimikunnan perustamisesta, joka hallinnoi pääsyä kaikkiin aineistoihin, joiden rekisterinpitäjänä organisaatiosi toimii. 

DAC vastaa:

- **Uusien FEGA-lähetysten koordinointi ja hyväksyntä organisaation sisällä**: Sen arviointi, mitkä aineistot lähetetään Federated EGAan organisaation nimissä ja rekisterinpitäjänä.
- **Pääsyn hallinta organisaation aineistoihin**: DAC:n hallinnoimiin aineistoihin kohdistuvien käyttöoikeuspyyntöjen arviointi, jotta noudatetaan määriteltyjä käytäntöjä, säädöksiä ja eettisiä ohjeita.

## Aineiston lisääminen SD Applyn luetteloon { #adding-a-dataset-to-catalogue-in-sd-apply }

![SD Apply -infografiikka](https://a3s.fi/docs-files/sensitive-data/SD_Apply/SD_Apply_infographic.png)

Aineistojen lisääminen SD Applyhin ensimmäistä kertaa tehdään tiiviissä yhteistyössä CSC Service Deskin kanssa, koska prosessi voi olla hieman monimutkainen. Varaa aikaa prosessille ja valmistaudu keskustelemaan lakitiimisi kanssa datan uudelleenkäyttöön tarvittavista sopimuksista. Alla on yleiset ohjeet prosessin tueksi.

## Vaiheittainen ohje { #step-by-step-guide }

### 1. Pyydä organisaatioprofiilia { #1-request-for-organization-profile }

Ennen kuin voit lisätä tietoja SD Applyhin, CSC Service Deskin tulee luoda organisaatioprofiili ja asettaa sinut organisaation ylläpitäjäksi. 

1. Lähetä sähköpostia osoitteeseen servicedesk@csc.fi aiheella "SD services" ja pyydä profiilin luontia.
2. Kirjaudu sisään [SD Apply -palveluun](https://sd-apply.csc.fi/).
3. Ilmoita Service Deskille, että olet kirjautunut sisään. Service Desk liittää sinut oikeaan organisaatioon.
4. Service Desk ilmoittaa, kun voit aloittaa aineistojen lisäämisen SD Applyhin. 

!!! note
    Käytä aina samaa tunnistautumispalvelua (Haka/Virtu tai CSC-kirjautuminen) kirjautuessasi SD Applyhin, koska roolisi ja hallinnoimasi aineistot ovat sidottuja kirjautumistunnisteeseesi.

### 2. Lisää aineisto luettelokohteena { #2-add-dataset-as-catalogue-item }

Luettelokohde mahdollistaa hakijalle aineistoosi pääsyn hakemisen. Kun lisäät aineistoja haettavaksi SD Applyn kautta, sinun on ensin luotava:

* **Lomake:** hakijat käyttävät hakemuslomaketta käyttöoikeuden hakemiseen.
* **Käytäntö (valinnainen):** käyttöehdot ja sopimukset, jotka kuvaavat, miten hakijat voivat uudelleenkäyttää dataa.
* **DAC:** Data Access Committee käsittelee hakemukset.
* **Tunniste:** aineiston tekninen tunniste, esimerkiksi DOI.

Sen jälkeen yhdistät nämä kohteet luomalla luettelokohteen. Voit myös käyttää olemassa olevia kohteita uudelleen. 

!!! note
    Sinun on luotava lomake-, käytäntö-, DAC- ja tunniste-kohteet ennen luettelokohteen luomista.

### 2.1. Luo hakemuslomake { #2-1-create-an-application-form }

Rekisterinpitäjä määrittelee, mitä tietoja hakijan on annettava hakemuslomakkeella saadakseen pääsyn dataan.

1. Kirjaudu SD Applyhin ja siirry kohtaan Administration > Forms.
2. Valitse **Create form**.
3. Anna lomakkeelle kuvaava nimi. Nimi näkyy lomakelistassa hakemisen helpottamiseksi, mutta se ei näy hakijalle.
4. Anna lomakkeelle otsikko. Tämä näytetään hakijalle. 
5. Lisää kentät, jotka haluat lomakkeeseen. Esikatselu oikealla näyttää, miltä hakemuslomake näyttää hakijalle. Lomakekenttien vaihtoehdot on selitetty tarkemmin alla.
6. Valitse **Save**, kun olet valmis.

!!! note
    Voit muokata lomaketta vain niin kauan kuin sitä ei ole liitetty luettelokohteeseen.

Voit sisällyttää sopimuksista ne osat, jotka hakijan tulee täyttää, suoraan SD Applyn hakemuslomakkeeseen. Loppu sopimussisällöstä voidaan toimittaa PDF-liitteenä ja lisätä käytännöksi (policy) SD Applyhin, jolloin hakijat voivat tarkistaa ja hyväksyä ehdot sähköisesti pyytäessään pääsyä aineistoon. Näin hakijat voivat täyttää tarvittavat osiot SD Applyssa ja hyväksyä käyttöehdot ilman manuaalista allekirjoitusta. Keskustele tästä mahdollisuudesta organisaatiosi lakitiimin kanssa.

#### Lomakekenttien selitykset { #form-fields-explained }

- **Hakemuksen otsikko**: Käytä tätä kenttää, jos haluat hakijoiden antavan hakemukselleen nimen.
- **Valintalista**: Käytä valintalistaa, jos haluat hakijan valitsevan yhden annetuista vaihtoehdoista. ID-koodi on vaihtoehdon tunniste. Se näkyy esimerkiksi raporteissa, mutta hakija näkee vain selitekentät. Esimerkiksi: Voit asettaa "Y" ID-koodiksi Kyllä-vaihtoehdolle ja "N" Ei-vaihtoehdolle.
- **Monivalintalista**: Käytä monivalintalistaa, jos haluat hakijan voivan valita yhden tai useamman annetuista vaihtoehdoista.
- **Taulukko**: Määritä taulukon sarakkeet. Hakija voi lisätä niin monta riviä kuin haluaa. Kaikki sarakkeet ovat pakollisia jokaisella rivillä. Voit vaatia vähintään yhden rivin täyttämistä.
- **Sähköpostiosoite**: Kenttä validoi hakijan antaman sähköpostiosoitteen.
- **Liite**: Hakija voi lisätä yhden tai useampia liitteitä.
- **Selite**: Käytä selitteitä kuvailevana tekstinä, jos haluat antaa hakijalle lisätietoja, kuten ohjeita, jostakin kentästä.
- **Otsikko**: Harkitse otsikoiden käyttöä, jos haluat jakaa hakemuslomakkeen osiin.
- **Puhelinnumero**: Puhelinnumero kansainvälisessä muodossa (E.164), esim. +14155552671.
- **IP-osoite**: Kenttä validoi hakijan antaman IP-osoitteen IPv4- tai IPv6-muodossa. IP-osoite ei saa kuulua yksityiseen osoiteavaruuteen.

#### Ehdollisten kenttien luominen { #creating-conditional-fields }

Tarvittaessa voit luoda kenttiä, jotka ovat hakijalta piilossa tai näkyvissä hänen vastaustensa perusteella.

Voit esimerkiksi luoda valintalistan "Haluatko lisätä liitteitä?" Kyllä - Ei. Jos hakija valitsee "Kyllä", liitekenttä näytetään hakijalle. Jos hän valitsee "Ei", liitekenttä ei näy.

!!! note
    Ehdolliset kentät toimivat vain Valintalista- ja Monivalintalista-kenttien kanssa.

1. Luo **Valintalista** ja lisää vaihtoehdot.
2. Luo toinen kenttä mitä tahansa kenttätyyppiä.
3. Valitse juuri luomassasi kentässä Additional settings > Visible > Only if.
4. Field: Etsi aiemmin luomasi Valintalista pudotusvalikosta.
5. Has one of the values: Valitse, milloin lista näytetään. Tässä esimerkissä Kenttä 2 "Lisää yksi tai useampi liite" näytetään, jos hakija valitsee "Kyllä"-vaihtoehdon Kentässä 1 "Haluatko lisätä liitteitä?".

Voit testata kenttien toiminnan sivun oikeassa reunassa olevassa esikatselussa.

### 2.2. Luo käytäntö { #2-2-create-a-policy }

Käytännöt määrittävät sopimukset ja käyttöehdot, jotka hakijan on hyväksyttävä voidakseen käyttää dataa. Käytännöt näytetään osana hakemuslomaketta, ja jokaisen käyttöoikeutta hakevan tutkimusryhmän jäsenen on hyväksyttävä käytännöt ennen kuin he voivat käyttää dataa.

Voit luoda kolmen tyyppisiä käytäntöjä:

- **Ulkoinen linkki**: Lisää linkki ulkoiselle sivulle, jolla on käyttöehdot. Käytä linkkejä esimerkiksi silloin, kun lisensoit resurssejasi standardilisensseillä, kuten [Creative Commons](https://creativecommons.org/choose/?lang=en).
- **Upotettu teksti**: Kirjoita käyttöehdot suoraan hakemuslomakkeeseen. Hakija näkee ne normaalina tekstinä hakemuslomakkeessa.
- **Liite**: Lataa tiedosto, jonka hakija voi ladata ja hyväksyä täyttäessään hakemuslomaketta. Suosittelemme PDF-muotoa. Suosittelemme laatimaan liitteen siten, että hakija voi hyväksyä ehdot sähköisesti SD Applyssa.

#### Datan käyttöpolitiikat Suomen Federated EGA:ssa { #data-access-policies-in-the-finnish-federated-ega }

Datan tallettaminen Suomen Federated EGA:han edellyttää sarjaa oikeudellisia sopimuksia: Federated EGA -palvelusopimus sekä Data Access Agreement, joka sisältää Data Transfer Agreement -sopimuksen. 

**Data Access Agreement**: Data Access Agreement (DAA) on sopimus Data Access Committee (DAC) -toimikunnan ja dataa uudelleenkäyttöön hakevan hakijan välillä. DAA:n avulla rekisterinpitäjä voi määritellä datan uudelleenkäytön ehdot ja rajoitukset, mukaan lukien datan käytön, julkaisemisen, lataamisen ja pääsyn säännöt. DAA:n tulisi sisältää myös Data Transfer Agreement (DTA), joka on tarpeen, kun EU/ETA-alueen ulkopuoliset tutkijat käyttävät dataa SD Desktopin kautta. DAA ja DTA sisällytetään SD Applyn käytäntöihin. Lisätietoja saat oman organisaatiosi lakipalveluista. Voit [ladata esimerkkipohjan](https://ega-archive.org/assets/files/Example_DAA.doc), jonka EGA on toimittanut.

Kysy organisaatiosi lakiasiantuntijoilta sopivat datan käyttöpolitiikat tähän tarkoitukseen.  

Käytännöt ovat valinnaisia. Käytäntöä ei voi muokata sen luomisen ja tallentamisen jälkeen.

### 2.3. Luo DAC { #2-3-create-a-dac }

Luomalla DAC:n määrität Data Access Committee (DAC) -toimikunnan jäsenet hakemusten käsittelijöiksi. He hyväksyvät tai hylkäävät organisaatiosi aineistoihin kohdistuvat käyttöoikeuspyynnöt ja saavat ilmoituksia uusista hakemuksista sähköpostitse.

Voit valita kahdesta eri prosessista: oletusprosessi ja päättäjäprosessi. Valitse organisaatiollesi parhaiten soveltuva. Muista antaa DAC:lle kuvaava nimi, jotta löydät sen myöhemmin helpommin.

- **Oletusprosessi**: DAC:n jäsenet vastaavat täysimääräisesti hakemusten hyväksymisestä tai hylkäämisestä. Lisäksi mukana voi olla arvioijia ja päättäjiä. Vain yhden DAC-jäsenen täytyy hyväksyä hakemus. 

- **Päättäjäprosessi**: Oletusprosessin rajoitettu versio. DAC:n jäsenillä ei ole valtuuksia hyväksyä tai hylätä hakemuksia. Heidän on pyydettävä erillistä päättäjäkäyttäjää hyväksymään tai hylkäämään hakemus. 

#### Määritä DAC-jäsenet { #assign-dac-members }

Lisää DAC-jäsenet hakemusten käsittelijöiksi etsimällä käyttäjää käyttäjänimellä tai valitsemalla hänet pudotusvalikosta. Suosittelemme **määrittämään enemmän kuin yhden käsittelijän DAC:iin**, jotta hakemuksia on riittävästi käsittelemässä. 

!!! note
    Löydät **vain sellaiset käsittelijät, jotka ovat aiemmin kirjautuneet SD Applyhin**. Jos et löydä etsimääsi käsittelijää, pyydä häntä kirjautumaan sisään ja yritä uudelleen.

Jos haluat piilottaa hakemusten käsittelijöiden (DAC, arvioijat, päättäjät) nimet hakijalta, valitse valintaruutu *Anonymized handling*.

DAC:n jäsenille ei lähetetä ilmoitusta silloin, kun heidät on lisätty käsittelijöiksi, mutta he saavat sähköposteja uusista hakemuksista.

#### Lisää lomake DAC:iin { #add-a-form-to-a-dac }

Jos tiedät, että kaikki organisaatiosi SD Applyssa hallinnoimat aineistot käyttävät samaa hakemuslomaketta, voit liittää luomasi lomakkeen DAC:iin valitsemalla sen pudotusvalikosta.  

Jos haluat kysyä hakijalta aineistokohtaisia kysymyksiä, voit luoda kaksi hakemuslomaketta ja liittää yleiset kysymykset sisältävän lomakkeen DAC:iin ja aineistokohtaiset kysymykset sisältävän lomakkeen luettelokohteeseen. Tällöin hakija näkee hakemuksen kahtena osana ja täyttää molemmat.

#### Lisää käytäntö DAC:iin { #add-a-policy-to-a-dac }

Jos tiedät, että kaikilla organisaatiosi SD Applyssa hallinnoimilla aineistoilla on samat käyttöehdot ja sopimukset, voit liittää luomasi käytännöt DAC:iin valitsemalla ne pudotusvalikosta.

Valitettavasti meillä on tällä hetkellä tekninen rajoitus, jonka vuoksi PDF-liitteiden maksimikoko on 1 MB. **Optimoi PDF-tiedostosi ennen kuin lisäät sen SD Applyhin**.  

Tällä tavalla nämä käytännöt lisätään automaattisesti kaikkiin luettelokohteisiin, joissa käytetään samaa DAC:ia. Voit myös lisätä aineistokohtaiset käyttöehdot liittämällä käytännön tunnisteeseen.

### 2.4. Luo tunniste { #2-4-create-a-identifier }

Kun tutkija toimittaa dataa Federated EGA:han, hän saa aineistolleen yksilöllisen tunnisteen, esimerkiksi EGAD12345. Jotta aineisto olisi haettavissa uudelleenkäyttöön SD Applyn kautta, FEGA-lähettäjän tulee toimittaa tämä tunniste rekisterinpitäjälle, jotta se voidaan lisätä SD Applyhin. 

1. Lisää FEGA-lähettäjän toimittama tunniste tunniste-kenttään. 
2. Valitse käytännöt, jotka haluat liittää tunnisteeseen, valitsemalla luomasi käytännöt pudotusvalikosta. Käytännöt ovat valinnaisia.

!!! note
    Et voi muokata tunnistetta sen luomisen ja tallentamisen jälkeen. Jos haluat muuttaa jotakin tunnisteen luomisen jälkeen, luo uusi tunniste ja arkistoi vanha.

### 2.5. Luo luettelokohde { #2-5-create-a-catalogue-item }

Luettelokohde yhdistää luomasi kohteet yhdeksi aineistoksi, johon hakija voi hakea käyttöoikeutta. 

1. Anna otsikkokenttään aineistoa kuvaava nimi. Se helpottaa hakijoita tunnistamaan, mihin aineistoon he haluavat hakea pääsyä.
2. Jos aineistosta on lisätietoja toisella verkkosivulla, voit lisätä linkin More info -kenttään.
3. Valitse luomasi DAC DAC-pudotusvalikosta.
4. Valitse SD Applyhin lisättävän aineiston tunniste tunnisteen pudotusvalikosta.
5. Jos et liittänyt lomaketta DAC:iin, valitse luomasi hakemuslomake pudotusvalikosta.
6. Valitse kategoriaksi FEGA.
7. **Ota luettelokohde käyttöön, jotta se näkyy hakijoille**. Luettelokohde on aluksi poistettu käytöstä, eikä kukaan voi hakea siihen pääsyä ennen sen käyttöönottoa. Kun otat luettelokohteen käyttöön, se näkyy aineistona Catalogue-sivulla.

#### Luettelokohteiden muokkaaminen { #editing-catalogue-items }

Voit muokata luettelokohteen nimeä, organisaatiota ja lisätietolinkkejä valitsemalla Muokkaa.

!!! note
    Tallennuksen jälkeen et voi muokata luettelokohteeseen liitettyä lomaketta, DAC:ia tai tunnistetta. Muokkaus ei myöskään ole mahdollista, kun jokin luettelokohteen osa on poistettu käytöstä.

Jos haluat muuttaa yhden tai useamman luettelokohteen hakemuslomaketta ja/tai DAC:ia, valitse muokattavat luettelokohteet valintaruudulla ja valitse **Update catalogue item**.

Tämä **poistaa käytöstä ja arkistoi vanhan luettelokohteen** ja luo uuden päivitetyn luettelokohteen. Tämä tarkoittaa, että hakijat eivät enää näe vanhaa luettelokohdetta eivätkä voi hakea siihen pääsyä.

## Lisää aineistoja organisaatiosi alle { #adding-more-datasets-under-your-organisation }

Kun olet kerran luonut lomakkeen, tarvittavat käytännöt ja DAC:n, voit käyttää näitä kohteita uudelleen tulevissa aineistolisäyksissä, jos aineistoilla on sama DAC.

Uuden aineiston lisääminen SD Applyn luetteloon samalla DAC:illa:

1. Luo uusi **tunniste**. FEGA-lähettäjän tulee toimittaa sinulle aineistonsa yksilöllinen tunniste. 
2. Luo **luettelokohde** yhdistämällä aiemmin luomasi kohteet (tunniste, lomake, DAC).
3. Ota luettelokohde käyttöön, jotta se näkyy hakijoille.

Varmista, että tarvittavat sopimukset on liitetty joko käyttämääsi DAC:iin tai jokaiseen SD Applyhin lisäämääsi uuteen tunnisteeseen.

## Kohteiden poistaminen käytöstä ja arkistointi { #disabling-and-archiving-items }

Voit poistaa käytöstä ja arkistoida kaikki kohteet. Poistaminen ei ole mahdollista, koska haluamme tarjota täyden tapahtumahistorian tietoturvasyistä.

### Kohteiden poistaminen käytöstä { #disabling-items }

Kun poistat kohteen, esimerkiksi lomakkeen, käytöstä, sitä **ei voi enää käyttää uusissa luettelokohteissa**. Käytöstä poistetut kohteet piilotetaan pudotusvalikoista.

**Jos poistat luettelokohteen käytöstä**, hakija ei voi enää hakea siihen pääsyä. Jos hakija on kuitenkin hakenut pääsyä luettelokohteeseen ennen käytöstä poistamista, käsittelijä voi edelleen viedä hakemuksen käsittelyn loppuun ja hyväksyä tai hylätä hakemuksen.

Voit ottaa käytöstä poistetut kohteet uudelleen käyttöön.

### Arkistointi { #archiving }

Arkistointi **piilottaa kohteen hallintanäkymästä ja hakijoilta**. Jos haluat tarkastella arkistoituja kohteita, valitse **Display archived**. Suosittelemme arkistoimaan vanhat kohteet, jotka eivät ole enää käytössä.

Voit poistaa kohteiden arkistoinnin.

Käsittelijöille näytetään varoitus, jos luettelokohde, johon hakija on hakenut pääsyä, on poistettu käytöstä tai arkistoitu. 

## Tuki { #support }

Jos sinulla on kysyttävää SD Applyn käytöstä, ota yhteyttä [CSC Service Deskiin](../../support/contact.md) (aihe: SD Apply).