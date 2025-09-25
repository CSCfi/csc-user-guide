---
tags:
  - Free
catalog:
  name: Trinity
  description: Transcriptome assembly tool
  description_fi: Transkriptomin kokoamistyökalu
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Trinity { #trinity }

Trinityä käytetään RNA-seq-aineistosta _de novo_ -rekonstruktioon (transkriptomien kokoamiseen). Trinity yhdistää kolme itsenäistä ohjelmamoduulia: **Inchworm**, **Chrysalis** ja **Butterfly**, joita ajetaan peräkkäin suurten RNA-seq-lukemamäärien käsittelemiseksi. Trinity jakaa sekvenssiaineiston lukuisiin erillisiin de Bruijn -graafeihin, joista kukin kuvaa tietyn geenin tai lokuksen transkriptionaalista monimutkaisuutta, ja käsittelee jokaisen graafin itsenäisesti tuottaakseen täyspitkät splicing-isoformit ja erotellakseen transkriptit.

CSC:n Trinity-moduuli sisältää myös TransDecoder- ja Trinotate-työkalut Trinity-ajon tulosten analysointiin.

[TOC]

## Lisenssi { #license }

Vapaa käyttää ja avoimen lähdekoodin ohjelmisto [Broad Institute -lisenssin](https://github.com/genome-vendor/trinity/blob/master/LICENSE) alaisena.

## Saatavilla { #available }

Puhti: 2.8.5, 2.11.0, 2.13.2, 2.14.0, 2.15.1

## Käyttö { #usage }

### Trinityn käyttö { #using-trinity }

Puhtissa Trinity otetaan käyttöön komennolla:

```bash
module load biokit
```

biokit-moduuli tuo käyttöön joukon yleisesti käytettyjä bioinformatiikan työkaluja, mukaan lukien Trinity 2.8.5. Jos haluat käyttää uudempaa versiota, esim. 2.13.2, suorita komento:

```bash
module load trinty/2.13.2
```

Trinityä tulisi käyttää [interaktiivisesti laskentasolmussa](../computing/running/interactive-usage.md) tai mieluiten eräajojärjestelmän kautta. Alla on esimerkkieräajon job-tiedosto Trinitylle.

```bash
#!/bin/bash 
#SBATCH --job-name=trinity
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=48:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=6
#SBATCH --mem=24000
#SBATCH --account=project_1234567

module load trinity/2.13.2

Trinity --seqType fq --max_memory 22G --left reads.left.fq --right \
reads.right.fq --SS_lib_type RF --CPU $SLURM_CPUS_PER_TASK \
--output trinity_run_out --grid_exec sbatch_commandlist
```

Yllä oleva eräajosk ripti varaa yhdeltä solmulta 6 laskentaydintä työtä varten. Esimerkkityön enimmäisaika on 48 tuntia. Muistia varataan noin 4 Gt jokaista ydintä kohden, joten kokonaismuistivaraus on `6 * 4 GB = 24 GB`. Puhtissa sinun on käytettävä eräajon valintaa `--account=` käytettävän projektin määrittämiseen. Korvaa esimerkissä käytetty `project_1234567` omalla projektillasi. Voit tarkistaa projektisi komennolla: `csc-projects`.

Varsinaisessa `Trinity`-komennossa käytettävien laskentaytimien määrä (`--CPU`) asetetaan ympäristömuuttujalla `$SLURM_CPUS_PER_TASK`. Tämä muuttuja sisältää arvon, joka on asetettu Slurmin `--cpus-per-task`-optiolla.

Puhtissa voit myös käyttää hajautettua laskentaa Trinity-työn nopeuttamiseksi. Kun komennolle lisätään määritys:

```bash
--grid_exec sbatch_commandlist
```

joitakin analyysin vaiheita ajetaan rinnakkaisina alitöinä. Suurissa Trinity-ajoissa `sbatch_commandlist`-työkalun asetukset ovat liian rajoittuneet. Näissä tapauksissa korvaa `sbatch_commandlist` työkalulla `sbatch_commandlist_trinity`.

```bash
--grid_exec sbatch_commandlist_trinity
```

Kun Trinity ajetaan `--grid_exec`-optiolla, se luo suuren määrän väliaikaistiedostoja, ja on hyvin todennäköistä, että ylität oletusrajan 100 000 tiedostoa. Siksi on suositeltavaa hakea suurempi tiedostomääräkiintiö Puhtin scratch-alueelle ennen suurten Trinity-töiden lähettämistä. Voit lähettää pyynnön [CSC Service Deskille](../support/contact.md).

Kun eräajon skripti on valmis, sen voi lähettää jonoon komennolla:

```bash
sbatch batch_job_file
```

Katso täältä [lisätietoja eräajojen suorittamisesta](../computing/running/getting-started.md).

Tutustu myös [Trinityn verkkosivuun](https://github.com/trinityrnaseq/trinityrnaseq/wiki) saadaksesi vinkkejä vaadittujen resurssien arviointiin.

### autoTrinotaten käyttö { #using-autotrinotate }

Voit analysoida Trinity-työsi tuloksia työkalulla `autoTrinotate`. Tarvitset kaksi tiedostoa, jotka syntyvät onnistuneesta Trinity-kokoamisesta.

1. Fasta-muotoinen nukleotidisekvenssitiedosto, joka sisältää Trinityn luomat lopulliset contigit (`Trinity.fasta`)
2. gene-to-trans -kartta syötteen fasta-tiedostolle (`Trinity.fasta.gene_to_trans_map`)

Huomaa, että Trinity-versiosta riippuen nimillä voi olla etuliite, joka on määritelty `--output`-optiolla (esim. `trinity_run_out.Trinity.fasta`).

Kopioi analyysiäsi varten mallipohjainen sqlite-tietokanta:

```bash
cp $TRINOTATE_HOME/databases/Trinotate.sqlite mydb.sqlite
```

Voit käynnistää `autoTrinotate`-ajon komennolla:

```bash
$TRINOTATE_HOME/auto/autoTrinotate.pl --Trinotate_sqlite mydb.sqlite --transcripts Trinity.fasta --gene_to_trans_map  Trinity.fasta.gene_to_trans_map --conf $TRINOTATE_HOME/auto/conf.txt --CPU  $SLURM_CPUS_PER_TASK
```

!!! warning "Huomio"
    autoTrinotate-analyysi voi vaatia runsaasti resursseja, joten suorita komento
    [interaktiivisessa istunnossa](../computing/running/interactive-usage.md) tai eräajona!

autoTrinotate tuottaa SQLite-tietokantatiedoston, jota voi analysoida edelleen komennolla:

```bash
$TRINOTATE_HOME/Trinotate
```

## Lisätietoja { #more-information }

- [Trinityn kotisivu](https://github.com/trinityrnaseq/trinityrnaseq/wiki)