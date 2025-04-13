
---
description: Asiat, jotka tulee sisällyttää CSC:n ServiceDesk-tukipyyntöön
---

# Kuinka kirjoittaa hyviä tukipyyntöjä

Hyvin kirjoitettu tukipyyntö auttaa meitä ratkaisemaan ongelmasi nopeammin. Alla on luettelo hyvistä käytännöistä.

## Määritä ympäristösi {#specify-your-environment}

Missä järjestelmässä suoritat ohjelmaa? Oletko sinä tai kollegasi koonnut koodin? Mitkä moduulit olivat ladattuna? Jos käytät muita kuin oletusmoduuleja tai esimerkiksi Conda-ympäristöjä etkä kerro niistä meille, aikaa kuluu turhaan, kun yritämme löytää ongelmaa toisessa ympäristössä.

## Sisällytä todelliset komennot ja virheilmoitukset {#include-actual-commands-and-error-messages}

Käsittelemme tätä alla, mutta se on niin tärkeää, että se on mainittava myös ylhäällä: sisällytä käyttämäsi todelliset komennot ja todelliset virheilmoitukset (myös Slurm-virheilmoitus ja -tuloste). Kopioi ja liitä.

## Anna kuvaileva otsikko {#give-a-descriptive-subject}

Otsikkosi tulisi olla kuvaileva. "Ongelma Mahtissa" ei ole hyvä otsikko, sillä se voisi sopia moniin saamiimme tukipyyntöihin. Tukitiimi on ryhmä. Otsikot ovat ensimmäinen asia, jonka näemme, ja hyvä otsikko nopeuttaa asian ohjaamista oikealle asiantuntijalle.

## Ole tarkka {#be-specific}

Mitä tahansa teetkin, älä sano "X ei toiminut". Anna tarkat komennot, joita käytit, ympäristö (katso yllä) ja virheilmoitukset. Todelliset virheilmoitukset merkitsevät paljon - sisällytä koko tuloste, se on helppo kopioida ja liittää.

Mitä paremmin kuvailet ongelman, sitä vähemmän meidän tarvitsee arvailla ja kysyä. Tee ongelmasta toistettavissa oleva. Katso myös seuraava kohta.

## Kerro, mitä dokumentaatiota olet jo lukenut {#tell-us-which-documentation-you-have-already-read}

Jos pyydät neuvoa esimerkiksi tietyn ohjelmistopaketin käyttöön, selitä yksityiskohtaisesti, mitä dokumentaatiota olet jo lukenut ja miksi se ei ole vielä täysin vastannut kysymykseesi. Tämä antaa meille mahdollisuuden vastata tarkemmin kysymykseesi sen sijaan, että vain viittaisimme olemassa olevaan dokumentaatioon.

## Lähetä pyyntösi ServiceDeskiin {#send-your-requests-to-servicedesk}

Lähetä pyynnöt aina [CSC ServiceDeskiin](contact.md) sen sijaan, että lähettäisit ne suoraan työntekijöille. ServiceDeskissä ne seurataan, niillä on suurempi näkyvyys ja ne ohjataan oikealle asiantuntijalle. Jotkut työntekijät tekevät tukiikkunoita vain osa-aikaisesti ja olemme joskus myös lomalla.

## Kerro myös, mikä toimi {#tell-us-also-what-worked}

Melko usein saamme pyyntöjä tyyliin "En saa X:ää toimimaan kahdella solmulla". Pyynnössä ei sitten mainita, toimiko se yhdellä solmulla tai yhdellä ytimellä, tai toimiiko se ensikerrallakaan ollenkaan. Ehkä ongelma ei edes liity mitenkään yhteen tai kahteen solmuun. Jotta ongelma voitaisiin rajata paremmin ja vältyttäisiin monilta edestakaisilta sähköposteilta, kerro meille, mikä todellisuudessa toimi tähän mennessä. Kerro meille, kuinka olet yrittänyt rajata ongelmaa. Tämä vaatii sinulta jonkin verran vaivaa, mutta se auttaa meitä ratkaisemaan ongelmasi nopeammin.

## Tunnista itsesi {#identify-yourself}

Anna CSC-käyttäjätunnuksesi ja ammatillinen yhteytesi (jos käytät ei-ammatillista sähköpostiosoitetta, kuten Gmailia).

## Uusi ongelma, uusi sähköposti {#new-problem-new-email}

Älä lähetä tukipyyntöjä vastaamalla vanhoihin lippuihin, jotka todennäköisesti koskevat asiattomia ongelmia. Jokainen asia saa numeron, ja tämä on se numero, jonka näet otsikkorivillä.

## XY-ongelma {#the-xy-problem}

Tämä on klassinen ongelma. Lue [lisää XY-ongelmasta täältä](https://xyproblem.info/). Usein tiedämme ratkaisun, mutta joskus emme tiedä ongelmaa.

Lyhyesti (lainaus edelliseltä verkkosivulta):

* Käyttäjä haluaa tehdä tehtävän X.
* Käyttäjä ei tiedä, miten tehdä X, mutta ajattelee sen onnistuvan Y:n kautta.
* Käyttäjä ei myöskään tiedä, miten tehdä Y.
* Käyttäjä pyytää apua Y:n kanssa.
* Muut yrittävät auttaa käyttäjää Y:ssä, mutta hämmentyvät, koska Y vaikuttaa oudolta ongelmalta ratkaistavaksi.
* Lopulta ongelma ratkaistaan tekemällä X ilman Y:tä.

Välttääksemme XY-ongelman, jos käsittelet Y:tä mutta todellisuudessa tavoitteesi on X, kerro meille myös X:stä. Kerro mitä todella haluat saavuttaa. Y:n ratkaiseminen voi viedä kauan.

## Luo esimerkki, joka toistaa ongelman {#create-an-example-which-reproduces-the-problem}

Luo esimerkki, jonka voimme mielellään kopioida ja liittää ja joka osoittaa ongelman. Muuten on hyvin aikaavievää, jos tuki henkilöstö joutuu kirjoittamaan syöttötiedostoja ja ajamaan ohjelmistoja todennäköisesti epätäydellisten kuvausten perusteella. Katso myös seuraava kohta. Tee tämä esimerkki meille saataville. Emme etsi emmekä lue lukuoikeudella suojattuja tiedostoja ilman lupaasi (ja vain harvat pystyvät).

## Tee esimerkistä mahdollisimman pieni ja nopea {#make-the-example-as-small-and-fast-as-possible}

Suoritat laskelman, joka kaatuu viikon suorittamisen jälkeen. Olet taipuvainen kirjoittamaan tukipyynnön heti tämän esimerkin kanssa, mutta tämä ei ole hyvä idea. Ennen kuin lähetät tukipyyntön tämän esimerkin kanssa, yritä ensin pienentää sitä. On mahdollista ja todennäköistä, että kaatuminen voidaan toistaan paljon pienemmällä esimerkillä (pienempi järjestelmäkoko tai ristikko tai perusjoukko). On paljon helpompaa ajoittaa ja selvittää ongelma, joka kaatuu muutamassa sekunnissa verrattuna ajona, joka kaatuu useiden tuntien jälkeen. Tämä vaatii tietysti jonkin verran vaivaa sinulta, mutta se auttaa meitä ratkaisemaan ongelmasi nopeammin. Usein ongelman eristämisen aikana ongelma ja ratkaisu kiteytyvät ennen edes tukipyynnön kirjoittamista.

## Jos et voi luoda esimerkkiä, selitä mitä olet tehnyt {#if-you-cant-create-an-example-explain-what-youve-done}

Selitä vaiheet ja komennot, jotka olet syöttänyt ennen ongelmaa, sekä tuotettu koko tuloste ja mahdolliset virheet. Jos datan määrä on suuri (yli 1MB), voit käyttää [FUNET FileSenderia](https://filesender.funet.fi/) tai [a-flipiä](../data/Allas/using_allas/a_commands.md#a-flip) lähettääksesi tiedostoja. Ole tarkka, katso yllä.

[_"Kuinka tehdä" käytetty HPC-ryhmän luvalla - UiT: The Arctic University of Norway._](https://hpc-uit.readthedocs.io/en/latest/help/writing-support-requests.html)
