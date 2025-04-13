## Hyödyllinen terminologia: palvelut ja tekniset näkökohdat {#useful-terminology-services-and-technical-aspects}

**Allas**: CSC:n pilvitallennuspalvelu. SD Connect on käyttöliittymä, joka helpottaa arkaluonteisten tietojen salauksen ja tallennuksen Allakseen. Käyttäjät voivat myös käyttää Allasta ohjelmallisesti rajapintojen avulla ei-arkaluontoisille tiedoille.  

**Laskentayksiköt**: laskentayksiköitä käytetään resurssien seurantaan. SD Connectin ja SD Desktopin käyttö kuluttaa laskentayksiköitä.  

**Bucket/Kontti**: Nämä termit viittaavat pääkansioon (teknisesti kutsutaan juurikansioksi), jossa salatut tiedostot tallennetaan SD Connectiin/Allakseen. Sangon/kontin nimi on näkyvissä internetissä. Voit luoda samassa projektissa useita sangoja (enintään 1000), mutta jokaisen sangon on oltava nimeltään uniikki koko tallennusjärjestelmässä (mukaan lukien muut projektit). Oletusarvoisesti sangon tiedot ovat vain projektin jäsenille. Voit kuitenkin jakaa ja antaa pääsyn muihin CSC-projekteihin tai käyttäjille SD Connectin kautta.  

**CSC-projekti**: CSC:n palveluiden käyttö perustuu projekteihin: kaikki CSC:ssä olevat tietosi kuuluvat projektiin. Jokaisella projektilla on pääkäyttäjä, CSC-projektipäällikkö, joka voi lisätä jäseniä ja hallinnoida pääsyä palveluihin. Projektipäällikkö vastaa projektin toiminnasta ja toimii tietojen käsittelijänä (tai akateemisen organisaation) edustajana. Heidän on esimerkiksi kuvattava, minkä tyyppisiä arkaluonteisia tietoja projekti käsittelee.

**Levykiintiö**: CSC:n palveluiden käyttäjille saatavilla oleva tallennuskapasiteetti. SD Connectilla on oletuskiintiö 10 TB. Voit hakea lisää tallennustilaa kirjoittamalla [CSC Service Deskille](../../support/contact.md). 

**Monivaiheinen todentaminen**: Kun kirjaudut SD Desktop -palveluun, sinun on suoritettava ylimääräinen varmistusvaihe käyttäjätunnuksen ja salasanan antamisen lisäksi. Näin tilisi on turvallisempi. Lisätarkistusvaihetta kutsutaan "kahden askeleen varmennukseksi" tai "monivaiheiseksi tunnistautumiseksi", koska todistat henkilöllisyytesi eri menetelmällä. Tässä tapauksessa sinun on kirjoitettava kuusinumeroisen koodi, joka saadaan avaamalla mobiilisovellus. Koodi on ainutlaatuinen ja se on voimassa vain rajoitetun ajan.

**Objekti**: tekninen termi tiedostosta, joka on tallennettu pilviobjektitallennukseen, kuten Allas (tai ladattu CSC:hen SD Connectin kautta). Tämä määritelmä korostaa, että SD Connectiin / Allakseen tallennettuja tiedostoja ei voi suoraan muokata, ellei niitä siirretä tai kopioida tietojenkäsittely-ympäristöön. Niitä voidaan kuitenkin käyttää vain luku -muodossa pilvilaskentaympäristöstä (esim. SD Desktop).  

**Projektitunniste**: synonyymi CSC-projektin tunnukselle komentorivityökalun käytössä. SD Connect -käyttöliittymä näytetään kohdassa Käyttäjätiedot > Projektin käyttö ja esitetään 32 numeron ja kirjaimen sarjana: esim. `AUTH_3a66dbf90b2940dc9c651362af595b23`.

**Virtuaalikone (VM) tai virtuaalipöytäkone**: virtuaalinen tietojenkäsittely-ympäristö (tai virtuaalinen tietokone), joka toimii fyysisenä tietokoneena. Sillä on prosessori, muisti ja käyttöjärjestelmä, mutta se on olemassa vain koodina tai osana isäntätietokonetta CSC:n datakeskuksessa. Arkaluontoisten tietojen palvelujen virtuaalikoneet ovat täysin eristettyjä internetistä turvallisuussyistä.  

**Virtuaalikoneen maku (VM-flavor) tai valmiiksi rakennettu pöytäoptio**: maku määrittelee pilvilaskentaympäristön resurssit ja kokoonpanot. Se määrittää laskentatehon, muistin ja tallennuskapasiteetin, joka voidaan osoittaa virtuaalikoneelle.

## Hyödyllinen terminologia: tietosuoja {#useful-terminology-data-protection}

**Rekisterinpitäjä ja tietojen käsittelijä**: GDPR:n mukaan rekisterinpitäjä on henkilö tai organisaatio, joka määrittelee henkilötietojen käsittelyn tarkoituksen ja keinot, ja se on yleensä akateeminen organisaatio. Tietojen käsittelijä puolestaan on henkilö tai organisaatio, joka käsittelee henkilötietoja rekisterinpitäjän puolesta, kuten IT-palveluntarjoaja, tässä tapauksessa CSC. 

**Tietojenkäsittelysopimus (DPA)**: tietojenkäsittelysopimus (DPA) on rekisterinpitäjän ja tietojen käsittelijän välinen sopimus. Se säätelee tietojenkäsittelyn erityispiirteitä – kuten sen laajuutta ja tarkoitusta – sekä rekisterinpitäjän ja tietojen käsittelijän suhdetta. Lisätietoja löytyy kohdasta [kun projektisi käsittelee henkilötietoja](../../accounts/when-your-project-handles-personal-data.md#data-processing-agreement) tämän käyttöoppaan alussa ja [CSC Yleiset käyttöehdot](https://research.csc.fi/general-terms-of-use) ja [CSC Tietojenkäsittelysopimus](https://research.csc.fi/data-processing-agreement) research.csc.fi-sivustolla. 

**Tietosuojavaikutusten arviointi (DPIA):** Tietosuojavaikutusten arviointi (DPIA) vaaditaan GDPR:n mukaan toimille, jotka "todennäköisesti aiheuttavat korkean riskin luonnollisten henkilöiden oikeuksille ja vapauksille". Lisätietoja löytyy [täältä](https://tietosuoja.fi/en/list-of-processing-operations-which-require-dpia) Suomen tietosuojavaltuutetun toimisto ja erityinen tuki kotiorganisaatiosi oikeustoimistolta. 

**Arkaluontoiset tiedot**: Arkaluontoiset tiedot ovat tietoja, jotka on suojattava luvattomalta käytöltä. Tietosuoja voi olla tarpeen oikeudellisista tai eettisistä syistä, henkilökohtaisen yksityisyyden ja yksinomaisuuden vuoksi. Arkaluontoiset tiedot voivat sisältää esimerkiksi:

* Henkilökohtaisia arkaluontoisia tietoja (esim. terveys, geneettiset ja henkilökohtaiset tiedot, rotu tai etninen alkuperä, poliittiset mielipiteet, uskonnolliset tai filosofiset uskomukset tai ammattiliittojen jäsenyys, geneettiset tiedot, biometriset tiedot luonnollisen henkilön yksilölliseen tunnistamiseen, terveyttä koskevat tiedot, seksielämää tai seksuaalista suuntautumista koskevat tiedot, rikostuomioita ja rikkomuksia tai niihin liittyviä turvallisuustoimenpiteitä koskevat tiedot, tunnistettavissa olevan henkilön tiedot)
* Ekologiset tiedot (esim. uhanalaisten lajien sijainti tai muut säilyttämistoimet)
* Luottamukselliset tiedot (esim. liikesalaisuudet)
* Tiedot, joita muuten pidetään arkaluontoisina