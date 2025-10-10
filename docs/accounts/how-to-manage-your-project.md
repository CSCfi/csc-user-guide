# Kuinka hallita projektejasi { #how-to-manage-your-projects }

CSC-projekti on pidennettävä vuosittain.

* Projektin jäsenet saavat muistutuksia projektin päättymisestä.
* Projektipäällikkö voi pidentää projektia [MyCSC:ssä](https://my.csc.fi)
* Kun projektille myönnetään uusia Billing Unitseja (BU), projekti pitenee automaattisesti vuodella.
* Fairdata IDA -palvelua käyttävät projektit pitenevät automaattisesti.

!!! Note
    Projektipäällikön CSC-tilin deaktivointi sulkee projektin kaikilta projektin jäseniltä.

* Projektipäällikön CSC-käyttäjätili on pidettävä aktiivisena. CSC lähettää sähköpostitse ilmoituksia ja ohjeita ennen kuin käyttäjätunnukset tai salasanat vanhenevat. Huomaa, että aktiivinen käyttäjätili ei pidennä projektia.
* Pidä käyttäjätiedot, kuten sähköpostiosoite, ajan tasalla.
* Tarvittaessa projektipäällikkö on vastuussa projektipäällikön tehtävien siirtämisestä toiselle projektin jäsenelle.

Käyttäjät ovat ensisijaisesti vastuussa [datan siirtämisestä](../data/moving/index.md) tai projektin sisällön poistamisesta itse ennen kuin projekti suljetaan. 
Jos et ole varma CSC-projektisi tai -tilisi tilasta, kirjaudu [MyCSC:hen](https://my.csc.fi) pidentämään projektiasi tai vaihtamaan tilisi salasanaa.
Jos haluat sulkea projektisi, vaihtaa tilisi sähköpostiosoitteen tai vaihtaa projektipäällikön, ole hyvä ja [ota yhteyttä ServiceDeskiin](../support/contact.md)

## Projektin keston pidentäminen { #project-lifetime-extension }

Voit hakea projektille yhden vuoden mittaista keston pidennystä.
Huomaa, että [opiskelijaprojektien](../support/tutorials/student_quick.md) enimmäiskesto on 6 kuukautta eikä niitä voi pidentää.

1. Kirjaudu sisään [MyCSC:hen](https://my.csc.fi).
1. Valitse vasemman laidan navigaatiovalikosta kohta _Projects_.
1. Valitse projekti, jota haluat pidentää
1. Napsauta 'Extend'-painiketta
1. Hyväksy muutokset napsauttamalla 'Apply'-painiketta
1. Projektisi kesto on nyt pidentynyt yhdellä vuodella.


## Projektin päättäminen { #project-closure }

CSC-projektit sulkeutuvat automaattisesti päättymispäivänään. Ennen CSC-projektin päättymistä kaikki projektin jäsenet saavat useita sähköposti-ilmoituksia tulevasta sulkemisesta. Projektipäällikkö voi pidentää CSC-projektia ennen sen sulkeutumista.

Projektipäällikkö voi myös sulkea CSC-projektin aiemmin MyCSC-portaalissa. Projektin jäsenille ilmoitetaan, kun CSC-projekti on suljettu. Huomaa, että palvelujen sisältö poistetaan CSC-projektin sulkemisen jälkeen, ellei toisin ole sovittu. Jos haluat säilyttää jotain sisältöä (esim. dataa, ohjelmistoja, palvelimia, järjestelmiä tai prosesseja), vie ja poista ne CSC:n palveluista ennen CSC-projektin päättymispäivää.

Jos CSC-projektin sulkeminen tapahtui vahingossa, projektipäällikön tulee ottaa CSC:hen yhteyttä mahdollisimman pian osoitteeseen servicedesk@csc.fi. Projektipäällikön pyynnöstä CSC-projekti voidaan avata uudelleen tai palveluihin voidaan myöntää tilapäinen käyttöoikeus.

Sisältöä ei voi enää palauttaa 90 päivän kuluttua CSC-projektin sulkemisesta.

#### Kun projekti on suljettu { #when-the-project-is-closed }

Käyttäjät eivät pysty käyttämään projektia varten haettuja palveluja, ja kaikki palveluiden sisältö poistetaan 90 päivää projektin sulkemisen jälkeen.

| Palvelu | Mitä tapahtuu, kun projekti on suljettu |
| -- | -- |
| Allas, Fairdata IDA, SD Connect | Projekti poistetaan käytöstä, eivätkä käyttäjät voi käyttää palvelua projektin puitteissa. |
| Mahti ja Puhti | Uusia Slurm-tehtäviä ei voi lähettää. Käyttäjät eivät enää pääse käsiksi projektin dataan. |
| cPouta ja ePouta | Projekti poistetaan käytöstä, eivätkä käyttäjät voi käyttää palvelua projektin puitteissa. Kaikki projektin virtuaalikoneet sammutetaan. |
| Rahti | Projektin pod-kiintiö asetetaan arvoon 0 ja kaikki työkuormat pysäytetään. |
| SD Desktop | Työpöydät keskeytetään, eikä projekti voi käynnistää uusia työpöytiä. |



!!! Note 
    
    Kaikki palveluiden sisältö poistetaan 90 päivää projektin sulkemisen jälkeen. Jos tarvitset vahvistuksen siitä, että kaikki sisältö on poistettu palveluista, ota yhteyttä Service Deskiin.