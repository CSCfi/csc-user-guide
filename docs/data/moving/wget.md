# Wgetin käyttäminen datan lataamiseen verkkosivuilta CSC:lle {#using-wget-to-download-data-from-websites-to-csc}

`wget` on komento, jolla voidaan ladata tiedostoja WWW-sivustoilta ja FTP-palvelimilta. Kun olet selvittänyt tiedoston URL-osoitteen, anna se `wget`-komennon argumenttina ladataksesi tiedoston nykyiseen hakemistoosi.

```bash
wget URL
```

Esimerkiksi:

```bash
wget ftp://ftp.gromacs.org/gromacs/gromacs-2024.2.tar.gz
```

tämä komento lataa tiedoston nimeltä `gromacs-2024.2.tar.gz` nykyiseen hakemistoosi. URL-osoitteen mallintaminen on mahdollista FTP:n yhteydessä, ts. URL alkaa `ftp://`:

```bash
wget ftp://ftp.gromacs.org/gromacs/gromacs-2024.*.tar.gz
```

Tämä komento hakee kaikki tiedostot, joiden nimi alkaa `gromacs-2024.` ja päättyy `.tar.gz`.

Voit hienosäätää `wget`-komennon käyttäytymistä useilla optioilla. Saat näkyviin käytettävissä olevien komentojen optioiden täydellisen listan komennolla:

```bash
man wget
```

Alla on lueteltu joitakin yleisimmin käytettyjä optioita.

|Optio       |Argumentti |Kuvaus         |
|------------|-----------|---------------|
|`-i`        |URL        |Lue tiedosto, joka sisältää haettavien URL-osoitteiden listan.|
|`-O`        |tiedoston nimi|Lähtötiedoston nimi.|
|`-o`        |tiedoston nimi|Latauksen lokitiedoston nimi.|
|`-p`        |hakemisto  |Määrittelee hakemiston, johon ladattu data tallennetaan. Oletuksena on nykyinen hakemisto.|
|`-c`        |           |Jatka osittain ladatun tiedoston hakemista.|
|`--user`    |käyttäjänimi|Määritä käyttäjänimi tiedoston hakua varten.|
|`--password`|salasana   |Määritä salasana tiedoston hakua varten.|
|`-N`        |           |Käytä aikaleimoja. Lataa tiedosto vain, jos se on uudempi kuin kohdehakemistossa oleva tiedosto.|
|`-m`        |           |Ota käyttöön peilaukseen sopivat optiot. Tämä optio ottaa käyttöön rekursion ja aikaleiman, asettaa rekursion syvyyden loputtomaksi ja säilyttää FTP-hakemistolistaukset.|

