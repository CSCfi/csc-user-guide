
---
search:
  boost: 4
---

# Yleiskatsaus {#overview}

Kvanttitietokoneet eroavat klassisista vastineistaan peruslaskentaoperaattoreiden osalta. Ennen kuin QPU:t voidaan ottaa käyttöön, ne vaativat räätälöityjä ohjelmia ja algoritmeja. [Finnish Quantum-Computing Infrastructure](https://fiqci.fi) FiQCI tarjoaa pääsyn kvanttitietokoneiden resursseihin CSC:n palveluportaalien kautta.

## Helmi {#helmi}

**5 Qubitin Kvanttitietokone**

Helmi, Suomen ensimmäinen kvanttitietokone, on VTT:n ja IQM Quantum Computersin yhteiskehittämä. Tällä hetkellä Helmillä on 5 kubittia. Helmillä käyttäjät voivat suorittaa kvanttiohjelmia ja -algoritmeja todellisella, fyysisellä laitteella.

Pääsy Helmiin tapahtuu LUMI-supertietokoneympäristön kautta. Käyttäjien on haettava kvanttitietoprojektia LUMIssa, joka mahdollistaa pääsyn Helmiin LUMIn työnhallintajärjestelmän (SLURM) kautta. Projektihakemus tehdään [MyCSC:n](../../accounts/how-to-create-new-project.md) kautta.

Lisätietoa lukemalla:

* [Teknisempi kuvaus Helmistä](./helmi/helmi-specs.md).
* [Erityiset ohjeet LUMI Helmi -osio](./helmi/fiqci-partition.md)
* [Helmin käytön aloittaminen](./helmi/helmi-from-lumi.md)
* [LUMI-dokumentaatiosivu](https://docs.lumi-supercomputer.eu/)


## Kvasi {#kvasi}

**Kvanttioppimiskone**

Kvasi on edistynyt kvanttitietokonesimulaattori/emulaattori. Kvasin avulla käyttäjä voi tutkia ja kehittää algoritmeja kvanttitietokoneita varten. Lue täältä [yksityiskohtaiset ohjeet käyttöön](../quantum-computing/kvasi/kvasi.md).

Kvasi tarjoaa ekosysteemin kvanttialgoritmien kehittämiseen ja simuloimiseen sekä ideaalissa että realistisessa, meluisassa tilanteessa. Kvasin avulla voit optimoida algoritmisi tiettyä laitteistokokoonpanoa (QPU) varten, jossa on tietty kubittiyhteys ja tietyt perusporttioperaatiot.

Algoritmit voidaan kehittää joko laitteistotasoa lähellä käyttäen Atos Quantum Assembler (AQASM) -kieltä tai korkeammalla tasolla Python-pohjaisen kielen ja käyttövalmiiden kirjastojen avulla. QLM sisältää useita valmiita esimerkkejä. Voit myös ladata ja suorittaa paikallisesti [myQLM](../quantum-computing/kvasi/kvasi.md#myqlm) - kevyemmän version QLM-ekosysteemistä.
