
---
tags:
  - Free
system:
  - www-puhti
---

# SNAP

[SNAP](https://step.esa.int/main/toolboxes/snap/) (Sentinel Application Platform) on Euroopan avaruusjärjestön kehittämä kaukokartoituksen työkalupakkiarkkitehtuuri. Se sisältää työkaluja kaikille yleisille satelliittialustoille.

## Saatavilla {#available}

__SNAP__ on saatavilla Puhtiissa seuraavilla versioilla:

* 9.0 (wrapped singularity -konteineri Python 3.6.9:llä sisältäen snappy ja snapista)
* 8.0 (Singularity -konteineri snappy 8.0.3:lla ja Python 3.6.9:llä)

Lisäksi tarjoamme moduulin `snap/jupyter`, jossa on SNAP 9.0 (wrapped singularity -konteineri Python 3.6.9:llä sisältäen snappy ja snapista) ja jupyter asennettuna. Voit esimerkiksi käyttää sitä Jupyter-sovelluksessa Puhti:n web-käyttöliittymän kautta **custom module** -vaihtoehdon avulla.

### Asennetut työkalupakit {#installed-toolboxes}

* Sentinel-työkalupakit (1,2,3) 
* SMOS-työkalupakki 
* Radarsat-työkalupakki 
* PROBA-V-työkalupakki

Voit asentaa lisää lisäosia omaan käyttäjähakemistoosi SNAP:n graafisesta käyttöliittymästä.

## Käyttö {#usage}

SNAP sisältyy __snap__-moduuliin ja sen voi ladata komennolla:

`module load snap`

Tämä lataa uusimman saatavilla olevan version. Voit ladata vanhemman version komennolla:

`module load snap/<VERSION>`

### SNAP:n käyttäminen graafisella käyttöliittymällä (GUI) Puhti:n web-käyttöliittymässä {#using-snap-with-graphical-user-interface-gui-in-puhti-web-interface}

Helpoin tapa käyttää SNAP:ia on avata se Puhti:n web-käyttöliittymässä.

1. Kirjaudu [Puhti:n web-käyttöliittymään](https://puhti.csc.fi).
2. Avaa [Desktop-sovellus](../computing/webinterface/desktop.md). 
3. Työpöydän käynnistämisen jälkeen kaksoisnapsauta SNAP-kuvaketta TAI avaa `Terminal` (työpöytäkuvake) ja käynnistä SNAP:

```
module load snap
source snap_add_userdir $TMPDIR
snap -J-xmx10G
```

#### SNAP userdir ja Java-temp-hakemiston määritykset {#snap-userdir-and-java-temp-dir-configuration}

SNAP käyttää merkittävästi tallennustilaa välimuistille ja tilapäistiedostoille. Oletusarvoisesti nämä kirjoitetaan HOME-hakemistoosi, ja ne voivat helposti täyttää sen. Vältäksesi tämän, määritä [snap-käyttäjähakemisto](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/15269950/SNAP+Configuration) ja Java-väliaikainen kansio. Sinun tulee ajaa tämä skripti joka kerta, kun alat käyttää SNAP:ia Puhti:ssa tai haluat muuttaa käytettäviä kansioita.

Lataa snap-moduuli ja suorita:

`source snap_add_userdir <YOUR-PROJECTS-SCRATCH-FOLDER>`

Voit myös pyytää nopeaa [nvme](../computing/running/creating-job-scripts-puhti.md#local-storage) levyä eräajossa ja suorittaa ensin käskyn eräajossa, jolloin kaikki tilapäis-/välimuistotiedostot kirjoitetaan nopealle levylle raapaisualueen sijaan. Tämä voi parantaa nopeutta vaativissa laskelmissa.

`source snap_add_userdir $LOCAL_SCRATCH` eräajoissa

`source snap_add_userdir $TMPDIR` interaktiivisissa ajoissa

Tämä skripti asettaa myös Java-väliaikaisen kansion, joka asetetaan olemaan snap/temp-alikansiossa määrittelemässäsi kansiossa. Jos haluat asettaa Java-väliaikaisen kansion jonnekin muualle, käytä:
`export _JAVA_OPTIONS="$_JAVA_OPTIONS -Djava.io.tmpdir=<SOME-FOLDER>"` käyttäjähakemiston määrityksen jälkeen.

!!! huom
        Graafinen käyttöliittymä ei seuraa snap.userdir-asetusta, mutta huomioi Java-asetuksen. SNAP GUI luo __.snap__ -kansion HOME-hakemistosi sisälle ja täyttää sen. Tyhjennä se, jos tilasi loppuu HOME-hakemistossasi.

#### Java-muistiasetukset {#java-memory-settings}

__Oletusarvoisesti SNAP/8.0 Puhtissa käyttää vain enintään 2 Gt muistia Java:lle.__ Lisää tätä, lisäämällä `-J-xmx10G` tai vastaava asetus `snap`- tai `gpt`-käskyyn. `-J-xmx10G` laajentaa Java:n maksimi muistin 10 Gt:iin. Säädä tämä tarpeidesi mukaan ja työn muistin varauksen mukaan. Työn muistin varaukseen verrattuna käytä Java:lle muutama Gt vähemmän.

### SNAP:n käyttäminen Graph Processing Tool (gpt) komennolla {#using-snap-with-graph-processing-tool-gpt-command}

Graph Processing Tool `gpt` on komentorivityökalu, jota käytetään eräprosessointiin. GPT:n avulla voidaan käyttää enemmän laskentatehoa kuin SNAP:n graafisessa käyttöliittymässä, koska sitä voidaan käyttää skripteissä ja siten sisällyttää töihin, jotka voidaan lähettää mille tahansa [Puhti-osastolle](../computing/running/batch-job-partitions.md).

GPT-komento näyttää usein tältä:

```
gpt -J-xmx10G <full_path_to_graph_xml_file> -Pfile=<inputfile> -t <outputfile>
```

Joihinkin merkittäviin __gpt__-asetuksiin kuuluu:

* __-J-xmx10G__    maksimi muisti, joka Java käyttää.
* __-q__    Kierteiden lukumäärä, jota GPT-instanssi käyttää. Aseta se pyydettyjen CPU-ydinten määräksi tai suuremmaksi
* __-c__    Välimuistitilan koko tavuina. Muuta tätä, jos tallennustilasta tulee ongelma
* __-x__    Tyhjennä sisäinen laatikkovälimuisti täydellisen laattarivin kirjoittamisen jälkeen tulostiedostoon. Lisää tämä, jos muistista tulee ongelma

Katso lisätietoja GPT:stä alla olevista viitteistä.

Myös seuraava komento on erittäin hyödyllinen luomaan graafeja eri operaattoreille. Se voidaan suorittaa interaktiivisessa istunnossa
```
sinteractive -i
module load snap
gpt <snap-operator> -h
```

`gpt --diag -J-Xmx60G -c 40G` voidaan käyttää näkemään, mitä muisti- ja välimuistiasetuksia `gpt` käyttää.

#### GPT-esimerkkejä Puhtille {#gpt-examples-for-puhti}

* [Täydelliset esimerkit GPT:n käytöstä Puhtilla GitHubissa](https://github.com/csc-training/geocomputing/tree/master/snap). Esimerkit sisältävät sekä yksinkertaisen työn yhden GPT-graafin kanssa että [tekijöitä-jobs](../computing/running/array-jobs.md), joissa samaa graafia lasketaan useille syötekuville.

### SNAP:n käyttäminen Python-rajapintojen kanssa {#using-snap-with-the-python-interfaces}

SNAP-toimintoihin on myös mahdollista päästä Pythonista __snappy__- ja __snapista__-kirjastoilla (vain SNAP 9).

__SNAP 9.0__

suoritetaan snappy/snapista skriptejä eräajoilla:
```
python3 <YOUR-PYTHON-SCRIPT>
```

Katso käytettävissä olevat paketit:
```
pip3 list
```

Uusien pakettien asentaminen `$HOME`-hakemistoon:

```
pip <NEW-PACKAGE-NAME> --user
```

On myös mahdollista asentaa paketteja muihin hakemistoihin kuin `$HOME`.
Katso ohjeet oppaastamme
[Python-käyttöohje](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).

__SNAP 8.0__

Suoritetaan snappy-skriptejä eräajoilla:
```
apptainer_wrapper exec python3 <YOUR-PYTHON-SCRIPT>
```

Katso käytettävissä olevat paketit:
```
apptainer_wrapper exec pip list
```

Uusien pakettien asentaminen `$HOME`-hakemistoon:

```
apptainer_wrapper exec pip <NEW-PACKAGE-NAME> --user
```

On myös mahdollista asentaa paketteja muihin hakemistoihin kuin `$HOME`.
Katso ohjeet oppaastamme
[Python-käyttöohje](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).

## Päivittäminen SNAP:iin {#updating-snap}

SNAP -pienempiä ja moduulipäivityksiä säilytetään kansiossa `$HOME/.snap`. Tämä tarkoittaa, että kaikki pienemmät päivitykset on asennettava käyttäjän toimesta. Voit joko tehdä tämän SNAP:n työpöytäohjelmassa seuraamalla käynnistyessä annettuja ohjeita tai SNAP 9:lle suorittamalla `source update_snap` SNAP-moduulin lataamisen jälkeen terminaalista.

## Lisenssi {#license}

Kaikki SNAP-ohjelmisto on julkaistu [GPL-3](https://www.gnu.org/licenses/gpl.html) lisenssillä.

## Viittaus {#citation}

```SNAP - ESA Sentinel Application Platform v{VERSION}, http://step.esa.int```



## Tunnustus {#acknowledgement}

Ole hyvä ja huomioi CSC ja Geoportti julkaisuissasi, sillä se on tärkeää projektin jatkumisen ja rahoitusraporttien kannalta.
Esimerkkinä voit kirjoittaa "Kirjoittajat haluavat kiittää CSC - Tieteen tietotekniikan keskusta, Suomi (urn:nbn:fi:research-infras-2016072531) ja Avoimen paikkatiedon tutkimusinfrastruktuuria (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta".


## Asennus {#installation}

SNAP asennettiin Puhti:lle käyttöön Singularity:n avulla käyttäen [SNAP Docker -kuvaa, jonka tarjoaa mundialis Dockerhubissa](https://hub.docker.com/r/mundialis/esa-snap) joidenkin pienten lisäysten kanssa, jotta snappy ja snapista Python-rajapinnat olisivat käytettävissä. Konteineri käärittiin lopulta [Tykky:n wrap-container-toiminnallisuuden](../computing/containers/tykky.md#container-based-installations) avulla: 

`wrap-container -w /usr/local/snap/bin,/usr/bin snap9_py.sif --prefix install_dir`

Täysimittainen [SNAP Singularity -määrittelytiedosto](https://raw.githubusercontent.com/CSCfi/singularity-recipes/main/snap/snap_py.def). 


## Viitteet {#references}

* [SNAP-etusivu](http://step.esa.int/main/toolboxes/snap/)
* [SNAP CSC -esimerkki](https://github.com/csc-training/geocomputing/tree/master/snap)
* [SNAP-komentorivikurssi (GPT)](http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf)
* [SNAP-wiki](https://senbox.atlassian.net/wiki/spaces/SNAP/overview)
* [SNAP-oppaat](http://step.esa.int/main/doc/tutorials/)
* [snappy Python -esimerkit](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python)
* [GPF-graafin luominen](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/70503590/Creating+a+GPF+Graph)
* [Massaprosessointi GPT-komennolla](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/70503475/Bulk+Processing+with+GPT)
```

