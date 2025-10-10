[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Johdanto Sensitive Data -palveluiden kanssa yhteensopivaan tietojen salaukseen { #introduction-to-data-encryption-compatible-with-sensitive-data-services }

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/dI1Py_1gA-k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


SD Connectin avulla tai ohjelmallisesti CSC:n pilvipalveluihin ladattavat arkaluonteiset tiedot on salattava. Tässä luvussa annettujen ohjeiden mukaisesti salatut tiedostot ovat yhteensopivia ja käytettävissä kaikkien Sensitive Data (SD) -palvelukomponenttien kautta. Näin SD Connect -palveluun tallennetut salatut tiedostot ovat käytettävissä analysointiin (SD Desktop -palvelulla) tai julkaisuun ja uudelleenkäyttöön valvotun pääsyn piirissä (SD Submitin, Federated EGA:n tai SD Applyn kautta). 

!!! Note
    Tietojen salaaminen ei vaadi teknistä asiantuntemusta, mutta edellyttää perehtymistä alla olevaan käyttöoppaaseen ja video-oppaisiin. Tarjoamme myös vaiheittaiset ohjeet verkossa tai palvelupisteen kautta. Jos sinulla on kysyttävää tai alla olevat ohjeet kaipaavat täsmennystä, älä epäröi [ottaa yhteyttä](../../support/contact.md) (aihe: Sensitive Data). 

Salaus on integroitu SD Connect -käyttöliittymään automaattiseksi vaiheeksi, erityisesti alle 1 Gt:n tiedostoille. Kaikki SD Connectin kautta ladatut tiedot salataan automaattisesti Sensitive Data -palveluiden julkisella salausavaimella. Voit kuitenkin valita erilaisia vaihtoehtoja tietojesi salaamiseen analysointia tai jakamista varten. 

Lyhyesti: palvelut käyttävät menetelmää nimeltä _asymmetrinen salaus_, joka perustuu kahteen toisiinsa kytkeytyvään salausavaimeen:

   * Julkista avainta käytetään tietojen salaamiseen. Julkisella avaimella ei voi purkaa salausta. Voit jakaa julkisen avaimesi muille, esimerkiksi yhteistyökumppaneillesi, jolloin he voivat salata aineistoa julkisella avaimellasi. 

   * Salaisella avaimella (myös yksityinen avain) puretaan sellaisen tiedoston salaus, joka on salattu vastaavalla julkisella avaimella. Tämä avain on suojattu salasanalla eikä sitä saa jakaa muille. 


Kun käytät SD Connectia tietojen lähettämiseen CSC:lle, sinulla on useita salausvaihtoehtoja:

1. Oletusvaihtoehto tietojen analysointiin:

      * Oletussalausasetuksilla voit ladata tiedot SD Connectin kautta verkkoselaimella analysointia varten. Tiedostot salataan automaattisesti ja ovat analysoitavissa SD Desktopin kautta. Et kuitenkaan voi purkaa tiedostojen salausta sen jälkeen, kun olet ladannut ne omalle tietokoneellesi tai organisaatiosi laskentaympäristöön. Kehitämme tämän vuoksi uutta ominaisuutta, joka mahdollistaa automaattisen salauksen purun SD Connectin kautta. Lisätietoja: [ota yhteyttä](../../support/contact.md) (Sensitive Data).

2. Useiden salausavainten lisääminen tietojen tallennusta, jakamista ja siirtoa varten:
   
      *  Voit ladata tiedot SD Connectin kautta verkkoselaimella ja lisätä julkisen salausavaimesi. Tiedostot salataan oletuksena SD-palveluiden avaimella, mutta voit lisäksi lisätä oman salausavaimesi. Tällä tavoin voit myös ladata ja purkaa tietojen salauksen tarvittaessa.
         
      *  Voit ladata tiedot SD Connectin kautta verkkoselaimella ja lisätä useita salausavaimia, esimerkiksi oman julkisen salausavaimesi sekä yhteistyökumppanisi julkisen salausavaimen. Myös tässä tapauksessa tiedostot salataan oletuksena SD-palveluiden salausavaimella ja ne ovat analysoitavissa SD Desktopin kautta. Lisäksi sekä sinä että yhteistyökumppanisi voitte tarvittaessa ladata ja purkaa tietojen salauksen.

   
Tämä salausmenetelmä perustuu Crypt4GH-työkaluun, joka alun perin kehitettiin ihmisen geneettisen datan salaamiseen ja jakamiseen [Global Alliance for Genomics and Health](https://www.ga4gh.org/) (GA4GH) -standardin mukaisesti. Crypt4GH:ta voidaan käyttää minkä tahansa tiedoston (kuvat, ääni, video, tekstitiedostot jne.) salaamiseen.
CSC on kehittänyt yksinkertaisen sovelluksen, jonka avulla voit **luoda omat salausavaimesi**. 

Seuraavissa kappaleissa kuvataan kaikki tarvittavat vaiheet: salausavainten luonti, tietojen lähetys ja salaus SD Connectin avulla sekä tiedostojen salauksen purku sen jälkeen, kun olet ladannut ne takaisin tietokoneellesi. Voit luonnollisesti suorittaa jokaisen näistä vaiheista myös ohjelmallisesti.