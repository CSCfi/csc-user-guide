
# Miksi tämä säilöraportti ilmoittaa käyttöoikeuksien epäämisestä? {#why-this-container-report-permission-denied-errors}

Yleisin syy sille, että säilö ei käynnisty Rahtissa, on se, että säilökuva odottaa suoritusta käyttäjänä `root`. Koska Rahti ei suorita kuvia root-käyttäjänä, käyttöoikeuksien epäämisvirheet pysäyttävät suorituksen.

Ratkaisu on käyttää toista kuvaa. Ensimmäinen vaihtoehto on löytää toinen kuva, joka on valmisteltu suoritettavaksi ilman root-käyttäjää. Jos ei ole kuvaa, joka on valmiina suoritettavaksi OpenShiftissä tai sitä ei tarjoa luotettava lähde, toinen vaihtoehto on muokata nykyistä kuvaa toimimaan ilman root-käyttäjää, esimerkiksi kuten kuvattu [Kuvien luominen](../../cloud/rahti/images/creating.md) osiossa.
