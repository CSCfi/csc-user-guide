# Tiedostojen kopiointi käyttäen scp:tä {#copying-files-using-scp}

Tiedostojen kopiointi eri Linux-, macOS- ja Windows-laitteiden välillä voidaan
tehdä `scp`-komennolla. Näin voit käyttää `scp`:tä siirtääksesi dataa CSC:n ja
paikallisen tietokoneesi välillä tai CSC:n eri tiedostojärjestelmien välillä.

Perussyntaksi datan kopioimiseksi paikalliselta koneelta etäpalvelimelle on:

```bash
scp /path/to/file username@server:/path/to/remote/destination
```

Vastaavasti syntaksi tiedostojen kopioimiseksi etäpalvelimelta paikalliselle
koneelle on:

```bash
scp username@server:/path/to/file /path/to/local/destination
```

Esimerkiksi komento paikallisen tiedoston `data.txt` kopioimiseksi nykyisestä
hakemistosta käyttäjän `bob` kotihakemistoon Puhtilla olisi:

```bash
scp data.txt bob@puhti.csc.fi:~/
```

Erityinen symboli `~` osoittaa käyttäjän kotihakemistoon. Voit käyttää
`csc-workspaces`-komentoa Puhtilla nähdäksesi muita saatavilla olevia
levyalueita.

Kopioidaksesi kokonaisia hakemistoja, sinun tulisi käyttää `scp`-komentoa
vaihtoehdolla `-r`. Esimerkiksi:

```bash
scp -r /path/to/data_directory bob@puhti.csc.fi:/scratch/project_2001234/data_dir 
```

Yllä oleva komento kopioisi hakemiston `data_directory` ja sen kaikki
sisällöt Puhtille hakemistoon `/scratch/project_2001234/data_dir`.

Datan kopiointi CSC-palvelimelta paikalliselle koneellesi tehdään samalla
tavalla:

```bash
scp bob@puhti.csc.fi:/scratch/project_2001234/data.txt .
```

Symboli `.` osoittaa nykyiseen työskentelyhakemistoon paikallisella
koneellasi, eli paikkaan, jossa suoritat `scp`-komentoa.

Yllä olevissa komennoissa tiedostoja ja hakemistoja on kopioitu yksi kerrallaan.
Kuitenkin, `scp` voi myös kopioida useita tiedostoja kerralla. Esimerkiksi:

```bash
scp data1.txt data2.txt data3.txt bob@puhti.csc.fi:~/
```

Voit myös käyttää yleismerkkejä määriteltäessä kopioitavia tiedostoja. Esimerkiksi,
kopioidaksesi kaikki tiedostot, joiden pääte on `.txt`, nykyisestä
hakemistosta paikallisella koneellasi kotihakemistoon Puhtilla, voisit käyttää
komentoa:

```bash
scp *.txt bob@puhti.csc.fi:~/
```

Oletuksena kopioidut tiedostot käsitellään uusina tiedostoina, mutta jos lisäät vaihtoehdon
`-p` `scp`-komentoon, kopioitu tiedosto perii aikaleiman ja
käyttöoikeusmoodin alkuperäiseltä tiedostolta.