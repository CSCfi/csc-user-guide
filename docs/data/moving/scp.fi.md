# Tiedostojen kopiointi scp:llä {#copying-files-using-scp}

Tiedostojen kopiointi eri Linux-, macOS- ja Windows-koneiden välillä onnistuu
`scp`-komennolla. Näin voit käyttää `scp`:tä tiedostojen siirtämiseen CSC:n
ja oman tietokoneesi välillä, tai CSC:n eri tiedostojärjestelmien välillä.

Perussyntaksi tiedostojen kopioimiseksi paikalliselta koneelta etäpalvelimelle on:

```bash
scp /path/to/file username@server:/path/to/remote/destination
```

Vastaavasti syntaksi tiedostojen kopioimiseksi etäpalvelimelta paikalliselle
koneelle on:

```bash
scp username@server:/path/to/file /path/to/local/destination
```

Esimerkiksi komento, jolla kopioidaan paikallinen tiedosto `data.txt`
nykyisestä hakemistosta käyttäjä `bob`:n kotihakemistoon Puhtiin, on:

```bash
scp data.txt bob@puhti.csc.fi:~/
```

Erikoismerkki `~` osoittaa käyttäjän kotihakemistoon. Voit käyttää
`csc-workspaces`-komentoa Puhtissa nähdäksesi muut käytettävissä olevat
levyalueet.

Kokonaisen hakemiston kopioimiseen kannattaa käyttää `scp`-komentoa valitsimella
`-r`. Esimerkiksi:

```bash
scp -r /path/to/data_directory bob@puhti.csc.fi:/scratch/project_2001234/data_dir 
```

Yllä oleva komento kopioi hakemiston `data_directory` ja kaikki sen sisällöt
Puhtiin polkuun `/scratch/project_2001234/data_dir`.

Datan kopiointi CSC:n palvelimelta paikalliselle koneellesi tapahtuu samalla
tavalla:

```bash
scp bob@puhti.csc.fi:/scratch/project_2001234/data.txt .
```

Symboli `.` osoittaa nykyiseen työhakemistoon paikallisella koneellasi,
eli sijaintiin, jossa suoritat `scp`-komentoa.

Yllä olevissa komennoissa tiedostot ja hakemistot kopioitiin yksi kerrallaan.
`scp` voi kuitenkin kopioida useita tiedostoja kerralla. Esimerkiksi:

```bash
scp data1.txt data2.txt data3.txt bob@puhti.csc.fi:~/
```

Voit myös käyttää jokerimerkkejä määrittäessäsi kopioitavia tiedostoja.
Esimerkiksi, kopioidaksesi kaikki `.txt`-päätteiset tiedostot nykyisestä
hakemistosta paikallisella koneellasi kotihakemistoosi Puhtissa, voit käyttää
komentoa:

```bash
scp *.txt bob@puhti.csc.fi:~/
```

Oletuksena kopioidut tiedostot käsitellään uusina, mutta jos lisäät valitsimen
`-p` `scp`-komentoon, tällöin kopioitu tiedosto säilyttää alkuperäisen
tiedoston aikaleiman ja käyttöoikeudet.