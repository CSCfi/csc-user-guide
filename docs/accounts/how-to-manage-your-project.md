# Kuinka hallita projektejasi

CSC-projekti tulee uusia vuosittain.

* Projektin jäsenet saavat muistutuksia projektin vanhenemisesta.
* Projektipäällikkö voi uusia projektin [MyCSC](https://my.csc.fi)-palvelussa.
* Kun projektille myönnetään uusia laskentayksiköitä (BU), projekti pitenee automaattisesti vuodella.
* Projektit, jotka käyttävät [Fairdata IDA](https://ida.fairdata.fi/), pitenevät automaattisesti.

!!! Huomio

    Projektipäällikön CSC-tilin inaktivointi sulkee projektin kaikilta projektin jäseniltä.

* Projektipäällikön CSC-tili tulee pitää aktiivisena vaihtamalla salasana vuosittain ja pitämällä käyttäjätiedot kuten sähköpostiosoite ajan tasalla. Tarvittaessa projektipäällikkö on vastuussa projektipäällikön tehtävien siirtämisestä toiselle projektin jäsenelle.

Käyttäjät ovat ensisijaisesti vastuussa [datan siirtämisestä](../data/moving/index.md) tai projektin sisällön poistamisesta itse ennen projektin sulkeutumista.
Jos olet epävarma CSC-projektisi tai tilisi tilasta, kirjaudu sisään [MyCSC](https://my.csc.fi) uusiaksesi projektisi tai muuttaaksesi tilisi salasanaa.
Jos haluat sulkea projektisi, vaihtaa tilisi sähköpostiosoitetta tai projektipäällikköä, ole hyvä ja [ota yhteyttä ServiceDeskiin](../support/contact.md).

## Projektin keston pidentäminen {#project-lifetime-extension}

Voit hakea projektin alkuperäistä keston pidennystä yhdellä vuodella.
Huomioithan, että [Opiskelijaprojektien](../support/tutorials/student_quick.md) enimmäiskesto on 6 kuukautta, eikä niitä voi pidentää.

1. Kirjaudu sisään [MyCSC](https://my.csc.fi).
1. Valitse _Projektit_ vasemmalla olevasta navigointivalikosta.
1. Valitse projekti, jota haluat pidentää.
1. Klikkaa 'Pidennä' painiketta.
1. Hyväksy muutokset klikkaamalla 'Hae' painiketta.
1. Projektisi kesto on nyt pidennetty yhdellä vuodella.

## Projektin sulkeminen {#project-closure}

CSC-projektit sulkeutuvat automaattisesti päättymispäivänään. Ennen CSC-projektin päättymistä kaikki projektin jäsenet saavat useita sähköposti-ilmoituksia sulkemisesta. Projektipäällikkö voi pidentää CSC-projektia ennen sen sulkeutumista.

Projektipäällikkö voi myös sulkea CSC-projektin aikaisemmin MyCSC-portaalin kautta. Projektin jäsenet saavat ilmoituksen, kun CSC-projekti on suljettu. Huomioithan, että sisällöt palveluissa poistetaan CSC-projektin sulkemisen jälkeen, ellei toisin ole sovittu. Jos haluat säilyttää jotain sisältöä (esim. data, ohjelmistot, palvelimet, järjestelmät tai prosessit), vie ja poista ne CSC:n palveluista ennen CSC-projektin päättymispäivää.

Jos CSC-projektin sulkeminen oli tahatonta, projektipäällikön tulisi ottaa yhteyttä CSC:hen mahdollisimman pian osoitteessa servicedesk@csc.fi. Projektipäällikön pyynnöstä CSC-projekti voidaan avata uudelleen tai tilapäinen pääsy palveluihin voidaan myöntää.

Sisältöä ei voi palauttaa 90 päivän jälkeen CSC-projektin sulkeutumisesta.

#### Kun projekti on suljettu {#when-the-project-is-closed}

Käyttäjät eivät voi käyttää projektin hakemia palveluita ja kaikki sisällöt palveluissa poistetaan 90 päivän kuluttua projektin sulkemisesta.

| Palvelu | Mitä tapahtuu, kun projekti on suljettu |
| -- | -- |
| Allas, Fairdata IDA, SD Connect | Projekti on poistettu käytöstä, eikä käyttäjät voi enää käyttää palvelua projektin kontekstissa. |
| Mahti ja Puhti | Uusia Slurm-tehtäviä ei voi lähettää. Käyttäjät eivät voi enää käyttää projektin dataa. |
| cPouta ja ePouta | Projekti on poistettu käytöstä, eikä käyttäjät voi enää käyttää palvelua projektin kontekstissa. Kaikki projektin virtuaalikoneet sammutetaan. |
| Rahti | Projektin pod-kvota asetetaan nollaan ja kaikki työkuormat pysäytetään. |
| SD Desktop | Työpöydät keskeytetään, projekti ei voi käynnistää uusia työpöytiä. |

!!! Huomio 

    Kaikki sisältö palveluissa poistetaan 90 päivän kuluttua projektin sulkemisesta. Jos tarvitset varmistuksen kaikkien sisältöjen poistamisesta palveluista, ole hyvä ja ota yhteyttä ServiceDesk:iin.
