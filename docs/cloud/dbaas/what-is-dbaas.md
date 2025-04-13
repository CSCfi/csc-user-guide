# Mitä on DBaaS {#what-is-dbaas}

Tietokanta palveluna (DBaaS) on itsepalvelu, tilauspohjainen tietokantapalvelu, mikä tarkoittaa, että voit käynnistää uuden tietokannan "yksinkertaisella klikkauksella". DBaaS:n tavoitteena on automatisoida tietokantojen ylläpito ja hallintatehtävät muiden palveluiden osalta, jotta kehittäjät/hallinnoijat voivat keskittyä asioihin, jotka tuovat todellista "arvoa" palveluille.

Sen sijaan, että asettaisit oman tietokannan manuaalisesti ja joutuisit ylläpitämään sitä itse, voit käyttää DBaaS:ia hallitsemaan työläitä tehtäviä, kuten varaaminen, konfigurointi, ylläpito, päivitys, dokumentointi ja tietokannan varmuuskopiointi.

DBaaS käyttää OpenStack-pohjaista palvelua. DBaaS-palvelu toimii cPoutan päällä, mikä tarkoittaa, että mikä tahansa ongelma, joka vaikuttaa cPoutaan, saattaa vaikuttaa myös DBaaS:iin.

Jokainen tietokanta-instanssi toimii omassa virtuaalikoneessaan, mikä merkitsee, että kaikki tietokanta-instanssit on eristetty toisistaan virtualisoinnin kautta. Kaikilla tietokanta-instansseilla on myös oma julkinen IP-osoite, joka on saavutettavissa internetin kautta, ja oma palomuurikonfiguraationsa, jonka käyttäjä voi määritellä. On käyttäjän vastuulla varmistaa, että heidän tietokanta-instansseillaan on tiukat palomuurisäännöt ja että he noudattavat hyviä salasanakäytäntöjä.

DBaaS on geneerinen tietokantapalvelu, mikä tarkoittaa, että sen pitäisi sopia suurimpaan osaan käyttötapauksista. DBaaS-palvelun lisäarvo on suurin kotisivuilla, pienissä palveluissa, tutkimusprojekteissa ja kehitysprojekteissa. DBaaS ei ole "tietokannan hallintaa palveluna", mikä tarkoittaa, että DBaaS ei tarjoa tukea, esimerkiksi kuinka optimoida tietokantakyselysi tai miten rakentaa tietokantaasi.