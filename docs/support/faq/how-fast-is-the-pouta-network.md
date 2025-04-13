
# Kuinka nopea Pouta-verkko on? {#how-fast-is-the-pouta-network}

Verkko on sekoitus 40 Gb/s ja 10 Gb/s Ethernetiä. HPC-muisteilla käynnistetyt koneet saavat 40 Gb/s verkon, kun taas tavallisilla muisteilla on 10 Gb/s. Lisätietoja löytyy luvusta virtuaalikoneiden muisteista: [Virtuaalikoneiden muistit ja kiintiöt](../../cloud/pouta/vm-flavors-and-billing.md)

Virtualisointi asettaa joitakin rajoituksia:

   - Intra node ja ulkoinen yhteys sisältää joitakin ylikuluja johtuen virtualisoinnista. Tämä vaikuttaa viiveeseen ja kaistanleveyteen, mutta meillä ei ole vertailudataa jaettavaksi tällä hetkellä.
   - Verkkoviiveherkät sovellukset saattavat toimia selvästi huonommin kuin käyttäessä klusteria (kuten Puhtia) natiivisti.
   - Ylikuluja syntyy Ethernetin käytön tarpeellisuudesta virtuaalikoneiden yhteyksiin ja yhteensopivuuteen.
