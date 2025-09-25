---
tags:
  - Free
catalog:
  name: SNAP
  description: for remote sensing applications
  description_fi: kaukokartoitussovelluksiin
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - web_interfaces:
        - Puhti
    - Puhti
---

# SNAP { #snap }

[SNAP](https://step.esa.int/main/toolboxes/snap/) (Sentinel Application Platform) on Euroopan avaruusjärjestön kehittämä kaukokartoituksen työkalupakkiarkkitehtuuri. Se sisältää työkalut kaikille yleisille satelliittialustoille.

## Available { #available }

__SNAP__ on käytettävissä Puhtissa seuraavina versioina:

* 9.0 (paketoitu Singularity-kontti, jossa Python 3.6.9 sekä snappy ja snapista)
* 8.0 (Singularity-kontti, jossa snappy 8.0.3 ja Python 3.6.9)

Lisäksi tarjoamme moduulin `snap/jupyter`, jossa on SNAP 9.0 (paketoitu Singularity-kontti, jossa Python 3.6.9 sekä snappy ja snapista) ja Jupyter asennettuna. Voit esimerkiksi käyttää sitä Puhtin verkkokäyttöliittymän Jupyter-sovelluksessa valitsemalla **custom module** -valinnan.

### Installed toolboxes { #installed-toolboxes }

* Sentinel-työkalupaketit (1,2,3) 
* SMOS-työkalupaketti 
* Radarsat-työkalupaketti 
* PROBA-V-työkalupaketti

Voit asentaa lisää liitännäisiä omaan käyttäjähakemistoosi SNAPin graafisesta käyttöliittymästä.

## Usage { #usage }

SNAP sisältyy __snap__-moduuliin ja se voidaan ladata komennolla:

`module load snap`

Tämä lataa uusimman saatavilla olevan version. Vanhemman version voit ladata komennolla:

`module load snap/<VERSION>`

### Using SNAP with Graphical User Interface (GUI) in Puhti web interface { #using-snap-with-graphical-user-interface-gui-in-puhti-web-interface }

Helpoin tapa käyttää SNAPia on avata se Puhtin verkkokäyttöliittymässä.

1. Kirjaudu [Puhtin verkkokäyttöliittymään](https://puhti.csc.fi).
2. Avaa [Desktop-sovellus](../computing/webinterface/desktop.md). 
3. Kun Desktop on käynnistynyt, kaksoisnapsauta SNAP-kuvaketta TAI avaa `Terminal` (Desktop-kuvake) ja käynnistä SNAP:

```
module load snap
source snap_add_userdir $TMPDIR
snap -J-xmx10G
```

#### SNAP userdir and Java temp dir configuration { #snap-userdir-and-java-temp-dir-configuration }

SNAP käyttää runsaasti levytilaa välimuistille ja väliaikaistiedostoille. Oletuksena nämä kirjoitetaan HOME-hakemistoosi ja HOME voi täyttyä helposti. Tämän välttämiseksi määritä [snap-käyttäjähakemisto](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/15269950/SNAP+Configuration) ja Javan väliaikaishakemisto. Aja tämä skripti aina kun alat käyttää SNAPia Puhtissa tai haluat muuttaa käytettäviä hakemistoja. 

Ladattuasi snap-moduulin suorita

`source snap_add_userdir <YOUR-PROJECTS-SCRATCH-FOLDER>`

Voit myös pyytää nopean [nvme](../computing/running/creating-job-scripts-puhti.md#local-storage) -levyn eräajoon ja suorittaa komennon ensin eräajossa, jolloin kaikki väliaikais-/välimuistitiedostot kirjoitetaan nopealle levylle scratchin sijaan. Tämä voi nopeuttaa vaativia laskentoja.

`source snap_add_userdir $LOCAL_SCRATCH` erätöissä

`source snap_add_userdir $TMPDIR` interaktiivisissa töissä

Tämä skripti asettaa myös Javan väliaikaishakemiston; se asetetaan määrittämääsi hakemistoon alihakemistoksi snap/temp. Jos haluat asettaa Javan väliaikaishakemiston johonkin muualle, käytä:
`export _JAVA_OPTIONS="$_JAVA_OPTIONS -Djava.io.tmpdir=<SOME-FOLDER>"` käyttäjähakemiston asettamisen jälkeen.

!!! note
        Graafinen käyttöliittymä ei noudata snap.userdir-asetusta, mutta huomioi Java-asetuksen. SNAPin graafisen käyttöliittymän käyttäminen luo __.snap__-kansion HOME-hakemistosi sisään ja täyttää sitä. Tyhjennä se, jos HOME-hakemistosi tila loppuu.

#### Java memory settings { #java-memory-settings }

__Oletuksena SNAP/8.0 Puhtissa käyttää enintään 2 Gt muistia Javalle.__ Voit kasvattaa tätä lisäämällä `-J-xmx10G` tai vastaavan asetuksen `snap`- tai `gpt`-komentoon. `-J-xmx10G` kasvattaa Javan enimmäismuistin 10 Gt:hen. Säädä tätä tarpeesi ja työn muistivarauksen mukaan. Varaa Javalle muutama gigatavu vähemmän kuin työn muistivaraus.

### Using SNAP with Graph Processing Tool (gpt) command { #using-snap-with-graph-processing-tool-gpt-command }

Graph Processing Tool `gpt` on komentorivityökalu massaprosessointiin. GPT:tä käyttämällä voidaan hyödyntää enemmän laskentatehoa kuin SNAPin graafisella käyttöliittymällä, koska sitä voidaan käyttää skripteissä ja siten sisällyttää töihin, jotka voidaan lähettää mihin tahansa [Puhti-osioon](../computing/running/batch-job-partitions.md).

GPT-komento näyttää usein tältä:

```
gpt -J-xmx10G <full_path_to_graph_xml_file> -Pfile=<inputfile> -t <outputfile>
```

Joidenkin keskeisten __gpt__-valintojen selitykset:

* __-J-xmx10G__    Javan käyttämä enimmäismuisti.
* __-q__    Säikeiden lukumäärä, jota gpt-instanssi käyttää. Aseta se pyydettyjen CPU-ytimien määrään tai suuremmaksi
* __-c__    Välimuistin koko tavuina. Muuta tätä, jos levytilasta tulee ongelma
* __-x__    Tyhjennä sisäinen ruutuvälimuisti sen jälkeen, kun yksi rivi ruutuja on kirjoitettu ulostulotiedostoon. Lisää tämä, jos muistista tulee ongelma

Lisätietoja GPT:stä löytyy tämän sivun lopussa olevien viitteiden linkeistä.

Myös seuraava komento on erittäin hyödyllinen eri operaattoreiden graafien luomiseen. Sen voi suorittaa interaktiivisessa sessiossa
```
sinteractive -i
module load snap
gpt <snap-operator> -h
```

`gpt --diag -J-Xmx60G -c 40G` näyttää, mitä muisti- ja välimuistiasetuksia `gpt` käyttää.

#### GPT examples for Puhti { #gpt-examples-for-puhti }

* [Täydet esimerkit GPT:n ajamisesta Puhtissa GitHubissa](https://github.com/csc-training/geocomputing/tree/master/snap). Esimerkit sisältävät sekä yksinkertaisen työn yhdellä GPT-grafilla että [taulukkoajon](../computing/running/array-jobs.md), jossa sama graafi lasketaan useille syötekuville.

### Using SNAP with the Python interfaces { #using-snap-with-the-python-interfaces }

SNAPin toimintoihin on mahdollista päästä käsiksi myös Pythonista __snappy__- ja __snapista__-kirjastoilla (vain SNAP 9).

__SNAP 9.0__

snappy/snapista-skriptien ajaminen erätöissä:
```
python3 <YOUR-PYTHON-SCRIPT>
```

Saatavilla olevat paketit:
```
pip3 list
```

Uusien pakettien asentaminen `$HOME`-hakemistoosi:

```
pip <NEW-PACKAGE-NAME> --user
```

Paketteja on mahdollista asentaa myös muihin hakemistoihin kuin `$HOME`.
Katso ohjeet sivulta
[Python usage guide](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).

__SNAP 8.0__

snappy-skriptien ajaminen erätöissä:
```
apptainer_wrapper exec python3 <YOUR-PYTHON-SCRIPT>
```

Saatavilla olevat paketit:
```
apptainer_wrapper exec pip list
```

Uusien pakettien asentaminen `$HOME`-hakemistoosi:

```
apptainer_wrapper exec pip <NEW-PACKAGE-NAME> --user
```

Paketteja on mahdollista asentaa myös muihin hakemistoihin kuin `$HOME`.
Katso ohjeet sivulta
[Python usage guide](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).

## Updating SNAP { #updating-snap }

SNAPin pienet päivitykset ja moduulipäivitykset tallennetaan hakemistoon `$HOME/.snap`. Tämä tarkoittaa, että kaikki pienet päivitykset käyttäjän on asennettava itse. Voit tehdä tämän joko SNAP Desktopissa noudattamalla käynnistyksen yhteydessä näkyvässä ponnahdusikkunassa annettuja ohjeita tai SNAP 9:ssä suorittamalla `source update_snap` sen jälkeen, kun olet ladannut SNAP-moduulin terminaalissa.

## License { #license }

Kaikki SNAP-ohjelmistot julkaistaan [GPL-3](https://www.gnu.org/licenses/gpl.html)-lisenssillä.

## Citation { #citation }

```SNAP - ESA Sentinel Application Platform v{VERSION}, http://step.esa.int```



##  Acknowledgement { #acknowledgement }

Ole hyvä ja mainitse CSC ja Geoportti julkaisuissasi; se on tärkeää projektien jatkuvuuden ja rahoitusraportoinnin kannalta.
Esimerkiksi voit kirjoittaa: "Kirjoittajat kiittävät CSC:tä – Tieteen tietotekniikan keskusta (urn:nbn:fi:research-infras-2016072531) ja tutkimuksen paikkatiedon infrastruktuuria Geoporttia (urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta."

## Installation { #installation }

SNAP asennettiin Puhtiin Singularitylla käyttäen [mundialiksen tarjoamaa SNAP Docker -imagea Dockerhubissa](https://hub.docker.com/r/mundialis/esa-snap) ja pieniä lisäyksiä snappy- ja snapista-Python-rajapintojen tarjoamiseksi. Kontti lopuksi paketoitiin [Tykky-työkalun wrap-container-toiminnolla](../computing/containers/tykky.md#container-based-installations): 

`wrap-container -w /usr/local/snap/bin,/usr/bin snap9_py.sif --prefix install_dir`

Täysi [SNAPin Singularity-määrittelytiedosto](https://raw.githubusercontent.com/CSCfi/singularity-recipes/main/snap/snap_py.def). 

## References { #references }

* [SNAPin kotisivu](http://step.esa.int/main/toolboxes/snap/)
* [SNAP CSC -esimerkki](https://github.com/csc-training/geocomputing/tree/master/snap)
* [SNAP komentoriviohje (GPT)](http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf)
* [SNAP-wiki](https://senbox.atlassian.net/wiki/spaces/SNAP/overview)
* [SNAP-oppaat](http://step.esa.int/main/doc/tutorials/)
* [snappy Python -esimerkkejä](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python)
* [GPF-graafin luominen](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/70503590/Creating+a+GPF+Graph)
* [Massaprosessointi GPT-komennolla](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/70503475/Bulk+Processing+with+GPT)