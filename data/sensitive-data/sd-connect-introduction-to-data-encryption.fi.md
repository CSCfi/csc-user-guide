# Johdanto tietojen salaukseen, joka on yhteensopiva Sensitive Data -palveluiden kanssa {#introduction-to-data-encryption-compatible-with-sensitive-data-services}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/dI1Py_1gA-k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Sensitive Data -data, joka ladataan CSC:n pilvipalveluihin SD Connectin kautta tai ohjelmallisesti, tulee salata. Tämän luvun ohjeiden mukaisesti salatut tiedostot ovat yhteensopivia ja käytettävissä kaikissa Sensitive Data (SD) -palvelukomponenteissa. Näin SD Connect -palveluun tallennetut salatut tiedostot ovat saatavilla analyysia varten (käyttäen SD Desktop -palvelua) tai julkaistavaksi ja uudelleenkäytettäväksi hallitun pääsyn kautta (SD Submitin, Federated EGA:n tai SD Applyn kautta).

!!! Huom
    Datan salaaminen ei vaadi teknistä osaamista, mutta edellyttää tutustumista tähän käyttäjän oppaaseen ja videotuotantoihin. Tarjoamme myös vaiheittaiset ohjeistukset verkossa ja palvelupisteen kautta. Mikäli sinulla on kysyttävää tai jokin ohje kaipaa tarkennusta, älä epäröi [ottaa yhteyttä](../../support/contact.md) (aihe: Sensitive Data).

Olemme integroineet salauksen automaattisena vaiheena SD Connect -käyttöliittymään erityisesti alle 1 GB:n kokoisille tiedostoille. Kaikki SD Connectin kautta ladattu data salataan automaattisesti Sensitive Data -palveluiden julkisella salausavaimella. Voit kuitenkin valita erilaisia vaihtoehtoja datasi salaamiseen analyysia tai jakamista varten.

Palvelut käyttävät salaustapaa, jota kutsutaan _asymmetriseksi salaukseksi_, ja se perustuu kahteen toisiinsa liittyvään avaimen:

  * Julkista salausavainta käytetään datan salaukseen. Julkista avainta ei voi käyttää tietojen purkamiseen. Voit jakaa julkisen avaimesi esimerkiksi yhteistyökumppaneillesi, jolloin he voivat salata dataa sinun julkisella avaimellasi.

  * Salainen avain (myös yksityinen avain), jota käytetään sellaisten tiedostojen purkamiseen, jotka on salattu vastaavalla julkisella avaimella. Tämä avain on suojattu salasanalla eikä sitä voi jakaa muille.

Kun käytät SD Connectia datan lataamiseen CSC:lle, käytössäsi on useita salausvaihtoehtoja:

1. Oletusvaihtoehto data-analyysiin:

   * Oletussalausvaihtoehdoilla voit ladata datan SD Connectilla verkkoselaimella data-analyysia varten. Tiedostot salataan automaattisesti ja ovat analysoitavissa SD Desktopin kautta. Et kuitenkaan voi purkaa salasanoja ladattuasi tiedostot omalle tietokoneellesi tai organisaatiosi laskentaympäristöön. Kehitämme uutta ominaisuutta, joka mahdollistaa automaattisen salauksen purun SD Connectin kautta. Lisätietoja saat [ottamalla yhteyttä](../../support/contact.md) (Sensitive Data).

2. Useiden salausavainten lisääminen tiedon tallennukseen, jakamiseen ja siirtoon:

   * Voit ladata datan SD Connectin kautta verkkoselaimella ja lisätä oman julkisen salausavaimesi. Tiedostot salataan SD-palveluilla oletusarvoisesti, mutta voit myös lisätä oman salausavaimesi. Tällä tavalla voit myös ladata ja purkaa datatiedostot tarvittaessa.

   * Voit ladata datan SD Connectin kautta verkkoselaimella ja lisätä useita salausavaimia. Esimerkiksi oman julkisen avaimesi ja yhteistyökumppanisi julkisen salausavaimen. Myös tässä tapauksessa tiedostot salataan oletusarvoisesti SD-palveluiden salausavaimella ja ovat analysoitavissa SD Desktopin kautta. Lisäksi sekä sinä että yhteistyökumppanisi voitte tarvittaessa ladata ja purkaa datan.

Tätä salaustapaa varten käytetään Crypt4GH-nimistä työkalua, joka on alun perin suunniteltu ihmisen geneettisen datan salaukseen ja jakamiseen [Global Alliance for Genomics and Health](https://www.ga4gh.org/) (GA4GH) -standardin mukaisesti. Crypt4GH:ta voi käyttää minkä tahansa tiedoston (kuvat, audio, video, tekstitiedostot jne.) salaamiseen.
CSC on kehittänyt yksinkertaisen sovelluksen, jonka avulla voit **luoda omat salausavaimesi**.

Seuraavissa kappaleissa esitellään kaikki tarvittavat vaiheet, joiden avulla voit luoda salausavaimet, ladata ja salata tietosi SD Connectilla sekä purkaa tiedostot, kun lataat ne takaisin koneellesi. Voit luonnollisesti suorittaa jokaisen näistä vaiheista myös ohjelmallisesti.