# FEGA-tietojen uudelleenkäytön mahdollistaminen {#enabling-reuse-of-fega-data}

CSC:ssä tallennetun ja valvotun saatavuuden alaisena julkaistun datan käyttöoikeutta hallinnoi rekisterinpitäjä tai heidän edustajansa SD Apply -palvelussa. Jotta voit mahdollistaa FEGA:an (Finnish Federated EGA) tallennettujen tietokokonaisuuksien uudelleenkäytön, sinun tulee lisätä organisaatiosi tarjoamat tietokokonaisuudet SD Apply -katalogiin. Huomioithan, että jos käytät SD Apply -palvelua hallitaksesi FEGA:an tallennettujen tietokokonaisuuksien käyttöoikeuksia, organisaatiollasi tulee olla palvelusopimus CSC:n kanssa. Lue lisää [FEGA:n oikeudellisista sopimuksista](./fega-submission.md#step-1-legal-agreements-data-access-committee-and-policies).

Rekisterinpitäjänä SD Apply -palvelussa olet vastuussa:

* Tietokokonaisuuksien lisäämisestä SD Apply -katalogiin hakemuslomakkeen ja käytäntöjen kanssa.
* Edustajien (Data Access Committee, DAC) nimeämisestä, jotka hallinnoivat käyttöoikeuspyyntöjä organisaatiosi tietokokonaisuuksiin.
* Datan uudelleenkäyttökäytäntöjen määrittelemisestä.

## Tietosuojatoimikunnan (DAC) muodostaminen {#forming-a-data-access-committee-dac}

Ennen kuin alat lisätä tietoja SD Apply -palveluun, suosittelemme keskustelemaan organisaatiossasi yleisen tietosuojatoimikunnan (DAC) muodostamisen mahdollisuudesta, joka hallinnoi pääsyä kaikkiin tietokokonaisuuksiin, joiden rekisterinpitäjä organisaatiosi on.

DAC on vastuussa:

- **Uusien FEGA-lähetysten koordinoinnista ja hyväksynnästä organisaationsa sisällä**: Tarkastamalla tietokokonaisuudet, jotka lähetetään Federated EGA:an organisaationsa hallinnassa.
- **Organisaation tietokokonaisuuksien käyttöoikeuksien hallinnasta**: Arvioimalla DAC:n hallinnoimien tietokokonaisuuksien käyttöoikeuspyyntöjä varmistaakseen määriteltyjen käytäntöjen, määräysten ja eettisten ohjeiden noudattamisen.

## Tietokokonaisuuden lisääminen SD Apply -katalogiin {#adding-a-dataset-to-catalogue-in-sd-apply}

![SD Apply Infograph](https://a3s.fi/docs-files/sensitive-data/SD_Apply/SD_Apply_infographic.png)

Tietokokonaisuuksien lisääminen SD Apply -palveluun ensimmäistä kertaa tapahtuu läheisessä yhteistyössä CSC:n Service Deskin kanssa, koska prosessi voi olla hieman monimutkainen. Varaa aikaa prosessille ja valmistaudu keskustelemaan oikeudellisen tiimisi kanssa tietojen uudelleenkäyttöön tarvittavista sopimuksista. Alla on yleisiä ohjeita, jotka ohjaavat sinua prosessin läpi.

## Vaiheittainen opas {#step-by-step-guide}

### 1. Pyydä organisaatioprofiilia {#request-for-organization-profile}

Ennen kuin voit lisätä tietoja SD Apply -palveluun, CSC Service Desk luo organisaatioprofiilin ja asettaa sinut organisaation ylläpitäjäksi.

1. Lähetä sähköpostia osoitteeseen servicedesk@csc.fi aiheenaan "SD services" pyytääksesi profiilin luomista.
2. Kirjaudu [SD Apply -palveluun](https://sd-apply.csc.fi/).
3. Ilmoita Service Deskille, että olet kirjautunut sisään. Service Desk lisää sinut oikeaan organisaatioon.
4. Service Desk ilmoittaa sinulle, kun voit aloittaa tietokokonaisuuksien lisäämisen SD Apply -palveluun. 

!!! huomautus
    Käytä aina samaa identiteetin tarjoajaa (Haka/Virtu tai CSC-tunnus) kirjauduttaessa SD Apply -palveluun, koska roolisi ja hallinnoimasi tietokokonaisuudet ovat yhteydessä kirjautumisidentiteettiisi.

### 2. Lisää tietokokonaisuus katalogiesineeksi {#add-dataset-as-catalogue-item}

Katalogiesine mahdollistaa hakijan hakea käyttöoikeutta tietokokonaisuuteesi. Kun lisäät tietokokonaisuuksia SD Apply -palveluun haettavaksi, sinun tulee ensin luoda:

* **Lomake:** hakijat käyttävät hakemuslomaketta hakeakseen käyttöoikeuksia.
* **Käytäntö (valinnainen):** Datan käyttöoikeussopimukset, jotka kuvaavat, miten hakijat voivat käyttää uudelleen dataa.
* **DAC:** Tietosuojatoimikunta käsittelee hakemuksia.
* **Tunniste:** tekninen tunniste tietokokonaisuudelle, esimerkiksi DOI.

Sitten yhdistät nämä kohteet luomalla katalogiesineen. Voit myös käyttää uudelleen olemassa olevia kohteita.

!!! huomautus
    Sinun on luotava lomake, käytäntö, DAC ja tunniste **ennen** kuin luot katalogiesineen.

### 2.1. Luo hakemuslomake {#create-an-application-form}

Rekisterinpitäjä määrittelee, mitä tietoja hakijan on annettava hakemuslomakkeessa saadakseen pääsyn dataan.

1. Kirjaudu SD Apply -palveluun ja siirry kohtaan Administration > Forms.
2. Valitse **Create form**.
3. Anna lomakkeelle kuvaileva nimi. Nimi näkyy lomakeluettelossa auttamaan sen löytämisessä, mutta sitä ei näytetä hakijalle.
4. Anna lomakkeelle otsikko. Tämä näytetään hakijalle. 
5. Lisää kenttiä, jotka haluat sisällyttää hakemukseen. Esikatselu oikealla puolella näyttää, miten hakija näkisi hakemuslomakkeen. Lomakkeen kenttävalinnat selitetään tarkemmin alla.
6. Valitse **Tallenna**, kun olet valmis lomakkeen kanssa.

!!! huomautus
    Voit muokata lomaketta vain niin kauan kuin sitä ei ole yhdistetty katalogiesineeseen.

Voit sisällyttää sopimusten osat, jotka on täytettävä suoraan SD Apply -hakemuslomakkeeseen. Loppusopimuksen sisältö voidaan toimittaa PDF-liitteenä ja lisätä käytännöksi SD Apply -palveluun, jolloin hakijat voivat tarkistaa ja hyväksyä ehdot sähköisesti pyytäessään pääsyä tietokokonaisuuteen. Tällä tavalla hakijat voivat täyttää tarvittavat osiot SD Apply -palvelun sisällä ja hyväksyä käyttöehdot ilman paperien manuaalista allekirjoittamista. Keskustele tästä mahdollisuudesta organisaatiosi oikeudellisen tiimin kanssa.

#### Lomakekenttien selitykset {#form-fields-explained}

- **Hakemuksen otsikko**: Käytä tätä kenttää, jos haluat hakijoiden antavan hakemukselleen nimen.
- **Vaihtoehtolista**: Käytä vaihtoehtolistaa, jos haluat hakijan valitsevan yhden annetuistä vaihtoehdoista. ID-koodi on vaihtoehdon tunniste. Se näytetään esimerkiksi raporteissa, mutta hakija näkee vain etikettikentän. Esimerkiksi: Voit laittaa "Y" ID-koodiksi kyllä-vaihtoehdolle ja "N" ei-vaihtoehdolle.
- **Monivalintalista**: Käytä monivalintalistaa, jos haluat hakijan valitsevan yhden tai useamman annetuista vaihtoehdoista.
- **Taulukko**: Tarjoa sarakkeiden joukko taulukolle. Hakija voi lisätä niin monta riviä kuin haluaa. Kaikki sarakkeet ovat pakollisia jokaiselle riville. Voit vaatia hakijaa täyttämään vähintään yhden rivin.
- **Sähköpostiosoite**: Sähköpostiosoitekenttä tarkistaa hakijan antaman sähköpostiosoitteen.
- **Liite**: Hakija voi lisätä yhden tai useamman liitteen.
- **Etiketti**: Käytä etikettejä kuvaavin teksteinä, jos haluat antaa hakijalle lisätietoja, kuten ohjeita jostakin kentästä.
- **Otsikko**: Harkitse otsikoiden käyttämistä, jos haluat jakaa hakemuslomakkeen osioihin.
- **Puhelinnumero**: Puhelinnumero kansainvälisessä muodossa (E.164), esimerkiksi +14155552671.
- **IP-osoite**: IP-osoitekenttä tarkistaa hakijan antaman IP-osoitteen IPv4- tai IPv6-muodoissa. IP-osoite ei saa kuulua tunnettuun yksityiseen alueeseen.

#### Ehdollisten kenttien luominen {#creating-conditional-fields}

Tarvittaessa voit luoda kenttiä, jotka ovat piilotettuja tai näkyvät hakijalle riippuen heidän vastauksistaan.

Esimerkiksi voit luoda vaihtoehtolistan "Haluatko lisätä liitteitä?" Kyllä - Ei. Jos hakija valitsee "Kyllä", liitekenttä näytetään hakijalle. Jos he valitsevat "Ei", he eivät näe liitekenttää.

!!! huomautus
    Ehdolliset kentät toimivat vain vaihtoehto- ja monivalintakenttien kanssa.

1. Luo **Vaihtoehto** ja täytä vaihtoehdot
2. Luo toinen kenttä mistä tahansa kenttätyypistä.
3. Valitse juuri luomassasi kentässä Lisäasetukset > Näkyvä > Vain jos
4. Kenttä: Etsi aiemmin luomasi vaihtoehtolista pudotusvalikosta
5. Sisältää yhden arvoista: Valitse, milloin haluat kentän olevan näkyvissä. Tässä esimerkissä Kenttä 2 "Lisää yksi tai useampi liite" näytetään, jos hakija valitsee "Kyllä"-vaihtoehdon Kenttä 1:stä, "Haluatko lisätä liitteitä?".

Voit testata kuinka kentät toimivat esikatseluosiossa sivun oikealla puolella.

### 2.2. Luo käytäntö {#create-a-policy}

Käytännöt määrittelevät sopimukset ja käyttöehdot, jotka hakijan on hyväksyttävä voidakseen käyttää dataa. Käytännöt näytetään osana hakemuslomaketta ja jokaisen tutkimusryhmän jäsenen, joka hakee käyttöoikeutta, on hyväksyttävä käytännöt ennen kuin he voivat käyttää dataa.

Voit luoda kolmea erilaista käytäntöä:

- **Ulkoinen linkki**: Tarjoa linkki ulkoiselle sivulle käyttöehdoilla. Käytä linkkejä esimerkiksi, jos haluat lisensoida resurssejasi standardisoiduilla lisensseillä, kuten [Creative Commons](https://creativecommons.org/choose/?lang=fi).
- **Sisäinen teksti**: Kirjoita käyttöehdot hakemuslomakkeeseen. Hakija näkee sen normaalina tekstinä lomakkeessa.
- **Liite**: Tallenna tiedosto, jonka hakija voi ladata ja hyväksyä, kun hän täyttää hakemuslomakkeen. Suosittelemme PDF-muodon käyttöä. Suosittelemme laatimaan politiikkaliitteet siten, että hakija voi hyväksyä ne sähköisesti SD Apply -palvelussa hyväksymällä käyttöehdot.

#### Datan käyttöoikeuskäytännöt Finnish Federated EGA:ssa {#data-access-policies-in-the-finnish-federated-ega}

Tietojen siirto Finnish Federated EGA:han vaatii joukon oikeudellisia sopimuksia: palvelusopimus Federated EGA:lle ja datan käyttöoikeussopimus, mukaan lukien datan siirtosopimus.

**Data Access Agreement**: Data Access Agreement (DAA) on sopimus tietosuojatoimikunnan (DAC) ja hakijan välillä, joka hakee käyttöoikeutta datan uudelleenkäyttöä varten. DAA:n kautta rekisterinpitäjä voi määritellä ehdot ja rajoitukset datan uudelleenkäytölle, mukaan lukien datan käytön, julkaisun, latauksen ja käyttöoikeuden hallinnointia koskevat käytännöt. DAA:n tulisi myös sisältää Data Transfer Agreement (DTA), joka on tarpeen, kun tutkijat EU/ETA:n ulkopuolisilta alueilta käyttävät dataa SD Desktopin kautta. DAA ja DTA sisällytetään SD Apply -palvelun politiikoihin. Lisätietoja saat ottamalla yhteyttä kotiorganisaatiosi oikeudellisiin palveluihin. Voit [ladata esimerkkimallin](https://ega-archive.org/assets/files/Example_DAA.doc), jonka EGA on tarjoanut.

Konsultoi organisaatiosi oikeudellisia asiantuntijoita määrittääksesi sopivat datan käyttöoikeuskäytännöt tähän tarkoitukseen.

Käytännöt ovat valinnaisia. Et voi muokata käytäntöä sen luomisen ja tallentamisen jälkeen.

### 2.3. Luo DAC {#create-a-dac}

Luomalla DAC:n asetat tietosuojatoimikunnan (DAC) jäsenet hakemuskäsittelijöiksi. He hyväksyvät tai hylkäävät datahaun tietokokonaisuuksien käyttöoikeuspyynnöt ja saavat sähköposti-ilmoitukset uusista hakemuksista.

Voit valita kahden eri prosessin välillä: dynaaminen prosessi ja päätösprosessi. Valitse organisaatiollesi parhaiten sopiva. Muista antaa DAC:lle kuvaileva nimi, jotta löydät sen helpommin myöhemmin.

- **Oletusprosessi**: DAC-jäsenet vastaavat täysin hakemusten hyväksymisestä tai hylkäämisestä. Lisäksi voi olla arvioijia ja päättäjiä. Vain yhden DAC-jäsenen on hyväksyttävä hakemus.

- **Päättäjäprosessi**: Oletusprosessin rajoitettu versio. DAC-jäsenillä ei ole valtuuksia hyväksyä tai hylätä hakemuksia. Heidän on pyydettävä erillistä päättäjäkäyttäjää hyväksymään tai hylkäämään hakemus.

#### DAC-jäsenten nimeäminen {#assign-dac-members}

Lisää DAC-jäsenet hakemuksen käsittelijöiksi etsimällä käyttäjää käyttäjänimellä tai valitsemalla sen pudotusvalikosta. Suosittelemme **nimittämään enemmän kuin yhden käsittelijän DAC:lle** varmistaaksesi, että hakemuksia käsittelemään on tarpeeksi käsittelijöitä.

!!! huomautus
    Voit **löytää vain ne käsittelijät, jotka ovat kirjautuneet SD Apply -palveluun**. Jos et löydä etsimääsi käsittelijää, pyydä häntä kirjautumaan sisään ja yritä uudelleen.

Jos haluat piilottaa hakemuksen käsittelijöiden (DAC, arvioijat, päättäjät) nimet hakijalta, valitse valintaruutu *Anonymized handling*.

DAC-jäsenet eivät saa ilmoitusta, kun heidät on nimetty käsittelijäksi, mutta he saavat sähköpostia uusista hakemuksista.

#### Lisää lomake DAC:lle {#add-a-form-to-a-dac}

Jos tiedät, että kaikki organisaatiosi hallinnoimat tietokokonaisuudet SD Apply -palvelussa käyttävät samaa hakemuslomaketta, voit yhdistää luomasi lomakkeen DAC:llä valitsemalla lomakkeen pudotusvalikosta.

Jos haluat esittää tietokokonaisuuskohtaisia kysymyksiä hakijalta, voit luoda kaksi hakemuslomaketta ja yhdistää yleisiä kysymyksiä sisältävän lomakkeen DAC:lle ja toisen tietokokonaisuuskohtaisia kysymyksiä sisältävän lomakkeen katalogiesineelle. Tällöin hakija näkee hakemuslomakkeet kahdessa osassa ja täyttää molemmat lomakkeet.

#### Lisää käytäntö DAC:lle {#add-a-policy-to-a-dac}

Jos tiedät, että kaikilla organisaatiosi SD Apply -palvelussa hallinnoimilla tietokokonaisuuksilla on samat käyttöehdot ja sopimukset, voit yhdistää luomasi käytännöt DAC:lle valitsemalla ne pudotusvalikosta.

Valitettavasti meillä on tällä hetkellä tekninen rajoitus PDF-liitteiden kokoon, joka on 1 MB. **Ole hyvä ja optimoi PDF-tiedostosi ennen lisäämistä SD Apply -palveluun**.

Tällä tavoin nämä käytännöt lisätään automaattisesti kaikkiin katalogiesineisiin, jotka käyttävät samaa DAC:ta. Voit myös lisätä tietokokonaisuuskohtaisia käyttöehtoja yhdistämällä käytännön tunnisteeseen.

### 2.4. Luo tunniste {#create-a-identifier}

Kun tutkija lähettää tietoja Federated EGA:lle, hän saa yksilöllisen tunnisteen tietokokonaisuudelleen, esimerkiksi EGAD12345. Jotta tietokokonaisuus olisi saatavilla uudelleenkäyttöön SD Apply -palvelussa, FEGA-lähettäjän tulisi lähettää tämä tunniste rekisterinpitäjälle, jotta se voidaan lisätä SD Apply -palveluun.

1. Lisää tunniste, jonka FEGA-lähettäjä on antanut sinulle tunnistekenttään.
2. Valitse käytännöt, jotka haluat liittää tunnisteeseesi, valitsemalla luomasi käytännöt pudotusvalikosta. Käytännöt ovat valinnaisia.

!!! huomautus
    Et voi muokata tunnistetta sen luomisen ja tallentamisen jälkeen. Jos haluat muuttaa jotain tunnisteen luomisen jälkeen, sinun tulee luoda uusi tunniste ja arkistoida vanha.

### 2.5. Luo katalogiesine {#create-a-catalogue-item}

Katalogiesine yhdistää luomasi kohteet yhdeksi tietokokonaisuudeksi, johon hakija voi hakea käyttöoikeutta.

1. Kirjoita kuvaileva nimi tietokokonaisuudelle otsikkokenttään. Se helpottaa hakijan tunnistamista, mihin tietokokonaisuuteen he haluavat hakea käyttöoikeutta.
2. Jos tietokokonaisuudesta on lisätietoja toisella verkkosivulla, voit lisätä linkin *Lisätietoa*-kenttään.
3. Valitse luomasi DAC pudotusvalikosta.
4. Valitse tunniste haluamallesi tietokokonaisuudelle SD Apply -palveluun tunnisteen pudotusvalikosta.
5. Jos et yhdistänyt lomaketta DAC:lle, valitse luomasi hakemuslomake pudotusvalikosta.
6. Valitse kategoriaksi FEGA.
7. **Ota katalogiesine käyttöön, jotta se näkyy hakijoille**. Katalogiesine on alun perin poistettu käytöstä, joten kukaan ei voi hakea siihen käyttöoikeutta ennen kuin se otetaan käyttöön. Kun olet ottanut käyttöön katalogiesineen, se näytetään tietokokonaisuutena Katalogisivulla.

#### Katalogiesineiden muokkaus {#editing-catalogue-items}

Voit muokata katalogiesineen nimeä, organisaatiota ja lisätietolinkkejä valitsemalla muokkaa.

!!! huomautus
    Tallentamisen jälkeen et voi muokata katalogiesineeseen yhdistettyä lomaketta, DAC:ta tai tunnistetta. Muokkaaminen ei myöskään ole mahdollista, kun jokin osa katalogiesineestä on poistettu käytöstä.

Jos haluat muuttaa yhden tai useamman katalogiesineiden hakemuslomaketta ja/tai DAC:ta, valitse muokattavat katalogiesineet klikkaamalla valintaruutua ja valitse sitten **Päivitä katalogiesine**.

Tämä **poistaa käytöstä ja arkistoi vanhan katalogiesineen** ja luo uuden päivitetyn katalogiesineen. Tämä tarkoittaa, että hakijat eivät näe tai hae pääsyä vanhaan katalogiesineeseen enää.

## Lisää tietokokonaisuuksia organisaatiosi alle {#adding-more-datasets-under-your-organisation}

Kun olet kerran luonut lomakkeen, tarvittavat käytännöt ja DAC:n, voit käyttää näitä kohteita uudelleen tulevissa tietokokonaisuuksien lähetyksissä, jos tietokokonaisuuksilla on sama DAC.

Lisää uusi tietokokonaisuus SD Apply -katalogiin samalla DAC:lla:

1. Luo uusi **tunniste**. FEGA-lähettäjän tulisi toimittaa sinulle yksilöllinen tunniste tietokokonaisuudelleen.
2. Luo **katalogiesine** yhdistämällä aiemmin luomasi kohteet (tunniste, lomake, DAC)
3. Ota katalogiesine käyttöön, jotta se näkyy hakijoille.

Varmista, että tarvittavat sopimukset on joko yhdistetty käyttämääsi DAC:iin tai jokaiseen uuteen tunnisteeseen, jonka lisäät SD Apply -palveluun.

## Kohteiden poistaminen käytöstä ja arkistointi {#disabling-and-arching-items}

Voit poistaa käytöstä ja arkistoida kaikki kohteet. Poistaminen ei ole mahdollista, koska haluamme tarjota täyden tapahtumahistorian tietoturvasyistä.

### Kohteiden poistaminen käytöstä {#disabling-items}

Kun poistat kohteen, esimerkiksi lomakkeen, käytöstä, sitä **ei voi enää käyttää uusissa katalogiesineissä**. Poistetut kohteet piilotetaan pudotusvalikoista.

**Jos poistat käytöstä katalogiesineen**, hakija ei voi enää hakea siihen käyttöoikeutta. Jos hakija on kuitenkin hakenut katalogiesineeseen käyttöoikeutta ennen poistamista, käsittelijä voi silti viimeistellä hakemusprosessin hyväksymällä tai hylkäämällä hakemuksen.

Voit ottaa poistetut kohteet uudelleen käyttöön.

### Arkistointi {#archiving}

Arkistointi **piilottaa kohteen hallintanäkymästä ja hakijoilta**. Jos haluat tarkastella arkistoituja kohteita, valitse **Näytä arkistoidut**. Suosittelemme arkistoimaan vanhat, ei enää käytössä olevat kohteet.

Voit poistaa arkistoinnin arkistoiduilta kohteilta.

Käsittelijöille ilmoitetaan, jos katalogiesine, johon hakija on hakenut käyttöoikeutta, on poistettu käytöstä tai arkistoitu.

## Tuki {#support}

Jos sinulla on kysyttävää SD Apply -palvelun käytöstä, ota yhteyttä [CSC Service Deskiin](../../support/contact.md) (aihe: SD Apply).