# Yleiskatsaus { #overview }

!!! Note
    Yleiskatsaus CSC:n seuraavaan kansalliseen supertietokoneeseen Roihuun, joka tulee vuonna 2026,
    [katso tältä sivulta](systems-roihu.md).

    Yleiskatsaus LUMI-supertietokoneeseen:
    [katso LUMI-dokumentaatio](https://docs.lumi-supercomputer.eu/hardware/).

Puhti ja Mahti ovat CSC:n supertietokoneita. Puhti on ollut CSC:n käyttäjien käytettävissä
2. syyskuuta 2019 alkaen ja Mahti 26. elokuuta 2020 alkaen. LUMI on yksi
paneurooppalaisista pre-eksaskaala-suertietokoneista, ja se sijaitsee CSC:n
konesalissa Kajaanissa. LUMIn CPU-osio (LUMI-C) on ollut käytettävissä
vuoden 2022 alusta, ja koko järjestelmä suuren LUMI-G-osion kanssa on ollut
käytettävissä vuoden 2023 alusta.

Puhtissa on CPU-solmuja eri muistimäärillä sekä laaja GPU-osio (Puhti AI),
kun taas Mahtissa on homogeeniset CPU-solmut ja se on tarkoitettu suuremmille
ajoille (vähintään 128 CPU-ydintä). Mahtissa on vuodesta 2021 lähtien myös
GPU-osio (Mahti AI), jossa on Nvidia Ampere -GPU:t. Katso järjestelmien
[yksityiskohdat](available-systems.md) ja [tältä sivulta LUMI-C:n ja Mahtin
erojen pääpiirteet](lumi-vs-mahti.md).

Puhti ja Mahti korvataan vuonna 2026 CSC:n seuraavalla kansallisella
supertietokoneella nimeltä **Roihu**. [Lue lisää Roihusta täältä](systems-roihu.md).

CSC:n supertietokoneissa käytetään Linux-käyttöjärjestelmää, ja suosittelemme
että tutustut [Linuxin komentorivin käytön](../support/tutorials/env-guide/index.md)
perusteisiin ennen aloittamista.

## Puhtiin ja Mahtiin pääsy { #accessing-puhti-and-mahti }

CSC:n supertietokoneiden käyttö edellyttää CSC:n käyttäjätiliä, joka kuuluu
laskentaprojektiin, jolla on pääsy kyseisiin supertietokoneisiin. CSC:n
käyttäjätilit ja projektit hallitaan [MyCSC-portaalissa](https://my.csc.fi).
Lisäohjeita on tämän käyttöoppaan [Tilit-osiossa](../accounts/index.md).

!!! Note
    Päästäksesi LUMI-supertietokoneelle sinun tulee [luoda LUMI-kohtainen
    projekti](../accounts/how-to-create-new-project.md#creating-a-lumi-project-and-applying-for-resources).
    Lisätietoja LUMIn käytön aloittamisesta: [LUMI-dokumentaatio](https://docs.lumi-supercomputer.eu/firststeps/getstarted/).

## Yhteyden muodostaminen supertietokoneille { #connecting-to-the-supercomputers }

--8<-- "auth-update-ssh.md"

Yhdistä SSH-asiakasohjelmalla:

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

Missä `yourcscusername` on CSC:ltä saamasi käyttäjätunnus.

Lisätietoja sivulla [yhteyden muodostaminen](connecting/index.md).

Puhtia ja Mahtia voi käyttää myös niiden
[verkkokäyttöliittymien](webinterface/index.md) kautta osoitteissa
[www.puhti.csc.fi](https://www.puhti.csc.fi) ja
[www.mahti.csc.fi](https://www.mahti.csc.fi).

### Skaalautuvuus { #scalability }

Älä varaa työllesi enempää resursseja kuin se pystyy käyttämään tehokkaasti.
Tämä tulee varmistaa jokaiselle uudelle koodille ja ajotyypille (eri syöte)
skaalaustestillä. Periaate on, että työn tulisi olla
**vähintään 1,5 kertaa nopeampi**, kun kaksinkertaistat resurssit (ytimet).
[Ohjeet skaalautuvuustestin suorittamiseen](../support/tutorials/cmdline-handson.md#scaling-test-for-an-mpi-parallel-job).
Huomioi myös [muut suorituskykyyn liittyvät tärkeät tekijät.](performance.md)

## Projektit ja kiintiöt { #projects-and-quotas }

Työskentely CSC:n supertietokoneissa perustuu projekteihin. Laskenta- ja
tallennusresurssit myönnetään projekteille, ja kun käynnistät eräajon,
sinun on aina määritettävä projekti, johon ajo kuuluu.

Projekteja hallitaan [MyCSC-portaalissa](https://my.csc.fi), jossa voit lisätä
palveluita, resursseja ja käyttäjiä CSC-projekteihisi.

CSC:n supertietokoneissa voit tarkistaa tällä hetkellä aktiiviset projektisi
komennolla:

```text
csc-projects
```

Tämä komento näyttää tiedot kaikista CSC-projekteistasi. Voit valita vain
yhden projektin raportoitavaksi `-p`-optiolla. Esimerkiksi:

```bash
[kkayttaj@puhti-login11 ~]$ csc-projects -p project_2012345
-----------------------------------------------------------------
Project: project_2012345        Owner: Kalle Käyttäjä
Title: "Ortotopology modeling"
Start: 2019-08-20 End: 2029-10-23 Status: open
Billing units      Budget        Used      Remain
-------------      ------        ----      ------
CPU BU:             60000          20       59980
GPU BU:              1000          30         970
Storage BU:        300000          40      299960
Cloud BU:             400          10         390
Latest resource grant: 2025-01-31
-----------------------------------------------------------------
Project info updated: 2025-09-02 15:12
```

Komento raportoi projektin omistajan, otsikon sekä alku- ja loppupäivämäärät.
Lisäksi komento tulostaa projektin budjetointitiedot: kuinka monta Billing
Unitia kutakin tyyppiä projektille on myönnetty, kuinka paljon on käytetty ja
kuinka paljon on jäljellä.

Projektiesi [levyalueet](disk.md) voi tarkistaa komennolla:

```text
csc-workspaces
```

## Puhtin ja Mahtin käyttö { #using-puhti-and-mahti }

* [Järjestelmät](available-systems.md): Mitä laskentaresursseja on saatavilla
* [Käyttösäännöt](usage-policy.md): CSC:n supertietokoneiden käyttösäännöt
* [Yhteyden muodostaminen](connecting/index.md): Kuinka muodostaa yhteys CSC:n supertietokoneille
* [Puhtin verkkokäyttöliittymä](webinterface/index.md): Kuinka käyttää Puhtia verkon
  kautta
* [Levyalueet](disk.md): Missä CSC:n supertietokoneilla voi tallentaa dataa
* [Moduulit](modules.md): Kuinka löytää tarvitsemiasi ohjelmia
* [Sovellukset](../apps/index.md): Sovelluskohtaiset ohjeet.
* [Ajojen suorittaminen](running/getting-started.md): Kuinka ajaa ohjelmia
  supertietokoneilla
* Sovellusten asentaminen ja kääntäminen:
    * [Ohjelmiston asentaminen](installing.md)
    * [Kääntäminen Puhtissa](compiling-puhti.md)
    * [Kääntäminen Mahtissa](compiling-mahti.md)
* [Sovellusten vianetsintä](debugging.md): Kuinka etsiä vikoja sovelluksistasi
* [Suorituskyvyn analysointi](performance.md): Kuinka ymmärtää sovellustesi
  suorituskykyä