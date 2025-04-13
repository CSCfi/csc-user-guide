
---
tags:
  - Free
system:
  - www-puhti
---

# Zonation

[Zonation](https://zonationteam.github.io/Zonation5/) on paikkatietoihin perustuva suojelusuunnittelun priorisointimenetelmä laajamittaiselle suojelusuunnittelulle. Se tunnistaa alueet tai maisemat, jotka ovat tärkeitä korkean elinympäristölaadun ja monimuotoisuuspiirteiden (esim. lajien) välisen yhteyden säilyttämiselle, ja tarjoaa määrällisen menetelmän lajien pitkäaikaisen säilymisen parantamiseksi.

## Saatavilla

__Zonation__ on saatavilla Puhtissa seuraavilla versioilla:

* 5.2.1 (sisältää graafisen käyttöliittymän)
* 5.2.0.2 (sisältää graafisen käyttöliittymän)
* 5.1.0 (sisältää graafisen käyttöliittymän)

## Käyttö

Zonation on käytettävissä __zonation__-moduulissa:

```
module load zonation
z5 <komentojen argumentit>
```

Versiolla 5.2.1 voit myös käyttää `zonation5 <komentojen argumentit>`

Zonationia voi käyttää Puhtissa komentorivin tai graafisen käyttöliittymän kanssa, interaktiivisena tehtävänä tai eräajojärjestelmän kanssa. Varaa joka tapauksessa sopiva määrä laskentaresursseja: ytimiä ja muisti. Zonation 5 toimii nopeammin, jos se voi käyttää useita ytimiä. Puhtissa se voi käyttää yhtä nodia, mikä on maksimissaan 40 ydintä.

Ennen Zonationin aloittamista siirrä datasi projektisi __scratch__-kansioon. Testaukseen voit käyttää [zonation5-tutorial data](https://github.com/zonationteam/Zonation5/releases/download/v1.0/manual_and_example_setups.zip).

### Zonation graafisella käyttöliittymällä

Zonationin graafisen käyttöliittymän (GUI) voi käynnistää Puhtin web-käyttöliittymässä:

1. Kirjaudu sisään [Puhtin web-käyttöliittymään](https://puhti.csc.fi).
2. Avaa [Desktop-sovellus](../computing/webinterface/desktop.md)
3. Tietokoneen avauksen jälkeen kaksoisnapsauta Zonation-kuvaketta.

### Työskentely Zonationin kanssa interaktiivisesti

Suhteellisen lyhyille analyysitöille Zonationia voi käyttää [interaktiivisessa istunnossa](../computing/running/interactive-usage.md).

```
sinteractive -i
cd /scratch/project_200xxxx/<sijainti_datalle>
z5 -w --mode=ABF minimal_settings.z5 /scratch/project_200xxxx/example1_out
```

### Zonationin käyttö eräajolla

Pidemmille analyysitöille Puhtin eräajojärjestelmän käyttö on suositeltavaa.

```
#!/bin/bash
#SBATCH --account=project_200xxxx
#SBATCH --cpus-per-task=40
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --mem=4G

module load zonation
cd /scratch/project_200xxxx/<sijainti_datalle>
srun z5 -w --mode=ABF minimal_settings.z5 /scratch/project_200xxxx/example1_out
```

## Lisenssi

Zonation 5 on jaettu täsmälleen tällaisena, vapaasti [GNU General Public License (GPL) version 3 (#GNUGPL) (#GNUGPLv3) lisenssillä.](https://www.gnu.org/licenses/gpl-3.0.html)

## Viittaaminen

`Moilanen, A., Lehtinen, P., Kohonen, I., Virtanen, E., Jalkanen, J. ja Kujala, H. 2022. Uudet menetelmät paikkatietopriorisointiin sovellettuna suojeluun, maankäytön suunnitteluun ja ekologisiin vaikutuksiin perustuviin väistöihin. Methods in Ecology and Evolution`

## Tunnustukset

Ole hyvä ja mainitse CSC ja Geoportti julkaisuissasi, se on tärkeää projektin jatkumiselle ja rahoitusraporteille. Esimerkiksi voit kirjoittaa "Kirjoittajat haluavat kiittää CSC - Tieteen tietotekniikan keskus, Suomi (urn:nbn:fi:research-infras-2016072531) ja avoin geoinformaatioinfrastruktuuri tutkimukselle (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta".

## Asennus

Zonation asennettiin Puhtiin Apptainerilla käyttäen [Zonation Apptainer määritelmätiedostoja](https://github.com/CSCfi/singularity-recipes/tree/main/zonation), jotka on kirjoittanut Pauli Lehtinen Helsingin yliopistosta pienillä muokkauksilla.

Kontti käärittiin lopulta [Tykky's wrap-container toiminnolla](../computing/containers/tykky.md#container-based-installations): 
`wrap-container -w /squashfs-root/AppRun --prefix install_dir zonation5_v2.1.sif`

Symbolisia linkkejä lisättiin `z5` ja `zonation5` toimimaan aloituskomentoina.

## Viitteet

* [Zonation kotisivu](https://zonationteam.github.io/Zonation5/)
* [Zonation Github](https://github.com/zonationteam/Zonation5)
* [Zonation 5 ohjekirja ja tutoriaali data](https://github.com/zonationteam/Zonation5/releases/download/v1.0/manual_and_example_setups.zip)

