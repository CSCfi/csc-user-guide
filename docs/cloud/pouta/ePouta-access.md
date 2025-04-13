
# Hakemus ePouta-käyttöoikeuden saamiseksi {#applying-for-epouta-access}

Hakemus **ePouta**-käyttöoikeuden saamiseksi ei ole itsepalveluprosessi, se saattaa vaatia manuaalista väliintuloa ja **viikkojen odotusta**. Tämä eroaa cPoutasta, joka on itsepalvelu, ja sinun pitäisi pystyä saamaan uusi projektisi muutamassa minuutissa.

ePouta on IaaS-pilvi, joka on suunniteltu käsittelemään ja säilyttämään **arkaluonteisia tietoja**. Tämän vuoksi suunnittelu keskittyy alustan ja siinä olevien tietojen turvallisuuteen. Se vaatii [MPLS](https://en.wikipedia.org/wiki/Multiprotocol_Label_Switching) VPN-yhteyden ePoutan ja käyttäjän VM:n paikallisen verkon välille. Toisin sanoen, ennen ePoutan käyttöä on tarpeen konfiguroida [MPLS](https://en.wikipedia.org/wiki/Multiprotocol_Label_Switching) VPN. Tämä verkkokokoonpano on manuaalinen vaihe, joka sisältää useita CSC:n ja VM-käyttäjän laitoksen tiimejä.

<center>![MPLS](../img/epouta_connection.drawio.svg)</center>

Lopputuloksena on "virtuaalinen yksityinen datakeskus", sillä asiakasverkon palvelimet ovat samassa verkossa CSC:n VM:ien kanssa.

1. Ensimmäinen askel on varmistaa, että ePouta on sopiva palvelu käyttötarkoitukseen. ePouta on suunniteltu säilyttämään ja käsittelemään **arkaluonteisia tietoja**. Jos käyttötapaus ei käsittele arkaluonteisia tietoja, cPouta voi olla parempi palvelu käyttötarkoitukseen.

1. Kun ePoutan soveltuvuus on vahvistettu, on tarpeen tarkistaa, onko ePoutassa jo luotu projekti, joka voi sisältää tämän käyttötapauksen. Joillakin laitoksilla on niin sanottu "sateenvarjoprojekti" tai muu etukäteen luotu tai etukäteen jaettu verkkoyhteyksien pooli. Ota yhteyttä laitoksesi IT-tiimiin tarkistaaksesi tämän.

1. Jos sopivaa projektia tai verkkoyhteyttä ei ole vielä saatavilla, sinun on lähettävä pyyntö sähköpostitse osoitteeseen <servicedesk@csc.fi> selittäen käyttötapauksesi. Muista mainita seuraavat tiedot:

    * Käyttötapauksen kuvaus ja miksi se tulee isännöidä ePoutassa.
    * Mainitse, ettei nykyisiä resursseja voida käyttää ja uusi on luotava.
    * Tarvittavien resurssien arviointi ja kuinka kauan resursseja käytetään. Voit tarkistaa [VM-maut ja -laskutus](vm-flavors-and-billing.md#epouta-flavors) -sivulta, mitä VM:itä on saatavilla ja arvioida tarvittavien Laskutusyksiköiden määrän.
    * Hallintakoneiden IP-osoitteet, jotka luovat, muokkaavat ja poistavat VM:t.

1. Kun tiketti on luotu, on tarpeen odottaa. CSC ottaa yhteyttä tarvittaviin verkostotiimeihin infrastruktuurin pystyttämiseksi. Sinuun otetaan yhteyttä vain valmistumisen yhteydessä tai jos kysymyksiä ilmenee.

1. Laitoksesi IT-tiimi saattaa ottaa sinuun yhteyttä ja pyytää tarkennuksia verkon konfiguraatioista.
