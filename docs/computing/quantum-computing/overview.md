---
search:
  boost: 4
---

!!! warning "HUOMAUTUS: QPU-ajan seuranta"
    Käytetty QPU-aika ei vielä näy oikein MyCSC:ssä. Käyttö kirjautuu kuitenkin oikein sisäisesti,
    ja korjaamme parhaillaan MyCSC:ssä näkyvää aikaa. Jos sinulla on kysyttävää, voit ottaa meihin yhteyttä osoitteessa
    [fiqci-feedback@postit.csc.fi](mailto:fiqci-feedback@postit.csc.fi). 


# Yleiskatsaus { #overview }

Kvanttitietokoneet poikkeavat klassisista vastineistaan peruslaskentaoperaattoreiden osalta. Ennen kuin QPU:ita voidaan hyödyntää, ne vaativat räätälöityjä ohjelmia ja algoritmeja. [Finnish Quantum-Computing Infrastructure](https://fiqci.fi) FiQCI tarjoaa pääsyn kvanttilaskennan resursseihin CSC:n palveluportaaleiden kautta.

## Kvanttitietokoneet { #quantum-computers }

### Helmi (VTT Q5) { #helmi-vtt-q5 }

Helmi, Suomen ensimmäinen kvanttitietokone, on VTT:n ja IQM Quantum Computersin yhteiskehittämä. Se tarjoaa 5-kubitisen järjestelmän, jonka avulla käyttäjät voivat suorittaa kvanttiohjelmia ja -algoritmeja fyysisellä kvanttilaitteella.

Pääsy Helmiin järjestetään LUMI-supertietokoneympäristön kautta. Käyttäjien tulee hakea LUMIin kvanttilaskentaprojektia, joka antaa pääsyn Helmiin LUMIn ajonhallinnan (SLURM) kautta. Projektia haetaan [MyCSC:n](../../accounts/how-to-create-new-project.md) kautta.


### VTT Q50 { #vtt-q50 }

Q50 on 53-kubitinen kvanttitietokone, jonka ovat myös kehittäneet yhdessä VTT ja IQM Quantum Computers.

Samoin kuin Helmiin, myös Q50:een pääsee LUMI-supertietokoneympäristön kautta. Käyttäjien tulee hakea LUMIin kvanttilaskentaprojektia. Hyväksymisen jälkeen Q50:een pääsee LUMIn ajonhallinnan (SLURM) avulla.
Katso [Open Call](https://fiqci.fi/publications/2025-03-04-Q50-Call-1_2025) -julkaisusta tarkemmat ohjeet Q50-käyttöoikeuden projektihakemuksesta.


Lisälukemista:

* [Teknisempi kuvaus kvanttitietokoneista](./specs.md).
* [fiqci-osion erityisohjeet](./fiqci-partition.md)
* [Helmi/Q50: käytön aloitus](./access.md)
* [LUMI:n dokumentaatiosivu](https://docs.lumi-supercomputer.eu/)


## Simulaattorit { #simulators }

### Qiskit { #qiskit }

LUMI-supertietokone tukee nyt kvanttialgoritmien simulointia jopa 44 kubittiin saakka Qiskitilla, IBM:n avoimen lähdekoodin kvanttilaskentakehyksellä. Tämän ansiosta tutkijat voivat tutkia ja testata laajamittaisia kvanttialgoritmeja valmistautuakseen kvanttietuun.

Lisätietoja löytyy tästä [blogikirjoituksesta](https://fiqci.fi/publications/2025-04-01-LUMI-quantum-simulations-qiskit-aer)