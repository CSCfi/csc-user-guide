[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Hyödyllisiä termejä: palvelut ja tekniset näkökohdat { #useful-terminology-services-and-technical-aspects }

**Allas**: CSC:n pilvitallennuspalvelu. SD Connect on käyttöliittymä, joka helpottaa arkaluonteisten tietojen salausta ja tallennusta Allakseen. Käyttäjät voivat myös käyttää Allasta ohjelmallisesti ei-arkaluonteisia tietoja varten tarjottujen rajapintojen kautta.

**Laskutusyksiköt (Billing Units)**: Laskutusyksiköitä käytetään resurssien seurantaan. SD Connectin ja SD Desktopin käyttö kuluttaa vastaavasti Storage- ja Cloud-laskutusyksiköitä.

**Bucket/Container**: Nämä termit viittaavat pääkansioon (teknisesti juurikansioon), johon salatut tiedostot tallennetaan SD Connectissa/Allaksessa. Bucketin/containerin nimi näkyy internetissä. Samassa projektissa voi olla useita bucketeja (enintään 1000), mutta jokaisella bucketilla on oltava yksilöllinen nimi koko tallennusjärjestelmässä (mukaan lukien muut projektit). Oletuksena bucketissa olevat tiedot ovat vain projektin jäsenten käytettävissä. Voit kuitenkin jakaa tietoja ja myöntää käyttöoikeuksia muihin CSC-projekteihin tai käyttäjille SD Connectin avulla.

**CSC-projekti**: CSC:n palveluiden käyttö perustuu projekteihin: kaikki CSC:ssä olevat tietosi kuuluvat projektiin. Jokaisella projektilla on ensisijainen käyttäjä, CSC-projektipäällikkö, joka voi lisätä jäseniä ja hallinnoi pääsyä palveluihin. Projektipäällikkö on vastuussa projektin toiminnasta ja toimii rekisterinpitäjän (tai akateemisen organisaation) edustajana. Hänen tulee esimerkiksi kuvata, millaista arkaluonteista dataa projekti käsittelee.

**Levykiintiö**: CSC:n palveluiden käyttäjille varattu tallennustila. SD Connectin oletuskiintiö on 10 TB. Voit hakea lisää tallennustilaa ottamalla yhteyttä [CSC Service Deskiin](../../support/contact.md). 

**Monivaiheinen tunnistautuminen**: Kun kirjaudut SD Desktop -palveluun, sinun on suoritettava lisävahvistusvaihe käyttäjätunnuksen ja salasanan lisäksi. Näin tilisi on turvatumpi. Tätä lisävahvistusvaihetta kutsutaan nimillä "Two-Step Verification" tai "Multifactor Authentication", koska todistat henkilöllisyytesi eri menetelmällä. Tässä tapauksessa sinun on syötettävä kertakäyttöinen koodi (6 numeroa), jonka saat avaamalla mobiilisovelluksen. Koodi on yksilöllinen ja voimassa rajoitetun ajan.

**Objekti**: tekninen nimitys tiedostolle, joka on tallennettu pilviobjektitallennukseen kuten Allakseen (tai ladattu CSC:hen SD Connectin kautta). Tämä määritelmä korostaa, että SD Connectiin / Allakseen tallennettuja tiedostoja ei voi muokata suoraan, ellei niitä siirretä tai kopioida laskentaympäristöön. Niihin voidaan kuitenkin päästä käsiksi vain luku -tilassa pilvilaskentaympäristöstä (esim. SD Desktopista). 

**Projektitunniste (Project Identifier)**: synonyymi CSC Project ID:lle, kun käytetään komentorivityökalua. SD Connectin käyttöliittymässä se näkyy kohdassa User Information> Project usage ja esitetään 32 numeron ja kirjaimen sarjana: esim. `AUTH_3a66dbf90b2940dc9c651362af595b23`.

**Virtuaalikone (VM) tai virtuaalityöpöytä**: virtuaalinen laskenta-ympäristö (tai virtuaalitietokone), joka toimii kuten fyysinen tietokone. Sillä on suoritin, muisti ja käyttöjärjestelmä, mutta se on olemassa vain koodina tai CSC:n konesalissa olevan isäntäkoneen osiona. Arkaluonteisten tietojen palveluissa käytetyt virtuaalikoneet ovat tietoturvasyistä täysin eristettyjä internetistä.

**Virtuaalikoneen flavor (VM flavor) tai valmiiksi määritelty työpöytävalinta**: flavor määrittää pilvilaskentaympäristön resurssit ja kokoonpanot. Se määrittelee laskenta-, muisti- ja tallennuskapasiteetin, joka voidaan varata virtuaalikoneelle.

## Hyödyllisiä termejä: tietosuoja { #useful-terminology-data-protection }

**Rekisterinpitäjä ja henkilötietojen käsittelijä** GDPR:n mukaan rekisterinpitäjä on yksityishenkilö tai organisaatio, joka määrittelee arkaluonteisten henkilötietojen käsittelyn tarkoitukset ja keinot, ja se on yleensä akateeminen organisaatio. Henkilötietojen käsittelijä puolestaan on yksityishenkilö tai organisaatio, joka käsittelee henkilötietoja rekisterinpitäjän puolesta, esimerkiksi IT-palveluntarjoaja, tässä tapauksessa CSC.

**Tietojenkäsittelysopimus (Data Processing Agreement, DPA)**: Tietojenkäsittelysopimus on sopimus rekisterinpitäjän ja henkilötietojen käsittelijän välillä. Se säätelee tietojenkäsittelyn erityispiirteitä – kuten sen laajuutta ja tarkoitusta – sekä rekisterinpitäjän ja käsittelijän välistä suhdetta. Lisätietoja löytyy tämän oppaan alussa olevasta osiosta [kun projektisi käsittelee henkilötietoja](../../accounts/when-your-project-handles-personal-data.md#data-processing-agreement) sekä sivustolta [CSC:n yleiset käyttöehdot](https://research.csc.fi/general-terms-of-use) ja [CSC:n tietojenkäsittelysopimus](https://research.csc.fi/data-processing-agreement) research.csc.fi-palvelussa. 

**Tietosuojan vaikutustenarviointi (Data Protection Impact Assessment, DPIA)**: Tietosuojan vaikutustenarviointi (DPIA) vaaditaan GDPR:n mukaan toiminnoissa, joiden "todennäköisesti katsotaan aiheuttavan korkean riskin luonnollisten henkilöiden oikeuksille ja vapauksille". Lisätietoja tarjoaa [täällä](https://tietosuoja.fi/en/list-of-processing-operations-which-require-dpia) Tietosuojavaltuutetun toimisto sekä kotiorganisaatiosi lakiyksikön tarjoama tuki. 

**Arkaluonteiset tiedot (Sensitive Data)**: Arkaluonteiset tiedot ovat tietoja, joita on suojattava luvattomalta käytöltä. Suojaus voi olla tarpeen oikeudellisista tai eettisistä syistä, yksityisyydensuojan vuoksi tai omistuksellisten etujen takia. Arkaluonteisiin tietoihin voi kuulua esimerkiksi:

* Henkilötietojen erityiset tietoryhmät (esim. terveys-, geneettiset ja henkilötiedot, rotu tai etninen alkuperä, poliittiset mielipiteet, uskonnolliset tai filosofiset vakaumukset tai ammattiliiton jäsenyys, geneettiset tiedot, biometriset tiedot luonnollisen henkilön yksilöimiseksi, terveystiedot, tiedot luonnollisen henkilön seksielämästä tai seksuaalisesta suuntautumisesta, rikostuomioita ja rikkomuksia tai niihin liittyviä turvatoimia koskevat tiedot, henkilön tunnistamiseen johtavat tiedot)
* Ekologiset tiedot (esim. uhanalaisten lajien sijainti tai muut suojelutoimet)
* Luottamukselliset tiedot (esim. liikesalaisuudet)
* Tiedot, joita muutoin pidetään arkaluonteisina