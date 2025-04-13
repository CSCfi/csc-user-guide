
# Known problems and limitations {#known-problems-and-limitations}

## Instances {#instances}

-   **Instance-kuvat saattavat joskus epäonnistua. Tämä jättää
    instanssin keskeytettyyn tilaan. Tämän ongelman välttämiseksi suosittelemme,
    että käyttäjät sammuttavat VM:nsä ennen kuvan ottamista.**
-   Käytettäessä olemassa olevan emoinstanssin kuvasnapshottia luodut
    lapsi-instanssit eivät sisällä ennalta määriteltyä
    tietoturvaryhmää. Valitse sopiva tietoturvaryhmä
    lapsi-instansseille ennen niiden käynnistämistä.
-   Lajiperheiden sisäinen koon muuttaminen (standard.*) on
    mahdollista, paitsi IO-mauille. Muuttaminen lajiperheiden
    välillä toimii harvoin erilaisten tallennusalustojen vuoksi.
    Jos käytät levyä juurilevynä, jotkin lajiperheiden
    väliset muutokset toimivat. Jos käytät kuvaa juurilevynä,
    se saattaa olla vaarallista. Testaa aina muutokset ensin
    väliaikaisella VM:llä. Jos virtuaalikoneesi päätyvät "virhe"
    tilaan, ota meihin yhteyttä.
-   Verkko: Saman kelluvan IP-osoitteen lisääminen
    useisiin instansseihin API:n kautta on mahdollista. Ei
    varoitusta tai virhettä ilmene. Viimeinen API-kutsu
    on se, joka vaikuttaa.
-   Levyt: Laitteiden nimien säilyminen uudelleenrakennuksen tai
    uudelleenkäynnistyksen jälkeen ei ole taattua. Jos haluat
    varmistaa, että oikea laite liitetään aina samaan
    polkuun, on hyvä idea käyttää UUID:eja polkujen sijaan.
-   Ubuntu-20.04-kuvat ja hpc.6-maut eivät pysty käynnistymään. 
    Bug aiheuttaa, että Ubuntu 20.04 -instanssit (luodut tai päivitetyt) 
    ja maku hpc.6.* eivät pysty käynnistymään. Odotamme tulevan
    päivityksen korjaavan tämän, mutta vältä toistaiseksi tätä yhdistelmää.

## EC2 tools (euca2ools) {#ec2-tools-euca2ools}

-   EC2 ei ole tällä hetkellä tuettu. EC2-tunnuksia voi kuitenkin käyttää
    objektitallennuksen kanssa.

## [Pouta FAQ entries](../../support/faq/index.md#pouta) {#pouta-faq-entries}
