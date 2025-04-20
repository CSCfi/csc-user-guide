## Hyödyllistä terminologiaa: palvelut ja tekniset näkökohdat {#useful-terminology-services-and-technical-aspects}

**Allas**: CSC:n pilvitallennuspalvelu. SD Connect on käyttöliittymä, joka mahdollistaa arkaluonteisten tietojen salaamisen ja tallentamisen Allas-palveluun. Käyttäjät voivat myös käyttää Allasta ohjelmallisesti ei-arkaluonteisen datan rajapinnoilla.

**Laskentayksiköt**: laskentayksiköillä seurataan resurssien käyttöä. SD Connectin ja SD Desktopin käyttö kuluttaa laskentayksiköitä.

**Bucket/Container**: Näillä termeillä tarkoitetaan pääkansiota (teknisesti juurikansiota), johon salatut tiedostot tallennetaan SD Connectissa tai Allas-palvelussa. Bucketin/containerin nimi on näkyvissä internetissä. Voit luoda useita bucketeja samaan projektiin (enintään 1000), mutta jokaisella bucketilla tulee olla yksilöllinen nimi koko tallennusjärjestelmässä (mukaan lukien muut projektit). Oletusarvoisesti bucketin data on vain projektin jäsenten saatavilla. Voit kuitenkin jakaa ja antaa käyttöoikeuksia myös muille CSC:n projekteille tai käyttäjille SD Connectin avulla.

**CSC-projekti**: CSC:n palveluiden käyttö perustuu projekteihin: kaikki CSC:ssä olevat tietosi kuuluvat projektiin. Jokaisessa projektissa on pääkäyttäjä, CSC-projektipäällikkö, joka voi lisätä jäseniä ja hallita palveluiden käyttöoikeuksia. Projektipäällikkö on vastuussa projektin toiminnoista ja toimii rekisterinpitäjänä (tai akateemisen organisaation edustajana). Projektipäällikön tehtäviin kuuluu esimerkiksi kuvata, minkä tyyppistä arkaluonteista dataa projektissa käsitellään.

**Levykiintiö**: CSC-palveluiden käyttäjille tarjolla oleva tallennustila. SD Connectin oletuskiintiö on 10 Tt. Voit hakea lisätilaa ottamalla yhteyttä [CSC Service Desk](../../support/contact.md) -palveluun.

**Monivaiheinen tunnistautuminen**: Kun kirjaudut SD Desktop -palveluun, sinun tulee tehdä lisävahvistus pelkän käyttäjätunnuksen ja salasanan lisäksi. Näin tilisi on turvallisempi. Tätä lisävahvistusvaihetta kutsutaan nimellä: "Kaksivaiheinen tunnistautuminen" tai "Monivaiheinen tunnistautuminen", koska todistat henkilöllisyytesi eri tavalla. Tässä tapauksessa sinun tulee syöttää kertakäyttöinen, 6-numeroinen koodi, jonka saat avaamalla mobiilisovelluksen. Koodi on yksilöllinen ja voimassa vain rajoitetun ajan.

**Objekti**: Tekninen nimitys tiedostolle, joka on tallennettu pilviobjektitallennukseen, kuten Allas (tai ladattu CSC:hen SD Connect -palvelun kautta). Tämä määritelmä korostaa, että SD Connectissa/Allas-palvelussa tallennettuja tiedostoja ei voi suoraan muokata, ellei niitä siirretä tai kopioida laskenta-ympäristöön. Niihin voi kuitenkin päästä pilvilaskenta-ympäristössä vain lukuoikeuksin (esim. SD Desktopista).

**Projektitunniste**: Synonyymi CSC:n projekti-ID:lle komentorivityökalun käytössä. SD Connectin käyttöliittymässä tieto löytyy kohdasta User Information > Project usage ja näkyy 32:numeron ja kirjaimen sarjana: esim. `AUTH_3a66dbf90b2940dc9c651362af595b23`.

**Virtuaalikone (VM) tai virtuaalityöpöytä**: Virtuaalinen laskenta-ympäristö (tai virtuaalitietokone), joka toimii kuten fyysinen tietokone. Siinä on prosessori, muistia ja käyttöjärjestelmä, mutta se on olemassa vain koodina tai CSC:n tietokeskuksen isäntäpalvelimen osiona. Arkaluonteisiin tietoihin käytetyt virtuaalikoneet ovat täysin eristettyjä internetistä turvallisuussyistä.

**Virtuaalikoneen flavor (VM flavor) tai valmiiksi rakennettu työpöytävalinta**: Flavor määrittää pilvilaskenta-ympäristön resurssit ja kokoonpanot. Se määrittelee virtuaalikoneelle varattavan laskenta-, muisti- ja tallennuskapasiteetin.


## Hyödyllistä terminologiaa: tietosuoja {#useful-terminology-data-protection}

**Rekisterinpitäjä ja henkilötietojen käsittelijä** GDPR:n mukaisesti rekisterinpitäjä on henkilö tai organisaatio, joka määrittelee henkilötietojen käsittelyn tarkoitukset ja keinot, ja se on yleensä akateeminen organisaatio. Henkilötietojen käsittelijä puolestaan on henkilö tai organisaatio, joka käsittelee henkilötietoja rekisterinpitäjän lukuun, esimerkiksi IT-palveluntarjoaja, tässä tapauksessa CSC.

**Tietojenkäsittelysopimus (DPA)**: Tietojenkäsittelysopimus (DPA) on rekisterinpitäjän ja henkilötietojen käsittelijän välinen sopimus. Se määrittelee tietojenkäsittelyn yksityiskohdat, kuten laajuuden ja tarkoituksen, sekä rekisterinpitäjän ja käsittelijän välisen suhteen. Lisätietoja löydät kohdasta [kun projektisi käsittelee henkilötietoja](../../accounts/when-your-project-handles-personal-data.md#data-processing-agreement) tämän oppaan alussa sekä [CSC:n yleiset käyttöehdot](https://research.csc.fi/general-terms-of-use) ja [CSC:n tietojenkäsittelysopimus](https://research.csc.fi/data-processing-agreement) sivustolla research.csc.fi.

**Tietosuojaa koskeva vaikutustenarviointi (DPIA)**: Tietosuojaa koskeva vaikutustenarviointi (DPIA) vaaditaan GDPR:n mukaan silloin, kun toimenpiteet "todennäköisesti aiheuttavat suuren riskin luonnollisten henkilöiden oikeuksille ja vapauksille". Lisätietoja saat [täältä](https://tietosuoja.fi/en/list-of-processing-operations-which-require-dpia) tietosuojavaltuutetun toimiston sivulta ja tarvittaessa oman organisaatiosi lakipalveluista.

**Arkaluonteiset tiedot**: Arkaluonteinen tieto on tietoa, jota on suojeltava luvattomalta käytöltä. Tietosuoja voi olla tarpeen oikeudellisista tai eettisistä syistä, yksityisyyden suojaamiseksi tai omistuksellisista syistä. Arkaluonteisia tietoja voivat olla esimerkiksi:

* Henkilöön liittyvät arkaluonteiset tiedot (esim. terveys-, geneettiset ja henkilötiedot, rotu tai etninen alkuperä, poliittiset mielipiteet, uskonnolliset tai filosofiset vakaumukset tai ammattiliittojen jäsenyys, geneettiset tiedot, biometriset tiedot luonnollisen henkilön yksilölliseen tunnistamiseen, terveyttä koskevat tiedot, luonnollisen henkilön seksuaalielämää tai seksuaalista suuntautumista koskevat tiedot, rikostuomiot ja rikkomukset tai niihin liittyvät turvallisuustoimenpiteet, tiedot, jotka voivat tunnistaa henkilön)
* Ekologiset tiedot (esim. uhanalaisten lajien sijainnit tai muut suojelutoimet)
* Luottamukselliset tiedot (esim. liikesalaisuudet)
* Muulla tavoin arkaluonteisiksi katsottava tieto