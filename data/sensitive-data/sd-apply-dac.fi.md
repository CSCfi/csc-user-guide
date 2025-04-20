# Mahdollistetaan FEGA-datan uudelleenkäyttö {#enabling-reuse-of-fega-data}

CSC:lle tallennettujen ja valvotun käyttöoikeuden piirissä julkaistujen aineistojen käyttöoikeuksia hallinnoi rekisterinpitäjä tai tämän edustajat SD Apply -palvelussa. Jotta Suomen Federaalisen EGA:n (FEGA) kautta tallennetut aineistot voidaan uudelleenkäyttää, sinun tulee lisätä organisaatiosi tarjoamat aineistot SD Applyn katalogiin. Huomioithan, että kun käytät SD Applyta FEGA:ssa tallennettujen aineistojen käytön hallintaan, organisaatiollasi tulee olla palvelusopimus CSC:n kanssa. Lue lisää [FEGA:n juridisista sopimuksista](./fega-submission.md#step-1-legal-agreements-data-access-committee-and-policies).

SD Applyn rekisterinpitäjänä olet vastuussa seuraavista:

* Lisäämällä aineistosi SD Applyn katalogiin yhdessä hakulomakkeen ja ehtojen kanssa.
* Nimeämällä edustajat (Data Access Committee, DAC), jotka käsittelevät organisaatiosi aineistojen käyttöoikeushakemuksia.
* Määrittelemällä datan käyttöehdot ja periaatteet uudelleenkäytölle.

## Data Access Committee (DAC) -toimikunnan muodostaminen {#forming-a-data-access-committee-dac}

Ennen kuin alat lisätä tietoja SD Applyhin, suosittelemme organisaatiosi sisällä keskustelua yleisen Data Access Committee (DAC) -toimikunnan perustamisesta, joka hallinnoi käyttöoikeuksia kaikkiin organisaatiosi rekisterinpitäjänä oleviin aineistoihin.

DAC on vastuussa seuraavista:

- **FEGA-aineistojen koordinoinnista ja hyväksynnästä organisaation sisällä**: Tarkistaa aineistot, jotka tullaan siirtämään Federaaliseen EGA:han organisaationsa hallinnoimina.
- **Organisaation aineistojen käyttöoikeuksien hallinnasta**: Arvioi DAC:n hallinnoimiin aineistoihin liittyvät käyttöoikeushakemukset varmistaen ehtojen, säädösten ja eettisten ohjeiden noudattamisen.

## Aineiston lisääminen katalogiin SD Applyssa {#adding-a-dataset-to-catalogue-in-sd-apply}

![SD Apply Infografiikka](https://a3s.fi/docs-files/sensitive-data/SD_Apply/SD_Apply_infographic.png)

Aineistojen lisääminen SD Applyhin ensimmäistä kertaa tehdään tiiviissä yhteistyössä CSC Service Deskin kanssa, sillä prosessi voi olla monimutkainen. Varaa aikaa prosessille ja ole valmis keskustelemaan organisaatiosi lakitiimin kanssa tarvittavista sopimuksista datan uudelleenkäyttöön liittyen. Alla on yleisohjeet prosessin tueksi.

## Vaihe vaiheelta -opas {#step-by-step-guide}

### 1. Organisaatioprofiilin pyytäminen {#1-request-for-organization-profile}

Ennen kuin voit lisätä tietoja SD Applyhin, CSC Service Deskin tulee luoda organisaatiolle profiili ja asettaa sinut organisaation ylläpitäjäksi.

1. Lähetä sähköposti osoitteeseen servicedesk@csc.fi aihekentällä "SD services" pyytääksesi profiilin luomista.
2. Kirjaudu sisään [SD Apply -palveluun](https://sd-apply.csc.fi/).
3. Ilmoita Service Deskille, että olet kirjautunut sisään. Service Desk lisää sinut oikeaan organisaatioon.
4. Service Desk ilmoittaa, kun voit alkaa lisätä aineistoja SD Applyhin.

!!! note
    Käytä aina samaa tunnistautumistapaa (Haka/Virtu tai CSC-kirjautuminen) kirjautuessasi SD Applyhin, koska roolisi ja hallinnoimasi aineistot on liitetty tunnistautumiseesi.

### 2. Aineiston lisääminen katalogiin {#2-add-dataset-as-catalogue-item}

Katalogikohde mahdollistaa hakijan hakea käyttöoikeutta aineistoosi. Lisätessäsi SD Applyhin haettavia aineistoja, sinun tulee ensin luoda:

* **Lomake:** hakijat käyttävät tätä hakemuksen jättämiseen.
* **Käyttöehdot (valinnainen):** käyttöehtosopimukset, joilla kerrotaan, miten hakija voi käyttää dataa uudelleen.
* **DAC:** Data Access Committee käsittelee hakemukset.
* **Tunniste:** tekninen tunniste aineistolle, esimerkiksi DOI.

Yhdistät nämä kohteet luomalla katalogikohteen. Voit myös käyttää jo olemassa olevia kohteita uudelleen.

!!! note
    Sinun täytyy luoda lomake, käyttöehdot, DAC ja tunniste **ennen** kuin luot katalogikohteen.

### 2.1. Hakemuslomakkeen luominen {#21-create-an-application-form}

Rekisterinpitäjä määrittelee, mitä tietoja hakijan tulee antaa saadakseen käyttöoikeuden dataan.

1. Kirjaudu SD Applyhin ja mene Hallinta > Lomakkeet.
2. Valitse **Luo lomake**.
3. Anna lomakkeelle kuvaava nimi. Nimi näkyy lomakelistanäkymässä, mutta ei hakijalle.
4. Anna lomakkeelle otsikko. Tämä näkyy hakijalle.
5. Lisää haluamasi kentät hakemukseen. Esikatselussa (oikealla) näet, miltä hakemus näyttää hakijalle. Kenttätyyppejä avataan tarkemmin alla.
6. Valitse **Tallenna** kun olet valmis.

!!! note
    Voit muokata lomaketta vain niin kauan kuin sitä ei ole liitetty katalogikohteeseen.

Voit sisällyttää sopimusten osat, jotka hakijan tulee täyttää suoraan SD Applyn hakemuslomakkeessa. Loput sopimussisällöstä voidaan liittää PDF-liitteenä käyttöehtoihin SD Applyssä, jolloin hakija voi tarkastella ja hyväksyä ehdot sähköisesti hakiessaan käyttöoikeutta aineistoon. Näin hakijat voivat täydentää tarvittavat osiot SD Applyn sisällä ja hyväksyä käyttöehdot ilman manuaalista allekirjoitusta. Keskustele tästä mahdollisuudesta organisaatiosi lakitiimin kanssa.

#### Lomakekenttien selitykset {#form-fields-explained}

- **Hakemuksen otsikko**: Käytä tätä, jos haluat hakijoiden nimeävän hakemuksensa.
- **Valintalista**: Käytä, jos haluat hakijan valitsevan yhden annetusta vaihtoehdosta. Tunnistekoodi näkyy esimerkiksi raporteissa, mutta hakijalle vain nimike näkyy. Esim. "Y" kyllä-vaihtoehdolle ja "N" ei-vaihtoehdolle.
- **Monivalintalista**: Käytä, jos hakija voi valita yhden tai useamman vaihtoehdon.
- **Taulukko**: Määrittele sarakkeet, hakija voi lisätä rivejä vapaasti. Kaikki sarakkeet vaaditaan jokaisella rivillä. Voit vaatia vähintään yhden rivin täytettäväksi.
- **Sähköpostiosoite**: Tarkistaa automaattisesti, että sähköposti on oikeassa muodossa.
- **Liite**: Hakija voi lisätä yhden tai useamman liitteen.
- **Seliteteksti**: Anna lisäohjeita, esim. Instrukstioita, tiettyihin kenttiin.
- **Otsikko**: Käytä, jos haluat jakaa lomakkeen osioihin.
- **Puhelinnumero**: Kansainvälisessä muodossa (E.164), esim. +14155552671.
- **IP-osoite**: Tarkistaa, että IP on IPv4- tai IPv6-muodossa, eikä kuulu tunnettuun yksityiseen osoitealueeseen.

#### Ehtokenttien luominen {#creating-conditional-fields}

Tarvittaessa voit luoda kenttiä, jotka piilotetaan tai näytetään hakijalle riippuen heidän antamistaan vastauksista.

Esimerkiksi voit luoda valintalistan "Haluatko lisätä liitteitä?" Kyllä – Ei. Jos hakija valitsee "Kyllä", liitekenttä näytetään. Jos "Ei”, liitekenttää ei näytetä.

!!! note
    Ehtokentät toimivat vain valinta- ja monivalintakentissä.

1. Luo **valintalista** ja täytä vaihtoehdot.
2. Luo toinen haluamasi kenttä.
3. Valitussa kentässä valitse "Lisäasetukset > Näkyvyys > Vain jos".
4. Kenttä: Valitse aiemmin luomasi valintalista alasvetovalikosta.
5. Arvo: Valitse, minkä valinnan perusteella kenttä näytetään. Tässä esimerkissä kenttä 2 "Lisää liitteitä" näytetään jos hakija valitsee ”Kyllä” kentässä 1.

Voit testata lomakkeen toimivuutta oikealla olevasta Esikatselu-näkymästä.

### 2.2. Käyttöehtojen luominen {#22-create-a-policy}

Käyttöehdot määrittelevät sopimukset ja käyttöehdot, jotka hakijan pitää hyväksyä saadakseen datan käyttöönsä. Käyttöehdot näkyvät osana hakemusta, ja jokaisen tutkimusryhmän jäsenen, joka hakee käyttöoikeutta, tulee hyväksyä ehdot ennen pääsyä aineistoon.

Voit luoda kolmen tyyppisiä käyttöehtoja:

- **Ulkoinen linkki**: Syötä linkki ulkoiselle sivulle, jossa käyttöehdot esitetään. Käytä esimerkiksi [Creative Commons](https://creativecommons.org/choose/?lang=en) -lisenssien yhteydessä.
- **Suora teksti**: Kirjoita ehdot hakemuslomakkeelle. Hakija näkee ne normaalina tekstinä.
- **Liite**: Lataa liitetiedosto, jonka hakija voi ladata ja hyväksyä. Suosittelemme PDF-muotoa ja muotoilua, joka mahdollistaa sähköisen hyväksymisen SD Applyssä.

#### Data Access Policies suomalaisessa Federaalisessa EGA:ssa {#data-access-policies-in-the-finnish-federated-ega}

Aineiston siirtäminen Suomen Federaaliseen EGA:an vaatii useita sopimuksia: Palvelusopimus Federaalista EGA:ta varten sekä Data Access Agreement, joka sisältää myös Data Transfer Agreementin.

**Data Access Agreement (DAA):** DAA on sopimus datan käyttöoikeustoimikunnan (DAC) ja käyttöoikeutta hakevan henkilön välillä. DAA:ssa rekisterinpitäjä voi määritellä ehdot ja rajoitukset datan käyttöön, kuten käyttö-, julkaisu-, lataus- ja pääsyoikeudet. DAA:n tulee sisältää myös Data Transfer Agreement (DTA), joka on tarpeellinen kun muista kuin EU/ETA-maista olevat tutkijat käyttävät dataa SD Desktopin kautta. DAA ja DTA liitetään SD Applyn käyttöehtoihin. Lisätietoa saat oman organisaatiosi lakipalveluista. Voit myös [ladata esimerkkipohjan](https://ega-archive.org/assets/files/Example_DAA.doc) EGA:lta.

Konsultoi organisaatiosi lakiasiantuntijoita sopivien käyttöehtojen määrittelyssä.

Käyttöehdot ovat valinnaisia. Et voi muokata ehtoja niiden tallentamisen jälkeen.

### 2.3. DAC:n (toimikunnan) luominen {#23-create-a-dac}

Luomalla DAC:n (Data Access Committee) nimeät toimikunnan jäsenet hakemuskäsittelijöiksi. He hyväksyvät tai hylkäävät hakemukset organisaatiosi aineistoille ja saavat sähköpostiviestin uusista hakemuksista.

Voit valita kahden prosessin väliltä: dynaaminen prosessi ja päätöksentekijäprosessi. Valitse sopiva. Nimeä DAC kuvaavasti, jotta löydät sen helposti myöhemmin.

- **Oletusprosessi:** DAC-jäsenet voivat hyväksyä tai hylätä hakemuksia. Mukana voi olla tarkastajia ja päättäjiä. Vain yhden DAC-jäsenen täytyy hyväksyä hakemus.

- **Päätäjäprosessi:** Oletusprosessin rajoitettu versio. DAC-jäsenet eivät voi itse hyväksyä/hylätä hakemuksia, vaan heidän täytyy pyytää erillistä päättäjää hyväksymään/hylkäämään.

#### DAC-jäsenten määrääminen {#assign-dac-members}

Lisää DAC-jäseniä hakemuskäsittelijöiksi etsimällä käyttäjiä käyttäjätunnuksen perusteella tai alasvetovalikosta. Suosittelemme lisäämään **useamman käsittelijän samaan DAC:iin**, jotta hakemukset käsitellään sujuvasti.

!!! note
    Voit **etsiä vain käyttäjiä, jotka ovat aiemmin kirjautuneet SD Applyhyn**. Jos et löydä haluamaasi käsittelijää, pyydä häntä kirjautumaan sisään ja yritä uudelleen.

Jos haluat piilottaa käsittelijöiden (DAC, tarkastajat, päättäjät) nimet hakijalta, valitse *Anonyymi käsittely*.

DAC-jäsenet eivät saa ilmoitusta, että heidät on lisätty käsittelijäksi, mutta he saavat sähköpostin uusista hakemuksista.

#### Lomakkeen liittäminen DAC:iin {#add-a-form-to-a-dac}

Jos kaikki SD Applyn hallinnoimat aineistot käyttävät samaa hakemuslomaketta, voit liittää sen DAC:iin alasvetovalikosta.

Jos haluat kysyä aineistokohtaisia kysymyksiä, voit luoda kaksi lomaketta: yleiset kysymykset DAC:lle ja aineistokohtaiset kysymykset katalogikohteelle. Hakija täyttää tällöin molemmat osiot.

#### Käyttöehtojen liittäminen DAC:iin {#add-a-policy-to-a-dac}

Jos kaikilla organisaatiosi hallinnoimilla aineistoilla on samat käyttöehdot ja sopimukset, voit liittää luomasi ehdot DAC:iin alasvetovalikosta.

Tällä hetkellä PDF-liitteiden kokorajoitus SD Applyssa on 1 MB. **Optimoithan PDF-tiedoston ennen lisäämistä!**

Tällöin käyttöehdot lisätään automaattisesti kaikkiin DAC:ia käyttäviin katalogikohtiin. Voit myös liittää aineistokohtaiset käyttöehdot tunnisteeseen.

### 2.4. Tunnisteen luominen {#24-create-a-identifier}

Tutkija saa aineistonsa tallentamisesta Federaaliseen EGA:an yksilöllisen tunnisteen, esim. EGAD12345. Jotta aineisto on haettavissa SD Applyn kautta, FEGA-lähettäjän tulee toimittaa tunniste rekisterinpitäjälle, joka lisää sen SD Applyhin.

1. Lisää FEGA-lähettäjän antama tunniste tunnistekenttään.
2. Valitse haluamasi käyttöehdot yhdistämällä aiemmin luodut ehdot alasvetovalikosta. Käyttöehdot ovat valinnaisia.

!!! note
    Et voi muokata tunnistetta sen tallentamisen jälkeen. Jos haluat muuttaa tunnistetta, luo uusi ja arkistoi vanha.

### 2.5. Katalogikohteen luominen {#25-create-a-catalogue-item}

Katalogikohde kokoaa luomasi kohteet yhdeksi aineistoksi, johon hakija voi hakea käyttöoikeutta.

1. Otsikkokenttään kuvaava nimi aineistolle, jotta hakija tunnistaa oikean aineiston.
2. Jos lisätietoa on toisella sivulla, lisää linkki "Lisätietoja"-kenttään.
3. Valitse luomasi DAC.
4. Valitse aineiston tunniste tunnisteen alasvetovalikosta.
5. Jos et liittänyt lomaketta DAC:iin, valitse luomasi hakemuslomake alasvetovalikosta.
6. Valitse kategoriaksi FEGA.
7. **Ota katalogikohde käyttöön, jotta se näkyy hakijoille.** Uusi katalogikohde on aluksi poissa käytöstä, eikä sitä voi vielä hakea. Kun otat sen käyttöön, se näkyy katalogisivulla aineistona.

#### Katalogikohteiden muokkaus {#editing-catalogue-items}

Voit muokata katalogikohteen nimeä, organisaatiota ja lisätietolinkkejä toiminnolla "muokkaa".

!!! note
    Tallennuksen jälkeen et voi muokata lomaketta, DAC:ia tai tunnistetta, jotka on liitetty katalogikohteeseen. Muokkaus ei ole mahdollista myöskään, jos jokin osa katalogikohteesta on pois päältä.

Jos haluat muuttaa hakemuslomaketta ja/tai DAC:ia useista katalogikohteista, valitse haluamasi kohteet valintalaatikolla ja sitten **Päivitä katalogikohde**.

Tämä **poistaa käytöstä ja arkistoi vanhan katalogikohteen** ja luo uuden version. Hakijat eivät näe eivätkä voi hakea käyttöoikeutta enää vanhaan kohteeseen.

## Lisää aineistoja organisaatiosi alle {#adding-more-datasets-under-your-organisation}

Kun olet kerran luonut lomakkeen, tarvittavat käyttöehdot ja DAC:n, voit käyttää näitä jatkossakin uusille aineistoille, mikäli aineistoilla on sama DAC.

Lisää uusi aineisto SD Applyn katalogiin samalla DAC:lla:

1. Luo uusi **tunniste**. FEGA-lähettäjä toimittaa yksilöllisen tunnisteen.
2. Luo **katalogikohde** yhdistämällä aiemmin luodut kohteet (tunniste, lomake, DAC).
3. Ota katalogikohde käyttöön, jotta hakijat näkevät sen.

Varmista, että tarvittavat sopimukset on yhdistetty käyttämääsi DAC:iin tai jokaisen uuden tunnisteen yhteyteen SD Applyhin.

## Kohteiden poistaminen käytöstä ja arkistointi {#disabling-and-archiving-items}

Voit poistaa kaikki kohteet käytöstä ja arkistoida ne. Poistaminen ei ole mahdollista, jotta tiedon tapahtumahistoria säilyy tietoturvasyistä.

### Kohteiden poistaminen käytöstä {#disabling-items}

Kun poistat kohteen, esim. lomakkeen, käytöstä, sitä **ei voi käyttää uusissa katalogikohteissa**. Käytöstä poistetut kohteet piilotetaan alasvetovalikoista.

**Jos poistat katalogikohteen käytöstä**, sitä ei voi enää hakea. Kuitenkin, jos hakemus on jo jätetty ennen käytöstä poistoa, käsittelijä voi edelleen käsitellä ja hyväksyä/hylätä hakemuksen.

Poistettuja kohteita voi aktivoida uudestaan.

### Arkistointi {#archiving}

Arkistointi **piilottaa kohteen hallintanäkymästä ja hakijoilta**. Jos haluat selata arkistoituja kohteita, valitse **Näytä arkistoidut**. Suosittelemme arkistoimaan vanhat, tarpeettomat kohteet.

Arkistoituja kohteita voi palauttaa näkyviin.

Käsittelijät saavat ilmoituksen, jos hakemuksen kohteena oleva katalogikohde on poistettu käytöstä tai arkistoitu.

## Tuki {#support}

Jos sinulla on kysyttävää SD Applyn käytöstä, ota yhteyttä [CSC Service Deskiin](../../support/contact.md) (aihe: SD Apply).