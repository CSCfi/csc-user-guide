
# Tarvitsen tietokannan, minne voin asentaa sen? {#i-need-a-database-where-can-i-deploy-it}

Jos tarvitset tietokannan, joka täytyy olla saavutettavissa muista järjestelmistä (kuten Puhti tai Mahti), paras ja helpoin vaihtoehto on [Pukki DBaaS -palvelu](../../cloud/dbaas/index.md), joka tukee tällä hetkellä PostgreSQL-tietokantoja. Muita tyyppejä harkitaan.

Jos tarvitset muun tyyppistä tietokantaa, voit asentaa sen itse [cPouta-pilvessä](../../cloud/pouta/index.md). Tässä tapauksessa sinun tulisi pyytää virtuaalikonetta ja sitten vain seurata valitsemasi tietokannan ohjeita. Käytä tietoturvaryhmiä antaaksesi verkkoyhteyden tietokantaasi.

!!! warning "Tärkeää"
    Kun käytät [tietoturvaryhmiä](../../cloud/pouta/launch-vm-from-web-gui.md#firewalls-and-security-groups), kiinnitä erityistä huomiota siihen, että avaat vain tarvittavat portit tarvittaville IP-osoitteille.

## Milloin Rahti on hyvä paikka asentaa tietokanta? {#when-is-rahti-a-good-place-to-deploy-a-database}

Rahti on hyvä valinta, jos sovellus, joka tarvitsee yhteyden tietokantaan, on jo asennettu Rahtiin. Rahti hyväksyy vain verkkoyhteydet Rahtin ulkopuolelta HTTP(s)-protokollaa käyttäen porteissa 80 ja 443.

Yksi tapa muodostaa yhteys Rahtiin CSC:n supertietokoneilta on luoda TCP-tunneli HTTP-yhteensopivan WebSocket-yhteyden yli. Katso lisätietoja tästä kiertotiestä [Tietokantoihin yhdistäminen Rahtissa CSC:n supertietokoneista](../../cloud/rahti/tutorials/connect-database-hpc.md).
