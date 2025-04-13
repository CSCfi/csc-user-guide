
# Pouta-tallennus

Jokaisessa virtuaalikoneessa on saatavilla vähintään yksi tallennustyyppi, joka
on virtuaalikonekuvan määrittämä tiedostojärjestelmä. Tämä on virtuaalikoneen
ensisijainen levy, jota kutsutaan myös juurilevyksi. Kuitenkin käytettävissä oleva tila on
tyypillisesti rajallinen ja siellä olevan datan elinikä on rajallista virtuaalikoneen mukaan, 
eli data pyyhitään, kun virtuaalikone poistetaan. Tässä artikkelissa esitellään 
CSC:n pilviympäristön tallennusvaihtoehdot. Tallennuksen käyttö edellyttää tiliä, projektia 
ja virtuaalikonetta.

## Lyhytikäinen tallennus {#ephemeral-storage}

Riippuen valitusta tyypistä, virtuaalikoneessa voi olla tietty määrä
lisättyä paikallista levytilaa, jota kutsutaan **lyhytikäiseksi tallennukseksi**
OpenStack-terminologiassa. Tämä tallennus näkyy virtuaalikoneessa toisena kiintolevynä.

Lyhytikäisen tallennuksen pääetu on suorituskyky, koska data tallennetaan palvelimen
kiintolevylle, jossa virtuaalikone toimii. Kuitenkin lyhytikäinen tallennus on
saatavilla vain kun virtuaalikone on käynnissä. Lisäksi, samalla tavoin kuin
ensisijaisen levyn data, myös lyhytikäisen tallennuksen data katoaa, kun poistat
virtuaalikoneen. Koska lyhytikäisen tallennuksen dataa ei replikoida, ei sinne tulisi
tallentaa pysyvää dataa, eikä lyhytikäistä tallennusta tulisi pitää luotettavana.

Lisätietoa löytyy [lyhytikäisen tallennuksen sivulta](ephemeral-storage.md).

## Pysyvät volyymit {#persistent-volumes}

Jos etsit tallennustilaa, jota voidaan käyttää kuten lisäkiintolevyä ja joka ei ole
sidottu yhteen virtuaalikoneeseen, etsit **pysyviä volyymeja**. Voit liittää pysyvän
volyymin virtuaalikoneeseen ja käyttää sitä kuten käyttäisit lyhytikäistä tallennusta.
Kuitenkin voit myös irrottaa sen virtuaalikoneesta ja liittää sen toiseen virtuaalikoneeseen.
Toisin sanoen, voit vapaasti poistaa ja luoda uudelleen virtuaalikoneitasi käyttämällä 
pysyviä volyymejä, sillä pysyvä volyymi ei ole sidottu yhden virtuaalikoneen elinikään. 
Lisäksi, pysyvät volyymit ovat luotettava tallennusvaihtoehto, sillä niiden data on replikoitu.

Lisätietoa löytyy [pysyvien volyymien sivulta](persistent-volumes.md).

## Objektitallennus {#object-storage}

Mikäli tarvitset tallennustilaa, jossa dataasi on helposti käytettävissä Internetin kautta,
esim. URL-osoitteiden avulla, **objektitallennus** on etsimäsi tallennusratkaisu. 
Käyttämällä objektitallennusta, voit vapaasti luoda ja poistaa virtuaalikoneita, 
koska objektitallennus ei ole sidottu mihinkään virtuaalikoneeseen. Lisäksi datasi on replikoitu,
joten objektitallennus on luotettava tallennusvaihtoehto.

CSC:ssä tarjoamme Allasta objektitallennusratkaisuna.
Lisätietoa löytyy [Allas-sivulta](../../data/Allas/index.md).

## Tilannevedokset {#snapshots}

Joskus haluat vain tehdä varmuuskopion virtuaalikoneen tai pysyvän volyymin datasta. 
Vaihtoehtoisesti saatat haluta tallentaa nykyisen virtuaalikoneen tilan, jotta voit 
aloittaa muita virtuaalikoneita kloonaamalla sama tila. Näissä tapauksissa voit käyttää 
**tilannevedoksia**.

Lisätietoa löytyy [tilannevedosten sivulta](snapshots.md).
