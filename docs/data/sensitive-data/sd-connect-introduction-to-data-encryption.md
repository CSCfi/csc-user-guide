# Johdanto tietojen salaukseen yhteensopivana Herkkä tieto -palvelujen kanssa {#introduction-to-data-encryption-compatible-with-sensitive-data-services}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/dI1Py_1gA-k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

CSC:n pilvipalveluihin SD Connectin kautta tai ohjelmallisesti siirrettävä herkkä tieto on salattava. Tämän luvun ohjeiden mukaisesti salatut tiedostot ovat yhteensopivia ja käytettävissä kaikkien Herkkä tieto (SD) -palvelukomponenttien kautta. Näin salatut tiedostot, jotka tallennetaan SD Connect -palveluun, ovat saatavilla analysointia varten (SD Desktop -palvelun avulla) tai julkaisua ja uudelleenkäyttöä varten hallitun pääsyn alaisina (SD Submitin, Federated EGA:n tai SD Applyn kautta).

!!! Huom
    Tietojen salaaminen ei vaadi teknistä osaamista, mutta se edellyttää tutustumista seuraavaan käyttäjän oppaaseen ja video-oppaisiin. Tarjoamme myös askel-askeleelta ohjeistusta verkossa tai asiakaspalvelun kautta. Jos sinulla on kysyttävää tai tarvitset ohjeiden alla selvennystä, älä epäröi [ottaa yhteyttä](../../support/contact.md) (aihe: Herkkä tieto).

Olemme integroineet salauksen automatisoituna askeleena SD Connect -käyttöliittymässä, erityisesti alle 1 Gt:n kokoisia tiedostoja varten. Kaikki SD Connectin kautta ladatut tiedot salataan automaattisesti Herkkä tieto -palvelujen julkisella salausavaimella. Voit kuitenkin valita erilaisia vaihtoehtoja tietojen salaamiseen analysointia tai jakamista varten.

Palvelut käyttävät lyhyesti sanottuna _epäsymmetristä salausta_, joka perustuu kahteen toisiinsa liitettyyn salausavaimeen:

   * Julkista avainta käytetään tietojen salaukseen. Julkista avainta ei voi käyttää tietojen purkamiseen. Voit jakaa julkisen avaimesi muiden kanssa, esim. yhteistyökumppaniesi kanssa, jolloin he voivat salata tietoja julkisella avaimesi.

   * Salainen avain (tunnetaan myös yksityisenä avaimena) käytetään tiedoston purkamiseen, joka on salattu vastaavalla julkisella avaimella. Tämä avain on suojattu salasanalla, eikä sitä saa jakaa muille.

Kun käytät SD Connectia tietojen lataamiseen CSC:hen, sinulla on useita mahdollisuuksia salaukseen:

1. Oletusvaihtoehto data-analyysille:

      * Oletuksena olevilla salausvaihtoehdoilla voit ladata tiedot SD Connectin kautta verkkoselaimellasi data-analyysia varten. Tiedostot salataan automaattisesti ja ovat käytettävissä analyysissä SD Desktopin kautta. Voit kuitenkin purkaa tiedostot ladattuasi ne takaisin kannettavaasi tai organisaatiosi tietojenkäsittely-ympäristöön. Kehitämme uutta ominaisuutta, joka tarjoaa automaattista purkamista SD Connectin kautta. Lisätietoja varten [ota yhteyttä](../../support/contact.md) (Herkkä tieto).

2. Useiden salausavainten lisääminen tietojen tallennukseen, jakamiseen ja siirtoon:
   
      * Voit ladata tiedot SD Connectin kautta verkkoselaimen avulla ja lisätä julkisen salausavaimesi. Tiedostot salataan oletuksena SD-palveluiden avulla, mutta voit myös lisätä oman salausavaimesi. Tällä tavoin voit myös ladata ja purkaa tiedot tarvittaessa.

      * Voit ladata tiedot SD Connectin kautta verkkoselaimellasi ja lisätä useita salausavaimia. Esimerkiksi, julkinen salausavaimesi ja yhteistyökumppanisi julkinen salausavain. Myös tässä tapauksessa tiedostot salataan oletuksena SD-palveluiden salausavaimella ja ovat saatavilla data-analyysiin SD Desktopin kautta. Lisäksi sinä ja yhteistyökumppanisi voitte myös ladata ja purkaa tiedot tarvittaessa.

Tämä salausmenetelmä perustuu Crypt4GH:ään, työkaluun, joka on alun perin suunniteltu ihmisen geneettisten tietojen salaamiseen ja jakamiseen [Global Alliance for Genomics and Health](https://www.ga4gh.org/) (GA4GH) -standardin mukaisesti. Crypt4GH:ta voidaan käyttää minkä tahansa tiedoston (kuva, ääni, video, tekstitiedostot jne.) salaamiseen. CSC on kehittänyt yksinkertaisen sovelluksen, jonka avulla voit **luoda salausavaimesi**.

Seuraavissa kappaleissa kuvataan kaikki tarvittavat askeleet salausavainten luomiseen, tietojen lataamiseen ja salaamiseen SD Connectin avulla sekä tiedostojen purkamiseen, kun ne on ladattu takaisin tietokoneellesi. Tietenkin voit myös suorittaa jokaisen näistä vaiheista ohjelmallisesti.