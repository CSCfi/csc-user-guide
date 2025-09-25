---
tags:
  - Free
catalog:
  name: Entrez Direct
  description: Entrez direct - command line tool to search and retrieve data from NCBI
  description_fi: Entrez Direct – komentorivityökalu tietojen hakemiseen ja noutamiseen NCBI:stä
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Entrez Direct { #entrez-direct }

Edirect eli Entrez Direct on työkalupaketti, jonka avulla voidaan hakea sekvenssejä ja muuta dataa NCBI:n sekvenssitietokannoista annettujen hakuehtojen perusteella. 
Paketti koostuu useista komennoista:

1. Navigointitoiminnot tukevat Entrez-tietokantojen selaamista:
    * `esearch` suorittaa uuden Entrez-haun käyttäen termejä indeksoiduista kentistä.
    * `elink` etsii naapurit (tietokannan sisällä) tai linkit (tietokantojen välillä).
    * `efilter` suodattaa tai rajoittaa aiemman kyselyn tuloksia.
2. Tietueita voidaan noutaa määrätyissä muodoissa tai dokumenttiyhteenvedoin:
    * `efetch` lataa tietueita tai raportteja määrätyssä muodossa.
3. Halutut kentät XML-tuloksista voidaan erottaa ilman ohjelmointia:
    * `xtract` muuntaa Edirectin XML-tulosteen taulukoksi arvoista.
4. Myös useita lisätoimintoja on tarjolla:
    * `einfo` hakee tietoa indeksoiduista kentistä Entrez-tietokannassa.
    * `epost` lataa yksilöllisiä tunnisteita (UID) tai sekvenssien tunnuksia (accession).
    * `nquire` lähettää URL-pyynnön verkkosivulle tai CGI-palveluun

[TOC]

## License { #license }

Vapaasti käytettävissä kaikille käyttäjille. [Public Domain notice](https://www.ncbi.nlm.nih.gov/books/NBK179288/#chapter6.Appendices).

## Available { #available }

Puhti: 13.4

## Usage { #usage }

Edellä luetellut `edirect`-komennot aktivoidaan lataamalla `biokit`-moduuli.

```bash
module load biokit
```

Tämän jälkeen voit esimerkiksi käyttää `esearch`- ja `efetch`-komentoja noutamaan proteiini- tai nukleotidisekvenssien tietueita, joiden annotaatio vastaa annettuja hakuehtoja. Hakuehdoissa voi käyttää myös jokerimerkkiä `*` vastaamaan mitä tahansa merkkijonoa. Haku on kirjainkoosta riippumaton: "Mus" ja "mus" tuottavat samat osumat. Voit myös rajata hakua tiettyihin hakutietokannan kenttiin (Keywords, Author, Organism, Accession, Gene name, Protein name, Sequence length jne.). Sekvenssipituuden tapauksessa alue määritellään syntaksilla `from:to`. Esimerkiksi: `120:125`.

Yleensä on viisasta käyttää ensin pelkkää `esearch`-komentoa saadakseen käsityksen siitä, kuinka monta osumaa löytyy. 
Esimerkiksi haku:

```bash
esearch -db nucleotide -query barc
```

ilmoittaa, että 267791 osumaa löytyi.

```xml
<ENTREZ_DIRECT>
  <Db>nucleotide</Db>
  <WebEnv>NCID_1_7176041_130.14.18.48_9001_1567161450_1478919739_0MetA0_S_MegaStore</WebEnv>
  <QueryKey>1</QueryKey>
  <Count>267791</Count>
  <Step>1</Step>
</ENTREZ_DIRECT>
```

Tässä tapauksessa voi olla järkevää tarkentaa hakua ennen kuin hakumäärittely putkitetaan eteenpäin `efetch`-komennolle varsinaista datan noutoa varten. Yksi haku voi sisältää useita hakuehtoja, jotka yhdistetään loogisilla operaattoreilla (`AND`, `OR`, `NOT`). Vastaavat sekvenssit voidaan tallentaa useissa eri muodoissa; esimerkiksi fasta- tai GenBank-muodot ovat tuettuja. Alla oleva komento noutaa vain yhden tietueen, _Lyngbya majuscula_ -lajin barbamidin biosynteesin geeniklastterin, joka sisältää geenin nimeltä _braC_.

```bash
esearch -db nucleotide -query "barc [GENE] AND Lyngbya majuscula [ORGN]" | efetch -format gb > barc_Lm.gb
```

## More information { #more-information }

* [Edirect-manuaali](https://www.ncbi.nlm.nih.gov/books/NBK179288/)