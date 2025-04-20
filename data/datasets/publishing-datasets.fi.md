# Datan julkistaminen {#publishing-datasets}

## Yleiskatsaus {#overview}

Usein dataan keskittyvä työ tuottaa uusia aineistoja, joko varsinaisina päätuloksina tai mahdollisesti tukimateriaalina päätuloksiin, kuten tieteellisiin julkaisuihin. Kun julkaiset aineistoja, huomion tulee olla siinä, että mahdollistetaan uusien tutkimusten tekeminen näiden aineistojen pohjalta joskus tulevaisuudessa. Julkaisemisen tulisi perustua yleisesti hyväksyttyihin standardeihin ja hyvään metatietoon, sillä aineistot saattavat päätyä täysin erilaisiin käyttökonteksteihin kuin missä ne on alun perin tuotettu. Usein tärkein tuleva käyttäjä aineistolle on kuitenkin alkuperäinen tekijä, joten kunnolliseen julkaisuun käytetty vaiva maksaa itsensä pian takaisin.

## Missä aineistoja kannattaa tallentaa ja julkaista {#where-to-host-and-publish-datasets}

Alla listatut palvelut ovat suomalaisia tai tuotettu yhteistyössä CSC:n kanssa, ja ne ovat ilmaisia loppukäyttäjille. Lisäksi on olemassa useita suositeltuja tallennuspaikkoja. Voit etsiä sopivia vaihtoehtoja osoitteesta [Re3data](https://www.re3data.org/), joka on tutkimusaineistojen rekisteri ja sisältää yksityiskohtaista tietoa lähes 3 000 tietovarannosta eri tieteenaloilla.

Mikäli mahdollista, käytä alakohtaisia tallennuspaikkoja aineistosi säilyttämiseen. Suosittelemme ottamaan yhteyttä oman organisaatiosi datatukeen saadaksesi lisäohjeita tutkimusaineiston avaamiseen.

[CSC:n aineiston julkaisemisen työkalut](https://research.csc.fi/en/service-catalog#open)

[Kuinka julkaista oma aineisto Fairdatassa](https://www.fairdata.fi/en/user-guides/fairdata-quick-guide/)

[EUDAT-palvelut](https://www.eudat.eu/)

[Kuinka julkaista paikkatietoaineisto Paituli-palvelussa](https://paituli.csc.fi/opendata.html)

[Esimerkkitapaus 1: Aineiston jakaminen tutkimushankkeen aikana, julkaise FAIR-muodossa kun valmis](https://research.csc.fi/example-case-1)

[Esimerkkitapaus 2: Aineiston elinkaari CSC:llä – keruusta säilytykseen](https://research.csc.fi/example-case-2)

## Aineistotyypit {#data-types}

Kun valitset, mitä tallennat tai/tai julkaiset, kannattaa tarkastella asiaa eri näkökulmista ja pohtia, mitä aineiston (uudelleen)käyttäjä näkee. Kuinka kauas artikkelisi lukija voi seurata prosessia kohti raaka-aineistoa, ennen kuin alkuperäisen prosessin toistaminen ei enää onnistu? Monissa tapauksissa ei ole mahdollista palata raaka-aineistoon, mutta jos aineiston dokumentointi, automaatio, lokien ja koodin tallennus sekä niiden versionhallinta tehdään alusta saakka, voidaan varmistaa mahdollisimman suuri läpinäkyvyys. Mikäli mahdollista (tämä riippuu vahvasti tieteenalasta), voi olla hyvä julkaista sekä raaka-aineisto että käsitelty aineisto asianmukaisella dokumentaatiolla.

![Aineistojen julkaisut](../../img/data-publications.png "Datan tyypit tekijän ja lukijan näkökulmasta")

Lisenssi: CC BY 4.0

Pohdi myös, mikä on se varsinainen datatuote, jonka julkaiset tieteellisen artikkelisi yhteydessä. Aineiston luokittelu voi olla hyödyllistä jo tutkimuksen alussa. Raaka-aineisto (raw data) on aineistoa, jonka keräät ja/tai digitoit tutkimustasi varten tai muuta aineistoa, joka on tallennettu ja otettu käyttöön eri lähteistä. Tarjolla oleva digitaalinen aineisto voi olla operatiivista (punainen) aineistoa, joka on julkaistu muussa tarkoituksessa ja hyvin dynaamisessa muodossa. **Operatiivinen aineisto** ei välttämättä ole viitattavissa eikä sen laatua ole tarkastettu lähteessä. Uudelleenkäyttöä varten aineistoa voidaan tallentaa operatiivisesta lähteestä tai sitä on jo kerätty ja julkaistu (kumulatiivisena/) **geneerisenä tutkimusdatan** (vihreä) aineistona. Geneerinen tutkimusdata on versionhallittua, dokumentoitua ja laadultaan tarkastettua, ja siihen tulisi olla mahdollista viitata. Tutkimuksesi tuloksena julkaistava aineisto on vakaa datatuote eli **tutkimusaineiston julkaisu** (sininen), joka koostuu (mahdollisuuksien mukaan) raaka-aineistosta ja dokumentaatiosta, joka kuvaa prosessin, joka on johtanut tuloksiin.

![Aineistotyypit](../../img/data_types.png "Operatiivinen data, geneerinen tutkimusdata ja tutkimusaineiston julkaisu")

Lisenssi: CC BY 4.0

## Pysyvät tunnisteet {#persistent-identifiers}

Pysyvät tunnisteet tarjoavat hallitun tavan yhdistää ja merkitä digitaalista tietoa. Käyttämällä tunnisteita, kuten DOI tai URN, kun julkaiset tai viittaat dataan, varmistat linkityksen säilyvän, vaikka nimet tai organisaatiot muuttuisivat. Tunnisteet ovat globaaleja ja yksilöllisiä, joten voit olla varma, että kyseessä on oikea aineisto tai että saat tunnustuksen omista julkaisuistasi.

Mitä enemmän pysyviä tunnisteita voit sisällyttää omiin työprosesseihisi, sitä parempaa ja helpompaa tiedonhallintasi on. Ota rohkeasti yhteyttä oman organisaatiosi tutkimusdatapalveluihin tai kirjastoon saadaksesi lisäapua.

!!! note "Lisätietoa"
    - [CSC:n tuki pysyville tunnisteille](https://wiki.eduuni.fi/x/9ZRYH)
    - [Viittaa dataasi – DataCite](https://datacite.org/cite-your-data.html)
    - [Digitaalisen objektin tunniste (DOI)](https://www.doi.org/)
    - [ORCID – tutkijatunniste](https://researcheridentifier.fi/)
    - [Digital Preservation Handbook](https://www.dpconline.org/handbook/technical-solutions-and-tools/persistent-identifiers) (Digital Preservation Coalition)
    - [ANDS Persistent Identifiers Expert Level Guide](https://www.ands.org.au/guides/persistent-identifiers-expert)

<iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="315" srcdoc="https://www.youtube.com/embed/_4cZVli_xiU" title="Manage well and get preserved – 3. Persistent identifiers" width="560"></iframe>

## Lisensointi & oikeudet {#licensing-rights}

Nykyisin aiemmin tuotettua tutkimusaineistoa on mahdollista hyödyntää monipuolisemmin uusissa tutkimuksissa, jolloin vältytään aineiston uudelleen keräämiseltä, uusien menetelmien kehittämiseltä tai koodin kirjoittamiselta alusta alkaen.

Kun käytät muiden tuottamaa aineistoa, heidän asettamat käyttöehdot tulee huomioida. Käyttöehdot määritellään yleensä lisenssissä, esimerkiksi avoimessa [Creative Commons](https://creativecommons.org/licenses/) -lisenssissä. Aineisto voi olla täysin vapaasti käytettävissä tai sen käyttöä voivat rajoittaa tietyt ehdot, jotka johtuvat yleensä tiedon arkaluonteisuudesta, liikesalaisuuksista tai tutkijoiden solmimista sopimuksista. Yleinen periaate on, että aineistoa voi käyttää sen käyttöehtojen mukaisesti.

Aineiston käyttöehdoista päättää aina aineiston tuottaja tai hän, jolle tuottaja on siirtänyt kyseisen aineiston oikeudet ([Tekijänoikeuslaki 404/1961](https://www.finlex.fi/en/legislation/translations/1961/eng/404)). Tarvittaessa voit ottaa yhteyttä aineiston omistajaan, jos käyttöön liittyy epäselvyyksiä.

### Kuinka lisensoida oma aineistosi? {#how-to-license-your-own-data}

Kun teet aineistoja saataville, on suositeltavaa käyttää lisenssejä. Näin voit esimerkiksi säilyttää tekijänoikeuden mutta sallia muiden kopioida, jakaa ja hyödyntää aineistoasi. [Creative Commons -lisenssejä](https://creativecommons.org/licenses/) (CC BY) käytetään yleisesti aineistojen lisensointiin. Creative commons -lisenssien skaala ulottuu julkisesta omistuksesta (ylhäällä kuvassa) kaikki oikeudet pidätettyihin (alhaalla). Kuvan vasen reuna esittää sallitut käyttötavat ja oikea lisenssikomponentit.

![Creative commons -lisenssien spektri](../../img/Creative_commons_license_spectrum.png "Creative commons license spectrum")

Lisenssi: CC BY 4.0

!!! note "Kokeile itse!"
    [License Chooser](https://creativecommons.org/choose/) (Creative Commons).

    **CC BY 4.0 -lisenssi** mahdollistaa aineistosi käytön, mutta vaatii, että alkuperäinen tekijä mainitaan.

    Voit antaa aineistosi myös **CC0-lisenssillä**. Tämä tarkoittaa, että annat muille täyden oikeuden käyttää aineistoa vapaasti.

## Käyttörajoitukset {#access-restrictions}

Aineiston julkaiseminen ei välttämättä tarkoita, että kaikkien pitää päästä todella käsiksi dataasi. Jos sinulla on huoli siitä, että aineiston avoin julkaiseminen voisi aiheuttaa haittaa jollekin henkilölle, taholle tai muutoin johtaa negatiivisiin seurauksiin, voit asettaa aineistolle käyttörajoituksia ja määritellä, miten aineistoon pääsee käsiksi. Tavallisimmin vaihtoehdot ovat:

1. **sallia kaikille** datasettiin liitettyjen tiedostojen lataaminen (Avoin),
1. sallia kaikkien ladata datasettiin liitetyt tiedostot **tietystä päivämäärästä alkaen** (Embargo),
1. sallia kaikkien **hakea käyttöoikeutta** datasettiin liitettyjen tiedostojen lataamiseksi (Välitetty käyttö),
1. **ei sallia** lainkaan datasettiin liitettyjen tiedostojen lataamista (Rajoitettu).

Riippumatta valitusta vaihtoehdosta aineiston kuvaileva metatieto on kuitenkin aina julkisesti nähtävillä julkaisuympäristössä. Eli vaikka tiedon käyttö olisi rajoitettua, julkaistun datan kuvailevat tiedot ovat näkyvillä. Kaikki rajoitukset tulee kuvata selkeästi ja yhteystiedot tulee ilmoittaa sekä pitää ajan tasalla.