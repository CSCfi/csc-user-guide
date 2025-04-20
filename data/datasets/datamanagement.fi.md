# Vinkkejä aineistonhallintaan {#tips-for-data-management}

## Yleiskatsaus {#overview}

Hyvä tutkimusaineiston hallinta (RDM, Research Data Management) on onnistuneen tutkimuksen perusta. Aineistonhallinta kattaa koko aineiston elinkaaren: aineiston luomisesta tai keräämisestä, sen hallintaan ja organisointiin projektin aikana, julkaisuun sekä digitaaliseen säilytykseen projektin aktiivisen vaiheen jälkeen. Tarkoituksena on varmistaa tutkimuksen toistettavuus, mikä on kaiken tieteellisen tutkimuksen keskeinen edellytys. Hyvä aineistonhallinta koko aineiston elinkaaren ajan on ratkaisevaa aineiston jakamisen helpottamiseksi sekä aineiston pitkäaikaisen säilyvyyden ja saavutettavuuden takaamiseksi ja siten myös sen uudelleenkäytölle tulevaisuuden tutkimuksessa.

!!! note "FAIR-periaatteet"
    [FAIR-periaatteiden](https://www.go-fair.org/fair-principles/) mukaan aineiston tulisi olla

    - Löydettävissä
    - Saavutettavissa
    - Yhteentoimivaa
    - Uudelleenkäytettävää

    [Tutustu periaatteisiin tällä videolla](https://youtu.be/K-kEvfaUJdA)

## Parhaat käytännöt {#best-practices}

Alla on ohjeita hyvään aineistonhallintaan. Selaamalla aineistonhallinnan sivuja löydät ohjeita esimerkiksi aineistomuotojen valintaan, lisensointiin, pysyviin tunnisteisiin ja arkaluontoisen aineiston käsittelyyn.

![Checklist for data management planning](../../img/Checklist_for_DMP_v1.png "Checklist for how to be successful in data management planning")

Lisenssi: CC BY 4.0

### Laadi aineistonhallintasuunnitelma {#maintain-a-data-management-plan}

Tee selkeä suunnitelma aineistosi hallintaa varten. Aineistonhallintasuunnitelma (DMP, Data Management Plan) on asiakirja, joka kuvaa, miten käsittelet aineistoasi projektin aikana ja mitä aineistolle tapahtuu projektin päätyttyä. Suunnitelman tulisi kattaa kaikki aineiston elinkaaren vaiheet löytämisestä, keruusta, organisoinnista ja käytöstä aina aineiston jakamiseen ja säilytykseen. Useimmat rahoittajat vaativat aineistonhallintasuunnitelman, kun rahoitus on myönnetty, ja DMP:tä tulisi pitää laadunvarmistuksen välineenä, joka auttaa varmistamaan tutkimuksen toistettavuuden sekä aineiston yhteentoimivuuden ja uudelleenkäytettävyyden.

### Säilytä alkuperäinen aineisto raakana {#keep-raw-data-raw}

Aineisto tulisi aina, kun mahdollista, säilyttää alkuperäisessä, käsittelemättömässä muodossaan läpinäkyvyyden mahdollistamiseksi ja uudelleenanalysoinnin helpottamiseksi. Tämä auttaa myös yhdistämään useita aineistolähteitä. On hyödyllistä tarjota sekä käsittelemätön että käsitelty versio aineistosta, sekä ohjeet tai koodi tiedon jalostamiseen.

### Luo analyysikelpoista aineistoa {#create-analysis-friendly-data}

Jotta aineistosta saisi täyden hyödyn irti, sen tulisi olla rakenteeltaan sellainen, että käyttö, tulkinta ja analyysi ovat helppoa. Jo etukäteen miettiminen, mitä tietoja tarvitset, milloin ja miten, auttaa luomaan analyysikelpoista aineistoa itsellesi ja muille. Yksi tapa on järjestää aineisto niin, että jokainen muuttuja on omassa sarakkeessaan, jokainen havainto omassa rivissään ja jokainen havaintoyksikkö omassa taulukossaan.

### Tee laadunvarmistus {#perform-quality-control}

Aineisto, kuten muutkin tutkimustuotokset, tulisi tarkistaa laadunvarmistuksen keinoin. Laadunvarmistus helpottaa oman aineiston analysointia ja on erityisen tärkeää, jos haluat jakaa aineistosi muiden kanssa. Voit aloittaa yksinkertaisilla järkevyystarkistuksilla, kuten varmistamalla, ettei numeerisessa aineistossa ole ei-numeerisia arvoja ja että mittayksiköt ja nimeämiskäytännöt ovat johdonmukaisia.

### Käytä standardeja, avoimia aineistomuotoja {#use-standard-open-data-formats}

Jokaisella tutkijalla on omat suosikkityökalunsa aineiston tallentamiseen ja analysointiin. Jotta aineistosi olisi helppokäyttöistä, se kannattaa tallentaa standardiin ja avoimeen [tiedostomuotoon](metadata-and-documentation.md#files-and-file-formats), jota monipuoliset ohjelmistot tukevat ja joka pysyy saavutettavana pitkällä aikavälillä (esim. CSV, XML). Tällaiset aineistomuodot ovat myös hyviä digitaalisessa säilytyksessä.

### Käytä hyviä muuttujanimiä ja merkitse puuttuvat arvot {#use-good-variable-names-and-null-values}

Ole johdonmukainen muuttujien nimeämisessä ja kirjaa riittävästi tietoa, jotta sekä muutujien että arvojen merkitys on ymmärrettävä. Noudata oman tieteenalasi nimeämiskäytäntöjä, esimerkiksi käytä täydellisiä taksonomisia nimiä. Useissa aineistoissa on puuttuvia tai tyhjiä arvoja, jotka tulee merkitä huolellisesti (esim. NaN), jotta ne erottuvat oikeista nollista.

### Dokumentoi käsittelyprosessisi {#document-your-data-processing}

Muista tallentaa ja raportoida, miten tutkimusaineistosi on analysoitu ja käsitelty. Tämä on välttämätöntä sekä toistettavuuden että tutkimuksen laadun arvioinnin kannalta. Hyvän [aineiston dokumentoinnin](metadata-and-documentation.md#data-documentation-also-called-detailed-descriptive-metadata-or-data-level-metadata) puute johtaa usein aineiston katoamiseen. [Jäsentääksesi aineiston ja dokumentaation hyvin](metadata-and-documentation.md#data-organization), ota käyttöön versiohallintajärjestelmä (manuaalinen tai automaattinen).

### Toistettavuus {#reproducibility}

Toistettavuus on tärkeä osa tutkimustulosten oikeellisuuden osoittamista. Muiden tutkijoiden täytyy pystyä tarkistamaan työnkulku ja arvioimaan kaikki analyysin vaiheet sekä toistamaan ne. Toistettavuus tarkoittaa mahdollisuutta saada johdonmukaiset tulokset käyttämällä alkuperäisen tutkimuksen aineistoa ja koodia (laskennallinen toistettavuus). Replikoitavuus tarkoittaa johdonmukaisten tulosten saamista eri tutkimuksissa, jotka pyrkivät vastaamaan samaan tieteelliseen kysymykseen uudella aineistolla tai menetelmällä. Tällöin kerätään tai luodaan uutta aineistoa. [Tutkimusohjelmistojen ja työnkulkujen dokumentointi ja jakaminen](metadata-and-documentation.md#versioning) ovat olennaisia osia toistettavuuden varmistamisessa.

### Lisää metatiedot {#provide-metadata}

[Metatiedot](metadata-and-documentation.md#metadata-types) ovat aineiston ja sen alkuperän taustatietoja, jotka ovat välttämättömiä aineiston tulkinnalle. Metatiedon tarjoaminen mahdollistaa sen, että sinä ja muut työstä kiinnostuneet voivat palata siihen myöhemmin. Tarjoamalla kattavat metatiedot tieteenalasi käytäntöjen mukaisesti teet aineistostasi löydettävää ja uudelleenkäytettävää.

### Hanki aineistolle tunniste {#get-identifiers-for-your-data}

Tutkimuksessa ja julkaisuissa käytetyn aineiston tulee olla yksiselitteisesti tunnistettavissa. Varmista, että käyttämäsi palvelu tarjoaa aineistoillesi [pysyvän tunnisteen](publishing-datasets.md#persistent-identifiers) (esim. DOI, URN). Käytä aineiston tunnistetta sen jakamisessa ja hyödyntämisessä, jotta siitä kertyy viittauksia sinulle.

### Huolehdi tallennuksesta {#take-care-of-storage}

[Talleta aineistosi](publishing-datasets.md#where-to-host-and-publish-datasets) hyvämaineiseen, luotettavan tahon ylläpitämään palveluun, jotta se tallentuu turvallisesti. Huomioi organisaatiosi tietopolitiikka sekä rahoittajien ja lehtien vaatimukset. Selvitä myös, mihin kollegasi alalla tallentavat aineistonsa, millaisia palveluita tallennuspalvelut tarjoavat ja mitä tarpeita sinulla on esimerkiksi tallennuskapasiteetin ja avoimuuden suhteen.

### Avaa aineistosi {#open-your-data}

Aineiston jakamista vaativat yhä useammin rahoittajat ja tieteelliset lehdet, sillä se hyödyttää koko tiedeyhteisöä. Se on usein hyödyllistä myös aineiston kerääjälle kasvattaen näkyvyyttä, yhteistyötä ja ansioita. Harkitse aineistosi jakamista, jotta muut voivat hyödyntää ja viitata siihen. Lisää aineistoon [vakiolisenssi](publishing-datasets.md#licensing-rights) (esim. Creative Commons), jotta muut tietävät, mitä voivat ja eivät voi sille tehdä.

!!! note "Lisälukemista ja aineistonhallinnan resursseja"
    - [Aineistonhallinnan muistilista](https://www.fairdata.fi/en/why-fairdata/data-management-checklist/) [Fairdata.fi:n](http://fairdata.fi/) sivuilla
    - Suomen sosiaalitieteellisen tietoarkiston [Aineistonhallintaohjeet](http://www.fsd.uta.fi/aineistonhallinta/en/)
    - Suomen Akatemian [Avoimen tieteen sivut](https://www.aka.fi/en/research-funding/responsible-science/open-science/)
    - ELIXIR:n Research Data Management Kit, [RDMkit](https://rdmkit.elixir-europe.org/), on verkko-opas hyvistä aineistonhallinnan käytännöistä koko aineiston elinkaaren ajan
    - [FAIRsharing.org](https://fairsharing.org/) Kuratoitu, informatiivinen ja koulutuksellinen resurssi data- ja metatietostandardeista sekä data- ja tietokantapolitiikoista.
    - [CSC:n tutkimusaineistojen hallinnan videot](https://video.csc.fi/playlist/details/0_xtsuml9w)


## Aineistonhallinnan budjetointi {#budgeting-research-data-management}

Aineistonhallinnan toimenpiteistä voi aiheutua kustannuksia. Tutkijan kannattaa suunnitella nämä kustannukset ja resurssien kohdentaminen jo projektin alkuvaiheessa. Useimmat rahoittajat hyväksyvät aineistonhallinnan projektin budjettiin sisällytettävänä kustannuksena.

Arvioi resurssit, joita tarvitset aineiston hallintaan, jakamiseen ja säilyttämiseen. Huomioi myös mahdolliset tietojärjestelmät ja lisäresurssit, joita tarvitset.

Budjetointi ja kustannuslaskenta perustuu usein organisaation omiin palveluihin ja politiikkoihin. Muistathan konsultoida organisaatiosi data-tukea.

!!! note "Esimerkkejä aineistonhallinnan mahdollisista kustannuksista"

    - Syntyykö aineiston tallentamisesta kustannuksia? Tarvitsetko lisää palvelintilaa tai räätälöityjä ratkaisuja?
    - Aiotko käyttää kaupallisia palveluita esimerkiksi aineiston anonymisointiin, ääniaineiston litterointiin tai sähköiseen laboratorion muistiinpanoon?
    - Tarvitsetko lisää palkattua apua aineiston organisointiin ja dokumentointiin; ovatko datatiedostot, taulukot ym. tallennettu yhtenäisessä muodossa, hyvin nimettyinä, järjestettyinä ja helposti ymmärrettävinä? Kustannukset nousevat, jos organisointi on laiminlyöty projektin aikana.
    - Kun arkistoit ja avaat aineistosi, syntyykö siitä kustannuksia?

Lue lisää [CSC:n maksuttomista käyttötapauksista ja hinnoittelusta](https://research.csc.fi/pricing-and-resources).


## Miten hallita arkaluontoista tietoa {#how-to-manage-sensitive-data}

EU:n yleinen tietosuoja-asetus (GDPR) määrittelee periaatteet arkaluontoisen datan käsittelyyn antamatta tarkkoja teknisiä ohjeita käsittelystä. Voit lukea lisää arkaluontoisesta datasta [CSC:n määritelmästä](https://research.csc.fi/en/definition-of-sensitive-data). Tässä korostetaan vain perusperiaatteita arkaluontoisten henkilötietojen käsittelyssä.

  1. Minimoi tiedon määrä. Tämä tarkoittaa, että sinun tulee käsitellä vain ehdottoman välttämätöntä tietoa.
  2. Anonymisoi tai pseudonymisoi tiedot aina kun mahdollista.
  3. Salaa aineisto.
  4. Tuhoa tarpeeton data.

Muista nimetä ja tunnistaa
  - **Rekisterinpitäjä** (esim. vastuullinen tutkija yksin tai yhdessä toisen henkilön tai oikeushenkilön kanssa), joka määrittelee tiedon käsittelyn keinot ja tarkoitukset, eli päättää, miten dataa käsitellään ja mihin tarkoitukseen.
  - **Käsittelijä**, joka käsittelee tietoja rekisterinpitäjän puolesta.

!!! note "Lisätietoa arkaluontoisen datan hallinnasta"
    - [CSC:n Sensitive Data Services for Research](https://research.csc.fi/sensitive-data)
    - [Managing sensitive data](https://research.csc.fi/en/managing-sensitive-data)
    - [Sensitive Data Services for Research – käyttöohje](../sensitive-data/index.md)
    - [Allas-palvelun asiakaspään salausvälineet](../Allas/allas_encryption.md)

<iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="315" srcdoc="https://www.youtube.com/embed/29XmiG5Zj0s" title="Webinar: What are the policies and possibilities for managing your sensitive data?" width="560"></iframe>


**Tämän parhaiden käytäntöjen katsauksen lähteet**

Goodman, A., Pepe, A., Blocker, et. al. (2014). Ten Simple Rules for the Care and Feeding of Scientific Data. PLoS Computational Biology, 10(4), e1003542. [http://doi.org/10.1371/journal.pcbi.1003542](http://doi.org/10.1371/journal.pcbi.1003542)

Griffin PC, Khadake J, LeMay KS et al. Best practice data life cycle approaches for the life sciences [version 2; peer review: 2 approved]. F1000Research 2018, 6:1618 [https://doi.org/10.12688/f1000research.12344.2](https://doi.org/10.12688/f1000research.12344.2)

Hart, E. M., Barmby, P., LeBauer, D., et al. (2016). Ten Simple Rules for Digital Data Storage. PLoS Computational Biology, 12(10), e1005097. [http://doi.org/10.1371/journal.pcbi.1005097](http://doi.org/10.1371/journal.pcbi.1005097)

Wilkinson, M., Dumontier, M., Aalbersberg, I. et al. The FAIR Guiding Principles for scientific data management and stewardship. Sci Data 3, 160018 (2016). [https://doi.org/10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. PLoS Computational Biology, 13(6), e1005510. [http://doi.org/10.1371/journal.pcbi.1005510](http://doi.org/10.1371/journal.pcbi.1005510)