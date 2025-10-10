# LUMIn FiQCI-osiota koskevat erityisohjeet { #specific-instructions-for-the-fiqci-partition-on-lumi }

LUMIn FiQCI-osio tarjoaa pääsyn kvanttiprosessoriyksiköihin (QPU) käyttäjille, jotka kuuluvat projekteihin, joille on myönnetty QPU-resursseja. LUMIn kautta suoritettavien kvanttikuormien lisäksi käyttäjät voivat hyödyntää koko LUMIn infrastruktuuria, mukaan lukien sen ohjelmistopino ja kvanttisimulaattorit, kehittämistä, testausta sekä hybridi kvantti-klassisia työnkulkuja varten.

!!! info "Näytä kvanttitietokoneiden tila"
	Voit tarkistaa yhteyden tilan täältä: [https://fiqci.fi/status](https://fiqci.fi/status)


## LUMIn kvanttilaskentaprojektit vs. tavalliset LUMI-projektit { #lumi-quantum-computing-projects-vs-regular-lumi-projects }

Kvanttilaskentaprojektit poikkeavat hieman tavanomaisista LUMI-projekteista. Tärkein ero on, että sinun on haettava kvanttiresursseja CPU-, GPU- ja tallennusresurssien lisäksi.
Lisätietoja kvanttilaskentaprojektien hakemisesta löytyy [täältä](./projects.md).

## FiQCI-osio `q_fiqci` { #the-fiqci-partition-q_fiqci }

LUMIn `q_fiqci`-osio on omistettu kvanttilaskentakuormille. Se tarjoaa suoran yhteyden [LUMI-C
solmun](https://docs.lumi-supercomputer.eu/hardware/lumic/) ja FiQCI:n kvanttitietokoneiden välille.

* [Lisätietoja LUMI-solmuista](https://docs.lumi-supercomputer.eu/hardware/)

FiQCI-projekteja vastaavassa LUMIn osiossa on yksi jono: `q_fiqci`. 
Tällä hetkellä kvanttitehtävän enimmäissuoritusaika on 2 tuntia.

| Nimi     | Enimmäisseinäaika | Enimmäismäärä töitä |
| -------- | ------------------ | ------------------- |
| _q_fiqci_ | _2 tuntia_        | _64_                |


## Tallennusalueet { #storage-areas }

`q_fiqci`-osio noudattaa samoja tallennuskäytäntöjä kuin LUMI. [Lisätietoja LUMIn tallennuksesta löytyy täältä](https://docs.lumi-supercomputer.eu/storage/).

## Käyttö ja laskutus { #usage-and-billing }

Kvanttilaskentaprojektit toimivat pitkälti kuten tavallinen LUMI-järjestelmä. Tärkeimmät erot ovat:

1. LUMIn erillinen kvanttilaskentaosio on `q_fiqci`.
2. Työn enimmäisseinäaika on **2 tuntia**.
3. Käyttö laskutetaan QPU-sekunteina (QPU:t).
4. LUMI-Fiqci-laskentaympäristö täytyy ladata erikseen. Katso lisätiedot kohdasta [Kvanttitöiden ajaminen](./running-quantum-jobs.md).


Tukeen saa yhteyden [CSC Service Deskin](../../support/contact.md) kautta LUMIin liittyvissä asioissa tai osoitteesta [fiqci-feedback@postit.csc.fi](mailto:fiqci-feedback@postit.csc.fi) FiQCIin ja kvanttilaskentapalveluihin liittyvissä asioissa.