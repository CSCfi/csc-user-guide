
# Yleiskatsaus

!!! Huom
    Katso [LUMI-dokumentaatiosta](https://docs.lumi-supercomputer.eu/hardware/)
    yleiskatsaus LUMI-supertietokoneesta.

Puhti ja Mahti ovat CSC:n supertietokoneita. Puhti on ollut CSC:n käyttäjien
käytettävissä 2. syyskuuta 2019 lähtien ja Mahti 26. elokuuta 2020 lähtien. LUMI on
yksi pan-eurooppalaisista pre-eksaskaala-suupertietokoneista, ja se sijaitsee CSC:n
datakeskuksessa Kajaanissa. LUMIn prosessori-osa (LUMI-C) on ollut saatavilla
vuoden 2022 alusta lähtien, ja koko järjestelmä suuremman LUMI-G-osion kanssa
on ollut saatavilla vuoden 2023 alusta lähtien.

Puhti sisältää prosessorisolmuja eri muistimäärillä sekä suuren GPU-osion (Puhti AI),
kun taas Mahti sisältää homogeenisia prosessorisolmuja ja on tarkoitettu suuremmille
töille (vähintään 128 suoritinydintä). Mahtiin sisältyy myös GPU-osio vuodesta 2021
lähtien (Mahti AI) Nvidia Ampeere GPU:illa. Katso [järjestelmien tarkemmat tiedot](available-systems.md)
ja [erot LUMI-C:n ja Mahtin välillä](lumi-vs-mahti.md).

CSC:n supertietokoneet käyttävät Linux-käyttöjärjestelmää ja suosittelemme
tutustumaan [Linux-käyttöjärjestelmän perusteisiin](../support/tutorials/env-guide/index.md)
ennen aloitusta.

## Puhtin ja Mahtin käyttö {#accessing-puhti-and-mahti}

Jotta voit käyttää CSC:n supertietokoneita, sinulla täytyy olla CSC-käyttäjätili,
joka kuuluu laskentahankkeeseen, jolla on pääsy kyseisiin supertietokoneisiin.
CSC-käyttäjätilit ja hankkeet hallitaan [MyCSC-portaalissa](https://my.csc.fi).
Lisäohjeita löytyy tästä käyttäjäoppaasta kohdasta [Tilien hallinta](../accounts/index.md).

!!! Huom
    LUMI-supertietokoneen käyttöoikeuden saamiseksi sinun täytyy [luoda LUMI-spesifinen
    projekti](../accounts/how-to-create-new-project.md#creating-a-lumi-project-and-applying-for-resources).
    Lisätietoja LUMIn käytön aloittamisesta löytyy [LUMI-dokumentaatiosta](https://docs.lumi-supercomputer.eu/firststeps/getstarted/).

## Yhteyden muodostaminen supertietokoneisiin {#connecting-to-the-supercomputers}

--8<-- "auth-update-ssh.md"

Yhdistä SSH-asiakkaan avulla:

```bash
ssh yourcscusername@puhti.csc.fi
```

tai

```bash
ssh yourcscusername@mahti.csc.fi
```

Tämä yhdistää sinut johonkin kirjautumissolmuista. Jos tarvitset yhteyden
tiettyyn kirjautumissolmuun, käytä komentoa:

```bash
ssh yourcscusername@puhti-login[11-12,14-15].csc.fi
```

tai

```bash
ssh yourcscusername@mahti-login[11-12,14-15].csc.fi
```

Missä `yourcscusername` on CSC:ltä saamasi käyttäjänimi.

Lisätietoja löytyy [yhteydenotto](connecting/index.md) sivulta.

Puhtiin ja Mahtiin voi myös liittyä niiden omien
[verkkorajapintojen](webinterface/index.md) kautta, jotka ovat saatavilla osoitteissa
[www.puhti.csc.fi](https://www.puhti.csc.fi) ja
[www.mahti.csc.fi](https://www.mahti.csc.fi).

### Skaalautuvuus {#scalability}

Älä varaa työhaullesi enemmän resursseja kuin se voi tehokkaasti käyttää.
Tämä täytyy varmistaa jokaisen uuden koodin ja työn tyypin (eri syötteen)
kohdalla skaalautuvuustestillä. Käytäntö on, että työn pitäisi olla **vähintään
1,5 kertaa nopeampi**, kun kaksinkertaistat resurssit (ytimet). [Ohjeet skaalautuvuustestin
suorittamiseen](../support/tutorials/cmdline-handson.md#scaling-test-for-an-mpi-parallel-job).
Huomioi myös [muut tärkeät suorituskykyyn liittyvät tekijät.](performance.md)

## Projektit ja kiintiöt {#projects-and-quotas}

Työskentely CSC:n supertietokoneilla perustuu projekteihin. Laskenta- ja tallennusresurssit
kohdennetaan projekteille, ja kun aloitat eräajon, sinun täytyy aina määritellä projekti,
jonka osa työ on.

Projektit hallitaan [MyCSC-portaalissa](https://my.csc.fi), missä voit lisätä
palveluita, resursseja ja käyttäjiä CSC-projekteihisi.

CSC:n supertietokoneilla voit tarkistaa tällä hetkellä aktiiviset projektisi komennolla:

```text
csc-projects
```

Tämä komento näyttää tiedot kaikista CSC-projekteistasi. Voit valita vain yhden projektin
raportoimaan `-p` optiolla. Esimerkiksi:

```bash
[kkayttaj@puhti ~]$ csc-projects -p project_2012345
-----------------------------------------------------------------
Project: project_2012345    Owner: Kalle Käyttäjä
Title: "Ortotopolgian mallintaminen"
Start: 2015-12-17 End: 2022-03-16 Status: open
Budget:   1174188  Used   1115284 Remain:      58904
Latest resource grant: 2019-03-04
-----------------------------------------------------------------
```

Komento raportoi projektin omistajan, otsikon, aloitus- ja päättymispäivät. Lisäksi
komento tulostaa projektin budjetointitiedot: kuinka monta laskentayksikköä
projektiisi on myönnetty, kuinka monta niistä on käytetty ja kuinka monta on
jäljellä.

Projektiisi liitetyt [levytilat](disk.md) voi tarkistaa komennolla:

```text
csc-workspaces
```

## Puhtin ja Mahtin käyttö {#using-puhti-and-mahti}

* [Järjestelmät](available-systems.md): Mitä laskentaresursseja on saatavilla
* [Käyttöpolitiikka](usage-policy.md): CSC:n supertietokoneiden käyttöpolitiikka
* [Yhteyden muodostaminen](connecting/index.md): Miten muodostaa yhteys CSC:n supertietokoneisiin
* [Puhti verkkorajapinta](webinterface/index.md): Miten yhdistää Puhtiin
  verkkorajapinnan avulla
* [Levyalueet](disk.md): Missä säilyttää dataa CSC:n supertietokoneilla
* [Moduulit](modules.md): Miten löytää tarvitsemasi ohjelmat
* [Sovellukset](../apps/index.md): Sovelluskohtaiset ohjeet.
* [Ajotehtävien suorittaminen](running/getting-started.md): Miten suorittaa ohjelmia
  supertietokoneilla
* Ohjelmistojen asennus ja kääntäminen:
    * [Ohjelmistojen asennus](installing.md)
    * [Kääntäminen Puhtissa](compiling-puhti.md)
    * [Kääntäminen Mahtissa](compiling-mahti.md)
* [Sovellusten virheenkorjaus](debugging.md): Miten virheenkorjata sovelluksia
* [Suorituskyvyn analysointi](performance.md): Miten ymmärtää sovellustesi suorituskykyä
