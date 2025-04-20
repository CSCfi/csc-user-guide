# Rsyncin käyttäminen tiedonsiirtoon ja synkronointiin {#using-rsync-for-data-transfer-and-synchronization}

**Rsync** on tiedonsiirtotyökalu, jota voi käyttää samalla tavalla kuin `scp`-komentoa. Kun tiedostoja siirretään, `rsync` tarkistaa lähde- ja kohdetiedostojen erot ja siirtää vain muuttuneet osat. Tämä tekee `rsync`:stä sopivan seuraaviin tarkoituksiin:

1. **Kansioiden synkronointi**. `scp` tai `cp` kopioisi ja siirtäisi kaiken, kun taas `rsync` kopioi ja siirtää vain muutokset.
2. **Suurten tiedostojen siirtäminen**. `rsync` voidaan asettaa tallentamaan siirtotilanne, joten jos siirto keskeytyy, sitä voidaan jatkaa samasta kohdasta.

`rsync`-komennon perussyntaksi on:

```bash
rsync -options lähde kohde
```

Jos tiedon lähde tai kohde sijaitsee etäkoneella, se määritellään seuraavasti:

```bash
käyttäjätunnus@palvelin:/polku/palvelimella
```

Kuitenkin sekä kohde että lähde voivat sijaita myös samalla koneella. Siinä tapauksessa voit yksinkertaisesti antaa lähde- ja kohdekansioiden hakemistopolut.

Alla olevassa taulukossa on yleisimmät käytetyt valitsimet:

|Valitsin      |Argumentti|Kuvaus|
|--------------|----------|------|
|`-r`          |          |Käy läpi kaikki hakemistot rekursiivisesti|
|`-a`          |          |Arkistotila: kopioi tiedostot ja kansiot rekursiivisesti ja säilyttää käyttöoikeudet sekä aikaleimat|
|`-v`          |          |Yksityiskohtainen tilatai|
|`-z`          |          |Pakkaa tiedot|
|`-e`          |`ssh`     |Määrittele käytettävä etäyhteysohjelma|
|`-n`          |          |Näytä, mitkä tiedostot siirrettäisiin|
|`--partial`   |          |Säilytä osittain siirretyt tiedostot|
|`--progress`  |          |Näytä siirron eteneminen|
|`-P`          |          |Sama kuin `--partial --progress`|

Komento paikallisen kansion siirtämiseksi Puhtiin ja siirron etenemisen sekä osittain siirrettyjen tiedostojen säilyttämisen näyttämiseksi voisi olla esimerkiksi:

```bash
rsync -rP /path/to/local/folder käyttäjätunnus@puhti.csc.fi:/path/to/target
```

Tämä suorittaa joko:

1. Luo kansion Puhtiin kohtaan `/path/to/target/folder`, jos kansiota ei ollut aiemmin olemassa. Tällöin kaikki paikallisen kansion sisältö siirretään.
2. Synkronoi lähde- ja kohdekansiot, jos kansio on jo olemassa Puhtissa. Tässä tapauksessa vain tehdyt muutokset siirretään.

Ja sama asia toiseen suuntaan:

```bash
rsync -rP käyttäjätunnus@puhti.csc.fi:/path/to/target/folder /path/to/local
```

!!! warning
    `rsync` korvaa aina kaikki muutokset, jotka on tehty kohteeseen, vaikka ne olisivat uudemmat kuin lähteen muutokset!