---
search:
  boost: 2
---

# Uuden projektin luominen { #creating-a-new-project }

Uuden projektin luominen edellyttää [CSC-käyttäjätunnusta](how-to-create-new-user-account.md#getting-an-account-with-haka-or-virtu).

1. Kirjaudu [MyCSC](http://my.csc.fi/):hen CSC-käyttäjätunnuksellasi **tai** Haka/Virtu-tunnuksella.
2. Valitse vasemmalta navigointivalikosta **Projects**.
3. Napsauta oikealla **+ New project**.
4. Valitse **Project category**. Saatavilla olevat kategoriat:
	* [Academic](how-to-create-new-project.md#academic)
	* [Course](how-to-create-new-project.md#course)
	* [LUMI](how-to-create-new-project.md#how-to-create-finnish-lumi-projects)
5. Täytä **Project name**, **Project description** ja kaikki vaaditut kentät.
6. Valitse tässä projektissa käytettävät palvelut.
7. Säädä projektisi resurssipaketteja.
8. Lue ja hyväksy käyttöehdot.

![Uuden projektin luontinäkymä.](../img/mycsc-create-new-project.png){width=400}

## Academic { #academic }

Akateminen projektikategoria on varattu [maksuttomille käyttötapauksille](https://research.csc.fi/free-of-charge-use-cases){:target="_blank"}, ja niitä voivat luoda vain suomalaisten korkeakoulujen, valtion tutkimuslaitosten sekä CSC:n henkilöstö.

!!! Note
    Jos olet opettaja ja tarvitset resursseja kurssille, tutustu [Course](how-to-create-new-project.md#course) -projektikategoriaan. Jos olet opiskelija, katso [Student](how-to-create-new-project.md#student) -projektikategoria.

6. Valitse projektissa tehtävän tutkimuksen **Field of Science** ja **Sub Science Area**.
7. Valitse _Yes_ tai _No_ sen mukaan, käsitelläänkö projektissasi henkilötietoja. Lue lisää [henkilötietojen käsittelystä projektissasi](../accounts/when-your-project-handles-personal-data.md).
8. Lue käyttöehdot ja vahvista hyväksyntäsi.
9. Klikkaa **Create project**.

Akatemiset projektit ovat yleensä voimassa vuoden kerrallaan, mutta niitä voidaan jatkaa. Projektin jatkamisesta katso sivu [How to manage your project](how-to-manage-your-project.md).

## Commercial { #commercial }

Kaupalliset projektit ovat toistaiseksi saatavilla vain Service Deskin kautta. Ole hyvä ja [ota yhteyttä CSC Service Deskiin](../support/contact.md) saadaksesi lisätietoja.

## Course { #course }

Kurssikategoria on varattu [maksuttomille](https://research.csc.fi/free-of-charge-use-cases){:target="_blank"} käyttötapauksille. Tämän kategorian projekti on määräaikainen (enintään 6 kuukautta, ei jatkettavissa), kiinteillä resursseilla, ja se on suunniteltu yhden kurssin toteuttamiseen. Kurssin uudelleentoteutus edellyttää uutta projektia. Huomaa, että kaikki data poistetaan projektin päättyessä.

6. Täytä kurssin ajankohdat ja tieteenala.
7. Lue käyttöehdot ja vahvista hyväksyntäsi.
8. Klikkaa **Create project**.

Helpoin tapa lisätä opiskelijoita kurssiprojektiin on käyttää [kutsulinkkiä](how-to-add-members-to-project.md#using-invitation-link).

## Kuinka luoda suomalaisia LUMI-projekteja { #how-to-create-finnish-lumi-projects }

LUMI-projekteja käytetään LUMI-ympäristöön pääsyn ja sen tarjoamien resurssien hallintaan. LUMI-projektit on rajattu koskemaan vain LUMI-ympäristöä (LUMI-C, LUMI-G jne.). Suomalaiset LUMI-projektit ovat ajallisesti ja resursseiltaan kiinteitä, ja kokonaisresurssit on määriteltävä jo projektihakemuksessa.

Suomalainen LUMI-projekti voi sisältää yhden tai useamman CSC-käyttäjätunnuksen, ja yksi CSC-käyttäjätunnus voi kuulua useaan suomalaiseen LUMI-projektiin. Jokaisella LUMI-projektilla on oltava vastuullinen tutkija (eli Project Manager), joka luo projektin ja hakee resursseja, hallitsee projektiin kuuluvia käyttäjätunnuksia ja vastaa resurssien käytöstä. LUMI-projektipäällikkö on tyypillisesti tutkimusryhmän johtaja tai muu senioritutkija. Katso lisää [projektipäällikön edellytyksistä](https://research.csc.fi/en/prerequisites-for-a-project-manager).

LUMI-palvelut ovat maksuttomia akateemiselle tutkimukselle suomalaisten korkeakoulujen ja valtion tutkimuslaitosten jäsenille.

### LUMI-projektin luominen ja resurssien hakeminen { #creating-a-lumi-project-and-applying-for-resources }

6. Valitse **LUMI** Project category -listasta.
7. Valitse LUMI **Access mode** (Regular, Benchmark tai Development).
8. Täytä **resources**: CPU core hours, GPU hours, Storage hours, sekä kaikki alla olevat **text fields** huolellisesti. Jos tiedot ovat puutteelliset tai riittämättömät, hakemus hylätään. Regular Access -hakemuksiin vaaditaan luettelo aiemmista julkaisuista ja asianmukainen tutkimussuunnitelma. Benchmark Access -hakemuksiin vaaditaan suunnitelma siitä, miten resursseja käytetään benchmarkeihin, ja Development Access -hakemuksiin kuvaus ohjelmistoista, menetelmistä ja kehitystavoitteista.
9. Valitse **Field of Science** ja täytä **Keywords**.
10. Käsitteleekö projektisi henkilötietoja? Huomaa: **LUMI-projekteissa henkilötietojen käsittely ei ole tällä hetkellä sallittua**.
11. Ruksaa ruutu I have read and accepted the LUMI General Terms of Use.
12. Klikkaa **Create project**.

Kun olet luonut projektin, [kutsu projektin jäsenet](how-to-add-members-to-project.md). LUMI-projektihakemuksesi lähetetään käsiteltäväksi CSC:n resurssien kohdennuksesta vastaavalle hallinnolle. CSC:n resurssien kohdennusryhmä kokoontuu [kolmen viikon välein](https://research.csc.fi/applying-for-computing-resources).

Huomaa, että LUMI-käyttöoikeus myönnetään vain SSH-avaimilla, ei salasanoilla. Kun olet saanut sähköpostiisi vahvistuksen LUMI-projektihakemuksesi hyväksymisestä, [lataa julkinen SSH-avaimesi MyCSC:hen ohjeiden mukaisesti](../computing/connecting/ssh-keys.md).

Lisätietoja LUMI-projekteista: [Users in Finland](https://www.lumi-supercomputer.eu/get-started-2021/users-in-finland/){:target="_blank"}

## Student { #student }

Opiskelija voi toimia opiskelijaprojektin projektipäällikkönä. Lue huolellisesti ohje [Getting started with the Student Project](../support/tutorials/student_quick.md) ja jatka sitten alla olevien ohjeiden mukaan.

Opiskelijakategoria on varattu [maksuttomille](https://research.csc.fi/free-of-charge-use-cases) käyttötapauksille. Tämän kategorian projekti on määräaikainen (enintään 6 kuukautta, ei jatkettavissa), kiinteillä resursseilla, ja se on tarkoitettu tukemaan opiskelijan työskentelyä korkeakoulujen kurssien ja opinnäytetyön parissa.

1. Kirjaudu [MyCSC](http://my.csc.fi/):hen CSC-käyttäjätunnuksellasi tai Haka/Virtu-tunnuksellasi.
2. Valitse vasemmalta navigointivalikosta **Projects**.
3. Valitse sivun yläreunasta **+ New project**.
4. Kirjoita **nimi-kenttään** kuvaava nimi projektille. Tämä voi olla esimerkiksi kurssin nimi tai opinnäytetyösi aihe.
5. Ilmoita **kuvaus-kentässä**, onko kyseessä esimerkiksi kurssiin liittyvä projekti vai opinnäytteeseen liittyvä projekti.
6. Valitse **resurssitarpeen tai kurssin päättymispäivä**, kuitenkin enintään kuusi kuukautta projektin luontipäivästä.
7. Täytä **kommentti-kenttään** mahdollinen yliopiston kurssikoodi ja -nimi tai vastaava.
8. Täytä **opintojesi ala** – tai sitä lähinnä vastaava.
9. Lue **käyttöehdot** ja vahvista hyväksyntäsi.
10. Klikkaa **Create project**.

Halutessasi voit lisätä projektiisi muitakin jäseniä. Helpoin tapa tehdä tämä on käyttää [kutsulinkkiä](how-to-add-members-to-project.md#using-invitation-link).

## Oikeus luoda CSC-projekteja Haka-affiliaation perusteella { #right-to-create-csc-projects-based-on-haka-affiliation }

Tässä kuvataan, miten CSC-tiliisi liitetty Haka-identiteetti vaikuttaa oikeuteesi luoda akateemisia, kurssi- ja opiskelijatyyppisiä CSC-projekteja. Haka-kirjautumisesi yhteydessä saamme tiedon asemastasi kotiorganisaatiossa. Alla tätä tietoa asemastasi kutsutaan nimellä ”Haka-affiliaatiotiedot”. Alla olevasta taulukosta näet, miten Haka-affiliaatio vaikuttaa oikeuteen luoda CSC-projekti ja toimia sen Project Managerina.

| Haka-affiliaatio ([eduPersonScopedAffiliation](https://wiki.eduuni.fi/spaces/CSCHAKA/pages/256884450/funetEduPersonSchema2dot5#funetEduPersonSchema2dot5-eduPersonScopedAffiliation)) | Kuvaus ([Haka-dokumentaatiosta](https://wiki.eduuni.fi/spaces/CSCHAKA/pages/256884450/funetEduPersonSchema2dot5#funetEduPersonSchema2dot5-eduPersonAffiliation)) | Akateminen projekti | Kurssiprojekti | Opiskelijaprojekti |
| -- | -- | -- | -- | -- |
| `faculty@org.fi` | tutkimus- ja opetushenkilöstö laboratorioissa ja laitoksissa; esim. professorit, tutkijat, lehtorit, assistentit, olipa heidät palkannut oppilaitos tai jokin muu organisaatio (kuten Suomen Akatemia). Dosentit voidaan liittää faculty-luokkaan, jos he osallistuvat aktiivisesti tutkimukseen tai opetukseen oppilaitoksessa. | ✅ | ✅ | ❌ |
| `staff@org.fi` | hallintohenkilöstö oppilaitoksessa, olipa heidät palkannut oppilaitos tai jokin muu organisaatio | ✅ | ✅ | ❌ |
| `employee@org.fi` | henkilö, joka on tosiasiallisesti oppilaitoksen palveluksessa | ✅ | ✅ | ❌ |
| `student@org.fi` (ilman faculty-, staff- tai employee-affiliaatiota) | opiskelija, joka on ilmoittautunut läsnä olevaksi. | ❌ | ❌ | ✅ |
| `member@org.fi` (ilman faculty-, staff- tai employee-affiliaatiota) | Tämä arvo kattaa kaikki yllä mainitut kategoriat sekä opiskelijat, jotka osallistuvat pätevöitymiseen tähtäävään täydennyskoulutukseen, muuhun täydennyskoulutukseen tai avoimen yliopiston/korkeakoulun opintoihin (pätevöitymiseen tähtäävä täydennyskoulutus, muu täydennyskoulutus, avoin yliopisto/korkeakoulu, täydennyskoulutuskeskuksen opiskelijat). | ❌ | ❌ | ✅ |

Lisäksi sinulla voi olla yksi tai useampi seuraavista Haka-affiliaatiotiedoista, mutta nämä eivät oikeuta CSC-projektien luomiseen: `affiliate@org.fi`, `alum@org.fi`, `library-walk-in@org.fi`

Lisätietoa käytännöstä: [Prerequisites and responsibilities for a CSC project manager](https://research.csc.fi/terms-of-use/prerequisites-for-a-project-manager/).

_Huom._: Jos et itse täytä projektipäällikön kelpoisuusehtoja, sinulla saattaa olla ohjaaja tai kollega, joka voi luoda CSC-projektin ja lisätä sinut sen jäseneksi.

### Haka-affiliaatiotietojesi tarkistaminen { #checking-your-haka-affiliation-information }

Voit tarkistaa Haka-attribuuttisi MyCSC-portaalissa:

1. Siirry osoitteeseen [https://my.csc.fi/userinfo](https://my.csc.fi/userinfo) ja klikkaa **Retrieve userinfo**
2. Kirjaudu organisaatiosi Haka-tunnuksella
3. Affiliaatiosi löytyvät kohdasta **eduPersonScopedAffiliation**

### Ongelmat Haka-affiliaatiotietojen kanssa { #problems-with-the-haka-affiliation-information }
- Jos et pysty luomaan CSC-projektia, kirjaudu MyCSC:hen uudelleen Hakan kautta päivittääksesi Haka-affiliaatiotietosi.
- Jos epäilet, että Haka-affiliaatiotietosi saattavat olla virheelliset, ota yhteyttä kotiorganisaatioosi.