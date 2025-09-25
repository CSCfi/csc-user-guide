---
tags:
  - Free
catalog:
  name: ParaView
  description: Free open-source visualization application
  description_fi: Ilmainen avoimen lähdekoodin visualisointisovellus
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - web_interfaces:
        - LUMI
        - Puhti
    - LUMI
    - Puhti
    - Mahti
---

# ParaView { #paraview }

ParaView on avoimen lähdekoodin, tehokas ohjelmisto tieteelliseen visualisointiin. Taustalla se käyttää VTK-kirjastoa Python-sidoksilla. Suosittelemme [HPC-verkkokäyttöliittymän etätyöpöytiä](../computing/webinterface/desktop.md) interaktiiviseen käyttöön.

!!! info "ParaViewin ajaminen GPU-kiihdytetyllä grafiikalla Puhtilla ja LUMIlla"
    Voit nyt ottaa käyttöön myös [interaktiivisen visualisoinnin GPU-kiihdytyksellä](../computing/webinterface/accelerated-visualization.md) paremman suorituskyvyn saavuttamiseksi. Valitse tässä tapauksessa Puhtin verkkokäyttöliittymässä _Accelerated visualization_ vaihtoehdon _Desktop_ sijaan. LUMIlla valitse _Desktop_-sovellus ja `lumid`-osio ([lisätietoja](https://docs.lumi-supercomputer.eu/runjobs/webui/desktop/)).

ParaView on suunniteltu ajamaan rinnakkaistehtäviä ja koostuu yhdestä asiakkaasta ja yhdestä tai useammasta palvelimesta (pvserver). ParaView’ta voi ajaa monella tavalla eri tarpeisiin.

## License { #license }

ParaView käyttää [sallivaa BSD-lisenssiä](https://www.paraview.org/paraview-license/), joka mahdollistaa mahdollisimman laajan käytön, mukaan lukien kaupalliset organisaatiot, rojaltivapaasti useimpiin tarkoituksiin.

## Available { #available }

* Puhti: 5.10.1
* Mahti: 5.10.1
* LUMI: 5.8.0

## Usage { #usage }

### Standalone mode { #standalone-mode }

Yksinkertaisin tapa käyttää ParaView’ta on ajaa se itsenäisessä tilassa (standalone). Tämä tila riittää perusvisualisointiin ja on hyvä lähtökohta myös monimutkaisempiin tehtäviin.

Itsenäisessä tilassa ParaView ei tarvitse pvserver-varausta. **Huomaa, että ParaView’ta ei pidä ajaa kirjautumissolmulla.** Voit käyttää komentoa `sinteractive -i` varataksesi yhden suorittimen ja enintään 16 Gt muistia interaktiiviselle istunnolle. Kun resurssit vapautuvat, istunto ohjataan laskentasolmulle. Lataa moduuli ja käynnistä ParaView:

```bash
module purge
module load paraview/5.10.1-paraview
paraview
```

Jos tarvitset enemmän resursseja, käytä `srun`-komentoa ja anna istunnon parametrit yhtenä rivinä. Seuraava varaa yhden suorittimen käyttöön 32 Gt muistia yhdeksi tunniksi:

```bash
srun --partition=small --time=01:00:00 --mem=32G --account=<project> --x11=first --pty bash
```

Kun sinut on ohjattu laskentasolmulle, lataa moduuli ja käynnistä ParaView kuten yllä olevassa esimerkissä.

Jos mallissasi on monimutkaista geometriaa, vuorovaikutus hidastuu ja näytön päivityksissä näkyy viivettä. ParaView’ssa on valintaruutu OSPRay-renderöijän käyttöön nopeampia näytön päivityksiä varten. Huomaa, että vaihtaminen oletus- ja OSPRay-renderöintitilojen välillä voi olla hidasta. Vaikka käyttäisit vain yhtä suoritinta, OSPRay-renderöinti on paljon nopeampaa.

OSPRay osaa käyttää useampaa suoritinta säikeinä ruudunpäivitysten nopeuttamiseksi. Säikeet varataan optiolla `--cpus-per-task`. Seuraava esimerkki varaa renderöintiä varten 5 säiettä ja käyttää yhteensä 32 Gt muistia jaettuna suorittimien kesken. Huomaa, että useimmat muut ParaView’n toiminnot eivät ole säikeistettyjä, joten ne käyttävät edelleen vain yhtä suoritinta.

```bash
srun --ntasks=1 --cpus-per-task=5 --partition=small --time=01:00:00 --mem=32G --account=<project> --x11=first --pty bash
```

Kuten aiemmin, kun sinut on ohjattu laskentasolmulle, lataa moduuli ja käynnistä ParaView.  

### Parallel mode - client using several servers (pvservers) and threads { #parallel-mode-client-using-several-servers-pvservers-and-threads }

Vaativissa töissä ParaView voidaan ajaa rinnakkaistilassa: yksi asiakas ja useita pvserver-palvelimia, kukin omalla suorittimellaan. Asiakas yhdistää yhteen pvserveriin, joka kommunikoi muiden pvservereiden kanssa.  

Huomaa, että jos suurin osa työstä tehdään vain yhdellä pvserverillä, rinnakkaisasetuksen käyttö voi itse asiassa hidastaa ParaView’ta, koska datan jakaminen eri suorittimien välillä vie aikaa. Voit tarkistaa, kuinka paljon kukin pvserver on käytössä, avaamalla ParaView’ssa ikkunan *Memory Inspector* (valikosta: *View/Memory Inspector*). ParaView’n *D3*-suodatinta voi käyttää työn tasaisempaan jakamiseen ytimien välillä.  

Alla oleva esimerkkiskripti `para5101-multi.sh` käynnistää useita pvservereitä ja yhden asiakkaan (etuosan) ja yhdistää ne. Kopioinnin jälkeen varmista, että skriptillä on tarvittavat suoritusoikeudet – myönnä ne komennolla `chmod u+x`. Skripti ei vaadi muokkausta. Resurssit tulisi varata `salloc`-komennolla. Varaus kattaa sekä asiakkaan että pvserverit. `--ntasks` on pvservereiden määrä plus yksi asiakas, ja `--cpus-per-task` on kullekin näistä tehtävistä varattujen säikeiden määrä, joten varattujen suorittimien kokonaismäärä on `--ntasks` * `cpus-per-task`. `--mem` on kaikkien yhteiskäyttöinen muistimäärä. Skripti varaa asiakkaalle yhden gigatavun muistia, ja loput jaetaan pvservereiden kesken.

Alla oleva `salloc`-esimerkki varaa resurssit yhdelle asiakkaalle ja yhdeksälle pvserverille, kullekin kaksi säiettä, joten yhteensä varataan 20 suorittinta. Pvservereille varataan yhteensä yhdeksän gigatavua muistia ja asiakkaalle yksi gigatavu. ParaView’n OSPRay-renderöijä hyödyntää säikeitä, kun taas useimmat muut ParaView’n toiminnot hyötyvät enemmän pvservereistä. **Huomaa, että kaikki nämä `salloc`-parametrit on annettava eksplisiittisesti,** muuten skripti `para581-multi.sh` ei toimi.  

```bash
salloc --nodes=1 --ntasks=10 --cpus-per-task=2 --mem=10G --time=01:00:00 --partition=small --account=<project> para5101-multi.sh
```

Kun asiakas yhdistää palvelimiin, saatat nähdä muutamia varoituksia (*connect failed, retrying*), jotka voi ohittaa. Jos viimeinen viesti kuitenkin oli *Creating default builtin connection*, yhteys lopulta epäonnistui ja asiakas toimii ilman pvservereitä. Jos näin käy, tarkista, että olet sisällyttänyt kaikki tarvittavat työparametrit `salloc`-komentoosi.  

#### Example script { #example-script }

```bash title="para5101-multi.sh"
#!/bin/bash 
######################################################
### This script starts paraview servers and client ###
### and connects them using a unique random port.  ###
### Run the script via salloc. All job parameters  ###
### are copied from the salloc command, no editing ###
### of this script is needed.                      ###
######################################################
export SLURM_EXACT=1
export XDG_RUNTIME_DIR=$HOME
export KNOB_MAX_WORKER_THREADS=$SLURM_CPUS_PER_TASK
export LP_NUM_THREADS=$SLURM_CPUS_PER_TASK
MACHINEFILE="nodes.${SLURM_JOB_ID}"
scontrol show hostnames ${SLURM_JOB_NODELIST} > $MACHINEFILE
FIRSTNODE=$(head -n 1 ${MACHINEFILE})
MYPORT=`comm -23 <(seq 22200 22299 | sort) <(ss -Htan | awk '{print $4}' | cut -d':' -f2 | sort -u) | shuf | head -n 1`
SERVER_NTASKS=$(( ${SLURM_NTASKS}-1 ))
SERVER_MEMORY=$(( ${SLURM_MEM_PER_NODE}-1000 ))
module purge
module load paraview/5.10.1-pvserverosmesa
srun --nodes=1 --ntasks=$SERVER_NTASKS --cpus-per-task=$SLURM_CPUS_PER_TASK --mem=$SERVER_MEMORY pvserver --server-port=$MYPORT &
srun --nodes=1 --ntasks=1 --cpus-per-task=$SLURM_CPUS_PER_TASK --mem=1000 --x11=first /appl/opt/vis/paraview/paraview-5.10.1-mesa-client/bin/paraview --server-url=cs://$FIRSTNODE.bullx:$MYPORT &
wait
```

## More Information { #more-information }

* [ParaViewin kotisivu](http://www.paraview.org/)
* [ParaView’n dokumentaatio ja opas](http://www.paraview.org/documentation/)
* [ParaView Wiki](http://paraview.org/Wiki/ParaView)
* [ParaView-tutoriaali](http://www.paraview.org/Wiki/The_ParaView_Tutorial)
* [Hae ParaView-käyttäjien postituslistalta](http://discourse.paraview.org)