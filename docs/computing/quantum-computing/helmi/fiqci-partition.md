
# Erityisohjeet LUMIn FiQCI-osioon

LUMIn FiQCI-osio tarjoaa pääsyn Helmi-kvantaalitietokoneeseen. Pääsy myönnetään käyttäjille, jotka kuuluvat projekteihin, joille on myönnetty QPU-resursseja. LUMIn kautta Helmi-laitteella suoritettavien tehtävien lisäksi käyttäjät voivat käyttää yleistä LUMI-järjestelmää ja ohjelmistopinoa, mukaan lukien simulaattoreiden käyttäminen.

!!! info "Helmin tilan tarkistaminen"
    Voit tarkistaa yhteyden tilan täältä: [https://fiqci.fi/status](https://fiqci.fi/status)

## LUMI Helmi -projektit vs. tavalliset LUMI-projektit {#lumi-helmi-projects-vs-regular-lumi-projects}

Helmi-projektit eroavat hieman tavallisista LUMI-projekteista. Suurin ero on siinä, että sinun tulee hakea kvanttiresursseja CPU-, GPU- ja varastointiresurssien lisäksi.

!!! info "Pilottivaihe"
    Pilottivaiheen aikana hyväksytyt projektit saavat 24 tuntia pääsyä FiQCI-osioon.
    [Katso kutsuteksti yksityiskohtia varten](https://fiqci.fi/_posts/2022-11-01-Helmi-pilot/).

## FiQCI-osio `q_fiqci` {#the-fiqci-partition}

Pääsy Helmiin on saatavilla vain LUMIn FiQCI-osion kautta, joka tarjoaa suoran yhteyden [LUMI-C-solmun](https://docs.lumi-supercomputer.eu/hardware/lumic/) ja Helmin välille.

* [Lisätietoja LUMI-solmuista](https://docs.lumi-supercomputer.eu/hardware/)

Helmin osiossa on yksi jono joka vastaa FiQCI-projekteja: `q_fiqci`.
Tällä hetkellä kvanttilaskentatehtävän enimmäiskäyttöaika on 2 tuntia.

| Nimi      | Enimmäisaika | Enimmäistehtävät |
| --------- | ------------ | ---------------- |
| _q_fiqci_ | _2 tuntia_   | _64_             |

## Tallennusalueet {#storage-areas}

Helmin osiossa käytetään samoja tallennuspolitiikkoja kuin LUMIlla. Katso [lisätietoja LUMI-tallennuksesta täältä](https://docs.lumi-supercomputer.eu/storage/).

## Käyttö ja laskutus {#usage-and-billing}

Kvanttijärjestelmäprojektit toimivat samankaltaisesti kuin tavallinen LUMI-järjestelmä. Tärkeimmät erot ovat:

1. FiQCI-projekteissa käytetään `--partition=q_fiqci` osiota tavanomaisen LUMI-C `--partition=standard` ja `--partition=small` sijasta.
2. Enimmäistöksen käyttöaika on **2 tuntia**.
3. Käyttö laskutetaan QPU-sekunteina **QPUs**:na `q_fiqci` osiossa.
4. LUMI-Helmi laskentaympäristö on ladattava erikseen. Katso [Suorittaminen Helmissä](./running-on-helmi.md) yksityiskohtia varten.

Tällä hetkellä `q_fiqci` jonon kautta suoritettavat tehtävät kuluttavat QPU-sekunteja sen mukaan, kuinka paljon käyttöaikaa kuluu `q_fiqci` jonossa.

!!! success "Käytettyjen QPUsien kysely"
    Voit tarkistaa käytetyt QPUsit käyttämällä `lumi-allocations` työkalua.

Helmi-spesifiseen tukeen pääsee [CSC Service Deskin](../../../support/contact.md) kautta. Huomaa, että tällä hetkellä käyttäjätuki on rajoitettu teknisiin kysymyksiin.
