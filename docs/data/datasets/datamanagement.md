# Vinkkejä tiedonhallintaan

## Yleiskatsaus {#overview}

Hyvä tutkimusdatan hallinta (RDM) on onnistuneen tutkimuksen perusta. RDM kattaa datan elinkaaren kaikissa vaiheissa, dataan luomisesta tai keräämisestä, datan hallintaan ja organisointiin projektin aikana, julkaisusta ja digitaalisesta säilyttämisestä projektin aktiivisen vaiheen jälkeen. Sen tarkoituksena on varmistaa tutkimuksen toistettavuus, joka on kaiken tieteellisen tutkimuksen perusvaatimus. Hyvä datanhallinta datan elinkaaren aikana on keskeistä datan jakamisen edistämiseksi ja datan pitkäaikaisen kestävyyden ja saavutettavuuden varmistamiseksi, ja siten sen uudelleenkäytön mahdollistamiseksi tulevaisuuden tieteessä.

!!! huom "FAIR-periaatteet"
    [FAIR-periaatteiden](https://www.go-fair.org/fair-principles/) mukaan datan tulisi olla
    
    - Löydettävissä
    - Saavutettavissa
    - Yhteentoimivaa
    - Uudelleen käytettävää
    
    [Tutustu periaatteisiin tämän videon avulla](https://youtu.be/K-kEvfaUJdA)
   

## Parhaat käytännöt {#best-practices}

Alla on joitakin ohjeita hyvän datanhallinnan käytänteille. Eri datanhallinnan sivustojen selaamisen avulla voit löytää ohjeita esimerkiksi datamuotojen valintaan, lisensointiin, pysyviin tunnisteisiin ja arkaluonteisen datan käsittelyyn.

![Tarkistuslista datanhallintasuunnitteluun](../../img/Checklist_for_DMP_v1.png "Tarkistuslista onnistuneeseen datanhallintasuunnitteluun")

Lisenssi: CC BY 4.0

### Pidä datanhallintasuunnitelma {#maintain-a-data-management-plan}

Tee selkeä suunnitelma datasi hallinnasta. Datanhallintasuunnitelma (lyhennettynä DMP) on asiakirja, joka kuvaa, miten käsittelet dataasi projektin aikana ja mitä datalle tapahtuu projektin päättyessä. Sen tulisi kattaa kaikki datan elinkaaren vaiheet lähtien löytämisestä, keräyksestä, organisoinnista, käytöstä, datan jakamiseen ja säilyttämiseen. Useimmat rahoittajatahot vaativat datanhallintasuunnitelman, kun rahoitus on myönnetty, ja DMP:ta tulee nähdä laadunvarmistustyökaluna, joka auttaa varmistamaan tutkimuksen toistettavuuden sekä datan yhteentoimivuuden ja uudelleenkäytettävyyden.

### Säilytä raakadata raakana {#keep-raw-data-raw}

Datan tulisi säilyttää raaka muodossaan aina kun mahdollista läpinäkyvyyden mahdollistamiseksi ja uudelleenanalyysin helpottamiseksi. Tämä helpottaa myös useiden tietolähteiden yhdistämistä. Saattaa olla järkevää tarjota sekä käsittelemättömiä että käsiteltyjä versioita datastasi, joko koodien tai selityksien avulla, miten käsitelty versio johdetaan.

### Luo analyysiin ystävällistä dataa {#create-analysis-friendly-data}

Hyödynnäksesi dataasi täysimäärin, sen tulisi olla rakenteellisesti sellaista, että käyttö, tulkinta ja analyysi on helppoa. Harkitse mitä dataa sinun tarvitsee käyttää, milloin ja miten, ja se auttaa sinua luomaan analyysiin ystävällistä dataa, sinulle ja mahdollisesti muille. Yksi mahdollinen rakenne on varastoida jokainen muuttuja sarakkeena, jokainen havainto rivinä ja jokainen havaintoyksikkö tyyppinä taulukkoon.

### Suorita laadunvalvontaa {#perform-quality-control}

Data, kuten muutkin tutkimuksen tuotokset, tulisi käydä läpi jonkinasteista laadunvalvontaa. Laadunvarmistus helpottaa oman datasi analysointia ja on olennaista, jos aiot jakaa datasi muiden kanssa. Voit aloittaa perus tarkastuksilla, kuten varmistamalla, ettei numeerisessa datassa ole ei-numeerisia arvoja ja tarkistamalla mittayksiköiden ja nimeämiskäytäntöjen johdonmukaisuuden.

### Käytä standardoituja, avoimia tiedostomuotoja {#use-standard-open-data-formats}

Jokaisella tutkijalla on omat suosikkityökalunsa datan tallentamiseen ja analysointiin. Jotta datasi olisi helppokäyttöistä, on parasta tallentaa se standardoituihin ja avoimiin [tiedostomuotoihin](metadata-and-documentation.md#files-and-file-formats), joita voi käyttää erilaiset ohjelmistot ja jotka pysyvät saavutettavissa ajan myötä (esim. CSV, XML). Tällaiset tiedostomuodot ovat myös hyviä ehdokkaita datan digitaaliseen säilyttämiseen.

### Käytä hyviä muuttujien nimiä ja nollaarvoja {#use-good-variable-names-and-null-values}

Ole johdonmukainen nimeämään muutettavat ja kirjaa riittävästi tietoa, jotta muutettavien ja arvojensa määritelmät ovat selkeitä. Seuraa käytänteitä tutkimusyhteisössäsi muuttujia nimetessäsi esim. käyttämällä täysiä taksonomisia nimiä. Monilla dataseteillä on myös puuttuvia tai tyhjiä datan arvoja, jotka tulisi merkata huolellisesti (esim. NaN), jotta ne erotetaan tosista nollista.

### Dokumentoi datan prosessointi {#document-your-data-processing}

Muista tallentaa ja raportoida, miten tutkimusdatan analysointi ja prosessointi on tehty. Tämä on välttämätöntä sekä toistettavuudelle että tutkimuksen laadun arvioinnille. Hyvä [dokumentoinnin puute](metadata-and-documentation.md#data-documentation-also-called-detailed-descriptive-metadata-or-data-level-metadata) johtaa usein datan häviämiseen. Jotta [data ja dokumentaatio pysyvät hyvin järjestettyinä](metadata-and-documentation.md#data-organization), käytössä tulisi olla versiokontrollijärjestelmä (manuaalinen tai automaattinen).

### Toistettavuus {#reproducibility}

Toistettavuus on tärkeä osa todisteiden tarjoamista tutkimustulosten oikeellisuudesta. Muiden tutkijoiden tulisi pystyä tarkastamaan työnkulku ja arvioimaan kaikki analyysin aikana tehdyt vaiheet sekä toistamaan ne. Toistettavuudella tarkoitetaan mahdollisuutta saavuttaa yhteneviä tuloksia käyttämällä samaa dataa ja koodia kuin alkuperäisessä tutkimuksessa (laskennallinen toistettavuus). Replikoitavuus tarkoittaa yhtenevien tulosten saavuttamista tutkimuksissa, joiden tarkoituksena on vastata samaan tieteelliseen kysymykseen käyttämällä uutta dataa tai muita uusia laskentamenetelmiä. Tässä tapauksessa uusi data kerätään tai luodaan. [Tutkimusohjelmistojen ja työnkulkujen dokumentointi ja jakaminen](metadata-and-documentation.md#versioning) on keskeinen osa toistettavuutta.

### Tarjoa metatietoja {#provide-metadata}

[Metatiedot](metadata-and-documentation.md#metadata-types) ovat kontekstuaalista tietoa datasta ja sen alkuperästä, joka on tarpeen datan tulkinnassa. Metatietojen tarjoaminen mahdollistaa sen, että sinä ja muut, jotka haluavat laajentaa työtäsi, voitte palata siihen myöhemmin. Kattavien metatietojen tarjoaminen oman tieteenalan käytäntöjen mukaan tekee datastasi löydettävää ja uudelleenkäytettävää.

### Hanki tunnisteita datallesi {#get-identifiers-for-your-data}

Tutkimuksessa ja julkaisuissa käytetyn datan tulisi olla yksilöitävissä. Varmista, että käyttämäsi tietovarasto antaa datallesi [pysyvän tunnisteen](publishing-datasets.md#persistent-identifiers) (esim. DOI, URN). Käytä datasetisi tunnistetta, kun jaat tai käytät sitä, jotta se kerää viittauksia puolestasi.

### Huolehdi tallennuksesta {#take-care-of-storage}

[Talleta datasi](publishing-datasets.md#where-to-host-and-publish-datasets) tunnettuun ja luotettuun arkistoon varmistaaksesi datan turvallisen säilymisen. Huomioi organisaatiosi datakäytäntö ja tutkimusrahoittajien sekä julkaisijoiden vaatimukset. Mieti, missä muut alan tutkijat tallentavat datansa, mitä palveluita tietovarastot tarjoavat ja mitä tarpeita sinulla on esimerkiksi tallennuskiintiön ja datan avoimuuden suhteen.

### Avaa datasi {#open-your-data}

Datasharing on yhä enenevässä määrin rahoittajien ja tieteellisten julkaisujen vaatimus, sillä se hyödyttää laajasti tieteellistä yhteisöä. Se on myös hyödyllistä datan kerääjille lisäämällä näkyvyyttä, yhteistyömahdollisuuksia ja ansioita. Sinun tulisi harkita datasi jakamista, jotta muut voivat saada pääsyn siihen ja siteerata sitä. Varmista datasi varustaminen tunnetulla [lisenssillä](publishing-datasets.md#licensing-rights) (esim. Creative Commons -lisenssit), jotta muut tietävät mitä voivat ja mitä eivät voi tehdä datan kanssa.

!!! huom "Lisälukemista ja resursseja datanhallinnasta"
    - [Datanhallinnan tarkistuslista](https://www.fairdata.fi/en/why-fairdata/data-management-checklist/) [Fairdata.fi:ssä](http://fairdata.fi/)
    - Suomalaisen Sosiaalitieteen Arkiston [Datanhallinnan ohjeet](http://www.fsd.uta.fi/aineistonhallinta/en/)
    - Suomen Akatemian [Avoimen tieteen sivut](https://www.aka.fi/en/research-funding/responsible-science/open-science/)
    - ELIXIRin Research Data Management Kit, [RDMkit](https://rdmkit.elixir-europe.org/), on online-opas, joka sisältää hyviä datanhallinnan käytänteitä koko datan elinkaaren ajalle
    - [FAIRsharing.org](https://fairsharing.org/) Kuratoitu, informatiivinen ja opettavainen resurssi data- ja metadatastandardeista, tietokannoista ja datapolitiikoista.
    - [CSC:n videot tutkimusdatan hallinnasta](https://video.csc.fi/playlist/details/0_xtsuml9w)  


## Tutkimusdatan hallinnan budjetointi {#budgeting-research-data-management}

Datanhallinnan prosessit saattavat aiheuttaa kustannuksia. Tutkijoiden tulisi suunnitella näiden kustannusten ja resurssien kohdentamisen kattaminen projektin alkuvaiheessa. Suurin osa rahoittajista hyväksyy datanhallinnan lailliseksi kustannukseksi, joka voidaan ja pitäisi sisällyttää projektin budjettiin.

Arvioi tarvittavat resurssit datan hallintaan, jakamiseen ja säilyttämiseen. Pohdi lisälaskentavälineiden ja resurssien tarvetta.

Projektin budjetointi ja kululaskenta riippuu usein institutionaalisista resursseista, palveluista ja politiikoista. Muista konsultoida organisaatiosi datasupport-toimistoa.

!!! huom "Esimerkkejä mahdollisista datanhallinnan kustannuksista"
    
    - Tuleeko datan säilytyksestä kustannuksia? Tarvitsetteko lisäpalvelintilaa tai räätälöityjä ratkaisuja?
    - Suunnitteletteko käyttävänne kaupallisia palveluita, esimerkiksi datan anonymisointiin, äänimateriaalin litteroimiseen tai elektronisen laboratoriovihkon käyttöön?
    - Tarvitsetteko lisäpalkattua apua datan organisointiin ja dokumentointiin; ovatko datatiedostosi, -tason yms. tallennettu yhtenäisessä muodossa ja selkeästi nimetty ja hyvin järjestetty ja ymmärrettävä? Korkeammat kulut ovat odotettavissa, jos datan organisointi on laiminlyöty projektin aikana.
    - Kustannuksia voi aiheutua myös silloin, kun arkistoitte ja avaatte datan.

Lue lisää [CSC maksuttomista käyttötapauksista ja hintatietoja](https://research.csc.fi/pricing-and-resources).


## Arkaluontoisen datan hallinta {#how-to-manage-sensitive-data}

EU:n yleinen tietosuoja-asetus (GDPR) hahmottelee arkaluontoisen datan käsittelyn periaatteet, antamatta täsmällisiä teknisiä yksityiskohtia siitä, miten arkaluontoista dataa käsitellään. Voit oppia lisää arkaluontoisesta datasta [CSC:n arkaluontoisen datan määrittelyssä](https://research.csc.fi/en/definition-of-sensitive-data). Tässä vaiheessa korostetaan vain joitakin perusperiaatteita liittyen arkaluonteiseen henkilötietoon.

1. Minimoi data. Tämä tarkoittaa, että käsittelet vain ne tiedot, jotka ovat ehdottoman tarpeellisia. 
2. Anonymisoi tai pseudonymisoi data aina kun mahdollista. 
3. Kryptaa data.
4. Tuhoa data, jota et tarvitse. 

Muista nimittää ja määritellä
  - **Rekisterinpitäjä** (esim. päätutkija yksin tai yhdessä toisen henkilön tai oikeushenkilön kanssa), joka määrittää datan käsittelykeinot ja -tavat, tarkoittaen että he kontrolloivat, miten data käsitellään ja mihin tarkoituksiin.
  - **Tietojen käsittelijä**, joka käsittelee dataa rekisterinpitäjän puolesta.

!!! huom "Lisätietoa arkaluontoisen datan hallinnasta"
    - [CSC:n Sensitive Data Services for Research](https://research.csc.fi/sensitive-data)
    - [Arkaluontoisen datan hallinta](https://research.csc.fi/en/managing-sensitive-data)
    - [Käyttöopas arkaluontoisen datan palveluihin](../sensitive-data/index.md)
    - [Työkalut asiakaspään kryptaukseen Allas-palvelussa](../Allas/allas_encryption.md)

<iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="315" srcdoc="https://www.youtube.com/embed/29XmiG5Zj0s" title="Webinaari: Mitkä ovat politiikat ja mahdollisuudet arkaluontoisen datan hallintaan?" width="560"></iframe>


**Parhaiden käytäntöjen tarkastelun lähteet** {#sources-for-this-best-practice-review}

Goodman, A., Pepe, A., Blocker, et. al. (2014). Kymmenen yksinkertaista sääntöä tieteellisen datan huoltoon ja ruokintaan. PLoS Computational Biology, 10(4), e1003542. [http://doi.org/10.1371/journal.pcbi.1003542](http://doi.org/10.1371/journal.pcbi.1003542)

Griffin PC, Khadake J, LeMay KS et al. Best practice data life cycle approaches for the life sciences [versio 2; vertaisarviointi: 2 hyväksytty]. F1000Research 2018, 6:1618 [https://doi.org/10.12688/f1000research.12344.2](https://doi.org/10.12688/f1000research.12344.2)

Hart, E. M., Barmby, P., LeBauer, D., et al. (2016). Kymmenen yksinkertaista sääntöä digitaalisen datan tallentamiselle. PLoS Computational Biology, 12(10), e1005097. [http://doi.org/10.1371/journal.pcbi.1005097](http://doi.org/10.1371/journal.pcbi.1005097)

Wilkinson, M., Dumontier, M., Aalbersberg, I. et al. The FAIR Guiding Principles for scientific data management and stewardship. Sci Data 3, 160018 (2016). [https://doi.org/10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. PLoS Computational Biology, 13(6), e1005510. [http://doi.org/10.1371/journal.pcbi.1005510](http://doi.org/10.1371/journal.pcbi.1005510)