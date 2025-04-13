
# Rsyncin käyttäminen tiedonsiirtoon ja synkronointiin {#using-rsync-for-data-transfer-and-synchronization}

**Rsync** on tiedonsiirtotyökalu, jota voidaan käyttää samoin kuin `scp`-komentoa. Kun tietoja siirretään, `rsync` tarkistaa eron lähde- ja kohdetiedostojen välillä ja siirtää vain muuttuneet osat. Tämä tekee `rsyncistä` sopivan:

1. **Kansioiden synkronointiin**. `scp` tai `cp` kopioisivat ja siirtäisivät kaiken, kun taas `rsync` kopioi ja siirtää vain muutokset.
2. **Suurten tiedostojen siirtämiseen**. `rsync` voidaan asettaa tallentamaan edistyminen, joten jos siirto keskeytyy, se voidaan jatkaa samasta kohdasta.

`Rsync`:in peruskomentosyntaksi on:

```bash
rsync -options source target
```

Jos datalähde tai -kohdesijainti on etäsivusto, se määritellään syntaksilla:

```bash
username@server:/path/on/server
```

Kohde ja lähde voivat kuitenkin sijaita samalla koneella. Tällöin voit yksinkertaisesti antaa hakemistopolut lähde- ja kohdesivustoille.

Alla olevassa taulukossa on lueteltu yleisimmin käytetyt vaihtoehdot:

|Vaihtoehto    |Argumentti|Kuvaus|
|--------------|----------|------|
|`-r`          |          |Sukella hakemistoihin|
|`-a`          |          |Käytä arkistotilaa: kopioi tiedostot ja hakemistot rekursiivisesti ja säilytä käyttöoikeudet ja aikaleimat|
|`-v`          |          |Näytä tarkka tieto|
|`-z`          |          |Pakkaa|
|`-e`          |`ssh`     |Määritä käytettävä etäkuori|
|`-n`          |          |Näytä mitkä tiedostot siirrettäisiin|
|`--partial`   |          |Säilytä osittain siirretyt tiedostot|
|`--progress`  |          |Näytä siirron edistyminen|
|`-P`          |          |Sama kuin `--partial --progress`|

Joten komentoa paikallisen kansion siirtämiseksi Puhtiin, näyttäen edistymisen ja säilyttäen osittain siirretyt tiedostot, käytettäisiin esimerkiksi:

```bash
rsync -rP /path/to/local/folder username@puhti.csc.fi:/path/to/target
```

Tämä joko:

1. Luo kansion Puhtiin sijaintiin `/path/to/target/folder`, jos kansiota ei ollut olemassa aiemmin. Tässä tapauksessa kaikki paikallisen kansion sisältö siirretään.
2. Synkronoi lähde- ja kohdekansiot, jos kansio on jo olemassa Puhtissa. Tässä tapauksessa vain tehdyt muutokset siirretään.

Ja sama asia päinvastoin:

```bash
rsync -rP username@puhti.csc.fi:/path/to/target/folder /path/to/local
```

!!! varoitus
    `rsync` korvaa aina kaikki kohteeseen tehdyt muutokset, vaikka ne olisivat uudempiakin kuin lähde!
