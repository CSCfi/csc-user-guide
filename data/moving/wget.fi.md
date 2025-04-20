# CSC:n käyttäminen wget-komennon avulla verkkosivujen datan lataamiseen {#using-wget-to-download-data-from-websites-to-csc}

`wget` on komento, jolla voidaan ladata tiedostoja WWW-sivuilta ja FTP-palvelimilta. Kun olet selvittänyt tiedoston URL-osoitteen, anna se argumenttina `wget`-komennolle ladataksesi tiedoston nykyiseen hakemistoosi.

```bash
wget URL
```

Esimerkiksi:

```bash
wget ftp://ftp.gromacs.org/gromacs/gromacs-2024.2.tar.gz
```

tämä komento lataa tiedoston nimeltä `gromacs-2024.2.tar.gz` nykyiseen hakemistoosi.
Jokaiselle URL-osoitteelle voidaan käyttää jokerimerkkejä FTP-siirroissa, eli kun URL-osoite alkaa muodossa `ftp://`:

```bash
wget ftp://ftp.gromacs.org/gromacs/gromacs-2024.*.tar.gz
```

Tämä komento noutaa kaikki tiedostot, joiden nimi alkaa `gromacs-2024.` ja päättyy `.tar.gz`.

Voit hienosäätää `wget`-komennon toimintaa useilla eri asetuksilla. Näet kaikki käytettävissä olevat komentoasetukset komennolla:

```bash
man wget
```

Alla on lueteltuna joitain yleisimmin käytetyistä asetuksista.

|Asetus       |Argumentti  |Kuvaus  |
|-------------|------------|--------|
|`-i`         |URL         |Lue tiedosto, joka sisältää haettavat URL-osoitteet.|
|`-O`         |tiedostonimi|Ulostulotiedoston nimi.|
|`-o`         |tiedostonimi|Latauslokitiedoston nimi.|
|`-p`         |hakemisto   |Määrittää hakemiston, johon ladattu data tallennetaan. Oletuksena nykyinen hakemisto.|
|`-c`         |            |Jatka aiemmin osittain ladatun tiedoston lataamista.|
|`--user`     |käyttäjätunnus|Määritä tiedoston hakemiseen käytettävä käyttäjätunnus.|
|`--password` |salasana    |Määritä tiedoston hakemiseen käytettävä salasana.|
|`-N`         |            |Käytä aikaleimaan perustuvaa latausta. Lataa tiedosto vain, jos se on uudempi kuin kohdehakemistossa oleva tiedosto.|
|`-m`         |            |Ota käyttöön peilaamiseen sopivat asetukset. Tämä asetus ottaa käyttöön rekursion ja aikaleimauksen, asettaa äärettömän rekursion syvyyden ja säilyttää FTP-hakemistolistat.|