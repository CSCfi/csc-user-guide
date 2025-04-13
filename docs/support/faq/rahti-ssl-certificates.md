
# Tarjoaako Rahti SSL-varmenteita? {#do-you-offer-in-rahti-ssl-certificates}

Kyllä, DNS-nimille `*.2.rahtiapp.fi` ja `*.rahtiapp.fi` on asennettu wildcard-varmenne, ja käyttäjä voi käyttää sitä suoraan.

Jos palvelusi DNS-nimi sijaitsee aliverkkotunnuksen `rahtiapp.fi` alla, ota yksinkertaisesti käyttöön *TLS-salaus* reitille, ja reitti saa automaattisesti voimassa olevan varmenteen. Rahti-tiimi hallitsee varmenteen, mikä sisältää uusimisen ja asennuksen.

Jos DNS-nimi ei ole aliverkkotunnuksen `rahtiapp.fi` alla, sinun on toimitettava oma varmenteesi. Sinun on huolehdittava varmenteen hankkimisesta, sen lisäämisestä `Route`-objektiin ja sen uudenmisesta ennen sen vanhentumista.

Voit lukea tästä lisää [Mukautetut verkkotunnukset ja turvallinen yhteys](../../cloud/rahti/tutorials/custom-domain.md) -oppaastamme.
